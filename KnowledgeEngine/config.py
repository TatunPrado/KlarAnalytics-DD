"""
Knowledge Engine for Prisma Consulting — Klar Analytics product.

Defines paths, file patterns, stopwords, and dimension mappings
used by the scanner, parsers, and prompt builder.
"""

import os
from dataclasses import dataclass, field
from typing import List, Dict

# ─── Project root detection ───

def detect_project_root() -> str:
    """Detect the project root by looking for the Agents/ directory."""
    candidates = [
        os.getcwd(),
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.expanduser("~/ANALISTA DE PYMES"),
        "C:/Users/Prado/OneDrive/Desktop/JUAN MANUEL/CONSULTORAA/ANALISTA DE PYMES",
    ]
    for path in candidates:
        if os.path.isdir(os.path.join(path, "Agents")):
            return path
    raise FileNotFoundError("Cannot detect project root. Set KE_ROOT env var or pass base_path explicitly.")


# ─── Configuration ───

@dataclass
class KEConfig:
    """Central configuration for the knowledge engine."""

    base_path: str = field(default_factory=detect_project_root)

    # Directory paths (relative to base_path)
    agents_dir: str = "Agents"
    skills_dir: str = "Skills"
    knowledge_dir: str = "Knowledge"
    playbooks_dir: str = "Playbooks"
    operations_dir: str = "Operations"

    # File patterns for discovery
    agent_pattern: str = "**/*.md"
    skill_pattern: str = "**/*.md"
    framework_pattern: str = "**/Framework_*.md"
    pattern_pattern: str = "**/*_Patterns.md"
    playbook_pattern: str = "**/*.md"
    process_pattern: str = "**/*.md"

    # Dimension aliases (for query matching)
    dimension_aliases: Dict[str, List[str]] = field(default_factory=lambda: {
        "finanzas":         ["finanzas", "finance", "financial", "cashflow", "profitability", "financiero"],
        "estrategia":       ["estrategia", "strategy", "estrategico", "strategic", "competitive"],
        "operaciones":      ["operaciones", "operations", "operativo", "process", "operational"],
        "talento":          ["talento", "talent", "organizacion", "organization", "cultura", "culture", "people"],
        "riesgos":          ["riesgos", "risk", "riesgo", "compliance"],
        "modelo_negocio":   ["modelo", "business_model", "bmc", "negocio"],
        "cliente":          ["cliente", "customer", "mercado", "market", "jbtb", "ventas", "sales"],
        "marketing":        ["marketing", "publicidad", "brand"],
        "tecnologia":       ["tecnologia", "technology", "digital", "transformacion"],
    })

    # Stopwords for text indexing (spanish + english)
    stopwords: set = field(default_factory=lambda: {
        "de", "la", "el", "en", "del", "con", "para", "por", "y", "a", "los", "las",
        "un", "una", "que", "es", "se", "su", "lo", "como", "más", "pero", "sus",
        "le", "ya", "este", "entre", "porque", "cuando", "muy", "sin", "sobre",
        "the", "and", "for", "with", "from", "this", "that", "are", "was", "were",
        "puede", "debe", "cada", "todo", "tiene", "hace", "forma", "través",
    })

    # LLM defaults
    max_context_tokens: int = 8000
    max_agent_output_tokens: int = 2000
    default_model: str = "gpt-4o"

    # Cache
    cache_enabled: bool = True
    cache_ttl_seconds: int = 300  # 5 minutes


# ─── Global singleton ───

_config: KEConfig = None


def get_config() -> KEConfig:
    """Get the global configuration singleton."""
    global _config
    if _config is None:
        _config = KEConfig()
    return _config


def set_config(cfg: KEConfig) -> None:
    """Override the global configuration (useful for testing)."""
    global _config
    _config = cfg
