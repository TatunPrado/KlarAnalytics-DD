"""
Knowledge Engine for Prisma Consulting — Klar Analytics.

Motor de carga dinámica de conocimiento que lee Agents, Skills, Frameworks,
Knowledge y Playbooks directamente desde el filesystem, eliminando la
necesidad de hardcodear prompts dentro del código.

Usage:
    from KnowledgeEngine import KnowledgeEngine
    
    engine = KnowledgeEngine()
    engine.init()
    
    # Build context for a diagnosis
    ctx = engine.build_context(dimensions=["finanzas", "operaciones"])
    
    # Assemble prompt for a specific agent
    prompt = engine.assemble_prompt(
        agent_name="Financial_Analyst",
        client_data={"company": "Cliente S.A.", "industry": "retail"},
        context=ctx,
    )
    
    # Send to LLM
    response = llm.chat(prompt["system"], prompt["user"])
"""

from .core import KnowledgeEngine
from .config import KEConfig, get_config, set_config
from .knowledge_loader import KnowledgeLoader
from .prompt_builder import PromptBuilder
from .parsers import (
    parse_file,
    parse_agent,
    parse_skill,
    parse_framework,
    parse_pattern,
    parse_playbook,
    detect_type,
    PARSER_REGISTRY,
)

__version__ = "1.0.0"
__all__ = [
    "KnowledgeEngine",
    "KEConfig",
    "get_config",
    "set_config",
    "KnowledgeLoader",
    "PromptBuilder",
    "parse_file",
    "parse_agent",
    "parse_skill",
    "parse_framework",
    "parse_pattern",
    "parse_playbook",
    "detect_type",
    "PARSER_REGISTRY",
]
