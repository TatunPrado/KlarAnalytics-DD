# KlarAnalytics-DD

**Due Diligence + Diagnóstico Empresarial con IA**

Aplicación web interactiva que combina una investigación de Due Diligence (cumplimiento, legal, financiero, tributario, compliance, reputacional) con un diagnóstico empresarial integral en 9 dimensiones, todo potenciado por Google Gemini y un motor de conocimiento dinámico.

---

## Funcionalidades

- **Due Diligence**: Investigación estructurada en 6 dominios: legal, tributario, financiero, compliance & AML, reputacional & OSINT, contrataciones & propiedad intelectual. El asistente hace preguntas una por una, detecta señales de alerta y genera un informe de riesgo con scoring.
- **Diagnóstico Empresarial**: Entrevista interactiva en 9 dimensiones (Finanzas, Estrategia, Operaciones, Talento, Riesgos, Modelo de Negocio, Cliente, Marketing, Tecnología). Micro-insights cada 3 respuestas. Genera informe con hallazgos, priorización y plan de acción.
- **Informes Combinados**: Al finalizar, ambos informes están disponibles para descarga en Markdown y JSON, individualmente o combinados.
- **Motor de Conocimiento Dinámico**: 66 artefactos (agentes, skills, frameworks, patrones, playbooks, procesos) leídos del filesystem sin prompts hardcodeados.

---

## Requisitos

- Python 3.11+
- Cuenta gratuita en [Google AI Studio](https://aistudio.google.com/apikey) para obtener una API Key de Gemini

---

## Instalación y uso local

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/KlarAnalytics-DD.git
cd KlarAnalytics-DD

# Crear entorno virtual
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app.py
```

Abrir `http://localhost:8501` en el navegador. Ingresar la API Key de Gemini en la barra lateral.

---

## Despliegue en Streamlit Cloud

1. Subir el repositorio a GitHub
2. Ingresar a [Streamlit Cloud](https://streamlit.io/cloud) y conectar el repositorio
3. Configurar:
   - **Main file path**: `app.py`
   - **Python version**: 3.11
4. Desplegar

No requiere configuración adicional de secrets. Cada usuario ingresa su propia API Key de Gemini.

---

## Estructura del proyecto

```
KlarAnalytics-DD/
├── app.py                   # Aplicación principal (Streamlit)
├── requirements.txt        # Dependencias
├── .gitignore
├── README.md
├── POLITICA_DE_USO.md      # Términos y condiciones
├── KnowledgeEngine/        # Motor de conocimiento
│   ├── __init__.py
│   ├── config.py           # Configuración (paths, dimensiones, stopwords)
│   ├── core.py             # Orquestador principal
│   ├── knowledge_loader.py # Escáner del filesystem
│   ├── parsers.py          # Parsers para cada tipo de artefacto
│   └── prompt_builder.py   # Ensamblador de prompts dinámicos
├── Agents/                 # 12 agentes especializados
├── Skills/                 # 20 habilidades/metodologías
├── Knowledge/              # 10 frameworks + 10 patrones
├── Playbooks/              # 3 playbooks de diagnóstico
├── Operations/             # 11 procesos operativos
└── templates/              # Plantillas HTML de reportes
```

---

## Tecnologías

- **Frontend**: Streamlit
- **LLM**: Google Gemini 3.1 Flash Lite (gratuito)
- **Motor de conocimiento**: KnowledgeEngine (propietario)
- **Lenguaje**: Python 3.11+

---

## Licencia

Uso interno y consultoría. Prohibida su redistribución comercial sin autorización. Ver `POLITICA_DE_USO.md`.
