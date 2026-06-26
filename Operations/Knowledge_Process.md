# Proceso de Conocimiento

> **Sistema Operativo** — Knowledge Process de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del Sistema de Conocimiento](#1-arquitectura-del-sistema-de-conocimiento)
2. [Ciclo de Vida del Conocimiento](#2-ciclo-de-vida-del-conocimiento)
3. [Estructura del Conocimiento](#3-estructura-del-conocimiento)
4. [Adquisición](#4-adquisición)
5. [Almacenamiento](#5-almacenamiento)
6. [Distribución](#6-distribución)
7. [Aplicación](#7-aplicación)
8. [Revisión y Mejora](#8-revisión-y-mejora)
9. [Gobernanza del Conocimiento](#9-gobernanza-del-conocimiento)
10. [KPIs de Conocimiento](#10-kpis-de-conocimiento)

---

## 1. Arquitectura del Sistema de Conocimiento

### 1.1 Visión General

```
                    ┌─────────────────────────────────┐
                    │      Ecosistema de Conocimiento  │
                    │           Klar Analytics          │
                    └──────────┬──────────┬────────────┘
                               │          │
              ┌────────────────┘          └────────────────┐
              │                                              │
     ┌────────▼────────┐                         ┌─────────▼─────────┐
     │  Conocimiento    │                         │  Conocimiento      │
     │  Estructurado    │                         │  No Estructurado   │
     │  (Knowledge/)    │                         │  (Casos, Lecciones)│
     └────────┬────────┘                         └─────────┬──────────┘
              │                                              │
     ┌────────▼────────┐                         ┌─────────▼─────────┐
     │  CORE/           │                         │  Casos/            │
     │    Finance       │                         │  Lecciones.md      │
     │    Operations    │                         │  Post-mortems      │
     │    Risk          │                         └───────────────────┘
     │    Strategy      │
     │    Talent        │
     └─────────────────┘
```

### 1.2 Principios del Sistema

| Principio | Descripción |
|---|---|
| **Captura Continua** | Todo aprendizaje se documenta dentro de 48h |
| **Estructura Consistente** | Todo conocimiento sigue templates estandarizados |
| **Accesibilidad** | Todo el equipo puede acceder a cualquier知识 |
| **Reusabilidad** | El conocimiento está diseñado para ser reutilizado en diagnósticos |
| **Mejora Continua** | Cada ciclo de uso retroalimenta y mejora el conocimiento |
| **Trazabilidad** | Todo conocimiento tiene fuente, fecha y responsable |

### 1.3 Ciclo OODA del Conocimiento

```
Observar ──► Orientar ──► Decidir ──► Actuar
   │            │            │           │
   │            │            │           │
   Leer         Analizar     Priorizar   Actualizar
   Knowledge/   Gaps vs      Qué         Knowledge/
   Casos/       Diagnósticos añadir      CORE/
   Skills/                                  Playbooks/
   Playbooks/                               Agents/
```

---

## 2. Ciclo de Vida del Conocimiento

### 2.1 Etapas

```
Adquisición → Almacenamiento → Distribución → Aplicación → Revisión → Mejora
     │              │              │              │           │         │
     │              │              │              │           │         │
     Crear       Estructurar     Publicar       Usar en     Evaluar   Retroalimentar
     Importar    Indexar         Notificar      Diagnóstico QA         Actualizar
     Extraer     Versionar       Capacitar      Informes    Impacto   Refinar
```

### 2.2 Flujo Completo

```
Nuevo aprendizaje identificado →
    ↓
Documentar (template estándar) →
    ↓
Revisar (peer review) →
    ↓
Aprobar (Director) →
    ↓
Almacenar (Knowledge/ o recurso correspondiente) →
    ↓
Notificar (Slack/email al equipo) →
    ↓
Aplicar en próximo diagnóstico relevante →
    ↓
Registrar uso (CRM / log de aplicaciones) →
    ↓
Revisar efectividad (post-diagnóstico) →
    ↓
Actualizar si es necesario →
    ↓
Retirar si obsoleto
```

---

## 3. Estructura del Conocimiento

### 3.1 Mapa del Conocimiento

| Directorio | Contenido | Formato | Responsable |
|---|---|---|---|
| `Knowledge/CORE/Finance/` | Frameworks y patrones financieros | Markdown | Finance Agent |
| `Knowledge/CORE/Operations/` | Frameworks y patrones operativos | Markdown | Operations Agent |
| `Knowledge/CORE/Risk/` | Frameworks y patrones de riesgo | Markdown | Risk Agent |
| `Knowledge/CORE/Strategy/` | Frameworks y patrones estratégicos | Markdown | Strategy Agent |
| `Knowledge/Casos/` | Diagnósticos completos por cliente | Markdown+PDF | Delivery Lead |
| `Knowledge/Benchmarks/` | Benchmarks por industria | Markdown | Knowledge Agent |
| `Playbooks/` | SOPs operativos | Markdown | Dirección |
| `Skills/` | Skills de agentes (fichas técnicas) | Markdown | Dirección |
| `Agents/` | Definiciones de agentes | Markdown | Dirección |
| `Brand/` | Identidad y marca | Markdown+assets | Dirección |
| `Operations/` | Sistema operativo (este directorio) | Markdown | Dirección |

### 3.2 Templates de Conocimiento

| Tipo | Template | Ubicación |
|---|---|---|
| Framework | `Knowledge/Templates/Framework_Template.md` | `Knowledge/Templates/` |
| Patrón | `Knowledge/Templates/Pattern_Template.md` | `Knowledge/Templates/` |
| Caso | `Knowledge/Templates/Case_Template.md` | `Knowledge/Templates/` |
| Lección Aprendida | `Knowledge/Templates/Lesson_Template.md` | `Knowledge/Templates/` |
| Benchmark | `Knowledge/Templates/Benchmark_Template.md` | `Knowledge/Templates/` |

### 3.3 Metadatos Obligatorios

Todo documento de conocimiento debe incluir:

| Campo | Ejemplo | Obligatorio |
|---|---|---|
| `title` | "Análisis Dupont para PyMEs" | Sí |
| `version` | "1.2" | Sí |
| `date` | "2026-06-15" | Sí |
| `author` | "Finance Agent" | Sí |
| `tags` | `[finanzas, ratios, rentabilidad]` | Sí |
| `status` | "active" / "draft" / "deprecated" | Sí |
| `source` | "Caso Cliente X, Libro Y" | Sí |
| `review_date` | "2026-09-15" | Sí |

---

## 4. Adquisición

### 4.1 Fuentes de Conocimiento

| Fuente | Tipo | Frecuencia | Responsable |
|---|---|---|---|
| Diagnósticos realizados | Interna | Por proyecto | Delivery Lead |
| Post-mortems de proyectos | Interna | Por proyecto | Delivery Lead |
| Investigación de mercado | Externa | Mensual | Knowledge Agent |
| Libros y publicaciones | Externa | Trimestral | Dirección |
| Cursos y certificaciones | Externa | Semestral | Team |
| Benchmarking de competidores | Externa | Trimestral | Knowledge Agent |
| Feedback de clientes | Interna | Por proyecto | Client Success |
| Comunidad / Redes profesionales | Externa | Continua | Todo el equipo |

### 4.2 Proceso de Adquisición

```
Identificar conocimiento valioso →
    ↓
¿Existe ya en Knowledge/?
    ├── Sí → ¿Actualización? → Actualizar versión
    └── No →
        ↓
Documentar usando template correspondiente →
    ↓
Agregar metadatos →
    ↓
Enviar a revisión
```

### 4.3 Priorización de Adquisición

| Criterio | Peso | Evaluación (1-5) |
|---|---|---|
| Relevancia para diagnósticos frecuentes | 30% | |
| Potencial de reutilización | 25% | |
| Diferencial competitivo | 20% | |
| Demanda del cliente (insights solicitados) | 15% | |
| Facilidad de adquisición | 10% | |
| **Total** | **100%** | |

---

## 5. Almacenamiento

### 5.1 Estructura de Archivos

```
Knowledge/
├── CORE/
│   ├── Finance/
│   │   ├── Financial_Ratios.md
│   │   ├── Cashflow_Analysis.md
│   │   └── Dupont_Analysis.md
│   ├── Operations/
│   │   ├── Process_Mapping_Frameworks.md
│   │   └── Operational_Excellence.md
│   ├── Risk/
│   │   ├── Risk_Matrix_Framework.md
│   │   └── ESG_Assessment.md
│   ├── Strategy/
│   │   ├── Business_Model_Canvas.md
│   │   └── Competitive_Advantage.md
│   └── Talent/
│       ├── 7S_Framework.md
│       └── Culture_Map.md
├── Casos/
│   ├── Cliente_A/
│   │   ├── Brief_Empresa.md
│   │   ├── Informe_Final.md
│   │   └── Lecciones.md
│   └── Cliente_B/
├── Benchmarks/
│   ├── Retail.md
│   └── Manufacturing.md
└── Templates/
    ├── Framework_Template.md
    ├── Pattern_Template.md
    └── Case_Template.md
```

### 5.2 Control de Versiones

| Práctica | Herramienta | Detalle |
|---|---|---|
| Versionado de documentos | Git | Cada documento incluye versión semántica (1.0.0) |
| CHANGELOG por directorio | Git | `Knowledge/CHANGELOG.md` |
| Tags por release | Git | `v1.0`, `v1.1`, etc. |
| Branch por actualización mayor | Git | `feature/nuevo-framework` |

### 5.3 Políticas de Almacenamiento

| Elemento | Política |
|---|---|
| Formato primario | Markdown (versionable, portable) |
| Formato secundario | PDF (para distribución externa) |
| Backup | Automático diario (Git + cloud) |
| Retención | Indefinida (con estado "deprecated" si obsoleto) |
| Archivo | Mover a `Knowledge/Archived/` tras 2 años sin uso |

---

## 6. Distribución

### 6.1 Canales de Distribución

| Canal | Tipo | Para Quién | Frecuencia |
|---|---|---|---|
| Repositorio Git | Pull | Todo el equipo | A demanda |
| Newsletter interna | Push | Equipo Klar | Semanal |
| Slack / Teams | Push | Equipo Klar | En tiempo real |
| Reunión semanal de conocimiento | Push | Equipo Klar | Semanal |
| Portal de conocimiento (futuro) | Pull | Equipo + Agentes | A demanda |

### 6.2 Proceso de Publicación

```
Nuevo conocimiento documentado →
    ↓
Revisión por par → ¿Cambios? → Iterar
    ↓
Aprobación de Director →
    ↓
Merge a main (Git) →
    ↓
Notificar al equipo (Slack) →
    ↓
Actualizar índice de conocimiento
```

### 6.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Nuevo commit en Knowledge/ | Notificar a Slack #conocimiento |
| Nueva versión de framework | Publicar en newsletter semanal |
| 30 días sin revisión de documento | Recordatorio de revisión |
| Documento marcado "deprecated" | Notificar a equipo, archivar |

---

## 7. Aplicación

### 7.1 Ciclo de Aplicación en Diagnósticos

```
Delivery Lead inicia diagnóstico →
    ↓
Consulta Knowledge/RELEVANTE para industria/cliente →
    ↓
Aplica frameworks del CORE/ correspondiente →
    ↓
Skills/ del agente guían la aplicación →
    ↓
Documenta hallazgos usando Knowledge/ →
    ↓
Post-mortem: ¿Qué funcionó? ¿Qué falta? →
    ↓
Retroalimenta Knowledge/ con nuevos patrones
```

### 7.2 Registro de Aplicación

Cada uso de conocimiento en un diagnóstico se registra:

| Campo | Ejemplo |
|---|---|
| **Knowledge Item** | Financial_Ratios.md |
| **Versión** | 1.2 |
| **Cliente** | Cliente A |
| **Fecha** | 2026-06-10 |
| **Hallazgo** | "ROE bajo indica mala gestión de capital" |
| **Efectividad** | 4/5 |
| **Notas** | "Faltó ratio de apalancamiento" |

---

## 8. Revisión y Mejora

### 8.1 Ciclo de Revisión

| Tipo | Frecuencia | Responsable | Alcance |
|---|---|---|---|
| Auto-revisión | Por uso | Quien lo usó | ¿Funcionó? ¿Faltó algo? |
| Revisión trimestral | Trimestral | Director + Agentes | Todo CORE/, Skills/ |
| Revisión anual | Anual | Dirección | Todo el repositorio |
| Post-mortem de diagnóstico | Por proyecto | Delivery Lead | Casos + lecciones |

### 8.2 Proceso de Mejora

```
Revisión identifica mejora potencial →
    ↓
Documentar propuesta de mejora →
    ↓
Evaluar impacto (priorización) →
    ↓
Si alta prioridad → Implementar →
    ↓
Peer review de cambios →
    ↓
Aprobar y publicar →
    ↓
Notificar actualización
```

### 8.3 Criterios para Deprecación

| Criterio | Acción |
|---|---|
| Framework reemplazado por versión superior | Marcar "deprecated", referenciar nuevo |
| Sin uso en 12 meses | Mover a `Knowledge/Archived/` |
| Información incorrecta o desactualizada | Corregir o deprecar |
| Duplicado de otro documento | Fusionar o deprecar |

---

## 9. Gobernanza del Conocimiento

### 9.1 Roles y Responsabilidades

| Rol | Persona | Responsabilidades |
|---|---|---|
| **Knowledge Director** | Director de Klar | Estrategia de conocimiento, aprobación de cambios mayores |
| **Knowledge Curator** | Designado rotativo | Calidad, consistencia, revisión de contenido |
| **Knowledge Contributor** | Todo el equipo | Documentar aprendizajes, actualizar contenido |
| **Knowledge Consumer** | Agentes (IA) + Equipo | Usar conocimiento en diagnósticos |

### 9.2 Reuniones de Conocimiento

| Reunión | Frecuencia | Duración | Participantes |
|---|---|---|---|
| Weekly Knowledge Sync | Semanal | 30 min | Todo el equipo |
| Knowledge Review Board | Mensual | 60 min | Director + Curator |
| Post-Mortem Review | Por proyecto | 30 min | Delivery Lead + Agentes |
| Quarterly Knowledge Audit | Trimestral | 120 min | Todo el equipo |

### 9.3 Políticas

| Política | Descripción |
|---|---|
| **Calidad sobre cantidad** | Todo contenido debe agregar valor demostrable |
| **No duplicación** | Verificar existencia antes de crear nuevo contenido |
| **Atribución** | Toda fuente debe ser citada |
| **Idioma** | Español (primario), inglés (aceptado para referencias) |
| **Confidencialidad** | No incluir datos sensibles de clientes en CORE/ |

---

## 10. KPIs de Conocimiento

| Indicador | Fórmula | Frecuencia | Meta | Semáforo |
|---|---|---|---|---|
| **Knowledge Items Creados/mes** | Documentos nuevos en Knowledge/ | Mensual | ≥ 3 | 🔴 < 1 🟡 1-3 🟢 ≥ 3 |
| **Knowledge Items Actualizados/mes** | Documentos con versión nueva | Mensual | ≥ 2 | 🔴 < 1 🟡 1-2 🟢 ≥ 2 |
| **Tasa de Reutilización** | Veces usado / Total diagnósticos | Mensual | ≥ 80% | 🔴 < 60% 🟡 60-80% 🟢 ≥ 80% |
| **Time-to-Publish** | Días desde identificación a publicación | Mensual | ≤ 7 días | 🔴 > 14 🟡 7-14 🟢 ≤ 7 |
| **Documentos Sin Revisar > 6 meses** | Conteo | Mensual | ≤ 3 | 🔴 > 5 🟡 3-5 🟢 ≤ 3 |
| **Tasa de Adopción** | Items usados / Items disponibles | Trimestral | ≥ 60% | 🔴 < 40% 🟡 40-60% 🟢 ≥ 60% |
| **Post-Mortem Completion** | Post-mortems realizados / Diagnósticos completados | Mensual | 100% | 🔴 < 80% 🟡 80-100% 🟢 = 100% |
| **Knowledge NPS** | Encuesta al equipo sobre utilidad del conocimiento | Trimestral | ≥ 70 | 🔴 < 50 🟡 50-70 🟢 ≥ 70 |

---

*Fin del documento — Knowledge_Process.md v1.0*
