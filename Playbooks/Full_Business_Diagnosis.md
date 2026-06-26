# Full_Business_Diagnosis

> **Procedimiento Operativo Estándar (SOP)** — Diagnóstico Integral de PyMEs
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Propósito y Alcance](#1-propósito-y-alcance)
2. [Arquitectura del Sistema Multi-Agente](#2-arquitectura-del-sistema-multi-agente)
3. [Flujo General del Proceso](#3-flujo-general-del-proceso)
4. [Etapa 1: Descubrimiento Inicial](#4-etapa-1-descubrimiento-inicial)
5. [Etapa 2: Entrevista Empresarial](#5-etapa-2-entrevista-empresarial)
6. [Etapa 3: Diagnóstico de Modelo de Negocio](#6-etapa-3-diagnóstico-de-modelo-de-negocio)
7. [Etapa 4: Diagnóstico Financiero](#7-etapa-4-diagnóstico-financiero)
8. [Etapa 5: Diagnóstico Operativo](#8-etapa-5-diagnóstico-operativo)
9. [Etapa 6: Diagnóstico Organizacional](#9-etapa-6-diagnóstico-organizacional)
10. [Etapa 7: Diagnóstico de Riesgos](#10-etapa-7-diagnóstico-de-riesgos)
11. [Etapa 8: Consolidación de Hallazgos](#11-etapa-8-consolidación-de-hallazgos)
12. [Etapa 9: Identificación de Causas Raíz](#12-etapa-9-identificación-de-causas-raíz)
13. [Etapa 10: Priorización de Problemas](#13-etapa-10-priorización-de-problemas)
14. [Etapa 11: Diseño de Iniciativas](#14-etapa-11-diseño-de-iniciativas)
15. [Etapa 12: Diseño de Roadmap](#15-etapa-12-diseño-de-roadmap)
16. [Etapa 13: Generación de Informe Ejecutivo](#16-etapa-13-generación-de-informe-ejecutivo)
17. [Apéndices](#17-apéndices)

---

## 1. Propósito y Alcance

### 1.1 Objetivo General
Ejecutar un diagnóstico integral de una PyME aplicando un sistema multi-agente que cubra las dimensiones estratégica, financiera, operativa, organizacional y de riesgos, para identificar problemas, causas raíz y oportunidades de mejora, y generar un plan de transformación con roadmap e iniciativas priorizadas.

### 1.2 Alcance
- Empresas PyME (1–250 empleados, facturación < 50M USD).
- Diagnóstico completo en 13 etapas secuenciales con ejecución paralela donde las dependencias lo permitan.
- Output final: Informe ejecutivo con hallazgos, causas raíz, iniciativas y roadmap.

### 1.3 Precondiciones del Sistema
- Todos los agentes deben estar disponibles y autenticados en el ecosistema.
- Las bases de conocimiento deben estar cargadas y accesibles vía API de conocimiento.
- Las skills deben estar registradas en el catálogo de capacidades del orquestador.
- El Interview_Orchestrator debe tener acceso al canal de comunicación con el cliente (chat, videollamada, cuestionario asíncrono).

---

## 2. Arquitectura del Sistema Multi-Agente

### 2.1 Agentes

| Agente | Rol | Responsabilidad Clave |
|---|---|---|
| **Interview_Orchestrator** | Conductor de entrevistas | Obtener información cualitativa del cliente mediante entrevista estructurada |
| **Business_Model_Analyst** | Analista de modelo de negocio | Evaluar propuesta de valor, segmentos, canales, relaciones, flujo de ingresos |
| **Financial_Analyst** | Analista financiero | Evaluar rentabilidad, liquidez, solvencia, eficiencia financiera |
| **Operations_Analyst** | Analista operativo | Evaluar procesos, capacidad, calidad, cadena de suministro |
| **Organization_Analyst** | Analista organizacional | Evaluar estructura, cultura, talento, liderazgo, comunicación |
| **Risk_Analyst** | Analista de riesgos | Identificar y evaluar riesgos estratégicos, operativos, financieros, de cumplimiento |
| **Master_Diagnosis_Orchestrator** | Orquestador maestro | Consolidar hallazgos, identificar causas raíz, priorizar problemas |
| **Strategy_Designer** | Diseñador de estrategia | Diseñar iniciativas de mejora y transformación |
| **AI_Transformation_Designer** | Diseñador de transformación AI | Evaluar oportunidades de automatización e IA en los procesos detectados |
| **Executive_Report_Generator** | Generador de informes | Producir el informe ejecutivo final en formato presentable |

### 2.2 Skills

| Skill | Descripción | Agente Propietario |
|---|---|---|
| **Profitability_Assessment** | Evalúa márgenes, rentabilidad por producto/cliente, estructura de costos | Financial_Analyst |
| **CashFlow_Assessment** | Evalúa ciclo de caja, capital de trabajo, proyecciones de liquidez | Financial_Analyst |
| **SevenS_Assessment** | Evalúa las 7S de McKinsey: Strategy, Structure, Systems, Skills, Style, Staff, Shared Values | Organization_Analyst |
| **Process_Assessment** | Evalúa madurez, eficiencia, cuellos de botella y estandarización de procesos | Operations_Analyst |
| **Business_Model_Assessment** | Evalúa modelo de negocio usando Canvas y patrones | Business_Model_Analyst |
| **Blue_Ocean_Assessment** | Evalúa potencial de innovación en valor usando marco de océano azul | Business_Model_Analyst |
| **JTBD_Assessment** | Evalúa Jobs To Be Done de los clientes para identificar necesidades profundas | Business_Model_Analyst |
| **Risk_Assessment** | Evalúa riesgos usando matriz de probabilidad e impacto | Risk_Analyst |

### 2.3 Bases de Conocimiento

| Base de Conocimiento | Contenido | Formato |
|---|---|---|
| **Business_Model_Patterns** | Catálogo de 55+ patrones de modelo de negocio (Osterwalder) | Knowledge Graph + JSON |
| **Financial_Patterns** | Ratios financieros, benchmarks por industria, señales de alerta | Knowledge Graph + CSV |
| **CashFlow_Patterns** | Patrones de ciclo de caja, estacionalidad, optimización de capital de trabajo | Knowledge Graph + JSON |
| **Sales_Patterns** | Metodologías de venta, funnel, KPI comerciales, benchmarks | Knowledge Graph + JSON |
| **Marketing_Patterns** | Canales, métricas de adquisición, retención, LTV, CAC | Knowledge Graph + JSON |
| **Customer_Patterns** | Segmentación, perfiles de cliente, journey maps, momentos de verdad | Knowledge Graph + JSON |
| **Process_Patterns** | Frameworks BPMN, Lean, Six Sigma, ISO 9001, madurez de procesos | Knowledge Graph + JSON |
| **Risk_Patterns** | Matrices de riesgo, taxonomías COSO, ISO 31000, heat maps | Knowledge Graph + JSON |
| **Organization_Patterns** | Estructuras organizacionales, culturas empresariales, modelos de liderazgo | Knowledge Graph + JSON |
| **Strategy_Patterns** | Marcos estratégicos: Porter, Blue Ocean, Ansoff, OKR, Balanced Scorecard | Knowledge Graph + JSON |

### 2.4 Flujo de Comunicación entre Agentes

```
Interview_Orchestrator
    → Business_Model_Analyst
    → Financial_Analyst
    → Operations_Analyst
    → Organization_Analyst
    → Risk_Analyst
        → Master_Diagnosis_Orchestrator
            → Strategy_Designer
            → AI_Transformation_Designer
                → Executive_Report_Generator
```

Los agentes de diagnóstico (Business_Model_Analyst a Risk_Analyst) pueden ejecutarse en paralelo si los inputs están disponibles.

---

## 3. Flujo General del Proceso

### 3.1 Diagrama de Flujo (Texto)

```
[INICIO] 
    │
    ▼
[E1. Descubrimiento Inicial] ───────────────────┐
    │                                             │
    ▼                                             │
[E2. Entrevista Empresarial]                     │
    │                                             │
    ├────────────────┬───────────────┬──────────┘
    │                │               │
    ▼                ▼               ▼
[E3. Modelo    [E4. Financiero] [E5. Operativo]
 de Negocio]                      
    │                │               │
    └────────┬───────┴───────┬───────┘
             │               │
             ▼               ▼
       [E6. Organizac.]  [E7. Riesgos]
             │               │
             └───────┬───────┘
                     │
                     ▼
            [E8. Consolidación]
                     │
                     ▼
            [E9. Causas Raíz]
                     │
                     ▼
            [E10. Priorización]
                     │
                     ▼
            [E11. Iniciativas]
                     │
                     ▼
            [E12. Roadmap]
                     │
                     ▼
            [E13. Informe Ejecutivo]
                     │
                     ▼
                  [FIN]
```

### 3.2 Reglas de Orquestación Globales

1. **Regla de continuidad**: Si una etapa falla por falta de datos, registrar como hallazgo "información insuficiente" y continuar. No bloquear el flujo.
2. **Regla de calidad mínima**: Cada etapa debe cumplir sus criterios de calidad antes de entregar output. Si no se cumplen, reejecutar con parámetros corregidos (máximo 3 intentos).
3. **Regla de versionado**: Cada output debe incluir versión (v1.0, v1.1, etc.), timestamp y agente responsable.
4. **Regla de trazabilidad**: Cada hallazgo debe poder trazarse a su fuente (entrevista, documento, análisis).
5. **Regla de confidencialidad**: Ningún agente debe persistir datos del cliente fuera del entorno seguro. Todos los outputs deben ser anonimizados para entrenamiento.

---

## 4. Etapa 1: Descubrimiento Inicial

### 4.1 Objetivo
Recopilar la información básica de la empresa cliente, el contexto de la industria y las expectativas del diagnóstico para alimentar todas las etapas posteriores.

### 4.2 Agente Responsable
**Interview_Orchestrator** (actúa como punto de entrada)

### 4.3 Skills Utilizadas
- Ninguna skill específica. El agente usa su capacidad de recolección de datos.

### 4.4 Frameworks Consultados
- Ficha de levantamiento de información básica
- Plantilla de perfil de empresa

### 4.5 Archivos de Conocimiento Utilizados
- Customer_Patterns (para segmentación industrial preliminar)
- Financial_Patterns (para benchmarks industriales iniciales)

### 4.6 Inputs Requeridos

| Input | Formato | Fuente | Obligatorio |
|---|---|---|---|
| Nombre / Razón social | String | Cliente | Sí |
| Industria / Sector | String (NAICS o similar) | Cliente | Sí |
| Año de fundación | Integer (YYYY) | Cliente | Sí |
| Número de empleados | Integer | Cliente | Sí |
| Facturación anual estimada | Float (USD) | Cliente | Sí |
| Ubicación geográfica | String | Cliente | No |
| Breve descripción del negocio | Texto libre (max 500 chars) | Cliente | Sí |
| Principales productos/servicios | Lista de strings | Cliente | Sí |
| Principales canales de venta | Lista de strings | Cliente | No |
| Objetivo del diagnóstico | Texto libre | Cliente | Sí |
| Documentos financieros disponibles | Lista de strings (EEFF, balances, etc.) | Cliente | Sí |

### 4.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `company_profile.json` | JSON | Perfil completo de la empresa |
| `industry_context.md` | Markdown | Contexto de la industria (tamaño, tendencias, benchmarks) |
| `diagnosis_scope.json` | JSON | Alcance del diagnóstico, objetivos, expectativas |
| `document_inventory.md` | Markdown | Inventario de documentos disponibles y faltantes |

### 4.8 Criterios de Calidad
- [ ] Todos los campos obligatorios están completos
- [ ] La industria está codificada en un estándar (NAICS o similar)
- [ ] Los datos financieros son consistentes (facturación >= 0, empleados >= 1)
- [ ] El objetivo del diagnóstico está redactado en lenguaje claro y medible
- [ ] El inventario de documentos identifica al menos qué EEFF están disponibles

### 4.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Faltan campos obligatorios | Rechazar input, solicitar completitud al cliente (máx. 2 reintentos) |
| Industria no reconocida | Solicitar aclaración con ejemplos de categorías estándar |
| Facturación inconsistente con empleados | Marcar alerta suave, continuar |
| Cliente no proporciona EEFF | Activar modo "diagnóstico sin EEFF" — usar estimaciones y ratios proxy |

### 4.10 Dependencias
- **Depende de**: Ninguna (etapa inicial)
- **Es requerido por**: E2, E3, E4 (inputs de perfil y contexto)
- **Tiempo estimado**: 15–30 min

---

## 5. Etapa 2: Entrevista Empresarial

### 5.1 Objetivo
Obtener información cualitativa profunda del líder de la PyME mediante una entrevista semi-estructurada que cubra todas las dimensiones del negocio.

### 5.2 Agente Responsable
**Interview_Orchestrator**

### 5.3 Skills Utilizadas
- Ninguna skill formal. El agente usa su motor de conducción de entrevistas.

### 5.4 Frameworks Consultados
- Guía de entrevista por dimensión (Modelo de Negocio, Finanzas, Operaciones, Organización, Riesgos)
- Pirámide de preguntas estratégicas (Cascada de preguntas: ¿Qué? → ¿Cómo? → ¿Por qué?)

### 5.5 Archivos de Conocimiento Utilizados
- Customer_Patterns
- Business_Model_Patterns
- Organization_Patterns

### 5.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 — Descubrimiento Inicial |
| `industry_context.md` | Markdown | E1 — Descubrimiento Inicial |
| Guía de entrevista predefinida | JSON | Sistema (plantilla interna) |

### 5.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `interview_transcript.md` | Markdown | Transcripción completa de la entrevista |
| `interview_notes_structured.json` | JSON | Notas estructuradas por dimensión (modelo, finanzas, ops, org, riesgos) |
| `pain_points_raw.json` | JSON | Lista de puntos de dolor mencionados textualmente por el cliente |
| `goals_and_aspirations.json` | JSON | Metas explícitas e implícitas del cliente |
| `org_context_summary.md` | Markdown | Resumen del contexto organizacional (antigüedad, estilo de liderazgo, dinámica) |

### 5.8 Criterios de Calidad
- [ ] Se cubrieron las 5 dimensiones de diagnóstico
- [ ] Se obtuvieron al menos 3 puntos de dolor explícitos
- [ ] Se identificaron al menos 2 metas u objetivos del cliente
- [ ] Las notas están etiquetadas por dimensión (Modelo, Finanzas, Operaciones, Organización, Riesgos)
- [ ] No hay contradicciones internas sin marcar

### 5.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Cliente no responde una dimensión | Marcar como "información no disponible", continuar |
| Cliente da respuestas contradictorias | Registrar ambas, marcar como "requiere verificación" |
| Cliente menciona urgencia explícita | Elevar prioridad de la dimensión correspondiente |
| Entrevista supera 90 min | Ofrecer pausa o sesión adicional |

### 5.10 Dependencias
- **Depende de**: E1 — Descubrimiento Inicial
- **Es requerido por**: E3, E4, E5, E6, E7 (todas las etapas de diagnóstico)
- **Tiempo estimado**: 45–90 min

---

## 6. Etapa 3: Diagnóstico de Modelo de Negocio

### 6.1 Objetivo
Evaluar la propuesta de valor, segmentos de cliente, canales, relaciones, fuentes de ingreso, recursos clave, actividades clave, socios clave y estructura de costos del modelo de negocio actual. Identificar brechas y oportunidades de innovación.

### 6.2 Agente Responsable
**Business_Model_Analyst**

### 6.3 Skills Utilizadas
- **Business_Model_Assessment**: Evaluación completa del modelo usando Business Model Canvas
- **Blue_Ocean_Assessment**: Evaluación de potencial de innovación en valor y diferenciación
- **JTBD_Assessment**: Identificación de los "jobs to be done" de los clientes objetivo

### 6.4 Frameworks Consultados
- Business Model Canvas (Osterwalder)
- Estrategia del Océano Azul (Kim & Mauborgne) — Marco de las 4 acciones (Eliminar, Reducir, Incrementar, Crear)
- Jobs To Be Done (Christensen)
- Value Proposition Canvas (Osterwalder)
- Lean Canvas (Maurya) (si aplica para startups)

### 6.5 Archivos de Conocimiento Utilizados
- **Business_Model_Patterns**: Para identificar patrones aplicables (Suscripción, Freemium, Long Tail, Multi-sided, etc.)
- **Customer_Patterns**: Para segmentación de clientes y perfiles
- **Sales_Patterns**: Para evaluación de canales de venta y distribución
- **Marketing_Patterns**: Para evaluación de canales de marketing y adquisición

### 6.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `industry_context.md` | Markdown | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |
| `goals_and_aspirations.json` | JSON | E2 |
| Catálogo de productos/servicios | Lista | Cliente (vía E1) |

### 6.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `bm_canvas.json` | JSON | Business Model Canvas completo (9 bloques) |
| `bm_assessment_report.md` | Markdown | Informe de evaluación del modelo de negocio |
| `bm_gaps.json` | JSON | Brechas identificadas entre el modelo actual y el deseado/óptimo |
| `bm_opportunities.json` | JSON | Oportunidades de innovación identificadas (Blue Ocean + JTBD) |
| `value_proposition_canvas.json` | JSON | Value Proposition Canvas (perfil de cliente + mapa de valor) |
| `bm_patron_matched.json` | JSON | Patrones de modelo de negocio identificados como aplicables |

### 6.8 Criterios de Calidad
- [ ] Los 9 bloques del Canvas están completos (sin "sin información")
- [ ] Se identificaron al menos 3 brechas significativas
- [ ] Se analizaron al menos 2 oportunidades de innovación
- [ ] Se aplicaron al menos 2 skills (BM_Assessment + una segunda)
- [ ] Los patrones sugeridos están justificados con evidencia del modelo actual
- [ ] Las oportunidades están priorizadas por impacto potencial (Alto/Medio/Bajo)

### 6.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| No hay información suficiente para un bloque del Canvas | Marcar como "No determinado", continuar |
| Se detectan múltiples segmentos de cliente | Crear un Canvas por segmento si hay diferencias significativas |
| El modelo actual es extremadamente simple (1 producto, 1 segmento) | No forzar complejidad, evaluar si necesita diversificación |
| Se identifica alta commoditización | Activar Blue_Ocean_Assessment para explorar diferenciación |
| Cliente reporta baja retención | Activar JTBD_Assessment para identificar necesidades no cubiertas |

### 6.10 Dependencias
- **Depende de**: E1, E2
- **Es requerido por**: E8 (Consolidación de Hallazgos)
- **Ejecución**: Puede ejecutarse en paralelo con E4, E5, E6, E7
- **Tiempo estimado**: 30–60 min

---

## 7. Etapa 4: Diagnóstico Financiero

### 7.1 Objetivo
Evaluar la salud financiera de la empresa en términos de rentabilidad, liquidez, solvencia, eficiencia y generación de caja. Identificar problemas financieros estructurales y oportunidades de optimización.

### 7.2 Agente Responsable
**Financial_Analyst**

### 7.3 Skills Utilizadas
- **Profitability_Assessment**: Análisis de márgenes (bruto, operativo, neto), rentabilidad por producto/cliente, punto de equilibrio
- **CashFlow_Assessment**: Análisis del ciclo de conversión de efectivo, capital de trabajo, proyecciones de flujo de caja

### 7.4 Frameworks Consultados
- Análisis de Ratios Financieros (Liquidez, Solvencia, Rentabilidad, Eficiencia)
- Análisis Vertical y Horizontal de EEFF
- Ciclo de Conversión de Efectivo (CCC)
- Análisis Dupont
- Análisis de Punto de Equilibrio
- Análisis de Tendencias (3+ años)

### 7.5 Archivos de Conocimiento Utilizados
- **Financial_Patterns**: Benchmarks por industria, ratios saludables, señales de alerta
- **CashFlow_Patterns**: Patrones de ciclo de caja, estacionalidad, optimización de capital de trabajo
- **Sales_Patterns**: Para correlacionar ingresos con esfuerzo comercial

### 7.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `industry_context.md` | Markdown | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |
| Balance General (últimos 2–3 años) | Excel/CSV | Cliente |
| Estado de Resultados (últimos 2–3 años) | Excel/CSV | Cliente |
| Flujo de Caja (si disponible, últimos 12 meses) | Excel/CSV | Cliente |
| Detalle de cuentas por cobrar y pagar (antigüedad) | Excel/CSV | Cliente (recomendado) |
| Presupuesto y/o proyecciones (si existe) | Excel/CSV | Cliente (opcional) |

### 7.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `financial_ratios.json` | JSON | Ratios calculados: liquidez, solvencia, rentabilidad, eficiencia, cobertura |
| `financial_trend_analysis.md` | Markdown | Análisis de tendencias (3 años si disponible) |
| `profitability_analysis.md` | Markdown | Desglose de rentabilidad, márgenes, punto de equilibrio |
| `cashflow_analysis.md` | Markdown | Análisis de flujo de caja, CCC, capital de trabajo |
| `financial_gaps.json` | JSON | Brechas financieras identificadas vs benchmarks |
| `financial_alerts.json` | JSON | Alertas financieras (señales de riesgo) |
| `financial_projections_scenarios.json` | JSON | Proyecciones bajo 3 escenarios: optimista, base, pesimista |

### 7.8 Criterios de Calidad
- [ ] Se calcularon al menos 6 ratios financieros clave (liquidez, solvencia, rentabilidad, eficiencia)
- [ ] Se compararon los ratios contra benchmarks de industria (vía Financial_Patterns)
- [ ] Se analizó el ciclo de conversión de efectivo (CCC) si hay datos de AR/AP
- [ ] Se identificaron al menos 3 alertas o brechas financieras
- [ ] Si hay 3+ años de datos, se incluyó análisis de tendencias
- [ ] Las proyecciones incluyen los 3 escenarios estándar

### 7.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| No hay EEFF disponibles | Activar modo "diagnóstico financiero estimado" — usar ratios proxy de la industria, entrevista y data transaccional disponible |
| Solo 1 año de EEFF | Realizar análisis vertical completo, omitir tendencias |
| Ratios muy por debajo del benchmark de industria | Marcar como "alerta roja", priorizar en E10 |
| CCC superior a 90 días | Activar análisis detallado de AR/AP, sugerir revisión de políticas de crédito |
| Margen neto negativo en 2+ años | Marcar como "alerta crítica de viabilidad" |
| Datos inconsistentes entre EEFF | Solicitar aclaración, marcar partidas como "no verificadas" |

### 7.10 Dependencias
- **Depende de**: E1, E2 (mínimo), documentos financieros del cliente
- **Es requerido por**: E8, E7 (Risk_Analyst usa outputs financieros)
- **Ejecución**: Puede ejecutarse en paralelo con E3, E5, E6
- **Tiempo estimado**: 45–90 min

---

## 8. Etapa 5: Diagnóstico Operativo

### 8.1 Objetivo
Evaluar la eficiencia, capacidad, calidad y madurez de los procesos operativos de la empresa, incluyendo producción/servicio, cadena de suministro, gestión de inventarios y control de calidad.

### 8.2 Agente Responsable
**Operations_Analyst**

### 8.3 Skills Utilizadas
- **Process_Assessment**: Evaluación de madurez de procesos, identificación de cuellos de botella, waste (desperdicios)

### 8.4 Frameworks Consultados
- BPMN (Business Process Model and Notation) — para mapeo de procesos
- Lean Manufacturing / Lean Service — para identificación de mudas (waste)
- Six Sigma DMAIC — para análisis de calidad y variabilidad
- ISO 9001 — para evaluación de sistema de gestión de calidad
- SCOR Model — para cadena de suministro
- Nivel de Madurez de Procesos (1–5: Inicial, Gestionado, Definido, Medido, Optimizado)

### 8.5 Archivos de Conocimiento Utilizados
- **Process_Patterns**: Patrones de procesos por industria, mejores prácticas, KPI operativos
- **Sales_Patterns**: Para correlacionar capacidad operativa con demanda comercial

### 8.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `industry_context.md` | Markdown | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |
| Descripción de procesos clave | Texto / Diagrama | Cliente |
| Indicadores operativos (si existen) | CSV / JSON | Cliente |
| Layout de instalaciones / mapa de flujo (si aplica) | Imagen / PDF | Cliente (opcional) |
| Datos de capacidad y utilización | CSV | Cliente (opcional) |

### 8.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `process_map_bpmn.json` | JSON | Mapa de procesos clave en notación BPMN simplificada |
| `process_maturity_matrix.json` | JSON | Matriz de madurez por proceso (1–5) |
| `bottleneck_analysis.md` | Markdown | Identificación de cuellos de botella y restricciones |
| `waste_identification.json` | JSON | Desperdicios identificados (Lean: 7+1 mudas) |
| `quality_assessment.md` | Markdown | Evaluación de calidad (tasas de defecto, reclamos, devoluciones) |
| `operational_kpi.json` | JSON | KPI operativos calculados o estimados |
| `operations_gaps.json` | JSON | Brechas operativas identificadas |
| `capacity_analysis.md` | Markdown | Análisis de capacidad utilizada vs disponible |

### 8.8 Criterios de Calidad
- [ ] Se mapearon al menos 3 procesos clave (core business)
- [ ] Se asignó nivel de madurez a cada proceso mapeado
- [ ] Se identificaron al menos 2 cuellos de botella o restricciones
- [ ] Se identificaron al menos 3 fuentes de desperdicio (mudas)
- [ ] Se calcularon al menos 3 KPI operativos (ej. capacidad, eficiencia, calidad)
- [ ] Las brechas identificadas están vinculadas a puntos de dolor del cliente (de E2)

### 8.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Cliente no proporciona datos de procesos | Mapear procesos basado en entrevista, marcar como "estimado" |
| Menos de 5 empleados | Evaluación simplificada (los procesos son informales por naturaleza) |
| Se detecta proceso con madurez nivel 1 (Inicial) | Priorizar estandarización en E11 |
| Tasa de defecto/reclamo > 10% | Marcar como "alerta de calidad" |
| Capacidad utilizada > 90% sostenido | Marcar como "riesgo de saturación", evaluar necesidad de expansión |
| Capacidad utilizada < 40% | Marcar como "capacidad ociosa", evaluar reducción de costos fijos |

### 8.10 Dependencias
- **Depende de**: E1, E2
- **Es requerido por**: E8, E7 (para riesgos operativos)
- **Ejecución**: Puede ejecutarse en paralelo con E3, E4, E6
- **Tiempo estimado**: 30–60 min

---

## 9. Etapa 6: Diagnóstico Organizacional

### 9.1 Objetivo
Evaluar la estructura organizacional, la cultura, el talento, el liderazgo y los sistemas de gestión de la empresa. Identificar brechas que afectan la ejecución estratégica y el clima laboral.

### 9.2 Agente Responsable
**Organization_Analyst**

### 9.3 Skills Utilizadas
- **SevenS_Assessment**: Evaluación de las 7S de McKinsey (Strategy, Structure, Systems, Skills, Style, Staff, Shared Values)

### 9.4 Frameworks Consultados
- McKinsey 7S Framework
- Modelo de Cultura Organizacional (Cameron & Quinn — Competing Values Framework)
- Modelo de Liderazgo Situacional (Hersey-Blanchard)
- Organizational Design (Galbraith Star Model)
- Niveles de Desarrollo Organizacional (Laloux)
- OKR / KPI de gestión del talento

### 9.5 Archivos de Conocimiento Utilizados
- **Organization_Patterns**: Estructuras organizacionales (funcional, divisional, matricial, plana, etc.), tipos de cultura
- **Strategy_Patterns**: Para alinear estructura con estrategia

### 9.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `industry_context.md` | Markdown | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |
| `goals_and_aspirations.json` | JSON | E2 |
| Organigrama (si existe) | Imagen / PDF / JSON | Cliente |
| Descripción de roles y responsabilidades | Texto / CSV | Cliente (opcional) |
| Indicadores de RRHH (rotación, clima, etc.) | CSV | Cliente (opcional) |

### 9.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `seven_s_assessment.json` | JSON | Evaluación de las 7S con puntuación (1–5) por dimensión |
| `seven_s_alignment_matrix.md` | Markdown | Matriz de alineación entre las 7S |
| `org_structure_analysis.md` | Markdown | Análisis de la estructura actual y recomendaciones |
| `culture_assessment.md` | Markdown | Evaluación cultural (tipo actual vs deseado) |
| `talent_gap_analysis.json` | JSON | Brechas de talento y habilidades críticas |
| `leadership_profile.json` | JSON | Perfil de liderazgo del fundador/CEO |
| `org_gaps.json` | JSON | Brechas organizacionales identificadas |

### 9.8 Criterios de Calidad
- [ ] Se evaluaron las 7S con puntuación individual y justificación
- [ ] Se identificaron al menos 3 brechas de alineamiento entre las 7S
- [ ] Se analizó la estructura organizacional (formal o inferida)
- [ ] Se identificó el perfil de liderazgo del fundador/CEO
- [ ] Las brechas están vinculadas a puntos de dolor del cliente (de E2)

### 9.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| No hay organigrama formal | Inferir estructura de la entrevista, marcar como "estructura informal" |
| Empresa < 10 empleados | Las 7S se evalúan de forma simplificada (estructura plana, estilo informal) |
| Rotación de personal > 20% anual | Marcar como "alerta de retención", profundizar en cultura |
| Fundador concentra todas las decisiones | Marcar como "centralización crítica", evaluar para E11 |
| Se detecta baja alineación Strategy ↔ Structure | Marcar como "brecha estratégico-estructural" |
| Puntuación 7S < 2.5 en 3+ dimensiones | Marcar como "alerta organizacional severa" |

### 9.10 Dependencias
- **Depende de**: E1, E2
- **Es requerido por**: E8
- **Ejecución**: Puede ejecutarse en paralelo con E3, E4, E5
- **Tiempo estimado**: 30–60 min

---

## 10. Etapa 7: Diagnóstico de Riesgos

### 10.1 Objetivo
Identificar, evaluar y priorizar los riesgos estratégicos, operativos, financieros y de cumplimiento que enfrenta la empresa, utilizando metodologías de gestión de riesgos empresariales.

### 10.2 Agente Responsable
**Risk_Analyst**

### 10.3 Skills Utilizadas
- **Risk_Assessment**: Evaluación cualitativa y cuantitativa de riesgos usando matriz de probabilidad e impacto

### 10.4 Frameworks Consultados
- ISO 31000 — Gestión de Riesgos
- COSO ERM 2017 — Enterprise Risk Management
- Matriz de Probabilidad e Impacto (5×5)
- Risk Heat Map
- Análisis FODA (extendido a riesgos)

### 10.5 Archivos de Conocimiento Utilizados
- **Risk_Patterns**: Taxonomía de riesgos por industria, patrones de materialización, estrategias de mitigación
- **Financial_Patterns**: Para riesgos financieros
- **Process_Patterns**: Para riesgos operativos

### 10.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `industry_context.md` | Markdown | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |
| `financial_alerts.json` | JSON | E4 (si ya está disponible) |
| `operations_gaps.json` | JSON | E5 (si ya está disponible) |
| `org_gaps.json` | JSON | E6 (si ya está disponible) |
| `bm_gaps.json` | JSON | E3 (si ya está disponible) |

### 10.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `risk_matrix.json` | JSON | Matriz de riesgos (categoría, probabilidad, impacto, nivel de riesgo) |
| `risk_heatmap.md` | Markdown | Mapa de calor de riesgos |
| `risk_report.md` | Markdown | Informe detallado de riesgos con análisis de causas y consecuencias |
| `top_risks.json` | JSON | Top 10 riesgos priorizados por nivel de riesgo = P × I |
| `risk_treatment_suggestions.json` | JSON | Sugerencias de tratamiento (evitar, reducir, transferir, aceptar) |
| `compliance_gaps.json` | JSON | Brechas de cumplimiento regulatorio/laboral/tributario |

### 10.8 Criterios de Calidad
- [ ] Se identificaron al menos 8 riesgos distribuidos en 3+ categorías
- [ ] Cada riesgo tiene asignada probabilidad (1–5) e impacto (1–5)
- [ ] Se calculó nivel de riesgo (P × I) para todos los riesgos
- [ ] Se generó un ranking de Top 10 riesgos
- [ ] Se incluyó al menos 1 sugerencia de tratamiento por riesgo Top 5
- [ ] Los riesgos están vinculados a hallazgos de etapas previas (E2–E6)

### 10.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Riesgo con P × I ≥ 15 | Marcar como "riesgo crítico", incluir en Top 5 obligatorio |
| Riesgo con P × I ≥ 20 | Marcar como "riesgo severo", requiere acción inmediata en E11 |
| Se detecta riesgo de cumplimiento normativo | Priorizar como crítico independientemente del score |
| No hay información para evaluar un riesgo | Marcar como "riesgo no evaluado por falta de datos" |
| Más de 3 riesgos críticos | Activar modo "alerta sistémica" en E8 |

### 10.10 Dependencias
- **Depende de**: E1, E2 (mínimo). Los outputs de E3–E6 mejoran la calidad pero no son bloqueantes.
- **Es requerido por**: E8
- **Ejecución**: Puede iniciarse con E1+E2; se enriquece cuando E3–E6 estén disponibles.
- **Tiempo estimado**: 30–60 min

---

## 11. Etapa 8: Consolidación de Hallazgos

### 11.1 Objetivo
Consolidar, estructurar y unificar todos los hallazgos generados por las etapas de diagnóstico (E3–E7) en un repositorio único, categorizado y trazable, eliminando duplicaciones y resolviendo contradicciones.

### 11.2 Agente Responsable
**Master_Diagnosis_Orchestrator**

### 11.3 Skills Utilizadas
- Ninguna skill específica. El agente orquesta la consolidación usando reglas de fusión de datos.

### 11.4 Frameworks Consultados
- Taxonomía unificada de problemas empresariales
- Matriz de consistencia cruzada
- Reglas de deduplicación y resolución de conflictos

### 11.5 Archivos de Conocimiento Utilizados
- Todos los patrones (para validación cruzada de hallazgos)

### 11.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| Todos los outputs de E3–E7 | Varios | Business_Model_Analyst, Financial_Analyst, Operations_Analyst, Organization_Analyst, Risk_Analyst |
| `company_profile.json` | JSON | E1 |
| `interview_notes_structured.json` | JSON | E2 |
| `pain_points_raw.json` | JSON | E2 |

### 11.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `consolidated_findings.json` | JSON | Todos los hallazgos unificados con ID único, categoría, fuente, severidad |
| `findings_cross_reference_matrix.md` | Markdown | Matriz de referencia cruzada (hallazgo ↔ fuente) |
| `contradictions_log.json` | JSON | Contradicciones detectadas entre hallazgos y cómo se resolvieron |
| `findings_summary.md` | Markdown | Resumen ejecutivo de hallazgos por dimensión |
| `severity_distribution.json` | JSON | Distribución de hallazgos por severidad (Crítica, Alta, Media, Baja) |

### 11.8 Criterios de Calidad
- [ ] Todos los hallazgos de E3–E7 están incluidos
- [ ] Cada hallazgo tiene un ID único, categoría, severidad y fuente
- [ ] No hay hallazgos duplicados
- [ ] Las contradicciones están documentadas y resueltas
- [ ] Al menos 1 hallazgo por dimensión (Modelo, Finanzas, Ops, Org, Riesgos)
- [ ] La severidad está calibrada (no más del 30% de hallazgos como "Crítica")

### 11.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Dos hallazgos contradictorios de distintas fuentes | Mantener ambos, documentar contradicción, resolver por mayoría de evidencia |
| Hallazgo duplicado | Fusionar, conservar el ID de mayor severidad |
| Hallazgo sin fuente trazable | Marcar como "no verificado", relegar a severidad "Baja" |
| 3+ hallazgos críticos en misma categoría | Crear hallazgo compuesto "Problema sistémico en [categoría]" |
| Categoría sin hallazgos | Registrar como "dimensión sin hallazgos significativos" |

### 11.10 Dependencias
- **Depende de**: E3, E4, E5, E6, E7 (al menos 3 de 5 deben estar completos)
- **Es requerido por**: E9
- **Tiempo estimado**: 20–40 min

---

## 12. Etapa 9: Identificación de Causas Raíz

### 12.1 Objetivo
Aplicar análisis de causa raíz (RCA) a los hallazgos consolidados para identificar las causas fundamentales de los problemas, distinguiendo síntomas de causas genuinas.

### 12.2 Agente Responsable
**Master_Diagnosis_Orchestrator**

### 12.3 Skills Utilizadas
- Ninguna skill específica. El agente aplica técnicas de RCA estructuradas.

### 12.4 Frameworks Consultados
- **5 Whys** (Toyota Production System)
- **Diagrama de Ishikawa** (Espina de Pescado / Causa-Efecto)
- **Árbol de Problemas** (Problem Tree Analysis)
- **Análisis de Pareto** (80/20)
- **Matriz Causa-Efecto**

### 12.5 Archivos de Conocimiento Utilizados
- **Strategy_Patterns**: Para vincular causas raíz a problemas estratégicos recurrentes
- **Organization_Patterns**: Para causas raíz organizacionales típicas

### 12.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `consolidated_findings.json` | JSON | E8 |
| `findings_cross_reference_matrix.md` | Markdown | E8 |
| `contradictions_log.json` | JSON | E8 |

### 12.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `root_cause_analysis.json` | JSON | Análisis de causa raíz: hallazgo → causa inmediata → causa raíz → categoría RCA |
| `fishbone_diagram.json` | JSON | Diagrama de Ishikawa estructurado (categorías + causas) |
| `root_cause_pareto.json` | JSON | Análisis de Pareto de causas raíz (frecuencia de aparición) |
| `symptom_vs_root_map.md` | Markdown | Mapa de síntomas vs causas raíz |
| `rca_summary.md` | Markdown | Resumen de causas raíz identificadas |

### 12.8 Criterios de Calidad
- [ ] Cada hallazgo crítico/alto tiene al menos un análisis 5 Whys completo
- [ ] Se identificaron al menos 3 causas raíz distintas
- [ ] Las causas raíz están categorizadas (Estratégica, Financiera, Operativa, Organizacional, Externa)
- [ ] Los síntomas están claramente diferenciados de las causas raíz
- [ ] El análisis de Pareto muestra al menos 2 causas raíz que explican >60% de los hallazgos

### 12.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Después de 5 Whys se llega a causa externa no controlable | Registrar como "restricción del entorno", sugerir adaptación |
| Una misma causa raíz explica 3+ hallazgos | Marcar como "causa raíz pivote" — priorizar en E10 |
| No se puede determinar causa raíz | Marcar como "requiere investigación adicional" |
| Síntoma parece ser causa raíz | Aplicar un Why adicional para verificar profundidad |
| Causa raíz identificada como "falta de capital" | Validar con E4, puede ser síntoma de problemas más profundos |

### 12.10 Dependencias
- **Depende de**: E8
- **Es requerido por**: E10
- **Tiempo estimado**: 30–60 min

---

## 13. Etapa 10: Priorización de Problemas

### 13.1 Objetivo
Priorizar los problemas y causas raíz identificados usando criterios de impacto en el negocio, urgencia, esfuerzo de resolución y alineación con objetivos del cliente.

### 13.2 Agente Responsable
**Master_Diagnosis_Orchestrator**

### 13.3 Skills Utilizadas
- Ninguna skill específica. El agente aplica marcos de priorización.

### 13.4 Frameworks Consultados
- **Matriz Impacto vs Esfuerzo** (Impact/Effort Matrix)
- **Matriz Urgencia vs Importancia** (Eisenhower Matrix)
- **Método MoSCoW** (Must have, Should have, Could have, Won't have)
- **RICE Scoring** (Reach, Impact, Confidence, Effort)
- **Algoritmo de priorización ponderada**

### 13.5 Archivos de Conocimiento Utilizados
- **Strategy_Patterns**: Para alinear prioridades con objetivos estratégicos
- **Financial_Patterns**: Para cuantificar impacto financiero potencial

### 13.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `root_cause_analysis.json` | JSON | E9 |
| `root_cause_pareto.json` | JSON | E9 |
| `rca_summary.md` | Markdown | E9 |
| `consolidated_findings.json` | JSON | E8 |
| `goals_and_aspirations.json` | JSON | E2 |

### 13.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `prioritized_problems.json` | JSON | Problemas priorizados con scoring (RICE o impacto/esfuerzo) |
| `impact_effort_matrix.json` | JSON | Matriz impacto × esfuerzo (Quick Wins, Major Projects, Fill-ins, Thankless) |
| `prioritization_rationale.md` | Markdown | Justificación de la priorización para cada problema Top 10 |
| `top_problems_summary.md` | Markdown | Resumen del Top 10 de problemas a resolver |

### 13.8 Criterios de Calidad
- [ ] Se priorizaron al menos 10 problemas/causas raíz
- [ ] Cada problema tiene scoring (cuantitativo o cualitativo con justificación)
- [ ] Los Top 5 problemas están alineados con los objetivos del cliente (de E2)
- [ ] La matriz impacto × esfuerzo clasifica cada problema en un cuadrante
- [ ] Se considera tanto el impacto financiero como el estratégico

### 13.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Problema es causa raíz pivote (de E9) | Priorizar automáticamente en Top 3 |
| Problema alineado con objetivo explícito del cliente | Aumentar prioridad en 1 nivel |
| Problema con impacto financiero cuantificable > 10% de ingresos | Priorizar como "Must have" |
| Quick Wins (alto impacto, bajo esfuerzo) | Marcar para implementación inmediata en E11 |
| Problema sin solución conocida | Marcar como "requiere investigación", prioridad condicional |
| Problema con riesgo crítico asociado (de E7) | Priorizar en Top 5 |

### 13.10 Dependencias
- **Depende de**: E9
- **Es requerido por**: E11, E12
- **Tiempo estimado**: 20–40 min

---

## 14. Etapa 11: Diseño de Iniciativas

### 14.1 Objetivo
Diseñar iniciativas concretas de mejora y transformación para cada problema priorizado, incluyendo objetivos, alcance, recursos estimados, plazo y métricas de éxito. Incluir evaluación de oportunidades de automatización e IA.

### 14.2 Agentes Responsables
- **Strategy_Designer**: Diseño de iniciativas estratégicas, operativas, financieras, organizacionales
- **AI_Transformation_Designer**: Diseño de iniciativas de automatización, IA y transformación digital

### 14.3 Skills Utilizadas
- Ninguna skill específica formal. Los agentes usan su capacidad de diseño de soluciones.

### 14.4 Frameworks Consultados
- OKR (Objectives and Key Results)
- SMART Goals
- Design Thinking
- Lean Startup (Build-Measure-Learn)
- AI Opportunity Canvas
- Automation Potential Assessment
- Business Case Canvas

### 14.5 Archivos de Conocimiento Utilizados
- **Strategy_Patterns**: Marcos estratégicos para diseño de iniciativas
- **Financial_Patterns**: Para estimar ROI de iniciativas
- **Process_Patterns**: Para rediseño de procesos
- **Organization_Patterns**: Para diseño de cambios organizacionales
- **Risk_Patterns**: Para mitigación de riesgos en iniciativas

### 14.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `prioritized_problems.json` | JSON | E10 |
| `impact_effort_matrix.json` | JSON | E10 |
| `top_problems_summary.md` | Markdown | E10 |
| `consolidated_findings.json` | JSON | E8 |
| `root_cause_analysis.json` | JSON | E9 |
| `company_profile.json` | JSON | E1 |
| `goals_and_aspirations.json` | JSON | E2 |

### 14.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `initiatives_catalog.json` | JSON | Catálogo de iniciativas con: ID, nombre, problema asociado, descripción, objetivos, alcance, recursos, plazo, KPI, ROI estimado |
| `ai_opportunities.json` | JSON | Oportunidades de IA/automatización identificadas (AI_Transformation_Designer) |
| `initiative_business_cases.json` | JSON | Business case por iniciativa (costos, beneficios, ROI, payback) |
| `initiative_dependencies.json` | JSON | Mapa de dependencias entre iniciativas |
| `initiative_summary.md` | Markdown | Resumen ejecutivo de iniciativas propuestas |

### 14.8 Criterios de Calidad
- [ ] Al menos 1 iniciativa por problema del Top 5 (E10)
- [ ] Cada iniciativa tiene: objetivo SMART, alcance definido, recursos estimados, plazo, KPI de éxito
- [ ] Las iniciativas Quick Win (alto impacto, bajo esfuerzo) tienen plazo ≤ 3 meses
- [ ] Las iniciativas de IA están justificadas con datos de procesos (E5)
- [ ] El business case incluye al menos ROI o payback estimado
- [ ] Las dependencias entre iniciativas están documentadas

### 14.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Iniciativa resuelve múltiples problemas | Marcar como "iniciativa multiplicadora", priorizar en roadmap |
| Iniciativa requiere inversión > 10% de facturación | Requerir validación financiera detallada |
| Iniciativa de IA sin data disponible | Marcar como "pre-requisito: habilitar datos", diferir |
| Dos iniciativas son mutuamente excluyentes | Registrar conflicto, recomendar selección basada en ROI |
| Iniciativa tiene payback > 24 meses | Marcar como "iniciativa estratégica de largo plazo" |
| Oportunidad de IA con alta factibilidad y alto impacto | Marcar como "AI Quick Win", priorizar en roadmap |

### 14.10 Dependencias
- **Depende de**: E10
- **Es requerido por**: E12, E13
- **Tiempo estimado**: 45–90 min

---

## 15. Etapa 12: Diseño de Roadmap

### 15.1 Objetivo
Secuenciar las iniciativas aprobadas en un roadmap temporal con fases, hitos, dependencias y asignación de recursos, balanceando Quick Wins con proyectos estratégicos.

### 15.2 Agente Responsable
**Strategy_Designer**

### 15.3 Skills Utilizadas
- Ninguna skill específica. El agente usa su capacidad de planificación estratégica.

### 15.4 Frameworks Consultados
- Roadmapping (3 horizontes: Corto, Mediano, Largo plazo)
- Gestión del Cambio (Kotter 8-step / ADKAR)
- Gestión de Portafolio de Proyectos (PMI)
- Critical Path Method (CPM)
- OKR Timeline

### 15.5 Archivos de Conocimiento Utilizados
- **Strategy_Patterns**: Para alineación estratégica del roadmap
- **Financial_Patterns**: Para planificación de inversiones

### 15.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `initiatives_catalog.json` | JSON | E11 |
| `initiative_dependencies.json` | JSON | E11 |
| `initiative_business_cases.json` | JSON | E11 |
| `ai_opportunities.json` | JSON | E11 |
| `prioritized_problems.json` | JSON | E10 |
| `company_profile.json` | JSON | E1 |
| `goals_and_aspirations.json` | JSON | E2 |

### 15.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `roadmap.json` | JSON | Roadmap con fases (corto/medio/largo), iniciativas por fase, hitos, fechas estimadas |
| `roadmap_gantt.md` | Markdown | Diagrama de Gantt textual del roadmap |
| `roadmap_phases_detail.md` | Markdown | Detalle por fase: objetivos, iniciativas, recursos, RACI, dependencias |
| `resource_allocation.json` | JSON | Asignación estimada de recursos por iniciativa y fase |
| `change_management_plan.md` | Markdown | Plan de gestión del cambio para iniciativas organizacionales |
| `risk_burndown.json` | JSON | Proyección de reducción de riesgo por iniciativa aplicada |

### 15.8 Criterios de Calidad
- [ ] El roadmap tiene 3 horizontes definidos (0–3, 3–9, 9–24 meses)
- [ ] Quick Wins están en Fase 1 (0–3 meses)
- [ ] Las dependencias entre iniciativas están respetadas en la secuencia
- [ ] Cada fase tiene hitos medibles
- [ ] La asignación de recursos es realista (no sobrecarga)
- [ ] El plan de cambio organizacional está incluido para iniciativas que afectan estructura/cultura

### 15.9 Reglas de Decisión
| Condición | Acción |
|---|---|
| Iniciativa depende de otra no planificada | Reprogramar, no permitir dependencias no resueltas |
| Quick Win no está en Fase 1 | Revisar priorización, debe estar en primeros 3 meses |
| Más de 3 iniciativas simultáneas en misma área | Espaciar para evitar sobrecarga operativa |
| Iniciativa con payback < 6 meses | Priorizar en Fase 1 |
| Iniciativa requiere cambio cultural significativo | Incluir plan de change management, extender timeline |
| Roadmap excede capacidad de la empresa | Reducir alcance, recomendar contratación o consultoría |

### 15.10 Dependencias
- **Depende de**: E11
- **Es requerido por**: E13
- **Tiempo estimado**: 30–60 min

---

## 16. Etapa 13: Generación de Informe Ejecutivo

### 16.1 Objetivo
Sintetizar todos los hallazgos, análisis, iniciativas y roadmap en un informe ejecutivo profesional, listo para presentar al cliente, estructurado para facilitar la toma de decisiones.

### 16.2 Agente Responsable
**Executive_Report_Generator**

### 16.3 Skills Utilizadas
- Ninguna skill específica. El agente usa su motor de generación de informes.

### 16.4 Frameworks Consultados
- Estructura de informe ejecutivo (Resumen → Metodología → Hallazgos → Causas → Iniciativas → Roadmap → Anexos)
- Pirámide de Minto (recomendación → argumentos → datos)
- Principios de visualización de datos (Tufte / Few)

### 16.5 Archivos de Conocimiento Utilizados
- **Strategy_Patterns**: Para lenguaje y framing estratégico
- Todos los outputs de etapas previas como fuentes de contenido

### 16.6 Inputs Requeridos

| Input | Formato | Fuente |
|---|---|---|
| `company_profile.json` | JSON | E1 |
| `diagnosis_scope.json` | JSON | E1 |
| `consolidated_findings.json` | JSON | E8 |
| `rca_summary.md` | Markdown | E9 |
| `top_problems_summary.md` | Markdown | E10 |
| `initiatives_catalog.json` | JSON | E11 |
| `roadmap.json` | JSON | E12 |
| `roadmap_phases_detail.md` | Markdown | E12 |
| `change_management_plan.md` | Markdown | E12 |
| Todos los reportes de diagnóstico (E3–E7) | Varios | Agentes de diagnóstico |

### 16.7 Outputs Generados

| Output | Formato | Descripción |
|---|---|---|
| `executive_report.md` | Markdown | Informe ejecutivo completo (15–20 páginas) |
| `executive_summary.md` | Markdown | Resumen ejecutivo (1–2 páginas) para alta dirección |
| `presentation_deck.md` | Markdown | Presentación estilo PPT narrativa (10–15 slides) |
| `action_plan_summary.md` | Markdown | Plan de acción resumido (1 página) |
| `dashboard_kpi.json` | JSON | KPIs clave para seguimiento de iniciativas |

### 16.8 Estructura del Informe (`executive_report.md`)

```
1. Resumen Ejecutivo
   1.1 Contexto del diagnóstico
   1.2 Principales hallazgos (Top 5)
   1.3 Recomendaciones clave
   
2. Metodología
   2.1 Agentes y skills aplicados
   2.2 Fuentes de información
   2.3 Limitaciones y supuestos

3. Diagnóstico por Dimensión
   3.1 Modelo de Negocio
   3.2 Situación Financiera
   3.3 Operaciones y Procesos
   3.4 Organización y Talento
   3.5 Riesgos

4. Causas Raíz Identificadas
   4.1 Árbol de causas
   4.2 Priorización

5. Plan de Transformación
   5.1 Iniciativas propuestas
   5.2 Business case
   5.3 Roadmap (corto, mediano, largo plazo)
   5.4 Gestión del cambio

6. Próximos Pasos
   6.1 Acciones inmediatas (siguientes 30 días)
   6.2 Hitos críticos
   6.3 Recomendaciones finales

Anexos
   A. Detalle de ratios financieros
   B. Business Model Canvas completo
   C. Matriz de riesgos detallada
   D. Fichas de iniciativas
   E. Glosario
```

### 16.9 Criterios de Calidad
- [ ] El informe cubre las 5 dimensiones de diagnóstico
- [ ] El resumen ejecutivo no excede 2 páginas y captura los hallazgos críticos
- [ ] Todas las recomendaciones están vinculadas a hallazgos y causas raíz
- [ ] El roadmap es accionable con fechas y responsables
- [ ] El lenguaje es profesional pero accesible para un dueño de PyME
- [ ] Los datos financieros y KPIs están correctamente formateados
- [ ] La presentación sigue una narrativa lógica: problema → causa → solución → plan

### 16.10 Reglas de Decisión
| Condición | Acción |
|---|---|
| Informe supera 25 páginas | Generar versión ejecutable (15 páginas) más anexos separados |
| Cliente prefiere español/inglés | Generar en idioma configurado en company_profile |
| Se detecta información sensible | Incluir cláusula de confidencialidad al inicio |
| El cliente solicitó formato específico (PPT, PDF, Word) | Generar en el formato base y activar convertidor post-proceso |
| Hay más de 10 iniciativas | Incluir solo Top 10 en el cuerpo, el resto en anexos |

### 16.11 Dependencias
- **Depende de**: E1, E8, E9, E10, E11, E12 (todas las etapas previas deben estar completas)
- **Es requerido por**: Ninguna (etapa terminal)
- **Tiempo estimado**: 45–90 min

---

## 17. Apéndices

### A. Formato de IDs de Hallazgos

```
H-{Etapa}-{Número secuencial}-{Versión}
Ejemplo: H-BM-003-v1.0
         H-FI-012-v1.2
         H-OP-007-v1.0
         H-OR-002-v1.1
         H-RI-005-v1.0
         H-RC-001-v1.0 (Raíz)
         H-IN-004-v1.0 (Iniciativa)
```

### B. Escala de Severidad

| Nivel | Valor | Definición | Plazo de Acción |
|---|---|---|---|
| Crítica | 5 | Amenaza la viabilidad/continuidad del negocio | Inmediato (0–30 días) |
| Alta | 4 | Impacto significativo en resultados o competitividad | Corto plazo (30–90 días) |
| Media | 3 | Impacto moderado, eficiencia o crecimiento | Mediano plazo (90–180 días) |
| Baja | 2 | Oportunidad de mejora menor | Largo plazo (180+ días) |
| Informativa | 1 | Observación, no requiere acción | Sin plazo |

### C. Escala de Madurez de Procesos

| Nivel | Nombre | Descripción |
|---|---|---|
| 1 | Inicial | Procesos impredecibles, no estandarizados, dependientes de personas |
| 2 | Gestionado | Procesos planificados, ejecutados y controlados a nivel de proyecto |
| 3 | Definido | Procesos estandarizados en toda la organización |
| 4 | Medido | Procesos con métricas cuantitativas de desempeño |
| 5 | Optimizado | Procesos con mejora continua basada en datos |

### D. Plantilla de Business Case para Iniciativas

```
ID: IN-{Número}-v1.0
Nombre: {Nombre de la iniciativa}
Problema asociado: {ID del problema en E10}
Descripción: {3–5 líneas}
Objetivo SMART: {Específico, Medible, Alcanzable, Relevante, con Tiempo}
Alcance: {Qué incluye / qué excluye}
Recursos estimados:
  - Humanos: {roles y dedicación}
  - Tecnológicos: {herramientas necesarias}
  - Financieros: {inversión estimada}
Plazo estimado: {días o meses}
KPI de éxito: {métrica objetivo}
ROI estimado: {% o ratio}
Payback: {meses}
Dependencias: {IDs de iniciativas de las que depende}
Riesgos: {principales riesgos de la iniciativa}

Alineación estratégica:
  - Objetivo del cliente: {de E2}
  - Causa raíz abordada: {de E9}
```

### E. Protocolo de Calidad y Validación Cruzada

Cada etapa debe ejecutar el siguiente protocolo antes de liberar sus outputs:

1. **Auto-verificación**: El agente responsable verifica que todos los criterios de calidad de la etapa se cumplen.
2. **Validación de formato**: Los outputs cumplen con los esquemas JSON definidos (si aplica).
3. **Trazabilidad**: Cada hallazgo, ratio o conclusión tiene una fuente identificable.
4. **Consistencia interna**: No hay contradicciones dentro de los outputs de la etapa.
5. **Registro**: Se genera un entry en el log de ejecución con timestamp y versión.

Si la validación falla, se registra el error y se reejecuta la etapa (máximo 3 intentos). Si persiste, se escala al operador humano.

### F. Diagrama de Dependencias entre Etapas

```
E1 ──► E2 ──┬──► E3 ──┐
             ├──► E4 ──┤
             ├──► E5 ──┤
             ├──► E6 ──┤
             └──► E7 ──┤
                       ▼
                      E8 ──► E9 ──► E10 ──┬──► E11 ──► E12 ──► E13
                                           │
                                           └──► E11.1 (AI_Transformation)
                                                     │
                                                     └──► E12 ──► E13
```

### G. Lista de Verificación de Pre-ejecución

Antes de iniciar el playbook, verificar:

- [ ] Agentes disponibles y autenticados (todos los 10)
- [ ] Skills registradas en el catálogo (todas las 8)
- [ ] Bases de conocimiento cargadas (todas las 10)
- [ ] Canal de comunicación con cliente operativo
- [ ] Cliente ha firmado consentimiento de datos
- [ ] Plantillas de output disponibles (JSON schemas)
- [ ] Límites de tiempo configurados por etapa
- [ ] Modo de ejecución: Full / Solo diagnóstico / Solo diseño

### H. Modos de Ejecución

| Modo | Etapas Incluidas | Tiempo Estimado | Uso |
|---|---|---|---|
| **Full** | E1 → E13 | 6–12 horas | Diagnóstico completo con plan de transformación |
| **Fast Track** | E1, E2, E3*, E4*, E8, E9, E10, E13 | 3–5 horas | Diagnóstico rápido sin profundizar en Ops/Org/Riesgos |
| **Solo Diagnóstico** | E1 → E10 | 4–8 horas | Solo identificación de problemas, sin diseño de soluciones |
| **Solo Diseño** | E10 (inputs manuales), E11 → E13 | 2–4 horas | Solo diseño de iniciativas y roadmap (datos de entrada externos) |

*Etapas simplificadas.

---

*Fin del documento — Full_Business_Diagnosis.md v1.0*
