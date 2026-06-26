# Sistema Integral de Indicadores

> **Sistema Operativo** — KPI System de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del Sistema de KPIs](#1-arquitectura-del-sistema-de-kpis)
2. [KPIs Comerciales (Sales)](#2-kpis-comerciales-sales)
3. [KPIs de Delivery (Operations)](#3-kpis-de-delivery-operations)
4. [KPIs de Customer Success](#4-kpis-de-customer-success)
5. [KPIs Administrativos (Admin)](#5-kpis-administrativos-admin)
6. [KPIs de Conocimiento (Knowledge)](#6-kpis-de-conocimiento-knowledge)
7. [KPIS Estratégicos (Dirección)](#7-kpis-estratégicos-dirección)
8. [Sistema de Semáforos](#8-sistema-de-semáforos)
9. [Dashboard de KPIs](#9-dashboard-de-kpis)
10. [Proceso de Revisión](#10-proceso-de-revisión)

---

## 1. Arquitectura del Sistema de KPIs

### 1.1 Principios

| Principio | Descripción |
|---|---|
| **Alineación** | Todo KPI se vincula a un objetivo estratégico |
| **Accionable** | Cada KPI tiene un responsable que puede influir en él |
| **Medible** | Todos los KPIs tienen fórmula y fuente de datos clara |
| **Frecuencia definida** | Cada KPI tiene periodicidad de medición establecida |
| **Semáforo** | Todo KPI tiene umbrales verde/amarillo/rojo |
| **Visible** | Todos los KPIs están en un dashboard accesible al equipo |

### 1.2 Estructura de un KPI

| Elemento | Descripción | Ejemplo |
|---|---|---|
| **Nombre** | Identificador único | Win Rate |
| **Categoría** | Área funcional | Sales |
| **Fórmula** | Cálculo matemático | OPP Won / OPP Total |
| **Unidad** | Unidad de medida | % |
| **Frecuencia** | Cada cuánto se mide | Mensual |
| **Fuente** | Dónde se obtienen los datos | CRM (Deals) |
| **Responsable** | Quién responde por el resultado | Ventas |
| **Meta** | Valor objetivo | ≥ 35% |
| **Semáforo** | Verde/Amarillo/Rojo | 🟢 ≥ 35% 🟡 25-35% 🔴 < 25% |
| **Histórico** | Tendencia últimos 3 meses | ↑ ↓ → |

### 1.3 Mapa de KPIs por Perspectiva (Balanced Scorecard)

| Perspectiva | KPIs |
|---|---|
| **Financiera** | MRR, Margen Bruto, Margen Neto, CAC, LTV, Cash Flow |
| **Clientes** | NPS, CSAT, Tasa de Retención, Tasa de Churn, Referidos |
| **Procesos Internos** | On-Time Delivery, Ciclo de Diagnóstico, QA Pass Rate |
| **Aprendizaje y Crecimiento** | Knowledge Items Creados, Tasa de Reutilización, Post-Mortem Completion |

---

## 2. KPIs Comerciales (Sales)

| # | KPI | Fórmula | Unidad | Frecuencia | Responsable | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| S1 | **MQLs Generados** | Conteo de leads entrantes | # | Semanal | Marketing | ≥ 20 | ≥ 20 | 10-20 | < 10 |
| S2 | **SQLs Generados** | Conteo de leads calificados | # | Semanal | Ventas | ≥ 8 | ≥ 8 | 5-8 | < 5 |
| S3 | **Lead-to-SQL Rate** | SQL / MQL | % | Mensual | Ventas | ≥ 25% | ≥ 25% | 15-25% | < 15% |
| S4 | **SQL-to-OPP Rate** | OPP / SQL | % | Mensual | Ventas | ≥ 50% | ≥ 50% | 35-50% | < 35% |
| S5 | **Discovery-to-Proposal** | PROP / Discovery | % | Mensual | Ventas | ≥ 70% | ≥ 70% | 50-70% | < 50% |
| S6 | **Win Rate** | OPP Won / OPP Total | % | Mensual | Ventas | ≥ 35% | ≥ 35% | 25-35% | < 25% |
| S7 | **Avg. Sales Cycle** | Días de SQL a Won | Días | Mensual | Ventas | ≤ 21 | ≤ 21 | 21-30 | > 30 |
| S8 | **Avg. Ticket** | Ingreso / OPP Won | USD | Mensual | Ventas | ≥ 3,500 | ≥ 3,500 | 2,500-3,500 | < 2,500 |
| S9 | **Pipeline Value** | Σ(Deal Value × Probabilidad) | USD | Semanal | Ventas | ≥ 3× MRR | ≥ 3× | 2-3× | < 2× |
| S10 | **CAC** | Gasto Comercial / Clientes Nuevos | USD | Mensual | Dirección | ≤ 1,500 | ≤ 1,500 | 1,500-2,500 | > 2,500 |
| S11 | **LTV:CAC** | Ticket Promedio × Diagnósticos año / CAC | Ratio | Trimestral | Dirección | ≥ 3:1 | ≥ 3:1 | 2-3:1 | < 2:1 |
| S12 | **Propuestas Enviadas/mes** | Conteo | # | Mensual | Ventas | ≥ 8 | ≥ 8 | 5-8 | < 5 |

---

## 3. KPIs de Delivery (Operations)

| # | KPI | Fórmula | Unidad | Frecuencia | Responsable | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| D1 | **On-Time Delivery** | Diagnósticos a tiempo / Total | % | Mensual | Delivery Lead | ≥ 90% | ≥ 90% | 80-90% | < 80% |
| D2 | **Avg. Delivery Cycle** | Días kickoff → presentación | Días | Mensual | Delivery Lead | ≤ 21 | ≤ 21 | 21-28 | > 28 |
| D3 | **NPS Post-Diagnóstico** | % Promotores - % Detractores | Puntos | Por proyecto | Delivery Lead | ≥ 50 | ≥ 50 | 30-50 | < 30 |
| D4 | **QA Pass Rate (1ra vez)** | Informes sin errores / Total | % | Mensual | Delivery Lead | ≥ 80% | ≥ 80% | 60-80% | < 60% |
| D5 | **Agent Output Completion** | Outputs generados / Planificados | % | Por proyecto | Delivery Lead | 100% | = 100% | 90-100% | < 90% |
| D6 | **Client Satisfaction** | Encuesta post-entrega (1-5) | Puntos | Por proyecto | Delivery Lead | ≥ 4.5 | ≥ 4.5 | 4.0-4.5 | < 4.0 |
| D7 | **Horas por Diagnóstico** | Horas totales / Diagnóstico | Horas | Mensual | Delivery Lead | ≤ 40h | ≤ 40 | 40-60 | > 60 |
| D8 | **Upsell/Cross-sell Rate** | Clientes con upsell / Total | % | Trimestral | Delivery Lead | ≥ 20% | ≥ 20% | 10-20% | < 10% |
| D9 | **Time-to-QA** | Días de informe draft a QA | Días | Mensual | Delivery Lead | ≤ 2 | ≤ 2 | 2-4 | > 4 |
| D10 | **Brief Completion** | Brief recibido ≤ 48h de kickoff | % | Mensual | Delivery Lead | ≥ 90% | ≥ 90% | 75-90% | < 75% |

---

## 4. KPIs de Customer Success

| # | KPI | Fórmula | Unidad | Frecuencia | Responsable | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| C1 | **NPS** | % Promotores - % Detractores | Puntos | Por proyecto | CS | ≥ 50 | ≥ 50 | 30-50 | < 30 |
| C2 | **CSAT** | Promedio satisfacción (1-5) | Puntos | Por proyecto | CS | ≥ 4.5 | ≥ 4.5 | 4.0-4.5 | < 4.0 |
| C3 | **Tasa de Retención** | Clientes activos / Total | % | Mensual | CS | ≥ 70% | ≥ 70% | 50-70% | < 50% |
| C4 | **Tasa de Churn** | Clientes perdidos / Total | % | Trimestral | CS | ≤ 10% | ≤ 10% | 10-20% | > 20% |
| C5 | **Plan 90 Days Completion** | Acciones completadas / Planificadas | % | Por proyecto | CS | ≥ 60% | ≥ 60% | 40-60% | < 40% |
| C6 | **Client Lifetime Value** | Ingreso total / Cliente (vida) | USD | Anual | CS | ≥ 8,000 | ≥ 8,000 | 4,000-8,000 | < 4,000 |
| C7 | **Time to Response (Quejas)** | Horas a 1ra respuesta | Horas | Por incidente | CS | ≤ 24h | ≤ 24 | 24-48 | > 48 |
| C8 | **Referral Rate** | Clientes que refieren / Total | % | Trimestral | CS | ≥ 15% | ≥ 15% | 5-15% | < 5% |
| C9 | **Testimonial Capture** | Testimonios obtenidos / Promotores | % | Mensual | CS | ≥ 30% | ≥ 30% | 15-30% | < 15% |
| C10 | **NPS Survey Response Rate** | NPS respondidas / Enviadas | % | Mensual | CS | ≥ 50% | ≥ 50% | 30-50% | < 30% |

---

## 5. KPIs Administrativos (Admin)

| # | KPI | Fórmula | Unidad | Frecuencia | Responsable | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | **Onboarding Time** | Días de WON a kickoff | Días | Mensual | Admin | ≤ 3 | ≤ 3 | 3-5 | > 5 |
| A2 | **Invoice-to-Payment** | Días promedio para cobrar | Días | Mensual | Admin | ≤ 15 | ≤ 15 | 15-25 | > 25 |
| A3 | **Aging > 30 días** | Facturas sin pagar > 30d / Total | % | Semanal | Admin | ≤ 5% | ≤ 5% | 5-10% | > 10% |
| A4 | **Contract-to-Sign** | Días de envío a firma | Días | Mensual | Admin | ≤ 3 | ≤ 3 | 3-5 | > 5 |
| A5 | **Cash Flow Accuracy** | Real vs Presupuesto | % | Mensual | Admin | ±10% | ±10% | 10-20% | > 20% |
| A6 | **Payment Compliance** | Pagos a tiempo / Emitidos | % | Mensual | Admin | ≥ 95% | ≥ 95% | 85-95% | < 85% |
| A7 | **Document Compliance** | Expedientes completos / Total | % | Mensual | Admin | 100% | 100% | 95-100% | < 95% |
| A8 | **Tax Filing Compliance** | Declaraciones a tiempo / Total | % | Anual | Admin | 100% | 100% | — | < 100% |
| A9 | **Gross Margin** | (Ingresos - Costos Directos) / Ingresos | % | Mensual | Admin | ≥ 60% | ≥ 60% | 50-60% | < 50% |
| A10 | **Operating Expense Ratio** | Gastos Operativos / Ingresos | % | Mensual | Admin | ≤ 40% | ≤ 40% | 40-50% | > 50% |

---

## 6. KPIs de Conocimiento (Knowledge)

| # | KPI | Fórmula | Unidad | Frecuencia | Responsable | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| K1 | **Knowledge Items Creados/mes** | Documentos nuevos en Knowledge/ | # | Mensual | Equipo | ≥ 3 | ≥ 3 | 1-3 | < 1 |
| K2 | **Knowledge Items Actualizados/mes** | Documentos con nueva versión | # | Mensual | Equipo | ≥ 2 | ≥ 2 | 1-2 | < 1 |
| K3 | **Tasa de Reutilización** | Veces usado / Total diagnósticos | % | Mensual | Delivery Lead | ≥ 80% | ≥ 80% | 60-80% | < 60% |
| K4 | **Time-to-Publish** | Días de identificación a publicación | Días | Mensual | Knowledge Curator | ≤ 7 | ≤ 7 | 7-14 | > 14 |
| K5 | **Documentos Sin Revisar > 6m** | Conteo de docs sin revisión reciente | # | Mensual | Knowledge Curator | ≤ 3 | ≤ 3 | 3-5 | > 5 |
| K6 | **Tasa de Adopción** | Items usados / Items disponibles | % | Trimestral | Knowledge Curator | ≥ 60% | ≥ 60% | 40-60% | < 40% |
| K7 | **Post-Mortem Completion** | Post-mortems realizados / Diagnósticos | % | Mensual | Delivery Lead | 100% | 100% | 80-100% | < 80% |
| K8 | **Knowledge NPS** | Encuesta al equipo sobre utilidad | Puntos | Trimestral | Director | ≥ 70 | ≥ 70 | 50-70 | < 50 |

---

## 7. KPIs Estratégicos (Dirección)

| # | KPI | Fórmula | Unidad | Frecuencia | Meta | 🟢 | 🟡 | 🔴 |
|---|---|---|---|---|---|---|---|---|
| E1 | **MRR (Monthly Recurring Revenue)** | Σ Ingresos recurrentes del mes | USD | Mensual | ≥ 5,000 | ≥ 5,000 | 2,500-5,000 | < 2,500 |
| E2 | **Margen Neto** | Utilidad Neta / Ingresos | % | Mensual | ≥ 25% | ≥ 25% | 15-25% | < 15% |
| E3 | **MRR Growth Rate** | (MRR mes - MRR mes ant) / MRR mes ant | % | Mensual | ≥ 15% | ≥ 15% | 5-15% | < 5% |
| E4 | **Cash Runway** | Caja / Gasto Mensual | Meses | Mensual | ≥ 6 | ≥ 6 | 3-6 | < 3 |
| E5 | **Clientes Activos** | Conteo de clientes en diagnóstico | # | Mensual | ≥ 5 | ≥ 5 | 3-5 | < 3 |
| E6 | **Revenue por Cliente (anualizado)** | Ingreso anual / Clientes activos | USD | Trimestral | ≥ 7,000 | ≥ 7,000 | 4,000-7,000 | < 4,000 |
| E7 | **NPS General** | Promedio NPS últimos 6 meses | Puntos | Trimestral | ≥ 50 | ≥ 50 | 30-50 | < 30 |
| E8 | **Health Score (compuesto)** | Promedio de semáforos de todos los KPIs | % | Mensual | ≥ 80% | ≥ 80% | 60-80% | < 60% |

---

## 8. Sistema de Semáforos

### 8.1 Definición

| Color | Significado | Acción |
|---|---|---|
| 🟢 **Verde** | Meta cumplida o superada. KPI saludable. | Mantener, documentar prácticas exitosas |
| 🟡 **Amarillo** | KPI por debajo de meta pero dentro de rango aceptable. Requiere atención. | Monitorear, crear plan de mejora si continúa 2 meses |
| 🔴 **Rojo** | KPI crítico. Muy por debajo de meta. Requiere intervención inmediata. | Reunión de crisis, plan de acción, escalar a Director |

### 8.2 Reglas de Semáforo

| Regla | Aplica |
|---|---|
| 3 meses consecutivos en 🟡 → Pasa a 🔴 automáticamente | Todos los KPIs |
| KPI en 🔴 por 2 meses → Plan de acción obligatorio del responsable | Todos los KPIs |
| Si el KPI mejora 2 meses seguidos → Pasa de 🔴 a 🟡 | Todos los KPIs |
| Health Score compuesto = % de KPIs en 🟢 | Dashboard general |

### 8.3 Fórmula de Health Score

```
Health Score = (KPIs en Verde / Total KPIs) × 100
```

| Score | Estado | Acción |
|---|---|---|
| ≥ 80% | 🟢 Saludable | Seguimiento normal |
| 60-80% | 🟡 Atención | Revisión mensual de director |
| < 60% | 🔴 Crítico | Reunión semanal de recuperación |

---

## 9. Dashboard de KPIs

### 9.1 Estructura del Dashboard

```
┌──────────────────────────────────────────────────────────────────────┐
│                    HEALTH SCORE: 78% 🟡                             │
├──────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌──────────────┐  │
│  │      FINANCIERA     │  │      CLIENTES       │  │  PROCESOS    │  │
│  │  MRR: $6,200 🟢   │  │  NPS: 52 🟢        │  │  On-Time:    │  │
│  │  Margen: 62% 🟢   │  │  Retención: 75% 🟢 │  │  88% 🟡     │  │
│  │  CAC: $1,200 🟢   │  │  Churn: 8% 🟢      │  │  Cycle: 18d  │  │
│  │                    │  │                     │  │  🟢          │  │
│  └─────────────────────┘  └─────────────────────┘  └──────────────┘  │
├──────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐  ┌─────────────────────┐                    │
│  │  APRENDIZAJE        │  │      ESTRATÉGICOS   │                    │
│  │  Items nuevos: 4 🟢│  │  MRR Growth: 12% 🟡│                    │
│  │  Reutilización:     │  │  Cash Runway: 8m 🟢│                    │
│  │  85% 🟢            │  │  Activos: 6 🟢      │                    │
│  │  Post-mortem: 100%  │  │                     │                    │
│  │  🟢                 │  │                     │                    │
│  └─────────────────────┘  └─────────────────────┘                    │
└──────────────────────────────────────────────────────────────────────┘
```

### 9.2 KPIs en Rojo (Acción Inmediata)

| KPI | Valor | Meta | Responsable | Plan de Acción |
|---|---|---|---|---|
| — | — | — | — | — |

### 9.3 KPIs en Mejora (Tendencia Positiva)

| KPI | Último mes | Mes anterior | Tendencia |
|---|---|---|---|
| — | — | — | — |

---

## 10. Proceso de Revisión

### 10.1 Calendario de Revisión

| Reunión | Frecuencia | Participantes | Agenda |
|---|---|---|---|
| **Daily Standup** | Diaria | Todo el equipo | KPIs del día anterior, blockers |
| **Weekly Ops Review** | Semanal | Delivery + Ventas + CS | KPIs operativos, pipeline, próximos diagnósticos |
| **Monthly KPI Review** | Mensual | Dirección + Leads | Todos los KPIs, health score, plan de acción |
| **Quarterly Strategy** | Trimestral | Dirección | Revisión de metas, ajuste de semáforos, roadmap |
| **Annual Planning** | Anual | Todo el equipo | Revisión anual, nuevas metas, OKRs |

### 10.2 Formato de Revisión Mensual

| Item | Descripción |
|---|---|
| **Health Score** | Score actual vs mes anterior |
| **KPIs en Rojo** | Lista, causa raíz, plan de acción |
| **KPIs en Verde** | Qué funcionó, cómo replicarlo |
| **Tendencias** | KPIS que mejoran/empeoran 3 meses consecutivos |
| **Decisiones** | Ajustes de proceso, recursos, metas |
| **Acciones** | Próximos pasos con responsables y deadlines |

### 10.3 Mejora Continua del Sistema de KPIs

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Revisar relevancia de cada KPI | Trimestral | Dirección |
| Ajustar metas según crecimiento | Semestral | Dirección |
| Agregar/eliminar KPIs | Trimestral | Dirección |
| Benchmark de metas vs industria | Anual | Dirección |

---

*Fin del documento — KPI_System.md v1.0*
