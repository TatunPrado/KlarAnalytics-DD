# Discovery_Interview

> **Procedimiento Operativo Estándar (SOP)** — Entrevista de Descubrimiento Empresarial para PyMEs
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Propósito y Alcance](#1-propósito-y-alcance)
2. [Preparación de la Entrevista](#2-preparación-de-la-entrevista)
3. [Estructura General](#3-estructura-general)
4. [Bloque 0: Apertura y Rapport](#4-bloque-0-apertura-y-rapport)
5. [Bloque 1: Perfil de la Empresa](#5-bloque-1-perfil-de-la-empresa)
6. [Bloque 2: Modelo de Negocio y Propuesta de Valor](#6-bloque-2-modelo-de-negocio-y-propuesta-de-valor)
7. [Bloque 3: Situación Financiera](#7-bloque-3-situación-financiera)
8. [Bloque 4: Operaciones y Procesos](#8-bloque-4-operaciones-y-procesos)
9. [Bloque 5: Organización y Talento](#9-bloque-5-organización-y-talento)
10. [Bloque 6: Riesgos y Entorno](#10-bloque-6-riesgos-y-entorno)
11. [Bloque 7: Objetivos y Expectativas](#11-bloque-7-objetivos-y-expectativas)
12. [Bloque 8: Cierre y Documentación](#12-bloque-8-cierre-y-documentación)
13. [Árboles de Decisión](#13-árboles-de-decisión)
14. [Señales de Alerta](#14-señales-de-alerta)
15. [Documentación Recomendada](#15-documentación-recomendada)
16. [Output Final: Brief_Empresa.md](#16-output-final-brief_empresamd)

---

## 1. Propósito y Alcance

### 1.1 Objetivo General
Recolectar información cualitativa y cuantitativa completa de una PyME mediante una entrevista semi-estructurada que cubra todas las dimensiones del negocio (modelo de negocio, finanzas, operaciones, organización y riesgos), generando un archivo `Brief_Empresa.md` estandarizado que alimentará a los agentes de diagnóstico posteriores.

### 1.2 Perfil del Entrevistado Ideal
- Fundador, CEO, Gerente General o socio mayoritario
- Conocimiento profundo del negocio (mínimo 2 años en el cargo)
- Idealmente: visión integral del área comercial, financiera y operativa

### 1.3 Modalidades de Entrevista
| Modalidad | Duración | Formato | Cuándo Usar |
|---|---|---|---|
| Presencial | 60–90 min | Cara a cara | Cliente local, alta confianza |
| Videollamada | 45–75 min | Zoom/Meet/Teams | Cliente remoto, estándar |
| Asíncrona | 7 días | Cuestionario + audio | Cliente sin disponibilidad horaria |
| Híbrida | 45 min (sincrónica) + 3 días (asíncrona) | Mix | Cliente con agenda limitada |

### 1.4 Precondiciones
- [ ] El entrevistador (Interview_Orchestrator) conoce el perfil básico del cliente (industria, tamaño, ubicación)
- [ ] La guía de entrevista está cargada en el contexto del agente
- [ ] El cliente ha sido informado de la duración estimada y objetivos
- [ ] El cliente ha firmado acuerdo de confidencialidad (NDA) si aplica
- [ ] Herramienta de captura (transcripción) activa

---

## 2. Preparación de la Entrevista

### 2.1 Investigación Previa (15 min antes de la entrevista)

```
1. Buscar la empresa en fuentes públicas (LinkedIn, sitio web, Google My Business)
2. Identificar:
   - Año de fundación
   - Tamaño (empleados, facturación estimada)
   - Principales productos/servicios
   - Presencia digital
   - Reseñas de clientes (Google, Social Media)
3. Preparar datos de benchmark rápido de la industria:
   - Margen bruto típico del sector
   - Ratios de liquidez recomendados
   - Tasa de crecimiento del mercado
4. Personalizar guía de entrevista según industria y tamaño
```

### 2.2 Checklist de Preparación

- [ ] Investigación previa completada
- [ ] Guía de entrevista personalizada cargada
- [ ] Sistema de transcripción listo
- [ ] Temporizador configurado (alertas a 60 min y 75 min)
- [ ] Lista de documentos a solicitar preparada
- [ ] Brief_Empresa.md template cargado para completar en vivo
- [ ] Preguntas obligatorias según tipo de empresa seleccionadas

### 2.3 Clasificación Inicial de la Empresa

Antes de comenzar, clasificar la empresa en uno de estos arquetipos para ajustar el enfoque:

| Arquetipo | Descripción | Enfoque de Entrevista |
|---|---|---|
| **Startup** | 0–5 años, buscando crecimiento | Validación de modelo, unit economics, financiamiento |
| **PyME Familiar** | Dueño fundador, familia en gestión | Sucesión, profesionalización, gobierno |
| **PyME Consolidada** | 5–20 años, rentable, estable | Escalamiento, eficiencia, competitividad |
| **PyME en Crisis** | Caída de ventas, problemas de caja | Supervivencia, racionalización, reestructuración |
| **PyME Profesionalizada** | Gerentes no dueños, procesos formales | Optimización, innovación, transformación digital |
| **Emprendimiento Individual** | Dueño = único empleado clave | Automatización, delegación, escalabilidad |

---

## 3. Estructura General

### 3.1 Timeline de la Entrevista

```
[0:00]  Bloque 0: Apertura y Rapport          (5 min)
[0:05]  Bloque 1: Perfil de la Empresa        (10 min)
[0:15]  Bloque 2: Modelo de Negocio            (15 min)
[0:30]  Bloque 3: Situación Financiera         (15 min)
[0:45]  Bloque 4: Operaciones y Procesos       (12 min)
[0:57]  Bloque 5: Organización y Talento       (10 min)
[1:07]  Bloque 6: Riesgos y Entorno            (8 min)
[1:15]  Bloque 7: Objetivos y Expectativas     (8 min)
[1:23]  Bloque 8: Cierre y Documentación       (7 min)
[1:30]  Fin
```

### 3.2 Técnica de Preguntas

Usar la **Pirámide de Profundidad** en cada bloque:

```
Nivel 1 (Superficie):   Preguntas cerradas para hechos (¿Cuántos empleados?)
Nivel 2 (Exploración):  Preguntas abiertas para contexto (¿Cómo organizó eso?)
Nivel 3 (Profundidad):  Preguntas de causa raíz (¿Por qué cree que pasa eso?)
Nivel 4 (Reflexión):    Preguntas de impacto (¿Qué efecto tiene eso en el negocio?)
```

### 3.3 Formato de Registro

Cada bloque debe registrar:

| Campo | Descripción |
|---|---|
| `bloque` | Nombre del bloque temático |
| `respuestas_textuales` | Citas textuales del cliente (entre 1 y 3 frases clave) |
| `hechos_constatables` | Datos objetivos extraídos |
| `impresiones_analista` | Notas subjetivas del analista (marcadas como "IMPRESIÓN:") |
| `alertas_detectadas` | Señales de alerta (con código AL-XX) |
| `info_faltante` | Información que no se pudo obtener y debe solicitarse después |

---

## 4. Bloque 0: Apertura y Rapport

**Duración:** 5 min | **Técnica:** Rapport + encuadre

### 4.1 Guion de Apertura

```
"Gracias por tomarse el tiempo [nombre del cliente]. 
El objetivo de esta entrevista es entender su negocio en profundidad 
para poder ofrecerle un diagnóstico preciso y recomendaciones accionables.

Vamos a cubrir 5 áreas principales: su modelo de negocio, la parte financiera, 
cómo operan, cómo está organizado el equipo y los riesgos que enfrentan.

No hay respuestas correctas o incorrectas — mientras más honesto sea, 
más valor podremos generar. Si hay algo que no sepa o no quiera responder, 
no hay problema, me lo dice y seguimos adelante.

¿Le parece bien si grabo la conversación solo para asegurar que no se me escape nada?"
```

### 4.2 Preguntas de Rapport (Obligatorias)

| # | Pregunta | Objetivo |
|---|---|---|
| R0.1 | Cuénteme brevemente: ¿cuál es su rol en la empresa y desde cuándo está involucrado? | Validar perfil del entrevistado |
| R0.2 | En una frase, ¿cuál diría que es el propósito o razón de ser de su empresa? | Obtener declaración de propósito |
| R0.3 | ¿Cómo está el ánimo general hoy? ¿Qué le gustaría que pasara como resultado de este diagnóstico? | Medir expectativas y urgencia |

### 4.3 Reglas de Profundización

| Si el entrevistado... | Entonces... |
|---|---|
| Da respuestas muy cortas | Usar preguntas Nivel 2: "Cuénteme más sobre..." |
| Se muestra ansioso o defensivo | Reforzar confidencialidad, tono más pausado |
| Habla demasiado sin estructura | Redirigir suavemente: "Entiendo, enfoquémonos en..." |
| Menciona una crisis desde el inicio | Saltar a Bloque 6 (Riesgos) y luego volver |

---

## 5. Bloque 1: Perfil de la Empresa

**Duración:** 10 min | **Objetivo:** Obtener datos demográficos y estructurales básicos

### 5.1 Preguntas Obligatorias

| # | Pregunta | Dato a Obtener | Validación |
|---|---|---|---|
| P1.1 | ¿Cuál es la razón social y el nombre comercial? | Nombre legal y de marca | Coincidencia con documentos |
| P1.2 | ¿En qué año se fundó la empresa? | Año de fundación | Consistencia con antigüedad |
| P1.3 | ¿Cuántos empleados tiene actualmente? (Tiempo completo y parcial) | Plantilla | Ratio empleados/facturación |
| P1.4 | ¿Cuál fue la facturación del último año fiscal? (y el anterior si es posible) | Ingresos anuales | Consistencia con industria |
| P1.5 | ¿Cuál es su mercado geográfico principal? (Local, regional, nacional, internacional) | Alcance geográfico | Coherencia con logística |
| P1.6 | ¿En qué industria o sector compite principalmente? | Clasificación NAICS/CIIU | Benchmarking |
| P1.7 | ¿Cuál es su principal producto o servicio? (El que genera más ingresos) | Core business | Claridad de propuesta |
| P1.8 | ¿Quiénes son sus clientes principales? (Segmentos) | Tipos de cliente | Coherencia con canales |

### 5.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| P1.9 | ¿Tienen sucursales o múltiples ubicaciones? | Si la empresa es > 20 empleados |
| P1.10 | ¿La empresa tiene deuda bancaria o con socios? | Siempre que sea posible (sensible) |
| P1.11 | ¿Están constituidos como persona física o moral? ¿Régimen fiscal? | Si la estructura legal es relevante |
| P1.12 | ¿Tienen certificaciones o registros especiales? | Si la industria lo requiere |

### 5.3 Árbol de Decisión: Perfil de Empresa

```
¿Facturación disponible?
├── Sí → ¿Facturación > 50M USD?
│        ├── Sí → FUERA DE ALCANCE PyME. Registrar, continuar con modo "gran empresa"
│        └── No → Continuar normal
└── No → Estimar por:
         ├── Empleados × (facturación promedio industria) → "Estimado"
         └── Marcar como "facturación no declarada"

¿Empleados declarados?
├── Sí → ¿Empleados consistentes con facturación?
│        ├── Sí → OK
│        └── No → Marcar alerta AL-PER-01 (inconsistencia empleados/ingresos)
└── No → Solicitar rango (1-5, 6-15, 16-50, 51-250)

¿Años de operación?
├── < 2 años → Activar modo "Startup temprana" — enfoque en validación
├── 2-10 años → Modo "PyME en desarrollo" — enfoque en crecimiento
└── > 10 años → Modo "PyME madura" — enfoque en eficiencia y legado
```

---

## 6. Bloque 2: Modelo de Negocio y Propuesta de Valor

**Duración:** 15 min | **Objetivo:** Entender cómo la empresa crea, entrega y captura valor

### 6.1 Preguntas Obligatorias

| # | Pregunta | Dimensión Canvas | Objetivo |
|---|---|---|---|
| MN.1 | ¿Qué problema resuelve o qué necesidad satisface su producto/servicio? | Propuesta de Valor | Validar propuesta de valor |
| MN.2 | ¿Qué diferencia a su oferta de la competencia? | Propuesta de Valor | Identificar ventaja competitiva |
| MN.3 | ¿Quién es su cliente ideal? (Describa el perfil del cliente que más valor aporta) | Segmentos de Cliente | Definir segmento objetivo |
| MN.4 | ¿Cómo llega su producto/servicio al cliente? (Venta directa, distribuidores, online, tienda) | Canales | Mapear canales |
| MN.5 | ¿Cómo es la relación con sus clientes? (Asistencia personal, automatizada, comunidad, co-creación) | Relaciones Cliente | Evaluar tipo de relación |
| MN.6 | ¿Cómo genera ingresos? (Venta directa, suscripción, comisión, publicidad, licencias) | Fuentes de Ingreso | Validar modelo de monetización |
| MN.7 | ¿Cuáles son los costos más grandes de su operación? | Estructura de Costos | Identificar cost drivers |
| MN.8 | ¿Qué actividades internas son críticas para que el negocio funcione? | Actividades Clave | Identificar core processes |
| MN.9 | ¿Qué recursos (físicos, intelectuales, humanos, financieros) son indispensables? | Recursos Clave | Identificar activos críticos |
| MN.10 | ¿Quiénes son sus socios clave? (Proveedores estratégicos, alianzas, joint ventures) | Socios Clave | Mapear ecosistema |

### 6.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| MN.11 | ¿Han pivotado su modelo de negocio alguna vez? ¿Por qué? | Siempre que el cliente mencione cambios |
| MN.12 | ¿Hay clientes que usan su producto de forma diferente a la esperada? | Si hay sospecha de usos no previstos |
| MN.13 | ¿Cuál es el ticket promedio por cliente? | Siempre |
| MN.14 | ¿Qué % de sus ingresos viene del cliente top 3? | Para evaluar concentración |
| MN.15 | ¿Tienen clientes que dejaron de comprar? ¿Sabe por qué? | Para identificar churn |

### 6.3 Árbol de Decisión: Modelo de Negocio

```
¿Propuesta de valor clara?
├── Sí → ¿Diferente a competidores?
│        ├── Sí → Ventaja competitiva identificada → continuar
│        └── No → Marcar alerta AL-MN-01 (commoditización)
└── No → Profundizar: "¿Qué es lo que el cliente valora más de usted?"
         ├── Aún no claro → Marcar alerta AL-MN-02 (propuesta de valor difusa)
         └── Claro ahora → Actualizar registro

¿Fuente de ingresos diversificada?
├── Sí (2+) → Evaluar contribución relativa
└── No (1 sola) → ¿Es estable?
         ├── Sí → Monitorear concentración
         └── No → Marcar alerta AL-MN-03 (dependencia de un solo ingreso)

¿Clientes leales o transaccionales?
├── Clientes recurrentes (>50% ingresos) → Modelo relacional
└── Clientes nuevos cada vez → Modelo transaccional → evaluar LTV y CAC
```

### 6.4 Información Mínima Requerida para este Bloque

- [ ] Problema o necesidad que resuelve
- [ ] Diferenciación vs competidores
- [ ] Segmento(s) de cliente definido(s)
- [ ] Canales de distribución identificados
- [ ] Fuente(s) de ingreso principal
- [ ] Principales costos operativos

---

## 7. Bloque 3: Situación Financiera

**Duración:** 15 min | **Objetivo:** Obtener datos cuantitativos y percepción cualitativa de la salud financiera

### 7.1 Preguntas Obligatorias

| # | Pregunta | Indicador | Dato a Obtener |
|---|---|---|---|
| F.1 | ¿Cuánto fueron sus ingresos el año pasado? ¿Y el anterior? | Crecimiento de ingresos | Valores anuales |
| F.2 | ¿Cuál es su margen de utilidad? (¿Cuánto queda después de costos directos y gastos?) | Rentabilidad | Margen neto estimado |
| F.3 | ¿Cuánto tiempo tardan en pagarle sus clientes? (días) | Días de Cuentas por Cobrar | Días promedio |
| F.4 | ¿A cuántos días paga a sus proveedores? | Días de Cuentas por Pagar | Días promedio |
| F.5 | ¿Mantienen inventario? ¿Cuántos días de venta tienen en inventario? | Rotación de inventario | Días de inventario |
| F.6 | ¿Tiene deudas bancarias o financieras actualmente? | Endeudamiento | Monto y condiciones |
| F.7 | ¿Cómo describiría la liquidez de la empresa? (¿Tiene efectivo disponible para operar?) | Liquidez | Percepción + datos |
| F.8 | ¿Cuánto gasta al mes en nómina? | Gastos de personal | Monto mensual |
| F.9 | ¿El negocio es estacional? ¿En qué meses ingresan más/menos? | Estacionalidad | Patrón de ingresos |

### 7.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| F.10 | ¿Tienen estados financieros actualizados? ¿Quién los prepara? | Siempre |
| F.11 | ¿Cuál es el sueldo del dueño o dividendos que se retira al año? | Si hay apertura |
| F.12 | ¿Han solicitado créditos recientemente? ¿Los aprobaron? | Si mencionan necesidad de capital |
| F.13 | ¿Cuánto invierten al año en marketing y ventas? | Si hay datos |
| F.14 | ¿Calculan el costo de adquisición de cliente (CAC)? | Siempre que tengan marketing digital |
| F.15 | ¿Tienen presupuesto formal? ¿Hacen proyecciones? | Para evaluar madurez financiera |

### 7.3 Datos Cuantitativos Mínimos a Solicitar

| Dato | Formato | Criticidad |
|---|---|---|
| Ingresos últimos 2 años | Valor numérico (USD/MXN/ARS) | **Alta** |
| Margen neto o costo de ventas | Porcentaje o valor | **Alta** |
| Días de cobro (DC) | Número de días | **Alta** |
| Días de pago (DP) | Número de días | **Alta** |
| Días de inventario (DI) | Número de días | Media |
| Gasto mensual de nómina | Valor numérico | **Alta** |
| Deuda total | Valor numérico | Media |
| Facturación del mejor y peor mes | Valores numéricos | Media |

### 7.4 Cálculos Rápidos en Vivo

Durante la entrevista, el agente debe calcular en tiempo real:

```
Ciclo de Conversión de Efectivo (CCC) = DC + DI - DP
  → Si CCC > 60 días: AL-FI-01 (ciclo de caja largo, riesgo de liquidez)

Relación Nómina / Ingresos = (Nómina mensual × 12) / Ingresos anuales
  → Si > 40%: AL-FI-02 (estructura de costos rígida)

Crecimiento de ingresos = (Ingreso Año Actual - Ingreso Año Anterior) / Ingreso Año Anterior
  → Si < 0%: AL-FI-03 (decrecimiento)
  → Si 0-5%: AL-FI-04 (crecimiento vegetativo)
  → Si > 20%: evaluar sostenibilidad
```

### 7.5 Árbol de Decisión: Financiero

```
¿Estados financieros disponibles?
├── Sí → Solicitar copia, marcar como "datos verificables"
└── No → Activar modo "estimaciones basadas en entrevista"
         → ¿Facturación disponible?
              ├── Sí → Preguntar estructura de costos:
              │        → ¿Cuánto es el costo de los productos vendidos? (margen bruto)
              │        → ¿Cuánto gastan en operación al mes? (gastos fijos)
              └── No → No se puede estimar rentabilidad → AL-FI-05 (datos financieros insuficientes)

¿CCC calculado?
├── CCC ≤ 30 días → Salud de caja buena
├── CCC 31-60 días → Atención moderada
└── CCC > 60 días → AL-FI-01 activada → Profundizar:
         → ¿Por qué los clientes tardan en pagar?
         → ¿Han intentado factoring o descuento por pronto pago?
         → ¿Tienen línea de crédito para capital de trabajo?

¿Margen reportado vs industria?
├── Margen > benchmark → Ventaja competitiva confirmada
├── Margen ~ benchmark → Competitivo
└── Margen < benchmark → AL-FI-06 (margen bajo) → preguntar por qué
```

---

## 8. Bloque 4: Operaciones y Procesos

**Duración:** 12 min | **Objetivo:** Entender cómo opera la empresa en el día a día

### 8.1 Preguntas Obligatorias

| # | Pregunta | Dimensión | Objetivo |
|---|---|---|---|
| O.1 | ¿Cuáles son los 3 procesos más importantes para que el negocio funcione? | Procesos clave | Identificar core processes |
| O.2 | ¿Cómo describiría la eficiencia de sus operaciones? (¿Hay demoras, errores, reprocesos?) | Eficiencia | Evaluar percepción de eficiencia |
| O.3 | ¿Tienen procesos documentados? (Manuales, procedimientos, instructivos) | Estandarización | Nivel de formalización |
| O.4 | ¿Cuánto tiempo pasa desde que reciben un pedido hasta que lo entregan? | Lead time | Tiempo de entrega |
| O.5 | ¿Cuál es su principal cuello de botella o limitación hoy? | Restricciones | Identificar bottleneck |
| O.6 | ¿Usan algún software o sistema para gestionar la operación? (ERP, CRM, POS, etc.) | Tecnología | Nivel de digitalización |
| O.7 | ¿Cómo manejan la calidad? (Inspecciones, métricas, reclamos) | Calidad | Control de calidad |
| O.8 | ¿Tienen proveedores críticos? (¿Qué pasa si uno falla?) | Cadena de suministro | Dependencia de proveedores |

### 8.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| O.9 | ¿Cuánto tiempo toma capacitar a un empleado nuevo para que sea productivo? | Si hay rotación o crecimiento |
| O.10 | ¿Tienen indicadores de producción o servicio? ¿Los revisan periódicamente? | Si hay datos operativos |
| O.11 | ¿Han implementado alguna mejora de procesos en el último año? | Para evaluar cultura de mejora |
| O.12 | ¿Qué porcentaje de su capacidad están usando hoy? | Si la operación es sensible a capacidad |
| O.13 | ¿Tercerizan alguna parte de su operación? ¿Cuál? | Para evaluar modelo operativo |

### 8.3 Árbol de Decisión: Operaciones

```
¿Procesos documentados?
├── Sí (todos) → Madurez nivel 3+ → enfocar en optimización
├── Algunos → Madurez nivel 2 → evaluar qué falta
└── No → Madurez nivel 1 → ¿Es crítico?
         ├── < 5 empleados → Natural, no forzar
         └── ≥ 5 empleados → AL-OP-01 (falta de estandarización)

¿Software de gestión?
├── ERP/CRM implementado → ¿Se usa realmente?
│        ├── Sí → Madurez digital media-alta
│        └── No → AL-OP-02 (herramienta subutilizada)
├── Solo Excel/Google Sheets → Madurez digital básica
└── Todo papel/manual → AL-OP-03 (digitalización nula)

¿Cuello de botella identificado?
├── Sí → ¿El cliente sabe la causa?
│        ├── Sí → Registrar, evaluar solución en E11
│        └── No → Profundizar con 5 Whys rápido
└── No → ¿Hay demoras o problemas de calidad?
         ├── Sí → Hay bottleneck no identificado → AL-OP-04
         └── No → Operación estable → continuar
```

---

## 9. Bloque 5: Organización y Talento

**Duración:** 10 min | **Objetivo:** Evaluar estructura organizacional, cultura y gestión del talento

### 9.1 Preguntas Obligatorias

| # | Pregunta | Dimensión | Objetivo |
|---|---|---|---|
| G.1 | ¿Cómo está organizada la empresa? (¿Hay departamentos, gerencias, áreas?) | Estructura | Tipo de organigrama |
| G.2 | ¿Hay alguien más además de usted tomando decisiones importantes? | Delegación | Centralización |
| G.3 | ¿Cómo描述了 la cultura de la empresa? (Formal/informal, colaborativa/competitiva, etc.) | Cultura | Clima y valores |
| G.4 | ¿Cómo es la rotación de personal? (¿Entra y sale mucha gente?) | Estabilidad | Retención de talento |
| G.5 | ¿Qué habilidades clave tiene el equipo hoy? ¿Cuáles les faltan? | Competencias | Brecha de talento |
| G.6 | ¿Cómo atraen y retienen talento? (Sueldos, beneficios, desarrollo) | Atracción | Estrategia de talento |
| G.7 | ¿Cómo se comunican internamente? (Reuniones, WhatsApp, email, pizarra) | Comunicación | Canales internos |

### 9.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| G.8 | ¿Hay un plan de sucesión? (¿Qué pasa si usted falta 1 mes?) | Si el dueño lo es "todo" |
| G.9 | ¿Tienen evaluaciones de desempeño formales? | Si > 15 empleados |
| G.10 | ¿Cuánto tiempo lleva el equipo actual en la empresa? | Si hay alta rotación o mucha antigüedad |
| G.11 | ¿Cómo toman decisiones importantes? (Unilateral, consenso, por áreas) | Para evaluar estilo de liderazgo |
| G.12 | ¿Hay conflictos internos que afecten el trabajo? | Si hay señales en entrevista |

### 9.3 Árbol de Decisión: Organización

```
¿Estructura definida?
├── Sí → ¿Formal o informal?
│        ├── Formal (roles, jerarquías) → Organización madura
│        └── Informal → AL-OR-01 (roles difusos) ¿Afecta la operación?
│              ├── Sí → Priorizar clarificación de roles
│              └── No → Monitorear
└── No → AL-OR-01 + ¿Cuántos empleados?
         ├── < 5 → Natural en empresas pequeñas
         └── ≥ 5 → Requiere estructura mínima

¿Decisiones concentradas en dueño?
├── Sí → ¿Hay empleados que podrían asumir más responsabilidad?
│        ├── Sí → AL-OR-02 (centralización delegable) → oportunidad
│        └── No → AL-OR-03 (dependencia crítica del fundador)
└── No → Distribución saludable

¿Rotación de personal?
├── < 5% anual → Baja saludable
├── 5-15% anual → Normal para el país/industria
└── > 15% anual → AL-OR-04 (rotación alta) → ¿Por qué?
         → Salarios bajos
         → Mal clima
         → Competencia por talento
         → Falta de desarrollo
```

---

## 10. Bloque 6: Riesgos y Entorno

**Duración:** 8 min | **Objetivo:** Identificar riesgos percibidos por el cliente y factores externos

### 10.1 Preguntas Obligatorias

| # | Pregunta | Tipo de Riesgo | Objetivo |
|---|---|---|---|
| R.1 | ¿Cuál diría que es la mayor amenaza que enfrenta su negocio hoy? | Estratégico | Riesgo principal percibido |
| R.2 | ¿Qué pasaría si su principal competidor bajara sus precios un 20%? | Competitivo | Evaluar ventaja competitiva |
| R.3 | ¿Qué pasaría si perdiera a su mejor empleado o su cliente más grande? | Operativo / Concentración | Evaluar dependencias |
| R.4 | ¿Hay algún tema regulatorio, fiscal o legal que le preocupe? | Cumplimiento | Riesgo normativo |
| R.5 | ¿Cómo está la economía del país/sector afectando su negocio? | Macroeconómico | Contexto externo |
| R.6 | ¿Qué es lo que más le preocupa cuando piensa en el futuro del negocio? | General | Riesgos no cubiertos |

### 10.2 Preguntas Opcionales

| # | Pregunta | Cuándo Usar |
|---|---|---|
| R.7 | ¿Tienen seguros? (Incendio, robo, responsabilidad civil, cibernético) | Siempre que no haya salido |
| R.8 | ¿Han tenido problemas legales o laborales recientes? | Si hay señales |
| R.9 | ¿Dependen de algún proveedor único? | Si la cadena de suministro es relevante |
| R.10 | ¿Cómo manejan la ciberseguridad? (Contraseñas, backups, datos) | Si usan sistemas digitales |

### 10.3 Árbol de Decisión: Riesgos

```
¿Riesgo principal identificado?
├── Sí → Clasificar en:
│        ├── Estratégico (competencia, modelo obsoleto)
│        ├── Operativo (proveedores, personal, procesos)
│        ├── Financiero (caja, deuda, clientes)
│        ├── Cumplimiento (fiscal, legal, regulatorio)
│        └── Externo (economía, desastres, pandemia)
│         → Registrar en risk_matrix
└── No → Preguntar de otra forma: "¿Hay algo que le impida dormir?"
         → Si aún no → Riesgos no conscientes → AL-RI-01 (percepción de riesgo baja)

¿Dependencia de cliente único?
├── Cliente > 30% ingresos → AL-RI-02 (alta concentración de clientes)
└── Varios clientes → Riesgo diversificado

¿El entorno es adverso (economía, regulatorio)?
├── Sí → AL-RI-03 (riesgo externo significativo) → evaluar resiliencia
└── No → Continuar
```

---

## 11. Bloque 7: Objetivos y Expectativas

**Duración:** 8 min | **Objetivo:** Capturar las metas del cliente y alinear expectativas del diagnóstico

### 11.1 Preguntas Obligatorias

| # | Pregunta | Objetivo |
|---|---|---|
| E.1 | Si este diagnóstico fuera 100% exitoso, ¿qué habríamos logrado? | Visión de éxito |
| E.2 | ¿Cuáles son sus 3 prioridades principales para el negocio en los próximos 12 meses? | Prioridades explícitas |
| E.3 | ¿Dónde le gustaría ver la empresa en 3 años? | Visión a mediano plazo |
| E.4 | ¿Qué está dispuesto a cambiar para lograr esos objetivos? | Disposición al cambio |
| E.5 | ¿Hay algún tema del que NO haya hablado y que sea importante que sepa? | Temas no cubiertos |

### 11.2 Clasificación de Objetivos

El agente debe categorizar cada objetivo mencionado:

| Categoría | Ejemplos |
|---|---|
| **Crecimiento** | Aumentar ventas X%, abrir nuevo mercado, nuevos productos |
| **Eficiencia** | Reducir costos, mejorar márgenes, automatizar procesos |
| **Estabilidad** | Mejorar flujo de caja, reducir deuda, asegurar clientes |
| **Transformación** | Digitalizar, innovar modelo de negocio, cambiar de industria |
| **Salida / Sucesión** | Vender la empresa, pasar a hijos, jubilación |
| **Supervivencia** | Evitar quiebra, recuperar mercado, pagar deudas |

---

## 12. Bloque 8: Cierre y Documentación

**Duración:** 7 min | **Objetivo:** Cerrar la entrevista, acordar próximos pasos y solicitar documentos pendientes

### 12.1 Preguntas Obligatorias

| # | Pregunta | Objetivo |
|---|---|---|
| C.1 | ¿Hay algo más que quiera agregar que no hayamos cubierto? | Capturar información residual |
| C.2 | ¿Podría compartirnos los documentos que mencionamos? (Listar) | Formalizar solicitud |
| C.3 | ¿Cuál es la mejor forma y horario para darle seguimiento? | Próximos pasos |
| C.4 | ¿Hay alguien más en su equipo con quien deberíamos hablar? | Identificar otras fuentes |

### 12.2 Lista de Documentos a Solicitar (Checklist)

El entrevistador debe marcar cuáles ya tiene y cuáles solicita:

- [ ] **Estados Financieros** (Balance General + Estado de Resultados) — últimos 2-3 años
- [ ] **Flujo de Caja** (últimos 12 meses, si existe)
- [ ] **Declaraciones fiscales** (último año)
- [ ] **Organigrama** (si existe)
- [ ] **Catálogo de productos/servicios** con precios
- [ ] **Lista de empleados** por área/rol (sin datos personales sensibles)
- [ ] **Manuales de procesos o procedimientos** (si existen)
- [ ] **Contratos con clientes clave** (opcional, anonimizados)
- [ ] **Reportes de ventas** (últimos 12 meses)
- [ ] **Presupuesto anual** (si existe)
- [ ] **Plan estratégico** (si existe)

### 12.3 Guion de Cierre

```
"Muchas gracias por su tiempo, [nombre]. Ha sido muy valioso entender
cómo funciona su negocio. Los siguientes pasos son:

1. Voy a procesar toda la información que me compartió
2. En [3-5 días hábiles] le presentaré un diagnóstico completo
3. Luego trabajaremos juntos en un plan de acción

Para eso, necesitaré que me comparta estos documentos: [lista corta].
¿Le parece bien?

¿Tiene alguna pregunta antes de cerrar?"
```

---

## 13. Árboles de Decisión

### 13.1 Árbol General de Conducción de la Entrevista

```
INICIO ENTREVISTA
│
├── ¿Cliente se muestra abierto?
│   ├── Sí → Seguir flujo normal (Bloque 0 → 1 → 2 → ...)
│   └── No → Invertir más tiempo en rapport, preguntas más ligeras primero
│
├── ¿Cliente menciona crisis o urgencia?
│   ├── Sí → Saltar a Bloque 6 (Riesgos), luego Bloque 7 (Objetivos)
│   │        → Preguntar: "¿Qué tan urgente diría que es?"
│   │        → Volver a bloques 2-5 después si hay tiempo
│   └── No → Flujo normal
│
├── ¿Cliente da respuestas muy breves?
│   ├── Sí → Usar técnica de profundización:
│   │        → "Cuénteme más sobre..."
│   │        → "¿Qué quiere decir exactamente con...?"
│   │        → "¿Puede darme un ejemplo?"
│   └── No → Continuar
│
├── ¿Cliente se desvía del tema?
│   ├── Leve → Dejar 1-2 min, luego redirigir: "Entiendo, y hablando de [tema]..."
│   └── Severo → Redirigir directamente: "Retomando el punto anterior..."
│
├── ¿Información es contradictoria?
│   ├── Sí → Registrar ambas versiones, preguntar: "Noté que antes mencionó X y ahora Y,
│   │        ¿podría ayudarme a entender mejor?"
│   └── No → Continuar
│
└── ¿Se acaba el tiempo?
    ├── Sí → Priorizar preguntas obligatorias restantes
    │        → Agendar sesión complementaria si es necesario
    └── No → Continuar con opcionales
```

### 13.2 Árbol de Decisión: Profundizar o Siguiente Pregunta

```
Respuesta del cliente
│
├── ¿La respuesta es superficial (Nivel 1)?
│   ├── ¿El tema es crítico para el diagnóstico?
│   │   ├── Sí → Profundizar (Nivel 2 o 3): "¿Cómo funciona eso exactamente?"
│   │   └── No → Registrar y pasar a siguiente pregunta
│
├── ¿La respuesta revela un problema potencial?
│   ├── ¿El problema es mencionado con emoción (frustración, preocupación)?
│   │   ├── Sí → Profundizar: "Eso suena importante, cuénteme más"
│   │   └── No → Registrar como hallazgo, continuar
│
├── ¿La respuesta contradice información anterior?
│   ├── Sí → Preguntar: "Ayúdeme a entender mejor... antes mencionó X y ahora Y"
│   └── No → Continuar
│
└── ¿La respuesta es completa y clara?
    ├── Sí → Siguiente pregunta
    └── No → Reformular: "Déjeme preguntarle de otra forma..."
```

### 13.3 Árbol de Decisión: Gestión del Tiempo

```
Tiempo transcurrido
│
├── < 50% del tiempo → Seguir ritmo normal
│
├── 50-75% del tiempo → ¿Preguntas obligatorias completas?
│   ├── Sí → Continuar con opcionales, priorizar por relevancia
│   └── No → Acelerar: omitir opcionales, ir a obligatorias restantes
│
└── > 75% del tiempo
    ├── ¿Faltan bloques completos?
    │   ├── Sí → Priorizar el bloque más relevante según arquetipo
    │   │        → Si aplica: agendar sesión complementaria
    │   └── No → Cerrar ordenadamente
    └── ¿Faltan preguntas sueltas?
        ├── Críticas → Hacerlas rápido
        └── Opcionales → Registrar como "información faltante"
```

---

## 14. Señales de Alerta

### 14.1 Catálogo de Alertas

| Código | Alerta | Bloque | Severidad | Acción Inmediata |
|---|---|---|---|---|
| AL-PER-01 | Inconsistencia empleados vs facturación | Bloque 1 | Media | Solicitar aclaración |
| AL-PER-02 | Año de fundación no coincide con madurez aparente | Bloque 1 | Baja | Verificar con documentos |
| AL-MN-01 | Commoditización (sin diferenciación clara) | Bloque 2 | Alta | Profundizar en propuesta de valor |
| AL-MN-02 | Propuesta de valor difusa | Bloque 2 | Alta | Usar JTBD para aclarar |
| AL-MN-03 | Dependencia de una sola fuente de ingreso | Bloque 2 | Alta | Evaluar diversificación |
| AL-MN-04 | Cliente no sabe quién es su cliente ideal | Bloque 2 | Alta | Sugerir segmentación |
| AL-FI-01 | Ciclo de caja (CCC) largo (>60 días) | Bloque 3 | Alta | Profundizar en políticas de cobro/pago |
| AL-FI-02 | Nómina > 40% de ingresos | Bloque 3 | Alta | Revisar estructura de costos |
| AL-FI-03 | Decrecimiento de ingresos | Bloque 3 | Alta | Investigar causas comerciales |
| AL-FI-04 | Crecimiento vegetativo (0-5%) | Bloque 3 | Media | Evaluar competitividad |
| AL-FI-05 | Datos financieros insuficientes | Bloque 3 | Alta | Solicitar documentos |
| AL-FI-06 | Margen bajo vs industria | Bloque 3 | Alta | Analizar estructura de costos |
| AL-OP-01 | Falta de estandarización de procesos | Bloque 4 | Media | Evaluar si afecta calidad/eficiencia |
| AL-OP-02 | Software subutilizado | Bloque 4 | Media | Evaluar capacitación o cambio |
| AL-OP-03 | Digitalización nula | Bloque 4 | Alta | Evaluar impacto en eficiencia |
| AL-OP-04 | Cuello de botella no identificado | Bloque 4 | Alta | Hacer mapeo de flujo de valor |
| AL-OP-05 | Dependencia de proveedor único | Bloque 4 | Alta | Evaluar plan de contingencia |
| AL-OR-01 | Roles y responsabilidades difusos | Bloque 5 | Media | Sugerir clarificación de roles |
| AL-OR-02 | Centralización delegable | Bloque 5 | Media | Identificar candidatos a delegación |
| AL-OR-03 | Dependencia crítica del fundador | Bloque 5 | Alta | Plan de sucesión urgente |
| AL-OR-04 | Rotación alta (>15%) | Bloque 5 | Alta | Investigar causas con encuesta de clima |
| AL-OR-05 | Conflictos internos evidentes | Bloque 5 | Alta | Sugerir mediación o intervención |
| AL-RI-01 | Percepción de riesgo baja | Bloque 6 | Media | El cliente puede estar subestimando riesgos |
| AL-RI-02 | Alta concentración de clientes (>30% en 1) | Bloque 6 | Alta | Evaluar dependencia |
| AL-RI-03 | Riesgo externo significativo | Bloque 6 | Alta | Incluir en matriz de riesgos |
| AL-RI-04 | Sin seguros ni protección | Bloque 6 | Alta | Recomendar evaluación de seguros |
| AL-GEN-01 | Cliente evita temas financieros | General | Media | Registrar como posible opacidad |
| AL-GEN-02 | Cliente parece desinformado de su propio negocio | General | Alta | Validar con otras fuentes |
| AL-GEN-03 | Cliente en modo "urgencia/desesperación" | General | Alta | Priorizar intervención rápida |

### 14.2 Reglas de Activación de Alertas

1. **Alerta inmediata**: Si la alerta es de severidad **Alta** y el cliente la menciona con emoción negativa, interrumpir el bloque actual y profundizar.
2. **Registro obligatorio**: Toda alerta debe registrarse en `brief_empresa.md` → sección `alertas_tempranas`.
3. **No alarmar al cliente**: Las alertas son para el sistema de diagnóstico, no se comparten en bruto con el cliente durante la entrevista.
4. **Acumulación**: Si se detectan 3+ alertas Altas, el Interview_Orchestrator debe notificar al Master_Diagnosis_Orchestrator para considerar modo "diagnóstico acelerado".

---

## 15. Documentación Recomendada

### 15.1 Documentación Financiera

| Documento | Prioridad | Formato | Uso en Diagnóstico |
|---|---|---|---|
| Balance General (2-3 años) | **Crítica** | Excel/PDF | E4 — Análisis de solvencia y liquidez |
| Estado de Resultados (2-3 años) | **Crítica** | Excel/PDF | E4 — Análisis de rentabilidad |
| Flujo de Efectivo (12 meses) | **Alta** | Excel/PDF | E4 — Ciclo de caja |
| Antigüedad de Cartera (AR Aging) | **Alta** | Excel/CSV | E4 — Calidad de cobranza |
| Antigüedad de Proveedores (AP Aging) | **Alta** | Excel/CSV | E4 — Gestión de pagos |
| Declaraciones Fiscales | Media | PDF | Verificación de ingresos |
| Presupuesto Anual | Media | Excel | E4 — Planificación financiera |
| Estados de Cuenta Bancarios (6 meses) | Baja | PDF/CSV | Validación de flujo |

### 15.2 Documentación Comercial

| Documento | Prioridad | Formato | Uso en Diagnóstico |
|---|---|---|---|
| Catálogo de productos/servicios | **Alta** | PDF/Excel | E3 — Modelo de negocio |
| Lista de precios | **Alta** | Excel | E3 — Fuentes de ingreso |
| Reporte de ventas (12 meses) | **Alta** | Excel/CSV | E3 — Estacionalidad, tendencias |
| Base de clientes (anonimizada) | Media | Excel/CSV | E3 — Segmentación |
| Contratos tipo con clientes | Media | PDF | E3 — Relaciones contractuales |
| Material de marketing/publicidad | Baja | PDF/URL | E3 — Canales y comunicación |

### 15.3 Documentación Operativa

| Documento | Prioridad | Formato | Uso en Diagnóstico |
|---|---|---|---|
| Diagrama de procesos / flujogramas | **Alta** | PDF/Imagen | E5 — Mapeo de procesos |
| Manuales de procedimientos | **Alta** | PDF/Word | E5 — Estandarización |
| KPIs operativos (si existen) | Media | Excel | E5 — Medición de desempeño |
| Layout de instalaciones | Baja | PDF/Imagen | E5 — Flujo físico |
| Registros de calidad/reclamos | Media | Excel | E5 — Control de calidad |

### 15.4 Documentación Organizacional

| Documento | Prioridad | Formato | Uso en Diagnóstico |
|---|---|---|---|
| Organigrama | **Alta** | PDF/Imagen | E6 — Estructural |
| Descripción de puestos | Media | PDF/Word | E6 — Roles |
| Nómina o plantilla (anonimizada) | Media | Excel | E6 — Estructura de costos de personal |
| Evaluaciones de desempeño (si existen) | Baja | PDF/Excel | E6 — Gestión del talento |
| Reglamento interior de trabajo | Baja | PDF | E6 — Políticas |

### 15.5 Documentación Estratégica

| Documento | Prioridad | Formato | Uso en Diagnóstico |
|---|---|---|---|
| Plan estratégico (si existe) | **Alta** | PDF/Word | E3/E8 — Alineación estratégica |
| Plan de marketing | Media | PDF/Word | E3 — Estrategia comercial |
| Estudios de mercado | Media | PDF | E3 — Contexto competitivo |
| Análisis FODA previo | Media | PDF | E8 — Comparativa |

---

## 16. Output Final: Brief_Empresa.md

### 16.1 Estructura del Archivo

```markdown
# Brief_Empresa — {Nombre de la Empresa}

> Generado: {YYYY-MM-DD HH:MM}
> Versión: v1.0
> Agente: Interview_Orchestrator
> Modalidad: {Presencial | Videollamada | Asíncrona | Híbrida}
> Duración: {minutos}
> Entrevistado: {Nombre}, {Cargo}

---

## 1. Datos Generales

| Campo | Valor |
|---|---|
| Razón Social |  |
| Nombre Comercial |  |
| Año de Fundación |  |
| Industria (NAICS/CIIU) |  |
| Número de Empleados | [TC: X, TP: X] |
| Facturación Anual (último año) | $ |
| Facturación Anual (año anterior) | $ |
| Mercado Geográfico |  |
| Principal Producto/Servicio |  |
| Tipo de Empresa | {Startup / Familiar / Consolidada / Crisis / Profesionalizada / Individual} |
| Ubicación |  |

---

## 2. Resumen de la Entrevista

{2-3 párrafos describiendo la impresión general, el contexto del cliente,
los temas más relevantes que surgieron y el estado de ánimo del entrevistado}

---

## 3. Modelo de Negocio (Business Model Canvas)

| Bloque | Descripción |
|---|---|
| Propuesta de Valor |  |
| Segmentos de Cliente |  |
| Canales |  |
| Relaciones Cliente |  |
| Fuentes de Ingreso |  |
| Recursos Clave |  |
| Actividades Clave |  |
| Socios Clave |  |
| Estructura de Costos |  |

---

## 4. Situación Financiera

| Indicador | Valor | Benchmark Industria | Alerta |
|---|---|---|---|
| Ingresos Último Año | $ | $ |  |
| Crecimiento de Ingresos | % | % |  |
| Margen Neto Estimado | % | % |  |
| Días de Cuenta por Cobrar | días | días |  |
| Días de Cuenta por Pagar | días | días |  |
| Días de Inventario | días | días |  |
| Ciclo de Conversión de Efectivo | días | días |  |
| Nómina / Ingresos | % |  |  |
| Deuda Total | $ |  |  |
| Estacionalidad | {Meses altos/bajos} |  |  |

**Notas Financieras Adicionales:**
- {Observaciones cualitativas sobre finanzas}

---

## 5. Operaciones

| Aspecto | Descripción |
|---|---|
| Procesos Clave (Top 3) |  |
| Lead Time Promedio |  |
| Nivel de Estandarización | {Alto / Medio / Bajo / Nulo} |
| Software / Sistemas |  |
| Cuello de Botella Principal |  |
| Control de Calidad |  |
| Dependencia de Proveedores |  |
| Capacidad Utilizada Estimada | % |

---

## 6. Organización

| Aspecto | Descripción |
|---|---|
| Estructura | {Funcional / Plana / Matricial / Informal / No definida} |
| Nivel de Delegación | {Alta / Media / Baja / Nula (centralizada)} |
| Cultura | {descripción cualitativa} |
| Rotación de Personal | % |
| Brecha de Talento |  |
| Estilo de Liderazgo |  |
| Conflictos Internos |  |

---

## 7. Riesgos Identificados

| Riesgo | Categoría | Prob. (1-5) | Impacto (1-5) | Nivel (P×I) |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## 8. Objetivos y Metas del Cliente

| Prioridad | Objetivo | Categoría | Horizonte |
|---|---|---|---|
| 1 |  |  | CP / MP / LP |
| 2 |  |  | CP / MP / LP |
| 3 |  |  | CP / MP / LP |

**Visión a 3 años:**
{Texto del cliente}

**Disposición al cambio:**
{Alta / Media / Baja — con justificación}

---

## 9. Alertas Tempranas

| Código | Descripción | Severidad | Estado |
|---|---|---|---|
| AL-XX |  | {Alta/Media/Baja} | {Activa / Pendiente de verificación} |
| AL-XX |  |  |  |

---

## 10. Documentación Obtenida

- [ ] Estados Financieros ({años})
- [ ] Flujo de Caja
- [ ] Organigrama
- [ ] Catálogo de productos
- [ ] Manuales de procesos
- [ ] KPIs operativos
- [ ] Plan estratégico
- [ ] Otros: {especificar}

---

## 11. Documentación Pendiente (a Solicitar)

- [ ] {Documento} — {prioridad} — {fecha de compromiso}

---

## 12. Notas del Analista

{Impresiones, observaciones, intuiciones y cualquier información contextual
que no encaje en las secciones anteriores. Prefijar con "IMPRESIÓN:" cuando
sea una interpretación subjetiva del analista.}

---

*Fin del Brief — {Nombre de la Empresa}*
```

### 16.2 Reglas de Generación del Brief

| Regla | Descripción |
|---|---|
| **Completitud** | Todos los campos deben rellenarse. Si no hay dato, usar "No disponible" o "No aplica" |
| **Trazabilidad** | Cada respuesta debe poder asociarse a su pregunta correspondiente |
| **Objetividad** | Separar hechos (datos textuales) de impresiones (prefijadas con "IMPRESIÓN:") |
| **Alertas** | Todas las alertas detectadas deben listarse en la sección 9 |
| **Versiones** | El Brief se genera como v1.0. Si se obtiene más info después, se incrementa versión |
| **Confidencialidad** | No incluir datos sensibles no autorizados (RFC, cuentas bancarias, etc.) |

### 16.3 Validación del Brief

Antes de entregar el Brief a los agentes de diagnóstico, el Interview_Orchestrator debe verificar:

- [ ] Los 12 bloques están completos (sin secciones vacías)
- [ ] Los datos cuantitativos tienen unidades y período especificado
- [ ] Las alertas tienen código, descripción y severidad
- [ ] Los objetivos están categorizados y priorizados
- [ ] La documentación obtenida/pendiente está claramente listada
- [ ] No hay información contradictoria sin marcar
- [ ] El tipo de empresa (arquetipo) está identificado

---

*Fin del documento — Discovery_Interview.md v1.0*
