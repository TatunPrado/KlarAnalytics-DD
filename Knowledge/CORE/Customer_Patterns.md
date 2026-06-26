# Customer_Patterns.md

**File:** Customer_Patterns.md
**Description:** Patrones de experiencia del cliente, satisfacción y fidelización para PyMEs — detección temprana de problemas en churn, retención, NPS, reclamos, fidelización, customer success, experiencia de cliente, LTV, segmentación y dependencia de clientes.
**Total Patterns:** 91 (CUS-001 a CUS-091)
**Categories:** 10
**Version:** 1.0

---

## Summary Table

| Category | Pattern IDs | Count | Description |
|---|---|---|---|
| Churn | CUS-001 a CUS-009 | 9 | Pérdida sistemática de clientes |
| Retención | CUS-010 a CUS-019 | 10 | Dificultad para mantener clientes activos |
| NPS | CUS-020 a CUS-027 | 8 | Net Promoter Score bajo o mal gestionado |
| Reclamos | CUS-028 a CUS-036 | 9 | Gestión deficiente de quejas y reclamos |
| Fidelización | CUS-037 a CUS-045 | 9 | Programas y prácticas de lealtad débiles |
| Customer Success | CUS-046 a CUS-055 | 10 | Procesos de éxito del cliente inexistentes o ineficaces |
| Customer Experience | CUS-056 a CUS-064 | 9 | Experiencia del cliente fragmentada o deficiente |
| Lifetime Value | CUS-065 a CUS-073 | 9 | LTV bajo, decreciente o mal gestionado |
| Segmentación | CUS-074 a CUS-082 | 9 | Segmentación de clientes incorrecta o inexistente |
| Dependencia de clientes | CUS-083 a CUS-091 | 9 | Concentración excesiva en pocos clientes |

---

# Patrones de Customer

## Churn

### CUS-001
**Pattern_Name:** Churn Creciente Sin Causa Identificada
**Category:** Churn
**Description:** La tasa de cancelación de clientes aumenta trimestre a trimestre sin que la empresa identifique las causas, poniendo en riesgo la base de ingresos recurrentes.
**Observable_Symptoms:** Más clientes se van cada mes sin explicación clara; el equipo dice "los clientes se van pero no sabemos por qué"; la tasa de churn sube y no hay plan de contención; las encuestas de salida no existen o no se analizan; los clientes que se van no dan razones específicas.
**Early_Warning_Signals:** Churn mensual > 5% y creciendo; tendencia de churn alcista por 3+ meses consecutivos; encuestas de salida sin completar; % de churn sin causa identificada > 40%; equipo no puede explicar el churn.
**Typical_Causes:** Falta de medición de causas de churn; ausencia de encuestas de salida; datos de clientes no analizados; cultura de "los clientes se van y llegan otros"; falta de proceso de análisis de churn.
**Business_Impact:** Ingresos recurrentes en declive; necesidad constante de adquirir clientes solo para mantener nivel; CAC alto por fuga; inestabilidad en la base de clientes; crecimiento comprometido.
**Metrics_To_Check:** Tasa de churn mensual; tendencia de churn; % de churn con causa identificada; ingresos perdidos por churn; costo de reemplazo de clientes perdidos.
**Diagnostic_Questions:** ¿Sabemos por qué se van los clientes? ¿Tenemos encuestas de salida? ¿Analizamos las causas de churn? ¿La tasa de churn está empeorando? ¿Podemos predecir qué clientes se irán?
**Recommended_Actions:** Implementar encuestas de salida; analizar causas de churn por segmento; crear dashboard de churn con causas; establecer reuniones mensuales de análisis de churn; desarrollar plan de contención para causas principales.
**Severity_Level:** Critical
**Related_Patterns:** CUS-002, CUS-005, CUS-008, CUS-010, CUS-013, CUS-044

### CUS-002
**Pattern_Name:** Churn en Clientes Nuevos (Primeros 90 Días)
**Category:** Churn
**Description:** Una proporción significativa de clientes nuevos cancela dentro de los primeros 90 días, indicando problemas de onboarding, expectativas incorrectas o mala calidad en la primera experiencia.
**Observable_Symptoms:** Clientes nuevos se van antes del tercer mes; el proceso de onboarding no está definido; clientes reportan "no era lo que esperaba"; la primera experiencia no cumple expectativas; la tasa de activación es baja.
**Early_Warning_Signals:** Churn en primeros 90 días > 15%; % de clientes que completan onboarding < 50%; NPS post-onboarding bajo; clientes nuevos no usan el producto/servicio; primer reclamo dentro de los primeros 30 días.
**Typical_Causes:** Onboarding deficiente o inexistente; expectativas creadas por ventas no realistas; producto/servicio no cumple lo prometido; falta de acompañamiento inicial; cliente no ve valor rápidamente.
**Business_Impact:** CAC desperdiciado en clientes que no se quedan; crecimiento ilusorio (clientes entran y salen); equipo comercial frustrado; inversión en adquisición no recuperada; base de clientes no se consolida.
**Metrics_To_Check:** Churn en primeros 90 días; tasa de activación; % de clientes que completan onboarding; NPS post-onboarding; tiempo hasta primer valor (time-to-value).
**Diagnostic_Questions:** ¿Cómo es la experiencia del cliente en los primeros 90 días? ¿El onboarding está estructurado? ¿Las expectativas creadas por ventas son realistas? ¿El cliente ve valor rápidamente? ¿Hay acompañamiento en la primera etapa?
**Recommended_Actions:** Diseñar programa de onboarding estructurado; alinear promesas de ventas con realidad; establecer hitos de activación en primeros 30-60-90 días; asignar customer success manager a clientes nuevos; medir time-to-value.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-003, CUS-010, CUS-046, CUS-047, CUS-054

### CUS-003
**Pattern_Name:** Churn por Falta de Adopción del Producto
**Category:** Churn
**Description:** Los clientes cancelan porque no utilizan el producto o servicio de manera consistente, no logran integrarlo en su operación y no perciben el valor por el que pagaron.
**Observable_Symptoms:** Clientes que compran pero no usan; baja frecuencia de uso; el producto/servicio no se integra en la operación del cliente; clientes reportan "no le sacamos provecho"; el equipo de soporte no ve a estos clientes.
**Early_Warning_Signals:** % de clientes con uso < 1 vez por semana > 30%; clientes sin login en > 30 días; baja adopción de funcionalidades clave; % de clientes que no asisten a capacitaciones; NPS bajo en clientes con baja adopción.
**Typical_Causes:** Producto complejo sin soporte de adopción; falta de entrenamiento al cliente; onboarding que no asegura uso; cliente no entiende el valor completo; falta de customer success proactivo.
**Business_Impact:** Clientes pagan pero no ven valor; eventual churn por falta de adopción; oportunidad de upselling perdida; cliente no se vuelve promotor; LTV muy por debajo del potencial.
**Metrics_To_Check:** Frecuencia de uso; % de funcionalidades adoptadas; clientes inactivos (>30 días); correlación adopción-churn; NPS por nivel de adopción.
**Diagnostic_Questions:** ¿Los clientes usan activamente el producto? ¿Con qué frecuencia? ¿Han adoptado las funcionalidades clave? ¿Hay clientes que pagan pero no usan? ¿El onboarding asegura adopción?
**Recommended_Actions:** Implementar programa de adopción proactiva; medir frecuencia de uso y alertar sobre baja adopción; ofrecer entrenamiento y capacitación; identificar funcionalidades infrautilizadas y promoverlas; asignar CSM a clientes con baja adopción.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-002, CUS-046, CUS-047, CUS-054, CUS-055

### CUS-004
**Pattern_Name:** Churn por Precio sin Análisis de Valor Percibido
**Category:** Churn
**Description:** Clientes cancelan argumentando "precio alto", pero la empresa no investiga si el problema es realmente el precio o la percepción de valor, perdiendo la oportunidad de retener.
**Observable_Symptoms:** Clientes citan precio como razón de cancelación; la empresa baja precios para retener sin evaluar otras opciones; no se analiza si el cliente percibe el valor; descuentos reactivos para evitar churn; margen se erosiona.
**Early_Warning_Signals:** % de churn por precio > 30%; descuentos para retener aumentan; precio vs valor percibido no medido; cliente no usa el producto antes de cancelar; clientes que pagan menos tienen mismo churn que los que pagan más.
**Typical_Causes:** Valor percibido no comunicado consistentemente; producto no entrega valor suficiente; precio mal posicionado vs competidores; falta de propuesta de valor clara; cliente no entiende el ROI.
**Business_Impact:** Erosión de margen por descuentos; cliente se va de todas formas; percepción de precio injusto; descuentos se convierten en expectativa; competitividad dañada.
**Metrics_To_Check:** % de churn por precio; descuentos para retener vs churn evitado; valor percibido medido (encuestas); ROI percibido por el cliente; precio relativo vs competidores.
**Diagnostic_Questions:** ¿El precio es realmente la causa o es la percepción de valor? ¿Hemos investigado qué valor percibe el cliente? ¿El cliente entiende el ROI? ¿Comunicamos el valor consistentemente? ¿Ofrecemos descuento sin resolver la causa raíz?
**Recommended_Actions:** Investigar valor percibido (encuestas, entrevistas); comunicar valor y ROI consistentemente; fortalecer propuesta de valor; considerar ajuste de precio solo si valor está demostrado; crear paquetes de valor que justifiquen precio.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-020, CUS-044, CUS-054, CUS-065

### CUS-005
**Pattern_Name:** Churn Sin Señales Tempranas Detectadas
**Category:** Churn
**Description:** Los clientes cancelan sin que la empresa haya detectado señales de alerta previas, indicando que no hay monitoreo proactivo de la salud del cliente.
**Observable_Symptoms:** La cancelación de un cliente es una "sorpresa"; no hay indicadores de salud del cliente; el equipo no ve venir el churn; clientes que parecían contentos se van; no hay alertas de riesgo.
**Early_Warning_Signals:** % de churn sorpresa > 50% del total; sin dashboard de salud del cliente; sin alertas de comportamiento de riesgo; equipo comercial no identificaba riesgo en clientes perdidos; encuestas de satisfacción no se usan para predecir.
**Typical_Causes:** Falta de customer health score; datos de cliente no integrados; ausencia de monitoreo proactivo; cultura reactiva; CSM no implementado o sin herramientas.
**Business_Impact:** Imposibilidad de retener proactivamente; clientes se pierden que podrían salvarse; ingresos recurrentes en riesgo; inversión en retención no dirigida; LTV menor al potencial.
**Metrics_To_Check:** % de churn sorpresa; customer health score implementado; precisión de predicción de churn; % de clientes en riesgo identificados antes de cancelar; tiempo entre detección y cancelación.
**Diagnostic_Questions:** ¿Detectamos señales de alerta antes de que un cliente cancele? ¿Tenemos sistema de health score? ¿Las cancelaciones son sorpresas? ¿Monitoreamos comportamiento proactivamente? ¿Podemos predecir qué clientes están en riesgo?
**Recommended_Actions:** Implementar customer health score (uso, satisfacción, engagement, reclamos); crear alertas automáticas de comportamiento de riesgo; monitorear clientes semanalmente; contactar clientes en riesgo proactivamente; medir precisión predictiva.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-013, CUS-020, CUS-046, CUS-056

### CUS-006
**Pattern_Name:** Churn Concentrado en Segmento Específico
**Category:** Churn
**Description:** La tasa de churn es significativamente más alta en un segmento específico de clientes (por industria, tamaño, producto o canal de adquisición), indicando un problema estructural no resuelto.
**Observable_Symptoms:** Un grupo de clientes consistentemente cancela más que otros; el churn no es uniforme; se identifica un patrón en los clientes que se van; el equipo sabe que "estos clientes no se quedan" pero no se actúa; segmento específico tiene churn sistemático.
**Early_Warning_Signals:** Diferencia de churn entre segmentos > 2x; segmento específico con churn > 10% mensual; patrón de churn por industria, tamaño o canal sin acción; % de clientes del segmento problemático creciente; ingresos del segmento en declive.
**Typical_Causes:** Producto/servicio no adecuado para ese segmento; proceso de ventas califica mal; segmento tiene características que generan insatisfacción; expectativas del segmento no alineadas con la propuesta; el segmento no es rentable naturalmente.
**Business_Impact:** Pérdida sistemática de un segmento; recursos invertidos en adquirir clientes que se irán; rentabilidad del segmento negativa; distorsión de métricas generales; oportunidad de enfocarse en segmentos mejores.
**Metrics_To_Check:** Tasa de churn por segmento; LTV por segmento; rentabilidad por segmento; % de clientes del segmento problemático; tendencia de churn por segmento.
**Diagnostic_Questions:** ¿El churn es uniforme o se concentra en algún segmento? ¿Qué segmento tiene peor churn? ¿Por qué? ¿El producto es adecuado para ese segmento? ¿Deberíamos dejar de vender a ese segmento?
**Recommended_Actions:** Analizar churn por segmento sistemáticamente; identificar causas específicas del segmento problemático; ajustar producto o propuesta para ese segmento; considerar dejar de vender a segmentos no rentables; mejorar calificación para evitar segmentos problemáticos.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-010, CUS-022, CUS-065, CUS-074

### CUS-007
**Pattern_Name:** Churn Post-Contrato (Fin de Período)
**Category:** Churn
**Description:** La mayoría de las cancelaciones ocurren al finalizar el período contractual (12 meses, 24 meses), indicando que el cliente no ve suficiente valor para renovar.
**Observable_Symptoms:** Renovaciones no automáticas; cliente evalúa cada renovación; alta concentración de churn en fechas de renovación; equipo comercial tiene que "re-vender" la renovación; cliente negocia precio en cada renovación.
**Early_Warning_Signals:** % de churn en renovación > 30%; tasa de renovación < 70%; clientes no renuevan automáticamente; % de clientes que negocian precio para renovar > 40%; satisfacción baja en clientes próximos a renovar.
**Typical_Causes:** Valor no demostrado durante el contrato; falta de engagement post-venta; cliente no percibe mejora continua; producto/servicio estancado; relación transaccional no de socio.
**Business_Impact:** Pérdida de clientes en renovación; necesidad de "re-vender" cada período; ingresos recurrentes no estables; LTV limitado a un período; crecimiento basado solo en nuevos clientes.
**Metrics_To_Check:** Tasa de renovación; % de churn en renovación; NPS de clientes próximos a renovar; % de renovaciones automáticas vs negociadas; tiempo dedicado a renovaciones.
**Diagnostic_Questions:** ¿Los clientes renuevan automáticamente? ¿Hay que "re-vender" la renovación? ¿El cliente ve valor incremental? ¿El engagement es consistente durante el contrato? ¿Hay comunicación de valor continua?
**Recommended_Actions:** Demostrar valor de manera continua no solo al inicio y final; implementar renovaciones automáticas con aviso previo; crear programa de valor incremental durante el contrato; contactar clientes 90 días antes de renovación; medir satisfacción pre-renovación.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-010, CUS-018, CUS-044, CUS-046

### CUS-008
**Pattern_Name:** Churn por Mala Atención al Cliente
**Category:** Churn
**Description:** Clientes cancelan debido a experiencias negativas con el servicio de atención al cliente (demoras, maltrato, no resolución), un problema recurrente que la empresa no aborda.
**Observable_Symptoms:** Reclamos sobre atención al cliente como causa de cancelación; tiempos de respuesta largos; clientes reportan "no resuelven nada"; el equipo de atención está desbordado o desmotivado; quejas recurrentes sobre el mismo tema.
**Early_Warning_Signals:** % de churn por atención al cliente > 15%; tiempo de respuesta > 24h; tasa de resolución en primer contacto < 50%; CSAT de atención < 3/5; reclamos recurrentes sobre atención.
**Typical_Causes:** Falta de inversión en atención al cliente; equipo no capacitado; procesos de atención ineficientes; cultura de "el cliente molesta"; herramientas de soporte inadecuadas.
**Business_Impact:** Churn evitable por atención deficiente; clientes insatisfechos se van; mala reputación (boca a boca negativo); NPS bajo; competidores con mejor atención ganan clientes.
**Metrics_To_Check:** % de churn por atención; tiempo de respuesta; tasa de resolución en primer contacto; CSAT de atención; reclamos recurrentes; NPS de clientes que usan soporte.
**Diagnostic_Questions:** ¿La atención al cliente es una causa de churn? ¿Los clientes están satisfechos con el soporte? ¿Los tiempos de respuesta son adecuados? ¿Los reclamos se resuelven en el primer contacto? ¿El equipo de atención está capacitado?
**Recommended_Actions:** Mejorar procesos de atención al cliente; reducir tiempos de respuesta; capacitar al equipo en servicio al cliente; implementar herramientas de soporte (tickets, chat, FAQ); medir satisfacción post-contacto; crear cultura de servicio.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-009, CUS-028, CUS-029, CUS-056

### CUS-009
**Pattern_Name:** Churn Silencioso (Clientes que Dejan de Usar)
**Category:** Churn
**Description:** Clientes que dejan de usar el producto o servicio pero no cancelan formalmente, generando una ilusión de clientes activos que en realidad no generan ingresos recurrentes o valor.
**Observable_Symptoms:** Clientes que pagan pero no usan; usuarios sin actividad por meses; ingresos de clientes "zombies"; base de clientes inflada con inactivos; el equipo reporta clientes que "existen pero no compran".
**Early_Warning_Signals:** % de clientes inactivos > 20%; clientes sin actividad en > 90 días; ingresos de clientes inactivos que pagan pero no usan > 10% del total; tendencia de inactividad creciente; clientes que no responden a comunicaciones.
**Typical_Causes:** Falta de monitoreo de actividad; contratos que no se cancelan pero tampoco se usan; proceso de baja difícil; cliente olvida que tiene el servicio; facturación automática sin control.
**Business_Impact:** Base de clientes sobreestimada; ingresos futuros inseguros (cancelarán eventualmente); recursos desperdiciados en clientes inactivos; métricas de retención engañosas; LTV sobreestimado.
**Metrics_To_Check:** % de clientes inactivos; días de inactividad promedio; % de ingresos de clientes inactivos; tendencia de inactividad; % de clientes inactivos que eventualmente cancelan.
**Diagnostic_Questions:** ¿Tenemos clientes que pagan pero no usan? ¿Monitoreamos la actividad de clientes? ¿La base de clientes incluye inactivos? ¿Sabemos cuándo un cliente deja de usar? ¿Hay plan de reactivación?
**Recommended_Actions:** Monitorear actividad de clientes semanalmente; segmentar clientes por nivel de actividad; crear campañas de reactivación para inactivos; facilitar cancelación para limpiar base; contactar clientes inactivos proactivamente.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-003, CUS-005, CUS-046, CUS-084


## Retención

### CUS-010
**Pattern_Name:** Tasa de Retención por Debajo del Benchmark
**Category:** Retención
**Description:** La tasa de retención de clientes está significativamente por debajo del benchmark del sector, indicando problemas estructurales en la propuesta de valor, la experiencia o el producto.
**Observable_Symptoms:** Clientes que no renuevan o recompran; la comparación con el sector muestra retención inferior; la empresa no sabe cuál es el benchmark de su industria; clientes se van a competidores; la retención no mejora con el tiempo.
**Early_Warning_Signals:** Tasa de retención anual < 70% (o < benchmark sectorial); tendencia de retención plana o decreciente; % de clientes que recompra < 40%; comparación con competidores desfavorable; retención por debajo del punto de equilibrio del negocio.
**Typical_Causes:** Propuesta de valor no diferencial; experiencia del cliente deficiente; producto/servicio no evoluciona; competidores ofrecen mejor valor; falta de estrategia de retención.
**Business_Impact:** Clientes se fugan antes de recuperar CAC; LTV bajo; necesidad constante de adquirir; crecimiento lento; inestabilidad en ingresos.
**Metrics_To_Check:** Tasa de retención (mensual, anual); benchmark del sector; % de recompra; LTV; tendencia de retención; retención por segmento.
**Diagnostic_Questions:** ¿Cuál es nuestra tasa de retención? ¿Cómo nos comparamos con el sector? ¿Los clientes recompran? ¿La retención mejora o empeora? ¿Tenemos una estrategia de retención definida?
**Recommended_Actions:** Medir tasa de retención consistentemente; comparar con benchmark del sector; identificar causas principales de baja retención; implementar programa de retención; mejorar propuesta de valor y experiencia del cliente.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-007, CUS-013, CUS-020, CUS-065

### CUS-011
**Pattern_Name:** Retención No Medida por Segmento
**Category:** Retención
**Description:** La empresa mide la retención promedio pero no desglosa por segmento, ocultando que algunos segmentos tienen alta retención y otros muy baja, impidiendo acciones focalizadas.
**Observable_Symptoms:** La retención se reporta como un número único; no se sabe qué segmento retiene mejor; segmentos con baja retención se ocultan en el promedio; decisiones de mejora genéricas sin foco; recursos de retención mal asignados.
**Early_Warning_Signals:** Retención solo medida a nivel global; sin retención por segmento; diferencia de retención entre segmentos > 20 puntos; % de clientes del segmento de baja retención significativo; sin acciones diferenciadas por segmento.
**Typical_Causes:** Falta de segmentación en análisis; datos no desglosados; cultura de "un número para todos"; desconocimiento de variabilidad; herramientas analíticas limitadas.
**Business_Impact:** Segmentos con baja retención no identificados; recursos de retención mal dirigidos; promedio engañoso esconde problemas; oportunidades de mejora perdidas; LTV no optimizado por segmento.
**Metrics_To_Check:** Retención por segmento; diferencia entre segmentos; % de clientes en segmentos de baja retención; tendencia de retención por segmento; recursos asignados por segmento.
**Diagnostic_Questions:** ¿Medimos retención por segmento? ¿Hay segmentos con retención muy diferente? ¿El promedio es engañoso? ¿Sabemos qué segmentos retener prioritariamente? ¿Las acciones son diferenciadas por segmento?
**Recommended_Actions:** Desglosar retención por segmento (industria, tamaño, producto, canal); identificar segmentos con baja retención; focalizar acciones de mejora en segmentos críticos; asignar recursos según prioridad de retención.
**Severity_Level:** High
**Related_Patterns:** CUS-006, CUS-010, CUS-022, CUS-065, CUS-074

