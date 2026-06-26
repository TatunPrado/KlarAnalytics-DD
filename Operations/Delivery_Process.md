# Proceso de Prestación del Servicio

> **Sistema Operativo** — Delivery Process de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del Servicio](#1-arquitectura-del-servicio)
2. [Fase 1: Kickoff](#2-fase-1-kickoff)
3. [Fase 2: Diagnóstico Multi-Agente](#3-fase-2-diagnóstico-multi-agente)
4. [Fase 3: Generación de Informe](#4-fase-3-generación-de-informe)
5. [Fase 4: Revisión y Calidad](#5-fase-4-revisión-y-calidad)
6. [Fase 5: Presentación de Resultados](#6-fase-5-presentación-de-resultados)
7. [Fase 6: Post-Entrega](#7-fase-6-post-entrega)
8. [Sistema de Agentes](#8-sistema-de-agentes)
9. [Gestión de Calidad](#9-gestión-de-calidad)
10. [KPIs de Delivery](#10-kpis-de-delivery)

---

## 1. Arquitectura del Servicio

### 1.1 Visión General

```
Kickoff ──► Diagnóstico Multi-Agente ──► Informe ──► Revisión ──► Presentación ──► Post-Entrega
   │              │                        │            │              │               │
   │              │                        │            │              │               │
   Alineación     ┌─────────────────┐      Draft       QA Interna    Reunión        Seguimiento
   Objetivos      │ Knowledge Agent│      Documento    + Cliente     Final          + Encuesta
                  │ Strategy Agent │                                 + Plan 90 días
                  │ Finance Agent  │
                  │ Operations Agent│
                  │ Risk Agent     │
                  │ Talent Agent   │
                  └─────────────────┘
```

### 1.2 Tipos de Diagnóstico

| Tipo | Duración | Dimensiones | Agentes Involucrados | Precio (USD) |
|---|---|---|---|---|
| **Express** | 7-10 días | 3 (a elección) | 3 | 1,500 - 2,500 |
| **Integral** | 14-21 días | 5 | 5 | 3,500 - 5,500 |
| **Premium** | 30-45 días | 5 + Taller + 3m Follow-up | 5 + Coach | 7,500 - 12,000 |

### 1.3 Mapa de Dimensiones vs Agentes

| Dimensión | Agente Primario | Skills Utilizados | Frameworks |
|---|---|---|---|
| Modelo de Negocio | Strategy Agent | Business_Model_Analysis | BMC, VRIO, Value Chain |
| Estrategia | Strategy Agent | Strategic_Foresight, Competitive_Advantage | Porter 5F, VRIO, OKRs |
| Finanzas | Finance Agent | Financial_Diagnosis, Cashflow_Analysis | 3S Financial Analysis, Dupont |
| Operaciones | Operations Agent | Process_Mapping, Quality_Assessment | Lean, TOC, Operational_Excellence |
| Talento y Org. | Talent Agent | Talent_Diagnosis, Culture_Map | 7S, OCAI, Belbin |
| Riesgos | Risk Agent | Risk_Matrix, ESG_Assessment | ISO 31000, Risk Matrix |
| Cliente y Mercado | Knowledge Agent | Market_Fit, Customer_Journey | Persona Map, JTBD, NPS |

---

## 2. Fase 1: Kickoff

### 2.1 Objetivo

Alinear expectativas, confirmar alcance y recopilar la documentación inicial del cliente.

### 2.2 Actividades

| Actividad | Responsable | Duración | Documento Generado |
|---|---|---|---|
| Reunión de kickoff (30 min) | Delivery Lead + Cliente | 30 min | `Kickoff_Notes.md` |
| Envío de Brief_Empresa | Delivery Lead | 1 hora | `Brief_Empresa.md` |
| Solicitud de documentación | Delivery Lead | — | Request email |
| Creación de expediente | Delivery Lead | 30 min | `Expediente_[Cliente].md` |

### 2.3 Documentación Solicitada al Cliente

| Documento | Formato | Obligatorio | Dimensión |
|---|---|---|---|
| Estados financieros (últimos 3 años) | Excel/PDF | Sí | Finanzas |
| Estados de resultados mensuales (último año) | Excel/PDF | Sí | Finanzas |
| Organigrama actual | PDF/PPT | Sí | Talento |
| Descripción de puestos | PDF/Word | No | Talento |
| Procesos documentados (si existen) | — | No | Operaciones |
| Plan estratégico (si existe) | — | No | Estrategia |
| Contratos clave, clientes principales | — | No | Cliente |

### 2.4 Automatizaciones

| Disparador | Acción |
|---|---|
| Kickoff agendado | Enviar recordatorio 24h antes |
| Kickoff completado | Crear expediente, disparar Brief_Empresa |
| Brief_Empresa recibido | Iniciar pool de agentes |

### 2.5 KPIs

| Indicador | Meta |
|---|---|
| Brief recibido ≤ 48h de kickoff | ≥ 90% |
| Documentación completa ≤ 72h | ≥ 80% |
| Kickoff-to-Agents | ≤ 24h |

---

## 3. Fase 2: Diagnóstico Multi-Agente

### 3.1 Arquitectura del Sistema Multi-Agente

```
                    ┌─────────────────────────────┐
                    │         Orchestrator         │
                    │      (Delivery Lead)         │
                    └──────┬──────┬──────┬─────────┘
                           │      │      │
              ┌────────────┘      │      └─────────────┐
              │                   │                    │
     ┌────────▼────────┐  ┌──────▼──────┐  ┌─────────▼────────┐
     │  Knowledge Agent│  │Finance Agent │  │Operations Agent  │
     │  Playbooks/     │  │  Skills/     │  │  Skills/         │
     │  Discovery      │  │  Financial   │  │  Process_Mapping │
     └────────┬────────┘  └──────┬──────┘  └─────────┬────────┘
              │                   │                    │
     ┌────────▼────────┐  ┌──────▼──────┐  ┌─────────▼────────┐
     │  Strategy Agent │  │  Risk Agent  │  │   Talent Agent   │
     │  Skills/        │  │  Skills/     │  │   Skills/        │
     │  Strategic      │  │  Risk_Matrix │  │   Talent_Diag    │
     └─────────────────┘  └─────────────┘  └──────────────────┘
```

### 3.2 Flujo de Trabajo de Agentes

```
Paso 1: Orchestrator recibe Brief_Empresa + Documentación
Paso 2: Orchestrator asigna trabajo a cada agente según dimensiones contratadas
Paso 3: Cada agente ejecuta diagnóstico en su dimensión:
         - Lee documentación relevante
         - Aplica frameworks (Knowledge/CORE/)
         - Genera hallazgos preliminares
         - Propone hipótesis
Paso 4: Los agentes devuelven sus outputs al Orchestrator
Paso 5: Orchestrator consolida hallazgos, identifica patrones cruzados
Paso 6: Orchestrator genera el informe consolidado
```

### 3.3 Inputs y Outputs por Agente

| Agente | Inputs | Outputs |
|---|---|---|
| **Knowledge Agent** | Brief_Empresa, Industry data | Contexto de industria, benchmarks |
| **Strategy Agent** | BMC actual, plan estratégico (si existe) | BMC propuesto, VRIO, gaps estratégicos |
| **Finance Agent** | EEFF, flujo de caja | Ratios financieros, Dupont, diagnóstico 3S |
| **Operations Agent** | Procesos, entrevistas | Procesos mapeados, cuellos de botella |
| **Risk Agent** | Operaciones, finanzas, industria | Matriz de riesgo, ESG score |
| **Talent Agent** | Organigrama, descripciones | Análisis 7S, mapa cultural, gaps de talento |

### 3.4 Entrevista de Descubrimiento

Como parte del diagnóstico, se realiza una entrevista estructurada con el cliente siguiendo el [Playbook Discovery_Interview](../Playbooks/Discovery_Interview.md).

| Actividad | Duración | Responsable |
|---|---|---|
| Entrevista con dueño/CEO | 60 min | Delivery Lead + Agentes |
| Entrevista con gerentes clave | 45 min c/u | Agentes |
| Observación de operaciones (opcional) | 2-3 horas | Operations Agent |

### 3.5 Automatizaciones

| Disparador | Acción |
|---|---|
| Brief_Empresa recibido | Iniciar pool de agentes automáticamente |
| Todos los agentes completados | Notificar a Orchestrator |
| Hallazgo detectado (score < umbral) | Marcar en dashboard, priorizar en informe |

### 3.6 Tiempos Estimados (Diagnóstico Integral)

| Actividad | Duración |
|---|---|
| Brief + documentación recibida | Día 1-2 |
| Análisis multi-agente | Día 3-7 |
| Entrevistas | Día 5-8 |
| Consolidación de hallazgos | Día 8-10 |
| Generación de informe (Draft) | Día 10-14 |

---

## 4. Fase 3: Generación de Informe

### 4.1 Estructura del Informe

| Sección | Origen | Descripción |
|---|---|---|
| Portada | Brand/Template | Logo Klar, cliente, fecha |
| Resumen Ejecutivo | Orchestrator | Síntesis del diagnóstico |
| Metodología | Template | Cómo se realizó el diagnóstico |
| Hallazgos por Dimensión | Cada agente | Análisis detallado por dimensión |
| Matriz de Priorización | Orchestrator | Impacto vs Esfuerzo |
| Plan de 90 Días | Orchestrator + Cliente | Acciones concretas inmediatas |
| Roadmap 12 Meses | Orchestrator | Visión a medio plazo |
| Apéndices | Agentes | Detalle técnico, ratios, frameworks aplicados |

### 4.2 Generación de Informe

```
Paso 1: Orchestrator escribe cada sección basado en outputs de agentes
Paso 2: Aplicar marca Klar (Brand/ - paleta azul+teal, logo)
Paso 3: Generar en formatos:
         - PDF (entrega formal al cliente)
         - DOCX (editable para el equipo)
         - Markdown (para Git/registro interno)
Paso 4: Guardar en expediente del cliente
```

### 4.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Draft de informe listo | Notificar a revisión de calidad |
| Informe generado | Guardar en `Knowledge/Casos/[Cliente]/` |

---

## 5. Fase 4: Revisión y Calidad

### 5.1 Checklist de Calidad

- [ ] Datos numéricos verificados (ratios financieros, etc.)
- [ ] Consistencia entre hallazgos (sin contradicciones entre agentes)
- [ ] Lenguaje claro y profesional (alineado con Brand/Tone_of_Voice.md)
- [ ] Plan de 90 días SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Recomendaciones priorizadas (impacto vs esfuerzo)
- [ ] Sin errores ortográficos o gramaticales
- [ ] Marca Klar Analytics aplicada correctamente
- [ ] Documentación interna completa (expediente + outputs de agentes)

### 5.2 Proceso de Revisión

| Paso | Responsable | Duración |
|---|---|---|
| Auto-revisión del Orchestrator | Delivery Lead | 1-2 horas |
| Revisión de par (peer review) | Otro Delivery Lead | 1-2 horas |
| QA final (Director) | Director | 30 min |
| Correcciones incorporadas | Delivery Lead | Variable |

### 5.3 Automatizaciones

| Disparador | Acción |
|---|---|
| QA completado | Mover a "Listo para presentar" |
| Errores detectados | Registrar en log de calidad, retroalimentar Knowledge/ |

### 5.4 KPIs

| Indicador | Meta |
|---|---|
| QA Pass Rate (1ra revisión) | ≥ 80% |
| Errores detectados por informe | ≤ 3 |
| Time-to-QA | ≤ 2 días |

---

## 6. Fase 5: Presentación de Resultados

### 6.1 Agenda de Presentación (60 min)

| Minuto | Tema | Responsable |
|---|---|---|
| 0-5 | Apertura, contexto, agradecimiento | Delivery Lead |
| 5-20 | Hallazgos clave (resumen ejecutivo) | Delivery Lead |
| 20-35 | Dimensión a fondo (según prioridad del cliente) | Delivery Lead |
| 35-45 | Plan de 90 días | Delivery Lead |
| 45-55 | Discusión, preguntas, próximos pasos | Delivery Lead + Cliente |
| 55-60 | Cierre, seguimiento acordado | Delivery Lead |

### 6.2 Entregables al Cliente

| Entregable | Formato | Cuándo |
|---|---|---|
| Informe de Diagnóstico | PDF | En presentación |
| Presentación ejecutiva | PPT/PDF | En presentación |
| Plan de 90 días | PDF | En presentación |
| Acceso a plataforma (futuro) | Link | Post-presentación |

### 6.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Presentación agendada | Enviar recordatorio 24h antes |
| Presentación completada | Mover estado a "Post-Entrega", disparar encuesta NPS |

---

## 7. Fase 6: Post-Entrega

### 7.1 Actividades Post-Entrega

| Actividad | Plazo | Responsable |
|---|---|---|
| Enviar encuesta NPS | 24h post-presentación | Automatizado |
| Check-in de seguimiento (semana 2) | 14 días | Client Success |
| Check-in de seguimiento (mes 1) | 30 días | Client Success |
| Revisión de plan de 90 días (mes 3) | 90 días | Client Success |
| Encuesta de impacto (mes 6) | 180 días | Client Success |

### 7.2 Archivo de Expediente

| Elemento | Ubicación |
|---|---|
| Brief_Empresa | `Knowledge/Casos/[Cliente]/Brief_Empresa.md` |
| Outputs de Agentes | `Knowledge/Casos/[Cliente]/Agents/` |
| Informe Final | `Knowledge/Casos/[Cliente]/Informe_Final.pdf` |
| Presentación | `Knowledge/Casos/[Cliente]/Presentacion.pptx` |
| Lecciones aprendidas | `Knowledge/Casos/[Cliente]/Lecciones.md` |

### 7.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Presentación completada | Enviar NPS, crear tareas de seguimiento |
| 30 días post-entrega | Email de check-in |
| 90 días post-entrega | Revisión de plan de 90 días |

---

## 8. Sistema de Agentes

### 8.1 Mapeo de Agentes por Dimensión

| Agente | Archivo | Dimensión Principal | Skills |
|---|---|---|---|
| **Knowledge Agent** | `Agents/Knowledge_Agent.md` | Contexto, Benchmark | Knowledge_Consolidation |
| **Strategy Agent** | `Agents/Strategy_Agent.md` | Estrategia, Modelo de Negocio | Business_Model_Analysis, Strategic_Foresight, Competitive_Advantage |
| **Finance Agent** | `Agents/Finance_Agent.md` | Finanzas | Financial_Diagnosis, Cashflow_Analysis, Investment_Evaluation |
| **Operations Agent** | `Agents/Operations_Agent.md` | Operaciones | Process_Mapping, Quality_Assessment |
| **Risk Agent** | `Agents/Risk_Agent.md` | Riesgos, ESG | Risk_Matrix, ESG_Assessment |
| **Talent Agent** | `Agents/Talent_Agent.md` | Talento, Organización | Talent_Diagnosis, Culture_Map |

### 8.2 Orquestración

El Delivery Lead actúa como **Orchestrator** con las siguientes funciones:

| Función | Descripción |
|---|---|
| Planificación | Definir qué agentes participan según tipo de diagnóstico |
| Asignación | Enviar Brief + documentación a cada agente |
| Coordinación | Gestionar tiempos y dependencias entre agentes |
| Consolidación | Integrar outputs en informe coherente |
| Calidad | Revisar consistencia y completitud |
| Presentación | Preparar y entregar resultados al cliente |

---

## 9. Gestión de Calidad

### 9.1 Indicadores de Calidad por Fase

| Fase | Indicador | Meta |
|---|---|---|
| Kickoff | Brief completitud | ≥ 80% |
| Diagnóstico | Outputs de agentes completos | 100% |
| Informe | Consistencia entre dimensiones | Sin contradicciones |
| Revisión | QA Pass (1ra vez) | ≥ 80% |
| Presentación | Satisfacción del cliente | NPS ≥ 50 |

### 9.2 Mejora Continua

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Post-mortem de cada diagnóstico | Por proyecto | Delivery Lead |
| Revisión trimestral de calidad | Trimestral | Dirección |
| Actualización de Playbooks | Trimestral | Dirección + Agentes |
| Benchmark de indicadores | Semestral | Dirección |

### 9.3 Errores Comunes y Prevención

| Error | Fase | Prevención |
|---|---|---|
| Brief incompleto | Kickoff | Checklist obligatorio |
| Hallazgos contradictorios entre agentes | Diagnóstico | Reunión de sync entre agentes |
| Recomendaciones no accionables | Informe | Validar SMART antes de QA |
| Timing no realista | Plan 90 días | Validar con cliente durante presentación |

---

## 10. KPIs de Delivery

| Indicador | Fórmula | Frecuencia | Meta | Semáforo |
|---|---|---|---|---|
| **On-Time Delivery** | Entregas a tiempo / Total | Mensual | ≥ 90% | 🔴 < 80% 🟡 80-90% 🟢 ≥ 90% |
| **Avg. Delivery Cycle** | Días desde kickoff a presentación | Mensual | ≤ 21 días (Integral) | 🔴 > 28 🟡 21-28 🟢 ≤ 21 |
| **NPS** | Promotores - Detractores | Por proyecto | ≥ 50 | 🔴 < 30 🟡 30-50 🟢 ≥ 50 |
| **QA Pass Rate** | Informes sin errores / Total | Mensual | ≥ 80% | 🔴 < 60% 🟡 60-80% 🟢 ≥ 80% |
| **Outputs por Agente** | % de outputs generados vs planificados | Por proyecto | 100% | 🔴 < 90% 🟡 90-100% 🟢 = 100% |
| **Client Satisfaction** | Encuesta post-entrega (1-5) | Por proyecto | ≥ 4.5 | 🔴 < 4.0 🟡 4.0-4.5 🟢 ≥ 4.5 |
| **Horas por Diagnóstico** | Horas totales del equipo / diagnóstico | Mensual | ≤ 40h (Integral) | 🔴 > 60 🟡 40-60 🟢 ≤ 40 |
| **Upsell/Cross-sell Rate** | Clientes que contratan más servicios | Trimestral | ≥ 20% | 🔴 < 10% 🟡 10-20% 🟢 ≥ 20% |

---

*Fin del documento — Delivery_Process.md v1.0*
