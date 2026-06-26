"""
Core engine — KnowledgeEngine for Prisma Consulting.

Orchestrates loading, indexing, context building, and prompt assembly.
Main entry point for all knowledge operations.
"""

import os
import re
import json
import time
from typing import List, Dict, Optional, Any
from concurrent.futures import ThreadPoolExecutor

from .config import get_config, KEConfig
from .knowledge_loader import KnowledgeLoader
from .prompt_builder import PromptBuilder


class KnowledgeEngine:
    """
    Central engine that loads, indexes, and queries the knowledge base.

    Usage:
        engine = KnowledgeEngine()
        engine.init()          # scan + load everything
        context = engine.build_context(dimensions=["finanzas"])
        prompt = engine.assemble_prompt(agent="Financial_Analyst", context=context, client_data=data)
    """

    def __init__(self, base_path: Optional[str] = None, config: Optional[KEConfig] = None):
        if config:
            from .config import set_config
            set_config(config)
        self.config = get_config()
        if base_path:
            self.config.base_path = base_path

        self.loader = KnowledgeLoader(self.config.base_path)
        self.prompt_builder = PromptBuilder()
        self._artifacts: Dict[str, List[Dict]] = {}
        self._index: Dict[str, List[Dict]] = {}    # keyword → matching artifacts
        self._dimension_index: Dict[str, List[Dict]] = {}  # dimension → matching artifacts
        self._initialized: bool = False
        self._last_load: float = 0.0

    # ─── Initialization ───

    def init(self, force: bool = False) -> "KnowledgeEngine":
        """Scan filesystem and load everything."""
        if self._initialized and not force:
            return self

        print(f"[KE] Loading knowledge from: {self.config.base_path}")
        self._artifacts = self.loader.load_everything()
        self._build_index()
        self._build_dimension_index()
        self._initialized = True
        self._last_load = time.time()

        summary = self.loader.summary()
        total = sum(summary.values())
        print(f"[KE] Loaded {total} artifacts: {summary}")
        return self

    def reload(self) -> "KnowledgeEngine":
        """Force reload from filesystem."""
        return self.init(force=True)

    # ─── Indexing ───

    def _build_index(self) -> None:
        """Build a keyword index over all loaded artifacts."""
        self._index = {}
        for category, items in self._artifacts.items():
            for item in items:
                text_pool = (
                    (item.get("title") or "") + " " +
                    (item.get("filename") or "") + " " +
                    " ".join(item.get("tags", []))
                ).lower()

                # Add section bodies for better search coverage
                for sect in item.get("sections", {}).values():
                    if isinstance(sect, dict):
                        text_pool += " " + sect.get("body", "")

                words = set(re.findall(r'\w+', text_pool))
                words -= self.config.stopwords
                for word in words:
                    if len(word) > 2:  # skip very short tokens
                        self._index.setdefault(word, []).append(item)

    def _build_dimension_index(self) -> None:
        """Map artifacts to business dimensions for targeted retrieval."""
        self._dimension_index = {}

        # Map each dimension alias to matching artifacts
        for dimension, aliases in self.config.dimension_aliases.items():
            matches = set()
            for alias in aliases:
                # Search in titles, filenames, and tags
                for category, items in self._artifacts.items():
                    for item in items:
                        text = (
                            (item.get("title") or "") + " " +
                            (item.get("filename") or "") + " " +
                            " ".join(item.get("tags", []))
                        ).lower()
                        if alias in text:
                            matches.add(id(item))

            self._dimension_index[dimension] = [
                self._find_by_id(rid) for rid in matches
                if self._find_by_id(rid) is not None
            ]

    def _find_by_id(self, obj_id: int) -> Optional[Dict]:
        for items in self._artifacts.values():
            for item in items:
                if id(item) == obj_id:
                    return item
        return None

    # ─── Query ───

    def search(self, query: str, top_k: int = 10) -> List[Dict]:
        """Simple keyword search across all artifacts."""
        words = set(re.findall(r'\w+', query.lower())) - self.config.stopwords
        scores: Dict[int, float] = {}
        results: Dict[int, Dict] = {}

        for word in words:
            for item in self._index.get(word, []):
                obj_id = id(item)
                scores[obj_id] = scores.get(obj_id, 0) + 1.0
                results[obj_id] = item

        # Sort by score
        ranked = sorted(results.values(), key=lambda x: scores[id(x)], reverse=True)
        return ranked[:top_k]

    def get_by_dimension(self, dimension: str) -> List[Dict]:
        """Get all artifacts related to a business dimension."""
        dimension = dimension.lower().strip()
        # Try exact match first
        if dimension in self._dimension_index:
            return self._dimension_index[dimension]

        # Try alias matching
        for dim, aliases in self.config.dimension_aliases.items():
            if dimension in aliases or dimension == dim:
                return self._dimension_index.get(dim, [])

        return []

    def get_by_filename(self, filename: str) -> Optional[Dict]:
        """Get a specific artifact by filename (with or without extension)."""
        key = filename.lower().replace(".md", "").strip()
        items = self._index.get(key, [])
        if items:
            return items[0]
        return None

    # ─── Context Building ───

    def build_context(
        self,
        dimensions: Optional[List[str]] = None,
        client_brief: Optional[Dict] = None,
        diagnosis_type: str = "integral",
        max_tokens: int = 6000,
    ) -> Dict[str, Any]:
        """
        Build a context dict for LLM consumption by selecting relevant artifacts.

        Args:
            dimensions: List of dimensions to diagnose (e.g. ["finanzas", "estrategia"])
            client_brief: Optional client information dict for relevance matching
            diagnosis_type: "express", "integral", or "premium"
            max_tokens: Maximum total tokens for the context

        Returns:
            Dict with keys: agents, skills, frameworks, patterns, playbooks, metadata
        """
        if not self._initialized:
            self.init()

        context = {
            "metadata": {
                "diagnosis_type": diagnosis_type,
                "dimensions": dimensions or [],
                "total_tokens": 0,
            },
            "agents": [],
            "skills": [],
            "frameworks": [],
            "patterns": [],
            "playbooks": [],
            "processes": [],
        }

        remaining = max_tokens

        # 1. Select agents relevant to requested dimensions
        if dimensions:
            selected = set()
            for dim in dimensions:
                for artifact in self.get_by_dimension(dim):
                    if artifact.get("doc_type") == "agent":
                        selected.add(id(artifact))
            context["agents"] = [self._find_by_id(s) for s in selected if self._find_by_id(s)]
        else:
            context["agents"] = self._artifacts.get("agents", [])

        remaining -= sum(a.get("tokens", 0) for a in context["agents"])

        # 2. Select skills referenced by chosen agents (deduplicated)
        def _normalize(name: str) -> str:
            return name.lower().replace("_", "-").replace(" ", "-").strip()

        referenced_skills = {}
        for agent in context["agents"]:
            for skill_name in agent.get("skills", []):
                norm_skill = _normalize(skill_name)
                for s in self._artifacts.get("skills", []):
                    if norm_skill in _normalize(s.get("filename", "")):
                        referenced_skills[id(s)] = s
        context["skills"] = list(referenced_skills.values())

        # 3. Select frameworks and patterns by dimension (deduplicated)
        if dimensions:
            selected_fw = {}
            selected_pt = {}
            for dim in dimensions:
                for artifact in self.get_by_dimension(dim):
                    if artifact.get("doc_type") == "framework":
                        selected_fw[id(artifact)] = artifact
                    elif artifact.get("doc_type") == "pattern":
                        selected_pt[id(artifact)] = artifact
            context["frameworks"] = list(selected_fw.values())
            context["patterns"] = list(selected_pt.values())
        else:
            context["frameworks"] = self._artifacts.get("frameworks", [])
            context["patterns"] = self._artifacts.get("patterns", [])

        # 4. Select playbook if relevant
        if diagnosis_type:
            for pb in self._artifacts.get("playbooks", []):
                title = (pb.get("title") or "").lower()
                if "diagnosis" in title or "diagnóstico" in title:
                    context["playbooks"] = [pb]
                    break

        # 5. Select relevant processes (deduplicated)
        if dimensions:
            selected_proc = {}
            for dim in dimensions:
                aliases = self.config.dimension_aliases.get(dim, [dim])
                for proc in self._artifacts.get("processes", []):
                    text = ((proc.get("title") or "") + " " + (proc.get("filename") or "")).lower()
                    if any(a in text for a in aliases):
                        selected_proc[id(proc)] = proc
            context["processes"] = list(selected_proc.values())

        # Calculate total tokens
        context["metadata"]["total_tokens"] = sum(
            a.get("tokens", 0) for category in ["agents", "skills", "frameworks", "patterns", "playbooks", "processes"]
            for a in context.get(category, [])
        )

        return context

    # ─── Prompt Assembly ───

    def assemble_prompt(
        self,
        agent_name: str,
        client_data: Dict,
        context: Optional[Dict] = None,
        dimensions: Optional[List[str]] = None,
    ) -> Dict[str, str]:
        """
        Assemble a complete prompt for a specific agent.

        Returns dict with keys: system, user, context_raw
        """
        if context is None:
            context = self.build_context(dimensions=dimensions or [])

        agent_def = None
        for a in context.get("agents", []):
            if agent_name.lower() in (a.get("filename") or "").lower():
                agent_def = a
                break

        if agent_def is None:
            for a in self._artifacts.get("agents", []):
                if agent_name.lower() in (a.get("filename") or "").lower():
                    agent_def = a
                    break

        return self.prompt_builder.build(
            agent=agent_def,
            client_data=client_data,
            context=context,
        )

    # ─── Utilities ───

    def summary(self) -> Dict[str, Any]:
        """Return a complete summary of the engine state."""
        return {
            "initialized": self._initialized,
            "base_path": self.config.base_path,
            "artifacts": self.loader.summary() if self._initialized else {},
            "index_terms": len(self._index) if self._initialized else 0,
            "dimensions": list(self.config.dimension_aliases.keys()),
            "last_load": self._last_load,
        }

    def export_index(self, filepath: str) -> None:
        """Export the full index as JSON for external tools."""
        data = {
            "metadata": self.summary(),
            "artifacts": self._artifacts,
            "dimension_index": {
                k: [a.get("filename") for a in v]
                for k, v in self._dimension_index.items()
            },
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[KE] Index exported to: {filepath}")