### CUS-012
**Pattern_Name:** Retención Basada Solo en Contrato
**Category:** Retención
**Description:** La retención de clientes depende exclusivamente de contratos de largo plazo, no de la satisfacción o el valor percibido; cuando el contrato termina, el cliente se va.
**Observable_Symptoms:** Clientes se quedan solo porque tienen contrato; insatisfechos pero atrapados; alta rotación en renovaciones; el equipo confía en el contrato no en el servicio; NPS bajo a pesar de retención contractual alta.
**Early_Warning_Signals:** Retención contractual alta pero NPS bajo; % de clientes que renuevan vs satisfacción; clientes que se quejan pero no se pueden ir; tasa de churn post-contrato alta; correlación baja entre retención y satisfacción.
**Typical_Causes:** Cultura de "el contrato retiene"; enfoque en barreras de salida no en valor; falta de inversión en experiencia; producto/servicio no fideliza; competidores ofrecen mejores alternativas.
**Business_Impact:** Retención artificial insostenible; cuando el mercado ofrece alternativas, el cliente se va; reputación de "trampa contractual"; clientes insatisfechos atrapados dañan la marca; LTV limitado a duración del contrato.
**Metrics_To_Check:** Retención vs satisfacción; % de clientes que renuevan voluntariamente; NPS de clientes en contrato; tasa de churn post-contrato; % de clientes que se irían si pudieran.
**Diagnostic_Questions:** ¿Los clientes se quedan por el contrato o porque quieren? ¿La satisfacción respalda la retención? ¿Si no hubiera contrato, se quedarían? ¿Estamos invirtiendo en valor o solo en barreras? ¿Hay clientes insatisfechos atrapados?
**Recommended_Actions:** Invertir en propuesta de valor y experiencia para que el cliente quiera quedarse; reducir dependencia de contratos largos; medir retención voluntaria vs contractual; eliminar barreras de salida y competir en valor; monitorear satisfacción de clientes con contrato vigente.
**Severity_Level:** High
**Related_Patterns:** CUS-007, CUS-010, CUS-020, CUS-044, CUS-054

### CUS-013
**Pattern_Name:** Sin Programa de Retención Proactivo
**Category:** Retención
**Description:** La empresa no tiene un programa estructurado de retención de clientes; solo reacciona cuando el cliente ya manifestó intención de irse, cuando es demasiado tarde.
**Observable_Symptoms:** No hay acciones de retención hasta que el cliente avisa que se va; el equipo reacciona cuando ya es tarde; intentos de retención de último minuto; no hay programa de fidelización; clientes que se van no son contactados antes.
**Early_Warning_Signals:** Sin programa de retención; % de clientes en riesgo contactados antes de cancelar < 20%; acciones de retención solo reactivas; sin customer health score; sin campañas de retención.
**Typical_Causes:** Cultura reactiva; falta de recursos para retención; desconocimiento de técnicas de retención; enfoque en adquisición sobre retención; no se mide ROI de retención.
**Business_Impact:** Clientes que podrían retenerse se pierden; CAC desperdiciado; ingresos recurrentes en riesgo; LTV menor al potencial; inestabilidad en base de clientes.
**Metrics_To_Check:** Tasa de retención vs programa activo; % de clientes en riesgo contactados antes de cancelar; éxito de retención proactiva vs reactiva; ROI de programa de retención; tendencia de churn evitable.
**Diagnostic_Questions:** ¿Tenemos un programa de retención proactivo? ¿Contactamos clientes antes de que cancelen? ¿Las acciones de retención son reactivas o proactivas? ¿Invertimos en retención? ¿Medimos el impacto?
**Recommended_Actions:** Implementar programa de retención proactivo; identificar clientes en riesgo antes de que cancelen; crear campañas de retención segmentadas; asignar recursos a retención; medir churn evitable.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-005, CUS-008, CUS-010, CUS-046, CUS-056

### CUS-014
**Pattern_Name:** Retención sin Análisis de Causas de Salida
**Category:** Retención
**Description:** La empresa no analiza sistemáticamente por qué los clientes se van, por lo que las acciones de retención son genéricas y no abordan las causas reales.
**Observable_Symptoms:** No hay encuestas de salida; las razones de cancelación no se registran; las causas de churn son "supuestas" no investigadas; se implementan acciones genéricas sin saber si atacan la causa; los mismos clientes se van por las mismas razones año tras año.
**Early_Warning_Signals:** Sin encuestas de salida; % de churn con causa documentada < 30%; causas de churn no analizadas periódicamente; acciones de retención no basadas en datos; patrones de churn no identificados.
**Typical_Causes:** Falta de proceso de análisis de churn; cultura de "siguiente cliente"; equipo no capacitado para investigar; herramientas CRM no usadas para registrar causas; recursos limitados.
**Business_Impact:** Acciones de retención inefectivas; causas raíz no resueltas; mismo churn recurrente; inversión en retención desperdiciada; imposibilidad de mejorar estructuralmente.
**Metrics_To_Check:** % de churn con causa documentada; encuestas de salida completadas; patrones de churn identificados; efectividad de acciones de retención; recurrencia de causas.
**Diagnostic_Questions:** ¿Sabemos por qué se van los clientes? ¿Tenemos encuestas de salida? ¿Documentamos las causas? ¿Analizamos patrones? ¿Las acciones de retención atacan las causas reales?
**Recommended_Actions:** Implementar encuestas de salida obligatorias; registrar causas de cancelación en CRM; analizar causas trimestralmente; identificar patrones; diseñar acciones basadas en causas reales.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-005, CUS-008, CUS-013, CUS-028

### CUS-015
**Pattern_Name:** Retención No Vinculada a Incentivos
**Category:** Retención
**Description:** Los incentivos del equipo comercial y de atención al cliente están basados solo en adquisición de nuevos clientes o ventas, no en retención, generando foco exclusivo en capturar no en mantener.
**Observable_Symptoms:** Comisiones solo por venta nueva; equipo no se preocupa por clientes existentes; no hay incentivos por renovación o retención; métricas de éxito solo incluyen nuevos clientes; clientes existentes descuidados.
**Early_Warning_Signals:** % de compensación variable vinculada a retención = 0%; KPIs de equipo solo de adquisición; sin incentivos por renovación; sin bonus por reducción de churn; equipo ignora clientes existentes.
**Typical_Causes:** Diseño de compensación tradicional; cultura de "vender más"; desconocimiento del valor de retención; enfoque de crecimiento basado en adquisición; falta de métricas de retención en gestión.
**Business_Impact:** Equipo enfocado en adquirir no en retener; clientes existentes descuidados; churn alto; CAC desperdiciado; LTV bajo; crecimiento insostenible.
**Metrics_To_Check:** % de compensación vinculada a retención; KPIs de equipo (adquisición vs retención); correlación incentivos-retención; tendencia de churn vs cambios en incentivos.
**Diagnostic_Questions:** ¿Los incentivos incluyen retención? ¿El equipo gana por retener clientes? ¿Las métricas de éxito incluyen retención? ¿Hay foco en clientes existentes? ¿La compensación impulsa el comportamiento correcto?
**Recommended_Actions:** Incorporar métricas de retención en compensación variable; incentivar renovaciones y reducción de churn; balancear KPIs de adquisición y retención; alinear incentivos con valor de largo plazo.
**Severity_Level:** High
**Related_Patterns:** CUS-010, CUS-013, CUS-044, CUS-066

### CUS-016
**Pattern_Name:** Retención sin Programa de Win-Back
**Category:** Retención
**Description:** La empresa no tiene un programa formal de recuperación de clientes perdidos (win-back), perdiendo la oportunidad de recuperar clientes que ya conocen la marca y que podrían regresar.
**Observable_Symptoms:** Clientes que se fueron nunca son contactados; no hay campañas de reactivación; clientes perdidos no se segmentan; la empresa no sabe si clientes que se fueron volverían; equipo da por perdidos a los que cancelan.
**Early_Warning_Signals:** Sin programa de win-back; % de clientes perdidos contactados < 10%; % de clientes que regresan sin intervención < 5%; sin segmentación de causas de salida para win-back; sin métricas de recuperación.
**Typical_Causes:** Cultura de "puerta giratoria"; enfoque en nuevos clientes; falta de recursos para win-back; desconocimiento del valor de recuperación; sistema no guarda datos de clientes perdidos.
**Business_Impact:** Clientes recuperables se pierden; inversión en adquirirlos originalmente se desperdicia; CAC de recuperación menor al de nuevos; oportunidad de ingresos perdida; base de clientes no recupera pérdidas.
**Metrics_To_Check:** Tasa de win-back; % de clientes perdidos contactados; CAC de win-back vs nuevos clientes; LTV de clientes recuperados; % de ingresos de clientes recuperados.
**Diagnostic_Questions:** ¿Contactamos a clientes que se fueron? ¿Tenemos programa de win-back? ¿Sabemos qué clientes podrían regresar? ¿El CAC de recuperación es menor que el de adquisición? ¿Invertimos en recuperación?
**Recommended_Actions:** Implementar programa de win-back con campañas segmentadas por causa de salida; contactar clientes perdidos a los 30, 60 y 90 días; ofrecer incentivos de regreso; medir tasa de recuperación; comparar CAC win-back vs nuevo.
**Severity_Level:** Medium
**Related_Patterns:** CUS-009, CUS-013, CUS-014, CUS-093

### CUS-017
**Pattern_Name:** Retención sin Métricas de Salud del Cliente
**Category:** Retención
**Description:** La empresa no utiliza un sistema de health score del cliente que permita identificar proactivamente el riesgo de churn y actuar antes de que el cliente cancele.
**Observable_Symptoms:** No hay indicadores de salud del cliente; el estado de la relación se evalúa subjetivamente; no se monitorean señales de riesgo; clientes que parecen "bien" cancelan; equipo no tiene visibilidad de la salud de la cartera.
**Early_Warning_Signals:** Sin health score implementado; % de clientes con health score desconocido = 100%; evaluación subjetiva del estado del cliente; sin alertas de riesgo; % de churn sorpresa > 40%.
**Typical_Causes:** Falta de herramienta de health score; desconocimiento de mejores prácticas; datos de cliente dispersos sin integrar; cultura reactiva; recursos para implementar.
**Business_Impact:** Churn evitable no detectado a tiempo; esfuerzos de retención no focalizados; clientes en riesgo no identificados; intervención tardía; LTV menor.
**Metrics_To_Check:** Health score implementado; % de clientes con health score activo; precisión predictiva del health score; % de churn sorpresa; tiempo entre alerta y acción.
**Diagnostic_Questions:** ¿Tenemos un sistema de health score? ¿Podemos identificar clientes en riesgo? ¿Las alertas son tempranas? ¿El health score es preciso? ¿Actuamos basados en el health score?
**Recommended_Actions:** Implementar customer health score (uso, satisfacción, engagement, reclamos, pago); definir umbrales de riesgo; crear alertas automáticas; asignar acciones por nivel de riesgo; revisar health scores semanalmente.
**Severity_Level:** High
**Related_Patterns:** CUS-005, CUS-013, CUS-020, CUS-046, CUS-056

### CUS-018
**Pattern_Name:** Retención sin Comunicación Post-Venta
**Category:** Retención
**Description:** Después de la venta inicial, la empresa no mantiene comunicación regular con el cliente, dejando que la relación se enfríe y aumentando el riesgo de churn por abandono.
**Observable_Symptoms:** Clientes no reciben comunicación entre la venta y la renovación; el único contacto es para cobrar o para renovar; clientes se sienten abandonados después de comprar; no hay newsletter, actualizaciones o check-ins; la relación es puramente transaccional.
**Early_Warning_Signals:** Frecuencia de comunicación post-venta < 1 vez por mes; % de clientes sin contacto en > 60 días; sin newsletter o comunicación periódica; clientes reportan "no sé nada de ellos"; NPS post-venta en declive.
**Typical_Causes:** Cultura de "vender y olvidar"; falta de estrategia de post-venta; recursos dedicados solo a adquisición; CRM no configurado para comunicación; desconocimiento del valor del contacto continuo.
**Business_Impact:** Relación cliente-empresa se enfría; cliente vulnerable a ofertas de competidores; oportunidades de upselling perdidas; cliente no desarrolla lealtad; churn por abandono aumenta.
**Metrics_To_Check:** Frecuencia de comunicación post-venta; % de clientes contactados en últimos 30 días; NPS por frecuencia de comunicación; correlación comunicación-retención; tasa de apertura de comunicaciones.
**Diagnostic_Questions:** ¿Mantenemos comunicación con clientes después de la venta? ¿Con qué frecuencia? ¿Los clientes sienten que los abandonamos? ¿La comunicación es solo transaccional o agrega valor? ¿La comunicación post-venta afecta la retención?
**Recommended_Actions:** Establecer programa de comunicación post-venta regular; crear newsletter o contenido de valor para clientes; programar check-ins periódicos; balancear comunicación transaccional y de valor; medir impacto en retención.
**Severity_Level:** High
**Related_Patterns:** CUS-007, CUS-010, CUS-037, CUS-044, CUS-054

### CUS-019
**Pattern_Name:** Retención sin Diferenciación por Valor del Cliente
**Category:** Retención
**Description:** Todos los clientes reciben el mismo esfuerzo de retención independientemente de su valor, desperdiciando recursos en clientes de bajo valor y descuidando a los de alto valor.
**Observable_Symptoms:** Clientes de alto y bajo valor reciben mismo tratamiento; no hay programa VIP; esfuerzos de retención uniformes; clientes de alto valor no identificados; recursos de retención mal asignados.
**Early_Warning_Signals:** % de recursos de retención asignados por valor del cliente; clientes de alto valor con misma tasa de contacto que bajo valor; sin segmentación por valor; % de clientes de alto valor con CSM dedicado < 30%; diferencias de retención entre segmentos de valor.
**Typical_Causes:** Falta de segmentación por valor; cultura de "todos los clientes son iguales"; recursos limitados sin priorización; desconocimiento de LTV por cliente; ausencia de programa de clientes estratégicos.
**Business_Impact:** Clientes de alto valor infra-atendidos; riesgo de perder los clientes más rentables; recursos desperdiciados en clientes de bajo valor; retención global subóptima; LTV no maximizado.
**Metrics_To_Check:** % de recursos por segmento de valor; retención por segmento de valor; satisfacción de clientes de alto valor; % de clientes de alto valor con CSM dedicado; LTV por segmento.
**Diagnostic_Questions:** ¿Diferenciamos esfuerzos de retención por valor del cliente? ¿Los clientes de alto valor reciben atención especial? ¿Sabemos quiénes son nuestros clientes más valiosos? ¿Los recursos de retención están bien asignados? ¿Los clientes top están satisfechos?
**Recommended_Actions:** Segmentar clientes por valor (LTV, ticket, potencial); asignar más recursos a clientes de alto valor; crear programa de clientes estratégicos con atención dedicada; optimizar inversión en retención por segmento; medir satisfacción de clientes top.
**Severity_Level:** High
**Related_Patterns:** CUS-006, CUS-011, CUS-065, CUS-074, CUS-083


## NPS

### CUS-020
**Pattern_Name:** NPS Bajo y Sin Tendencia de Mejora
**Category:** NPS
**Description:** El Net Promoter Score se mantiene consistentemente bajo o en declive, indicando insatisfacción generalizada y un riesgo estructural de pérdida de clientes.
**Observable_Symptoms:** NPS < 0 o por debajo del benchmark; detractores superan a promotores; el NPS no mejora a pesar de acciones; encuestas regulares muestran estancamiento; el equipo no sabe cómo mejorar el NPS.
**Early_Warning_Signals:** NPS < 30 (o < benchmark sectorial); tendencia de NPS decreciente por 3+ mediciones; % de detractores > 30%; ratio promotores/detractores < 1; % de clientes que recomendarían < 30%.
**Typical_Causes:** Problemas estructurales de producto o servicio; cultura no centrada en el cliente; quejas no resueltas; falta de innovación en experiencia; competidores mejor valorados.
**Business_Impact:** Clientes insatisfechos que no recomiendan; crecimiento orgánico por referidos bajo; reputación de marca dañada; churn alto; LTV bajo.
**Metrics_To_Check:** NPS; tendencia de NPS; % de promotores, pasivos y detractores; ratio promotores/detractores; correlación NPS-churn; benchmark vs sector.
**Diagnostic_Questions:** ¿Cuál es nuestro NPS? ¿Mejora o empeora? ¿Qué dice nuestro NPS sobre la salud del negocio? ¿Estamos por debajo del benchmark? ¿Sabemos qué genera detractores?
**Recommended_Actions:** Implementar medición regular de NPS (post-compra, post-soporte, periódico); analizar causas de detractores; crear plan de acción para principales causas; cerrar el ciclo con clientes (follow-up); celebrar y replicar lo que genera promotores.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-010, CUS-021, CUS-028, CUS-054, CUS-056

### CUS-021
**Pattern_Name:** NPS Sin Acción Posterior
**Category:** NPS
**Description:** La empresa mide el NPS pero no actúa sobre los resultados — no contacta a detractores, no investiga causas ni implementa mejoras, convirtiendo la medición en un ejercicio sin valor.
**Observable_Symptoms:** Se mide NPS pero no se hace nada con los datos; detractores no reciben follow-up; pasivos no se convierten en promotores; las causas de baja puntuación no se investigan; el NPS no mejora aunque se mida regularmente.
**Early_Warning_Signals:** % de detractores contactados después de encuesta < 20%; sin proceso de follow-up; acciones de mejora no vinculadas a resultados de NPS; NPS medido pero no accionado; equipo no conoce los resultados.
**Typical_Causes:** Cultura de "medir por medir"; falta de proceso de gestión de NPS; equipo no empoderado para actuar; recursos limitados; desconocimiento de mejores prácticas de NPS.
**Business_Impact:** Inversión en medir desperdiciada; oportunidades de mejora perdidas; detractores no convertidos; NPS no mejora; clientes perciben que su opinión no importa.
**Metrics_To_Check:** % de detractores contactados; % de pasivos convertidos a promotores; % de acciones implementadas basadas en NPS; mejora de NPS post-acción; satisfacción post-follow-up.
**Diagnostic_Questions:** ¿Actuamos sobre los resultados del NPS? ¿Contactamos a detractores? ¿Investigamos causas? ¿Implementamos mejoras? ¿El NPS mejora porque accionamos?
**Recommended_Actions:** Establecer proceso de gestión de NPS: detractores contactados en 24h, pasivos en 72h; investigar causas raíz; implementar mejoras; cerrar el ciclo con el cliente; medir mejora post-acción.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-020, CUS-028, CUS-029, CUS-054

### CUS-022
**Pattern_Name:** NPS No Segmentado
**Category:** NPS
**Description:** La empresa mide el NPS general pero no desglosa por segmento de cliente, producto, canal o punto de contacto, ocultando diferencias importantes en la satisfacción.
**Observable_Symptoms:** NPS único para toda la empresa; no se sabe qué segmento está más satisfecho; problemas en un segmento específico se ocultan; decisiones basadas en promedio engañoso; no hay NPS por punto de contacto.
**Early_Warning_Signals:** Sin NPS por segmento; sin NPS por punto de contacto; diferencia de NPS entre segmentos > 20 puntos; NPS promedio aceptable esconde segmentos malos; sin análisis de NPS por driver.
**Typical_Causes:** Falta de segmentación en encuestas; herramienta de NPS básica; cultura de "promedio es suficiente"; desconocimiento de análisis por driver; recursos limitados.
**Business_Impact:** Segmentos insatisfechos no identificados; acciones de mejora genéricas inefectivas; recursos mal asignados; problemas ocultos en segmentos específicos; oportunidad de mejora focalizada perdida.
**Metrics_To_Check:** NPS por segmento; NPS por punto de contacto; drivers de NPS identificados; diferencia entre segmentos; NPS promedio vs segmentos.
**Diagnostic_Questions:** ¿Desglosamos NPS por segmento? ¿Sabemos qué clientes están más insatisfechos? ¿El NPS promedio esconde problemas? ¿Medimos NPS por punto de contacto? ¿Sabemos qué impulsa el NPS?
**Recommended_Actions:** Segmentar NPS por cliente, producto, canal y punto de contacto; identificar segmentos con NPS bajo; focalizar acciones en drivers de mayor impacto; medir NPS transaccional y relacional.
**Severity_Level:** High
**Related_Patterns:** CUS-006, CUS-011, CUS-020, CUS-056, CUS-074

