import sys, os, json, time
from pathlib import Path

import streamlit as st
ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))

from KnowledgeEngine import KnowledgeEngine

# ─── API Key config ───
CONFIG_DIR = Path.home() / ".klaranalytics"
CONFIG_FILE = CONFIG_DIR / "config.json"


def _load_api_key() -> str:
    # Cloud: check Streamlit secrets first
    try:
        key = st.secrets.get("gemini_api_key", "")
        if len(key) > 10:
            return key
    except (Exception,):
        pass
    # Local: check config file
    if CONFIG_FILE.exists():
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            key = data.get("gemini_api_key", "")
            if len(key) > 10:
                return key
        except (json.JSONDecodeError, OSError):
            pass
    return ""


def _save_api_key(key: str):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(
        json.dumps({"gemini_api_key": key}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

BLUE_800 = "#0f172a"
BLUE_700 = "#1e40af"
BLUE_500 = "#2563eb"
BLUE_200 = "#bfdbfe"
BLUE_100 = "#eff6ff"
TEAL_500 = "#10b981"
GRAY_50  = "#f8fafc"
GRAY_400 = "#94a3b8"
GRAY_600 = "#475569"
GRAY_800 = "#0f172a"

DOMINIOS_DD = [
    ("legal", "Informaci\u00f3n Legal"),
    ("tributario", "Situaci\u00f3n Tributaria"),
    ("financiero", "Situaci\u00f3n Financiera"),
    ("compliance", "Compliance & AML"),
    ("reputacional", "Reputaci\u00f3n & OSINT"),
    ("contrataciones", "Contrataciones & Propiedad Intelectual"),
]

DIMENSIONES = {
    "finanzas":       "Finanzas",
    "estrategia":     "Estrategia",
    "operaciones":    "Operaciones",
    "talento":        "Talento y Organizaci\u00f3n",
    "riesgos":        "Riesgos",
    "modelo_negocio": "Modelo de Negocio",
    "cliente":        "Cliente y Mercado",
    "marketing":      "Marketing",
    "tecnologia":     "Tecnolog\u00eda",
}

CSS = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}
    .stApp {{ background-color: {GRAY_50}; }}
    .main .block-container {{ padding-top: 2rem; }}
    h1, h2, h3 {{ color: {BLUE_800} !important; font-weight: 600 !important; }}
    .stButton button {{ background: linear-gradient(135deg, {BLUE_500}, #3b82f6); color: white; border-radius: 8px; padding: 0.5rem 2rem; font-weight: 500; border: none; box-shadow: 0 4px 14px rgba(37,99,235,0.2); }}
    .stButton button:hover {{ background: linear-gradient(135deg, {BLUE_700}, {BLUE_500}); transform: translateY(-1px); box-shadow: 0 6px 20px rgba(37,99,235,0.3); }}
    .card {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 1rem; }}
    .kpi-box {{ background: white; border-radius: 12px; padding: 1rem 1.5rem; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04); border-top: 3px solid {BLUE_500}; }}
    .kpi-number {{ font-size: 2rem; font-weight: 700; color: {BLUE_800}; }}
    .kpi-label {{ font-size: 0.8rem; color: {GRAY_400}; text-transform: uppercase; letter-spacing: 0.05em; }}
    .stChatFocused {{ border-color: {BLUE_500} !important; }}
    footer {{ display: none; }}
    .phase-badge {{ display: inline-block; padding: 0.2rem 0.8rem; border-radius: 20px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
    .phase-dd {{ background: #FEF3C7; color: #92400E; }}
    .phase-dx {{ background: #DBEAFE; color: #1E40AF; }}
    .phase-done {{ background: #D1FAE5; color: #065F46; }}
    .report-section {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 1.5rem; border-left: 4px solid {BLUE_500}; }}
</style>
"""



@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng

def _find_in_list(items, name_key):
    name_key = name_key.lower().replace("_", "-").replace(" ", "-")
    for item in items:
        fname = (item.get("filename") or "").lower().replace("_", "-").replace(" ", "-")
        title = (item.get("title") or "").lower().replace("_", "-").replace(" ", "-")
        if name_key in fname or name_key in title:
            return item
    return None

def _extract_body(item, limit=600):
    for key in ("descripci\u00f3n", "description", "descripcion", "summary", "objetivo"):
        body = item.get("sections", {}).get(key, {}).get("body", "")
        if body:
            return body[:limit]
    return (item.get("description") or "")[:limit]

def _build_knowledge_section(context, dims):
    parts = ["=== BASE DE CONOCIMIENTO ==="]
    AGENTES_POR_DIMENSION = {
        "finanzas":       ["Financial_Analyst"],
        "estrategia":     ["Strategy_Designer"],
        "operaciones":    ["Operations_Analyst"],
        "talento":        ["Organization_Analyst"],
        "riesgos":        ["Risk_Analyst", "due-diligence-officer"],
        "modelo_negocio": ["Business_Model_Analyst"],
        "cliente":        ["Business_Diagnosis_Assistant"],
        "marketing":      ["Business_Diagnosis_Assistant"],
        "tecnologia":     ["AI_Transformation_Designer"],
    }
    for d in dims:
        label = DIMENSIONES.get(d, d)
        agent_names = AGENTES_POR_DIMENSION.get(d, [])
        parts.append(f"\n--- {label} ---")
        for agent_name in agent_names:
            agent_def = _find_in_list(context.get("agents", []), agent_name)
            if agent_def:
                desc = agent_def.get("description", "")
                if desc:
                    parts.append(desc)
                for sn in agent_def.get("skills", []):
                    skill = _find_in_list(context.get("skills", []), sn)
                    if skill:
                        parts.append(f"\nMetodolog\u00eda: {skill.get('title', '')}")
                        sd = skill.get("description", "")
                        if sd:
                            parts.append(sd[:400])
                        for sn2, sdata in skill.get("sections", {}).items():
                            body = sdata.get("body", "") if isinstance(sdata, dict) else ""
                            if body and len(body) > 80:
                                parts.append(f"  {body[:400]}")
        for fw in context.get("frameworks", []):
            text = ((fw.get("title") or "") + " " + (fw.get("filename") or "") + " " + " ".join(fw.get("tags", []))).lower()
            if d in text or any(a in text for a in [d]):
                parts.append(f"\nMarco: {fw.get('title', '')}")
                body = _extract_body(fw, 500)
                if body:
                    parts.append(body)
        rel_pats = [p for p in context.get("patterns", []) if d in ((p.get("title") or "") + " " + (p.get("filename") or "")).lower()]
        if rel_pats:
            parts.append(f"\nPatrones ({len(rel_pats)} disponibles):")
            for p in rel_pats[:5]:
                pd = p.get("description", "")[:150]
                if pd:
                    parts.append(f"  \u00b7 {p.get('title', '') or p.get('filename', '')}: {pd}")
        for proc in context.get("processes", []):
            proc_text = ((proc.get("title") or "") + " " + (proc.get("filename") or "")).lower()
            if d in proc_text:
                parts.append(f"Proceso: {proc.get('title', '')}")
    for pb in context.get("playbooks", []):
        parts.append(f"\nPlaybook: {pb.get('title', '')}")
        desc = pb.get("description", "")[:300]
        if desc:
            parts.append(desc)
    return "\n".join(parts)

def _build_agent_prompt_block(agent, context, max_skills=6):
    parts = []
    desc = agent.get("description", "")
    if desc:
        parts.append(desc)
    sections = agent.get("sections", {})
    for h_key in ("PRINCIPIOS FUNDAMENTALES", "DOMINIOS DE INVESTIGACI\u00d3N", "MATRIZ DE RIESGO", "REGLAS OBLIGATORIAS", "GENERACI\u00d3N DE INFORMES", "ENTREGABLES"):
        if h_key in sections:
            sbody = sections[h_key].get("body", "")
            if sbody:
                parts.append(f"\n=== {h_key} ===\n{sbody}")
    sk_list = agent.get("skills", [])
    if sk_list:
        parts.append("\n=== HABILIDADES DISPONIBLES ===")
        for sn in sk_list[:max_skills]:
            skill = _find_in_list(context.get("skills", []), sn)
            if skill:
                title = skill.get("title", sn)
                sdesc = skill.get("description", "")
                if sdesc:
                    parts.append(f"- {title}: {sdesc[:300]}")
                else:
                    parts.append(f"- {title}")
                for h_key in ("FUENTES OFICIALES", "COBERTURA", "TAREAS", "SALIDA", "REGLAS"):
                    if h_key in skill.get("sections", {}):
                        sbody = skill["sections"][h_key].get("body", "")
                        if sbody and len(sbody) > 50:
                            parts.append(f"  {h_key}: {sbody[:400]}")
    return "\n".join(parts)

def _build_agent_skills_section(dd_agent, ctx):
    parts = []
    for sn in dd_agent.get("skills", []):
        skill = _find_in_list(ctx.get("skills", []), sn)
        if skill:
            title = skill.get("title", sn)
            sdesc = skill.get("description", "")
            if sdesc:
                parts.append(f"- **{title}**: {sdesc[:300]}")
            else:
                parts.append(f"- **{title}**")
            for h_key in ("FUENTES OFICIALES", "COBERTURA", "TAREAS", "PROCEDIMIENTO", "SALIDA", "REGLAS"):
                if h_key in skill.get("sections", {}):
                    sbody = skill["sections"][h_key].get("body", "")
                    if sbody and len(sbody) > 50:
                        parts.append(f"  _{h_key}_: {sbody[:300]}")
    return "\n".join(parts)

def build_dd_system_prompt(engine, company, cuit):
    ctx = engine.build_context(dimensions=["riesgos"])
    dd_agent = _find_in_list(ctx.get("agents", []), "due-diligence-officer")
    agent_block = _build_agent_prompt_block(dd_agent, ctx) if dd_agent else ""

    return f"""Sos un Oficial Senior de Due Diligence, Compliance e Inteligencia Corporativa de Prisma Consulting.

Est\u00e1s investigando a: {company} (CUIT: {cuit})

{agent_block}

INSTRUCCIONES ESPEC\u00cdFICAS:
- Presentate como Oficial de Due Diligence de Prisma Consulting.
- Hac\u00e9 UNA pregunta por vez. No bombardees.
- Us\u00e1 tono profesional pero cercano, en espa\u00f1ol.
- Cubr\u00ed TODOS los dominios de investigaci\u00f3n. Avanz\u00e1 al siguiente despu\u00e9s de 3-4 intercambios.
- Si el cliente no sabe un dato, anotalo como "No disponible" y segu\u00ed.
- Identific\u00e1 se\u00f1ales de alerta (red flags) cuando aparezcan.
- Despu\u00e9s de cubrir todos los dominios, ofrec\u00e9 generar el Informe de Due Diligence.
"""

def build_dd_auto_prompt(engine, company, cuit, datasource_text=""):
    ctx = engine.build_context(dimensions=["riesgos"])
    dd_agent = _find_in_list(ctx.get("agents", []), "due-diligence-officer")
    agent_block = _build_agent_prompt_block(dd_agent, ctx) if dd_agent else ""
    from datetime import date as _dt
    fecha = _dt.today().strftime("%d/%m/%Y")
    
    datasource_section = ""
    if datasource_text:
        datasource_section = f"""DATOS OFICIALES OBTENIDOS DE FUENTES EN TIEMPO REAL:
Los siguientes datos fueron obtenidos autom\u00e1ticamente desde las APIs oficiales del BCRA.
DEB\u00c9S usar estos datos en tu an\u00e1lisis, especialmente en las secciones de situaci\u00f3n financiera y crediticia.

{datasource_text}

"""
    
    return f"""Sos un Oficial Senior de Due Diligence, Compliance e Inteligencia Corporativa de Prisma Consulting.

Est\u00e1s realizando un DUE DILIGENCE AUTOM\u00c1TICO sobre: {company} (CUIT: {cuit})

{agent_block}

{datasource_section}INSTRUCCIONES ESPEC\u00cdFICAS:
- Gener\u00e1 un INFORME DE DUE DILIGENCE completo y estructurado sin hacerle preguntas al usuario.
- Bas\u00e1 tu an\u00e1lisis en los DATOS OFICIALES provistos arriba (si hay), el nombre de la empresa, el CUIT, y tu conocimiento general.
- Para cada factor de riesgo, asign\u00e1 un SCORE NUM\u00c9RICO 0-100 y un NIVEL (Bajo / Bajo-Medio / Medio / Alto / Cr\u00edtico) seg\u00fan la escala y los pesos definidos abajo.
- Marc\u00e1 cada hallazgo con: \u2705 [INFO CONFIRMADA] si se obtuvo de fuente oficial, \u2705 [INFO P\u00daBLICA] si pod\u00e9s determinarlo del nombre/CUIT, \u26a0\ufe0f [ESTIMADO] si es inferencia razonable, \U0001f50d [VERIFICAR] si requiere consultar fuente externa.
- Inclu\u00ed al inicio una secci\u00f3n "RESUMEN DE HALLAZGOS" con 5-7 vi\u00f1etas de los puntos cr\u00edticos.

== SISTEMA DE SCORING ==

### Escala de Riesgo
| Nivel | Rango | Color | Descripci\u00f3n |
|-------|-------|-------|-------------|
| Bajo | 0\u201320 | Verde | Sin hallazgos relevantes |
| Bajo-Medio | 21\u201340 | Verde claro | Hallazgos menores, controlables |
| Medio | 41\u201360 | Amarillo | Hallazgos que requieren monitoreo |
| Alto | 61\u201380 | Rojo | Hallazgos graves, requieren acci\u00f3n |
| Cr\u00edtico | 81\u2013100 | Rojo oscuro | Hallazgos que impiden continuar |

### Factores de Riesgo (7 dimensiones)

**1. Financiero (Peso: 20%)**
- Clasificaci\u00f3n BCRA (1\u20136): 6\u219280, 5\u219265, 4\u219250, 3\u219235, 2\u219220, 1\u219210
- Cheques rechazados: frecuencia + monto
- Relaci\u00f3n deuda/patrimonio: >2\u219270, 1-2\u219250, <1\u219220
- Resultado del ejercicio: P\u00e9rdida\u219270, equilibrio\u219240, super\u00e1vit\u219210
- Sanciones cambiarias: S\u00ed\u219280, No\u21920

**2. Tributario (Peso: 15%)**
- Estado ARCA: Inactivo\u2192100
- Deudas fiscales p\u00fablicas: existencia\u219260+
- Embargos fiscales: S\u00ed\u219280
- Categor\u00eda (Monotributo vs RI)
- IIBB / Convenio Multilateral: incumplimiento\u219270

**3. Legal (Peso: 20%)**
- Causas judiciales activas: cantidad + gravedad
- Embargos / inhibiciones: S\u00ed\u219270+
- Sumarios administrativos
- Condenas previas: S\u00ed\u219290

**4. AML / Sanciones (Peso: 20%)**
- Coincidencia OFAC/ONU/UE: directa\u2192100
- Posible coincidencia fon\u00e9tica: 40
- PEP (Persona Pol\u00edticamente Expuesta): S\u00ed\u219250
- Estructura societaria compleja sin justificaci\u00f3n: 60
- Jurisdicci\u00f3n no cooperante: 50

**5. Reputacional (Peso: 10%)**
- Noticias negativas graves: cantidad + gravedad
- Controversias p\u00fablicas: S\u00ed\u219260+
- Antig\u00fcedad positiva (+5 a\u00f1os sin incidentes): -20 puntos

**6. Operativo (Peso: 5%)**
- Dependencia de un solo cliente/proveedor: >50%\u219265
- Concentraci\u00f3n geogr\u00e1fica: una sola locaci\u00f3n\u219240
- Antig\u00fcedad: <1 a\u00f1o\u219260
- Cantidad de empleados: <5\u219240

**7. Compliance / Integridad (Peso: 10%)**
- PEP o v\u00ednculos con PEP: S\u00ed\u219260+
- Contrataciones con el Estado sin control: monto elevado\u219260
- Inhabilitaciones para contratar: S\u00ed\u219280
- Causas de corrupci\u00f3n / soborno: S\u00ed\u219290

### C\u00e1lculo del Riesgo General
RGeneral = (Financiero x 0.20) + (Tributario x 0.15) + (Legal x 0.20) + (AML x 0.20) + (Reputacional x 0.10) + (Operativo x 0.05) + (Compliance x 0.10)

### Matriz Impacto vs Probabilidad
```
                IMPACTO
            Bajo  Medio  Alto  Cr\u00edtico
Prob Alto   Medio  Alto  Cr\u00edt  Cr\u00edt
Prob Medio  Bajo   Medio  Alto  Cr\u00edt
Prob Bajo   Bajo   Bajo   Medio  Alto
```

### Recomendaci\u00f3n Final
- 0\u201325: APROBAR
- 26\u201350: APROBAR CON MITIGACIONES
- 51\u201375: RECHAZAR (requiere revisi\u00f3n de Compliance)
- 76\u2013100: RECHAZAR

== ESTRUCTURA DEL INFORME ==

# Informe de Due Diligence Autom\u00e1tico \u2014 {company}

## Resumen de Hallazgos
[5-7 vi\u00f1etas con hallazgos cr\u00edticos]

## Resumen Ejecutivo
Descripci\u00f3n del perfil de riesgo general, score general, nivel y recomendaci\u00f3n.

## Ficha del Sujeto
- Raz\u00f3n Social: {company}
- CUIT: {cuit}
- Tipo de persona: [jur\u00eddica/f\u00edsica seg\u00fan CUIT]
- Jurisdicci\u00f3n: [provincia seg\u00fan CUIT]
- Fecha del an\u00e1lisis: {fecha}

## An\u00e1lisis por Factor de Riesgo

### 1. Riesgo Financiero (Peso: 20%) \u2014 Score: [0-100] \u2014 Nivel: [Bajo/Bajo-Medio/Medio/Alto/Cr\u00edtico]
- An\u00e1lisis de datos BCRA, perfil crediticio, cheques rechazados
- Fuentes consultadas
- Hallazgos y nivel de confianza

### 2. Riesgo Tributario (Peso: 15%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- Situaci\u00f3n ARCA probable, deudas fiscales
- Fuentes a consultar
- Hallazgos y nivel de confianza

### 3. Riesgo Legal (Peso: 20%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- Tipo societario, causas judiciales, embargos
- Fuentes a consultar
- Hallazgos y nivel de confianza

### 4. Riesgo AML / Sanciones (Peso: 20%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- Listas restrictivas (OFAC, ONU, UE, UIF)
- PEP / UIF
- Hallazgos y nivel de confianza

### 5. Riesgo Reputacional (Peso: 10%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- Noticias, litigios, presencia online
- Hallazgos y nivel de confianza

### 6. Riesgo Operativo (Peso: 5%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- Dependencia, concentraci\u00f3n, antig\u00fcedad
- Hallazgos y nivel de confianza

### 7. Riesgo Compliance (Peso: 10%) \u2014 Score: [0-100] \u2014 Nivel: [...]
- PEP, contrataciones Estado, inhabilitaciones
- Hallazgos y nivel de confianza

## Matriz de Riesgos Consolidada
| Factor | Score | Nivel | Peso | Contribuci\u00f3n |
|--------|-------|-------|------|----------------|
| Financiero | 0-100 | ... | 20% | score x 0.20 |
| Tributario | 0-100 | ... | 15% | score x 0.15 |
| Legal | 0-100 | ... | 20% | score x 0.20 |
| AML | 0-100 | ... | 20% | score x 0.20 |
| Reputacional | 0-100 | ... | 10% | score x 0.10 |
| Operativo | 0-100 | ... | 5% | score x 0.05 |
| Compliance | 0-100 | ... | 10% | score x 0.10 |
| **General** | **0-100** | **...** | **100%** | **suma** |

## Matriz Impacto vs Probabilidad
[Inclu\u00ed la matriz con el resultado estimado]

## Score General de Riesgo: [0-100] \u2014 [Bajo/Bajo-Medio/Medio/Alto/Cr\u00edtico]

## Recomendaci\u00f3n
[APROBAR / APROBAR CON MITIGACIONES / RECHAZAR]
[Lista de mitigaciones requeridas si corresponde]

## Pr\u00f3ximos Pasos
Verificaciones que un analista humano debe realizar.

EXTENSI\u00d3N: 600-1200 palabras. S\u00e9 concreto, no gen\u00e9rico. Inclu\u00ed scores num\u00e9ricos en CADA factor.

IMPORTANTE: Al final del informe, inclu\u00ed esta secci\u00f3n estructurada con los scores EXACTOS:

===SCORES===
Financiero: [0-100]
Tributario: [0-100]
Legal: [0-100]
AML: [0-100]
Reputacional: [0-100]
Operativo: [0-100]
Compliance: [0-100]
General: [0-100]
Recomendacion: [APROBAR|APROBAR CON MITIGACIONES|RECHAZAR]
===END SCORES===
"""

def build_dd_report_prompt(company, cuit, transcript):
    return f"""Sos un Oficial Senior de Due Diligence de Prisma Consulting.

Gener\u00e1 un INFORME DE DUE DILIGENCE estructurado para {company} (CUIT: {cuit}).

TRANSCRIPCI\u00d3N DE LA INVESTIGACI\u00d3N:
{transcript}

ESTRUCTURA DEL INFORME (en markdown):

# Informe de Due Diligence \u2014 {company}

## Resumen Ejecutivo
Breve descripci\u00f3n del perfil de riesgo general.

## Ficha del Sujeto
- Raz\u00f3n Social: {company}
- CUIT: {cuit}
- Fecha del an\u00e1lisis: [fecha actual]

## An\u00e1lisis por Dominio

### 1. Informaci\u00f3n Legal
- Tipo societario
- Estado de constituci\u00f3n
- Autoridades
- Hallazgos y alertas

### 2. Situaci\u00f3n Tributaria
- Situaci\u00f3n ARCA
- Impuestos registrados
- Empleados declarados
- Hallazgos y alertas

### 3. Situaci\u00f3n Financiera
- Perfil crediticio
- Deudas / cheques
- Capacidad financiera
- Hallazgos y alertas

### 4. Compliance & AML
- Listas restrictivas
- PEP / UIF
- Riesgo AML
- Hallazgos y alertas

### 5. Reputaci\u00f3n & OSINT
- Noticias y litigios
- Causas judiciales
- Riesgo reputacional
- Hallazgos y alertas

### 6. Contrataciones & PI
- Contratos con el Estado
- Marcas y patentes
- Dominios
- Hallazgos y alertas

## Matriz de Riesgos

| Factor | Nivel | Score | Fundamento |
|--------|-------|-------|------------|
| Legal | Bajo/Medio/Alto/Cr\u00edtico | 0-100 | ... |
| Tributario | ... | ... | ... |
| Financiero | ... | ... | ... |
| Compliance | ... | ... | ... |
| Reputacional | ... | ... | ... |
| Contractual | ... | ... | ... |

## Score General de Riesgo: [0-100] \u2014 [Bajo/Medio/Alto/Cr\u00edtico]

## Conclusiones y Recomendaciones

EXTENSI\u00d3N: 800-1500 palabras. Inclu\u00ed solo informaci\u00f3n respaldada por la transcripci\u00f3n.
"""

def build_diagnosis_system_prompt(engine, dims, dd_report):
    context = engine.build_context(dimensions=dims)
    ctx_section = _build_knowledge_section(context, dims)
    dd_context = ""
    if dd_report and "No se realiz\u00f3" not in dd_report:
        dd_context = f"""
INFORME DE DUE DILIGENCE (investigaci\u00f3n previa):
{dd_report}

Us\u00e1 esta informaci\u00f3n como contexto. No preguntes de nuevo lo que ya se investig\u00f3.
Profundiz\u00e1 en las \u00e1reas que necesiten m\u00e1s detalle."""
    else:
        dd_context = "\nNOTA: No se realiz\u00f3 un Due Diligence previo. Investig\u00e1 todos los aspectos del negocio durante la entrevista.\n"
    return f"""Sos un consultor senior de Prisma Consulting especializado en diagn\u00f3stico empresarial para PyMEs.

Tu objetivo es entrevistar al due\u00f1o o gerente para completar el diagn\u00f3stico de su empresa.
{dd_context}

REGLAS DE CONDUCTA:
- Salud\u00e1 al usuario y presentate como consultor de Prisma Consulting.
- Hac\u00e9 UNA pregunta por vez. No bombardees.
- Us\u00e1 tono profesional pero cercano, en espa\u00f1ol.
- Despu\u00e9s de 3-4 intercambios sobre un tema, avanz\u00e1 al siguiente.
- Bas\u00e1 tus preguntas en las metodolog\u00edas, marcos y patrones listados.
- Cubr\u00ed TODAS las dimensiones seleccionadas.
- Cuando hayas cubierto todas, ofrec\u00e9 generar el diagn\u00f3stico final.

{ctx_section}

REGLA DE ORO (Micro-Insights):
Cada 3 respuestas del usuario, interrump\u00ed brevemente el formato de preguntas para ofrecer
un 'Micro-Insight' (ej: 'Basado en tu respuesta, esto es un riesgo operativo t\u00edpico en tu sector...').
Manten\u00e9 esto breve (m\u00e1ximo 2 l\u00edneas).

ESTRUCTURA:
1. Pregunt\u00e1 por el contexto general si hace falta (rubro, tama\u00f1o, mercado).
2. Abord\u00e1 cada dimensi\u00f3n con preguntas basadas en sus metodolog\u00edas y marcos.
3. Identific\u00e1 patrones aplicables seg\u00fan lo que cuenta el cliente.
4. Cada 3 respuestas, ofrec\u00e9 un Micro-Insight de 1-2 l\u00edneas.
5. Al final, pregunt\u00e1 si quiere agregar algo m\u00e1s.

FORMATO: espa\u00f1ol, p\u00e1rrafos cortos, emojis con moderaci\u00f3n.
"""

def build_diagnosis_report_prompt(engine, dims, transcript, dd_report, company):
    from datetime import date as _dt
    fecha = _dt.today().strftime("%d/%m/%Y")
    context = engine.build_context(dimensions=dims)
    ctx_section = _build_knowledge_section(context, dims)
    dims_str = ", ".join(DIMENSIONES.get(d, d) for d in dims)
    dd_section = f"\nINFORME DE DUE DILIGENCE:\n{dd_report}" if dd_report and "No se realiz\u00f3" not in dd_report else "\nNOTA: No se realiz\u00f3 Due Diligence previo.\n"
    dd_instruction = "Integr\u00e1 los hallazgos del Due Diligence donde corresponda." if dd_report and "No se realiz\u00f3" not in dd_report else "El diagn\u00f3stico se basa \u00fanicamente en la entrevista."
    return f"""Sos un consultor senior de Prisma Consulting. Gener\u00e1 un diagn\u00f3stico empresarial estructurado.

DIMENSIONES ANALIZADAS: {dims_str}

{ctx_section}
{dd_section}
TRANSCRIPCI\u00d3N DE LA ENTREVISTA:
{transcript}

INSTRUCCIONES \u2014 Gener\u00e1 un informe en markdown con esta estructura:

# Diagn\u00f3stico Empresarial \u2014 {company}
**Fecha de emisi\u00f3n: {fecha}**

## Resumen Ejecutivo
2-3 p\u00e1rrafos citando los marcos usados y referenciando hallazgos del Due Diligence.

## An\u00e1lisis por Dimensi\u00f3n
### [Nombre de la dimensi\u00f3n]
- **Metodolog\u00eda aplicada:** [frameworks/patrones usados]
- **Hallazgos clave:**
- **Fortalezas:**
- **\u00c1reas de mejora:**
- **Recomendaciones:** (2-3 acciones citando patrones)

## Priorizaci\u00f3n
| Prioridad | Acci\u00f3n | Dimensi\u00f3n | Impacto | Plazo |

## Plan de Acci\u00f3n
3-5 acciones con plazo y responsable.

IMPORTANTE: cit\u00e1 los frameworks y patrones de Prisma Consulting usados. {dd_instruction} S\u00e9 espec\u00edfico, no gen\u00e9rico. Extensi\u00f3n: 1000-2000 palabras.
"""

def init_session():
    defaults = {
        "chat_history": [],
        "phase": "setup",
        "dd_report": None,
        "diagnosis_report": None,
        "company": "",
        "cuit": "",
        "selected_dims": list(DIMENSIONES.keys()),
        "do_dd": True,
        "dx_chat": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def render_header(company, phase_label, phase_class, progress_val=None, stage_text=None):
    st.markdown(f"""<div style="background:linear-gradient(135deg,{BLUE_800},{BLUE_700});border-radius:12px;padding:1rem 1.5rem;margin-bottom:1rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;color:white;">
            <div><strong style="font-size:1.1rem;">Prisma Consulting</strong><br>
            <span style="font-size:0.7rem;opacity:0.7;">Klar Analytics</span><br>
            <span style="font-size:0.85rem;opacity:0.9;">{company}</span></div>
            <div style="text-align:right;">
                <span class="phase-badge {phase_class}">{phase_label}</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    if progress_val is not None:
        col_pbar, col_stage = st.columns([3, 1])
        with col_pbar:
            st.progress(progress_val)
        with col_stage:
            if stage_text:
                st.markdown(f"""<div style="background:{BLUE_100};border-radius:8px;padding:0.3rem 0.8rem;text-align:center;font-size:0.85rem;font-weight:500;color:{BLUE_800};">{stage_text}</div>""", unsafe_allow_html=True)

def sidebar_api_key():
    if not st.session_state.get("api_key"):
        cfg_key = _load_api_key()
        if cfg_key:
            st.session_state.api_key = cfg_key

    key = st.session_state.get("api_key", "")

    if key:
        st.sidebar.success("\U0001f510 API Key configurada")
        mask = key[:6] + "*" * (len(key) - 10) + key[-4:]
        st.sidebar.caption(f"`{mask}`")
        if st.sidebar.button("Cambiar key", key="btn_change_key"):
            del st.session_state["api_key"]
            st.rerun()
        return key

    new_key = st.sidebar.text_input(
        "\U0001f511 Gemini API Key",
        type="password",
        key="api_key_input",
        help="Obten\u00e9 tu key gratis en https://aistudio.google.com/apikey",
    )
    if st.sidebar.button("\U0001f4be Guardar", key="btn_save_key"):
        if new_key and len(new_key) > 10 and " " not in new_key:
            st.session_state.api_key = new_key
            _save_api_key(new_key)
            st.rerun()
        else:
            st.sidebar.error("La key debe tener m\u00e1s de 10 caracteres y sin espacios")
    return st.session_state.get("api_key", "")

def page_setup(engine):
    st.markdown("### Datos de la Empresa")
    st.markdown("Ingres\u00e1 los datos de la empresa que quer\u00e9s analizar:")
    c1, c2 = st.columns(2)
    with c1:
        company = st.text_input("Nombre o Raz\u00f3n Social", key="f_company", placeholder="Ej: MiPyME S.A.")
    with c2:
        cuit = st.text_input("CUIT", key="f_cuit", placeholder="Ej: 30-12345678-9", max_chars=13)
    st.markdown("### \U0001f50d Due Diligence Autom\u00e1tico")
    do_dd = st.checkbox("Realizar Due Diligence Autom\u00e1tico", value=True,
                        help="El agente investigar\u00e1 autom\u00e1ticamente usando el nombre y CUIT, y generar\u00e1 un informe preliminar de riesgos legales, tributarios, financieros, compliance, reputacionales y contractuales")
    st.caption("Si no lo activ\u00e1s, se pasar\u00e1 directamente al diagn\u00f3stico empresarial.")
    st.markdown("### Dimensiones a diagnosticar (etapa posterior)")
    st.caption("Luego se realizar\u00e1 un diagn\u00f3stico empresarial en estas \u00e1reas:")
    cols_dim = st.columns(3)
    dims = []
    for i, (key, label) in enumerate(DIMENSIONES.items()):
        with cols_dim[i % 3]:
            if st.checkbox(label, value=True, key=f"dim_{key}"):
                dims.append(key)
    st.markdown("---")
    if st.button("\U0001f680 Iniciar", type="primary", use_container_width=True):
        errores = []
        if not company: errores.append("Ingres\u00e1 el nombre de la empresa.")
        if not cuit: errores.append("Ingres\u00e1 el CUIT.")
        if not dims: errores.append("Seleccion\u00e1 al menos una dimensi\u00f3n.")
        if errores:
            for e in errores: st.error(e)
        else:
            st.session_state.company = company
            st.session_state.cuit = cuit
            st.session_state.selected_dims = dims
            st.session_state.do_dd = do_dd
            st.session_state.phase = "dd_auto" if do_dd else "diagnosis"
            st.rerun()

def _step_status(status, label, state="running"):
    """Update a st.status step. state: 'running', 'complete', 'error'."""
    if state == "running":
        status.update(label=label, state="running")
    elif state == "complete":
        status.update(label=label, state="complete")
    elif state == "error":
        status.update(label=label, state="error")

def phase_dd_auto(engine):
    company = st.session_state.company
    cuit = st.session_state.cuit
    api_key = sidebar_api_key()
    if not api_key:
        return

    render_header(company, "DUE DILIGENCE AUTOM\u00c1TICO", "phase-dd")

    if not st.session_state.get("dd_report"):
        status = st.status("Iniciando Due Diligence...", expanded=True)

        # ── Step 1: BCRA Cheques ──
        _step_status(status, "\U0001f4b0 Consultando BCRA - Cheques Rechazados...", "running")
        cheques_text = ""
        try:
            from tools.data_sources import consultar_bcra_cheques, formatear_cheques
            cheques_data = consultar_bcra_cheques(cuit)
            cheques_text = formatear_cheques(cheques_data)
            if cheques_data.get("ok"):
                _step_status(status, "\u2705 BCRA - Cheques Rechazados: consultado correctamente", "complete")
            else:
                _step_status(status, "\u26a0\ufe0f BCRA - Cheques Rechazados: %s" % cheques_data.get("error", "error"), "error")
        except Exception as e:
            cheques_text = "- BCRA Cheques Rechazados: Error inesperado: %s" % e
            _step_status(status, "\u274c BCRA - Cheques Rechazados: error de conexi\u00f3n", "error")

        # ── Step 2: BCRA Deudas ──
        _step_status(status, "\U0001f4b0 Consultando BCRA - Central de Deudores...", "running")
        deudas_text = ""
        try:
            from tools.data_sources import consultar_bcra_deudas, formatear_deudas
            deudas_data = consultar_bcra_deudas(cuit)
            deudas_text = formatear_deudas(deudas_data)
            if deudas_data.get("ok"):
                _step_status(status, "\u2705 BCRA - Central de Deudores: consultado correctamente", "complete")
            else:
                _step_status(status, "\u26a0\ufe0f BCRA - Central de Deudores: %s" % deudas_data.get("error", "error"), "error")
        except Exception as e:
            deudas_text = "- BCRA Central de Deudores: Error inesperado: %s" % e
            _step_status(status, "\u274c BCRA - Central de Deudores: error de conexi\u00f3n", "error")

        # ── Step 3: CUIT Online ──
        _step_status(status, "\U0001f50d Consultando CUIT Online (datos fiscales)...", "running")
        fiscal_text = ""
        try:
            from tools.data_sources import consultar_cuit_online, formatear_fiscal
            fiscal_data = consultar_cuit_online(cuit)
            fiscal_text = formatear_fiscal(fiscal_data)
            if fiscal_data.get("ok"):
                _step_status(status, "\u2705 CUIT Online: datos fiscales obtenidos", "complete")
            else:
                _step_status(status, "\u26a0\ufe0f CUIT Online: %s" % fiscal_data.get("error", "error"), "error")
        except Exception as e:
            fiscal_text = "- CUIT Online: Error inesperado: %s" % e
            _step_status(status, "\u274c CUIT Online: error de conexi\u00f3n", "error")

        # ── Assemble datasource text ──
        datasource_text = """=== DATOS OBTENIDOS DE FUENTES OFICIALES ===

[ARCA/AFIP - Datos Fiscales (via CUIT Online)]
%s

[BCRA - Cheques Rechazados]
%s

[BCRA - Central de Deudores]
%s

=== FIN DE DATOS OFICIALES ===""" % (fiscal_text, cheques_text, deudas_text)

        # ── Step 4: Gemini DD generation (with retries) ──
        max_retries = 3
        last_error = None
        for attempt in range(1, max_retries + 1):
            label = "Generando informe de Due Diligence con IA%s..." % (
                " (intento %d/%d)" % (attempt, max_retries) if max_retries > 1 else ""
            )
            _step_status(status, label, "running")
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                prompt = build_dd_auto_prompt(engine, company, cuit, datasource_text)
                model = genai.GenerativeModel("gemini-3.1-flash-lite")
                resp = model.generate_content(prompt)
                st.session_state.dd_report = resp.text
                _step_status(status, "\u2705 Informe de Due Diligence generado exitosamente", "complete")
                status.update(state="complete")
            except Exception as e:
                last_error = e
                if attempt < max_retries:
                    _step_status(status, "\u26a0\ufe0f Intento %d/%d fall\u00f3: %s. Reintentando..." % (attempt, max_retries, e), "error")
                    import time
                    time.sleep(2 ** attempt)  # exponential backoff
                else:
                    _step_status(status, "\u274c Error al generar el informe de Due Diligence", "error")
                    status.update(state="error")
                    st.error("Error ejecutando Due Diligence despu\u00e9s de %d intentos: %s" % (max_retries, last_error))
                    return

    # Show summary of findings
    dd_text = st.session_state.dd_report

    # Parse "Resumen de Hallazgos" section from the report
    summary_section = ""
    if "## Resumen de Hallazgos" in dd_text:
        import re as _re
        m = _re.search(r"## Resumen de Hallazgos\s*(.*?)(?=\n## |\Z)", dd_text, _re.DOTALL)
        if m:
            summary_section = m.group(1).strip()

    st.markdown(f"""<div class="card" style="border-left:4px solid {BLUE_500};">
        <h3 style="margin-top:0;color:{BLUE_800};">\U0001f4cb Resumen de Hallazgos</h3>
    </div>""", unsafe_allow_html=True)
    if summary_section:
        st.markdown(summary_section)
    else:
        st.markdown(dd_text[:600])

    with st.expander("Ver informe completo de Due Diligence"):
        st.markdown(dd_text)

    # Generate professional HTML report (primary format)
    try:
        from tools.html_report import generate_dd_html
        html_report = generate_dd_html(company, cuit, dd_text)
        st.components.v1.html(html_report, height=700, scrolling=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.download_button(
                "\U0001f4c4 Descargar Informe (HTML)",
                data=html_report,
                file_name="due_diligence_%s.html" % company,
                mime="text/html",
                use_container_width=True,
            )
        with col2:
            st.markdown(
                '<div style="padding:8px;font-size:0.75rem;color:#94a3b8;text-align:center">'
                'Tambi\u00e9n pod\u00e9s usar <kbd>Ctrl+P</kbd> en el visor<br>para guardar como PDF</div>',
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.caption("No se pudo generar el visor profesional: %s" % e)

    st.markdown("---")
    c1, c2 = st.columns([3, 1])
    with c1:
        if st.button("Continuar al Diagn\u00f3stico Empresarial", type="primary", use_container_width=True):
            st.session_state.phase = "diagnosis"
            st.rerun()
    with c2:
        if st.button("↺ Reiniciar"):
            for key in list(st.session_state.keys()):
                if key not in ("api_key",):
                    del st.session_state[key]
            st.rerun()

def phase_diagnosis(engine):
    company = st.session_state.company
    dims = st.session_state.selected_dims
    dd_report = st.session_state.dd_report or "(No se realiz\u00f3 Due Diligence)"
    api_key = sidebar_api_key()
    if not api_key:
        return

    dims_totales = len(dims)
    user_msgs = sum(1 for m in st.session_state.chat_history if m["role"] == "user")
    msgs_por_dim = 3
    dim_idx = min(user_msgs // msgs_por_dim, dims_totales - 1) if dims_totales > 0 else 0
    dim_actual = DIMENSIONES.get(dims[dim_idx], dims[dim_idx]) if dims else ""
    progreso = min(user_msgs / (dims_totales * msgs_por_dim), 1.0)

    render_header(company, "DIAGN\u00d3STICO", "phase-dx", progreso, dim_actual)

    if not st.session_state.get("dx_chat"):
        with st.spinner("Iniciando diagn\u00f3stico..."):
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                system_prompt = build_diagnosis_system_prompt(engine, dims, dd_report)
                model = genai.GenerativeModel("gemini-3.1-flash-lite", system_instruction=system_prompt)
                chat = model.start_chat(history=[])
                dd_context = "Se complet\u00f3 un Due Diligence previo. Usalo como contexto." if st.session_state.get("dd_report") and "No se realiz\u00f3" not in dd_report else "No hay Due Diligence previo. Investig\u00e1 todo durante la entrevista."
                greeting = chat.send_message(
                    f"El cliente es {company}. "
                    f"{dd_context} "
                    f"Inici\u00e1 la entrevista de diagn\u00f3stico empresarial. "
                    f"Presentate como consultor de Prisma Consulting."
                )
                st.session_state.dx_chat = chat
                st.session_state.chat_history = [{"role": "assistant", "content": greeting.text}]
                st.rerun()
            except Exception as e:
                st.error(f"Error conectando con Gemini: {e}")
                return

    chat_container = st.container(height=450, border=True)
    with chat_container:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    if prompt := st.chat_input("Escrib\u00ed tu respuesta..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        ok = True
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            response = st.session_state.dx_chat.send_message(prompt)
            st.session_state.chat_history.append({"role": "assistant", "content": response.text})
        except Exception as e:
            ok = False
            st.error(f"Error de conexi\u00f3n: {e}")
        if ok:
            st.rerun()

    st.markdown("---")
    c1, c2, c3 = st.columns([2, 2, 1])
    with c1:
        if st.button("📋 Generar diagn\u00f3stico final", type="primary", use_container_width=True):
            transcript = "\n".join(
                f"{'Cliente' if m['role']=='user' else 'Consultor'}: {m['content']}"
                for m in st.session_state.chat_history
            )
            ok = True
            with st.spinner("Generando diagn\u00f3stico..."):
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=api_key)
                    report_prompt = build_diagnosis_report_prompt(engine, dims, transcript, dd_report, company)
                    model = genai.GenerativeModel("gemini-3.1-flash-lite")
                    resp = model.generate_content(report_prompt)
                    st.session_state.diagnosis_report = resp.text
                    st.session_state.phase = "done"
                except Exception as e:
                    ok = False
                    st.error(f"Error al generar diagn\u00f3stico: {e}")
            if ok:
                st.rerun()
    with c3:
        if st.button("↺ Reiniciar"):
            for key in list(st.session_state.keys()):
                if key not in ("api_key",):
                    del st.session_state[key]
            st.rerun()

def phase_done():
    company = st.session_state.company
    cuit = st.session_state.cuit
    dd_report = st.session_state.dd_report
    diagnosis_report = st.session_state.diagnosis_report
    render_header(company, "COMPLETADO", "phase-done")

    tab1, tab2 = st.tabs(["Informe de Due Diligence", "Diagn\u00f3stico Empresarial"])
    with tab1:
        if dd_report:
            try:
                from tools.html_report import generate_dd_html
                html_report = generate_dd_html(company, cuit, dd_report)
                st.components.v1.html(html_report, height=700, scrolling=True)
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.download_button(
                        "\U0001f4c4 Descargar Informe (HTML)",
                        data=html_report,
                        file_name="due_diligence_%s.html" % company,
                        mime="text/html",
                        use_container_width=True,
                    )
                with col2:
                    st.markdown(
                        '<div style="padding:8px;font-size:0.75rem;color:#94a3b8;text-align:center">'
                        'Tambi\u00e9n pod\u00e9s usar <kbd>Ctrl+P</kbd> en el visor<br>para guardar como PDF</div>',
                        unsafe_allow_html=True,
                    )
            except Exception as e:
                st.caption("Visor profesional no disponible: %s" % e)
            with st.expander("Ver texto original del informe"):
                st.markdown(dd_report)
        else:
            st.warning("No hay informe de Due Diligence disponible.")
    with tab2:
        if diagnosis_report:
            st.markdown(diagnosis_report)
            try:
                from tools.pdf_report import make_diagnosis_pdf
                pdf_bytes = make_diagnosis_pdf(company, cuit, diagnosis_report)
                st.download_button("📥 Descargar Diagn\u00f3stico (PDF)",
                                   data=pdf_bytes,
                                   file_name=f"diagnostico_{company}.pdf",
                                   mime="application/pdf")
            except Exception as e:
                st.caption(f"No se pudo generar el PDF: {e}")
        else:
            st.warning("No hay diagn\u00f3stico disponible.")
    st.markdown("---")
    cols = st.columns(3)
    with cols[0]:
        st.markdown(
            '<div style="font-size:0.75rem;color:#94a3b8;text-align:center;padding:8px;">'
            'Us\u00e1 <kbd>Ctrl+P</kbd> en los visores HTML para exportar como PDF</div>',
            unsafe_allow_html=True,
        )
    with cols[1]:
        if st.button("📧 Enviar por correo", use_container_width=True):
            st.info("Funcionalidad pr\u00f3ximamente disponible.")
    with cols[2]:
        if st.button("🔄 Nuevo an\u00e1lisis", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key not in ("api_key",):
                    del st.session_state[key]
            st.rerun()

def main():
    st.set_page_config(
        page_title="Prisma Consulting | Klar Analytics \u2014 Diagn\u00f3stico Empresarial",
        page_icon="\u25c6",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(CSS, unsafe_allow_html=True)
    engine = load_engine()
    init_session()

    with st.sidebar:
        st.markdown(f"""<div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
            <span style="font-size:30px;color:{BLUE_500};">&#9670;</span>
            <div>
                <div style="font-size:22px;font-weight:700;color:{BLUE_800};letter-spacing:-0.5px;line-height:1.1;">Prisma</div>
                <div style="font-size:12px;color:{GRAY_600};margin-top:-2px;">Klar Analytics</div>
            </div>
        </div>""", unsafe_allow_html=True)
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.8rem; margin-top:-0.1rem;">Diagn\u00f3stico con IA para PYMEs</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.session_state.phase and st.session_state.phase not in ("setup",):
            st.markdown(f"**Empresa:** {st.session_state.company}")
            st.markdown(f"**CUIT:** {st.session_state.cuit}")
            st.markdown("---")
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.75rem;">Powered by Gemini + KnowledgeEngine<br>Prisma Consulting \u00a9 2026</div>', unsafe_allow_html=True)

    phase = st.session_state.phase or "setup"

    if phase == "setup":
        page_setup(engine)
    elif phase == "dd_auto":
        phase_dd_auto(engine)
    elif phase == "diagnosis":
        phase_diagnosis(engine)
    elif phase == "done":
        phase_done()

if __name__ == "__main__":
    main()
