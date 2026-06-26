"""
Prompt Builder — dynamic prompt assembly for Prisma Consulting agents.

Assembles LLM prompts from parsed knowledge artifacts, avoiding hardcoded prompts.
Produces structured prompts with system role definition, knowledge context,
instructions extracted from skills, and client data.
"""

from typing import List, Dict, Optional, Any


SYSTEM_TEMPLATE = """Eres {agent_name}, un agente especializado en {agent_role} de Prisma Consulting.

{agent_objective}

{agent_responsibilities}

{agent_frameworks_context}

{agent_skills_context}
"""

USER_TEMPLATE = """## INFORMACIÓN DEL CLIENTE

{client_data}

## DIMENSIONES A DIAGNOSTICAR

{dimensions_context}

## INSTRUCCIONES ESPECÍFICAS

{instructions}

## FORMATO DE SALIDA ESPERADO

{output_format}

Por favor, genera tu análisis siguiendo la estructura indicada.
"""


class PromptBuilder:
    """Assembles dynamic prompts from parsed knowledge artifacts."""

    def build(
        self,
        agent: Optional[Dict],
        client_data: Dict,
        context: Dict[str, Any],
    ) -> Dict[str, str]:
        """
        Build a complete prompt.

        Returns:
            dict with keys:
                - system: system prompt (agent role + knowledge context)
                - user: user prompt (client data + instructions)
                - context_raw: all knowledge used (for logging/debugging)
        """
        system = self._build_system(agent, context)
        user = self._build_user(client_data, context)
        context_raw = self._serialize_context(context)

        return {
            "system": system,
            "user": user,
            "context_raw": context_raw,
        }

    def _build_system(self, agent: Optional[Dict], context: Dict) -> str:
        if agent is None:
            return self._generic_system(context)

        sections = agent.get("sections", {})
        agent_name = agent.get("filename", "Analyst")
        agent_role = agent.get("title", "Analista")

        # Extract from parsed sections
        rol_text = self._section_body(sections, "Rol")
        objetivo_text = self._section_body(sections, "Objetivo")
        responsabilidades_text = self._section_body(sections, "Responsabilidades")
        no_analizar_text = self._section_body(sections, "No analizar", "No analizarás")
        salida_text = self._section_body(sections, "Salida")

        # Frameworks context
        frameworks_context = ""
        if agent.get("frameworks"):
            frameworks_context = "Frameworks que debes utilizar:\n"
            for fw_name in agent["frameworks"]:
                fw_detail = self._find_framework_detail(fw_name, context)
                frameworks_context += f"- {fw_detail}\n"

        # Skills context
        skills_context = ""
        if agent.get("skills"):
            skills_context = "Habilidades que debes aplicar:\n"
            for sk_name in agent["skills"]:
                sk_detail = self._find_skill_detail(sk_name, context)
                skills_context += f"- {sk_detail}\n"

        return SYSTEM_TEMPLATE.format(
            agent_name=agent_name,
            agent_role=rol_text or agent_role,
            agent_objective=objetivo_text or "",
            agent_responsibilities=responsabilidades_text or "",
            agent_frameworks_context=frameworks_context,
            agent_skills_context=skills_context,
        )

    def _build_user(self, client_data: Dict, context: Dict) -> str:
        # Serialize client data
        client_str = "\n".join(f"- {k}: {v}" for k, v in client_data.items())

        # Dimensions context
        dimensions = context.get("metadata", {}).get("dimensions", [])
        dim_context = ""
        if dimensions:
            dim_context = "Dimensiones solicitadas: " + ", ".join(dimensions)

        # Instructions from playbooks
        instructions = self._extract_instructions(context)

        # Output format from agent definition or defaults
        output_format = self._extract_output_format(context)

        return USER_TEMPLATE.format(
            client_data=client_str,
            dimensions_context=dim_context,
            instructions=instructions or "Realiza un análisis completo de la dimensión asignada.",
            output_format=output_format or "Informe estructurado con hallazgos, evidencia y recomendaciones.",
        )

    def _generic_system(self, context: Dict) -> str:
        return """Eres un analista de Prisma Consulting, consultora especializada en diagnóstico empresarial para PyMEs.

Debes analizar la información del cliente utilizando los frameworks y patrones disponibles en la base de conocimiento.

Objetivo: Identificar hallazgos, priorizar problemas y recomendar acciones concretas.

No implementas soluciones. Diagnosticas, analizas y recomiendas con objetividad total."""

    # ─── Helpers ───

    def _section_body(self, sections: Dict, *keys) -> str:
        for key in keys:
            if key in sections:
                return sections[key].get("body", "")
        return ""

    def _find_framework_detail(self, fw_name: str, context: Dict) -> str:
        clean_name = fw_name.strip().replace("framework-", "").replace("_", "-").replace(" ", "-").lower()
        for fw in context.get("frameworks", []):
            fw_filename = (fw.get("filename") or "").lower().replace("_", "-").replace("framework-", "")
            if clean_name in fw_filename or fw_filename in clean_name:
                return fw.get("title", fw_name)
        return fw_name

    def _find_skill_detail(self, sk_name: str, context: Dict) -> str:
        clean_name = sk_name.strip().replace("_", "-").replace(" ", "-").lower()
        for sk in context.get("skills", []):
            sk_filename = (sk.get("filename") or "").lower().replace("_", "-")
            if clean_name in sk_filename or sk_filename in clean_name:
                title = sk.get("title", "")
                return title if title else sk_name
        # Try to find a matching framework for the skill
        for fw in context.get("frameworks", []):
            fw_filename = (fw.get("filename") or "").lower().replace("_", "-")
            if clean_name in fw_filename:
                return fw.get("title", sk_name)
        return sk_name.title().replace("-", " ")

    def _extract_instructions(self, context: Dict) -> str:
        instructions = []
        # Extract steps from relevant playbooks
        for pb in context.get("playbooks", []):
            pb_title = pb.get("title", "")
            sections = pb.get("sections", {})
            for heading, section in sections.items():
                if "procedimiento" in heading.lower() or "instrucciones" in heading.lower():
                    steps = section.get("ordered_items", [])
                    for step in steps:
                        instructions.append(f"- {step}")
                bullets = section.get("bullets", [])
                for b in bullets:
                    if len(instructions) < 15:
                        instructions.append(f"- {b}")

        # Extract from skills in context
        for sk in context.get("skills", []):
            sections = sk.get("sections", {})
            for heading, section in sections.items():
                if "procedimiento" in heading.lower():
                    steps = section.get("ordered_items", [])
                    for step in steps:
                        instructions.append(f"- {step}")

        return "\n".join(instructions[:20]) if instructions else ""

    def _extract_output_format(self, context: Dict) -> str:
        for agent in context.get("agents", []):
            sections = agent.get("sections", {})
            for heading, section in sections.items():
                if "salida" in heading.lower() or "output" in heading.lower():
                    return section.get("body", "")
        return ""

    def _serialize_context(self, context: Dict) -> Dict:
        """Serialize context for logging/debugging."""
        return {
            "agents": [a.get("filename") for a in context.get("agents", [])],
            "skills": [s.get("filename") for s in context.get("skills", [])],
            "frameworks": [f.get("filename") for f in context.get("frameworks", [])],
            "patterns_count": sum(
                len(p.get("patterns", [])) for p in context.get("patterns", [])
            ),
            "playbooks": [p.get("filename") for p in context.get("playbooks", [])],
            "processes": [p.get("filename") for p in context.get("processes", [])],
            "metadata": context.get("metadata", {}),
        }