### CUS-023
**Pattern_Name:** NPS Sin Benchmark Competitivo
**Category:** NPS
**Description:** La empresa mide su NPS pero no lo compara con el benchmark de su sector o competidores, por lo que no sabe si su desempeño es bueno o malo en contexto.
**Observable_Symptoms:** El NPS se reporta sin referencia; no se sabe el NPS de competidores; la empresa celebra un NPS que podría ser bajo para el sector; no hay comparación externa; decisiones sin contexto competitivo.
**Early_Warning_Signals:** Sin benchmark de NPS del sector; NPS no comparable con competidores; no se participa en estudios sectoriales; celebración de NPS sin contexto; desconocimiento de estándares de la industria.
**Typical_Causes:** Falta de investigación de mercado; datos de competidores no disponibles; cultura de "compararse con uno mismo"; presupuesto limitado para estudios; desconocimiento de fuentes de benchmark.
**Business_Impact:** Percepción incorrecta del desempeño; celebrar un NPS bajo para el sector; no identificar oportunidades de mejora vs competidores; perder clientes frente a competidores con mejor NPS; estrategia sin referencia externa.
**Metrics_To_Check:** NPS vs benchmark sectorial; NPS vs competidores directos; posición relativa en el mercado; tendencia relativa.
**Diagnostic_Questions:** ¿Sabemos cuál es el NPS promedio de nuestro sector? ¿Cómo nos comparamos con competidores? ¿Nuestro NPS es bueno en contexto? ¿Participamos en estudios de benchmark? ¿Tenemos referencias externas?
**Recommended_Actions:** Investigar benchmark de NPS del sector (estudios, asociaciones, informes); comparar NPS con competidores directos; establecer metas basadas en benchmark; monitorear posición relativa; participar en estudios sectoriales.
**Severity_Level:** Medium
**Related_Patterns:** CUS-010, CUS-020, CUS-054

### CUS-024
**Pattern_Name:** NPS No Comunicado Internamente
**Category:** NPS
**Description:** Los resultados del NPS no se comparten con el equipo, por lo que los empleados no saben cómo está la satisfacción del cliente ni pueden alinear sus acciones para mejorarla.
**Observable_Symptoms:** El equipo no conoce el NPS; resultados no se comparten en reuniones; empleados no saben cómo contribuir a mejorar; el NPS es solo de la gerencia; no hay visibilidad de la satisfacción del cliente.
**Early_Warning_Signals:** % de empleados que conocen el NPS < 30%; NPS no se discute en reuniones de equipo; sin dashboard visible de NPS; resultados no compartidos regularmente; equipo no tiene metas de NPS.
**Typical_Causes**: Cultura de datos no transparente; gerencia no prioriza comunicación; falta de reuniones de revisión; desconocimiento del valor de compartir; equipos no alineados con metas de satisfacción.
**Business_Impact:** Equipo no orientado al cliente; falta de accountability en satisfacción; oportunidades de mejora no aprovechadas; decisiones descentralizadas sin brújula de cliente; NPS no mejora.
**Metrics_To_Check:** % de empleados que conocen el NPS; frecuencia de comunicación de NPS; metas de NPS por equipo; correlación entre conocimiento de NPS y mejora; participación en iniciativas de mejora.
**Diagnostic_Questions:** ¿El equipo conoce el NPS? ¿Se discute en reuniones? ¿Hay metas de NPS? ¿Los empleados saben cómo impactan la satisfacción? ¿El NPS es visible para todos?
**Recommended_Actions:** Comunicar NPS regularmente a toda la organización; crear dashboard visible de NPS; incorporar NPS en reuniones de equipo; establecer metas de NPS por área; celebrar mejoras y reconocer contribuciones.
**Severity_Level:** Medium
**Related_Patterns:** CUS-020, CUS-021, CUS-056

### CUS-025
**Pattern_Name:** NPS sin Medición Transaccional
**Category:** NPS
**Description:** La empresa solo mide NPS relacional (cada cierto tiempo) pero no transaccional (post-interacción), perdiendo la oportunidad de detectar problemas en puntos de contacto específicos.
**Observable_Symptoms:** NPS solo se mide una vez al trimestre o año; no hay encuestas post-compra, post-soporte o post-entrega; problemas en puntos de contacto específicos no se detectan; no se puede actuar sobre interacciones concretas; encuesta general no da granularidad.
**Early_Warning_Signals:** Frecuencia de NPS < trimestral; sin NPS transaccional; sin encuestas post-interacción; problemas recurrentes en puntos de contacto no detectados; NPS relacional no permite acción específica.
**Typical_Causes:** Desconocimiento de NPS transaccional; sobriedad de recursos para encuestas frecuentes; cultura de "medir general"; herramientas limitadas; miedo a molestar con encuestas.
**Business_Impact:** Problemas en puntos de contacto no detectados a tiempo; oportunidades de mejora perdidas; experiencia del cliente no optimizada; acción correctiva tardía.
**Metrics_To_Check:** Frecuencia de NPS transaccional; % de interacciones con encuesta post; NPS por punto de contacto; mejora post-acción en punto de contacto.
**Diagnostic_Questions:** ¿Medimos NPS después de interacciones clave? ¿Sabemos qué puntos de contacto generan insatisfacción? ¿La frecuencia de medición permite acción oportuna? ¿Tenemos NPS transaccional y relacional?
**Recommended_Actions:** Implementar NPS transaccional en puntos de contacto clave (compra, soporte, entrega, renovación); medir NPS relacional periódicamente; correlacionar ambos; actuar sobre puntos de contacto con bajo NPS.
**Severity_Level:** Medium
**Related_Patterns:** CUS-020, CUS-028, CUS-054, CUS-056

### CUS-026
**Pattern_Name:** NPS sin Análisis de Drivers
**Category:** NPS
**Description:** La empresa mide el NPS pero no analiza qué factores lo impulsan, por lo que no sabe qué mejorar para aumentar la satisfacción y recomendación.
**Observable_Symptoms:** Se sabe el NPS pero no por qué es ese número; no hay preguntas abiertas en encuestas; no se correlacionan variables con NPS; decisiones de mejora sin base; no se identifican palancas de satisfacción.
**Early_Warning_Signals:** Sin análisis de drivers de NPS; encuestas sin preguntas abiertas; no se correlacionan variables internas con NPS; % de mejora sin base drivers; equipo no sabe qué mueve el NPS.
**Typical_Causes:** Encuesta solo con pregunta de recomendación; falta de análisis estadístico; desconocimiento de metodología de drivers; recursos analíticos limitados; cultura de "el número es suficiente".
**Business_Impact:** No se sabe qué mejora el NPS; acciones de mejora no focalizadas; inversión en mejora sin dirección; NPS no mejora a pesar de esfuerzos; recursos desperdiciados en palancas equivocadas.
**Metrics_To_Check:** Drivers de NPS identificados; capacidad predictiva del modelo; correlación entre drivers y NPS; % de acciones basadas en drivers; mejora en drivers vs NPS.
**Diagnostic_Questions:** ¿Sabemos qué impulsa nuestro NPS? ¿Qué factores son más importantes para la satisfacción? ¿Las acciones de mejora se basan en análisis de drivers? ¿Correlacionamos variables internas con NPS? ¿Entendemos por qué los clientes nos recomiendan o no?
**Recommended_Actions:** Incluir preguntas abiertas y de atributos en encuestas NPS; analizar drivers de NPS (regresión, correlación); identificar palancas de mayor impacto; focalizar acciones en drivers clave; medir mejora en drivers vs NPS.
**Severity_Level:** High
**Related_Patterns:** CUS-020, CUS-021, CUS-022, CUS-054

### CUS-027
**Pattern_Name:** NPS por Debajo del Punto de Equilibrio de Crecimiento
**Category:** NPS
**Description:** El NPS está por debajo del nivel necesario para generar crecimiento orgánico (referidos, boca a boca positivo), por lo que la empresa depende exclusivamente de inversión paga para crecer.
**Observable_Symptoms:** Crecimiento solo por inversión en ads; pocos clientes llegan por referidos; el boca a boca no genera negocio; la empresa invierte cada vez más para crecer; clientes no recomiendan activamente.
**Early_Warning_Signals:** NPS < 50 (punto de referencia para crecimiento orgánico); % de clientes por referidos < 10%; % de promotores < 40%; correlación NPS-crecimiento < 0.3; costo de adquisición creciente sin mejora de NPS.
**Typical_Causes:** Experiencia del cliente no genera promotores; falta de programa de referidos; producto/servicio no memorable; servicio al cliente no destaca; valor no supera expectativas.
**Business_Impact**: Dependencia de inversión para crecer; CAC alto y creciente; crecimiento no orgánico; menor rentabilidad; vulnerabilidad a cambios en canales pagos; techo de crecimiento por falta de referidos.
**Metrics_To_Check:** NPS vs punto de equilibrio de crecimiento; % de clientes por referidos; CAC vs NPS; ratio promotores/clientes nuevos; tendencia de crecimiento orgánico.
**Diagnostic_Questions:** ¿Nuestro NPS genera crecimiento orgánico? ¿Los clientes nos recomiendan activamente? ¿Dependemos de inversión para crecer? ¿El boca a boca trae clientes? ¿Qué NPS necesitamos para crecer orgánicamente?
**Recommended_Actions:** Elevar NPS al punto de crecimiento orgánico (50+); implementar programa de referidos; crear experiencias que generen promotores; pedir referidos activamente; medir y celebrar crecimiento orgánico.
**Severity_Level:** High
**Related_Patterns:** CUS-020, CUS-037, CUS-042, CUS-054, CUS-065


## Reclamos

### CUS-028
**Pattern_Name:** Reclamos Recurrentes No Resueltos
**Category:** Reclamos
**Description:** Los mismos tipos de reclamos se repiten sistemáticamente sin que la empresa resuelva la causa raíz, indicando que hay problemas estructurales que no se abordan.
**Observable_Symptoms:** Los mismos reclamos aparecen mes tras mes; el equipo sabe qué reclamos van a recibir; no se investigan causas raíz; acciones correctivas temporales no definitivas; clientes se quejan de lo mismo que otros clientes.
**Early_Warning_Signals:** % de reclamos recurrentes (mismo tipo) > 30%; causas raíz no identificadas en > 50% de reclamos; tiempo sin solución definitiva > 3 meses; tendencia de reclamos por tipo sin mejora; backlog de reclamos sin resolver.
**Typical_Causes:** Falta de análisis de causas raíz; cultura de "apagar incendios"; equipo no empoderado para resolver; procesos de mejora continua inexistentes; liderazgo no prioriza solución definitiva.
**Business_Impact:** Clientes insatisfechos recurrentemente; aumento de churn por problemas no resueltos; equipo de atención desgastado; reputación dañada; costos operativos por atender mismos reclamos.
**Metrics_To_Check:** % de reclamos recurrentes; tiempo de resolución definitiva; tendencia por tipo de reclamo; % de causas raíz identificadas; satisfacción post-resolución.
**Diagnostic_Questions:** ¿Los reclamos se repiten? ¿Investigamos causas raíz? ¿Resolvemos definitivamente o solo apagamos incendios? ¿Hay mejora en los tipos de reclamo? ¿El equipo puede identificar patrones?
**Recommended_Actions:** Implementar análisis de causas raíz para reclamos recurrentes; crear comité de mejora basado en reclamos; establecer metas de reducción por tipo; resolver definitivamente, no temporalmente; medir recurrencia como KPI.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-008, CUS-029, CUS-030, CUS-054

### CUS-029
**Pattern_Name:** Tiempo de Resolución de Reclamos Excesivo
**Category:** Reclamos
**Description:** Los reclamos tardan demasiado en resolverse, aumentando la frustración del cliente y el riesgo de churn por cada día que pasa sin solución.
**Observable_Symptoms:** Clientes esperan días o semanas por una solución; el equipo no tiene metas de tiempo de respuesta; los reclamos se pierden en el sistema; clientes tienen que hacer seguimiento; la resolución se alarga innecesariamente.
**Early_Warning_Signals:** Tiempo promedio de resolución > 72h (o > benchmark); % de reclamos resueltos en 24h < 30%; clientes hacen seguimiento de su reclamo; reclamos sin actividad por > 48h; satisfacción post-resolución baja.
**Typical_Causes:** Procesos de atención ineficientes; equipo insuficiente; falta de herramientas de ticketing; reclamos escalan sin criterio; cultura de "ya se resolverá".
**Business_Impact:** Cliente frustrado; churn por mala experiencia de soporte; reclamos se acumulan; equipo desbordado; reputación de "no resuelven"; cliente comparte mala experiencia.
**Metrics_To_Check:** Tiempo promedio de resolución; % resuelto en 24h; % reclamos con actividad en 48h; satisfacción post-resolución; correlación tiempo de resolución-churn.
**Diagnostic_Questions:** ¿Cuánto tardamos en resolver reclamos? ¿El cliente está satisfecho con el tiempo? ¿Tenemos metas de tiempo de resolución? ¿Los reclamos se estancan? ¿El equipo tiene herramientas para resolver rápido?
**Recommended_Actions:** Establecer metas de tiempo de resolución (SLA); implementar sistema de ticketing con alertas; priorizar reclamos por severidad; empoderar al equipo para resolver sin escalar; medir y mejorar tiempo de resolución.
**Severity_Level:** High
**Related_Patterns:** CUS-008, CUS-028, CUS-031, CUS-054

### CUS-030
**Pattern_Name:** Sin Sistema de Gestión de Reclamos
**Category:** Reclamos
**Description:** La empresa no tiene un sistema formal para gestionar reclamos, por lo que se pierden, no se hace seguimiento y no se pueden analizar patrones.
**Observable_Symptoms:** Reclamos llegan por múltiples canales sin consolidar; no hay registro único; reclamos se pierden; no se puede hacer seguimiento; no hay reportes de reclamos; cada reclamo se maneja de manera diferente.
**Early_Warning_Signals:** Sin herramienta de ticketing; reclamos gestionados por email, teléfono y redes sin integración; % de reclamos registrados < 50%; sin reporte de reclamos; sin historial de cliente (mismos reclamos repetidos).
**Typical_Causes:** Falta de inversión en herramientas; cultura de "apagar incendios" sin proceso; equipo pequeño que cree no necesitarlo; desconocimiento de herramientas disponibles; priorización de otras inversiones.
**Business_Impact:** Reclamos se pierden; clientes se quejan dos veces; imposibilidad de analizar patrones; mala experiencia para el cliente; equipo sin visibilidad; mejora imposible sin datos.
**Metrics_To_Check:** % de reclamos registrados; herramientas de ticketing implementadas; tiempo de registro; % de reclamos con seguimiento completo; capacidad de reporte.
**Diagnostic_Questions:** ¿Tenemos un sistema de gestión de reclamos? ¿Todos los reclamos se registran? ¿Podemos hacer seguimiento? ¿Analizamos patrones? ¿Los reclamos se pierden?
**Recommended_Actions:** Implementar sistema de ticketing (gratuito o pago); centralizar reclamos de todos los canales; registrar cada reclamo con categoría y severidad; crear reportes semanales; analizar patrones para mejora.
**Severity_Level:** High
**Related_Patterns:** CUS-008, CUS-028, CUS-029, CUS-032, CUS-054

### CUS-031
**Pattern_Name:** Reclamos sin Priorización por Severidad
**Category:** Reclamos
**Description:** Todos los reclamos se tratan con la misma prioridad, resultando en que reclamos críticos (pérdida de servicio, error en facturación) se atienden al mismo ritmo que consultas simples.
**Observable_Symptoms:** Reclamos críticos y menores reciben mismo tiempo de respuesta; clientes con problemas graves esperan igual; el equipo no tiene criterios de priorización; reclamos urgentes no se identifican; insatisfacción en reclamos críticos.
**Early_Warning_Signals:** Sin criterios de priorización de reclamos; % de reclamos críticos sin respuesta en 4h > 30%; reclamos urgentes y no urgentes mismo SLA; clientes con problemas graves insatisfechos; escalamientos no definidos.
**Typical_Causes:** Falta de definición de niveles de severidad; equipo no entrenado en priorización; cultura de "primero en llegar, primero en atenderse"; herramientas sin capacidad de priorización; procesos planos.
**Business_Impact:** Problemas críticos no resueltos a tiempo; clientes con mayor impacto insatisfechos; riesgo de churn en clientes con problemas graves; daño reputacional por incidentes no atendidos; eficiencia subóptima.
**Metrics_To_Check:** Tiempo de respuesta por severidad; % de reclamos críticos con respuesta rápida; satisfacción por severidad; escalamientos activos; tiempo de resolución por severidad.
**Diagnostic_Questions:** ¿Priorizamos reclamos por severidad? ¿Los reclamos críticos se atienden primero? ¿Hay criterios de priorización definidos? ¿El equipo sabe identificar severidad? ¿Las herramientas soportan priorización?
**Recommended_Actions:** Definir niveles de severidad con criterios claros; establecer SLA por severidad; configurar herramientas para priorización automática; entrenar al equipo; monitorizar cumplimiento de SLA por severidad.
**Severity_Level:** High
**Related_Patterns:** CUS-028, CUS-029, CUS-030, CUS-054

### CUS-032
**Pattern_Name:** Reclamos sin Seguimiento Post-Resolución
**Category:** Reclamos
**Description:** Después de resolver un reclamo, la empresa no hace seguimiento para confirmar que el cliente quedó satisfecho, perdiendo la oportunidad de recuperar su confianza.
**Observable_Symptoms:** Cliente no es contactado después de resolver su reclamo; no se confirma satisfacción post-resolución; cliente puede quedar insatisfecho sin que la empresa lo sepa; no hay encuesta post-soporte; el caso se cierra sin validación del cliente.
**Early_Warning_Signals:** % de reclamos con seguimiento post-resolución < 30%; sin encuesta post-soporte; reclamos cerrados sin confirmación del cliente; reclamos reabiertos por misma causa > 15%; satisfacción post-resolución desconocida.
**Typical_Causes:** Proceso termina en resolución técnica no en satisfacción; cultura de "cerrar el ticket"; falta de proceso de follow-up; recursos limitados; desconocimiento del valor del cierre del ciclo.
**Business_Impact:** Cliente puede quedar insatisfecho sin que se sepa; oportunidad de recuperar confianza perdida; reclamos reabiertos; NPS post-soporte bajo; churn por insatisfacción no detectada.
**Metrics_To_Check:** % de reclamos con seguimiento post-resolución; satisfacción post-resolución; % de reclamos reabiertos; NPS post-soporte; tasa de recuperación de clientes con reclamo.
**Diagnostic_Questions:** ¿Contactamos al cliente después de resolver su reclamo? ¿Verificamos su satisfacción? ¿Tenemos encuesta post-soporte? ¿Los reclamos se reabren? ¿Aprovechamos la oportunidad de recuperar confianza?
**Recommended_Actions:** Implementar seguimiento post-resolución obligatorio (24-48h después); enviar encuesta de satisfacción post-soporte; contactar personalmente reclamos críticos; cerrar el ciclo con el cliente; medir satisfacción post-resolución.
**Severity_Level:** Medium
**Related_Patterns:** CUS-008, CUS-028, CUS-029, CUS-054

### CUS-033
**Pattern_Name:** Volumen de Reclamos Creciente
**Category:** Reclamos
**Description:** El número de reclamos está aumentando más rápido que la base de clientes, indicando problemas de calidad, servicio o producto que están empeorando.
**Observable_Symptoms:** Más clientes se quejan cada mes; el equipo de atención está cada vez más desbordado; los reclamos crecen más que los clientes nuevos; se normaliza el aumento de reclamos; causas raíz no se abordan.
**Early_Warning_Signals:** Tasa de reclamos por cliente creciente; % de aumento de reclamos > % de aumento de clientes; tendencia alcista por 3+ meses; equipo de atención pide refuerzos constantemente; reclamos por cliente > 1.
**Typical_Causes:** Problemas de calidad no resueltos; producto o servicio empeora; cambios en procesos que generan insatisfacción; equipo de atención no da abasto; falta de mejora continua.
**Business_Impact:** Clientes cada vez más insatisfechos; equipo de atención saturado; calidad de respuesta disminuye; churn aumenta; reputación se deteriora; costos operativos crecen.
**Metrics_To_Check:** Tasa de reclamos por cliente; tendencia de reclamos; % de aumento vs crecimiento de clientes; capacidad del equipo vs volumen; causas de reclamos crecientes.
**Diagnostic_Questions:** ¿Los reclamos están aumentando? ¿Crecen más que los clientes? ¿Sabemos por qué? ¿El equipo está desbordado? ¿Se están abordando las causas raíz?
**Recommended_Actions:** Investigar causas del aumento; implementar acciones correctivas urgentes; reforzar equipo de atención temporalmente; analizar si hay cambios recientes que generaron reclamos; establecer metas de reducción.
**Severity_Level:** High
**Related_Patterns:** CUS-001, CUS-028, CUS-029, CUS-030, CUS-054

### CUS-034
**Pattern_Name:** Reclamos en Redes Sociales sin Gestión
**Category:** Reclamos
**Description:** Los clientes expresan reclamos en redes sociales y la empresa no los gestiona adecuadamente, amplificando el daño reputacional y mostrando desinterés públicamente.
**Observable_Symptoms:** Reclamos en redes sin respuesta; clientes se quejan públicamente; la empresa no monitorea menciones; reclamos en redes tardan en atenderse; la reputación online se deteriora.
**Early_Warning_Signals:** Tiempo de respuesta a reclamos en redes > 4h; % de reclamos en redes sin respuesta > 30%; sin herramienta de social listening; reclamos virales no gestionados; reseñas negativas en aumento.
**Typical_Causes**: Falta de monitoreo de redes; equipo no dedicado a redes sociales; desconocimiento de impacto reputacional; cultura de ignorar redes; recursos limitados.
**Business_Impact:** Daño reputacional público; reclamos se viralizan; clientes potenciales ven quejas sin respuesta; percepción de desinterés; pérdida de confianza; impacto en ventas.
**Metrics_To_Check:** Tiempo de respuesta en redes; % de reclamos en redes respondidos; sentimiento de menciones; reseñas promedio; correlación reclamos en redes-ventas.
**Diagnostic_Questions:** ¿Monitoreamos reclamos en redes sociales? ¿Respondemos a tiempo? ¿Tenemos un proceso de gestión de redes? ¿Las quejas públicas se atienden? ¿Medimos el impacto reputacional?
**Recommended_Actions:** Implementar monitoreo de redes sociales; establecer SLA de respuesta en redes (< 2h); crear protocolo de gestión de crisis en redes; responder pública y privadamente; medir sentimiento y reseñas.
**Severity_Level:** High
**Related_Patterns:** CUS-028, CUS-029, CUS-030, CUS-054, CUS-057

