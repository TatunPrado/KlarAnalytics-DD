# Proceso Comercial

> **Sistema Operativo** — Sales Process de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del Pipeline](#1-arquitectura-del-pipeline)
2. [Fase 1: Generación de Leads](#2-fase-1-generación-de-leads)
3. [Fase 2: Calificación](#3-fase-2-calificación)
4. [Fase 3: Descubrimiento](#4-fase-3-descubrimiento)
5. [Fase 4: Presentación y Propuesta](#5-fase-4-presentación-y-propuesta)
6. [Fase 5: Cierre](#6-fase-5-cierre)
7. [Fase 6: Onboarding](#7-fase-6-onboarding)
8. [Estados del Pipeline](#8-estados-del-pipeline)
9. [Automatizaciones](#9-automatizaciones)
10. [KPIs Comerciales](#10-kpis-comerciales)
11. [Documentos Generados](#11-documentos-generados)

---

## 1. Arquitectura del Pipeline

### 1.1 Visión General

```
                   ┌──────────┐
                   │  MQL     │  Marketing Qualified Lead
                   └────┬─────┘
                        │ Calificación (BANT)
                   ┌────▼─────┐
                   │  SQL     │  Sales Qualified Lead
                   └────┬─────┘
                        │ Discovery Call
                   ┌────▼─────┐
                   │  OPP     │  Oportunidad Comercial
                   └────┬─────┘
                        │ Propuesta Enviada
                   ┌────▼─────┐
                   │  PROP    │  Propuesta en Negociación
                   └────┬─────┘
                        │ Cierre
              ┌─────────┴──────────┐
              │                    │
         ┌────▼────┐         ┌────▼────┐
         │  WON    │         │  LOST   │
         └────┬────┘         └─────────┘
              │ Onboarding
         ┌────▼────┐
         │  ACTIVE │  Cliente activo en diagnóstico
         └─────────┘
```

### 1.2 Ciclo de Vida del Cliente (Lead a Active)

| Fase | Duración Estimada | Actividades Clave | Responsable |
|---|---|---|---|
| MQL → SQL | ≤ 24h | Calificación BANT | Ventas (CRM Agent) |
| SQL → OPP | ≤ 48h | Discovery Call | Ventas |
| OPP → PROP | ≤ 5 días | Propuesta personalizada | Ventas |
| PROP → WON/LOST | ≤ 7 días | Negociación y cierre | Ventas / Dirección |
| WON → ACTIVE | ≤ 3 días | Onboarding + Alta Admin | Ventas → Operaciones |
| **Total ciclo** | **≤ 18 días** | | |

### 1.3 Perfiles de Cliente Objetivo (Buyer Personas)

| Persona | Descripción | Dolor Principal | Cómo Llegan |
|---|---|---|---|
| **Dueño PyME** | Fundador/CEO de empresa 5-50 empleados | No entiende qué limita su crecimiento | LinkedIn, referidos, búsqueda orgánica |
| **Gerente General** | Gerente no dueño de PyME 50-250 empleados | Necesita datos objetivos para reportar al dueño | Contenido técnico, webinars |
| **Director de PyME Familiar** | Miembro de familia dueña, 2da/3ra generación | Conflictos internos, falta de profesionalización | Referidos de contadores/abogados |
| **Emprendedor** | Founder de startup 0-5 años | Validación de modelo, unit economics | Redes de emprendedores, aceleradoras |

---

## 2. Fase 1: Generación de Leads

### 2.1 Canales de Generación

| Canal | Tipo | Costo Relativo | Volumen Esperado/mes | Prioridad |
|---|---|---|---|---|
| **LinkedIn (orgánico + ads)** | Inbound | Medio | 10-15 MQLs | Alta |
| **Contenido (blog, whitepapers)** | Inbound | Bajo | 5-10 MQLs | Alta |
| **Referidos de clientes** | Inbound | Muy bajo | 3-5 MQLs | Alta |
| **Alianzas (contadores, estudios)** | Partner | Bajo | 3-5 MQLs | Media |
| **Google Ads (branded + sector)** | Inbound | Medio | 5-8 MQLs | Media |
| **Email marketing (newsletter)** | Inbound | Bajo | 2-4 MQLs | Media |
| **Webinars / eventos** | Inbound | Medio | 3-6 MQLs | Media |
| **Outbound (prospección directa)** | Outbound | Alto | 5-10 MQLs | Baja (fase inicial) |

### 2.2 Actividades

| Actividad | Responsable | Frecuencia | Automatizable |
|---|---|---|---|
| Publicar contenido en LinkedIn | Dirección / Marketing | 2-3x/semana | Parcial (programación) |
| Escribir artículos de blog | Dirección / Agentes | 1x/semana | Parcial (IA genera borrador) |
| Enviar newsletter semanal | Marketing | 1x/semana | Total (CRM + email) |
| Activar campañas de ads | Marketing | Continua | Total |
| Gestionar alianzas | Dirección | 2x/mes (reuniones) | No |
| Prospección outbound | Ventas | 10 contactos/día | Parcial (secuencias) |

### 2.3 Automatizaciones

| Disparador | Acción Automática | Herramienta |
|---|---|---|
| Nuevo lead de LinkedIn | Crear registro en CRM, asignar owner | CRM API + LinkedIn |
| Nuevo lead de web (formulario) | Enviar email de bienvenida, crear CRM | Webhook → CRM |
| Lead descarga whitepaper | Clasificar como MQL, notificar a ventas | CRM + Email |
| Referido mencionado por cliente activo | Crear lead con tag "referido", prioridad alta | CRM + NPS |

### 2.4 KPIs

| Indicador | Fórmula | Meta | Semáforo |
|---|---|---|---|
| MQLs generados/mes | Conteo | ≥ 20 | 🔴 < 10 🟡 10-20 🟢 ≥ 20 |
| Costo por Lead (CPL) | Gasto marketing / MQLs | ≤ USD 50 | 🔴 > 100 🟡 50-100 🟢 ≤ 50 |
| Lead por fuente | Conteo por canal | Diversificado (≤ 40% 1 canal) | 🔴 > 60% 1 canal 🟡 40-60% 🟢 ≤ 40% |

---

## 3. Fase 2: Calificación

### 3.1 Criterios BANT

| Criterio | Pregunta | Mínimo para Calificar |
|---|---|---|
| **Budget** | ¿Tienen presupuesto asignado para diagnóstico? | Sí, o proceso de aprobación iniciado |
| **Authority** | ¿Quién decide la compra? | Contacto directo con decisor (dueño/gerente) |
| **Need** | ¿Qué problema buscan resolver? | Dolor claro y reconocido |
| **Timeline** | ¿Cuándo necesitan el diagnóstico? | ≤ 60 días |

### 3.2 Proceso de Calificación

```
Lead Recibido →
    ↓
¿Industria objetivo? (PyME 1-250 emp.)
    ├── No → Mover a "No Califica" → registrar motivo
    └── Sí →
        ↓
¿BANT completo?
    ├── No → Secuencia de nutrición (email + contenido)
    │         Reintentar calificar en 30 días
    └── Sí →
        ↓
Lead Score calculado:
    High (4/4 BANT) → SQL → Asignar a ventas inmediatamente
    Medium (3/4 BANT) → SQL → Asignar a ventas, requiere confirmación
    Low (2/4 BANT) → Nutrición → No calificar aún
```

### 3.3 Lead Scoring

| Factor | Puntos |
|---|---|
| Industria objetivo | 20 |
| Tamaño empresa (5-250 emp.) | 15 |
| Budget confirmado | 25 |
| Authority confirmada | 20 |
| Timeline ≤ 60 días | 20 |
| **Total máximo** | **100** |

| Score | Clasificación | Acción |
|---|---|---|
| 80-100 | **SQL** | Contactar dentro de 24h |
| 60-79 | **MQL (maduro)** | Nutrir con contenido, contactar en 7 días |
| 40-59 | **MQL (temprano)** | Nutrir automatizado por 30 días |
| 0-39 | **Lead frío** | Newsletter general, reevaluar en 90 días |

### 3.4 Automatizaciones

| Disparador | Acción |
|---|---|
| Lead score ≥ 80 | Notificar a ventas por Slack/email, crear tarea de seguimiento |
| Lead score 40-79 | Iniciar secuencia de emails automatizada (3 emails en 14 días) |
| Lead score < 40 | Añadir a newsletter mensual |
| Lead no responde en 14 días | Mover a "Nutrición", pausar contacto telefónico |
| Lead responde positivo a email | Recalificar, si score ≥ 80 → SQL |

### 3.5 KPIs

| Indicador | Fórmula | Meta |
|---|---|---|
| Lead-to-SQL rate | SQL / MQL | ≥ 25% |
| Time-to-qualify | Horas desde lead → SQL | ≤ 24h |
| SQL-to-Opportunity | OPP / SQL | ≥ 50% |

---

## 4. Fase 3: Descubrimiento

### 4.1 Objetivo

Entender en profundidad la situación del prospecto, validar el fit con el servicio y preparar el terreno para una propuesta alineada.

### 4.2 Agenda del Discovery Call (30 min)

| Min | Tema | Objetivo |
|---|---|---|
| 0-3 | Apertura y contexto | Alinear expectativas, confirmar agenda |
| 3-12 | Entendimiento del negocio | Industria, tamaño, modelo, situación actual |
| 12-20 | Problemas y dolores | ¿Qué los trajo? ¿Qué han intentado? |
| 20-25 | Presentación de valor | Cómo funciona Klar Analytics (beneficios) |
| 25-30 | Próximos pasos | Scope, pricing indicativo, timeline |

### 4.3 Outputs del Discovery

| Documento | Contenido | Responsable |
|---|---|---|
| `Discovery_Notes.md` | Notas estructuradas del call | Ventas |
| `Fit_Assessment.md` | Evaluación de adecuación (1-5) | Ventas |
| `Scope_Definition.md` | Tipo de diagnóstico, depth, servicios adicionales | Ventas |

### 4.4 Criterios de Avance (Gate: Discovery → Propuesta)

- [ ] Dolor confirmado y alineado con servicios de Klar
- [ ] Prospecto entiende la propuesta de valor
- [ ] Budget estimado confirmado (rango)
- [ ] Timeline acordado
- [ ] Persona con authority presente en el call
- [ ] No hay señales de no-fit (expectativas irreales, falta de compromiso)

### 4.5 Automatizaciones

| Disparador | Acción |
|---|---|
| Discovery completado | Enviar email de agradecimiento + resumen |
| Fit score ≥ 4/5 | Disparar alerta para preparar propuesta |
| Fit score ≤ 2/5 | Mover a "No Califica", enviar email de declinación cordial |

### 4.6 KPIs

| Indicador | Meta |
|---|---|
| Discovery calls por semana | ≥ 4 |
| Discovery-to-Proposal rate | ≥ 70% |
| Fit score promedio | ≥ 3.5/5 |

---

## 5. Fase 4: Presentación y Propuesta

### 5.1 Estructura de la Propuesta

Sección | Contenido | Duración (páginas)
---|---|---
Portada | Cliente, Klar Analytics, fecha, tipo de diagnóstico | 1
Resumen Ejecutivo | Contexto, objetivo, alcance | 1
Nuestra Metodología | Cómo funciona el diagnóstico multi-agente | 1-2
Alcance del Diagnóstico | Dimensiones cubiertas, entregables | 1
Pricing | Planes (Diagnóstico Integral, Financiero, Estratégico, Operativo) | 1
Timeline | Cronograma estimado | 1
Por Qué Klar | Diferenciación, casos de éxito, equipo | 1-2
Términos y Condiciones | Plazos, forma de pago, confidencialidad | 1

### 5.2 Modelo de Pricing

| Plan | Alcance | Precio (USD) | Duración |
|---|---|---|---|
| **Diagnóstico Express** | 3 dimensiones (a elección), informe ejecutivo, sin presentación | 1,500 - 2,500 | 7-10 días |
| **Diagnóstico Integral** | 5 dimensiones, informe completo + presentación + plan 90 días | 3,500 - 5,500 | 14-21 días |
| **Diagnóstico Premium** | Integral + taller de alineación + 3 meses de seguimiento | 7,500 - 12,000 | 30-45 días |
| **Retainer Mensual** | Diagnóstico rápido mensual + consulta permanente | 1,500 - 3,000/mes | Continuo |

### 5.3 Proceso de Propuesta

```
Discovery completado →
    ↓
Preparar propuesta (Plantilla + personalización)
    ↓
Revisión interna (Accuracy, pricing, términos)
    ↓
Enviar propuesta (email + CRM)
    ↓
Seguimiento día 1: Confirmar recepción
    ↓
Seguimiento día 3: Preguntar dudas
    ↓
Seguimiento día 7: Solicitar feedback
    ↓
Negociación (si aplica)
    ↓
Aceptación → Avanzar a Cierre
```

### 5.4 Automatizaciones

| Disparador | Acción |
|---|---|
| Propuesta enviada | CRM → Estado "Propuesta Enviada", crear tareas de seguimiento |
| Propuesta vista (tracking) | Notificar a ventas |
| Propuesta no vista en 5 días | Enviar email automatizado de re-engagement |
| Propuesta vista múltiples veces | Disparar alerta "alta intención", contactar |

### 5.5 KPIs

| Indicador | Fórmula | Meta |
|---|---|---|
| Win Rate | OPP Ganadas / OPP Totales | ≥ 35% |
| Avg. Ticket | Ingreso total / OPP Ganadas | Según plan |
| Propuesta-to-Cierre | Días | ≤ 7 días |
| Propuestas enviadas/mes | Conteo | ≥ 8 |

---

## 6. Fase 5: Cierre

### 6.1 Proceso de Cierre

```
Propuesta aceptada →
    ↓
Enviar contrato (firma digital)
    ↓
Recibir contrato firmado
    ↓
Enviar factura inicial (50% adelanto)
    ↓
Recibir comprobante de pago
    ↓
Cliente marcado como "WON" en CRM
    ↓
Iniciar Onboarding
```

### 6.2 Documentos de Cierre

| Documento | Formato | Responsable | Plazo |
|---|---|---|---|
| Contrato de servicios | PDF (firma digital) | Admin / Dirección | ≤ 2 días de aceptación |
| Factura inicial | PDF / Electrónica | Admin | ≤ 1 día de contrato firmado |
| Welcome Kit | PDF | Ventas | ≤ 1 día de pago recibido |
| Formulario de onboarding | Online | Cliente | ≤ 3 días de pago recibido |

### 6.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Contrato firmado | Crear factura automática, enviar welcome email |
| Pago recibido (integración bancaria) | Marcar como "Pagado", activar onboarding |
| No pago en 7 días | Email de recordatorio, alerta a admin |
| Post-cierre | Programar encuesta NPS para 30 días |

### 6.4 KPIs

| Indicador | Meta |
|---|---|
| Cash-to-Onboarding | ≤ 3 días |
| Contract-to-Sign | ≤ 5 días |
| Payment Compliance | ≥ 95% |

---

## 7. Fase 6: Onboarding

### 7.1 Checklist de Onboarding

- [ ] Cliente creado en CRM + ERP
- [ ] Expediente documental iniciado
- [ ] Acceso a plataforma de diagnóstico creado
- [ ] Brief_Empresa template preparado
- [ ] Kickoff agendado (dentro de 5 días)
- [ ] Entrevista de descubrimiento agendada
- [ ] Documentación solicitada al cliente (EEFF, organigrama, etc.)

### 7.2 Proceso de Onboarding

```
Día 1: Cliente WON → Crear en sistemas
Día 2: Enviar Welcome Kit + solicitar documentación
Día 3: Agendar kickoff (Meet calendario)
Día 5: Kickoff call (30 min): equipo Klar, cliente, objetivos, cronograma
Día 5+: Iniciar entrevista de descubrimiento (Delivery Process)
```

### 7.3 Automatizaciones

| Disparador | Acción |
|---|---|
| Cliente WON | Crear expediente, enviar welcome kit, disparar checklist |
| Kickoff agendado | Invitación automática, recordatorio 24h antes |
| Documentación solicitada | Email automático con lista de documentos |
| Onboarding completado | Mover a "Active", notificar a Operaciones |

### 7.4 KPIs

| Indicador | Meta |
|---|---|
| Time-to-Kickoff | ≤ 5 días |
| Onboarding Completion Rate | 100% |
| Documentación recibida (kickoff) | ≥ 60% de la solicitada |

---

## 8. Estados del Pipeline

| Código | Estado | Descripción | Acción Siguiente |
|---|---|---|---|
| `MQL` | Marketing Qualified Lead | Lead generado por marketing, sin calificar | Calificar (BANT) |
| `SQL` | Sales Qualified Lead | Lead calificado, listo para contacto | Agendar discovery |
| `OPP` | Oportunidad | Discovery completado, fit confirmado | Preparar propuesta |
| `PROP` | Propuesta Enviada | Propuesta entregada al cliente | Follow-up |
| `NEG` | Negociación | Cliente contrapropone o pide ajustes | Negociar |
| `WON` | Ganado | Contrato firmado y pago recibido | Onboarding |
| `LOST` | Perdido | Cliente no compró | Analizar motivo, nutrir |
| `CLOSED` | Completado | Diagnóstico entregado y cliente satisfecho | Post-venta |
| `ARCHIVED` | Archivado | Lead sin actividad > 90 días | Newsletter |

### 8.1 Diagrama de Transición de Estados

```
         MQL ──► SQL ──► OPP ──► PROP ──► NEG ──► WON ──► CLOSED
          │       │        │        │        │        │
          │       │        │        │        ├──► LOST
          │       │        │        ├──► LOST
          │       │        ├──► LOST
          │       ├──► NUTRIÇÃO (pausa)
          ├──► NUTRIÇÃO (pausa)
          
LOST ──► NUTRIÇÃO (posible re-engagement)
NUTRIÇÃO ──► SQL (si recalifica)
CLOSED ──► ARCHIVED (automático a los 12 meses sin actividad)
```

---

## 9. Automatizaciones

### 9.1 Catálogo Completo de Automatizaciones

| ID | Disparador | Acción | Herramienta | Prioridad |
|---|---|---|---|---|
| A1 | Nuevo MQL | Crear lead en CRM, asignar owner | CRM | Crítica |
| A2 | Lead Score ≥ 80 | Notificar a ventas (Slack + email) | CRM → Slack | Crítica |
| A3 | Lead Score 40-79 | Iniciar secuencia de nutrición (3 emails) | Email Marketing | Alta |
| A4 | Discovery completado | Enviar email resumen + crear OPP | CRM | Alta |
| A5 | Propuesta enviada | Tracking de apertura, crear tareas follow-up | CRM | Alta |
| A6 | Propuesta no vista 5 días | Email re-engagement automático | CRM | Media |
| A7 | Contrato firmado | Crear factura, enviar welcome kit, crear expediente | CRM → ERP | Crítica |
| A8 | Pago recibido | Marcar WON, activar onboarding, notificar ops | ERP → CRM | Crítica |
| A9 | Onboarding completado | Mover a ACTIVE, notificar a operaciones | CRM | Alta |
| A10 | 30 días post-cierre | Enviar encuesta NPS automatizada | CRM → Survey | Alta |
| A11 | 90 días sin actividad | Mover a ARCHIVED, último email | CRM | Baja |
| A12 | MQL sin calificar 7 días | Recordatorio a ventas | CRM | Media |

### 9.2 Secuencia de Emails Automatizada (Nutrición)

| Email | Día | Asunto | Objetivo |
|---|---|---|---|
| E1 | 0 | "Gracias por tu interés en Klar Analytics" | Agradecer, presentar valor |
| E2 | 3 | "¿Sabías que el 60% de las PyMEs no tiene un diagnóstico financiero?" | Educar, generar necesidad |
| E3 | 7 | "Casos de éxito: cómo ayudamos a [industria similar]" | Prueba social, credibilidad |
| E4 (SDR) | 14 | "¿Te gustaría ver un demo rápido?" | Conversión |

---

## 10. KPIs Comerciales

| Indicador | Fórmula | Frecuencia | Responsable | Meta | Semáforo |
|---|---|---|---|---|---|
| **MQLs/mes** | Conteo de leads entrantes calificados por marketing | Semanal | Marketing | ≥ 20 | 🔴 < 10 🟡 10-20 🟢 ≥ 20 |
| **SQLs/mes** | Conteo de leads calificados por ventas | Semanal | Ventas | ≥ 8 | 🔴 < 5 🟡 5-8 🟢 ≥ 8 |
| **Lead-to-SQL** | SQL / MQL | Mensual | Ventas | ≥ 25% | 🔴 < 15% 🟡 15-25% 🟢 ≥ 25% |
| **SQL-to-OPP** | OPP / SQL | Mensual | Ventas | ≥ 50% | 🔴 < 35% 🟡 35-50% 🟢 ≥ 50% |
| **Win Rate** | OPP Won / OPP Total | Mensual | Ventas | ≥ 35% | 🔴 < 25% 🟡 25-35% 🟢 ≥ 35% |
| **Avg. Sales Cycle** | Días desde SQL a Won | Mensual | Ventas | ≤ 21 días | 🔴 > 30 🟡 21-30 🟢 ≤ 21 |
| **Avg. Ticket** | Ingreso mensual / OPP Won | Mensual | Dirección | ≥ USD 3,500 | 🔴 < 2,500 🟡 2,500-3,500 🟢 ≥ 3,500 |
| **Pipeline Value** | Suma de valor de OPP abiertas | Semanal | Dirección | ≥ 3× objetivo mensual | 🔴 < 2× 🟡 2-3× 🟢 ≥ 3× |
| **CAC** | Gasto comercial / OPP Won | Mensual | Dirección | ≤ USD 1,500 | 🔴 > 2,500 🟡 1,500-2,500 🟢 ≤ 1,500 |
| **LTV:CAC** | Ticket promedio × diagnósticos/año / CAC | Trimestral | Dirección | ≥ 3:1 | 🔴 < 2:1 🟡 2-3:1 🟢 ≥ 3:1 |

---

## 11. Documentos Generados

| Fase | Documento | Formato | Plantilla |
|---|---|---|---|
| Leads | `Lead_Record` | CRM Entry | — |
| Calificación | `Lead_Score.md` | Markdown | Templates/Lead_Score.md |
| Discovery | `Discovery_Notes.md` | Markdown | Templates/Discovery_Notes.md |
| Discovery | `Fit_Assessment.md` | Markdown | Templates/Fit_Assessment.md |
| Propuesta | `Proposal.md` | Docx/PDF | Templates/Proposal_Template.md |
| Cierre | `Contract.md` | PDF | Templates/Contract_Template.md |
| Cierre | `Invoice.md` | PDF/XML | Templates/Invoice_Template.md |
| Onboarding | `Welcome_Kit.md` | PDF | Templates/Welcome_Kit.md |
| Onboarding | `Onboarding_Checklist.md` | Markdown | Templates/Onboarding_Checklist.md |

---

*Fin del documento — Sales_Process.md v1.0*
