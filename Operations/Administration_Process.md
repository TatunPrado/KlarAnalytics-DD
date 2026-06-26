# Proceso Administrativo

> **Sistema Operativo** — Administration Process de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura Administrativa](#1-arquitectura-administrativa)
2. [Onboarding de Clientes](#2-onboarding-de-clientes)
3. [Facturación y Cobranzas](#3-facturación-y-cobranzas)
4. [Gestión de Contratos](#4-gestión-de-contratos)
5. [Gestión de Pagos a Proveedores](#5-gestión-de-pagos-a-proveedores)
6. [Contabilidad y Reporting](#6-contabilidad-y-reporting)
7. [Gestión Documental](#7-gestión-documental)
8. [Cumplimiento Legal y Fiscal](#8-cumplimiento-legal-y-fiscal)
9. [KPIs Administrativos](#9-kpis-administrativos)

---

## 1. Arquitectura Administrativa

### 1.1 Visión General

```
                    ┌──────────────────────────────────────┐
                    │        Sistema Administrativo         │
                    └──────────────────────────────────────┘
                                    │
         ┌────────────┬─────────────┼─────────────┬──────────────┐
         │            │             │             │              │
    ┌────▼───┐  ┌────▼────┐  ┌────▼────┐  ┌─────▼─────┐  ┌────▼────┐
    │Clientes│  │Facturas │  │Contratos│  │Proveedores │  │Reporting│
    │Onboard │  │Cobranza │  │Legal    │  │Pagos      │  │Contable │
    └────────┘  └─────────┘  └─────────┘  └───────────┘  └─────────┘
```

### 1.2 Principios

| Principio | Descripción |
|---|---|
| **Digital First** | Todo proceso es digital, sin papel |
| **Automatización** | Máxima automatización de procesos repetitivos |
| **Trazabilidad** | Cada transacción tiene auditoría completa |
| **Cumplimiento** | 100% compliant con regulaciones fiscales locales |
| **Cash Flow Health** | Cobranza proactiva, pagos optimizados |

### 1.3 Herramientas

| Sistema | Función | Estado |
|---|---|---|
| Google Sheets | ERP contable inicial | Actual (MVP) |
| CRM (ver CRM_Model.md) | Gestión de clientes y pipeline | Actual (MVP) |
| Firma digital (ej. DocuSign/Firmafy) | Contratos | A implementar |
| Pasarela de pago (Mercado Pago, Stripe) | Cobranzas | A implementar |
| Contabilidad (QuickBooks / Xero) | Contabilidad | Futuro |
| ERP Integrado (ver ERP_Blueprint.md) | Todo-en-uno | Futuro |

---

## 2. Onboarding de Clientes

### 2.1 Proceso de Alta

```
Cliente WON (CRM) →
    ↓
Alta en Google Sheets/ERP:
    - Datos fiscales (RUT/CUIT, razón social, dirección)
    - Datos de contacto (email, teléfono, persona responsable)
    - Plan contratado, precio, forma de pago
    - Fecha de kickoff / inicio
    ↓
Crear expediente digital (Google Drive) →
    ↓
Enviar factura inicial (50% adelanto) →
    ↓
Registrar pago cuando se reciba →
    ↓
Confirmar onboarding completado →
    ↓
Mover a ACTIVE en CRM
```

### 2.2 Datos Requeridos del Cliente

| Campo | Obligatorio | Formato |
|---|---|---|
| Razón Social | Sí | Texto |
| RUT/CUIT/NIT | Sí | Número |
| Dirección fiscal | Sí | Texto |
| Email de facturación | Sí | Email |
| Persona de contacto (facturación) | Sí | Texto |
| Teléfono | Sí | Número |
| Industria | Sí | Texto |
| Tamaño (empleados) | Sí | Número |
| Plan contratado | Sí | Selección |
| Precio | Sí | Número |
| Forma de pago | Sí | Transferencia / Tarjeta / Cheque |
| Fecha de kickoff | Sí | Fecha |
| Notas adicionales | No | Texto |

### 2.3 Checklist de Onboarding Administrativo

- [ ] Datos fiscales registrados en ERP
- [ ] Expediente creado en Drive
- [ ] Contrato firmado (digital)
- [ ] Factura inicial emitida
- [ ] Método de pago confirmado
- [ ] Comprobante de pago recibido (si aplica)
- [ ] Contacto de facturación registrado

---

## 3. Facturación y Cobranzas

### 3.1 Esquema de Facturación

| Plan | Esquema | Factura 1 | Factura 2 |
|---|---|---|---|
| **Diagnóstico Express** | 100% upfront | 100% al inicio | — |
| **Diagnóstico Integral** | 50/50 | 50% al inicio | 50% a la presentación |
| **Diagnóstico Premium** | 40/40/20 | 40% al inicio | 40% al informe, 20% post-presentación |
| **Retainer Mensual** | Mensual | 1er día del mes | Mensual |

### 3.2 Proceso de Facturación

```
Disparador (nuevo cliente / inicio de mes) →
    ↓
Generar factura (monto, impuestos, datos fiscales) →
    ↓
Enviar al cliente (email automático) →
    ↓
Registrar en ERP (pendiente de pago) →
    ↓
Seguimiento de cobranza:
    Día 0: Factura enviada
    Día 7: Recordatorio amable (email)
    Día 14: Recordatorio (email + llamada)
    Día 21: Aviso de mora (email formal)
    Día 30: Escalar a Director
    Día 45: Pausar servicio / Gestión judicial (según contrato)
    ↓
Registrar pago cuando se reciba →
    ↓
Conciliar en ERP
```

### 3.3 Automatizaciones de Cobranza

| Disparador | Acción |
|---|---|
| Factura emitida | Enviar email con factura adjunta + instrucciones de pago |
| Vencimiento en 7 días | Email recordatorio automático |
| Vencimiento hoy | Email de "vencimiento hoy" |
| Vencimiento +7 días | Email de mora + llamada |
| Vencimiento +14 días | Email formal + alerta a Director |
| Pago recibido | Marcar como pagado, enviar comprobante |
| Pago atrasado > 30 días | Suspender envío de nuevos servicios hasta pago |

### 3.4 Métodos de Pago Aceptados

| Método | Costo | Prioridad | Notas |
|---|---|---|---|
| Transferencia bancaria | 0% | 1 | Preferido (sin comisiones) |
| Mercado Pago / Stripe | 3-5% | 2 | Automatizable, débito automático |
| Tarjeta de crédito | 3-5% | 3 | Vía pasarela |
| Cheque | 0% | 4 | Riesgo de rebote |
| Cripto (USDT) | 0% | 5 | Bajo volumen |

---

## 4. Gestión de Contratos

### 4.1 Tipos de Contrato

| Tipo | Cliente | Alcance |
|---|---|---|
| **Contrato de Servicio** | Todos los clientes | Diagnóstico, entregables, plazos, pricing, confidencialidad |
| **NDA** | Clientes que lo requieran | Confidencialidad mutua |
| **Retainer Agreement** | Clientes con retainer | Servicio mensual, renovación automática |
| **Addendum** | Cambios sobre contrato original | Modificaciones |

### 4.2 Proceso de Contratos

```
Propuesta aceptada →
    ↓
Preparar contrato (plantilla + datos del cliente) →
    ↓
Enviar para firma digital →
    ↓
Cliente firma →
    ↓
Klar Analytics firma (Director) →
    ↓
Contrato sellado → Archivar en expediente →
    ↓
Enviar copia al cliente →
    ↓
Facturar según esquema
```

### 4.3 Cláusulas Obligatorias

| Cláusula | Incluye |
|---|---|
| Alcance del servicio | Dimensiones, entregables, exclusiones |
| Plazos | Fecha de kickoff, fecha de entrega estimada |
| Precio y forma de pago | Monto, impuestos, esquema, método de pago |
| Confidencialidad | Protección de datos del cliente |
| Propiedad intelectual | El informe es del cliente; frameworks/metodología son de Klar |
| Cancelación | Condiciones, cargos por cancelación, reembolsos |
| Mora | Intereses, suspensión del servicio |
| Legislación aplicable | Jurisdicción |

---

## 5. Gestión de Pagos a Proveedores

### 5.1 Proveedores Potenciales

| Tipo | Ejemplo | Frecuencia de Pago |
|---|---|---|
| Cloud / SaaS | OpenAI API, Vercel, Google Cloud | Mensual |
| Pasarela de pago | Mercado Pago, Stripe | Por transacción |
| Herramientas | Slack, Notion, CRM, Mailchimp | Mensual/Anual |
| Consultores externos | Freelancers, partners | Por proyecto |
| Marketing | Google Ads, LinkedIn Ads | Mensual |

### 5.2 Proceso de Pagos

```
Recibir factura de proveedor →
    ↓
Verificar contra servicio recibido →
    ↓
Aprobar pago (Director) →
    ↓
Programar pago (según términos) →
    ↓
Ejecutar pago →
    ↓
Registrar en ERP →
    ↓
Archivar factura
```

### 5.3 Calendario de Pagos Fijos

| Concepto | Monto Estimado (USD/mes) | Fecha de Pago |
|---|---|---|
| OpenAI API | 200 - 1,000 | 5 del mes |
| Vercel / Hosting | 20 - 50 | 5 del mes |
| Google Workspace | 30 - 60 | 1 del mes |
| Slack | 15 - 30 | 1 del mes |
| Dominios y DNS | 10 - 20 | Anual renovación |
| Pasarela de pago (comisiones) | Variable | Por transacción |

---

## 6. Contabilidad y Reporting

### 6.1 Estados Contables Básicos

| Estado | Frecuencia | Responsable |
|---|---|---|
| Estado de Resultados | Mensual | Admin / Contador |
| Balance General | Mensual | Admin / Contador |
| Flujo de Caja | Semanal | Admin |
| Cuenta de Resultados por Cliente | Por proyecto | Admin |
| Reporte de Cobranza | Semanal | Admin |

### 6.2 Estructura de Cuentas (Plan de Cuentas)

| Categoría | Subcategorías |
|---|---|
| **Ingresos** | Diagnósticos, Retainers, Talleres, Otros |
| **Costos Directos** | Agentes (API), Consultores externos, Herramientas por proyecto |
| **Gastos Operativos** | Cloud/SaaS, Marketing, Sueldos, Oficina, Legal/Contable |
| **Activos** | Caja, Bancos, Cuentas por cobrar, Equipos |
| **Pasivos** | Cuentas por pagar, Impuestos por pagar |
| **Patrimonio** | Capital, Resultados acumulados |

### 6.3 Dashboard Financiero (Reporting Mensual)

| Indicador | Fórmula | Meta |
|---|---|---|
| **MRR** | Ingresos recurrentes mensuales | ≥ USD 5,000 |
| **Margen Bruto** | (Ingresos - Costos Directos) / Ingresos | ≥ 60% |
| **Margen Neto** | Utilidad Neta / Ingresos | ≥ 25% |
| **Cash Runway** | Caja / Gasto Mensual | ≥ 6 meses |
| **Días de Cobranza** | Promedio días para cobrar | ≤ 15 días |
| **CAC Payback** | CAC / Margen mensual por cliente | ≤ 6 meses |

---

## 7. Gestión Documental

### 7.1 Estructura de Expedientes

```
Drive / Expedientes /
├── Clientes/
│   ├── [Cliente A]/
│   │   ├── 01_Contratos/
│   │   ├── 02_Facturas/
│   │   ├── 03_Informes/
│   │   └── 04_Correspondencia/
│   └── [Cliente B]/
├── Proveedores/
├── Legal/
├── Financiero/
│   ├── Estados_Contables/
│   ├── Impuestos/
│   └── Bancos/
└── Interno/
    ├── Políticas/
    ├── Plantillas/
    └── Actas/
```

### 7.2 Políticas de Documentos

| Política | Detalle |
|---|---|
| **Formato** | Preferentemente PDF para documentos oficiales |
| **Naming** | `[Tipo]_[Cliente]_[Fecha].pdf` (ej. `Factura_ClienteA_2026-06-15.pdf`) |
| **Retención** | Mínimo 5 años (según legislación local) |
| **Respaldo** | Google Drive + backup semanal externo |
| **Acceso** | Admin total; Director acceso completo; Agentes solo informes |
| **Confidencialidad** | Expedientes de cliente en carpeta privada |

---

## 8. Cumplimiento Legal y Fiscal

### 8.1 Obligaciones Fiscales

| Obligación | Frecuencia | Fecha Límite |
|---|---|---|
| IVA / VAT | Mensual | Día 12 del mes siguiente |
| Impuesto a la Renta | Anual | Marzo - Abril |
| Retenciones (si aplica) | Mensual | Día 10 del mes siguiente |
| Libros contables | Anual | Antes del cierre fiscal |

### 8.2 Obligaciones Legales

| Obligación | Frecuencia | Responsable |
|---|---|---|
| Contrato social actualizado | Anual | Director |
| Registro de marca (Klar Analytics) | Una vez | Director |
| Términos y condiciones (web) | Revisión anual | Director |
| Política de privacidad (GDPR/LOPD) | Revisión anual | Director |
| Seguro de responsabilidad profesional | Anual | Director |

### 8.3 Proceso de Cumplimiento

```
Identificar obligación → 
    ↓
Agendar en calendario de cumplimiento →
    ↓
Preparar documentación requerida →
    ↓
Presentar / Pagar dentro del plazo →
    ↓
Archivar comprobante →
    ↓
Registrar en checklist de cumplimiento
```

---

## 9. KPIs Administrativos

| Indicador | Fórmula | Frecuencia | Meta | Semáforo |
|---|---|---|---|---|
| **Onboarding Time** | Días de WON a kickoff | Mensual | ≤ 3 días | 🔴 > 5 🟡 3-5 🟢 ≤ 3 |
| **Invoice-to-Payment** | Días promedio para cobrar | Mensual | ≤ 15 días | 🔴 > 25 🟡 15-25 🟢 ≤ 15 |
| **Aging > 30 días** | % facturas sin pagar > 30 días | Semanal | ≤ 5% | 🔴 > 10% 🟡 5-10% 🟢 ≤ 5% |
| **Contract-to-Sign** | Días de envío a firma | Mensual | ≤ 3 días | 🔴 > 5 🟡 3-5 🟢 ≤ 3 |
| **Cash Flow Accuracy** | Real vs presupuesto | Mensual | ± 10% | 🔴 > 20% 🟡 10-20% 🟢 ≤ 10% |
| **Payment Compliance** | Pagos a tiempo / Total emitido | Mensual | ≥ 95% | 🔴 < 85% 🟡 85-95% 🟢 ≥ 95% |
| **Document Compliance** | Expedientes completos / Total | Mensual | 100% | 🔴 < 95% 🟡 95-100% 🟢 = 100% |
| **Tax Filing Compliance** | Declaraciones a tiempo | Anual | 100% | 🔴 < 100% 🟡 100% 🟢 = 100% |
| **Gross Margin** | (Ingresos - Costos Directos) / Ingresos | Mensual | ≥ 60% | 🔴 < 50% 🟡 50-60% 🟢 ≥ 60% |
| **Operating Expense Ratio** | Gastos operativos / Ingresos | Mensual | ≤ 40% | 🔴 > 50% 🟡 40-50% 🟢 ≤ 40% |

---

*Fin del documento — Administration_Process.md v1.0*