### CUS-035
**Pattern_Name:** Reclamos sin Categorización para Análisis
**Category:** Reclamos
**Description:** Los reclamos no se categorizan de manera consistente, imposibilitando el análisis de patrones, la identificación de causas raíz y la mejora sistemática.
**Observable_Symptoms:** Los reclamos se registran sin categoría; cada persona clasifica diferente; no se pueden generar reportes por tipo; patrones no identificables; imposible saber qué problemas son más frecuentes.
**Early_Warning_Signals:** Sin categorías de reclamos definidas; % de reclamos sin categoría > 30%; categorías inconsistentes entre agentes; sin reportes por tipo de reclamo; análisis de reclamos no existe.
**Typical_Causes:** Falta de taxonomía de reclamos; herramienta sin categorización; equipo no entrenado; cultura de "resolver y seguir"; desconocimiento del valor del análisis.
**Business_Impact:** Improvisibilidad de mejorar; mismos reclamos se repiten sin identificar; causas raíz no detectadas; inversión en mejora sin dirección; aprendizaje organizacional perdido.
**Metrics_To_Check:** Categorías definidas; % de reclamos categorizados; consistencia entre agentes; reportes por categoría disponibles; mejoras implementadas por categoría.
**Diagnostic_Questions:** ¿Categorizamos los reclamos? ¿Las categorías son consistentes? ¿Podemos generar reportes por tipo? ¿Identificamos patrones? ¿Usamos los datos para mejorar?
**Recommended_Actions:** Definir taxonomía de reclamos (categorías y subcategorías); configurar herramienta para categorización obligatoria; entrenar al equipo; generar reportes semanales por categoría; usar datos para mejora continua.
**Severity_Level:** Medium
**Related_Patterns:** CUS-028, CUS-030, CUS-033, CUS-054

### CUS-036
**Pattern_Name:** Reclamos sin Empoderamiento del Equipo
**Category:** Reclamos
**Description:** El equipo de atención al cliente no tiene autoridad para resolver reclamos sin escalar, resultando en demoras, clientes frustrados y sobrecarga de supervisores.
**Observable_Symptoms:** Cada reclamo debe escalarse para tomar decisiones; el equipo no puede ofrecer soluciones; clientes esperan mientras "consulto con mi supervisor"; procesos de aprobación lentos; equipo desmotivado por falta de autonomía.
**Early_Warning_Signals:** % de reclamos que requieren escalamiento > 40%; tiempo de resolución por falta de autoridad alto; equipo reporta "no me dejan resolver"; clientes piden hablar con supervisor; satisfacción del equipo baja.
**Typical_Causes:** Cultura de control centralizado; desconfianza en el equipo; falta de políticas claras de autorización; procesos rígidos; liderazgo no empodera.
**Business_Impact:** Resolución lenta; cliente frustrado; equipo desmotivado; supervisores cuello de botella; costos operativos altos por múltiples niveles; churn evitable por demora.
**Metrics_To_Check:** % de reclamos resueltos sin escalar; tiempo de resolución con vs sin escalamiento; satisfacción del cliente por nivel de resolución; satisfacción del equipo; costo por reclamo.
**Diagnostic_Questions:** ¿El equipo puede resolver reclamos sin escalar? ¿Hay políticas claras de autorización? ¿Los supervisores son cuello de botella? ¿Los clientes piden hablar con supervisores? ¿El equipo está empoderado?
**Recommended_Actions:** Definir políticas de autorización por nivel; empoderar al equipo para resolver dentro de parámetros; reducir niveles de escalamiento; entrenar al equipo en toma de decisiones; medir resolución en primer nivel.
**Severity_Level:** Medium
**Related_Patterns:** CUS-008, CUS-029, CUS-030, CUS-031


## Fidelización

### CUS-037
**Pattern_Name:** Sin Programa de Fidelización
**Category:** Fidelización
**Description:** La empresa no tiene un programa formal de fidelización que incentive la recompra, la lealtad y la recomendación, perdiendo una de las herramientas más efectivas para retener clientes.
**Observable_Symptoms:** No hay programa de puntos, descuentos por recurrencia o beneficios para clientes frecuentes; clientes leales no reciben reconocimiento; no hay incentivos para recomprar; la fidelización depende solo de la buena voluntad del cliente; competidores tienen programa de lealtad.
**Early_Warning_Signals:** Sin programa de fidelización implementado; % de clientes que recompran sin incentivo < 30%; tasa de recompra baja; clientes no tienen beneficios por antigüedad o frecuencia; programa de lealtad no considerado estratégico.
**Typical_Causes:** Desconocimiento de programas de fidelización; falta de recursos para implementar; cultura de "el cliente vuelve si quiere"; creencia de que "nuestro producto fideliza solo"; priorización de adquisición sobre fidelización.
**Business_Impact:** Clientes no incentivados a recomprar; competidores con programa captan clientes; LTV menor al potencial; tasa de recompra baja; falta de datos de preferencias de clientes.
**Metrics_To_Check:** % de clientes en programa de fidelización; tasa de recompra con vs sin programa; LTV de clientes fidelizados vs no; retención de miembros del programa; ROI del programa.
**Diagnostic_Questions:** ¿Tenemos un programa de fidelización? ¿Los clientes reciben beneficios por su lealtad? ¿Incentivamos la recompra? ¿Nuestros competidores tienen programa? ¿Sabemos qué valor tiene un cliente fidelizado?
**Recommended_Actions:** Implementar programa de fidelización (puntos, niveles, beneficios exclusivos); definir reglas claras de acumulación y canje; comunicar el programa activamente; medir impacto en recompra y retención; iterar basado en datos.
**Severity_Level:** High
**Related_Patterns:** CUS-010, CUS-018, CUS-027, CUS-038, CUS-044, CUS-065

### CUS-038
**Pattern_Name:** Programa de Fidelización Sin Engagement
**Category:** Fidelización
**Description:** La empresa tiene un programa de fidelización pero los clientes no participan activamente, acumulan puntos sin canjear o lo ignoran, indicando que el programa no es atractivo o está mal comunicado.
**Observable_Symptoms:** Baja inscripción en el programa; puntos acumulados sin canjear; clientes no conocen el programa; beneficios no son atractivos; el programa no genera cambio de comportamiento.
**Early_Warning_Signals:** % de clientes inscritos en programa < 30%; % de puntos canjeados < 20%; % de clientes que conocen el programa < 40%; sin actividad en programa en últimos 3 meses; NPS de miembros vs no miembros sin diferencia.
**Typical_Causes:** Beneficios poco atractivos; programa complejo de entender; comunicación insuficiente; canje difícil o limitado; programa no alineado con lo que valora el cliente.
**Business_Impact:** Inversión en programa desperdiciada; no genera lealtad incremental; clientes no cambian comportamiento; retención no mejora; recursos mal invertidos.
**Metrics_To_Check:** % de clientes inscritos; % de puntos canjeados; % de clientes activos en programa; frecuencia de compra de miembros vs no miembros; retención de miembros vs no miembros.
**Diagnostic_Questions:** ¿Los clientes participan activamente? ¿Canjean sus puntos? ¿El programa es atractivo? ¿Es fácil de entender y usar? ¿El programa genera lealtad incremental?
**Recommended_Actions:** Rediseñar programa basado en preferencias del cliente; simplificar reglas de acumulación y canje; ofrecer beneficios que realmente valoren; comunicar el programa activamente; medir engagement y ajustar.
**Severity_Level:** Medium
**Related_Patterns:** CUS-037, CUS-044, CUS-054, CUS-065

### CUS-039
**Pattern_Name:** Fidelización sin Personalización
**Category:** Fidelización
**Description:** El programa de fidelización trata a todos los clientes por igual, sin reconocer diferencias en valor, preferencias o comportamiento, perdiendo efectividad en clientes de alto valor.
**Observable_Symptoms:** Todos los clientes reciben los mismos beneficios; clientes de alto valor no reciben reconocimiento especial; el programa no se segmenta; ofertas genéricas para todos; clientes top no se sienten valorados.
**Early_Warning_Signals:** Programa único para todos los segmentos; % de personalización en programa < 20%; clientes de alto valor con mismo trato que bajo valor; sin segmentación por valor en beneficios; satisfacción de clientes top no mejora con programa.
**Typical_Causes:** Falta de segmentación de clientes; programa diseñado para ser simple; recursos limitados para personalizar; desconocimiento de técnicas de personalización; cultura de "igualdad para todos".
**Business_Impact:** Clientes de alto valor no retenidos óptimamente; inversión en fidelización mal dirigida; programa no genera lealtad diferenciada; clientes top sensibles a ofertas de competidores; LTV no maximizado.
**Metrics_To_Check:** % de personalización en programa; satisfacción de clientes top con programa; retención de clientes top con vs sin personalización; LTV de clientes con programa personalizado.
**Diagnostic_Questions:** ¿El programa reconoce diferencias entre clientes? ¿Los clientes de alto valor reciben beneficios especiales? ¿Personalizamos ofertas? ¿El programa trata a todos igual? ¿Los clientes top se sienten valorados?
**Recommended_Actions:** Segmentar clientes por valor y preferencias; crear niveles en el programa (bronce, plata, oro); personalizar beneficios y comunicación; reconocer a clientes top con experiencias exclusivas; medir impacto por segmento.
**Severity_Level:** High
**Related_Patterns:** CUS-019, CUS-037, CUS-065, CUS-074, CUS-083

### CUS-040
**Pattern_Name:** Fidelización sin Medición de Impacto
**Category:** Fidelización
**Description:** La empresa invierte en fidelización pero no mide el impacto en retención, recompra o LTV, por lo que no sabe si el programa genera retorno.
**Observable_Symptoms:** Se invierte en el programa pero no se mide su efectividad; no hay KPIs de fidelización; no se compara comportamiento de miembros vs no miembros; el programa existe "porque sí"; no se puede calcular ROI.
**Early_Warning_Signals:** Sin KPIs del programa de fidelización; % de miembros vs no miembros no medido; sin análisis de incrementalidad; retención de miembros desconocida; ROI del programa no calculado.
**Typical_Causes:** Falta de cultura de medición; programa implementado sin métricas; desconocimiento de cómo medir impacto; recursos limitados para analytics; creencia de que "fidelización siempre es buena".
**Business_Impact:** Inversión sin retorno medible; programa puede no estar generando valor; recursos potencialmente desperdiciados; imposibilidad de optimizar; justificación del programa difícil.
**Metrics_To_Check:** (Deberían medirse) retención de miembros vs no miembros; frecuencia de compra incremental; LTV incremental; ROI del programa; costo del programa vs ingresos incrementales.
**Diagnostic_Questions:** ¿Medimos el impacto del programa de fidelización? ¿Sabemos si genera más recompra? ¿Comparamos miembros vs no miembros? ¿Calculamos el ROI? ¿Optimizamos basado en datos?
**Recommended_Actions:** Definir KPIs del programa (retención, frecuencia, LTV); medir comportamiento de miembros vs grupo de control; calcular ROI del programa; reportar impacto periódicamente; optimizar basado en datos.
**Severity_Level:** Medium
**Related_Patterns:** CUS-037, CUS-038, CUS-065, CUS-066

### CUS-041
**Pattern_Name:** Fidelización sin Beneficios Emocionales
**Category:** Fidelización
**Description:** El programa de fidelización ofrece solo beneficios transaccionales (descuentos) sin componentes emocionales (reconocimiento, exclusividad, pertenencia), limitando la creación de lealtad genuina.
**Observable_Symptoms:** El programa solo da descuentos; no hay reconocimiento, estatus o pertenencia; clientes no sienten conexión emocional; el programa es puramente transaccional; no hay comunidad de clientes.
**Early_Warning_Signals:** % de beneficios transaccionales vs emocionales > 80%; sin reconocimiento de estatus; sin comunidad o eventos exclusivos; clientes no expresan orgullo de pertenecer; programa fácilmente replicable por competidores.
**Typical_Causes:** Desconocimiento de fidelización emocional; presupuesto limitado para beneficios no transaccionales; cultura de "descuento es lo único que funciona"; falta de creatividad en diseño de programa; enfoque en corto plazo.
**Business_Impact:** Lealtad frágil basada en precio; cliente se va por mejor descuento; programa no genera defensores de marca; competidores igualan beneficios; LTV no potenciado.
**Metrics_To_Check:** % de beneficios emocionales vs transaccionales; NPS de miembros; % de clientes que recomiendan el programa; sentido de pertenencia en encuestas; defensa de marca.
**Diagnostic_Questions:** ¿Nuestro programa ofrece algo más que descuentos? ¿Los clientes sienten pertenencia? ¿Hay reconocimiento y estatus? ¿Generamos comunidad? ¿La lealtad es transaccional o emocional?
**Recommended_Actions:** Incorporar beneficios emocionales (reconocimiento, exclusividad, acceso anticipado, comunidad); crear niveles con estatus; organizar eventos exclusivos; reconocer hitos del cliente; medir conexión emocional.
**Severity_Level:** Medium
**Related_Patterns:** CUS-010, CUS-037, CUS-039, CUS-054

### CUS-042
**Pattern_Name:** Fidelización sin Programa de Referidos
**Category:** Fidelización
**Description:** La empresa fideliza clientes pero no aprovecha su satisfacción para generar nuevos clientes a través de un programa de referidos, perdiendo una fuente de crecimiento de bajo costo.
**Observable_Symptoms:** Clientes satisfechos recomiendan esporádicamente; no hay incentivo para referir; no se pide referidos; no hay programa formal; el potencial de referidos no se mide.
**Early_Warning_Signals:** Sin programa de referidos; % de clientes que llegan por referidos < 5%; % de clientes que referirían sin incentivo < 10%; sin medición de intención de recomendar; sin proceso de solicitud de referidos.
**Typical_Causes:** Desconocimiento del poder del referido; miedo a "molestar" al cliente; falta de recursos para implementar; cultura de "el cliente recomienda si quiere"; priorización de otros canales.
**Business_Impact:** Fuente de crecimiento orgánico desaprovechada; CAC más alto del necesario; clientes satisfechos no activados como promotores; oportunidad de ingresos perdida; crecimiento más lento.
**Metrics_To_Check:** % de clientes por referidos; CAC de referidos vs otros canales; LTV de clientes referidos; tasa de referidos por cliente; efectividad del programa.
**Diagnostic_Questions:** ¿Tenemos programa de referidos? ¿Pedimos referidos activamente? ¿Incentivamos las recomendaciones? ¿Sabemos cuántos clientes llegan por referido? ¿Estamos maximizando este canal?
**Recommended_Actions:** Implementar programa de referidos con incentivos atractivos; integrar solicitud de referidos en puntos de alta satisfacción; promover el programa; medir y optimizar; agradecer a los que refieren.
**Severity_Level:** High
**Related_Patterns:** CUS-027, CUS-037, CUS-043, CUS-054, CUS-065

### CUS-043
**Pattern_Name:** Fidelización sin Comunicación Post-Compra
**Category:** Fidelización
**Description:** La empresa no mantiene comunicación con el cliente después de la compra (más allá de lo transaccional), perdiendo la oportunidad de construir relación y lealtad a largo plazo.
**Observable_Symptoms:** Después de la compra, el cliente no recibe comunicación relevante; solo emails transaccionales (facturas, envíos); no hay contenido de valor, tips o actualizaciones; el cliente siente que la relación terminó con la compra; no hay programa de comunicación post-venta.
**Early_Warning_Signals:** Frecuencia de comunicación post-compra < 1 vez al mes; % de comunicación no transaccional < 20%; clientes reportan "no sé nada de ellos"; tasa de apertura de comunicaciones baja; clientes no desarrollan relación con la marca.
**Typical_Causes:** Cultura de "vender y olvidar"; falta de estrategia de comunicación post-venta; recursos dedicados a adquisición; CRM no configurado; desconocimiento del valor del contacto continuo.
**Business_Impact:** Relación no se profundiza; cliente no desarrolla lealtad; oportunidades de upselling perdidas; vulnerable a ofertas de competidores; recompra no incentivada.
**Metrics_To_Check:** Frecuencia de comunicación post-compra; % de comunicación de valor vs transaccional; tasa de apertura; NPS por frecuencia de comunicación; tasa de recompra por comunicación.
**Diagnostic_Questions:** ¿Comunicamos con clientes después de la compra? ¿La comunicación agrega valor? ¿El cliente siente que mantenemos la relación? ¿La comunicación post-compra genera lealtad? ¿Tenemos un plan de comunicación?
**Recommended_Actions:** Implementar programa de comunicación post-compra con contenido de valor; segmentar comunicación por perfil y etapa; balancear frecuencia; medir impacto en lealtad y recompra; personalizar mensajes.
**Severity_Level:** High
**Related_Patterns:** CUS-018, CUS-037, CUS-044, CUS-054, CUS-055

### CUS-044
**Pattern_Name:** Fidelización sin Customer Success
**Category:** Fidelización
**Description:** La empresa espera que los clientes se fidelicen solos, sin un proceso proactivo de customer success que asegure que obtienen valor, resuelven sus problemas y quieran renovar.
**Observable_Symptoms:** No hay CSM asignado a clientes; el cliente solo recibe contacto cuando tiene problemas; no hay check-ins proactivos; la renovación depende del cliente; el éxito del cliente no se gestiona.
**Early_Warning_Signals:** Sin equipo o función de customer success; % de clientes con CSM asignado < 20%; sin check-ins proactivos; renovación no gestionada; cliente no contactado entre venta y renovación.
**Typical_Causes:** Desconocimiento de customer success; cultura de "el cliente es responsable de su éxito"; recursos limitados; enfoque en ventas sobre servicio; falta de metodología CS.
**Business_Impact:** Clientes no guiados al éxito; churn evitable por falta de soporte proactivo; LTV menor; upselling no identificado; cliente no alcanza su máximo potencial de uso.
**Metrics_To_Check:** % de clientes con CSM asignado; frecuencia de check-ins; NPS de clientes con vs sin CSM; retención con vs sin CSM; tiempo para alcanzar valor.
**Diagnostic_Questions:** ¿Tenemos un proceso de customer success? ¿Aseguramos que el cliente obtenga valor? ¿Hay check-ins proactivos? ¿Gestionamos activamente la renovación? ¿El cliente tiene un interlocutor de éxito?
**Recommended_Actions:** Implementar función de customer success; asignar CSM a clientes clave; establecer check-ins periódicos; medir adopción y salud del cliente; intervenir proactivamente ante señales de riesgo.
**Severity_Level:** High
**Related_Patterns:** CUS-002, CUS-003, CUS-007, CUS-010, CUS-046, CUS-047

### CUS-045
**Pattern_Name:** Fidelización sin Encuestas de Satisfacción Periódicas
**Category:** Fidelización
**Description:** La empresa no mide la satisfacción del cliente de manera regular, por lo que no sabe si los clientes están contentos hasta que es demasiado tarde (cuando cancelan).
**Observable_Symptoms:** No se realizan encuestas de satisfacción regulares; el estado de la relación se desconoce; la primera noticia de insatisfacción es la cancelación; no hay pulso de la satisfacción del cliente; decisiones sin datos de satisfacción.
**Early_Warning_Signals:** Frecuencia de encuestas de satisfacción < 1 vez al año; % de clientes encuestados < 30% anual; sin encuesta post-interacción; satisfacción desconocida para la mayoría de clientes; sin sistema de alerta de insatisfacción.
**Typical_Causes:** Falta de recursos para encuestas; desconocimiento de herramientas gratuitas; cultura de "si no se quejan, están contentos"; miedo a obtener feedback negativo; priorización de otras actividades.
**Business_Impact:** Imposibilidad de detectar insatisfacción temprana; clientes discontentos no identificados; churn evitable no prevenido; oportunidad de mejora perdida; relación no monitoreada.
**Metrics_To_Check:** Frecuencia de encuestas; % de clientes encuestados; tendencia de satisfacción; % de clientes insatisfechos detectados antes de churn; acciones basadas en encuestas.
**Diagnostic_Questions:** ¿Medimos la satisfacción regularmente? ¿Sabemos cómo está la relación con cada cliente? ¿Detectamos insatisfacción antes de la cancelación? ¿Usamos encuestas periódicas? ¿Actuamos sobre los resultados?
**Recommended_Actions:** Implementar encuestas periódicas de satisfacción (post-interacción y periódicas); usar herramientas gratuitas (Google Forms, Typeform, SurveyMonkey); establecer frecuencia mínima (trimestral); cerrar el ciclo con clientes; actuar sobre resultados.
**Severity_Level:** High
**Related_Patterns:** CUS-005, CUS-020, CUS-021, CUS-045, CUS-054


## Customer Success

