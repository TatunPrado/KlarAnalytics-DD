# Diseño del CRM

> **Sistema Operativo** — CRM Model de Klar Analytics
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Arquitectura del CRM](#1-arquitectura-del-crm)
2. [Pipeline de Ventas](#2-pipeline-de-ventas)
3. [Gestión de Contactos](#3-gestión-de-contactos)
4. [Gestión de Oportunidades](#4-gestión-de-oportunidades)
5. [Secuencias de Comunicación](#5-secuencias-de-comunicación)
6. [Automatizaciones](#6-automatizaciones)
7. [Dashboards y Reportes](#7-dashboards-y-reportes)
8. [Implementación MVP](#8-implementación-mvp)
9. [Migración a CRM Profesional](#9-migración-a-crm-profesional)

---

## 1. Arquitectura del CRM

### 1.1 Visión General

```
                    ┌─────────────────────────────────────┐
                    │              CRM Klar Analytics      │
                    │         (MVP: Sheets → HubSpot)      │
                    └─────────────────────────────────────┘

┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
│  Pipeline  │  │  Contacts  │  │  Companies │  │  Deals     │  │ Activities │
│  (Etapas)  │  │  (Personas)│  │  (Empresas)│  │ (Oportunid)│  │(Actividad) │
└────────────┘  └────────────┘  └────────────┘  └────────────┘  └────────────┘
```

### 1.2 Funcionalidades por Fase

| Funcionalidad | MVP (Sheets) | Intermedio (HubSpot Free) | Avanzado (HubSpot Pro) |
|---|---|---|---|
| Pipeline de ventas | Manual | Visual | Automatizado |
| Contactos | Hoja simple | Importación | Enriquecimiento |
| Oportunidades | Manual | Tracking | Forecasting |
| Secuencias de email | Manual | Plantillas | Automatizado |
| Dashboards | Manual | Predefinidos | Personalizados |
| Automatizaciones | Apps Script | Workflows | Workflows avanzados |
| Integración ERP | Manual | API | API bidireccional |

---

## 2. Pipeline de Ventas

### 2.1 Etapas del Pipeline

| Etapa | Código | Descripción | % Probabilidad | Acción Siguiente |
|---|---|---|---|---|
| **Nuevo Lead** | new | Lead ingresado, sin calificar | 10% | Calificar (BANT) |
| **Calificado** | qualified | BANT completo, listo para discovery | 25% | Agendar discovery |
| **Discovery** | discovery | Discovery call realizada | 40% | Preparar propuesta |
| **Propuesta** | proposal | Propuesta enviada | 60% | Follow-up |
| **Negociación** | negotiation | En negociación | 75% | Cerrar |
| **Ganado** | won | Contrato firmado + pago | 100% | Onboarding |
| **Perdido** | lost | No compró | 0% | Analizar + nutrir |
| **Archivado** | archived | Sin actividad > 90 días | 0% | Newsletter |

### 2.2 Campos por Oportunidad (Deal)

| Campo | Tipo | Ejemplo |
|---|---|---|
| deal_id | ID | DEAL-001 |
| company_id | Relación | Company A |
| contact_id | Relación | Juan Pérez |
| deal_name | Texto | Diagnóstico Integral - Company A |
| stage | Etapa | proposal |
| amount | Moneda | $4,500 |
| probability | % | 60% |
| expected_close_date | Fecha | 2026-07-15 |
| diagnosis_type | Selección | integral |
| source | Selección | linkedin |
| owner | Persona | Ventas |
| created_at | Fecha | 2026-06-01 |
| last_activity | Fecha | 2026-06-10 |
| notes | Texto | Cliente interesado en finanzas |

### 2.3 Reglas de Movimiento entre Etapas

| De | A | Condición |
|---|---|---|
| new | qualified | BANT ≥ 3/4 |
| qualified | discovery | Discovery call agendada |
| discovery | proposal | Fit score ≥ 4/5 + scope definido |
| proposal | negotiation | Cliente solicitó cambios en pricing |
| proposal | won | Contrato firmado |
| negotiation | won | Contrato firmado + pago |
| any | lost | Cliente dijo no, o sin respuesta > 30 días |
| any | archived | Sin actividad > 90 días |

---

## 3. Gestión de Contactos

### 3.1 Perfil de Contacto

| Sección | Campos |
|---|---|
| **Datos Básicos** | Nombre, email, teléfono, cargo |
| **Empresa** | Razón social, industria, tamaño |
| **Rol en Venta** | ¿Decision maker? ¿Influyente? ¿Usuario? |
| **Actividad** | Última interacción, próxima acción, histórico |
| **Preferencias** | Canal preferido, mejor horario, idioma |
| **Notas** | Notas libres del equipo comercial |

### 3.2 Segmentación de Contactos

| Segmento | Criterio | Estrategia |
|---|---|---|
| **Hot Leads** | BANT completo, en discovery | Contacto directo, alta frecuencia |
| **Warm Leads** | BANT parcial, en nutrición | Secuencia automatizada |
| **Cold Leads** | Sin actividad > 30 días | Re-engagement trimestral |
| **Clientes Activos** | Diagnóstico en curso | Check-ins regulares (CS) |
| **Clientes Históricos** | Diagnóstico completado | Upsell / Cross-sell / Referidos |
| **Promotores** | NPS ≥ 9 | Pedir testimonio, referidos |
| **Detractores** | NPS ≤ 6 | Plan de recuperación |
| **Referidos** | Llegaron por recomendación | Prioridad alta, agradecimiento |

### 3.3 Enriquecimiento de Contactos

| Fuente | Datos | Automatizable |
|---|---|---|
| LinkedIn | Cargo, empresa, industria, conexiones | Manual |
| Web (formulario) | Nombre, email, empresa, teléfono | Sí |
| Discovery Call | Necesidades, presupuesto, timeline | Manual |
| Redes sociales | Intereses, actividad | Manual (ocasional) |

---

## 4. Gestión de Oportunidades

### 4.1 Ciclo de Vida de la Oportunidad

```
Lead → Calificación → Discovery → Propuesta → Negociación → Won/Lost
                                                              │
                                                    ┌─────────┴─────────┐
                                                    │                   │
                                               Won (contrato)     Lost (analizar)
```

### 4.2 Actividades por Oportunidad

| Actividad | Responsable | Trigger |
|---|---|---|
| Envío de propuesta | Ventas | Discovery completado |
| Follow-up día 1 | Ventas | Propuesta enviada |
| Follow-up día 3 | Ventas | Sin respuesta |
| Follow-up día 7 | Ventas | Sin respuesta |
| Llamada de cierre | Ventas | Cliente interesado |
| Envío de contrato | Admin | Aceptación verbal |
| Envío de factura | Admin | Contrato firmado |
| Onboarding | Delivery Lead | Pago recibido |

### 4.3 Registro de Actividades

| Campo | Tipo | Ejemplo |
|---|---|---|
| activity_id | ID | ACT-001 |
| deal_id | Relación | DEAL-001 |
| type | Selección | call / email / meeting / task |
| subject | Texto | Discovery Call - Company A |
| description | Texto | Cliente interesado en mejorar flujo de caja |
| due_date | Fecha | 2026-06-10 |
| completed_date | Fecha | 2026-06-10 |
| owner | Persona | Ventas |
| outcome | Selección | positive / neutral / negative |

---

## 5. Secuencias de Comunicación

### 5.1 Secuencia de Nutrición (Lead → Calificado)

| Paso | Día | Canal | Contenido |
|---|---|---|---|
| 1 | 0 | Email | "Gracias por tu interés" + Klar Analytics overview |
| 2 | 3 | Email | "¿Sabías que el 60% de las PyMEs..." (contenido educativo) |
| 3 | 7 | Email | Caso de éxito relevante para su industria |
| 4 | 14 | Email + Call | "¿Te gustaría agendar un discovery?" |

### 5.2 Secuencia de Propuesta (Propuesta → Cierre)

| Paso | Día | Canal | Contenido |
|---|---|---|---|
| 1 | 0 | Email | Propuesta adjunta + resumen |
| 2 | 1 | Email | "¿Recibiste la propuesta?" |
| 3 | 3 | Email | "¿Tienes alguna duda?" |
| 4 | 5 | Call | Follow-up telefónico |
| 5 | 7 | Email | Último seguimiento antes de archivar |

### 5.3 Secuencia de Re-engagement (Lead Frío)

| Paso | Día | Canal | Contenido |
|---|---|---|---|
| 1 | 0 | Email | "¿Todavía estás interesado?" |
| 2 | 7 | Email | Nuevo contenido relevante |
| 3 | 30 | Call | Último intento de contacto |
| 4 | 90 | — | Mover a "Archivado" |

---

## 6. Automatizaciones

### 6.1 Automatizaciones del CRM

| ID | Disparador | Acción | Estado |
|---|---|---|---|
| CRM-A1 | Nuevo lead creado | Enviar email de bienvenida, asignar owner | MVP |
| CRM-A2 | Lead pasa a "qualified" | Notificar a ventas (Slack) | MVP |
| CRM-A3 | Discovery completado | Enviar email de agradecimiento + resumen | MVP |
| CRM-A4 | Propuesta enviada | Crear tareas de follow-up (días 1,3,7) | MVP |
| CRM-A5 | Propuesta no vista en 5 días | Email de re-engagement | MVP |
| CRM-A6 | Oportunidad ganada | Crear contrato, notificar a admin | Futuro |
| CRM-A7 | Oportunidad perdida | Mover a nutrición, registrar motivo | MVP |
| CRM-A8 | 30 días sin actividad | Alerta a owner | MVP |
| CRM-A9 | Lead score ≥ 80 | Priorizar, notificar urgente | Futuro |
| CRM-A10 | NPS registrado ≤ 6 | Alerta a Director + CS | Futuro |

### 6.2 Reglas de Notificación

| Evento | Notificar a | Canal | Prioridad |
|---|---|---|---|
| Nuevo lead calificado (score ≥ 80) | Ventas | Slack + Email | Alta |
| Propuesta enviada | Ventas (auto) | Tarea CRM | Media |
| Oportunidad ganada | Todos | Slack | Alta |
| Oportunidad perdida | Ventas | Notificación CRM | Media |
| NPS ≤ 6 | Director + CS | Email + Slack | Urgente |
| Pago recibido | Admin + Delivery Lead | Slack | Alta |
| Factura vence mañana | Admin | Email | Alta |

---

## 7. Dashboards y Reportes

### 7.1 Dashboard de Ventas (Tiempo Real)

| Widget | Fuente | Actualización |
|---|---|---|
| **Pipeline Value** (suma de deals abiertos × probabilidad) | Deals | En tiempo real |
| **Deals por Etapa** (conteo + valor) | Deals | En tiempo real |
| **Actividades Vencidas** (tareas sin completar) | Activities | En tiempo real |
| **Top 5 Oportunidades** (por valor) | Deals | En tiempo real |
| **Últimas Actividades** (feed) | Activities | En tiempo real |

### 7.2 Reportes Semanales

| Reporte | Destinatario | Contenido |
|---|---|---|
| **Pipeline Review** | Equipo | Leads nuevos, cambios de etapa, próximos pasos |
| **Actividades** | Ventas | Llamadas realizadas, emails enviados, reuniones |
| **Proyección de Cierre** | Director | Expected revenue para el mes |

### 7.3 Reportes Mensuales

| Reporte | Destinatario | Contenido |
|---|---|---|
| **Sales Performance** | Dirección | Leads generados, tasa de conversión, win rate, avg ticket |
| **Pipeline Health** | Dirección | Valor del pipeline, distribución por etapa, antigüedad |
| **Forecast** | Dirección | Proyección de ingresos a 30/60/90 días |

---

## 8. Implementación MVP (Google Sheets)

### 8.1 Estructura de Hojas

```
📊 CRM Klar Analytics /
├── Pipeline           // Deals activos (una fila por oportunidad)
├── Contacts           // Todos los contactos
├── Companies          // Todas las empresas
├── Activities         // Registro de actividades
├── Email_Sequences    // Secuencias de email
└── _Config            // Valores, enums, fórmulas
```

### 8.2 Campos de la Hoja Pipeline

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deal ID | Company | Contact | Deal Name | Stage | Amount | Probability | Expected Value | Close Date | Owner | Source | Last Activity | Notes |
| DEAL-001 | Company A | Juan P. | Diag. Integral | proposal | $4,500 | 60% | $2,700 | 15/07 | Ventas | LinkedIn | 10/06 | Interesado en finanzas |

### 8.3 Fórmulas Clave

| Propósito | Fórmula |
|---|---|
| Valor esperado del deal | `=F2*G2` |
| Pipeline total | `=SUMA(H:H)` |
| Pipeline por etapa | `=SUMAR.SI.CONJUNTO(H:H;E:E;"proposal")` |
| Próximo paso (vencimiento) | `=SI(HOY()>I2;"VENCIDO";I2-HOY()&" días")` |

### 8.4 Apps Script (Automatización)

```javascript
// Enviar notificación cuando un deal cambia a "won"
function onEdit(e) {
  var range = e.range;
  var sheet = range.getSheet();
  if (sheet.getName() === "Pipeline" && range.getColumn() === 5) {
    var newValue = range.getValue();
    if (newValue === "won") {
      var row = range.getRow();
      var company = sheet.getRange(row, 2).getValue();
      MailApp.sendEmail(
        "admin@klaranalytics.com",
        "🎉 Nuevo Cliente Ganado: " + company,
        "Se ha ganado un nuevo cliente: " + company + ". Iniciar onboarding."
      );
    }
  }
}
```

---

## 9. Migración a CRM Profesional

### 9.1 Criterios para Migrar

| Criterio | Umbral |
|---|---|
| Número de contactos | > 500 |
| Número de oportunidades/mes | > 20 |
| Tamaño del equipo de ventas | > 3 personas |
| Leads generados/mes | > 100 |
| Necesidad de automatización avanzada | Sí/No |

### 9.2 Opciones de CRM

| CRM | Ideal para | Costo | Automatización | Complejidad |
|---|---|---|---|---|
| **HubSpot (Free/Starter)** | Pequeño equipo, escalable | Gratuito / $50/mes | Alta | Baja |
| **Pipedrive** | Pipeline visual, ventas | $15/mes | Media | Baja |
| **Salesforce** | Empresa grande | $25/mes | Muy alta | Alta |
| **Monday CRM** | Equipos pequeños | $12/mes | Media | Baja |
| **Custom (Supabase + App)** | Control total | $10-50/mes (hosting) | Total | Alta |

### 9.3 Plan de Migración

| Fase | Actividad | Duración |
|---|---|---|
| **1** | Exportar datos de Sheets a CSV | 1 día |
| **2** | Mapear campos del CRM destino | 2 días |
| **3** | Importar Companies → Contacts → Deals → Activities | 1 día |
| **4** | Configurar pipelines y automatizaciones | 3 días |
| **5** | Configurar dashboards | 2 días |
| **6** | Capacitar al equipo | 1 día |
| **7** | Desactivar Sheets CRM (mantener como backup 30 días) | — |

---

*Fin del documento — CRM_Model.md v1.0*
