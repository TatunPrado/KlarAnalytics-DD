# Manual del Sistema Operativo

> **Sistema Operativo** — Operating System Manual de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [¿Qué es el Sistema Operativo?](#1-qué-es-el-sistema-operativo)
2. [Arquitectura del Sistema](#2-arquitectura-del-sistema)
3. [Cómo Usar Este Manual](#3-cómo-usar-este-manual)
4. [Procesos Transversales](#4-procesos-transversales)
5. [Ritmos de Gestión](#5-ritmos-de-gestión)
6. [Órganos de Gobierno](#6-órganos-de-gobierno)
7. [Dashboard de Gestión](#7-dashboard-de-gestión)
8. [Plan de Contingencia](#8-plan-de-contingencia)
9. [Glosario](#9-glosario)
10. [Referencias](#10-referencias)

---

## 1. ¿Qué es el Sistema Operativo?

### 1.1 Definición

El **Sistema Operativo de Klar Analytics** es el conjunto integrado de procesos, herramientas, indicadores y ritmos de gestión que gobiernan la operación diaria de la firma. Inspirado en los sistemas operativos de empresas de alto rendimiento (RocksDB, OKR, EOS), este manual describe **cómo hacemos lo que hacemos**.

### 1.2 Propósito

| Propósito | Descripción |
|---|---|
| **Estandarizar** | Definir la única manera correcta de ejecutar cada proceso |
| **Escalar** | Permitir crecer de 1 a N colaboradores sin perder calidad |
| **Automatizar** | Identificar todo lo que puede y debe automatizarse |
| **Medir** | Tener visibilidad en tiempo real de la salud del negocio |
| **Mejorar** | Incorporar aprendizaje continuo en el ADN de la firma |
| **Integrar** | Conectar todas las piezas (Agentes, Skills, Knowledge, Brands) en un sistema coherente |

### 1.3 Filosofía Operativa

> **"Sistemas sobre héroes. Procesos sobre ocurrencias. Datos sobre opiniones."**

| Principio | Significado |
|---|---|
| **Sistemas sobre héroes** | No necesitamos superhéroes; necesitamos sistemas que cualquier persona competente pueda operar |
| **Procesos sobre ocurrencias** | No improvisamos; seguimos procesos documentados que mejoramos continuamente |
| **Datos sobre opiniones** | Las decisiones se basan en KPIs y hechos, no en corazonadas |
| **Calidad sobre velocidad** | Preferimos entregar bien a entregar rápido; la velocidad se gana con práctica, no con atajos |
| **Mejora continua** | Cada diagnóstico, cada interacción, cada error es una oportunidad para mejorar |

---

## 2. Arquitectura del Sistema

### 2.1 Mapa del Sistema Operativo

```
                     ┌─────────────────────────────────────────────┐
                     │           SISTEMA OPERATIVO KLAR            │
                     │                                            │
                     │  Procesos Primarios (Cadena de Valor)       │
                     │  ┌────────┐  ┌──────────┐  ┌────────────┐ │
                     │  │ VENTAS │→│ DELIVERY │→│ CS + ADMIN  │ │
                     │  └────────┘  └──────────┘  └────────────┘ │
                     │        │           │              │        │
                     │        └──────┬────┘──────────────┘        │
                     │               │                            │
                     │  Procesos de Soporte                      │
                     │  ┌────────────┐  ┌──────────────────┐     │
                     │  │Knowledge   │  │Data & Tech       │     │
                     │  │(Cap. 3)    │  │(KPIs + ERP)      │     │
                     │  └────────────┘  └──────────────────┘     │
                     │                                            │
                     │  Ritmos de Gestión                        │
                     │  ┌──────┐ ┌──────┐ ┌──────┐ ┌─────────┐  │
                     │  │Diario│ │Semanal││Mensual││Trimestral│  │
                     │  └──────┘ └──────┘ └──────┘ └─────────┘  │
                     └─────────────────────────────────────────────┘
```

### 2.2 Relación entre Componentes

| Componente | Archivo(s) | Función |
|---|---|---|
| **Process Map** | `Operations/Process_Map.md` | Mapa completo de procesos, subprocesos y RACI |
| **Sales Process** | `Operations/Sales_Process.md` | Pipeline comercial: lead a onboarding |
| **Delivery Process** | `Operations/Delivery_Process.md` | Prestación del servicio: kickoff a presentación |
| **Knowledge Process** | `Operations/Knowledge_Process.md` | Ciclo de aprendizaje organizacional |
| **Client Success Process** | `Operations/Client_Success_Process.md` | Seguimiento post-diagnóstico |
| **Administration Process** | `Operations/Administration_Process.md` | Onboarding, facturación, cobranzas, contratos |
| **Database Model** | `Operations/Database_Model.md` | Estructura de datos (Sheets → PostgreSQL) |
| **CRM Model** | `Operations/CRM_Model.md` | Sistema de gestión de relaciones con clientes |
| **ERP Blueprint** | `Operations/ERP_Blueprint.md` | Blueprint del ERP futuro |
| **KPI System** | `Operations/KPI_System.md` | Todos los indicadores, semáforos y metas |
| **Operating System Manual** | **Este archivo** | Consolidación, ritmos, gobierno |

### 2.3 Referencia Cruzada con el Repositorio

| Recurso Externo | Relación |
|---|---|
| `Agents/` (10 agentes) | Son los ejecutores del Delivery Process |
| `Skills/` (8 skills) | Son las capacidades que los agentes aplican |
| `Knowledge/CORE/` (12+ frameworks) | Son el conocimiento que los agentes usan y generan |
| `Playbooks/` (3 SOPs) | Son los procedimientos detallados que implementan los procesos de Operations/ |
| `Brand/` (15 archivos) | Definen la identidad que se aplica en todos los entregables al cliente |

---

## 3. Cómo Usar Este Manual

### 3.1 Para Cada Rol

| Si eres... | Lee primero... | Consulta... |
|---|---|---|
| **Director** | Este manual (completo) + KPI_System.md | Procesos relevantes según el día |
| **Ventas** | Sales_Process.md + CRM_Model.md | Process_Map.md (visión general) |
| **Delivery Lead** | Delivery_Process.md + Process_Map.md | Knowledge_Process.md + KPI_System.md (KPIs de ops) |
| **CS** | Client_Success_Process.md | Sales_Process.md (post-venta) + KPI_System.md |
| **Admin** | Administration_Process.md + ERP_Blueprint.md | Database_Model.md + KPI_System.md |
| **Nuevo integrante** | Este manual (capítulos 1-3) → Process_Map.md → El proceso de tu área | — |

### 3.2 Cómo se Actualiza este Manual

| Evento | Acción | Responsable |
|---|---|---|
| Cambio en un proceso | Actualizar el archivo correspondiente + este manual si hay cambio estructural | Dueño del proceso |
| Nueva versión de Operations/ | Revisión trimestral completa | Director |
| Feedback del equipo | Incorporar en la revisión trimestral | Todos |

---

## 4. Procesos Transversales

### 4.1 Proceso de Excepción

Cuando un caso no puede seguir el proceso estándar (por ejemplo, un diagnóstico fuera de scope o una solicitud especial):

```
Identificar excepción →
    ↓
Documentar: ¿qué proceso estándar no aplica y por qué? →
    ↓
Escalar a Director para aprobación →
    ↓
Si se aprueba → Ejecutar con proceso adaptado →
    ↓
Post-mortem: ¿deberíamos actualizar el proceso estándar?
```

### 4.2 Proceso de Escalamiento

| Nivel | Decide | Cuándo |
|---|---|---|
| **N1 — Delivery Lead** | Decisiones operativas del diagnóstico | Scope dentro del contrato, cambios menores |
| **N2 — Director** | Decisiones tácticas | Cambios de alcance, descuentos, quejas de cliente |
| **N3 — Socios** | Decisiones estratégicas | Nuevos servicios, pricing, alianzas, crisis |

### 4.3 Proceso de Mejora Continua

Cada vez que se completa un ciclo de cualquier proceso (un diagnóstico, un cierre de mes, un ciclo de knowledge), se activa el ciclo de mejora:

```
Ejecutar proceso →
    ↓
Medir resultados (KPIs + semáforos) →
    ↓
Identificar desviaciones →
    ↓
Analizar causa raíz →
    ↓
Proponer mejora →
    ↓
Implementar cambio →
    ↓
Actualizar documentación →
    ↓
Comunicar al equipo
```

---

## 5. Ritmos de Gestión

### 5.1 Calendario Anual de Gestión

| Ritmo | Frecuencia | Duración | Participantes | Formato |
|---|---|---|---|---|
| **Daily Standup** | Diaria (L-V) | 10 min | Todo el equipo | Virtual/Slack |
| **Weekly Ops Review** | Semanal (lunes) | 30 min | Delivery + Ventas + CS | Virtual |
| **Weekly Sales Review** | Semanal (miércoles) | 30 min | Ventas + Director | Virtual |
| **Monthly KPI Review** | Mensual (día 5) | 60 min | Dirección + Leads | Virtual |
| **Monthly Team Meeting** | Mensual (día 15) | 60 min | Todo el equipo | Presencial/Virtual |
| **Quarterly Strategy** | Trimestral | 120 min | Dirección | Presencial |
| **Annual Planning** | Anual (enero) | 1 día | Todo el equipo | Presencial |

### 5.2 Daily Standup

| Item | Formato |
|---|---|
| **¿Qué hice ayer?** | Una línea por persona |
| **¿Qué haré hoy?** | Una línea por persona |
| **¿Qué me bloquea?** | Identificar blockers |
| **KPIs del día** | Pipeline, clientes activos, cobranzas |
| **Herramienta** | Slack (thread diario) o reunión virtual |

### 5.3 Weekly Ops Review (Agenda)

| Minuto | Tema | Quién |
|---|---|---|
| 0-5 | KPIs de la semana (semáforo) | Director |
| 5-10 | Pipeline: nuevos, movimientos, próximos cierres | Ventas |
| 10-20 | Diagnósticos: estado, blockers, calidad | Delivery Lead |
| 20-25 | CS: check-ins, NPS, riesgos | CS |
| 25-30 | Próximos pasos, decisiones, acciones | Director |

### 5.4 Monthly KPI Review (Agenda)

| Minuto | Tema | Quién |
|---|---|---|
| 0-5 | Health Score del mes | Director |
| 5-15 | KPIs en rojo: causa raíz + plan de acción | Responsable de cada KPI |
| 15-25 | KPIs en verde: qué funcionó, cómo replicar | Responsable de cada KPI |
| 25-35 | Tendencias y proyecciones | Director |
| 35-45 | Decisiones: ajustes de proceso, recursos, metas | Director |
| 45-60 | Acciones: próximos pasos con deadlines | Todos |

### 5.5 Reuniones Cancelación/Postergación

| Ritmo | Solo si... | Máximo |
|---|---|---|
| **Daily Standup** | No hay actividad del equipo | 2 días seguidos |
| **Weekly Ops** | No hay novedades operativas | 1 semana |
| **Monthly Review** | *No se cancela* | — |
| **Quarterly Strategy** | *No se cancela* | — |

---

## 6. Órganos de Gobierno

### 6.1 Estructura de Roles

| Rol | Persona | Responsabilidad Principal |
|---|---|---|
| **Director** | — | Estrategia, calidad, decisiones finales, visión |
| **Delivery Lead** | — | Ejecución de diagnósticos, gestión de agentes, calidad |
| **Sales / Ventas** | — | Pipeline, prospección, cierre de ventas |
| **Customer Success** | — | Seguimiento post-diagnóstico, NPS, retención |
| **Administración** | — | Facturación, cobranzas, contratos, contabilidad |
| **Knowledge Curator** | — | Calidad y evolución del conocimiento (rol rotativo) |

### 6.2 Matriz de Decisiones (RAPID)

| Decisión | Recomendar | Aprobar | Ejecutar | Informar |
|---|---|---|---|---|
| Cambio de pricing | Ventas | Director | Admin | Todos |
| Descuento > 10% | Ventas | Director | Ventas | Admin |
| Nuevo servicio | Director | Socios | Delivery Lead | Todos |
| Contratación | Director | Socios | Admin | Todos |
| Gasto > $1,000 | Delivery Lead | Director | Admin | Director |
| Cambio en proceso | Dueño del proceso | Director | Dueño | Todos |
| Caso de excepción | Delivery Lead | Director | Delivery Lead | Admin |

### 6.3 Políticas de Comunicación

| Tipo | Canal | Tiempo de Respuesta |
|---|---|---|
| **Urgente** (cliente en crisis, error crítico) | Slack @director + llamada | ≤ 1h |
| **Alta prioridad** (queja de cliente, blocker) | Slack @responsable | ≤ 4h |
| **Normal** (consulta, coordinación) | Slack / Email | ≤ 24h |
| **Baja prioridad** (sugerencia, mejora) | Email / Documento | ≤ 72h |
| **Comunicación oficial** (anuncios) | Email + Slack + Reunión | Programado |

---

## 7. Dashboard de Gestión

### 7.1 Tablero de Control Semanal

| Indicador | Valor | Semáforo | Tendencia | Acción Requerida |
|---|---|---|---|---|
| **Pipeline Value** | — | — | — | — |
| **Clientes Activos** | — | — | — | — |
| **NPS del Mes** | — | — | — | — |
| **On-Time Delivery** | — | — | — | — |
| **Cash Flow** | — | — | — | — |

### 7.2 Tablero de Control Mensual

| Perspectiva | KPI | Valor | Meta | 🟢🟡🔴 |
|---|---|---|---|---|
| **Financiera** | MRR | — | ≥ $5,000 | — |
| | Margen Bruto | — | ≥ 60% | — |
| | CAC | — | ≤ $1,500 | — |
| **Clientes** | NPS | — | ≥ 50 | — |
| | Retención | — | ≥ 70% | — |
| | Churn | — | ≤ 10% | — |
| **Procesos** | On-Time Delivery | — | ≥ 90% | — |
| | Ciclo Promedio | — | ≤ 21 días | — |
| | QA Pass Rate | — | ≥ 80% | — |
| **Aprendizaje** | Items Creados | — | ≥ 3/mes | — |
| | Tasa Reutilización | — | ≥ 80% | — |
| | Post-Mortem | — | 100% | — |
| **Health Score** | — | — | ≥ 80% | — |

### 7.3 Cómo se Llena el Dashboard

| Frecuencia | Quién | Cómo |
|---|---|---|
| **Diario** | Cada persona | Actualiza su pipeline, estado de proyectos, cobranzas |
| **Semanal** | Ventas + Delivery + CS | Pre-work 15 min antes de Weekly Ops |
| **Mensual** | Director | Consolidación antes de Monthly KPI Review |

---

## 8. Plan de Contingencia

### 8.1 Escenarios de Riesgo

| Riesgo | Probabilidad | Impacto | Plan de Contingencia |
|---|---|---|---|
| **Baja demanda / leads insuficientes** | Media | Alto | Intensificar outbound, activar alianzas, reducir gastos |
| **Cliente insatisfecho (NPS bajo)** | Media | Alto | Protocolo de recuperación (Director contacta en 24h) |
| **Error en diagnóstico (datos incorrectos)** | Baja | Muy alto | QA obligatorio, doble verificación de datos numéricos |
| **Fuga de información confidencial** | Baja | Muy alto | NDA obligatorio, acceso restringido, 2FA |
| **Enfermedad / ausencia de miembro clave** | Media | Alto | Procesos documentados permiten reemplazo temporal |
| **Problema de liquidez (cobranza lenta)** | Media | Alto | Seguimiento agresivo de cobranza, adelanto de pagos |
| **Obsolescencia de knowledge/frameworks** | Baja | Medio | Revisión trimestral de Knowledge/ |

### 8.2 Plan de Continuidad por Rol

| Rol Ausente | Reemplazo | Tiempo de Transferencia |
|---|---|---|
| **Delivery Lead** | Otro Delivery Lead o Director | 1-2 días |
| **Ventas** | Director (temporal) + proceso documentado | Inmediato |
| **Admin** | Director + plantillas y automatizaciones | 2-3 días |
| **CS** | Delivery Lead (temporal) | 1 día |

### 8.3 Backup y Recuperación de Datos

| Activo | Backup | Frecuencia | Tiempo de Recuperación |
|---|---|---|---|
| Google Sheets | Google Drive (version history) | Continua | Inmediato |
| Documentos de clientes | Google Drive | Continua | Inmediato |
| Knowledge/ (Git) | GitHub + cloud | Por commit | Inmediato |
| Contabilidad | Google Drive + contador externo | Mensual | 1-2 días |
| Contratos firmados | Google Drive + firma digital | Por contrato | Inmediato |

---

## 9. Glosario

| Término | Definición |
|---|---|
| **Agente** | Sistema de IA especializado en una dimensión de diagnóstico |
| **BANT** | Budget, Authority, Need, Timeline — criterios de calificación de leads |
| **CRM** | Customer Relationship Management — gestión de relaciones con clientes |
| **CS** | Customer Success — éxito del cliente (post-venta) |
| **Delivery Lead** | Líder de entrega del diagnóstico (orquestador de agentes) |
| **Diagnóstico** | Servicio principal de Klar Analytics: análisis multi-dimensión de una PyME |
| **ERP** | Enterprise Resource Planning — planificación de recursos empresariales |
| **Health Score** | Porcentaje de KPIs en verde — indicador compuesto de salud del negocio |
| **KPI** | Key Performance Indicator — indicador clave de rendimiento |
| **MQL** | Marketing Qualified Lead — lead calificado por marketing |
| **MRR** | Monthly Recurring Revenue — ingresos recurrentes mensuales |
| **NPS** | Net Promoter Score — métrica de satisfacción y lealtad |
| **OPP** | Oportunidad comercial en pipeline |
| **Orchestrator** | Delivery Lead actuando como coordinador de agentes |
| **Playbook** | Procedimiento operativo estandarizado (SOP) |
| **Pipeline** | Tubería de ventas: etapas desde lead a cliente |
| **Post-Mortem** | Revisión post-proyecto para extraer lecciones aprendidas |
| **QA** | Quality Assurance — aseguramiento de calidad |
| **Skill** | Capacidad específica de un agente (ej. Financial_Diagnosis) |
| **SQL** | Sales Qualified Lead — lead calificado por ventas |
| **WON** | Estado de oportunidad ganada (contrato firmado) |

---

## 10. Referencias

### 10.1 Documentos del Sistema Operativo

| Documento | Descripción | Ubicación |
|---|---|---|
| Process_Map | Mapa integral de procesos, subprocesos y RACI | `Operations/Process_Map.md` |
| Sales_Process | Pipeline comercial completo | `Operations/Sales_Process.md` |
| Delivery_Process | Proceso de prestación del servicio | `Operations/Delivery_Process.md` |
| Knowledge_Process | Ciclo de aprendizaje organizacional | `Operations/Knowledge_Process.md` |
| Client_Success_Process | Seguimiento post-diagnóstico | `Operations/Client_Success_Process.md` |
| Administration_Process | Gestión administrativa y financiera | `Operations/Administration_Process.md` |
| Database_Model | Modelo de datos completo | `Operations/Database_Model.md` |
| CRM_Model | Diseño del CRM | `Operations/CRM_Model.md` |
| ERP_Blueprint | Blueprint del ERP futuro | `Operations/ERP_Blueprint.md` |
| KPI_System | Sistema integral de indicadores | `Operations/KPI_System.md` |
| Operating_System_Manual | **Este documento — manual consolidado** | `Operations/Operating_System_Manual.md` |

### 10.2 Recursos del Repositorio

| Recurso | Descripción | Ubicación |
|---|---|---|
| Agentes | Definiciones de los 10 agentes de diagnóstico | `Agents/` |
| Skills | Fichas técnicas de las 8 capacidades de agente | `Skills/` |
| Knowledge CORE | Frameworks y patrones (12+ archivos) | `Knowledge/CORE/` |
| Casos | Diagnósticos completos por cliente | `Knowledge/Casos/` |
| Playbooks | SOPs detallados de entrevista, diagnóstico y consolidación | `Playbooks/` |
| Brand | Identidad visual, tono de voz, logo, guías | `Brand/` |

### 10.3 Frameworks y Metodologías Referenciadas

| Framework | Uso en Klar |
|---|---|
| **EOS (Entrepreneurial Operating System)** | Ritmos de gestión, reuniones, accountability |
| **Balanced Scorecard** | Perspectivas de KPIs (financiera, clientes, procesos, aprendizaje) |
| **OKR** | Alineación estratégica trimestral |
| **RACI** | Matriz de responsabilidades en procesos |
| **RAPID** | Matriz de decisiones |
| **BANT** | Calificación de leads |
| **OODA Loop** | Ciclo de conocimiento (Observe, Orient, Decide, Act) |
| **SMART** | Criterios para objetivos y recomendaciones |

---

## Apéndice A: Checklist de Implementación

- [ ] **Fase 1 — Setup**: Leer todo el Operations/ folder. Comprender la arquitectura.
- [ ] **Fase 2 — CRM**: Implementar CRM MVP en Sheets (siguiendo CRM_Model.md + Database_Model.md).
- [ ] **Fase 3 — Procesos**: Capacitar al equipo en Sales_Process y Delivery_Process.
- [ ] **Fase 4 — KPIs**: Configurar dashboard con KPIs de KPI_System.md.
- [ ] **Fase 5 — Ritmos**: Establecer daily standup, weekly ops review, monthly KPI review.
- [ ] **Fase 6 — Knowledge**: Activar Knowledge_Process con curator designado.
- [ ] **Fase 7 — CS**: Implementar programa de seguimiento post-diagnóstico.
- [ ] **Fase 8 — Admin**: Configurar facturación, cobranza, contratos.
- [ ] **Fase 9 — ERP**: Iniciar desarrollo de migración de Sheets a PostgreSQL.
- [ ] **Fase 10 — Mejora Continua**: Primera revisión trimestral del sistema operativo.

## Apéndice B: Hoja de Ruta de Madurez Operativa

| Nivel | Estado | Características |
|---|---|---|
| **N1 — Caótico** | ❌ | Procesos no documentados, cada quien hace lo suyo, sin KPIs |
| **N2 — Documentado** | 🟡 (actual) | Procesos documentados (este repositorio), implementación parcial en Sheets |
| **N3 — Gestionado** | 🎯 | CRM funcionando, KPIs en dashboard, ritmos establecidos, equipo entrenado |
| **N4 — Automatizado** | 🚀 | Automatizaciones activas, agentes integrados, ERP operativo |
| **N5 — Optimizado** | 🌟 | Mejora continua incorporada, machine learning en diagnósticos, escalado a miles |

---

*Fin del documento — Operating_System_Manual.md v1.0*