### CUS-046
**Pattern_Name:** Customer Success Reactivo
**Category:** Customer Success
**Description:** El equipo de customer success solo actúa cuando el cliente tiene problemas o solicita ayuda, en lugar de ser proactivo en asegurar que el cliente obtenga valor y éxito con el producto.
**Observable_Symptoms:** CSM solo contacta clientes cuando hay quejas; no hay check-ins programados; las acciones son reactivas a problemas; cliente no recibe orientación proactiva; el equipo CS está en modo "apagar incendios".
**Early_Warning_Signals:** % de actividades de CS proactivas vs reactivas < 30%; sin calendario de check-ins; CSM dedicados a resolver problemas no a prevenir; clientes solo contactan cuando tienen problemas; % de clientes con plan de éxito < 20%.
**Typical_Causes:** Cultura reactiva; equipo CS desbordado por reclamos; falta de metodología de CS proactivo; KPIs de CS basados en resolución no en prevención; recursos insuficientes.
**Business_Impact:** Clientes no guiados al éxito; problemas no prevenidos; churn evitable; upselling no identificado; valor no maximizado; LTV menor.
**Metrics_To_Check:** Ratio actividades proactivas vs reactivas; % de clientes con plan de éxito; frecuencia de check-ins proactivos; NPS de clientes con CS proactivo vs reactivo; retención diferencial.
**Diagnostic_Questions:** ¿El equipo CS es proactivo o reactivo? ¿Tenemos check-ins programados? ¿Prevenimos problemas o solo los resolvemos? ¿Los clientes tienen un plan de éxito? ¿El equipo CS tiene tiempo para ser proactivo?
**Recommended_Actions:** Redefinir rol de CS como proactivo; establecer check-ins periódicos por segmento; crear planes de éxito para clientes clave; separar funciones de soporte y CS; medir proactividad como KPI.
**Severity_Level:** Critical
**Related_Patterns:** CUS-002, CUS-003, CUS-005, CUS-013, CUS-044, CUS-047

### CUS-047
**Pattern_Name:** Sin Proceso de Onboarding Formal
**Category:** Customer Success
**Description:** No existe un proceso estructurado de onboarding para nuevos clientes, por lo que muchos no logran activarse correctamente y aumentan las probabilidades de churn temprano.
**Observable_Symptoms:** Cada nuevo cliente experimenta un onboarding diferente; no hay checklist de activación; clientes nuevos no saben por dónde empezar; el equipo asume que el cliente "ya sabe"; primeros pasos del cliente no están guiados.
**Early_Warning_Signals:** Sin proceso de onboarding documentado; % de clientes que completan onboarding < 40%; tiempo hasta primer valor (TTV) no medido; clientes nuevos con baja activación; churn temprano > 15%.
**Typical_Causes:** Falta de inversión en onboarding; cultura de "cada cliente es diferente"; equipo sin metodología; producto/servicio complejo sin guía; desconocimiento del impacto del onboarding.
**Business_Impact:** Clientes no logran activarse; churn temprano alto; CAC desperdiciado; cliente no ve valor; NPS post-onboarding bajo; equipo de soporte recibe consultas básicas evitables.
**Metrics_To_Check:** % de clientes que completan onboarding; tiempo hasta primer valor; churn en primeros 90 días; NPS post-onboarding; satisfacción con onboarding.
**Diagnostic_Questions:** ¿Tenemos un proceso de onboarding estructurado? ¿Los clientes nuevos saben qué hacer? ¿Miden el tiempo hasta que el cliente ve valor? ¿El onboarding es consistente? ¿Los clientes se activan correctamente?
**Recommended_Actions:** Diseñar proceso de onboarding estructurado con hitos claros; crear checklist de activación; asignar responsable de onboarding; medir tiempo hasta primer valor; hacer seguimiento en primeros 30-60-90 días.
**Severity_Level:** Critical
**Related_Patterns:** CUS-002, CUS-003, CUS-044, CUS-046, CUS-048, CUS-054

### CUS-048
**Pattern_Name:** Customer Success Sin Segmentación
**Category:** Customer Success
**Description:** Todos los clientes reciben el mismo nivel de atención de customer success, sin diferenciar por valor, potencial o riesgo, desperdiciando recursos en clientes de bajo valor y descuidando a los estratégicos.
**Observable_Symptoms:** Clientes pequeños y grandes reciben mismo servicio de CS; no hay niveles de servicio; recursos de CS mal asignados; clientes estratégicos no tienen atención diferenciada; el equipo CS está desbordado con clientes de bajo valor.
**Early_Warning_Signals:** % de clientes con CSM dedicado no segmentado por valor; sin niveles de servicio; clientes de alto valor con misma frecuencia de contacto que bajo valor; recursos CS no priorizados; clientes estratégicos insatisfechos con atención.
**Typical_Causes:** Falta de segmentación de clientes; cultura de "todos los clientes merecen lo mismo"; recursos CS limitados sin priorización; desconocimiento de modelos de servicio segmentados; ausencia de programa de clientes estratégicos.
**Business_Impact:** Clientes de alto valor infra-atendidos; riesgo de perder los clientes más rentables; recursos desperdiciados en clientes de bajo valor; equipo CS ineficiente; retención subóptima.
**Metrics_To_Check:** % de recursos CS por segmento de valor; frecuencia de contacto por segmento; retención por segmento con CS; satisfacción de clientes de alto valor; NPS por nivel de servicio.
**Diagnostic_Questions:** ¿Diferenciamos el servicio de CS por valor del cliente? ¿Los clientes estratégicos tienen atención especial? ¿Los recursos CS están bien asignados? ¿Hay niveles de servicio definidos? ¿Los clientes top están satisfechos con CS?
**Recommended_Actions:** Segmentar clientes por valor y potencial; definir niveles de servicio (auto-servicio, digital, CSM compartido, CSM dedicado); asignar recursos según segmento; crear programa de clientes estratégicos; medir satisfacción por nivel.
**Severity_Level:** High
**Related_Patterns:** CUS-019, CUS-044, CUS-046, CUS-065, CUS-083

### CUS-049
**Pattern_Name:** Customer Success Sin Métricas de Salud
**Category:** Customer Success
**Description:** El equipo de customer success no utiliza un sistema de health score para priorizar clientes en riesgo, por lo que las intervenciones son reactivas y no focalizadas.
**Observable_Symptoms:** CSM no tiene visibilidad de la salud de sus clientes; no hay alertas de riesgo; se actúa cuando el cliente ya está insatisfecho; no hay criterios objetivos para priorizar; intervenciones tardías.
**Early_Warning_Signals:** Sin health score implementado; CSM no tiene dashboard de salud; % de intervenciones basadas en health score = 0; clientes en riesgo no identificados antes de churn; % de churn sorpresa > 40%.
**Typical_Causes:** Falta de herramienta de health score; datos de cliente no integrados; desconocimiento de mejores prácticas; cultura reactiva; recursos limitados para implementar.
**Business_Impact:** Intervenciones tardías; clientes que podrían salvarse se pierden; esfuerzos de CS no focalizados; eficiencia de CS baja; churn evitable no prevenido.
**Metrics_To_Check:** Health score implementado; % de clientes con health score activo; precisión predictiva; % de churn sorpresa; tiempo entre alerta e intervención.
**Diagnostic_Questions:** ¿El equipo CS tiene health score de clientes? ¿Pueden identificar clientes en riesgo? ¿Las intervenciones son basadas en datos? ¿El health score es preciso? ¿Reducimos churn con health score?
**Recommended_Actions:** Implementar customer health score (uso, satisfacción, engagement, reclamos, pago); integrar datos en dashboard de CSM; definir umbrales de riesgo y alertas; priorizar intervenciones por health score; medir precisión predictiva.
**Severity_Level:** High
**Related_Patterns:** CUS-005, CUS-017, CUS-046, CUS-047, CUS-056

### CUS-050
**Pattern_Name:** Customer Success Sin Proceso de Renovación
**Category:** Customer Success
**Description:** El proceso de renovación de contratos no está gestionado por customer success, dejando la renovación al azar y resultando en pérdidas evitables de clientes.
**Observable_Symptoms:** No hay proceso de renovación anticipado; cliente no es contactado antes del vencimiento; la renovación depende del cliente; se descubre que el cliente no renovará cuando ya es tarde; no hay gestión del ciclo de renovación.
**Early_Warning_Signals:** Sin proceso de renovación documentado; % de clientes contactados 90 días antes de renovación < 30%; renovación gestionada reactivamente; % de renovaciones no gestionadas > 40%; churn en renovación alto.
**Typical_Causes:** Falta de proceso de renovación; cultura de "el cliente renovará solo"; CS no involucrado en renovaciones; equipo comercial enfocado en nuevos clientes; CRM no configurado para alertas de renovación.
**Business_Impact:** Clientes que podrían renovar no lo hacen por falta de gestión; ingresos recurrentes en riesgo; churn por inacción; LTV no realizado; inestabilidad en ingresos.
**Metrics_To_Check:** % de renovaciones gestionadas; % de clientes contactados pre-renovación; tasa de renovación con gestión vs sin; anticipación de contacto; churn en renovación.
**Diagnostic_Questions:** ¿Gestionamos activamente las renovaciones? ¿Contactamos clientes antes del vencimiento? ¿CS participa en renovaciones? ¿Las renovaciones son automáticas o gestionadas? ¿Perdemos clientes por falta de gestión?
**Recommended_Actions:** Establecer proceso de renovación anticipado (90-60-30 días); asignar responsable de renovaciones; configurar alertas en CRM; contactar clientes con valor demostrado; medir tasa de renovación.
**Severity_Level:** High
**Related_Patterns:** CUS-007, CUS-010, CUS-044, CUS-046, CUS-054

### CUS-051
**Pattern_Name:** Customer Success Sin Expansión (Upsell/Cross-sell)
**Category:** Customer Success
**Description:** El equipo de customer success no identifica ni aprovecha oportunidades de expansión en la cartera existente, perdiendo ingresos incrementales que clientes satisfechos estarían dispuestos a comprar.
**Observable_Symptoms:** CSM no tiene metas de expansión; no se identifican necesidades adicionales del cliente; no hay revisión periódica de oportunidades de upselling; clientes compran más productos sin ser ofrecidos; ingresos de clientes existentes planos.
**Early_Warning_Signals:** % de ingresos de expansión sobre base < 10%; CSM sin metas de upselling; sin revisión de oportunidades en cartera; clientes satisfechos no expandidos; tasa de adopción de nuevos productos baja.
**Typical_Causes:** CSM enfocado solo en retención; falta de incentivos de expansión; desconocimiento de necesidades del cliente; cultura de no "vender" a clientes existentes; productos adicionales no desarrollados.
**Business_Impact:** Ingresos por cliente no maximizados; LTV por debajo del potencial; oportunidad de crecimiento rentable (bajo CAC) perdida; cliente satisfecho compra a competidores productos complementarios.
**Metrics_To_Check:** % de ingresos por expansión; tasa de upselling en cartera; ingresos por cliente en el tiempo; LTV; satisfacción de clientes que expandieron.
**Diagnostic_Questions:** ¿CSM identifica oportunidades de expansión? ¿Hay metas de upselling para CS? ¿Los clientes satisfechos compran más? ¿Revisamos periódicamente oportunidades? ¿Perdemos ingresos por no ofrecer más?
**Recommended_Actions:** Incorporar metas de expansión en CS; entrenar CSM en identificación de oportunidades; revisar cartera periódicamente; coordinar con equipo comercial para upselling; medir ingresos por expansión.
**Severity_Level:** High
**Related_Patterns:** CUS-044, CUS-046, CUS-054, CUS-065, CUS-066

### CUS-052
**Pattern_Name:** Customer Success Sin Herramientas de Automatización
**Category:** Customer Success
**Description:** El equipo de customer success opera sin herramientas de automatización, realizando tareas manuales repetitivas que limitan su capacidad de ser proactivos y escalar.
**Observable_Symptoms:** CSM envía emails manualmente; tareas repetitivas consumen tiempo; no hay automatización de check-ins; seguimientos manuales; CSM dedica tiempo a administración no a valor.
**Early_Warning_Signals:** Sin herramienta de CS; tareas manuales > 40% del tiempo de CSM; check-ins no automatizados; sin alertas automáticas de salud; sin playbooks de CS; ratio clientes por CSM bajo.
**Typical_Causes:** Falta de inversión en herramientas; cultura de "procesos manuales funcionan"; desconocimiento de herramientas de CS; priorización de otras inversiones; equipo pequeño.
**Business_Impact:** CSM ineficientes; tiempo dedicado a tareas administrativas no a clientes; escalabilidad limitada; clientes no reciben atención oportuna; CS no puede ser proactivo; retención subóptima.
**Metrics_To_Check:** % de tiempo de CSM en tareas de valor vs administrativas; herramientas de CS implementadas; ratio clientes por CSM; automatización de check-ins; NPS de clientes con CS automatizado.
**Diagnostic_Questions:** ¿El equipo CS tiene herramientas adecuadas? ¿Automatizan tareas repetitivas? ¿El tiempo de CSM se usa en valor? ¿Pueden escalar? ¿La falta de herramientas limita la proactividad?
**Recommended_Actions:** Implementar herramientas de CS (Gainsight, Totango, ChurnZero, o planillas avanzadas); automatizar check-ins, alertas y reportes; crear playbooks de CS; liberar tiempo de CSM para valor; medir eficiencia.
**Severity_Level:** Medium
**Related_Patterns:** CUS-005, CUS-046, CUS-049, CUS-050

### CUS-053
**Pattern_Name:** Customer Success Sin Métricas de Desempeño
**Category:** Customer Success
**Description:** El equipo de customer success no tiene KPIS claros de desempeño, por lo que no se mide su impacto en retención, expansión o satisfacción del cliente.
**Observable_Symptoms:** CSM no tiene metas claras; no se mide su efectividad; el impacto de CS en el negocio es desconocido; no hay reportes de desempeño; decisiones sobre CS sin datos.
**Early_Warning_Signals:** Sin KPIs de CS definidos; CSM sin metas individuales; % de actividades de CS medidas < 30%; retención atribuible a CS desconocida; sin reportes de desempeño de CS.
**Typical_Causes:** Falta de definición de rol de CS; cultura de "CS no se mide"; desconocimiento de KPIs de CS; recursos limitados para reporting; liderazgo no exige métricas.
**Business_Impact:** Imposibilidad de evaluar efectividad de CS; recursos de CS no optimizados; CSM sin dirección; retención no atribuible; justificación de inversión en CS difícil.
**Metrics_To_Check:** (Deberían medirse) retención de clientes con CS; NPS de clientes con CS; tasa de expansión; % de clientes saludables; tiempo de respuesta; satisfacción con CS.
**Diagnostic_Questions:** ¿El equipo CS tiene KPIs claros? ¿Medimos su impacto en retención? ¿Sabemos si CS es efectivo? ¿Los CSM tienen metas? ¿Podemos justificar la inversión en CS?
**Recommended_Actions:** Definir KPIs de CS (retención, NPS, expansión, health score, tiempo de respuesta); establecer metas individuales; crear dashboard de desempeño; reportar impacto periódicamente; vincular compensación a KPIs.
**Severity_Level:** High
**Related_Patterns:** CUS-044, CUS-046, CUS-048, CUS-051, CUS-066

### CUS-054
**Pattern_Name:** Customer Experience Sin Mapeo de Journey
**Category:** Customer Experience
**Description:** La empresa no ha mapeado el customer journey, por lo que no entiende la experiencia del cliente en cada punto de contacto, las emociones que genera ni las oportunidades de mejora.
**Observable_Symptoms:** No hay mapa del customer journey; se desconocen los puntos de contacto del cliente; las emociones del cliente en cada etapa no se entienden; decisiones sobre experiencia sin base; momentos críticos no identificados.
**Early_Warning_Signals:** Sin customer journey map; % de puntos de contacto identificados < 30%; sin investigación de experiencia del cliente; decisiones de CX sin datos; momentos de verdad no conocidos.
**Typical_Causes:** Desconocimiento de la herramienta; falta de recursos; cultura de "conocemos al cliente"; priorización de otras actividades; falta de metodología de CX.
**Business_Impact:** Experiencia del cliente no gestionada; puntos de dolor no identificados; inversión en CX sin dirección; oportunidades de mejora perdidas; cliente insatisfecho sin entender por qué.
**Metrics_To_Check:** Customer journey map creado; puntos de contacto identificados; satisfacción por punto de contacto; momentos de verdad conocidos; mejoras implementadas por touchpoint.
**Diagnostic_Questions:** ¿Tenemos mapeado el customer journey? ¿Entendemos la experiencia del cliente en cada punto de contacto? ¿Conocemos los momentos de verdad? ¿Identificamos puntos de dolor? ¿Tomamos decisiones basadas en el journey?
**Recommended_Actions:** Realizar mapeo del customer journey (estado actual); identificar puntos de contacto y momentos de verdad; medir satisfacción por touchpoint; priorizar mejoras de alto impacto; actualizar journey periódicamente.
**Severity_Level:** Critical
**Related_Patterns:** CUS-002, CUS-008, CUS-020, CUS-028, CUS-055, CUS-056

### CUS-055
**Pattern_Name:** Customer Experience Fragmentada entre Canales
**Category:** Customer Experience
**Description:** La experiencia del cliente es inconsistente entre canales (web, teléfono, presencial, email), generando frustración por tener que repetir información y sentir que cada canal es una empresa diferente.
**Observable_Symptoms:** Cliente tiene que repetir su historia en cada canal; información no fluye entre canales; la experiencia en un canal no refleja la de otro; el cliente siente que habla con empresas diferentes; la transición entre canales es abrupta.
**Early_Warning_Signals:** % de clientes que reportan consistencia entre canales < 40%; cliente repite información > 1 vez; sin integración de canales; NPS por canal varía > 20 puntos; quejas sobre tener que repetir.
**Typical_Causes:** Canales gestionados en silos; sistemas no integrados; falta de visión omnicanal; cultura departamental; inversión fragmentada en canales.
**Business_Impact:** Experiencia frustrante para el cliente; percepción de poca profesionalidad; cliente insatisfecho; churn por mala experiencia; recomendación negativa; eficiencia operativa baja.
**Metrics_To_Check:** % de clientes con experiencia omnicanal consistente; NPS por canal; % de información compartida entre canales; tasa de repetición de información; satisfacción con transiciones.
**Diagnostic_Questions:** ¿La experiencia es consistente entre canales? ¿El cliente tiene que repetir información? ¿Los sistemas están integrados? ¿La transición entre canales es fluida? ¿Hay visión omnicanal?
**Recommended_Actions:** Implementar estrategia omnicanal; integrar sistemas y datos entre canales; asegurar continuidad de información; entrenar al equipo en visión omnicanal; medir consistencia de experiencia.
**Severity_Level:** High
**Related_Patterns:** CUS-008, CUS-018, CUS-028, CUS-043, CUS-054, CUS-057


### CUS-056
**Pattern_Name:** Customer Experience Sin Medición
**Category:** Customer Experience
**Description:** La empresa no mide la experiencia del cliente de manera sistemática (encuestas, CSAT, CES), por lo que no tiene datos objetivos para mejorarla ni sabe si está empeorando.
**Observable_Symptoms:** No hay encuestas de satisfacción post-interacción; no se mide CSAT o CES; la experiencia se evalúa subjetivamente; no hay datos de satisfacción por punto de contacto; mejoras basadas en corazonadas.
**Early_Warning_Signals:** Sin sistema de medición de CX; frecuencia de medición < trimestral; % de puntos de contacto medidos < 20%; CSAT/CES no implementados; decisiones de CX sin datos.
**Typical_Causes:** Falta de recursos para medición; desconocimiento de métricas de CX; cultura de "sentimos" al cliente; herramientas limitadas; priorización de otras métricas.
**Business_Impact:** Imposibilidad de mejorar lo que no se mide; puntos de dolor no detectados; experiencia empeora sin saberlo; inversión en CX sin dirección; cliente insatisfecho no identificado.
**Metrics_To_Check:** (Deberían medirse) CSAT por touchpoint; CES (Customer Effort Score); NPS transaccional; tasa de resolución en primer contacto; satisfacción post-interacción.
**Diagnostic_Questions:** ¿Medimos la experiencia del cliente sistemáticamente? ¿Tenemos CSAT o CES? ¿Sabemos cómo es la experiencia en cada punto de contacto? ¿Los datos de CX guían decisiones? ¿La experiencia mejora con el tiempo?
**Recommended_Actions:** Implementar medición sistemática de CX (CSAT post-interacción, CES); medir satisfacción en cada punto de contacto; crear dashboard de CX; establecer metas de mejora; cerrar el ciclo con clientes.
**Severity_Level:** Critical
**Related_Patterns:** CUS-005, CUS-020, CUS-028, CUS-054, CUS-055

### CUS-057
**Pattern_Name:** Customer Experience Sin Voz del Cliente
**Category:** Customer Experience
**Description:** La empresa no tiene un programa estructurado de "voz del cliente" (VoC) que capture, analice y actúe sobre el feedback del cliente de manera continua.
**Observable_Symptoms:** No hay canales estructurados de feedback; las opiniones del cliente no se capturan sistemáticamente; el feedback que llega no se centraliza ni analiza; las decisiones no incorporan la voz del cliente; clientes sienten que no son escuchados.
**Early_Warning_Signals:** Sin programa VoC; % de feedback capturado < 20% del total; feedback no centralizado; sin análisis de tendencias de feedback; decisiones sin input del cliente.
**Typical_Causes:** Desconocimiento de VoC; falta de herramientas; cultura de "nosotros sabemos lo que el cliente quiere"; recursos limitados; miedo al feedback negativo.
**Business_Impact:** Cliente no escuchado; oportunidades de mejora perdidas; decisiones sin perspectiva del cliente; insatisfacción no detectada; churn evitable; innovación sin base de cliente.
**Metrics_To_Check:** Programa VoC implementado; % de clientes que proveen feedback; % de feedback analizado; acciones implementadas basadas en VoC; satisfacción con ser escuchado.
**Diagnostic_Questions:** ¿Tenemos un programa de voz del cliente? ¿Capturamos feedback sistemáticamente? ¿Lo analizamos y actuamos? ¿Los clientes sienten que los escuchamos? ¿Las decisiones incorporan la voz del cliente?
**Recommended_Actions:** Implementar programa VoC (encuestas, entrevistas, análisis de reclamos, redes sociales, reseñas); centralizar feedback; analizar tendencias; cerrar el ciclo con clientes; incorporar VoC en decisiones estratégicas.
**Severity_Level:** High
**Related_Patterns:** CUS-020, CUS-028, CUS-034, CUS-054, CUS-056

