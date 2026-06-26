"""
Knowledge Loader — filesystem scanner for Prisma Consulting knowledge base.

Discovers, reads, and parses all knowledge artifacts from the project filesystem.
Returns structured dicts ready for indexing and prompt assembly.
"""

import os
import glob
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import get_config
from .parsers import parse_file, detect_type


class KnowledgeLoader:
    """Scans the filesystem and loads all knowledge artifacts."""

    def __init__(self, base_path: Optional[str] = None):
        self.config = get_config()
        if base_path:
            self.config.base_path = base_path
        self._artifacts: Dict[str, List[Dict]] = {}
        self._loaded: bool = False

    # ─── Path resolvers ───

    def _abs(self, rel_path: str) -> str:
        return os.path.join(self.config.base_path, rel_path)

    def _discover_files(self, directory: str, pattern: str) -> List[str]:
        """Glob for files in a directory matching a pattern."""
        search_path = os.path.join(self._abs(directory), pattern)
        return [f for f in glob.glob(search_path, recursive=True) if os.path.isfile(f)]

    # ─── Load by type ───

    def load_agents(self) -> List[Dict]:
        files = self._discover_files(self.config.agents_dir, self.config.agent_pattern)
        return self._load_all(files)

    def load_skills(self) -> List[Dict]:
        files = self._discover_files(self.config.skills_dir, self.config.skill_pattern)
        return self._load_all(files)

    def load_frameworks(self) -> List[Dict]:
        files = self._discover_files(self.config.knowledge_dir, self.config.framework_pattern)
        return self._load_all(files)

    def load_patterns(self) -> List[Dict]:
        files = self._discover_files(self.config.knowledge_dir, self.config.pattern_pattern)
        return self._load_all(files)

    def load_playbooks(self) -> List[Dict]:
        files = self._discover_files(self.config.playbooks_dir, self.config.playbook_pattern)
        return self._load_all(files)

    def load_processes(self) -> List[Dict]:
        files = self._discover_files(self.config.operations_dir, self.config.process_pattern)
        return self._load_all(files)

    def load_all_knowledge(self) -> List[Dict]:
        """Load all Knowledge/ files (frameworks + patterns + misc)."""
        files = self._discover_files(self.config.knowledge_dir, "**/*.md")
        return self._load_all(files)

    # ─── Bulk load ───

    def load_everything(self) -> Dict[str, List[Dict]]:
        """Load all artifacts from the entire project."""
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {
                "agents": pool.submit(self.load_agents),
                "skills": pool.submit(self.load_skills),
                "frameworks": pool.submit(self.load_frameworks),
                "patterns": pool.submit(self.load_patterns),
                "playbooks": pool.submit(self.load_playbooks),
                "processes": pool.submit(self.load_processes),
                "knowledge": pool.submit(self.load_all_knowledge),
            }
            for key, future in futures.items():
                self._artifacts[key] = future.result()

        # Deduplicate artifacts by filepath across all categories
        # (files under Knowledge/ can appear in both frameworks/patterns and knowledge)
        seen_paths: Dict[str, Dict] = {}
        for category in list(self._artifacts.keys()):
            deduped = []
            for item in self._artifacts[category]:
                fp = item.get("filepath", "")
                if fp not in seen_paths:
                    seen_paths[fp] = item
                    deduped.append(item)
                else:
                    # Merge tags from duplicates
                    existing_tags = set(seen_paths[fp].get("tags", []))
                    existing_tags.update(item.get("tags", []))
                    seen_paths[fp]["tags"] = list(existing_tags)
            self._artifacts[category] = deduped

        self._loaded = True
        return self._artifacts

    # ─── Internal ───

    def _read_file(self, filepath: str) -> Optional[str]:
        """Read a file with encoding fallback."""
        for encoding in ["utf-8", "latin-1", "cp1252"]:
            try:
                with open(filepath, "r", encoding=encoding) as f:
                    return f.read()
            except (UnicodeDecodeError, IOError):
                continue
        return None

    def _load_single(self, filepath: str) -> Optional[Dict]:
        text = self._read_file(filepath)
        if text is None:
            return None
        try:
            return parse_file(text, filepath)
        except Exception as e:
            return {
                "type": "error",
                "filepath": filepath,
                "error": str(e),
                "tokens": 0,
            }

    def _load_all(self, files: List[str]) -> List[Dict]:
        results = []
        with ThreadPoolExecutor(max_workers=16) as pool:
            futures = {pool.submit(self._load_single, f): f for f in files}
            for future in as_completed(futures):
                result = future.result()
                if result:
                    results.append(result)
        return results

    # ─── Accessors ───

    @property
    def agents(self) -> List[Dict]:
        return self._artifacts.get("agents", [])

    @property
    def skills(self) -> List[Dict]:
        return self._artifacts.get("skills", [])

    @property
    def frameworks(self) -> List[Dict]:
        return self._artifacts.get("frameworks", [])

    @property
    def patterns(self) -> List[Dict]:
        return self._artifacts.get("patterns", [])

    @property
    def playbooks(self) -> List[Dict]:
        return self._artifacts.get("playbooks", [])

    @property
    def processes(self) -> List[Dict]:
        return self._artifacts.get("processes", [])

    @property
    def knowledge(self) -> List[Dict]:
        return self._artifacts.get("knowledge", [])

    def summary(self) -> Dict[str, int]:
        """Return a summary of loaded artifacts."""
        return {
            k: len(v) for k, v in self._artifacts.items()
        } if self._loaded else {"status": "not loaded"}
