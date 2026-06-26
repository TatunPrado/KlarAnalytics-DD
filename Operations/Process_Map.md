# Mapa Integral de Procesos

> **Sistema Operativo** — Arquitectura de Procesos de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura de Macroprocesos](#1-arquitectura-de-macroprocesos)
2. [Procesos Estratégicos](#2-procesos-estratégicos)
3. [Procesos Comerciales](#3-procesos-comerciales)
4. [Procesos Operativos](#4-procesos-operativos)
5. [Procesos Administrativos](#5-procesos-administrativos)
6. [Procesos de Mejora Continua](#6-procesos-de-mejora-continua)
7. [Flujo Integral: Lead a Learning](#7-flujo-integral-lead-a-learning)
8. [Matriz de Responsabilidades (RACI)](#8-matriz-de-responsabilidades-raci)
9. [Indicadores Globales del Sistema](#9-indicadores-globales-del-sistema)

---

## 1. Arquitectura de Macroprocesos

### 1.1 Cadena de Valor

```
                 ┌────────────────────────────────────────────────────────────┐
                 │                    PROCESOS ESTRATÉGICOS                     │
                 │  Planificación | Marketing | Innovación | Gobierno | KPIs   │
                 └────────────────────────────────────────────────────────────┘
                            ▲                                ▲
                            │                                │
┌───────────────────────────┴────────────────────────────────┴───────────────────────────┐
│                              PROCESOS OPERATIVOS                                        │
│                                                                                         │
│  Lead → Calificación → Descubrimiento → Diagnóstico → Informe → Presentación → Cierre  │
│                                                                                         │
│  [Sales_Process]           [Delivery_Process]                    [Client_Success]       │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                            ▲                                ▲
                            │                                │
                 ┌──────────┴────────────────────────────────┴──────────┐
                 │               PROCESOS DE SOPORTE                     │
                 │  Admin | Facturación | Cobranza | IT | Knowledge     │
                 └───────────────────────────────────────────────────────┘
                            ▲                                ▲
                            │                                │
                 ┌──────────┴────────────────────────────────┴──────────┐
                 │            PROCESOS DE MEJORA CONTINUA                │
                 │  Auditoría | Feedback | Aprendizaje | Optimización   │
                 └───────────────────────────────────────────────────────┘
```

### 1.2 Clasificación de Procesos

| Categoría | ID | Proceso | Responsable |
|---|---|---|---|
| **Estratégicos** | PE-01 | Planificación Estratégica | Dirección |
| | PE-02 | Marketing y Posicionamiento | Dirección / Marketing |
| | PE-03 | Innovación de Servicios | Dirección / Strategy_Designer |
| | PE-04 | Gobierno y Cumplimiento | Dirección |
| | PE-05 | Gestión de KPIs y OKRs | Dirección |
| **Comerciales** | PC-01 | Generación de Leads | Marketing / Ventas |
| | PC-02 | Calificación de Leads | Ventas (CRM) |
| | PC-03 | Descubrimiento y Demo | Ventas |
| | PC-04 | Propuesta y Cierre | Ventas |
| | PC-05 | Onboarding de Clientes | Ventas / Operaciones |
| **Operativos** | PO-01 | Inicio de Diagnóstico | Operaciones |
| | PO-02 | Entrevista y Recolección | Interview_Orchestrator |
| | PO-03 | Análisis Multi-Agente | Agentes de Diagnóstico |
| | PO-04 | Consolidación | Master_Diagnosis_Orch. |
| | PO-05 | Diseño de Iniciativas | Strategy_Designer |
| | PO-06 | Generación de Informe | Executive_Report_Gen. |
| | PO-07 | Presentación al Cliente | Operaciones / Dirección |
| | PO-08 | Cierre y Post-Venta | Client Success |
| **Soporte (Admin)** | PA-01 | Alta de Clientes | Administración |
| | PA-02 | Facturación | Administración |
| | PA-03 | Cobranza | Administración |
| | PA-04 | Gestión Documental | Administración |
| | PA-05 | Contratos | Administración / Legal |
| **Mejora Continua** | PM-01 | Auditoría de Calidad | Calidad |
| | PM-02 | Encuesta de Satisfacción | Client Success |
| | PM-03 | Consolidación de Conocimiento | Knowledge_Consolidator |
| | PM-04 | Revisión de Patrones | Knowledge_Reviewer |
| | PM-05 | Optimización de Procesos | Operaciones |

### 1.3 Mapa de Interacciones entre Procesos

```
PE-01 Planif. Estratégica ──► PC-01 Generación Leads
       │                          │
       ▼                          ▼
PE-02 Marketing ◄────────── PC-02 Calificación
                                     │
                                     ▼
                              PC-03 Descubrimiento
                                     │
                                     ▼
                              PC-04 Propuesta y Cierre
                                     │
                                     ▼
                              PC-05 Onboarding
                                     │
                                     ▼
         ┌─────────────────── PO-01 Inicio Diagnóstico
         │                         │
         │                         ▼
         │                  PO-02 Entrevista y Recolección
         │                         │
         │                         ▼
         │                  PO-03 Análisis Multi-Agente
         │                         │
         │                         ▼
         │                  PO-04 Consolidación
         │                         │
         │                         ▼
         │                  PO-05 Diseño de Iniciativas
         │                         │
         │                         ▼
         │                  PO-06 Generación de Informe
         │                         │
         │                         ▼
         │                  PO-07 Presentación al Cliente
         │                         │
         │                         ├─────────────────────┐
         │                         │                     │
         ▼                         ▼                     ▼
PA-01 Alta Cliente ◄────── PO-08 Cierre         PM-02 Encuesta
PA-02 Facturación                                     │
PA-03 Cobranza                                        ▼
PA-04 Gestión Doc.                             PM-03 Consolidación
PA-05 Contratos                                       │
                                                      ▼
                                               PM-04 Revisión Patrones
                                                      │
                                                      ▼
                                               PM-05 Optimización
                                                      │
                                                      ▼
                                               PE-03 Innovación
```

---

## 2. Procesos Estratégicos

### 2.1 PE-01: Planificación Estratégica

| Atributo | Descripción |
|---|---|
| **Objetivo** | Definir la dirección estratégica de la consultora, incluyendo metas de crecimiento, posicionamiento y capacidades |
| **Responsable** | Dirección (socios fundadores) |
| **Inputs** | Dashboard de KPIs, tendencias de mercado, resultados de auditorías de calidad, capacidad del equipo |
| **Outputs** | OKRs trimestrales, prioridades estratégicas, presupuesto asignado |
| **Documentos** | `Plan_Estrategico_Anual.md`, `OKRs_Trimestre.json`, `Budget_Allocation.md` |
| **Indicadores** | OKR achievement rate ≥ 70%, revenue growth ≥ 30% YoY |
| **Dependencias** | PE-05 (KPIs), PM-05 (Optimización) |
| **Frecuencia** | Trimestral (revisión), anual (definición) |

### 2.2 PE-02: Marketing y Posicionamiento

| Atributo | Descripción |
|---|---|
| **Objetivo** | Construir autoridad de marca, generar demanda calificada y posicionar a Klar Analytics como referente en diagnóstico empresarial con IA |
| **Responsable** | Dirección / Marketing |
| **Inputs** | Brand_Strategy, Tone_of_Voice, buyer personas, datos de mercado |
| **Outputs** | Calendario editorial, campañas, contenido publicado, leads generados |
| **Documentos** | `Content_Calendar.md`, `Campaign_Reports.md`, `Industry_POVs.md` |
| **Indicadores** | MQLs/mes ≥ 20, SQL conversion rate ≥ 15%, website traffic growth ≥ 40% YoY |
| **Dependencias** | PE-01 (Estrategia), Brand/ (guías de marca) |
| **Frecuencia** | Semanal (ejecución), mensual (reporte) |

### 2.3 PE-03: Innovación de Servicios

| Atributo | Descripción |
|---|---|
| **Objetivo** | Desarrollar nuevos servicios, mejorar los existentes e incorporar nuevas capacidades de IA basadas en aprendizaje organizacional |
| **Responsable** | Dirección / Strategy_Designer |
| **Inputs** | Patrones de Knowledge/Learned, feedback de clientes, tendencias de IA, brechas de cobertura |
| **Outputs** | Nuevos skills, nuevos frameworks, nuevos playbooks o servicios |
| **Documentos** | `Service_Blueprint.md`, `AI_Opportunity_Canvas.md`, `Release_Notes.md` |
| **Indicadores** | Nuevos servicios/año ≥ 2, time-to-market ≤ 90 días |
| **Dependencias** | PM-03 (Consolidación), PM-02 (Feedback) |
| **Frecuencia** | Mensual (revisión de oportunidades), trimestral (lanzamiento) |

### 2.4 PE-04: Gobierno y Cumplimiento

| Atributo | Descripción |
|---|---|
| **Objetivo** | Garantizar que la operación cumpla con regulaciones aplicables, estándares de seguridad de la información y mejores prácticas de gobierno |
| **Responsable** | Dirección |
| **Inputs** | Regulaciones (GDPR, Ley de Protección de Datos local), políticas de seguridad, resultados de auditorías |
| **Outputs** | Políticas actualizadas, registros de cumplimiento, planes de acción |
| **Documentos** | `Security_Policy.md`, `Data_Protection_Register.md`, `Compliance_Checklist.md` |
| **Indicadores** | Auditorías sin hallazgos críticos ≥ 90%, time-to-close de hallazgos ≤ 15 días |
| **Dependencias** | PM-01 (Auditoría) |
| **Frecuencia** | Continua (monitoreo), trimestral (revisión formal) |

### 2.5 PE-05: Gestión de KPIs y OKRs

| Atributo | Descripción |
|---|---|
| **Objetivo** | Monitorear el desempeño global de la consultora a través de indicadores clave y asegurar la alineación estratégica |
| **Responsable** | Dirección |
| **Inputs** | Datos de CRM, datos financieros, encuestas de satisfacción, métricas operativas |
| **Outputs** | Dashboard ejecutivo, reportes de desempeño, alertas de desviación |
| **Documentos** | `KPI_System.md` (referencia), `Executive_Dashboard.json`, `Monthly_Review.md` |
| **Indicadores** | Dashboard actualización ≤ 24h, alertas respondidas ≤ 48h |
| **Dependencias** | Todos los procesos (reportan métricas) |
| **Frecuencia** | Tiempo real (dashboard), semanal (revisión), mensual (reporte formal) |

---

## 3. Procesos Comerciales

### 3.1 PC-01: Generación de Leads

| Atributo | Descripción |
|---|---|
| **Objetivo** | Atraer prospectos calificados hacia el pipeline comercial |
| **Responsable** | Marketing (con apoyo de Dirección) |
| **Inputs** | Contenido (artículos, whitepapers, casos de estudio), campañas (LinkedIn, Google Ads, email), referidos, alianzas |
| **Outputs** | Leads en CRM con fuente, fecha y perfil básico |
| **Documentos** | `Lead_Record` en CRM (nombre, empresa, cargo, email, teléfono, fuente, fecha) |
| **Indicadores** | MQLs/mes, Costo por Lead (CPL), Lead-to-Opportunity rate |
| **Dependencias** | PE-02 (Marketing), Brand/ (contenido) |
| **Detalle** | Ver Sales_Process.md |

### 3.2 PC-02: Calificación de Leads

| Atributo | Descripción |
|---|---|
| **Objetivo** | Evaluar si un lead cumple los criterios mínimos para ser una oportunidad comercial |
| **Responsable** | Ventas (CRM Agent) |
| **Inputs** | Lead Record, BANT criteria (Budget, Authority, Need, Timeline) |
| **Outputs** | Lead calificado (SQL) o lead rechazado con motivo |
| **Documentos** | `Lead_Score`, `Qualification_Checklist.md` |
| **Indicadores** | Lead-to-SQL rate ≥ 25%, time-to-qualify ≤ 24h |
| **Dependencias** | PC-01 |
| **Detalle** | Ver Sales_Process.md |

### 3.3 PC-03: Descubrimiento y Demo

| Atributo | Descripción |
|---|---|
| **Objetivo** | Entender la necesidad del prospecto, demostrar el valor del diagnóstico y evaluar fit |
| **Responsable** | Ventas / Interview_Orchestrator |
| **Inputs** | Lead calificado, brief inicial del prospecto |
| **Outputs** | Discovery notes, fit assessment, next steps acordados |
| **Documentos** | `Discovery_Notes.md`, `Fit_Assessment.md` |
| **Indicadores** | SQL-to-Opportunity rate ≥ 50%, discovery meetings/mes |
| **Dependencias** | PC-02 |
| **Detalle** | Ver Sales_Process.md |

### 3.4 PC-04: Propuesta y Cierre

| Atributo | Descripción |
|---|---|
| **Objetivo** | Preparar y presentar una propuesta comercial alineada a la necesidad detectada, negociar y cerrar |
| **Responsable** | Ventas / Dirección |
| **Inputs** | Discovery notes, scope definition, pricing guidelines |
| **Outputs** | Propuesta firmada → contrato → comprobante de pago inicial |
| **Documentos** | `Proposal_Template.md`, `Contract_Template.md`, `Order_Form.md` |
| **Indicadores** | Win rate ≥ 35%, avg. sales cycle ≤ 21 días, avg. ticket |
| **Dependencias** | PC-03, PA-05 (Contratos) |
| **Detalle** | Ver Sales_Process.md |

### 3.5 PC-05: Onboarding de Clientes

| Atributo | Descripción |
|---|---|
| **Objetivo** | Incorporar al cliente de forma estructurada, recolectar información inicial y activar el diagnóstico |
| **Responsable** | Ventas → Operaciones |
| **Inputs** | Contrato firmado, datos de facturación, acceso a información del cliente |
| **Outputs** | Cliente activado en CRM, caso creado en sistema de diagnóstico, kickoff agendado |
| **Documentos** | `Onboarding_Checklist.md`, `Client_Welcome_Kit.md` |
| **Indicadores** | Time-to-kickoff ≤ 5 días, onboarding completion rate = 100% |
| **Dependencias** | PC-04, PA-01 (Alta de Clientes) |
| **Detalle** | Ver Sales_Process.md |

---

## 4. Procesos Operativos

### 4.1 PO-01: Inicio de Diagnóstico

| Atributo | Descripción |
|---|---|
| **Objetivo** | Iniciar formalmente el diagnóstico, asignar recursos y preparar el sistema multi-agente |
| **Responsable** | Operaciones / Master_Diagnosis_Orchestrator |
| **Inputs** | Cliente activado (PC-05), datos de onboarding, tipo de diagnóstico contratado |
| **Outputs** | Diagnóstico creado en sistema, agentes asignados, cronograma definido |
| **Documentos** | `Diagnosis_Order.json`, `Case_Assignment.md`, `Timeline.md` |
| **Indicadores** | Time-to-start ≤ 2 días post-onboarding |
| **Dependencias** | PC-05 |
| **Detalle** | Ver Delivery_Process.md |

### 4.2 PO-02: Entrevista y Recolección

| Atributo | Descripción |
|---|---|
| **Objetivo** | Realizar la entrevista de descubrimiento empresarial y recolectar toda la documentación necesaria |
| **Responsable** | Interview_Orchestrator |
| **Inputs** | Diagnosis order, datos del cliente, plantilla de entrevista |
| **Outputs** | Brief_Empresa.md, interview_transcript.md, documentos del cliente |
| **Documentos** | `Brief_Empresa.md`, `Document_Inventory.md` |
| **Indicadores** | Entrevista completada ≤ 5 días, documentación obtenida ≥ 80% de la solicitada |
| **Dependencias** | PO-01, Playbooks/Discovery_Interview.md |
| **Detalle** | Ver Delivery_Process.md |

### 4.3 PO-03: Análisis Multi-Agente

| Atributo | Descripción |
|---|---|
| **Objetivo** | Ejecutar los diagnósticos especializados en paralelo usando los agentes, skills y knowledge correspondientes |
| **Responsable** | Agentos de Diagnóstico (Business_Model, Financial, Operations, Organization, Risk) |
| **Inputs** | Brief_Empresa.md, documentos del cliente, Knowledge/Core, Skills, Frameworks |
| **Outputs** | Diagnósticos individuales por dimensión |
| **Documentos** | `bm_assessment_report.md`, `financial_analysis.md`, `operations_report.md`, `org_assessment.md`, `risk_matrix.json` |
| **Indicadores** | Todos los diagnósticos completados ≤ 7 días, cobertura de patrones ≥ 70% |
| **Dependencias** | PO-02, Skills/, Knowledge/, Agents/ |
| **Detalle** | Ver Delivery_Process.md |

### 4.4 PO-04: Consolidación

| Atributo | Descripción |
|---|---|
| **Objetivo** | Unificar hallazgos, eliminar duplicidades, resolver contradicciones e identificar causas raíz |
| **Responsable** | Master_Diagnosis_Orchestrator |
| **Inputs** | Todos los diagnósticos de PO-03, Brief_Empresa.md |
| **Outputs** | Diagnóstico integrado, causas raíz identificadas, problemas priorizados |
| **Documentos** | `consolidated_findings.json`, `root_cause_analysis.json`, `prioritized_problems.json` |
| **Indicadores** | Consolidación ≤ 2 días, contradicciones resueltas = 100% |
| **Dependencias** | PO-03 (mínimo 3 de 5 diagnósticos) |
| **Detalle** | Ver Delivery_Process.md, Playbooks/Full_Business_Diagnosis.md |

### 4.5 PO-05: Diseño de Iniciativas

| Atributo | Descripción |
|---|---|
| **Objetivo** | Diseñar iniciativas de mejora, evaluar oportunidades de IA, construir roadmap |
| **Responsable** | Strategy_Designer / AI_Transformation_Designer |
| **Inputs** | Problemas priorizados, causas raíz, hallazgos consolidados |
| **Outputs** | Catálogo de iniciativas, business cases, roadmap |
| **Documentos** | `initiatives_catalog.json`, `ai_opportunities.json`, `roadmap.json` |
| **Indicadores** | Iniciativas diseñadas para Top 5 problemas, business case completo por iniciativa |
| **Dependencias** | PO-04 |
| **Detalle** | Ver Delivery_Process.md |

### 4.6 PO-06: Generación de Informe

| Atributo | Descripción |
|---|---|
| **Objetivo** | Producir el informe ejecutivo final en formato presentable al cliente |
| **Responsable** | Executive_Report_Generator |
| **Inputs** | Todos los outputs de PO-03 a PO-05, Brand/ (identidad visual) |
| **Outputs** | Informe ejecutivo (.docx/.pdf), presentación, resumen ejecutivo |
| **Documentos** | `executive_report.docx`, `presentation.pptx`, `executive_summary.md` |
| **Indicadores** | Informe generado ≤ 2 días, sin errores de formato |
| **Dependencias** | PO-05, Brand/, Templates/ |
| **Detalle** | Ver Delivery_Process.md |

### 4.7 PO-07: Presentación al Cliente

| Atributo | Descripción |
|---|---|
| **Objetivo** | Presentar los hallazgos y recomendaciones al cliente, responder preguntas y acordar próximos pasos |
| **Responsable** | Dirección / Master_Diagnosis_Orchestrator |
| **Inputs** | Informe ejecutivo, presentación |
| **Outputs** | Cliente informado, preguntas resueltas, próximos pasos acordados |
| **Documentos** | `Presentation_Feedback.md`, `Next_Steps_Agreement.md` |
| **Indicadores** | Presentación ≤ 30 días desde inicio, cliente entiende hallazgos (score ≥ 4/5) |
| **Dependencias** | PO-06 |
| **Detalle** | Ver Delivery_Process.md |

### 4.8 PO-08: Cierre y Post-Venta

| Atributo | Descripción |
|---|---|
| **Objetivo** | Cerrar formalmente el diagnóstico, recolectar feedback, activar procesos de post-venta y aprendizaje |
| **Responsable** | Client Success / Operaciones |
| **Inputs** | Feedback del cliente, resultados de presentación |
| **Outputs** | Caso cerrado, encuesta enviada, lecciones aprendidas registradas |
| **Documentos** | `Case_Closure.md`, `Satisfaction_Survey.md`, `Lessons_Learned.md` |
| **Indicadores** | NPS ≥ 50, encuesta completada ≤ 5 días post-cierre |
| **Dependencias** | PO-07, PM-02 (Encuesta) |
| **Detalle** | Ver Client_Success_Process.md |

---

## 5. Procesos Administrativos

### 5.1 PA-01: Alta de Clientes

| Atributo | Descripción |
|---|---|
| **Objetivo** | Registrar al cliente en el sistema con todos los datos necesarios para operación y facturación |
| **Responsable** | Administración |
| **Inputs** | Contrato firmado, datos fiscales, datos de contacto |
| **Outputs** | Cliente creado en CRM + ERP, expediente documental iniciado |
| **Documentos** | `Client_Record`, `Tax_Info_Form`, `Expediente_Cliente.md` |
| **Indicadores** | Alta completada ≤ 24h del contrato, datos 100% verificados |
| **Dependencias** | PC-04 (Contrato firmado) |
| **Detalle** | Ver Administration_Process.md |

### 5.2 PA-02: Facturación

| Atributo | Descripción |
|---|---|
| **Objetivo** | Emitir facturas según lo contratado, en tiempo y forma |
| **Responsable** | Administración |
| **Inputs** | Orden de facturación (hito cumplido o fecha de ciclo), datos fiscales del cliente |
| **Outputs** | Factura emitida (electrónica), registro contable |
| **Documentos** | `Invoice.xml/.pdf`, `Receivables_Register.md` |
| **Indicadores** | Facturas emitidas ≤ 3 días del hito, tasa de error ≤ 1% |
| **Dependencias** | PA-01, PO-01 |
| **Detalle** | Ver Administration_Process.md |

### 5.3 PA-03: Cobranza

| Atributo | Descripción |
|---|---|
| **Objetivo** | Gestionar el cobro de las facturas emitidas, minimizando días de cobro y morosidad |
| **Responsable** | Administración |
| **Inputs** | Factura emitida, condiciones de pago del contrato |
| **Outputs** | Pago registrado, conciliación bancaria |
| **Documentos** | `Aging_Report.md`, `Collection_Action_Log.md` |
| **Indicadores** | DSO ≤ 30 días, aging > 60 días ≤ 5% de cartera |
| **Dependencias** | PA-02 |
| **Detalle** | Ver Administration_Process.md |

### 5.4 PA-04: Gestión Documental

| Atributo | Descripción |
|---|---|
| **Objetivo** | Almacenar, organizar y proteger toda la documentación de clientes y operativa |
| **Responsable** | Administración / Sistemas |
| **Inputs** | Documentos de clientes, informes, contratos, facturas |
| **Outputs** | Archivo digital organizado, backups, política de retención aplicada |
| **Documentos** | `Document_Index.md`, `Retention_Policy.md`, `Backup_Log.md` |
| **Indicadores** | Documentos indexados = 100%, tiempo de búsqueda ≤ 2 min |
| **Dependencias** | Todos los procesos (generan documentos) |
| **Detalle** | Ver Administration_Process.md |

### 5.5 PA-05: Contratos

| Atributo | Descripción |
|---|---|
| **Objetivo** | Preparar, revisar y gestionar los contratos con clientes y proveedores |
| **Responsable** | Administración / Legal (si aplica) |
| **Inputs** | Propuesta aceptada, datos del cliente |
| **Outputs** | Contrato firmado, archivado, con alertas de renovación |
| **Documentos** | `Contract_Template.md`, `Signed_Contract.pdf`, `Contract_Register.md` |
| **Indicadores** | Tiempo de preparación ≤ 2 días, contratos sin errores legales |
| **Dependencias** | PC-04 |
| **Detalle** | Ver Administration_Process.md |

---

## 6. Procesos de Mejora Continua

### 6.1 PM-01: Auditoría de Calidad

| Atributo | Descripción |
|---|---|
| **Objetivo** | Evaluar la calidad de los diagnósticos entregados contra estándares definidos |
| **Responsable** | Calidad (rol rotativo entre agentes seniors) |
| **Inputs** | Diagnósticos completados, checklist de calidad, estándares definidos |
| **Outputs** | Reporte de auditoría, hallazgos de calidad, plan de acciones correctivas |
| **Documentos** | `Quality_Audit_Report.md`, `Quality_Scorecard.md` |
| **Indicadores** | Calidad score ≥ 85%, hallazgos cerrados ≤ 30 días |
| **Dependencias** | PO-08, Operating_System_Manual.md |
| **Frecuencia** | Muestreo del 20% de diagnósticos completados |

### 6.2 PM-02: Encuesta de Satisfacción

| Atributo | Descripción |
|---|---|
| **Objetivo** | Medir la satisfacción del cliente post-diagnóstico y detectar áreas de mejora |
| **Responsable** | Client Success |
| **Inputs** | Contacto del cliente, diagnóstico completado |
| **Outputs** | Encuesta completada, NPS calculado, feedback cualitativo |
| **Documentos** | `NPS_Survey.md`, `Feedback_Analysis.md` |
| **Indicadores** | Tasa de respuesta ≥ 60%, NPS ≥ 50 |
| **Dependencias** | PO-08 |
| **Detalle** | Ver Client_Success_Process.md |

### 6.3 PM-03: Consolidación de Conocimiento

| Atributo | Descripción |
|---|---|
| **Objetivo** | Extraer patrones y aprendizajes de los diagnósticos completados para mejorar la base de conocimiento |
| **Responsable** | Knowledge_Consolidator |
| **Inputs** | Diagnósticos completados, hallazgos, resultados |
| **Outputs** | Nuevos patrones, patrones enriquecidos, métricas de conocimiento |
| **Documentos** | Ver Knowledge_Process.md, Playbooks/Knowledge_Consolidation.md |
| **Indicadores** | Nuevos patrones/semana, precisión del conocimiento ≥ 80% |
| **Dependencias** | PO-08, Playbooks/Knowledge_Consolidation.md |
| **Detalle** | Ver Knowledge_Process.md |

### 6.4 PM-04: Revisión de Patrones

| Atributo | Descripción |
|---|---|
| **Objetivo** | Evaluar patrones candidatos en Knowledge/Learned para promoción a Knowledge/Core |
| **Responsable** | Knowledge_Reviewer |
| **Inputs** | Patrones en Learned con soporte ≥ 10 y confianza ≥ 0.80 |
| **Outputs** | Patrones promovidos a Core, patrones rechazados con retroalimentación |
| **Documentos** | `Promotion_Review.md`, `Core_Update_Log.json` |
| **Indicadores** | Promociones/mes, tiempo promedio en Learned antes de promoción |
| **Dependencias** | PM-03 |
| **Frecuencia** | Mensual |

### 6.5 PM-05: Optimización de Procesos

| Atributo | Descripción |
|---|---|
| **Objetivo** | Identificar y ejecutar mejoras en los procesos operativos de la consultora |
| **Responsable** | Operaciones |
| **Inputs** | Auditorías de calidad, feedback de clientes, feedback del equipo, métricas de procesos |
| **Outputs** | Procesos optimizados, procedimientos actualizados, KPIs mejorados |
| **Documentos** | `Process_Improvement_Log.md`, `Updated_Procedures.md` |
| **Indicadores** | Reducción de tiempo de ciclo ≥ 10% anual, reducción de errores ≥ 15% anual |
| **Dependencias** | PM-01, PM-02 |
| **Frecuencia** | Continua (revisión mensual formal) |

---

## 7. Flujo Integral: Lead a Learning

```
FASE 1: CAPTURA COMERCIAL (Sales_Process)
═══════════════════════════════════════════════════════

Lead → Calificación → Discovery → Propuesta → Cierre → Onboarding
 │          │             │           │          │         │
 │          │             │           │          │         └──► Cliente activado
 │          │             │           │          │              en CRM + ERP
 │          │             │           │          └──► Contrato firmado
 │          │             │           │               Factura inicial emitida
 │          │             │           └──► Propuesta enviada
 │          │             │                Pricing aprobado
 │          │             └──► Fit assessment completado
 │          │                  Scope preliminar definido
 │          └──► Lead calificado (SQL)
 │               BANT validado
 └──► Lead raw inbound/outbound

FASE 2: EJECUCIÓN DEL DIAGNÓSTICO (Delivery_Process)
═══════════════════════════════════════════════════════

Inicio → Entrevista → Recolección → Análisis → Consolidación → Informe → Presentación
  │         │            │           │            │             │         │
  │         │            │           │            │             │         └──► Cliente
  │         │            │           │            │             │              informado
  │         │            │           │            │             └──► Reporte final .docx
  │         │            │           │            │                  Presentación PPT
  │         │            │           │            └──► Causas raíz identificadas
  │         │            │           │                 Problemas priorizados
  │         │            │           └──► 5 diagnósticos completados
  │         │            │                Business Model
  │         │            │                Financial
  │         │            │                Operations
  │         │            │                Organization
  │         │            │                Risk
  │         │            └──► Documentación del cliente recibida
  │         │                 Document_Inventory actualizado
  │         └──► Brief_Empresa.md completado
  │              Transcript de entrevista
  └──► Caso creado en sistema
       Agentes asignados
       Timeline definido

FASE 3: POST-VENTA Y APRENDIZAJE (Client_Success + Knowledge)
═══════════════════════════════════════════════════════

Cierre → Encuesta → Consolidación Conocimiento → Actualización Core → Optimización
  │         │               │                         │                  │
  │         │               │                         │                  └──► Procesos
  │         │               │                         │                       mejorados
  │         │               │                         │                       KPIs suben
  │         │               │                         └──► Nuevos patrones Core
  │         │               │                              Agentes más precisos
  │         │               └──► Patrones Learned
  │         │                    Knowledge/Learned actualizado
  │         └──► NPS calculado
  │              Feedback documentado
  └──► Caso marcado como completado
       Lecciones aprendidas registradas
```

---

## 8. Matriz de Responsabilidades (RACI)

| Proceso | Dirección | Ventas | Operaciones | Admin | Cliente | IA/Agentes |
|---|---|---|---|---|---|---|
| **PE-01** Planif. Estratégica | **R/A** | C | C | C | I | C |
| **PE-02** Marketing | **A** | C | I | I | I | R |
| **PE-03** Innovación | **A** | I | C | I | C | R |
| **PE-04** Gobierno | **R/A** | I | C | C | I | I |
| **PE-05** KPIs | **A** | C | R | C | I | **R** |
| **PC-01** Generación Leads | C | **R** | I | I | I | R |
| **PC-02** Calificación | I | **R/A** | I | I | I | R |
| **PC-03** Discovery | I | **R** | C | I | C | C |
| **PC-04** Propuesta/Cierre | A | **R** | I | C | C | I |
| **PC-05** Onboarding | I | **R** | C | C | C | I |
| **PO-01** Inicio Diagnóstico | I | I | **R** | C | I | A |
| **PO-02** Entrevista | I | I | **A** | I | R | **R** |
| **PO-03** Análisis | I | I | **A** | I | I | **R** |
| **PO-04** Consolidación | C | I | **A** | I | I | **R** |
| **PO-05** Iniciativas | C | I | **A** | I | I | **R** |
| **PO-06** Informe | I | I | **A** | I | I | **R** |
| **PO-07** Presentación | **R/A** | I | C | I | C | C |
| **PO-08** Cierre | I | C | **R** | C | C | I |
| **PA-01** Alta Clientes | I | C | C | **R/A** | C | I |
| **PA-02** Facturación | I | I | C | **R/A** | I | I |
| **PA-03** Cobranza | I | I | I | **R/A** | C | I |
| **PA-04** Gestión Doc. | I | I | C | **R/A** | I | I |
| **PA-05** Contratos | A | C | I | **R** | C | I |
| **PM-01** Auditoría | **A** | I | R | I | I | C |
| **PM-02** Encuesta | I | I | **R** | C | C | I |
| **PM-03** Conocimiento | I | I | A | I | I | **R** |
| **PM-04** Revisión Patrones | A | I | C | I | I | **R** |
| **PM-05** Optimización | A | I | **R** | C | I | C |

**Leyenda:** R = Responsable, A = Aprueba, C = Consultado, I = Informado

---

## 9. Indicadores Globales del Sistema

| Indicador | Fórmula | Frecuencia | Responsable | Meta | Semáforo |
|---|---|---|---|---|---|
| **Lead Conversion Rate** | SQL / MQL | Semanal | Ventas | ≥ 25% | 🔴 < 15% 🟡 15-25% 🟢 ≥ 25% |
| **Win Rate** | Oportunidades ganadas / total | Mensual | Ventas | ≥ 35% | 🔴 < 25% 🟡 25-35% 🟢 ≥ 35% |
| **Avg. Sales Cycle** | Días desde SQL → Cierre | Mensual | Ventas | ≤ 21 días | 🔴 > 30 🟡 21-30 🟢 ≤ 21 |
| **Time-to-Kickoff** | Días desde pago a inicio | Por caso | Operaciones | ≤ 5 días | 🔴 > 8 🟡 5-8 🟢 ≤ 5 |
| **Diagnóstico Completo** | Días desde inicio a entrega | Por caso | Operaciones | ≤ 14 días | 🔴 > 21 🟡 14-21 🟢 ≤ 14 |
| **Calidad del Informe** | Score de auditoría | Muestreo | Calidad | ≥ 85% | 🔴 < 70% 🟡 70-85% 🟢 ≥ 85% |
| **NPS** | Promotores - Detractores | Mensual | Client Success | ≥ 50 | 🔴 < 30 🟡 30-50 🟢 ≥ 50 |
| **DSO** | (Cuentas por cobrar / facturación) × 30 | Mensual | Admin | ≤ 30 días | 🔴 > 45 🟡 30-45 🟢 ≤ 30 |
| **Knowledge Coverage** | % hallazgos explicables por patrones Core | Mensual | Knowledge | ≥ 70% | 🔴 < 55% 🟡 55-70% 🟢 ≥ 70% |
| **Precisión Patrones** | Tasa de aciertos en predicciones | Mensual | Knowledge | ≥ 80% | 🔴 < 70% 🟡 70-80% 🟢 ≥ 80% |

---

*Fin del documento — Process_Map.md v1.0*