### CUS-058
**Pattern_Name:** Customer Experience con Puntos de Dolor No Resueltos
**Category:** Customer Experience
**Description:** Existen puntos de dolor conocidos en la experiencia del cliente que la empresa no resuelve, ya sea por falta de recursos, voluntad o priorización, acumulando insatisfacción.
**Observable_Symptoms:** El equipo sabe qué puntos de dolor existen pero no se resuelven; los mismos problemas se repiten; clientes mencionan las mismas frustraciones; hay "parches" pero no soluciones definitivas; la experiencia no mejora.
**Early_Warning_Signals:** Puntos de dolor identificados pero no resueltos > 6 meses; % de puntos de dolor resueltos < 30%; clientes mencionan los mismos problemas recurrentemente; NPS de clientes que experimentan el punto de dolor es muy bajo; equipo normaliza el problema.
**Typical_Causes:** Falta de recursos para resolver; cultura de "siempre fue así"; baja priorización de CX; problemas crónicos normalizados; falta de accountability.
**Business_Impact:** Insatisfacción recurrente; churn por problemas no resueltos; clientes frustrados; reputación dañada; equipo desmotivado por no resolver; competitividad disminuida.
**Metrics_To_Check:** Puntos de dolor identificados; tiempo promedio sin resolver; % resueltos; impacto en NPS; % de clientes afectados por punto de dolor no resuelto.
**Diagnostic_Questions:** ¿Conocemos los puntos de dolor en la experiencia del cliente? ¿Hemos resuelto los más importantes? ¿Cuánto tiempo llevan sin resolverse? ¿Por qué no se han resuelto? ¿Cuál es el impacto en el negocio?
**Recommended_Actions:** Listar puntos de dolor conocidos; priorizar por impacto y esfuerzo; asignar responsables y recursos; establecer fechas límite de resolución; medir satisfacción post-resolución; evitar nuevos puntos de dolor.
**Severity_Level:** High
**Related_Patterns:** CUS-008, CUS-028, CUS-054, CUS-056, CUS-057

### CUS-059
**Pattern_Name:** Customer Experience Sin Personalización
**Category:** Customer Experience
**Description:** La experiencia del cliente es genérica y estandarizada, sin reconocer las preferencias, historia o necesidades individuales del cliente, resultando en una sensación de trato impersonal.
**Observable_Symptoms:** Todos los clientes reciben la misma experiencia; el equipo no conoce la historia del cliente; las comunicaciones son genéricas; el cliente siente que es "un número más"; no hay reconocimiento de preferencias.
**Early_Warning_Signals:** % de personalización en CX < 20%; clientes reportan trato impersonal; comunicaciones genéricas sin segmentar; sistema no reconoce al cliente recurrente; NPS bajo en experiencia.
**Typical_Causes:** Falta de datos de cliente; sistemas no integrados; cultura de procesos estandarizados; recursos limitados; desconocimiento de técnicas de personalización.
**Business_Impact:** Cliente no se siente valorado; experiencia commodity; menor lealtad; competidores con personalización ganan; LTV menor; cliente no desarrolla conexión emocional.
**Metrics_To_Check:** % de interacciones personalizadas; satisfacción con personalización; NPS de clientes con experiencia personalizada vs genérica; tasa de recompra; datos de cliente disponibles para personalización.
**Diagnostic_Questions:** ¿Personalizamos la experiencia del cliente? ¿Reconocemos al cliente cuando regresa? ¿Las comunicaciones son personalizadas? ¿El cliente siente trato individual? ¿Tenemos datos para personalizar?
**Recommended_Actions:** Implementar CRM con historial del cliente; usar datos para personalizar interacciones; entrenar al equipo en atención personalizada; segmentar comunicaciones; medir satisfacción con personalización.
**Severity_Level:** High
**Related_Patterns:** CUS-018, CUS-043, CUS-054, CUS-055, CUS-074

### CUS-060
**Pattern_Name:** Customer Experience con Momentos de Verdad Descuidados
**Category:** Customer Experience
**Description:** Los momentos críticos de la experiencia del cliente (primer uso, renovación, resolución de problema) no reciben atención especial, perdiendo oportunidades clave de generar satisfacción y lealtad.
**Observable_Symptoms:** Momentos importantes del ciclo del cliente no tienen procesos especiales; la primera experiencia es genérica; la renovación es un trámite; la resolución de problemas no tiene seguimiento; los hitos del cliente no se celebran.
**Early_Warning_Signals:** % de momentos de verdad con proceso definido < 30%; satisfacción en momentos críticos baja; sin celebración de hitos; NPS en transiciones bajo; procesos genéricos para todo el ciclo.
**Typical_Causes:** Desconocimiento de momentos de verdad; falta de diseño de experiencia; cultura de procesos uniformes; recursos limitados; falta de empatía con el cliente.
**Business_Impact:** Oportunidades de generar lealtad perdidas; momentos críticos son experiencias mediocres; cliente no desarrolla conexión; churn en transiciones; LTV no maximizado.
**Metrics_To_Check:** % de momentos de verdad con diseño; satisfacción por momento crítico; NPS en transiciones; tasa de éxito en momentos clave; correlación momentos-LTV.
**Diagnostic_Questions:** ¿Identificamos los momentos de verdad del cliente? ¿Diseñamos experiencias especiales para ellos? ¿Los hitos del cliente se celebran? ¿Las transiciones son gestionadas? ¿Aprovechamos los momentos clave para generar lealtad?
**Recommended_Actions:** Identificar momentos de verdad en el customer journey; diseñar experiencias especiales para cada uno; asignar recursos a momentos críticos; medir satisfacción en esos momentos; celebrar hitos del cliente.
**Severity_Level:** High
**Related_Patterns:** CUS-002, CUS-007, CUS-028, CUS-047, CUS-054

### CUS-061
**Pattern_Name:** Customer Experience Sin Cultura de Servicio
**Category:** Customer Experience
**Description:** La organización no tiene una cultura centrada en el cliente; los empleados no priorizan la satisfacción del cliente, los procesos no están diseñados para servir y el cliente siente que "molesta".
**Observable_Symptoms:** Empleados no priorizan al cliente; procesos diseñados para la empresa no para el cliente; cliente siente que es una molestia; las políticas priorizan la eficiencia interna sobre la experiencia; el equipo no está motivado para servir.
**Early_Warning_Signals:** Employee NPS bajo; % de empleados que priorizan al cliente < 40%; procesos diseñados sin considerar al cliente; políticas anti-cliente; satisfacción del cliente correlacionada con employee engagement; rotación alta en roles de atención.
**Typical_Causes:** Liderazgo no modela cultura de servicio; contratación sin filtro de actitud de servicio; entrenamiento insuficiente; procesos diseñados para la empresa; incentivos no alineados con servicio.
**Business_Impact:** Experiencia del cliente deficiente consistentemente; NPS bajo; churn alto; empleados desmotivados; reputación de mal servicio; competitividad dañada.
**Metrics_To_Check:** Employee NPS; % de empleados que priorizan al cliente; satisfacción del cliente vs employee engagement; rotación en atención al cliente; NPS.
**Diagnostic_Questions:** ¿Hay cultura de servicio al cliente? ¿Los empleados priorizan al cliente? ¿Los procesos están diseñados para servir o para la empresa? ¿El liderazgo modela la cultura? ¿Los incentivos refuerzan el servicio?
**Recommended_Actions:** Definir y comunicar valores de servicio al cliente; contratar por actitud de servicio; entrenar en cultura de servicio; diseñar procesos centrados en el cliente; alinear incentivos con satisfacción del cliente; reconocer y celebrar servicio excepcional.
**Severity_Level:** Critical
**Related_Patterns:** CUS-008, CUS-028, CUS-054, CUS-055, CUS-056

### CUS-062
**Pattern_Name:** Customer Experience Sin Innovación
**Category:** Customer Experience
**Description:** La experiencia del cliente no evoluciona; se mantienen los mismos procesos, canales y prácticas año tras año, mientras competidores mejoran la experiencia y el cliente espera más.
**Observable_Symptoms:** La experiencia no ha cambiado en años; competidores ofrecen mejores experiencias; clientes mencionan "fulano tiene esto y ustedes no"; no hay iniciativas de innovación en CX; el equipo dice "siempre lo hicimos así".
**Early_Warning_Signals:** Tiempo desde última innovación en CX > 2 años; % de presupuesto invertido en innovación de CX < 5%; comparación con competidores desfavorable en experiencia; clientes piden funcionalidades o canales que no existen; NPS relativo estancado.
**Typical_Causes:** Falta de inversión en CX; cultura de "no arreglar lo que funciona"; desconocimiento de tendencias de CX; falta de recursos o habilidades; priorización de producto sobre experiencia.
**Business_Impact:** Experiencia obsoleta; clientes migran a competidores con mejor experiencia; marca percibida como anticuada; crecimiento limitado por experiencia; LTV menor.
**Metrics_To_Check:** Tiempo desde última innovación en CX; % de presupuesto en innovación CX; comparación con competidores; satisfacción con modernidad de la experiencia; NPS relativo.
**Diagnostic_Questions:** ¿Cuándo fue la última mejora significativa en la experiencia? ¿Nuestra experiencia es moderna o anticuada? ¿Competidores ofrecen mejor experiencia? ¿Invertimos en innovación de CX? ¿Los clientes piden mejoras?
**Recommended_Actions:** Investigar tendencias de CX en el sector; realizar benchmark de experiencia contra competidores; asignar presupuesto a innovación de CX; implementar mejoras de experiencia continuas; medir percepción de modernidad.
**Severity_Level:** Medium
**Related_Patterns:** CUS-008, CUS-054, CUS-055, CUS-057, CUS-060

### CUS-063
**Pattern_Name:** Customer Experience con Alta Fricción
**Category:** Customer Experience
**Description:** El cliente enfrenta demasiados obstáculos, pasos y esfuerzos para hacer negocios con la empresa, resultando en una experiencia de alta fricción que desalienta la compra y la recompra.
**Observable_Symptoms:** Procesos complicados para el cliente; múltiples pasos para completar una acción; formularios largos; información difícil de encontrar; el cliente tiene que hacer mucho esfuerzo; tasas de abandono altas en procesos.
**Early_Warning_Signals:** Customer Effort Score (CES) alto (> 3/5); tasa de abandono en procesos > 40%; % de clientes que completan proceso vs inician < 50%; clientes reportan "es muy complicado"; quejas sobre procesos engorrosos.
**Typical_Causes:** Procesos diseñados para la empresa no para el cliente; falta de simplificación; sistemas legados; cultura burocrática; falta de diseño centrado en el usuario.
**Business_Impact:** Clientes abandonan procesos; tasa de conversión baja; churn por fricción; clientes evitan interactuar; reputación de "complicado"; competidores con menor fricción ganan.
**Metrics_To_Check:** Customer Effort Score; tasa de abandono en procesos; tiempo para completar acciones clave; % de clientes que completan procesos; satisfacción con facilidad de hacer negocios.
**Diagnostic_Questions:** ¿Es fácil hacer negocios con nosotros? ¿Cuánto esfuerzo tiene que hacer el cliente? ¿Los procesos son simples o complicados? ¿Los clientes abandonan procesos? ¿Medimos el esfuerzo del cliente?
**Recommended_Actions:** Mapear procesos del cliente e identificar fricciones; simplificar procesos; reducir pasos; implementar diseño centrado en el cliente; medir Customer Effort Score; eliminar obstáculos identificados.
**Severity_Level:** High
**Related_Patterns:** CUS-045, CUS-054, CUS-055, CUS-058, CUS-060

### CUS-064
**Pattern_Name:** Customer Experience Sin Alineación con Marca
**Category:** Customer Experience
**Description:** La experiencia del cliente no refleja la promesa de marca; la marca promete una cosa y la experiencia entrega otra, generando brecha de credibilidad.
**Observable_Symptoms:** La marca promete excelencia y la experiencia es mediocre; los valores de marca no se viven en la interacción; el cliente nota la desconexión entre lo que se dice y lo que se hace; la experiencia no construye la marca; el branding y la operación están desconectados.
**Early_Warning_Signals:** Diferencia entre promesa de marca y experiencia real; % de interacciones que reflejan valores de marca < 40%; clientes notan brecha; reseñas mencionan "dicen una cosa y hacen otra"; NPS de clientes que notan la brecha es mucho menor.
**Typical_Causes:** Marca definida por marketing sin input de operaciones; experiencia diseñada sin considerar marca; cultura de "marca es marketing"; ejecución no capacitada en valores de marca; falta de alineación estratégica.
**Business_Impact:** Credibilidad de marca dañada; cliente desconfía; promesa de marca no se cumple; posicionamiento no se sostiene; inversión en marca desperdiciada; cliente elige marcas que cumplen.
**Metrics_To_Check:** Consistencia entre promesa de marca y experiencia; % de interacciones alineadas con marca; percepción de credibilidad; NPS de clientes que notan alineación vs no; brecha promesa-realidad.
**Diagnostic_Questions:** ¿La experiencia refleja la promesa de marca? ¿El cliente vive los valores de marca en cada interacción? ¿Hay brecha entre lo que prometemos y lo que entregamos? ¿Operaciones conoce los valores de marca? ¿La experiencia construye o daña la marca?
**Recommended_Actions:** Alinear experiencia del cliente con promesa de marca; diseñar puntos de contacto que reflejen valores; entrenar a toda la organización en marca; medir consistencia; corregir brechas.
**Severity_Level:** High
**Related_Patterns:** MKT-003, MKT-014, CUS-054, CUS-055, CUS-061


## Lifetime Value

### CUS-065
**Pattern_Name:** LTV No Calculado
**Category:** Lifetime Value
**Description:** La empresa no calcula el valor de vida del cliente (LTV), por lo que no sabe cuánto puede invertir en adquirir un cliente ni si sus clientes son rentables a largo plazo.
**Observable_Symptoms:** No hay métrica de LTV; decisiones de inversión en adquisición sin base; no se sabe si los clientes son rentables; se invierte igual en todos los clientes; no hay diferenciación por valor del cliente.
**Early_Warning_Signals:** LTV no calculado; % de decisiones basadas en LTV = 0; CAC no contrastado con LTV; clientes no segmentados por valor; rentabilidad por cliente desconocida.
**Typical_Causes:** Desconocimiento de la métrica; falta de datos históricos; complejidad percibida; cultura de "medir ingresos totales"; falta de herramientas analíticas.
**Business_Impact:** Inversión en adquisición sin límite; CAC puede exceder LTV sin saberlo; clientes no rentables no identificados; rentabilidad global desconocida; decisiones sin base de valor del cliente.
**Metrics_To_Check:** (Deberían calcularse) LTV por cliente y segmento; ratio CAC/LTV; tiempo de payback; margen por cliente; rentabilidad por cliente.
**Diagnostic_Questions:** ¿Calculamos el LTV? ¿Sabemos cuánto vale un cliente a largo plazo? ¿Comparamos CAC con LTV? ¿Sabemos qué clientes son rentables? ¿Diferenciamos inversión por valor del cliente?
**Recommended_Actions:** Implementar cálculo de LTV (ingresos promedio x frecuencia x vida útil x margen); segmentar clientes por LTV; usar LTV para decisiones de inversión en adquisición; monitorear LTV por segmento; incorporar LTV en reporting.
**Severity_Level:** Critical
**Related_Patterns:** CUS-006, CUS-010, CUS-020, CUS-066, CUS-074, CUS-083

### CUS-066
**Pattern_Name:** LTV Decreciente en el Tiempo
**Category:** Lifetime Value
**Description:** El LTV de los clientes está disminuyendo con el tiempo, indicando que los clientes nuevos valen menos que los antiguos, ya sea por menor retención, menor ticket o menor margen.
**Observable_Symptoms:** Clientes nuevos compran menos que los antiguos; la retención de clientes nuevos es menor; los márgenes se comprimen en nuevas ventas; el LTV de cohortes recientes es menor; la tendencia de LTV es negativa.
**Early_Warning_Signals:** LTV por cohorte decreciente; retención de clientes nuevos menor que antiguos; ticket promedio de clientes nuevos menor; margen de clientes nuevos más bajo; tendencia de LTV negativa por 3+ cohortes.
**Typical_Causes:** Clientes nuevos de menor calidad; canales de adquisición atraen clientes de menor valor; producto/servicio se commoditiza; precios a la baja para atraer; competidores erosionan valor.
**Business_Impact:** Rentabilidad futura menor; necesidad de más clientes para mismo ingreso; CAC no se recupera; inversión en adquisición menos eficiente; negocio menos sostenible.
**Metrics_To_Check:** LTV por cohorte (trimestral); tendencia de LTV; retención por cohorte; ticket promedio por cohorte; margen por cohorte.
**Diagnostic_Questions:** ¿El LTV de clientes nuevos es menor que el de antiguos? ¿La retención de clientes nuevos empeora? ¿El ticket de clientes nuevos baja? ¿Los márgenes se comprimen? ¿Las cohortes recientes son menos valiosas?
**Recommended_Actions:** Analizar LTV por cohorte sistemáticamente; identificar causas de decrecimiento; ajustar canales de adquisición para atraer mejor perfil; mejorar onboarding y retención de nuevos clientes; revisar estrategia de precios.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-006, CUS-010, CUS-065, CUS-074

### CUS-067
**Pattern_Name:** LTV No Segmentado
**Category:** Lifetime Value
**Description:** La empresa calcula el LTV promedio pero no desglosa por segmento, ocultando grandes diferencias entre clientes de alto y bajo valor y limitando la capacidad de focalizar recursos.
**Observable_Symptoms:** LTV promedio único; no se sabe qué segmentos son más valiosos; clientes de alto y bajo valor se mezclan en el promedio; decisiones uniformes para todos; segmentos valiosos no identificados.
**Early_Warning_Signals:** LTV solo calculado a nivel global; sin LTV por segmento; diferencia de LTV entre segmentos > 3x; % de clientes de bajo LTV significativo; acciones de marketing y retención no diferenciadas.
**Typical_Causes:** Falta de segmentación en análisis; datos no desglosados; cultura de promedios; herramientas analíticas limitadas; desconocimiento de variabilidad.
**Business_Impact:** Recursos mal asignados; segmentos de alto valor infra-atendidos; segmentos de bajo valor sobre-invertidos; rentabilidad subóptima; decisiones basadas en promedio engañoso.
**Metrics_To_Check:** LTV por segmento; diferencia entre segmentos; % de clientes por rango de LTV; recursos asignados por LTV; rentabilidad por segmento.
**Diagnostic_Questions:** ¿Desglosamos LTV por segmento? ¿Hay grandes diferencias entre segmentos? ¿El promedio es engañoso? ¿Sabemos qué segmentos son más valiosos? ¿Asignamos recursos según LTV?
**Recommended_Actions:** Calcular LTV por segmento (industria, tamaño, producto, canal); identificar segmentos de alto y bajo valor; asignar recursos según LTV; focalizar retención en segmentos de alto valor; desinvertir en segmentos de bajo LTV.
**Severity_Level:** High
**Related_Patterns:** CUS-006, CUS-011, CUS-065, CUS-074, CUS-083

### CUS-068
**Pattern_Name:** LTV Bajo por Baja Frecuencia de Compra
**Category:** Lifetime Value
**Description:** El LTV es bajo porque los clientes compran con poca frecuencia, indicando que no hay incentivos para la recompra ni estrategia de recurrencia.
**Observable_Symptoms:** Clientes compran una vez y no regresan; tiempo entre compras largo; no hay recompra natural; sin programa de recurrencia; el negocio depende de clientes nuevos.
**Early_Warning_Signals:** Frecuencia de compra promedio < 2 veces al año; % de clientes que recompran < 30%; tiempo entre compras > 12 meses; ingresos de clientes recurrentes < 30% del total; LTV bajo vs adquisición.
**Typical_Causes:** Producto/servicio de baja recurrencia natural; falta de estrategia de recompra; sin programa de fidelización; no hay upselling post-venta; relación transaccional.
**Business_Impact:** LTV bajo; necesidad constante de adquirir nuevos clientes; CAC alto en relación al LTV; negocio no genera ingresos recurrentes; crecimiento depende de adquisición.
**Metrics_To_Check:** Frecuencia de compra promedio; % de clientes que recompran; tiempo entre compras; ingresos de clientes recurrentes vs nuevos; LTV.
**Diagnostic_Questions:** ¿Con qué frecuencia compran los clientes? ¿Recompran naturalmente? ¿Hay incentivos para la recompra? ¿El negocio depende de clientes nuevos? ¿Tenemos estrategia de recurrencia?
**Recommended_Actions:** Implementar estrategia de recurrencia (suscripción, programa de fidelización, recordatorios); incentivar la recompra; crear productos/servicios complementarios; medir frecuencia y mejorarla; calcular LTV con y sin recurrencia.
**Severity_Level:** High
**Related_Patterns:** CUS-010, CUS-037, CUS-065, CUS-066, CUS-069

