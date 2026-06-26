# Modelo de Base de Datos

> **Sistema Operativo** — Database Model de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura de Datos](#1-arquitectura-de-datos)
2. [Modelo Entidad-Relación](#2-modelo-entidad-relación)
3. [Catálogo de Tablas](#3-catálogo-de-tablas)
4. [Diccionario de Datos](#4-diccionario-de-datos)
5. [Vistas y Reportes](#5-vistas-y-reportes)
6. [Implementación en Sheets](#6-implementación-en-sheets)
7. [Migración a PostgreSQL](#7-migración-a-postgresql)

---

## 1. Arquitectura de Datos

### 1.1 Principios

| Principio | Descripción |
|---|---|
| **Integridad Referencial** | Todas las relaciones entre tablas deben ser consistentes |
| **Single Source of Truth** | Cada dato se almacena una sola vez |
| **Auditable** | Todo cambio tiene trazabilidad (fecha, usuario, acción) |
| **Evolutivo** | Diseñado para migrar de Sheets a PostgreSQL sin reingeniería |
| **Seguro** | Datos de clientes protegidos, acceso por roles |

### 1.2 Stack de Datos

| Capa | Herramienta Actual | Herramienta Futura |
|---|---|---|
| **Base de datos operacional** | Google Sheets | PostgreSQL (Supabase/RDS) |
| **CRM** | Google Sheets + Manual | HubSpot / Salesforce / Custom |
| **ERP** | Google Sheets | Odoo / Custom |
| **BI / Dashboards** | Google Data Studio (Looker) | Metabase / Superset |
| **Backup** | Google Drive | AWS S3 / Backups automáticos |

---

## 2. Modelo Entidad-Relación

### 2.1 Diagrama de Entidades

```
┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│   Company    │1──N│    Contact       │N──1│    User      │
│  (Cliente)   │    │  (Personas)      │    │  (Equipo)    │
└──────┬───────┘    └──────────────────┘    └──────────────┘
       │                                              
       │1                                             
       │                                              
┌──────▼───────┐    ┌──────────────────┐    ┌──────────────┐
│   Contract   │1──N│  Diagnosis       │1──N│ AgentOutput  │
│  (Contrato)  │    │  (Diagnóstico)   │    │(Output Agte) │
└──────┬───────┘    └──────┬───────────┘    └──────────────┘
       │                   │
       │N                  │1
       │                   │
┌──────▼───────┐    ┌──────▼───────────┐    ┌──────────────┐
│   Invoice    │    │   Finding        │1──N│ Recommendation│
│  (Factura)   │    │  (Hallazgo)      │    │(Recomendación)│
└──────────────┘    └──────────────────┘    └──────────────┘

┌──────────────┐    ┌──────────────────┐
│   Payment    │    │  KpiLog          │
│  (Pago)      │    │(Historial KPI)   │
└──────────────┘    └──────────────────┘

┌──────────────┐    ┌──────────────────┐
│   Knowledge  │    │  Interaction     │
│  (Artículo)  │    │(Interacción Cli) │
└──────────────┘    └──────────────────┘
```

### 2.2 Relaciones Clave

| Entidad Padre | Entidad Hija | Cardinalidad | Campo Clave |
|---|---|---|---|
| Company | Contact | 1:N | company_id |
| Company | Contract | 1:N | company_id |
| Contract | Diagnosis | 1:N | contract_id |
| Diagnosis | Finding | 1:N | diagnosis_id |
| Finding | Recommendation | 1:N | finding_id |
| Contract | Invoice | 1:N | contract_id |
| Invoice | Payment | 1:N | invoice_id |
| Diagnosis | AgentOutput | 1:N | diagnosis_id |

---

## 3. Catálogo de Tablas

### 3.1 Company (Cliente)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| company_id | UUID / INTEGER | ID único | PK |
| legal_name | VARCHAR(200) | Razón social | Sí |
| trade_name | VARCHAR(200) | Nombre de fantasía | No |
| tax_id | VARCHAR(50) | RUT/CUIT/NIT | Sí |
| industry | VARCHAR(100) | Industria | Sí |
| size | VARCHAR(20) | Micro/Pequeña/Mediana | Sí |
| employees | INTEGER | Número de empleados | Sí |
| annual_revenue | DECIMAL(12,2) | Facturación anual (USD) | No |
| website | VARCHAR(200) | Sitio web | No |
| address | TEXT | Dirección fiscal | Sí |
| country | VARCHAR(50) | País | Sí |
| status | VARCHAR(20) | lead/sql/opp/won/lost/active/archived | Sí |
| source | VARCHAR(50) | Canal de origen | Sí |
| created_at | TIMESTAMP | Fecha de creación | Sí |
| updated_at | TIMESTAMP | Última actualización | Sí |

### 3.2 Contact (Contacto)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| contact_id | UUID / INTEGER | ID único | PK |
| company_id | UUID / INTEGER | ID de empresa | FK |
| full_name | VARCHAR(150) | Nombre completo | Sí |
| email | VARCHAR(200) | Email | Sí |
| phone | VARCHAR(50) | Teléfono | No |
| role | VARCHAR(100) | Cargo / Rol | Sí |
| is_decision_maker | BOOLEAN | ¿Toma decisiones? | Sí |
| is_billing_contact | BOOLEAN | ¿Contacto de facturación? | No |
| notes | TEXT | Notas adicionales | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |

### 3.3 User (Equipo Klar)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| user_id | UUID / INTEGER | ID único | PK |
| full_name | VARCHAR(150) | Nombre completo | Sí |
| email | VARCHAR(200) | Email corporativo | Sí |
| role | VARCHAR(50) | Rol (Director, Ventas, CS, Admin) | Sí |
| is_active | BOOLEAN | ¿Activo en la empresa? | Sí |
| agent_type | VARCHAR(50) | Agente asignado (si aplica) | No |
| created_at | TIMESTAMP | Fecha de alta | Sí |

### 3.4 Contract (Contrato)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| contract_id | UUID / INTEGER | ID único | PK |
| company_id | UUID / INTEGER | ID de empresa | FK |
| contract_type | VARCHAR(50) | service/nda/retainer/addendum | Sí |
| diagnosis_type | VARCHAR(50) | express/integral/premium/retainer | Sí |
| scope_description | TEXT | Alcance detallado | Sí |
| total_amount | DECIMAL(10,2) | Monto total (USD) | Sí |
| currency | VARCHAR(3) | USD / ARS / CLP / etc | Sí |
| payment_scheme | VARCHAR(50) | upfront/50-50/40-40-20/monthly | Sí |
| start_date | DATE | Fecha de inicio | Sí |
| end_date | DATE | Fecha de fin estimada | Sí |
| signed_date | DATE | Fecha de firma | No |
| status | VARCHAR(20) | draft/signed/active/completed/cancelled | Sí |
| pdf_url | VARCHAR(500) | URL del PDF firmado | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |

### 3.5 Diagnosis (Diagnóstico)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| diagnosis_id | UUID / INTEGER | ID único | PK |
| contract_id | UUID / INTEGER | ID de contrato | FK |
| company_id | UUID / INTEGER | ID de empresa | FK |
| status | VARCHAR(20) | kickoff/in_progress/draft/qa/presented/completed | Sí |
| dimensions | TEXT[] | Dimensiones cubiertas (array) | Sí |
| delivery_lead_id | UUID / INTEGER | ID del Delivery Lead | FK |
| kickoff_date | DATE | Fecha de kickoff | Sí |
| presentation_date | DATE | Fecha de presentación | No |
| completion_date | DATE | Fecha de finalización | No |
| nps_score | INTEGER | NPS obtenido (0-10) | No |
| notes | TEXT | Notas internas | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |
| updated_at | TIMESTAMP | Última actualización | Sí |

### 3.6 Finding (Hallazgo)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| finding_id | UUID / INTEGER | ID único | PK |
| diagnosis_id | UUID / INTEGER | ID de diagnóstico | FK |
| agent_type | VARCHAR(50) | Agente que lo identificó | Sí |
| dimension | VARCHAR(50) | Dimensión | Sí |
| title | VARCHAR(200) | Título del hallazgo | Sí |
| description | TEXT | Descripción detallada | Sí |
| severity | VARCHAR(20) | critical/high/medium/low | Sí |
| impact_score | INTEGER | Impacto (1-5) | Sí |
| effort_score | INTEGER | Esfuerzo para resolver (1-5) | Sí |
| priority | VARCHAR(10) | A/B/C/D (de matriz impacto-esfuerzo) | Sí |
| evidence | TEXT | Evidencia o fuente | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |

### 3.7 Recommendation (Recomendación)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| recommendation_id | UUID / INTEGER | ID único | PK |
| finding_id | UUID / INTEGER | ID de hallazgo | FK |
| action | TEXT | Acción recomendada | Sí |
| responsible | VARCHAR(100) | Responsable de ejecución | No |
| timeline | VARCHAR(50) | Corto/Mediano/Largo plazo | Sí |
| kpi_to_measure | VARCHAR(200) | KPI para medir éxito | No |
| estimated_impact | TEXT | Impacto esperado | No |
| status | VARCHAR(20) | pending/in_progress/completed/discarded | Sí |
| completed_date | DATE | Fecha de completitud | No |

### 3.8 Invoice (Factura)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| invoice_id | UUID / INTEGER | ID único | PK |
| company_id | UUID / INTEGER | ID de empresa | FK |
| contract_id | UUID / INTEGER | ID de contrato | FK |
| invoice_number | VARCHAR(50) | Número de factura | Sí |
| amount | DECIMAL(10,2) | Monto | Sí |
| tax_amount | DECIMAL(10,2) | Impuesto | Sí |
| total_amount | DECIMAL(10,2) | Total | Sí |
| currency | VARCHAR(3) | Moneda | Sí |
| issue_date | DATE | Fecha de emisión | Sí |
| due_date | DATE | Fecha de vencimiento | Sí |
| paid_date | DATE | Fecha de pago | No |
| status | VARCHAR(20) | pending/paid/overdue/cancelled | Sí |
| payment_method | VARCHAR(50) | transfer/credit_card/check/crypto | No |
| pdf_url | VARCHAR(500) | URL del PDF | No |

### 3.9 Payment (Pago)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| payment_id | UUID / INTEGER | ID único | PK |
| invoice_id | UUID / INTEGER | ID de factura | FK |
| amount | DECIMAL(10,2) | Monto pagado | Sí |
| payment_date | DATE | Fecha de pago | Sí |
| payment_method | VARCHAR(50) | Método | Sí |
| reference | VARCHAR(200) | Referencia / comprobante | No |
| status | VARCHAR(20) | confirmed/pending/rejected/refunded | Sí |

### 3.10 AgentOutput (Output de Agente)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| output_id | UUID / INTEGER | ID único | PK |
| diagnosis_id | UUID / INTEGER | ID de diagnóstico | FK |
| agent_type | VARCHAR(50) | Tipo de agente | Sí |
| dimension | VARCHAR(50) | Dimensión analizada | Sí |
| input_summary | TEXT | Resumen de inputs | Sí |
| output_content | TEXT | Output completo del agente | Sí |
| findings_count | INTEGER | Hallazgos generados | Sí |
| confidence_score | DECIMAL(3,2) | Score de confianza (0.00-1.00) | No |
| processing_time | INTEGER | Segundos de procesamiento | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |

### 3.11 KpiLog (Historial de KPIs)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| kpi_id | UUID / INTEGER | ID único | PK |
| kpi_name | VARCHAR(100) | Nombre del KPI | Sí |
| value | DECIMAL(12,2) | Valor | Sí |
| unit | VARCHAR(50) | Unidad de medida | Sí |
| recorded_at | DATE | Fecha del registro | Sí |
| dimension | VARCHAR(50) | sales/delivery/admin/cs/knowledge | Sí |
| notes | TEXT | Notas | No |

### 3.12 Knowledge (Artículo de Conocimiento)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| knowledge_id | UUID / INTEGER | ID único | PK |
| title | VARCHAR(200) | Título | Sí |
| type | VARCHAR(50) | framework/pattern/benchmark/lesson/template | Sí |
| file_path | VARCHAR(500) | Ruta en el repositorio | Sí |
| version | VARCHAR(10) | Versión semántica | Sí |
| author | VARCHAR(100) | Autor | Sí |
| tags | TEXT[] | Tags | Sí |
| status | VARCHAR(20) | draft/active/deprecated | Sí |
| usage_count | INTEGER | Veces utilizado | No |
| created_at | TIMESTAMP | Fecha de creación | Sí |
| updated_at | TIMESTAMP | Última actualización | Sí |

### 3.13 Interaction (Interacción con Cliente)

| Campo | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| interaction_id | UUID / INTEGER | ID único | PK |
| company_id | UUID / INTEGER | ID de empresa | FK |
| contact_id | UUID / INTEGER | ID de contacto | FK |
| user_id | UUID / INTEGER | ID de usuario Klar | FK |
| type | VARCHAR(50) | call/email/meeting/presentation/support | Sí |
| subject | VARCHAR(200) | Asunto | Sí |
| notes | TEXT | Notas | No |
| duration_minutes | INTEGER | Duración en minutos | No |
| outcome | VARCHAR(50) | positive/neutral/negative | No |
| created_at | TIMESTAMP | Fecha de la interacción | Sí |

---

## 4. Diccionario de Datos

### 4.1 Enums y Valores Permitidos

| Campo | Valores |
|---|---|
| company.status | lead, sql, opp, won, lost, active, archived |
| company.source | linkedin, referral, organic, ad, partner, outbound, other |
| company.size | micro, small, medium |
| company.country | AR, CL, UY, PE, CO, MX, ES, US, OTRO |
| contract.type | service, nda, retainer, addendum |
| contract.diagnosis_type | express, integral, premium, retainer |
| contract.payment_scheme | upfront, 50-50, 40-40-20, monthly, custom |
| contract.status | draft, signed, active, completed, cancelled |
| diagnosis.status | kickoff, in_progress, draft, qa, presented, completed |
| invoice.status | pending, paid, overdue, cancelled |
| payment.status | confirmed, pending, rejected, refunded |
| finding.severity | critical, high, medium, low |
| recommendation.status | pending, in_progress, completed, discarded |
| knowledge.type | framework, pattern, benchmark, lesson, template |
| knowledge.status | draft, active, deprecated |
| interaction.type | call, email, meeting, presentation, support |

### 4.2 Tipos de Datos

| Tipo Sheets | Tipo PostgreSQL | Descripción |
|---|---|---|
| Texto | VARCHAR(n) | Cadena de longitud variable |
| Número | INTEGER / DECIMAL | Números enteros o decimales |
| Fecha | DATE / TIMESTAMP | Fechas y timestamps |
| Checkbox | BOOLEAN | Verdadero/Falso |
| Lista (dropdown) | ENUM / VARCHAR | Valores controlados |
| Notas largas | TEXT | Texto multilínea |

---

## 5. Vistas y Reportes

### 5.1 Vistas del Sistema

| Vista | Tablas Fuente | Propósito |
|---|---|---|
| v_pipeline | Company, Contact, Contract | Pipeline de ventas en tiempo real |
| v_active_clients | Company, Contract, Diagnosis | Clientes activos con diagnóstico en curso |
| v_accounts_receivable | Invoice, Payment, Company | Cuentas por cobrar |
| v_monthly_revenue | Invoice, Payment | Ingresos mensuales |
| v_diagnosis_progress | Diagnosis, Finding | Progreso de diagnósticos activos |
| v_client_history | Diagnosis, Finding, Interaction | Historial completo del cliente |
| v_kpi_dashboard | KpiLog | Dashboard de indicadores |
| v_knowledge_usage | Knowledge | Estadísticas de uso de conocimiento |

### 5.2 Reportes Predefinidos

| Reporte | Frecuencia | Contenido |
|---|---|---|
| Pipeline Report | Semanal | Leads por etapa, valor, antigüedad |
| Revenue Report | Mensual | Ingresos por cliente, tipo, tendencia |
| Cash Flow | Semanal | Ingresos, egresos, saldo proyectado |
| Client Health | Mensual | NPS, CSAT, estado de clientes activos |
| Operations Report | Mensual | Diagnósticos entregados, tiempo promedio, QC |
| KPI Dashboard | Semanal | Todos los KPIs con semáforos |

---

## 6. Implementación en Sheets

### 6.1 Estructura de Archivos Sheets

```
📊 Klar Analytics - Data Platform/
├── 01_Pipeline (CRM)         // Company + Contact combinado
├── 02_Contratos              // Contract
├── 03_Diagnósticos           // Diagnosis
├── 04_Hallazgos              // Finding
├── 05_Recomendaciones        // Recommendation
├── 06_Invoice                // Invoice
├── 07_Pagos                  // Payment
├── 08_AgentOutputs           // AgentOutput
├── 09_KPIs                   // KpiLog
├── 10_Knowledge_Registry     // Knowledge
├── 11_Interacciones          // Interaction
├── 12_Dashboard              // Vistas + gráficos
└── _Admin
    ├── Config                // Enums, valores de referencia
    └── Backup_Log            // Historial de backups
```

### 6.2 Reglas de Validación en Sheets

| Hoja | Regla | Fórmula |
|---|---|---|
| Pipeline | status debe ser válido | Data validation (lista) |
| Pipeline | company_id único | =COUNTIF(A:A,A2)=1 |
| Diagnósticos | delivery_lead debe existir en Users | Data validation desde hoja _Admin |
| Invoice | monto ≥ 0 | =B2>=0 |
| Pagos | invoice_id debe existir en Invoice | Data validation |

### 6.3 Automatización en Sheets

| Disparador | Acción | Google Apps Script |
|---|---|---|
| Nueva fila en Pipeline (< 1h) | Notificar por email a ventas | onEdit trigger |
| Invoice status = "paid" | Actualizar Diagnosis status | onEdit trigger |
| Fecha de vencimiento hoy | Email de recordatorio | Time-driven trigger |
| NPS registrado | Si NPS ≤ 6, email a Director | onEdit trigger |

---

## 7. Migración a PostgreSQL

### 7.1 Plan de Migración

| Fase | Actividad | Dependencia |
|---|---|---|
| **Fase 1** | Implementar en Sheets (MVP) | — |
| **Fase 2** | Definir schema SQL completo | Fase 1 |
| **Fase 3** | Migrar datos de Sheets a PostgreSQL | Fase 2 |
| **Fase 4** | Conectar aplicación web a PostgreSQL | Fase 3 |
| **Fase 5** | Desactivar Sheets, migrar dashboards | Fase 4 |

### 7.2 Schema SQL de Referencia

```sql
-- Esquema PostgreSQL para Klar Analytics
-- Versión 1.0

CREATE SCHEMA IF NOT EXISTS klar;

-- Enums
CREATE TYPE company_status AS ENUM ('lead','sql','opp','won','lost','active','archived');
CREATE TYPE diagnosis_type AS ENUM ('express','integral','premium','retainer');
CREATE TYPE diagnosis_status AS ENUM ('kickoff','in_progress','draft','qa','presented','completed');
CREATE TYPE finding_severity AS ENUM ('critical','high','medium','low');
CREATE TYPE invoice_status AS ENUM ('pending','paid','overdue','cancelled');

-- Tablas
CREATE TABLE klar.company (
    company_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    legal_name VARCHAR(200) NOT NULL,
    trade_name VARCHAR(200),
    tax_id VARCHAR(50) NOT NULL UNIQUE,
    industry VARCHAR(100) NOT NULL,
    size VARCHAR(20),
    employees INTEGER,
    annual_revenue DECIMAL(12,2),
    website VARCHAR(200),
    address TEXT,
    country VARCHAR(50),
    status company_status NOT NULL DEFAULT 'lead',
    source VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE klar.contact (
    contact_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID NOT NULL REFERENCES klar.company(company_id),
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(200) NOT NULL,
    phone VARCHAR(50),
    role VARCHAR(100),
    is_decision_maker BOOLEAN DEFAULT FALSE,
    is_billing_contact BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ... (continuación del schema completo en archivo separado)
```

### 7.3 Índices Recomendados

| Tabla | Índice | Propósito |
|---|---|---|
| company | tax_id | Búsqueda por CUIT/RUT |
| company | status | Pipeline por estado |
| diagnosis | company_id | Diagnósticos por cliente |
| diagnosis | delivery_lead_id | Carga de trabajo |
| invoice | company_id | Facturas por cliente |
| invoice | status | Cuentas por cobrar |
| finding | diagnosis_id | Hallazgos por diagnóstico |

---

*Fin del documento — Database_Model.md v1.0*
