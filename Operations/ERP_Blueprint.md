# Blueprint del ERP

> **Sistema Operativo** — ERP Blueprint de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del ERP](#1-arquitectura-del-erp)
2. [Módulos del Sistema](#2-módulos-del-sistema)
3. [Módulo Financiero](#3-módulo-financiero)
4. [Módulo de Clientes](#4-módulo-de-clientes)
5. [Módulo de Proyectos](#5-módulo-de-proyectos)
6. [Módulo de RRHH](#6-módulo-de-rrhh)
7. [Módulo de Reporting](#7-módulo-de-reporting)
8. [Integraciones](#8-integraciones)
9. [Plan de Implementación](#9-plan-de-implementación)

---

## 1. Arquitectura del ERP

### 1.1 Visión General

```
                    ┌─────────────────────────────────────────────┐
                    │              ERP Klar Analytics              │
                    │         (MVP: Sheets → Odoo / Custom)        │
                    └─────────────────────────────────────────────┘

┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Finance  │ │ Clients  │ │ Projects │ │   HR     │ │ Reporting│
│ Module   │ │ Module   │ │ Module   │ │ Module   │ │ Module   │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │            │            │
     └────────────┴────────────┴────────────┴────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Base de Datos   │
                    │   (PostgreSQL)    │
                    └───────────────────┘
```

### 1.2 Principios de Diseño

| Principio | Descripción |
|---|---|
| **Modular** | Cada módulo es independiente y desacoplable |
| **API-First** | Todas las funciones expuestas via REST API |
| **Integrable** | Conectable con CRM, pasarelas de pago, herramientas externas |
| **Escalable** | De 1 a 100 usuarios sin reingeniería |
| **Auditable** | Log completo de todas las transacciones |
| **Multi-moneda** | Soporte USD, ARS, CLP, etc. |

### 1.3 Stack Recomendado

| Capa | Tecnología | Razón |
|---|---|---|
| **Backend** | Node.js / Python (FastAPI) | Equipo conoce el stack |
| **Base de datos** | PostgreSQL | Relacional, maduro, escalable |
| **Frontend** | React / Next.js | Componentes modernos |
| **Autenticación** | Auth0 / Supabase Auth | Seguro, rápido de implementar |
| **Hosting** | Vercel / Railway / AWS | Escalable, costo manejable |
| **ERP base (alternativa)** | Odoo (Community) | Open source, modular, maduro |

---

## 2. Módulos del Sistema

### 2.1 Mapa de Módulos

| Módulo | Función | Prioridad | Estado |
|---|---|---|---|
| **Finance** | Contabilidad, facturación, cobranzas, pagos | Crítica | MVP Sheets |
| **Clients** | CRM básico, expedientes, historial | Crítica | MVP Sheets |
| **Projects** | Diagnósticos, entregables, agentes | Crítica | MVP Sheets |
| **HR** | Equipo, roles, carga de trabajo | Media | Futuro |
| **Reporting** | Dashboards, KPIs, exportación | Alta | MVP (manual) |
| **Knowledge** | Conexión con Knowledge/, Skills/, Playbooks | Alta | Git |
| **Inventory** | Activos, suscripciones, licencias | Baja | Futuro |
| **Automation** | Workflows, reglas de negocio | Media | Futuro |

### 2.2 Relación entre Módulos

```
Clients ──► Projects ──► Finance
   │            │            │
   │            │            │
   └── HR ──────┘            │
         │                   │
         └──► Reporting ◄────┘
```

---

## 3. Módulo Financiero

### 3.1 Funcionalidades

| Función | MVP (Sheets) | Futuro (ERP) |
|---|---|---|
| Plan de cuentas | Manual estructurado | Configurable |
| Facturación | Manual | Automática (con template + envío) |
| Cobranzas | Manual + recordatorios | Automatizada con pasarela de pago |
| Pagos a proveedores | Manual | Automatizada |
| Conciliación bancaria | Manual | Automática (API bancaria) |
| Estados financieros | Manual (fórmulas) | Generados automáticamente |
| Multi-moneda | Manual con tipo de cambio | Automático |
| Cierre contable | Manual | Automatizado |

### 3.2 Procesos en el ERP

| Proceso | Flujo |
|---|---|
| **Facturación** | Contrato firmado → Generar factura → Enviar → Registrar pago → Conciliar |
| **Cobranza** | Factura emitida → Seguimiento automatizado → Pago registrado → Recibo emitido |
| **Pago a proveedores** | Factura recibida → Verificar → Aprobar → Pagar → Conciliar |
| **Cierre mensual** | Verificar transacciones → Conciliar bancos → Generar estados → Archivar |

### 3.3 Reportes Financieros

| Reporte | Frecuencia | Contenido |
|---|---|---|
| Estado de Resultados | Mensual | Ingresos, costos, gastos, resultado |
| Balance General | Mensual | Activos, pasivos, patrimonio |
| Flujo de Caja | Semanal | Ingresos reales, egresos, proyección |
| Cuentas por Cobrar | Semanal | Facturas pendientes por antigüedad |
| Cuentas por Pagar | Semanal | Facturas de proveedores pendientes |
| Rentabilidad por Cliente | Mensual | Ingreso - costos directos por cliente |

---

## 4. Módulo de Clientes

### 4.1 Funcionalidades

| Función | MVP (Sheets) | Futuro (ERP) |
|---|---|---|
| Perfil de cliente | Fila en hoja | Página completa con histórico |
| Contactos | Hoja separada | Relación 1:N dentro del perfil |
| Contratos | Archivo Drive + hoja | Gestión de contratos digital |
| Historial de compras | Manual | Automático (relación con facturas) |
| Segmentación | Manual | Automática (reglas de negocio) |
| Notas y actividades | Columna de notas | Timeline completo |

### 4.2 Interfaz de Cliente (Futuro)

```
┌─────────────────────────────────────────────────────────┐
│  Cliente: Razón Social X        Estado: ● Activo        │
├─────────────────────────────────────────────────────────┤
│  Información General │ Contratos │ Facturas │ Proyectos │
├─────────────────────────────────────────────────────────┤
│  Datos Fiscales      │ Contactos          │ Notas       │
│  - RUT: XX-XXXX     │ Juan Pérez (CEO)   │ Llamar      │
│  - Dirección: ...   │ María García (CFO) │ para rev.   │
│  - Industria: ...   │                    │ trimestral  │
├─────────────────────────────────────────────────────────┤
│  Últimas Actividades                                    │
│  10/06 - Factura emitida                                │
│  05/06 - Diagnóstico Integral completado                │
│  01/06 - Pago recibido                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 5. Módulo de Proyectos

### 5.1 Funcionalidades

| Función | MVP (Sheets) | Futuro (ERP) |
|---|---|---|
| Creación de proyecto | Manual | Automática (al ganar deal) |
| Asignación de equipo | Manual | Automática (disponibilidad) |
| Seguimiento de fases | Manual | Kanban visual |
| Gestión de agentes | Manual | Disparo automático de agentes |
| Control de calidad | Manual | Workflow de QA integrado |
| Timesheet | Manual | Registro de horas del equipo |

### 5.2 Flujo de Proyecto en el ERP

```
Deal WON → Crear proyecto automáticamente →
    ↓
Asignar Delivery Lead (manual o automático) →
    ↓
Establecer fases: Kickoff → Diagnóstico → Informe → QA → Presentación →
    ↓
Cada fase dispara tareas automáticas:
    - Kickoff: Enviar Brief, solicitar documentos
    - Diagnóstico: Iniciar agentes
    - Informe: Generar template con datos del cliente
    - QA: Notificar a revisor
    - Presentación: Agendar reunión, enviar materiales
```

---

## 6. Módulo de RRHH

### 6.1 Funcionalidades (Futuro)

| Función | Descripción |
|---|---|
| **Equipo** | Perfiles, roles, contacto, disponibilidad |
| **Carga de trabajo** | Proyectos activos por persona, horas estimadas |
| **Timesheet** | Registro de horas por proyecto |
| **Vacaciones y ausencias** | Calendario, solicitudes, aprobaciones |
| **Evaluación** | Desempeño, feedback, objetivos |

### 6.2 Roles en el Sistema

| Rol | Acceso | Módulos |
|---|---|---|
| **Superadmin** | Total | Todos |
| **Director** | Total | Todos (solo lectura en finanzas sensibles) |
| **Delivery Lead** | Proyectos asignados + Clientes | Proyectos, Clientes |
| **Ventas** | Pipeline + Clientes | Clientes (solo leads/oportunidades) |
| **CS** | Clientes activos | Clientes, Proyectos (solo lectura) |
| **Admin** | Financiero + RRHH | Finance, HR, Clientes |

---

## 7. Módulo de Reporting

### 7.1 Dashboard Principal

```
┌─────────────────────────────────────────────────────────────────┐
│  MRR: $XX,XXX    │  Clientes Activos: XX   │  NPS Promedio: XX │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐  ┌──────────────────────────────────┐  │
│  │  Ingresos Mensuales  │  │  Pipeline Value ($)             │  │
│  │  [Gráfico de línea]  │  │  [Gráfico de barras por etapa]  │  │
│  └─────────────────────┘  └──────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐  ┌──────────────────────────────────┐  │
│  │  KPIs con Semáforo   │  │  Próximos Vencimientos          │  │
│  │  ● Win Rate: 35%    │  │  Factura A: vence 20/06        │  │
│  │  ● NPS: 52          │  │  Factura B: vence 25/06        │  │
│  │  ● On-Time: 88%     │  │                                 │  │
│  └─────────────────────┘  └──────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Reportes Automáticos

| Reporte | Frecuencia | Destinatario | Formato |
|---|---|---|---|
| **Executive Summary** | Semanal | Dirección | Dashboard |
| **Pipeline Review** | Semanal | Ventas | Dashboard |
| **Cash Flow** | Semanal | Admin | Dashboard + PDF |
| **Financial Statements** | Mensual | Dirección + Contador | PDF |
| **Operations Report** | Mensual | Delivery Leads | Dashboard |
| **KPI Scorecard** | Mensual | Todo el equipo | Dashboard |
| **Annual Report** | Anual | Stakeholders | PDF |

---

## 8. Integraciones

### 8.1 Integraciones Planificadas

| Sistema | Propósito | Tipo | Prioridad |
|---|---|---|---|
| **Pasarela de pago** (Mercado Pago / Stripe) | Cobranzas automáticas | API | Alta |
| **Email** (SendGrid / Resend) | Envío de facturas, notificaciones | API | Alta |
| **Slack** | Notificaciones al equipo | Webhook | Alta |
| **Google Drive** | Almacenamiento de documentos | API | Alta |
| **OpenAI / LLM** | Agentes de diagnóstico | API | Alta |
| **HubSpot / Pipedrive** | Sincronización de CRM | API | Media |
| **QuickBooks / Xero** | Contabilidad profesional | API | Media |
| **Calendly** | Agendamiento de reuniones | API | Media |

### 8.2 Mapa de Integraciones

```
Pasarela de Pago ◄──► ERP (Módulo Finance)
       │
       │ (webhook)
       ▼
ERP registra pago → Notifica a Slack
                → Actualiza CRM (cliente WON)
                → Dispara onboarding
                → Genera recibo
```

---

## 9. Plan de Implementación

### 9.1 Fases

| Fase | Alcance | Duración | Dependencias |
|---|---|---|---|
| **Fase 0 — MVP** | Google Sheets + Apps Script | Operando | — |
| **Fase 1 — Finance** | Módulo financiero en PostgreSQL | 4-6 semanas | Database model |
| **Fase 2 — Projects** | Módulo de proyectos + agentes | 4-6 semanas | Fase 1 |
| **Fase 3 — Clients** | Módulo de clientes + integración CRM | 3-4 semanas | Fase 1, 2 |
| **Fase 4 — Reporting** | Dashboards automáticos | 2-3 semanas | Fase 1, 2, 3 |
| **Fase 5 — HR** | Módulo de RRHH | 3-4 semanas | Fase 1 |
| **Fase 6 — Automation** | Workflows y reglas de negocio | 4-6 semanas | Fase 1-5 |

### 9.2 MVP a Futuro: Timeline

```
Q3 2026: Fase 1 (Finance) + Fase 2 (Projects)
Q4 2026: Fase 3 (Clients + CRM integration)
Q1 2027: Fase 4 (Reporting)
Q2 2027: Fase 5 (HR)
Q3 2027: Fase 6 (Automation)
```

### 9.3 Alternativa Odoo

Si se opta por Odoo Community en lugar de desarrollo custom:

| Módulo Odoo | Función en Klar |
|---|---|
| Accounting | Contabilidad, facturación, cobranzas |
| CRM | Pipeline de ventas |
| Project | Gestión de proyectos y tareas |
| Timesheet | Registro de horas |
| HR | Empleados, vacaciones |
| Invoicing | Facturación electrónica |

---

*Fin del documento — ERP_Blueprint.md v1.0*