### CUS-069
**Pattern_Name:** LTV Bajo por Bajo Ticket Promedio
**Category:** Lifetime Value
**Description:** El LTV es bajo porque el ticket promedio de compra es pequeño, y la empresa no tiene estrategias de upselling, cross-selling o aumento de precio para incrementarlo.
**Observable_Symptoms:** Clientes compran solo el producto básico; no hay upselling; no se ofrecen versiones premium; precios bajos sin justificación; ticket no crece con el tiempo.
**Early_Warning_Signals:** Ticket promedio bajo vs competidores; % de clientes que compran producto premium < 15%; sin estrategia de upselling; ticket plano en el tiempo; margen bajo.
**Typical_Causes:** Producto/servicio básico sin versiones superiores; falta de estrategia de upselling; miedo a subir precios; equipo no entrenado en venta adicional; propuesta de valor no justifica premium.
**Business_Impact:** LTV menor al potencial; ingresos por cliente bajos; rentabilidad limitada; necesidad de más clientes para mismo ingreso; crecimiento requiere alta adquisición.
**Metrics_To_Check:** Ticket promedio; % de clientes con compra adicional; tendencia de ticket; margen por nivel de producto; LTV por nivel de producto.
**Diagnostic_Questions:** ¿El ticket promedio es bajo? ¿Ofrecemos opciones de mayor valor? ¿Hacemos upselling? ¿Los clientes compran más con el tiempo? ¿Podríamos subir precios?
**Recommended_Actions:** Desarrollar versiones premium o paquetes; implementar estrategia de upselling; entrenar al equipo en venta adicional; revisar precios; medir ticket promedio y mejorarlo.
**Severity_Level:** High
**Related_Patterns:** CUS-037, CUS-051, CUS-065, CUS-068, CUS-070

### CUS-070
**Pattern_Name:** LTV Bajo por Baja Retención
**Category:** Lifetime Value
**Description:** El LTV es bajo porque los clientes no se quedan el tiempo suficiente; la retención es pobre y los clientes se van antes de generar valor suficiente para recuperar la inversión.
**Observable_Symptoms:** Clientes cancelan temprano; vida útil del cliente corta; CAC no se recupera; clientes no alcanzan a generar margen; rotación alta de clientes.
**Early_Warning_Signals:** Vida útil promedio del cliente < 12 meses; ratio CAC/LTV > 1; retención anual < 50%; clientes cancelan antes de recuperar CAC; LTV de clientes que se quedan vs promedio.
**Typical_Causes:** Problemas de retención estructurales; onboarding deficiente; propuesta de valor no sostenible; competidores mejores; falta de customer success.
**Business_Impact:** LTV negativo o muy bajo; negocio no sostenible; necesidad de financiar adquisición constantemente; crecimiento consume caja; rentabilidad por cliente negativa.
**Metrics_To_Check:** Vida útil promedio; retención anual; ratio CAC/LTV; tiempo de payback; % de clientes que alcanzan payback.
**Diagnostic_Questions:** ¿Cuánto tiempo se quedan los clientes? ¿Alcanzan a generar valor para recuperar CAC? ¿La retención es suficiente para un LTV saludable? ¿Los clientes se van antes de ser rentables? ¿El negocio es sostenible?
**Recommended_Actions:** Aumentar retención (mejorar producto, customer success, experiencia); reducir CAC mientras se mejora retención; focalizar en segmentos con mejor retención; calcular payback; monitorear LTV vs CAC.
**Severity_Level:** Critical
**Related_Patterns:** CUS-001, CUS-010, CUS-044, CUS-046, CUS-065, CUS-066

### CUS-071
**Pattern_Name:** LTV sin Estrategia de Expansión
**Category:** Lifetime Value
**Description:** La empresa acepta el LTV actual sin tener una estrategia activa para expandirlo mediante upselling, cross-selling, aumento de precios o mejora de retención.
**Observable_Symptoms:** No hay metas de aumento de LTV; el equipo no trabaja en expansión; no hay iniciativas de upselling; la retención no se gestiona activamente; el LTV es un dato no una meta.
**Early_Warning_Signals:** Sin metas de LTV; % de ingresos de expansión < 10%; sin iniciativas de upselling; retención no gestionada; LTV plano en el tiempo.
**Typical_Causes:** Cultura de "LTV es lo que es"; falta de accountability; desconocimiento de palancas de LTV; enfoque en adquisición; recursos no asignados a expansión.
**Business_Impact:** LTV no maximizado; ingresos por cliente por debajo del potencial; rentabilidad menor; crecimiento requiere más adquisición; valor del negocio menor.
**Metrics_To_Check:** Meta de LTV definida; % de ingresos de expansión; iniciativas de upselling activas; tendencia de LTV; LTV por cohorte mejorando.
**Diagnostic_Questions:** ¿Tenemos metas de aumento de LTV? ¿Trabajamos activamente en expandir el LTV? ¿Hay iniciativas de upselling y retención? ¿El LTV mejora con el tiempo? ¿Sabemos qué palancas mueven el LTV?
**Recommended_Actions:** Establecer metas de LTV; identificar palancas (retención, upselling, precio, frecuencia); implementar iniciativas por palanca; medir progreso; asignar responsables.
**Severity_Level:** High
**Related_Patterns:** CUS-037, CUS-051, CUS-065, CUS-068, CUS-069

### CUS-072
**Pattern_Name:** LTV sin Modelo Predictivo
**Category:** Lifetime Value
**Description:** La empresa calcula el LTV histórico pero no utiliza modelos predictivos para estimar el LTV futuro de clientes nuevos, perdiendo la capacidad de segmentar y priorizar desde el inicio.
**Observable_Symptoms:** LTV solo se conoce después de que el cliente se fue; no se puede predecir el valor futuro de un cliente nuevo; decisiones de adquisición sin estimación de LTV; segmentación de clientes sin predictive LTV; no se priorizan clientes de alto potencial.
**Early_Warning_Signals:** Sin LTV predictivo; decisiones de adquisición sin estimación de LTV; clientes de alto potencial no identificados tempranamente; inversión en adquisición sin filtro de LTV; sin modelo de scoring de LTV.
**Typical_Causes:** Falta de datos históricos; desconocimiento de modelos predictivos; complejidad técnica; recursos analíticos limitados; cultura reactiva.
**Business_Impact:** Imposibilidad de priorizar clientes de alto potencial desde el inicio; inversión en adquisición no optimizada por LTV; clientes de bajo LTV reciben misma inversión que los de alto; ROI de adquisición subóptimo.
**Metrics_To_Check:** Modelo de LTV predictivo implementado; precisión del modelo; % de decisiones basadas en LTV predictivo; diferenciación de inversión por LTV potencial.
**Diagnostic_Questions:** ¿Podemos predecir el LTV de un cliente nuevo? ¿Usamos LTV predictivo para decisiones de adquisición? ¿Identificamos tempranamente clientes de alto potencial? ¿Segmentamos inversión por LTV potencial? ¿Tenemos modelo de scoring?
**Recommended_Actions:** Implementar modelo predictivo de LTV basado en datos históricos; usar LTV predictivo para priorizar canales y segmentos; crear scoring de potencial; ajustar inversión según LTV estimado; validar precisión periódicamente.
**Severity_Level:** Medium
**Related_Patterns:** CUS-065, CUS-066, CUS-067, CUS-074, CUS-083

### CUS-073
**Pattern_Name:** LTV No Comunicado al Negocio
**Category:** Lifetime Value
**Description:** El LTV se calcula pero no se comunica al equipo, por lo que las decisiones operativas no consideran el valor de largo plazo del cliente y se prioriza el corto plazo.
**Observable_Symptoms:** Equipo no conoce el LTV; decisiones se basan en ingresos inmediatos; no se considera el valor futuro del cliente en decisiones de servicio; inversiones se justifican solo con retorno inmediato; cultura de corto plazo.
**Early_Warning_Signals:** % de empleados que conocen el LTV < 20%; LTV no mencionado en reuniones; decisiones sin considerar LTV; KPIs solo de corto plazo; inbound de decisiones contrario a LTV.
**Typical_Causes:** Falta de comunicación; cultura de métricas de corto plazo; desconocimiento del valor de LTV como brújula; liderazgo no lo prioriza; herramientas no lo muestran.
**Business_Impact:** Decisiones que maximizan corto plazo a costa de LTV; inversiones en servicio no justificadas; clientes tratados por transacción no por valor de vida; desalineación estratégica; LTV no mejora.
**Metrics_To_Check:** % de empleados que conocen el LTV; % de decisiones que consideran LTV; tendencia de LTV; inversiones en servicio y retención; balance corto vs largo plazo.
**Diagnostic_Questions:** ¿El equipo conoce el LTV? ¿Las decisiones consideran el valor de largo plazo? ¿La organización piensa en LTV o solo en venta inmediata? ¿El LTV guía decisiones estratégicas? ¿La cultura es de corto o largo plazo?
**Recommended_Actions:** Comunicar LTV a toda la organización; incorporar LTV en reporting y reuniones; usar LTV para justificar inversiones en servicio y retención; alinear KPIs con LTV; celebrar decisiones que mejoran LTV.
**Severity_Level:** Medium
**Related_Patterns:** CUS-044, CUS-065, CUS-066, CUS-071


## Segmentación (Clientes)

### CUS-074
**Pattern_Name:** Sin Segmentación de Clientes
**Category:** Segmentación (Clientes)
**Description:** La empresa no segmenta su base de clientes, tratando a todos por igual independientemente de su valor, comportamiento o necesidades, resultando en estrategias genéricas inefectivas.
**Observable_Symptoms:** Todos los clientes reciben el mismo tratamiento; no hay diferenciación por valor o necesidad; las comunicaciones son genéricas; las estrategias de retención son iguales para todos; no se identifican grupos de clientes.
**Early_Warning_Signals:** Sin segmentación de clientes; % de clientes categorizados < 20%; estrategias únicas para toda la base; sin diferenciación en retención o marketing; recursos asignados uniformemente.
**Typical_Causes:** Falta de datos; herramientas analíticas limitadas; cultura de "todos los clientes son iguales"; desconocimiento de técnicas de segmentación; recursos limitados.
**Business_Impact:** Estrategias inefectivas por ser genéricas; recursos mal asignados; clientes de alto valor no reciben atención especial; clientes de bajo valor consumen recursos; retención y LTV subóptimos.
**Metrics_To_Check:** Segmentación implementada; % de clientes segmentados; estrategias diferenciadas por segmento; recursos asignados por valor; resultados por segmento.
**Diagnostic_Questions:** ¿Segmentamos nuestra base de clientes? ¿Diferenciamos estrategias por segmento? ¿Sabemos qué clientes son más valiosos? ¿Los recursos se asignan según valor del segmento? ¿Las comunicaciones son segmentadas?
**Recommended_Actions:** Implementar segmentación de clientes (por valor, comportamiento, necesidades, industria); definir estrategias diferenciadas por segmento; asignar recursos según valor; personalizar comunicaciones; medir resultados por segmento.
**Severity_Level:** Critical
**Related_Patterns:** CUS-006, CUS-011, CUS-019, CUS-048, CUS-065, CUS-083

### CUS-075
**Pattern_Name:** Segmentación por Valor No Actualizada
**Category:** Segmentación (Clientes)
**Description:** La segmentación de clientes por valor se hizo una vez y no se actualiza, por lo que clientes que cambiaron de valor (crecieron o decrecieron) reciben un tratamiento inadecuado.
**Observable_Symptoms:** Clientes que eran pequeños siguen recibiendo trato de pequeños aunque crecieron; clientes que decrecieron siguen recibiendo trato premium; la segmentación no refleja la realidad actual; clientes notan el desajuste; decisiones basadas en segmentación obsoleta.
**Early_Warning_Signals:** Última actualización de segmentación > 12 meses; % de clientes reclasificados en último año < 10%; clientes cuyo valor cambió significativamente no reclasificados; quejas de clientes sobre trato inadecuado; decisiones basadas en datos desactualizados.
**Typical_Causes:** Falta de proceso de revisión periódica; datos de cliente no actualizados en CRM; cultura de "segmentación es única"; recursos limitados; desconocimiento de cambios en clientes.
**Business_Impact:** Clientes de alto valor no reconocidos; recursos mal asignados; oportunidades de upselling perdidas; clientes infra-atendidos; segmentación irrelevante.
**Metrics_To_Check:** Fecha última actualización; % de clientes reclasificados; precisión de segmentación vs valor actual; cambios en valor de clientes; satisfacción por segmento.
**Diagnostic_Questions:** ¿Cuándo fue la última actualización de segmentación? ¿Clientes que crecieron fueron reclasificados? ¿La segmentación refleja la realidad actual? ¿Hay clientes mal categorizados? ¿Revisamos segmentación periódicamente?
**Recommended_Actions:** Establecer revisión trimestral de segmentación; actualizar segmentos basados en datos recientes; reclasificar clientes cuyo valor cambió; automatizar reclasificación en CRM; medir precisión de segmentación.
**Severity_Level:** High
**Related_Patterns:** CUS-019, CUS-048, CUS-065, CUS-074, CUS-083

### CUS-076
**Pattern_Name:** Segmentación sin Acción Comercial Diferenciada
**Category:** Segmentación (Clientes)
**Description:** La empresa segmenta clientes pero no traduce esa segmentación en acciones comerciales, de servicio o retención diferenciadas, por lo que la segmentación existe solo en papel.
**Observable_Symptoms:** Segmentos definidos pero todos reciben mismo tratamiento; no hay estrategias por segmento; el equipo comercial no ajusta su approach; campañas no segmentadas; segmentación teórica sin ejecución.
**Early_Warning_Signals:** % de segmentos con estrategia definida < 30%; equipo no conoce los segmentos ni cómo actuar; campañas no segmentadas; procesos de atención uniformes; segmentación no operativa.
**Typical_Causes:** Segmentación creada por analytics sin implementación; falta de integración con operaciones; equipos no capacitados; ausencia de playbooks por segmento; cultura de "tratar a todos igual".
**Business_Impact:** Inversión en segmentación desperdiciada; oportunidad de diferenciación perdida; recursos no optimizados; resultados no mejoran; clientes no perciben diferencias.
**Metrics_To_Check:** % de segmentos con estrategia operativa; % de campañas segmentadas; % de equipo que conoce y aplica segmentación; resultados por segmento con vs sin acción.
**Diagnostic_Questions:** ¿La segmentación se traduce en acciones concretas? ¿El equipo sabe cómo tratar cada segmento? ¿Hay estrategias diferenciadas? ¿Las campañas son segmentadas? ¿La segmentación es operativa o teórica?
**Recommended_Actions:** Crear playbooks por segmento; entrenar al equipo en segmentación; implementar campañas segmentadas; diseñar procesos de atención por segmento; medir efectividad de acciones segmentadas.
**Severity_Level:** High
**Related_Patterns:** CUS-019, CUS-048, CUS-074, CUS-075

### CUS-077
**Pattern_Name:** Segmentación sin Automatización en CRM
**Category:** Segmentación (Clientes)
**Description:** La segmentación de clientes existe pero no está configurada en el CRM, por lo que las acciones automáticas (comunicaciones, alertas, workflows) no pueden diferenciarse por segmento.
**Observable_Symptoms:** Segmentos definidos en Excel pero CRM no los refleja; las comunicaciones no se segmentan automáticamente; los workflows no consideran segmento; el equipo ingresa manualmente el segmento; alertas no diferenciadas.
**Early_Warning_Signals:** % de segmentos configurados en CRM < 30%; segmentación manual (Excel); acciones automáticas no segmentadas; workflows genéricos; datos de segmento no disponibles en CRM.
**Typical_Causes:** CRM no configurado para segmentación; falta de integración entre analytics y CRM; recursos técnicos limitados; cultura de procesos manuales; priorización de otras configuraciones.
**Business_Impact:** Automatización no diferenciada; esfuerzo manual para segmentar; errores de segmentación; acciones no oportunas; escalabilidad limitada; segmentación no operativa.
**Metrics_To_Check:** % de segmentos en CRM; % de acciones automatizadas segmentadas; tiempo dedicado a segmentación manual; errores de segmentación; escalabilidad de segmentación.
**Diagnostic_Questions:** ¿Los segmentos están configurados en el CRM? ¿Las comunicaciones se segmentan automáticamente? ¿Los workflows son diferenciados? ¿La segmentación es manual o automática? ¿El CRM soporta segmentación?
**Recommended_Actions:** Configurar segmentos en CRM; automatizar asignación de segmento basada en reglas; crear workflows por segmento; automatizar comunicaciones segmentadas; medir adopción de segmentación en CRM.
**Severity_Level:** Medium
**Related_Patterns:** CUS-074, CUS-075, CUS-076

### CUS-078
**Pattern_Name:** Segmentación Solo por Valor, No por Necesidad
**Category:** Segmentación (Clientes)
**Description:** La empresa segmenta clientes solo por valor económico (LTV, ticket) pero no por necesidades, comportamiento o perfil, perdiendo la oportunidad de personalizar la propuesta de valor.
**Observable_Symptoms:** Segmentación solo en "alto/medio/bajo valor"; no se consideran necesidades diferentes; clientes con mismas necesidades pero diferente valor reciben trato distinto; clientes con mismo valor pero diferentes necesidades reciben trato igual; la personalización es limitada.
**Early_Warning_Signals:** Criterios de segmentación solo financieros; sin segmentación por necesidades o comportamiento; % de clientes con perfil de necesidades conocido < 20%; propuesta de valor no personalizada; satisfacción similar entre segmentos de valor.
**Typical_Causes:** Facilidad de segmentar por valor; falta de investigación de necesidades; datos de comportamiento no capturados; cultura de "valor es lo único que importa"; recursos limitados.
**Business_Impact:** Propuesta de valor no alineada con necesidades; clientes no se sienten comprendidos; personalización limitada; oportunidades de diferenciación perdidas; retención subóptima.
**Metrics_To_Check:** Criterios de segmentación; % de clientes con perfil de necesidades; personalización por segmento; satisfacción por segmento de necesidad; correlación necesidad-retención.
**Diagnostic_Questions:** ¿Segmentamos solo por valor o también por necesidad? ¿Entendemos las necesidades de cada segmento? ¿La propuesta de valor se adapta a cada segmento? ¿Los clientes se sienten comprendidos? ¿Personalizamos por necesidad?
**Recommended_Actions:** Incorporar segmentación por necesidades y comportamiento; investigar necesidades de cada segmento; crear propuestas de valor por necesidad; personalizar comunicación y producto; medir satisfacción por segmento de necesidad.
**Severity_Level:** High
**Related_Patterns:** CUS-039, CUS-059, CUS-074, CUS-076, CUS-079

### CUS-079
**Pattern_Name:** Sobresegmentación de Clientes Sin Acción
**Category:** Segmentación (Clientes)
**Description:** La empresa tiene demasiados segmentos de clientes que no puede gestionar efectivamente, resultando en parálisis estratégica y falta de acción diferenciada.
**Observable_Symptoms:** Decenas de segmentos definidos; la mayoría no tiene acciones específicas; el equipo está abrumado; segmentos se solapan; no hay recursos para atender todos; la complejidad paraliza.
**Early_Warning_Signals:** Número de segmentos > capacidad de gestión (10+); % de segmentos con estrategia activa < 30%; equipo no conoce todos los segmentos; segmentos sin datos suficientes; acciones no diferenciadas a pesar de muchos segmentos.
**Typical_Causes:** Segmentación excesivamente granular; falta de criterios de agrupación; cultura académica sin pragmatismo; falta de priorización; equipos sin capacidad operativa.
**Business_Impact:** Parálisis por análisis; segmentos no accionables; recursos dispersos; segmentos importantes infra-atendidos; complejidad innecesaria; ROI de segmentación bajo.
**Metrics_To_Check:** Número de segmentos; % de segmentos accionables; % con estrategia activa; recursos por segmento; efectividad de segmentación.
**Diagnostic_Questions:** ¿Tenemos demasiados segmentos? ¿Podemos gestionarlos todos? ¿Cada segmento tiene una estrategia? ¿Hay segmentos sin acción? ¿Deberíamos consolidar?
**Recommended_Actions:** Consolidar segmentos similares; priorizar segmentos por valor y potencial; eliminar segmentos no accionables; asegurar que cada segmento tenga presupuesto y plan; medir efectividad por segmento.
**Severity_Level:** Medium
**Related_Patterns:** CUS-048, CUS-074, CUS-076

### CUS-080
**Pattern_Name:** Segmentación sin Integración con Estrategia de Retención
**Category:** Segmentación (Clientes)
**Description:** La segmentación de clientes existe pero no se utiliza para diseñar estrategias de retención diferenciadas, por lo que todos los clientes reciben el mismo esfuerzo de retención independientemente de su segmento.
**Observable_Symptoms:** Estrategias de retención uniformes para toda la base; segmentación no alimenta acciones de retención; clientes de alto y bajo riesgo reciben mismo tratamiento; recursos de retención mal asignados; segmentos no priorizados en retención.
**Early_Warning_Signals:** % de acciones de retención segmentadas < 20%; recursos de retención asignados uniformemente; estrategias de retención genéricas; segmentación no usada en retención; % de clientes en riesgo por segmento desconocido.
**Typical_Causes:** Falta de integración entre segmentación y retención; equipos trabajando en silos; cultura de retención genérica; desconocimiento del valor de segmentar retención; recursos limitados.
**Business_Impact:** Esfuerzos de retención inefectivos; clientes de alto valor en riesgo no identificados; recursos desperdiciados en clientes de bajo valor; retención subóptima; LTV no protegido.
**Metrics_To_Check:** % de acciones de retención segmentadas; recursos de retención por segmento; efectividad de retención por segmento; % de clientes en riesgo por segmento; LTV protegido por segmento.
**Diagnostic_Questions:** ¿Usamos segmentación para diseñar retención? ¿Diferenciamos acciones de retención por segmento? ¿Los clientes de alto valor reciben más esfuerzo de retención? ¿Los recursos de retención se asignan según valor? ¿La segmentación guía la retención?
**Recommended_Actions:** Integrar segmentación con estrategia de retención; diseñar acciones de retención por segmento; asignar más recursos a segmentos de alto valor; monitorear riesgo por segmento; medir efectividad de retención segmentada.
**Severity_Level:** High
**Related_Patterns:** CUS-013, CUS-019, CUS-048, CUS-074, CUS-083

### CUS-081
**Pattern_Name:** Segmentación sin Ciclo de Vida del Cliente
**Category:** Segmentación (Clientes)
**Description:** La segmentación no considera la etapa del ciclo de vida del cliente (nuevo, activo, en riesgo, inactivo), por lo que clientes en diferentes etapas reciben el mismo tratamiento.
**Observable_Symptoms:** Clientes nuevos y antiguos reciben misma comunicación; clientes en riesgo no identificados; clientes inactivos no segmentados; no hay diferenciación por etapa; el ciclo de vida no se gestiona.
**Early_Warning_Signals:** Sin segmentación por ciclo de vida; % de comunicación personalizada por etapa < 20%; clientes en riesgo no identificados por segmentación; clientes inactivos mezclados con activos; sin estrategia por etapa.
**Typical_Causes:** Falta de modelo de ciclo de vida; CRM no configurado para etapas; desconocimiento de lifecycle marketing; cultura de tratar a todos igual; recursos limitados.
**Business_Impact:** Clientes en riesgo no atendidos; inactivos no reactivados; nuevos no reciben onboarding adecuado; ciclo de vida no optimizado; LTV menor.
**Metrics_To_Check:** Etapas del ciclo de vida definidas; % de clientes segmentados por etapa; acciones por etapa; efectividad de intervenciones por etapa; LTV por etapa.
**Diagnostic_Questions:** ¿Segmentamos clientes por etapa del ciclo de vida? ¿Identificamos clientes en riesgo? ¿Los clientes nuevos reciben tratamiento diferente? ¿Los inactivos se segmentan? ¿Hay estrategia por etapa?
**Recommended_Actions:** Definir etapas del ciclo de vida del cliente; segmentar clientes por etapa; diseñar estrategias y comunicaciones por etapa; configurar CRM para lifecycle; medir transición entre etapas.
**Severity_Level:** High
**Related_Patterns:** CUS-002, CUS-009, CUS-018, CUS-074, CUS-080

### CUS-082
**Pattern_Name:** Segmentación sin Feedback del Cliente
**Category:** Segmentación (Clientes)
**Description:** La segmentación de clientes se basa solo en datos internos (transacciones, valor) sin incorporar feedback del cliente (preferencias, necesidades, satisfacción), resultando en segmentos incompletos.
**Observable_Symptoms:** Segmentos basados solo en datos transaccionales; no se incorporan encuestas o preferencias; necesidades del cliente no reflejadas en segmentación; segmentos no capturan diferencias cualitativas; falta de voz del cliente en segmentación.
**Early_Warning_Signals:** Datos de segmentación solo transaccionales; % de segmentos que incorporan feedback < 20%; sin encuestas de preferencias en segmentación; segmentos no reflejan necesidades; clientes no se sienten representados.
**Typical_Causes:** Facilidad de datos transaccionales; falta de integración de feedback; herramientas limitadas; cultura de "datos duros" solamente; recursos para investigación cualitativa limitados.
**Business_Impact:** Segmentación incompleta; necesidades no capturadas; propuesta de valor no alineada; personalización limitada; oportunidades de diferenciación perdidas.
**Metrics_To_Check:** % de segmentos con datos de feedback; fuentes de datos de segmentación; precisión de segmentación vs necesidades reales; satisfacción por segmento; alineación propuesta-necesidad.
**Diagnostic_Questions:** ¿La segmentación incorpora feedback del cliente? ¿Capturamos preferencias y necesidades? ¿Los segmentos reflejan la realidad del cliente? ¿Usamos datos cualitativos además de cuantitativos? ¿Los clientes se sienten representados?
**Recommended_Actions:** Incorporar feedback del cliente en segmentación (encuestas, entrevistas, análisis de reclamos); enriquecer segmentos con datos cualitativos; validar segmentos con clientes; actualizar segmentos con nuevo feedback; medir precisión de segmentación.
**Severity_Level:** Medium
**Related_Patterns:** CUS-057, CUS-074, CUS-078


## Dependencia de clientes

### CUS-083
**Pattern_Name:** Concentración de Ingresos en Pocos Clientes
**Category:** Dependencia de clientes
**Description:** Un pequeño número de clientes representa un porcentaje muy alto de los ingresos totales, generando un riesgo enorme si alguno de ellos se pierde.
**Observable_Symptoms:** Top 3-5 clientes representan > 40% de ingresos; la empresa "vive" para esos clientes; decisiones condicionadas por clientes grandes; miedo a perder al cliente principal; el equipo dedica tiempo desproporcionado a pocos clientes.
**Early_Warning_Signals:** % de ingresos del top 1 cliente > 15%; % de ingresos del top 5 > 40%; cliente único representa riesgo de continuidad; dependencia operativa de clientes grandes; % de margen concentrado > 50%.
**Typical_Causes:** Enfoque de ventas en clientes grandes; falta de diversificación de cartera; producto/servicio niche para grandes clientes; comodidad con pocos clientes; falta de capacidad para atender más.
**Business_Impact:** Riesgo extremo de concentración; pérdida de un cliente grande puede quebrar el negocio; bajo poder de negociación (cliente lo sabe); crecimiento limitado por cartera concentrada; valor de empresa bajo por riesgo.
**Metrics_To_Check:** % de ingresos del top 1, 3, 5, 10 clientes; % de margen concentrado; índice de concentración (Herfindahl); % de clientes que representan 80% de ingresos; tendencia de concentración.
**Diagnostic_Questions:** ¿Qué % de ingresos viene de nuestros top 5 clientes? ¿Qué pasaría si perdiéramos al cliente más grande? ¿Estamos diversificando la cartera? ¿El riesgo de concentración es aceptable? ¿Los clientes grandes saben que los necesitamos?
**Recommended_Actions:** Medir concentración de ingresos trimestralmente; establecer límite máximo por cliente; diversificar cartera activamente; fortalecer relaciones con clientes medianos; desarrollar nuevos segmentos; reducir dependencia gradualmente.
**Severity_Level:** Critical
**Related_Patterns:** CUS-006, CUS-019, CUS-048, CUS-065, CUS-074, CUS-084

### CUS-084
**Pattern_Name:** Dependencia Operativa de Cliente Específico
**Category:** Dependencia de clientes
**Description:** La empresa ha adaptado sus procesos, producto o equipo a un cliente específico, generando dependencia operativa que dificulta atender a otros clientes o perder al cliente principal.
**Observable_Symptoms:** Procesos diseñados para un cliente; equipo dedicado a ese cliente; el producto se personalizó para ese cliente; otros clientes se quejan de no recibir misma atención; si el cliente se va, hay que rediseñar la operación.
**Early_Warning_Signals:** % de recursos dedicados a un solo cliente > 30%; procesos no estandarizados por cliente; producto personalizado no reutilizable; equipo especializado en un cliente; dificultad para atender nuevos clientes.
**Typical_Causes:** Crecimiento orgánico alrededor de un cliente grande; falta de estandarización; mentalidad de "cuenta estratégica"; falta de visión de portafolio; cultura de servicio extremo.
**Business_Impact:** Dependencia operativa difícil de romper; dificultad para escalar; vulnerabilidad si el cliente se va; inversiones no recuperables si se pierde el cliente; crecimiento limitado por falta de estandarización.
**Metrics_To_Check:** % de recursos dedicados a top clientes; % de procesos estandarizados vs personalizados; % de producto personalizado; capacidad de atender nuevos clientes; tiempo de reasignación si se pierde cliente.
**Diagnostic_Questions:** ¿Hemos adaptado demasiado nuestra operación a un cliente? ¿Podríamos atender a otros clientes con la misma operación? ¿Qué pasaría si ese cliente se fuera? ¿La dependencia operativa es un riesgo? ¿Estamos sobre-personalizando?
**Recommended_Actions:** Estandarizar procesos para reducir dependencia; balancear personalización con escalabilidad; desarrollar nuevos clientes para diversificar; medir dependencia operativa; crear plan de contingencia para cliente clave.
**Severity_Level:** High
**Related_Patterns:** CUS-083, CUS-085, CUS-086, CUS-089

### CUS-085
**Pattern_Name:** Cliente Tiene Poder de Fijar Precios
**Category:** Dependencia de clientes
**Description:** Un cliente grande tiene el poder de imponer condiciones de precio, descuento o pago, erosionando el margen de la empresa y generando dependencia económica insostenible.
**Observable_Symptoms:** Cliente grande exige descuentos crecientes; no se puede subir precios a ese cliente; las condiciones las pone el cliente; el margen de ese cliente es mucho menor; la empresa acepta condiciones desfavorables por miedo a perderlo.
**Early_Warning_Signals:** Margen del cliente grande significativamente menor que el promedio; descuentos crecientes sin justificación; cliente exige condiciones especiales; precio del cliente grande no se ajusta con inflación; % de ingresos del cliente grande crece pero margen decrece.
**Typical_Causes:** Concentración excesiva; bajo poder de negociación; cliente sabe que es indispensable; falta de alternativas para la empresa; cultura de "cliente grande manda".
**Business_Impact:** Erosión de margen; trabajo no rentable para cliente grande; subsidio de cliente grande por otros; dificultad para crecer rentablemente; dependencia nociva.
**Metrics_To_Check:** Margen del cliente grande vs promedio; tendencia de descuentos; precio relativo del cliente grande; % de rentabilidad del cliente grande; contribución marginal.
**Diagnostic_Questions:** ¿El cliente grande tiene poder para fijar precios? ¿Su margen es menor que el promedio? ¿Aceptamos condiciones desfavorables? ¿Podríamos renegociar? ¿Estamos subsidiando al cliente grande?
**Recommended_Actions:** Diversificar cartera para reducir dependencia; fortalecer poder de negociación (diferenciación, valor agregado); establecer políticas de precio mínimas; renegociar condiciones gradualmente; aceptar perder clientes no rentables.
**Severity_Level:** Critical
**Related_Patterns:** CUS-083, CUS-084, CUS-086, CUS-089

### CUS-086
**Pattern_Name:** Cliente Único Representa Riesgo de Continuidad
**Category:** Dependencia de clientes
**Description:** Un solo cliente representa tal proporción de ingresos (> 30%) que su pérdida pondría en riesgo la continuidad del negocio, y no hay plan de contingencia.
**Observable_Symptoms:** Un cliente es > 30% de ingresos; la empresa no sobreviviría sin ese cliente; no hay plan B; el equipo vive "pendiente" de ese cliente; cualquier problema con ese cliente genera crisis.
**Early_Warning_Signals:** % de ingresos de un cliente > 30%; % de margen de un cliente > 30%; sin plan de contingencia; estrés organizacional por dependencia; cliente único mencionado en riesgos financieros.
**Typical_Causes**: Éxito inicial con un cliente grande; falta de diversificación; crecimiento sin estrategia de cartera; dependencia construida gradualmente sin conciencia; comodidad vs urgencia.
**Business_Impact:** Riesgo existencial; cualquier cambio en el cliente (pérdida, reducción, atraso) amenaza la empresa; valor de empresa muy bajo; difícil conseguir financiamiento; estrés organizacional permanente.
**Metrics_To_Check:** % de ingresos del cliente principal; % de margen del cliente principal; probabilidad de pérdida estimada; plan de contingencia; reservas financieras para crisis.
**Diagnostic_Questions:** ¿Podríamos sobrevivir si perdiéramos nuestro cliente más grande? ¿Qué % de ingresos representa? ¿Tenemos plan de contingencia? ¿Cuánto tiempo podríamos operar sin ese cliente? ¿Estamos trabajando en diversificar?
**Recommended_Actions:** Establecer plan de diversificación urgente; límite máximo de concentración (25% por cliente); desarrollar nuevos clientes y segmentos; crear reserva financiera; monitorear salud del cliente grande.
**Severity_Level:** Critical
**Related_Patterns:** CUS-083, CUS-084, CUS-085, CUS-089

### CUS-087
**Pattern_Name:** Dependencia de Clientes de Bajo Margen
**Category:** Dependencia de clientes
**Description:** La empresa depende de clientes que generan alto volumen de ingresos pero márgenes muy bajos, ocupando capacidad operativa que podría destinarse a clientes más rentables.
**Observable_Symptoms:** Clientes grandes pero de bajo margen; ocupan mucha capacidad; el margen neto de esos clientes es casi nulo; la empresa está "ocupada pero no gana"; el esfuerzo no justifica el retorno.
**Early_Warning_Signals:** % de ingresos de clientes de bajo margen > 40%; margen neto de clientes grandes < 5%; capacidad ocupada por clientes de bajo margen; rentabilidad por hora/cliente baja; costo de servir alto vs margen.
**Typical_Causes:** Desesperación por ingresos; falta de segmentación por rentabilidad; clientes históricos que ya no son rentables; miedo a perder ingresos; estructura de costos no entendida.
**Business_Impact:** Ocupación sin rentabilidad; capacidad desperdiciada; imposibilidad de atender clientes más rentables; rentabilidad general baja; crecimiento no rentable.
**Metrics_To_Check:** Margen neto por cliente; % de capacidad ocupada por clientes de bajo margen; rentabilidad por hora/cliente; costo de servir; margen de contribución.
**Diagnostic_Questions:** ¿Hay clientes que ocupan mucha capacidad pero generan bajo margen? ¿El volumen de ingresos oculta la falta de rentabilidad? ¿Podríamos reasignar capacidad a clientes más rentables? ¿Deberíamos dejar de servir a esos clientes?
**Recommended_Actions:** Analizar rentabilidad por cliente; identificar clientes de bajo margen; renegociar precios o reducir servicio; liberar capacidad para clientes más rentables; establecer rentabilidad mínima por cliente.
**Severity_Level:** High
**Related_Patterns:** CUS-065, CUS-083, CUS-085, CUS-088, CUS-089

### CUS-088
**Pattern_Name:** Dependencia sin Estrategia de Profundización
**Category:** Dependencia de clientes
**Description:** La empresa depende de clientes grandes pero no invierte en profundizar la relación (upselling, cross-selling, múltiples contactos), por lo que la dependencia es frágil y cualquier cambio en el interlocutor puede significar la pérdida del cliente.
**Observable_Symptoms:** Relación con un solo contacto en el cliente; no hay upselling a clientes grandes; solo se vende un producto/servicio; la relación no se profundiza; si el contacto se va, se pierde el cliente.
**Early_Warning_Signals:** % de clientes grandes con un solo contacto < 30%; % de clientes grandes con upselling < 20%; relación con un solo producto; rotación de contacto en cliente grande afecta ingresos; sin plan de profundización.
**Typical_Causes:** Conformismo con el cliente grande; falta de estrategia de cuenta; recursos limitados para profundizar; cultura de "si no se queja, no molestes"; miedo a "arriesgar" la relación.
**Business_Impact:** Relación frágil; vulnerable a rotación de contacto; oportunidad de crecimiento en cuenta perdida; dependencia sin defensa; LTV de cliente grande no maximizado.
**Metrics_To_Check:** Número de contactos por cliente grande; % de clientes grandes con upselling; % de clientes grandes con múltiples productos; % de ingresos del cliente por producto principal vs adicionales; rotación de contactos.
**Diagnostic_Questions:** ¿Tenemos múltiples contactos en nuestros clientes grandes? ¿Hacemos upselling/cross-selling? ¿La relación depende de una sola persona? ¿Qué pasaría si nuestro contacto se fuera? ¿Estamos profundizando la relación?
**Recommended_Actions:** Desarrollar múltiples contactos en clientes grandes; identificar oportunidades de upselling; diversificar productos/servicios vendidos; crear plan de cuenta para clientes clave; medir profundidad de relación.
**Severity_Level:** High
**Related_Patterns:** CUS-036, CUS-051, CUS-083, CUS-084, CUS-089

### CUS-089
**Pattern_Name:** Dependencia sin Plan de Sucesión de Clientes
**Category:** Dependencia de clientes
**Description:** La empresa depende de clientes grandes pero no tiene un plan de sucesión si esos clientes se pierden, resultando en crisis cuando ocurre lo inevitable.
**Observable_Symptoms:** No hay plan B para clientes grandes; la empresa reacciona en crisis cuando pierde un cliente; no hay pipeline de reemplazo; el equipo entra en pánico; la operación no puede reajustarse rápidamente.
**Early_Warning_Signals:** Sin plan de contingencia para top clientes; % de ingresos sin cobertura de reemplazo; tiempo estimado para reemplazar cliente grande > 6 meses; sin pipeline de clientes potenciales; sin reserva financiera.
**Typical_Causes:** Optimismo excesivo; cultura de "eso no va a pasar"; falta de previsión; recursos dedicados a clientes actuales no a prospectos; negación del riesgo.
**Business_Impact:** Crisis cuando se pierde cliente grande; decisión apresurada de reemplazo (clientes no rentables); posible quiebra; estrés organizacional; pérdida de valor.
**Metrics_To_Check:** Plan de contingencia para top clientes; pipeline de reemplazo; % de ingresos reemplazables en 3, 6, 12 meses; reserva financiera; tiempo de recuperación estimado.
**Diagnostic_Questions:** ¿Tenemos un plan de contingencia si perdemos nuestro cliente más grande? ¿Cuánto tiempo tomaría reemplazarlo? ¿Tenemos pipeline de prospectos? ¿Hay reserva financiera? ¿Estamos preparados para lo peor?
**Recommended_Actions:** Crear plan de contingencia para cada cliente grande; mantener pipeline de prospectos activo para reemplazo; construir reserva financiera (3-6 meses); diversificar ingresos; monitorear salud de clientes grandes.
**Severity_Level:** Critical
**Related_Patterns:** CUS-083, CUS-084, CUS-086, CUS-088

### CUS-090
**Pattern_Name:** Dependencia Emocional de Clientes Históricos
**Category:** Dependencia de clientes
**Description:** La empresa mantiene relaciones con clientes que ya no son rentables o estratégicos por razones emocionales (historia, amistad, "siempre estuvieron"), impidiendo una gestión objetiva de la cartera.
**Observable_Symptoms:** Clientes que ya no son rentables pero se mantienen; la empresa "les tiene cariño"; se les da trato preferencial sin justificación comercial; no se suben precios por "no molestarlos"; ocupan recursos que podrían ser mejor utilizados.
**Early_Warning_Signals:** Clientes con margen negativo mantenidos por razones emocionales; % de clientes no rentables en cartera > 15%; precios no ajustados por "no molestar"; recursos desproporcionados para clientes históricos; falta de objetividad en decisiones de cartera.
**Typical_Causes:** Fundador con relación personal; cultura de "familia"; miedo al conflicto; falta de revisión objetiva de cartera; mezcla de amistad y negocio.
**Business_Impact:** Rentabilidad general menor; recursos mal asignados; objetividad perdida; clientes rentables subsidian a históricos; crecimiento limitado; cultura de "amiguismo".
**Metrics_To_Check:** % de clientes no rentables en cartera; margen de clientes históricos vs nuevos; precio relativo de clientes históricos; % de recursos dedicados a clientes no rentables; tasa de rotación objetiva de cartera.
**Diagnostic_Questions:** ¿Mantenemos clientes no rentables por razones emocionales? ¿Hay clientes que reciben trato preferencial sin justificación? ¿Subimos precios objetivamente? ¿Revisamos la cartera con criterios objetivos? ¿Las decisiones de cartera son emocionales o racionales?
**Recommended_Actions:** Revisar cartera con criterios objetivos (rentabilidad, potencial, estratégico); separar relaciones personales de comerciales; establecer política de precios y condiciones objetiva; desinvertir en clientes no rentables; profesionalizar gestión de cartera.
**Severity_Level:** Medium
**Related_Patterns:** CUS-083, CUS-085, CUS-087, CUS-089

### CUS-091
**Pattern_Name:** Dependencia sin Métricas de Riesgo de Cartera
**Category:** Dependencia de clientes
**Description:** La empresa no mide el riesgo de concentración de su cartera de clientes (índice de concentración, probabilidad de pérdida, impacto), por lo que no gestiona activamente la dependencia.
**Observable_Symptoms:** No se mide concentración de ingresos; no se evalúa riesgo de pérdida de clientes; no hay métricas de salud de cartera; decisiones de cartera sin datos; el riesgo de dependencia se descubre cuando es demasiado tarde.
**Early_Warning_Signals:** Sin métricas de concentración de cartera; sin índice de riesgo de dependencia; sin probabilidad de pérdida por cliente; sin límites de concentración; sin reportes de riesgo de cartera.
**Typical_Causes:** Desconocimiento de métricas de riesgo; cultura de "vender nomás"; falta de herramientas analíticas; recursos limitados; priorización de crecimiento sobre riesgo.
**Business_Impact:** Riesgo de concentración no gestionado; sorpresas cuando se pierde un cliente grande; imposibilidad de anticipar y mitigar; cartera no optimizada; valor de empresa afectado.
**Metrics_To_Check:** (Deberían medirse) índice de concentración (Herfindahl); % de ingresos top 1/5/10; probabilidad de pérdida por cliente; impacto de pérdida; límites de concentración vs reales.
**Diagnostic_Questions:** ¿Medimos el riesgo de concentración de la cartera? ¿Tenemos índices de dependencia? ¿Sabemos cuál es el impacto de perder un cliente grande? ¿Hay límites de concentración? ¿Gestionamos activamente el riesgo de cartera?
**Recommended_Actions:** Implementar métricas de riesgo de cartera (concentración, dependencia, probabilidad de pérdida); establecer límites de concentración; monitorear trimestralmente; crear reportes de riesgo; incorporar en decisiones estratégicas.
**Severity_Level:** High
**Related_Patterns:** CUS-083, CUS-084, CUS-086, CUS-089
