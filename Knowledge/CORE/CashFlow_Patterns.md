# Cash Flow Patterns — SME Knowledge Base

> Base de conocimiento para que agentes de IA detecten patrones de flujo de efectivo relevantes en PyMEs: flujo operativo, flujo de inversión, flujo financiero, ciclo de conversión de efectivo, cobranzas, pagos, necesidad de capital de trabajo, tensiones de caja, estacionalidad, financiamiento operativo y riesgo de iliquidez.

---

## Categorías cubiertas

| # | Categoría | Patrones |
|---|-----------|----------|
| 1 | Flujo Operativo | 10 |
| 2 | Flujo de Inversión | 7 |
| 3 | Flujo Financiero | 8 |
| 4 | Ciclo de Conversión de Efectivo | 9 |
| 5 | Cobranzas | 11 |
| 6 | Pagos | 8 |
| 7 | Necesidad de Capital de Trabajo | 8 |
| 8 | Tensiones de Caja | 7 |
| 9 | Estacionalidad | 8 |
| 10 | Financiamiento Operativo | 8 |
| 11 | Riesgo de Iliquidez | 9 |
| **Total** | | **93** |

---

## Flujo Operativo

### CFL-001
**Pattern_Name:** CFLO Negativo Recurrente
**Category:** Flujo Operativo
**Description:** El flujo de efectivo operativo (CFLO) es consistentemente negativo durante varios períodos consecutivos, lo que indica que las operaciones del negocio no generan suficiente efectivo para sostenerse.
**Observable_Symptoms:** La empresa reporta ganancias contables pero el efectivo disminuye; necesidad constante de financiamiento externo para cubrir gastos operativos; solicitudes recurrentes de préstamos para capital de trabajo; saldo de caja disminuye período a período.
**Early_Warning_Signals:** CFLO negativo por dos trimestres consecutivos; diferencia creciente entre EBITDA y CFLO; rotación de cuentas por cobrar en aumento; días de inventario crecientes; cuentas por pagar que se extienden más allá de lo normal.
**Typical_Causes:** Crecimiento no rentable con márgenes negativos; descalce entre ciclo de cobro y pago; capital de trabajo mal gestionado; ventas a crédito sin control de cobranza; gastos operativos fijos demasiado altos para el nivel de ingresos.
**Business_Impact:** Dependencia creciente de deuda o capital externo; deterioro de la relación con proveedores; imposibilidad de reinvertir en el negocio; riesgo de insolvencia técnica a mediano plazo.
**Metrics_To_Check:** CFLO (negativo por más de 2 períodos); Relación CFLO / EBITDA (< 0.5); Días de Cobro (CPP) + Días de Inventario (DPI) vs Días de Pago (DPP); Ratio de Liquidez Corriente; CFLO / Ventas Netas.
**Diagnostic_Questions:** ¿Cuántos períodos consecutivos lleva el CFLO negativo? ¿El CFLO negativo se debe a crecimiento o a pérdidas operativas? ¿Qué proporción del CFLO negativo se explica por aumento de capital de trabajo? ¿Tiene la empresa acceso a financiamiento para cubrir el déficit?
**Recommended_Actions:** Identificar y reducir gastos operativos no esenciales; renegociar condiciones de pago con proveedores; implementar política de cobranzas más agresiva; evaluar descuento de facturas para acelerar cobro; considerar reestructuración de deuda para liberar efectivo.
**Severity_Level:** High
**Related_Patterns:** CFL-002, CFL-026, CFL-035, CFL-085

### CFL-002
**Pattern_Name:** CFLO Creciendo Menos que Ventas
**Category:** Flujo Operativo
**Description:** Las ventas crecen a un ritmo significativamente mayor que el CFLO, indicando que el crecimiento no se traduce en efectivo debido a la absorción por capital de trabajo o márgenes decrecientes.
**Observable_Symptoms:** Ventas en aumento pero el efectivo en caja no mejora; la empresa reporta crecimiento en ingresos pero sigue necesitando financiamiento; incremento desproporcionado en cuentas por cobrar e inventarios; presión constante sobre líneas de crédito.
**Early_Warning_Signals:** CFLO crece menos de la mitad del crecimiento de ventas; relación CFLO/Ventas en descenso continuo; días de cobro estables pero volumen creciente; margen EBITDA estable pero CFLO no acompaña.
**Typical_Causes:** Crecimiento financiado con capital de trabajo (vender más requiere más inventario y más cuentas por cobrar); plazos de cobro que no se ajustan al crecimiento; márgenes que se comprimen por competencia de precios.
**Business_Impact:** Crecimiento insostenible que genera estrés de caja; necesidad de financiamiento externo para sostener el crecimiento; rentabilidad diluida por costo de financiamiento; límite natural al crecimiento por restricción de caja.
**Metrics_To_Check:** Tasa de Crecimiento de Ventas vs Tasa de Crecimiento de CFLO; CFLO / Ventas Netas (tendencia); Incremento en NWC / Incremento en Ventas; Rotación de Activos; Margen EBITDA.
**Diagnostic_Questions:** ¿A qué velocidad crece el capital de trabajo en relación a las ventas? ¿El crecimiento de ventas requiere inversión proporcional en inventario y cuentas por cobrar? ¿Se han ajustado los precios para mantener el margen? ¿Hay estacionalidad que afecta la comparación?
**Recommended_Actions:** Evaluar rentabilidad por línea de producto/cliente; implementar políticas de cobro más estrictas en clientes nuevos; buscar financiamiento de capital de trabajo ligado al crecimiento (factoraje, confirming); revisar política de inventarios (justo a tiempo); considerar desacelerar crecimiento si no es rentable.
**Severity_Level:** Medium
**Related_Patterns:** CFL-001, CFL-054, CFL-060, CFL-085

### CFL-003
**Pattern_Name:** Descalce entre EBITDA y CFLO
**Category:** Flujo Operativo
**Description:** Existe una brecha significativa y persistente entre el EBITDA (utilidad operativa) y el CFLO, indicando que el beneficio contable no se convierte en efectivo debido a aumento de capital de trabajo u otros factores.
**Observable_Symptoms:** La empresa muestra EBITDA positivo pero no tiene efectivo; los estados financieros muestran rentabilidad pero caja decreciente; necesidad de financiamiento a pesar de resultados positivos; diferencia sistemática entre utilidad neta y flujo de efectivo.
**Early_Warning_Signals:** Relación CFLO/EBITDA < 0.7 por más de 2 períodos; incremento sostenido en cuentas por cobrar e inventarios; diferencia entre EBITDA reportado y generación de caja real.
**Typical_Causes:** Crecimiento acelerado que consume caja en capital de trabajo; política de crédito laxa para impulsar ventas; acumulación de inventario por mala gestión de demanda; clientes que pagan cada vez más lento; provisiones contables que no afectan caja.
**Business_Impact:** Percepción errónea de salud financiera del negocio; decisiones equivocadas basadas en EBITDA; riesgo de iliquidez a pesar de rentabilidad; falta de recursos para reinversión y crecimiento.
**Metrics_To_Check:** CFLO / EBITDA (ratio); Tendencia de Capital de Trabajo Neto (NWC); Diferencia absoluta EBITDA - CFLO; Variación en Cuentas por Cobrar, Inventarios y Cuentas por Pagar; Ciclo de Conversión de Efectivo (CCC).
**Diagnostic_Questions:** ¿Cuál es la relación CFLO/EBITDA en los últimos 4 trimestres? ¿Qué componentes del capital de trabajo explican la brecha? ¿Hay partidas contables no monetarias significativas? ¿Se ha analizado el estado de flujo de efectivo completo?
**Recommended_Actions:** Elaborar un estado de flujo de efectivo proyectado mensual; implementar políticas de gestión de capital de trabajo; revisar plazos de crédito y cobranza; segmentar clientes por comportamiento de pago; establecer metas de conversión de EBITDA a caja.
**Severity_Level:** High
**Related_Patterns:** CFL-001, CFL-026, CFL-035, CFL-085

### CFL-004
**Pattern_Name:** CFLO Dependiente de Adelantos de Clientes
**Category:** Flujo Operativo
**Description:** Una porción significativa del CFLO proviene de anticipos o adelantos de clientes, lo que infla artificialmente el flujo operativo y puede ocultar debilidades subyacentes.
**Observable_Symptoms:** Alta proporción de pasivos por anticipos de clientes; dependencia de pagos por adelantado para cubrir gastos operativos; crecimiento en la cuenta de anticipos recibidos; descalce entre ingresos diferidos y ejecución.
**Early_Warning_Signals:** Anticipos de clientes > 20% del pasivo corriente; relación CFLO/EBITDA > 1.3 (artificialmente alta); anticipos creciendo más rápido que ventas; ejecución de proyectos retrasada vs anticipos cobrados.
**Typical_Causes:** Modelo de negocio basado en suscripciones o prepago; necesidad de efectivo para financiar operaciones; incapacidad de acceder a crédito bancario; clientes dispuestos a pagar por adelantado por descuentos.
**Business_Impact:** Riesgo de no poder ejecutar los proyectos/entregas por los que se recibieron anticipos; presión para entregar rápido y quemar caja; percepción distorsionada de la salud financiera; dependencia peligrosa si los clientes dejan de adelantar.
**Metrics_To_Check:** Anticipos de Clientes / Pasivo Corriente; Anticipos de Clientes / Ventas; CFLO Ajustado (excluyendo variación de anticipos); Relación Anticipos / EBITDA.
**Diagnostic_Questions:** ¿Qué porcentaje del CFLO proviene de anticipos de clientes? ¿Los anticipos corresponden a proyectos/entregables futuros o son solo financiamiento? ¿Hay capacidad operativa para ejecutar lo cobrado por adelantado? ¿Qué pasa si los clientes dejan de adelantar?
**Recommended_Actions:** Separar contablemente los anticipos del CFLO real; proyectar CFLO sin considerar anticipos; diversificar fuentes de financiamiento; gestionar activamente la ejecución de proyectos anticipados; alerta si los anticipos caen consistentemente.
**Severity_Level:** Medium
**Related_Patterns:** CFL-003, CFL-068, CFL-077, CFL-090

### CFL-005
**Pattern_Name:** CFLO con Alta Participación No Recurrente
**Category:** Flujo Operativo
**Description:** El CFLO incluye ingresos no recurrentes (ventas de activos, reembolsos extraordinarios, seguros, juicios ganados) que ocultan la verdadera capacidad de generación de efectivo operativa.
**Observable_Symptoms:** CFLO positivo pero la empresa lucha para pagar gastos corrientes; mejora puntual en efectivo seguida de deterioro; partidas inusuales en el estado de flujo de efectivo; CFLO que no se correlaciona con el nivel de actividad.
**Early_Warning_Signals:** Partidas no recurrentes representan > 15% del CFLO en un período; CFLO ajustado (excluyendo no recurrente) es negativo o muy bajo; el negocio no genera caja sin eventos extraordinarios.
**Typical_Causes:** Deterioro del negocio principal que se enmascara con eventos no recurrentes; presión de la dirección por mostrar flujo positivo; venta de activos para cubrir déficit operativo; necesidad de cumplir covenants bancarios.
**Business_Impact:** Percepción equivocada de la capacidad real del negocio; decisiones de inversión o crecimiento basadas en flujo insostenible; riesgo de iliquidez cuando se agotan los eventos no recurrentes; planificación financiera irreal.
**Metrics_To_Check:** CFLO Ajustado (excluyendo no recurrente); Partidas No Recurrentes / CFLO; Frecuencia de eventos no recurrentes; CFLO / Ventas Netas Ajustado.
**Diagnostic_Questions:** ¿Cuánto del CFLO del período corresponde a partidas no recurrentes? ¿Se puede sostener el CFLO sin estos eventos? ¿Hay un patrón de venta de activos para cubrir déficit operativo? ¿Cuál es el CFLO normalizado excluyendo extraordinarios?
**Recommended_Actions:** Ajustar el CFLO para excluir partidas no recurrentes en análisis; proyectar flujo de efectivo solo con operaciones recurrentes; identificar si la empresa está liquidándose lentamente; establecer alerta automática cuando no recurrentes superen 15%.
**Severity_Level:** Medium
**Related_Patterns:** CFL-001, CFL-003, CFL-013, CFL-085

### CFL-006
**Pattern_Name:** CFLO Absorbido por Crecimiento
**Category:** Flujo Operativo
**Description:** El crecimiento de ventas consume todo el CFLO generado, dejando a la empresa sin efectivo disponible para otros fines a pesar de estar creciendo.
**Observable_Symptoms:** La empresa crece en ventas pero el efectivo no aumenta; después de cada ciclo de crecimiento la caja está igual o peor; necesidad constante de capital de trabajo adicional; crecimiento autofinanciado que no libera efectivo.
**Early_Warning_Signals:** Incremento en NWC mayor que CFLO generado; relación CFLO/Ventas en descenso; tasa de reinversión en NWC > 100% del CFLO; crecimiento de ventas > 20% anual con CFLO estable.
**Typical_Causes:** Crecimiento intensivo en capital de trabajo (ventas a crédito, alta rotación de inventario requerido); márgenes bajos que no generan efectivo suficiente para financiar el crecimiento; política de crédito laxa para ganar mercado; empresas en etapa de alto crecimiento.
**Business_Impact:** Crecimiento insostenible que lleva a crisis de liquidez; necesidad de dilución (capital) o deuda para financiar crecimiento; la empresa no puede crecer sin financiamiento externo; riesgo de sobreendeudamiento.
**Metrics_To_Check:** Tasa de Crecimiento de NWC vs CFLO; CFLO Libre (después de inversión en NWC); Relación Incremento NWC / Incremento Ventas; Días de Cobro, Inventario y Pago; Capital de Trabajo como % de Ventas.
**Diagnostic_Questions:** ¿Qué parte del CFLO se destina a financiar el crecimiento del NWC? ¿El crecimiento es rentable después de considerar el costo de financiar el NWC? ¿Hay margen para ajustar condiciones de pago con clientes y proveedores? ¿Se puede reducir la intensidad de capital de trabajo del crecimiento?
**Recommended_Actions:** Estimar el punto de inflexión donde el crecimiento comienza a liberar efectivo; buscar financiamiento ligado al crecimiento (factoraje, confirming); priorizar segmentos de clientes con mejores condiciones de pago; negociar con proveedores plazos más largos para financiar el crecimiento.
**Severity_Level:** Medium
**Related_Patterns:** CFL-001, CFL-002, CFL-054, CFL-060, CFL-085

### CFL-007
**Pattern_Name:** CFLO Deteriorado por Caída de Precios
**Category:** Flujo Operativo
**Description:** La presión sobre precios de venta (por competencia, regulación o cambios de mercado) reduce el margen de contribución y consecuentemente el CFLO, aunque el volumen de ventas se mantenga.
**Observable_Symptoms:** Ventas estables o crecientes, pero CFLO decreciente; márgenes brutos comprimidos; necesidad de aumentar volumen para mantener el mismo nivel de caja; reducción de precios para mantener participación de mercado.
**Early_Warning_Signals:** Margen Bruto en caída por 3+ trimestres consecutivos; precio de venta promedio en descenso; relación CFLO/Unidad Vendida decreciente; incremento en descuentos y bonificaciones.
**Typical_Causes:** Competencia agresiva que presiona precios a la baja; entrada de nuevos competidores o sustitutos; pérdida de poder de negociación con clientes; productos commodity sin diferenciación; regulación que limita precios.
**Business_Impact:** Menor capacidad de generación de caja operativa; necesidad de reducir costos para compensar; deterioro de la rentabilidad del negocio; posible necesidad de reestructuración operativa.
**Metrics_To_Check:** Margen Bruto (tendencia); CFLO por Unidad Vendida; Precio Promedio de Venta; Elasticidad Precio-Volumen; Margen de Contribución; Relación CFLO / Margen Bruto.
**Diagnostic_Questions:** ¿El CFLO se deteriora por caída de precio o por aumento de costos? ¿Se ha intentado diferenciar el producto para evitar competencia en precio? ¿Hay oportunidades de reducción de costos variables? ¿El volumen compensa la caída de precio?
**Recommended_Actions:** Identificar segmentos donde se pueda mantener precio; reducir costos variables y fijos para recuperar margen; buscar diferenciación (calidad, servicio, branding); diversificar productos o servicios hacia mayor valor agregado; evaluar salida de segmentos no rentables.
**Severity_Level:** Medium
**Related_Patterns:** CFL-001, CFL-003, CFL-026, CFL-085

### CFL-008
**Pattern_Name:** CFLO con Alta Dependencia de Descuentos por Pronto Pago
**Category:** Flujo Operativo
**Description:** El CFLO depende significativamente de descuentos ofrecidos a clientes por pago anticipado, lo que comprime el margen y puede indicar una necesidad urgente de efectivo.
**Observable_Symptoms:** Alta proporción de clientes tomando descuentos por pronto pago; incremento en el porcentaje de descuentos financieros sobre ventas; disminución en el precio efectivo de venta; clientes que pagan antes solo por descuento.
**Early_Warning_Signals:** Descuentos por Pronto Pago > 2% de las ventas; tendencia creciente en descuentos financieros; relación CFLO/Descuentos en descenso; clientes nuevos reciben descuentos agresivos.
**Typical_Causes:** Necesidad urgente de efectivo para cubrir gastos; política de descuentos agresiva para acelerar cobro; falta de acceso a otras fuentes de financiamiento; cultura de descuentos establecida en la empresa.
**Business_Impact:** Erosión de margen por descuentos financieros; dependencia peligrosa de los descuentos para mantener flujo; percepción de debilidad financiera por parte de clientes; clientes que se acostumbran a los descuentos y exigen cada vez más.
**Metrics_To_Check:** Descuentos por Pronto Pago / Ventas; Costo Efectivo del Descuento (tasa implícita); CFLO Neto de Descuentos; Porcentaje de Clientes que Toman Descuento; Tendencia de Descuentos.
**Diagnostic_Questions:** ¿A qué tasa efectiva está financiando la empresa a sus clientes? ¿El costo del descuento es menor que el costo de otras fuentes de financiamiento? ¿Se ha evaluado el costo real del programa de descuentos? ¿Hay clientes que solo compran por los descuentos?
**Recommended_Actions:** Calcular el costo efectivo del descuento vs costo de otras fuentes de financiamiento; reducir gradualmente los descuentos; segmentar clientes: mantener descuento solo para los estratégicos; buscar financiamiento alternativo más barato; ajustar términos de descuento para que sean menos agresivos.
**Severity_Level:** Low
**Related_Patterns:** CFL-004, CFL-038, CFL-068, CFL-085

### CFL-009
**Pattern_Name:** CFLO Volátil por Concentración de Clientes
**Category:** Flujo Operativo
**Description:** El CFLO muestra alta volatilidad debido a la dependencia de pocos clientes grandes, cuyos ciclos de pago y comportamiento afectan significativamente la generación de caja.
**Observable_Symptoms:** CFLO con picos y valles marcados que no se correlacionan con el nivel de actividad general; cambios bruscos en la caja cuando un cliente grande paga o deja de pagar; alta concentración de ventas en 1-3 clientes.
**Early_Warning_Signals:** Cliente único representa > 25% de ventas; varianza del CFLO > 30% entre períodos; cliente grande paga con patrones irregulares; mora concentrada en pocos deudores.
**Typical_Causes:** Dependencia de clientes grandes (gobierno, grandes empresas); contratos grandes con pagos contra hitos o entregables; estacionalidad en compras de clientes grandes; poca diversificación de base de clientes.
**Business_Impact:** CFLO impredecible que dificulta la planificación; riesgo severo si un cliente grande retrasa pagos; impacto desproporcionado en caja por eventos de un solo cliente; vulnerabilidad ante pérdida de cliente grande.
**Metrics_To_Check:** Concentración de Ventas (Top 1, Top 3, Top 5); Desviación Estándar del CFLO; Correlación CFLO vs Pagos de Cliente Principal; Días de Cobro por Cliente; % de Cuentas por Cobrar concentradas.
**Diagnostic_Questions:** ¿Cómo varía el CFLO cuando el cliente principal paga o no paga? ¿Cuánto tiempo puede operar la empresa sin el pago de su cliente principal? ¿Hay cláusulas contractuales que protejan la cobranza? ¿Se está diversificando activamente la base de clientes?
**Recommended_Actions:** Diversificar base de clientes; negociar contratos con pagos parciales o hitos más frecuentes; mantener reserva de efectivo equivalente a 1-2 ciclos de pago del cliente principal; implementar monitoreo de salud financiera de clientes grandes; considerar seguros de crédito.
**Severity_Level:** High
**Related_Patterns:** CFL-005, CFL-035, CFL-036, CFL-085, CFL-090

### CFL-010
**Pattern_Name:** CFLO Decreciente con Ventas Estables
**Category:** Flujo Operativo
**Description:** El CFLO disminuye consistentemente mientras las ventas se mantienen estables, lo que indica un deterioro en la eficiencia de conversión de ventas a efectivo.
**Observable_Symptoms:** Ventas planas pero efectivo decreciente; márgenes que se comprimen sin explicación aparente; aumento en costos operativos como porcentaje de ventas; necesidad creciente de capital de trabajo para mantener el mismo nivel de ventas.
**Early_Warning_Signals:** CFLO/Ventas en caída libre con ventas estables; margen EBITDA decreciente; rotación de activos en descenso; gastos operativos creciendo más que inflación.
**Typical_Causes:** Aumento de costos operativos no trasladado a precios; ineficiencias operativas que se acumulan; mezcla de ventas hacia productos/servicios de menor margen; aumento en costos de personal, alquiler o insumos; deterioro de la productividad laboral.
**Business_Impact:** Erosión gradual de la capacidad de generar caja; menor flexibilidad financiera; eventual necesidad de ajuste de costos o reestructuración; riesgo de caer en CFLO negativo si la tendencia continúa.
**Metrics_To_Check:** CFLO / Ventas Netas (tendencia 12 meses); Margen EBITDA; Gastos Operativos / Ventas; Rotación de Activos; Productividad Laboral (Ventas por Empleado).
**Diagnostic_Questions:** ¿Qué componentes del CFLO están deteriorándose? ¿Los costos variables o fijos están creciendo más que las ventas? ¿Se ha intentado trasladar el aumento de costos a precios? ¿Hay ineficiencias operativas identificables? ¿Está cambiando la mezcla de productos hacia menor margen?
**Recommended_Actions:** Realizar análisis de estructura de costos; identificar y eliminar ineficiencias; ajustar precios para reflejar aumento de costos; mejorar mezcla de ventas hacia mayor margen; implementar programa de productividad y reducción de costos.
**Severity_Level:** High
**Related_Patterns:** CFL-001, CFL-003, CFL-007, CFL-054, CFL-085


## Flujo de Inversión

### CFL-011
**Pattern_Name:** Capex Excesivo vs Depreciación
**Category:** Flujo de Inversión
**Description:** El gasto en activos fijos (Capex) supera significativa y sostenidamente la depreciación, lo que puede indicar sobreinversión o expansión no justificada.
**Observable_Symptoms:** Capex consistentemente > 2x depreciación; la empresa invierte más en activos de los que consume; incremento en activos fijos sin aumento proporcional en ventas; inmovilizado creciente con rendimientos decrecientes.
**Early_Warning_Signals:** Relación Capex / Depreciación > 2.0 por 3+ años; Capex / CFLO > 0.7; Retorno sobre Activos (ROA) en descenso; capacidad instalada no utilizada creciente.
**Typical_Causes:** Estrategia de expansión agresiva sin sustento; reinversión excesiva por presión competitiva; compras de activos por oportunidad fiscal sin análisis de negocio; exceso de confianza en la demanda futura; capex financiado con deuda que presiona el flujo.
**Business_Impact:** Presión sobre la caja por salidas de inversión; menor efectivo disponible para operaciones y deuda; activos ociosos que generan costos de mantenimiento; riesgo de sobrecapacidad y guerras de precios.
**Metrics_To_Check:** Capex / Depreciación; Capex / CFLO; ROA (tendencia); Rotación de Activos Fijos; Capacidad Instalada Utilizada; Capex / Ventas.
**Diagnostic_Questions:** ¿Hay un plan de negocio que justifique el nivel de Capex? ¿El Capex está generando el retorno esperado? ¿Cuánta capacidad ociosa tiene la empresa actualmente? ¿El Capex se financia con CFLO o con deuda? ¿Hay proyectos con VAN negativo en curso?
**Recommended_Actions:** Reevaluar todos los proyectos de inversión con criterios de rentabilidad; detener Capex no esencial; vender activos ociosos o subutilizados; establecer política de Capex ligada a CFLO y ROA; priorizar inversiones de mantenimiento vs expansión.
**Severity_Level:** Medium
**Related_Patterns:** CFL-012, CFL-016, CFL-056, CFL-085

### CFL-012
**Pattern_Name:** Inversiones Financiadas con Flujo Operativo Débil
**Category:** Flujo de Inversión
**Description:** La empresa financia sus inversiones en activos principalmente con un CFLO débil, desviando recursos críticos para operaciones o aumentando peligrosamente su deuda.
**Observable_Symptoms:** CFLO insuficiente para cubrir Capex; necesidad de deuda para financiar inversiones; Capex + servicio de deuda > CFLO; la empresa invierte pero no genera efectivo para pagar esas inversiones.
**Early_Warning_Signals:** Capex > CFLO; Cobertura de Capex con CFLO < 1.0; Deuda Neta / CFLO en aumento; Intereses / CFLO en aumento; relación Capex/CFLO > 0.8.
**Typical_Causes:** Decisiones de inversión desacopladas de la capacidad de generación de caja; presión de accionistas por crecimiento; planificación financiera deficiente; exceso de optimismo en proyecciones de CFLO.
**Business_Impact:** Dependencia de deuda para capex que aumenta el riesgo financiero; presión sobre CFLO para servir deuda e inversión; menor flexibilidad financiera; riesgo de incumplimiento si CFLO se deteriora.
**Metrics_To_Check:** Capex / CFLO; Cobertura de Capex (CFLO - Intereses / Capex); Deuda Neta / CFLO; Ratio de Apalancamiento; CFLO Libre después de Capex.
**Diagnostic_Questions:** ¿Cuánto del CFLO se destina a Capex? ¿La empresa puede mantener su nivel de inversión si el CFLO disminuye? ¿Las inversiones están generando el retorno esperado? ¿Hay activos que se puedan arrendar en lugar de comprar?
**Recommended_Actions:** Evaluar cada proyecto de inversión con criterios de CFLO; priorizar inversiones de mantenimiento sobre expansión; considerar leasing/arrendamiento en lugar de compra; establecer regla: Capex no debe exceder X% del CFLO; buscar co-inversión con socios estratégicos.
**Severity_Level:** High
**Related_Patterns:** CFL-011, CFL-016, CFL-056

### CFL-013
**Pattern_Name:** Venta de Activos para Cubrir Operaciones
**Category:** Flujo de Inversión
**Description:** La empresa vende activos fijos o inversiones de largo plazo regularmente para generar efectivo que cubra déficits operativos, indicando deterioro del negocio principal.
**Observable_Symptoms:** Ventas periódicas de propiedades, equipos o inversiones; la empresa genera caja de inversiones pero no de operaciones; reducción de la base de activos productivos; mejora temporal de caja seguida de deterioro.
**Early_Warning_Signals:** FCF (Flujo de Caja de Inversión) positivo por venta de activos en múltiples períodos; CFLO negativo consistente; disminución en propiedad, planta y equipo neto; venta de activos por debajo del valor de mercado.
**Typical_Causes:** Incapacidad de generar CFLO positivo; presión de prestamistas o accionistas por liquidez; falta de acceso a financiamiento; liquidación encubierta del negocio; empresa en estado de declive.
**Business_Impact:** Erosión de la capacidad productiva futura; empresa se vuelve más pequeña y menos competitiva; señal de alarma para inversores y prestamistas; eventual agotamiento de activos para vender; camino hacia la insolvencia.
**Metrics_To_Check:** CFLO vs FCF; Ventas de Activos / CFLO (tendencia); Propiedad, Planta y Equipo Neto (tendencia); Activos Totales (tendencia); FCF recurrente vs no recurrente.
**Diagnostic_Questions:** ¿Es la venta de activos una práctica recurrente o excepcional? ¿Cuántos activos productivos quedan por vender? ¿Se está reduciendo la capacidad de generar ingresos futuros? ¿Hay un plan para restaurar la rentabilidad operativa?
**Recommended_Actions:** Detener la venta de activos productivos; buscar reestructuración de deuda antes de liquidar activos; evaluar si la empresa es viable como negocio en marcha; considerar cierre de operaciones no rentables; buscar inversor o socio estratégico.
**Severity_Level:** Critical
**Related_Patterns:** CFL-005, CFL-085, CFL-089, CFL-090

### CFL-014
**Pattern_Name:** Inversiones en Curso sin Retorno Claro
**Category:** Flujo de Inversión
**Description:** La empresa mantiene proyectos de inversión activos (expansión, desarrollo, tecnología) sin haber definido o validado el retorno esperado, consumiendo caja sin certeza de beneficio futuro.
**Observable_Symptoms:** Múltiples proyectos en curso sin seguimiento de KPIs; inversiones en etapas tempranas sin revisión de continuidad; falta de indicadores de retorno por proyecto; proyectos que se extienden más allá del plazo previsto con sobrecostos.
**Early_Warning_Signals:** Proyectos > 12 meses sin hito de rentabilidad; sobrecosto > 20% del presupuesto original; proyectos sin ROI definido formalmente; múltiples proyectos simultáneos que compiten por recursos.
**Typical_Causes:** Falta de proceso formal de evaluación de inversiones; cultura de "crecer por crecer"; presión de accionistas o directivos por expansión; decisiones emocionales o políticas en lugar de analíticas; falta de gobierno corporativo.
**Business_Impact:** Consumo de caja sin creación de valor; recursos desviados del negocio principal; distracción gerencial; eventual fracaso de proyectos con pérdida total de la inversión; deterioro de la rentabilidad general.
**Metrics_To_Check:** ROI por Proyecto; TIR estimada vs real; Desviación de Presupuesto por Proyecto; Proyectos Activos / CFLO; Tiempo Promedio de Proyectos; Tasa de Abandono de Proyectos.
**Diagnostic_Questions:** ¿Cada proyecto de inversión tiene un ROI definido y aprobado? ¿Hay revisiones periódicas de continuidad de proyectos? ¿Qué proyectos se pueden detener sin pérdida significativa? ¿Hay proyectos que ya debieron cancelarse por bajo rendimiento?
**Recommended_Actions:** Establecer proceso formal de evaluación y seguimiento de inversiones; detener proyectos sin ROI claro; implementar política de kill criteria para proyectos; asignar presupuesto de inversión limitado y por aprobación; revisar cartera de proyectos trimestralmente.
**Severity_Level:** Medium
**Related_Patterns:** CFL-011, CFL-012, CFL-016, CFL-056

### CFL-015
**Pattern_Name:** Reinversión Insuficiente
**Category:** Flujo de Inversión
**Description:** La empresa invierte consistentemente menos que la depreciación, indicando que no está manteniendo su base de activos productivos, lo que lleva a deterioro operativo futuro.
**Observable_Symptoms:** Equipos y maquinaria envejecidos; instalaciones en mal estado; aumento en averías y mantenimiento correctivo; quejas de clientes por calidad del producto o servicio; pérdida de eficiencia operativa.
**Early_Warning_Signals:** Capex / Depreciación < 0.7 por 2+ años; aumento en gastos de mantenimiento; edad promedio de activos fijos en aumento; rotura de equipos frecuente; disminución en capacidad productiva.
**Typical_Causes:** CFLO insuficiente para reinvertir; priorización de pago de deuda sobre inversión; falta de visión a largo plazo; dueños extrayendo efectivo en lugar de reinvertir; empresa en declive que no invierte en el futuro.
**Business_Impact:** Deterioro de la competitividad; pérdida de eficiencia productiva; aumento de costos de mantenimiento; eventual obsolescencia; menor capacidad de generar ingresos futuros; pérdida de cuota de mercado.
**Metrics_To_Check:** Capex / Depreciación; Edad Promedio de Activos Fijos; Gastos de Mantenimiento / Activos Fijos; Capacidad Productiva (tendencia); Eficiencia Operativa (Costo por Unidad).
**Diagnostic_Questions:** ¿Cuánto tiempo puede operar la empresa con su actual nivel de inversión? ¿Los activos actuales pueden mantener la producción el próximo año? ¿Hay un plan de inversión para los próximos 3-5 años? ¿El mantenimiento correctivo está aumentando?
**Recommended_Actions:** Elaborar plan de inversiones mínimo para mantener competitividad; destinar al menos el 70% de la depreciación a reinversión; priorizar inversiones críticas para la operación; considerar financiamiento específico para renovación de activos; evaluar si el negocio sigue siendo viable.
**Severity_Level:** High
**Related_Patterns:** CFL-011, CFL-056, CFL-085

### CFL-016
**Pattern_Name:** Expansión de Capacidad sin Demanda
**Category:** Flujo de Inversión
**Description:** La empresa invierte en ampliar capacidad productiva sin que exista demanda actual o proyectada que justifique la inversión, generando activos ociosos y presión de caja.
**Observable_Symptoms:** Nueva capacidad instalada no utilizada; inversión en plantas, equipos o personal sin aumento de ventas; capacidad ociosa creciente; costos fijos que aumentan sin incremento de ingresos.
**Early_Warning_Signals:** Capacidad Utilizada < 60% después de expansión; Ventas / Activos Fijos en descenso; Costos Fijos / Ventas en aumento; inversión completada sin contratos que la respalden; proyecciones de demanda no cumplidas.
**Typical_Causes:** Optimismo excesivo en proyecciones de demanda; decisión basada en intuición sin análisis de mercado; presión competitiva para tener capacidad disponible; inversión en anticipación a demanda que no se materializa; error estratégico.
**Business_Impact:** Activos ociosos que generan costo (depreciación, mantenimiento, seguros); presión sobre CFLO por inversión no productiva; menor rentabilidad sobre activos; posible necesidad de desinversión con pérdida; deterioro de ratios financieros.
**Metrics_To_Check:** Capacidad Utilizada (post-expansión); Rotación de Activos Fijos; ROA; Costo de Capacidad Ociosa; Punto de Equilibrio en Unidades vs Capacidad; Diferencia entre Demanda Real y Proyectada.
**Diagnostic_Questions:** ¿Qué porcentaje de la nueva capacidad se está utilizando? ¿Hay contratos o pedidos que justifiquen la expansión? ¿Cuánto tiempo tomará llenar la capacidad instalada? ¿Cuál es el costo mensual de mantener la capacidad ociosa? ¿Se puede arrendar o vender el exceso de capacidad?
**Recommended_Actions:** Detener nuevas inversiones en expansión hasta llenar capacidad actual; explorar arrendamiento de capacidad ociosa; evaluar venta de activos no utilizados; ajustar estructura de costos fijos a nivel de capacidad real; enfocar esfuerzo comercial en llenar capacidad instalada.
**Severity_Level:** Medium
**Related_Patterns:** CFL-011, CFL-012, CFL-014, CFL-056

### CFL-017
**Pattern_Name:** Inversión en Tecnología sin Mejora de CFLO
**Category:** Flujo de Inversión
**Description:** La empresa realiza inversiones significativas en tecnología (software, automatización, digitalización) que no se traducen en mejora del CFLO, indicando mala implementación o retorno insuficiente.
**Observable_Symptoms:** Implementación de sistemas sin cambios operativos visibles; inversión en tecnología pero procesos siguen igual; costos de TI aumentan sin reducción en otros costos; empleados no usan las nuevas herramientas; CFLO no mejora después de la inversión.
**Early_Warning_Signals:** Gastos de TI / Ventas en aumento sin mejora en eficiencia; proyectos tecnológicos que exceden plazo y presupuesto; baja adopción de nuevas herramientas por empleados; retorno no medido o no alcanzado; CFLO estable o decreciente post-implementación.
**Typical_Causes:** Inversión en tecnología por moda o presión competitiva sin análisis de necesidad; implementación deficiente sin cambio de procesos; falta de capacitación y gestión del cambio; tecnología incorrecta para las necesidades del negocio; expectativas irreales de retorno.
**Business_Impact:** Inversión sin retorno que consume caja; frustración organizacional; resistencia a futuras inversiones tecnológicas; desventaja competitiva por no obtener los beneficios esperados; costo hundido que no se puede recuperar.
**Metrics_To_Check:** CFLO Antes vs Después de Inversión Tecnológica; ROI de Proyectos TI; Tasa de Adopción de Nuevas Herramientas; Productividad por Empleado (pre vs post); Gastos TI / Ventas (tendencia); Tiempo de Implementación vs Planificado.
**Diagnostic_Questions:** ¿Se midió el ROI esperado antes de la inversión? ¿Se está midiendo el ROI real después? ¿Los empleados usan las nuevas herramientas? ¿Hubo un proceso de gestión del cambio adecuado? ¿La tecnología resolvió el problema que debía resolver?
**Recommended_Actions:** Realizar evaluación post-implementación de todas las inversiones tecnológicas; identificar causas del bajo retorno y corregirlas; intensificar capacitación y gestión del cambio; detener nuevas inversiones en tecnología hasta que las actuales rindan; considerar si la tecnología actual debe reemplazarse o desecharse.
**Severity_Level:** Medium
**Related_Patterns:** CFL-011, CFL-014, CFL-056


## Flujo Financiero

### CFL-018
**Pattern_Name:** Refinanciación Constante de Deuda
**Category:** Flujo Financiero
**Description:** La empresa refinancia deuda de manera recurrente porque no puede pagar el principal con CFLO, volviendo la deuda permanente en lugar de temporal.
**Observable_Symptoms:** Nueva deuda que se toma para pagar deuda anterior; el saldo de deuda no disminuye a pesar de pagos regulares; llamadas frecuentes a prestamistas para renegociar; estructura de deuda cada vez más compleja.
**Early_Warning_Signals:** Relación Deuda Neta / EBITDA constante o creciente; Pago de Principal siempre refinanciado; la empresa no ha reducido su deuda en 2+ años; gastos financieros estables o crecientes; múltiples prestamistas involucrados.
**Typical_Causes:** CFLO insuficiente para pagar principal; apalancamiento excesivo inicial; condiciones de deuda no alineadas con la capacidad de pago; crecimiento financiado con deuda; falta de disciplina de desapalancamiento.
**Business_Impact:** Deuda que se vuelve permanente; mayor exposición a cambios en tasas de interés; dependencia de la buena voluntad de prestamistas; riesgo de que un prestamista se niegue a refinanciar; eventual crisis de deuda.
**Metrics_To_Check:** Deuda Neta / EBITDA (tendencia); Cobertura de Intereses; CFLO / Servicio de Deuda; Plazo Promedio de Deuda; Número de Refinanciaciones por Año; Deuda Bancaria / Deuda Total.
**Diagnostic_Questions:** ¿Cuántas veces se ha refinanciado la deuda en los últimos 3 años? ¿Hay capacidad de generar CFLO suficiente para pagar el principal? ¿Qué pasa si un prestamista se niega a refinanciar? ¿Hay activos libres de gravamen para nueva deuda? ¿Se puede convertir deuda en capital?
**Recommended_Actions:** Desarrollar plan de desapalancamiento realista; buscar deuda de largo plazo alineada con capacidad de pago; considerar venta de activos no estratégicos para reducir deuda; evaluar conversión de deuda en capital; mejorar CFLO antes de buscar nueva deuda.
**Severity_Level:** High
**Related_Patterns:** CFL-019, CFL-085, CFL-088, CFL-090, CFL-092

### CFL-019
**Pattern_Name:** Pago de Deuda con Nuevo Endeudamiento
**Category:** Flujo Financiero
**Description:** La empresa paga deuda existente exclusivamente con nuevos préstamos (no con CFLO), lo que la mantiene en un ciclo perpetuo de endeudamiento sin reducción de apalancamiento.
**Observable_Symptoms:** Pagos de deuda seguidos inmediatamente de nuevos desembolsos de préstamos; saldo de deuda sin cambios sustanciales; estructura de deuda tipo bola de nieve; el pago de intereses consume CFLO.
**Early_Warning_Signals:** Nuevos préstamos >= pagos de deuda en cada período; Deuda Neta estable a pesar de pagos; Intereses / CFLO en aumento; la empresa no genera CFLO libre después de intereses; tasa de apalancamiento no mejora.
**Typical_Causes:** CFLO insuficiente para pagar principal y funcionar; dependencia de crédito para operar; deuda contratada a plazos muy cortos; política agresiva de apalancamiento; falta de generación de efectivo del negocio.
**Business_Impact:** Deuda permanente; aumento del costo financiero acumulado; exposición a cambios en tasas; riesgo de refinanciación; eventual punto de inflexión donde la deuda se vuelve impagable.
**Metrics_To_Check:** Nuevo Endeudamiento / Pago de Deuda; Deuda Neta (tendencia); CFLO / Intereses; CFLO / (Intereses + Pago Principal); Apalancamiento Financiero.
**Diagnostic_Questions:** ¿Cuánto tiempo lleva este ciclo de pagar deuda con nueva deuda? ¿Existe un plan para salir de este ciclo? ¿Cuánto de CFLO se requiere para pagar el servicio de deuda? ¿Hay activos subyacentes que respalden la deuda? ¿Los accionistas pueden aportar capital?
**Recommended_Actions:** Detener el ciclo: buscar una reestructuración integral de deuda; establecer meta de reducción de deuda con hitos; destinar un % del CFLO a pago de principal sin refinanciar; considerar capitalización de deuda; mejorar CFLO como prioridad estratégica.
**Severity_Level:** Critical
**Related_Patterns:** CFL-018, CFL-085, CFL-088, CFL-090

### CFL-020
**Pattern_Name:** Dividendos Incompatibles con CFLO
**Category:** Flujo Financiero
**Description:** La empresa distribuye dividendos a accionistas a pesar de que el CFLO no los respalda, forzando un déficit de caja o la toma de deuda para pagarlos.
**Observable_Symptoms:** Pago de dividendos consistente pero CFLO débil; venta de activos o nuevo endeudamiento para pagar dividendos; CFLO libre después de dividendos negativo; discordia entre accionistas por política de dividendos.
**Early_Warning_Signals:** Payout Ratio (Dividendos / Utilidad Neta) > 80%; Dividendos / CFLO > 0.5; CFLO después de dividendos negativo; deuda que aumenta en períodos de pago de dividendos; CFLO decreciente con dividendos crecientes.
**Typical_Causes:** Accionistas que dependen de los dividendos para su ingreso personal; presión de accionistas mayoritarios; falta de comprensión de la salud de caja real; priorización de retorno al accionista sobre reinversión; acuerdo previo no revisado.
**Business_Impact:** Erosión de la caja de la empresa; necesidad de deuda para financiar dividendos; menor capacidad de inversión y crecimiento; riesgo de incumplimiento de deuda; conflicto entre accionistas.
**Metrics_To_Check:** Dividendos / CFLO; Payout Ratio (Dividendos / Utilidad Neta); Dividendos / CFLO Libre; CFLO después de Dividendos; Tasa de Crecimiento de Dividendos vs CFLO.
**Diagnostic_Questions:** ¿Los dividendos se pagan con CFLO o con deuda? ¿Qué pasa si se suspenden los dividendos por un año? ¿Los accionistas están dispuestos a reinvertir dividendos en la empresa? ¿Hay un acuerdo formal de política de dividendos ligado a CFLO? ¿Se ha considerado dividendo en acciones en lugar de efectivo?
**Recommended_Actions:** Establecer política de dividendos ligada a CFLO (no solo a utilidad); suspender dividendos temporalmente hasta recuperar CFLO; proponer dividendo en acciones como alternativa; educar a accionistas sobre la importancia de la salud de caja; acordar fórmula de dividendos: máx. 30% del CFLO promedio.
**Severity_Level:** Medium
**Related_Patterns:** CFL-001, CFL-003, CFL-085, CFL-090

### CFL-021
**Pattern_Name:** Aporte de Capital por Socios como Única Fuente
**Category:** Flujo Financiero
**Description:** La empresa depende exclusivamente de aportes de capital de los socios para cubrir déficits operativos, lo que indica que el negocio no es autosostenible.
**Observable_Symptoms:** Aportes de capital recurrentes de accionistas; la empresa no genera CFLO positivo por sí sola; cada cierto período los socios deben inyectar efectivo; aumento de capital frecuente sin crecimiento correspondiente.
**Early_Warning_Signals:** Aportes de Capital / CFLO > 1.0 en múltiples períodos; CFLO negativo consistente; la empresa no puede sobrevivir sin aportes de socios; frecuencia de aportes aumenta con el tiempo; aportes no ligados a expansión sino a operación.
**Typical_Causes:** Modelo de negocio no viable sin financiamiento externo; crecimiento que no genera retorno; gastos operativos estructuralmente superiores a ingresos; falta de disciplina de gastos; negocio en etapa prematura que no madura.
**Business_Impact:** Cansancio y desgaste de los socios; imposibilidad de escalar sin dilución constante; riesgo de abandono del negocio por los socios; percepción de negocio no viable para terceros; valorización negativa.
**Metrics_To_Check:** Aportes de Capital / CFLO; Frecuencia de Aportes; CFLO Ajustado (excluyendo aportes); Dependencia de Financiamiento de Socios; Tiempo para Alcanzar CFLO Positivo.
**Diagnostic_Questions:** ¿Cuánto tiempo más están dispuestos los socios a aportar capital? ¿Hay un plan concreto para alcanzar CFLO positivo? ¿Qué cambios estructurales se requieren para eliminar la dependencia de aportes? ¿Se ha considerado cerrar el negocio si no es viable? ¿Los socios pueden seguir aportando?
**Recommended_Actions:** Establecer meta clara de fecha para alcanzar CFLO positivo; reducir gastos estructurales drásticamente; renegociar alquileres, salarios y costos fijos; considerar pivote del modelo de negocio; si no hay viabilidad, evaluar cierre ordenado.
**Severity_Level:** Critical
**Related_Patterns:** CFL-001, CFL-085, CFL-090

### CFL-022
**Pattern_Name:** Dependencia de Líneas de Crédito Revolventes
**Category:** Flujo Financiero
**Description:** La empresa mantiene un saldo permanentemente alto y constante en líneas de crédito revolventes, usándolas como capital de trabajo permanente en lugar de financiamiento temporal.
**Observable_Symptoms:** Líneas de crédito siempre al límite o cerca; giros diarios para cubrir operaciones; pago y nueva disposición en el mismo día; imposibilidad de reducir el saldo de la línea; solicitudes de aumento de límite frecuentes.
**Early_Warning_Signals:** Uso Promedio de Línea de Crédito > 80% del límite por 6+ meses; Línea de Crédito / Ventas constante o creciente; la línea nunca se paga a cero; interés pagado por línea similar a deuda de largo plazo; banco solicita reducción de exposición.
**Typical_Causes:** Capital de trabajo estructuralmente insuficiente; CFLO que no cubre necesidades operativas; crecimiento que requiere más financiamiento del disponible; política de cobranzas laxa; falta de financiamiento de largo plazo adecuado.
**Business_Impact:** Alto costo financiero por uso permanente de crédito caro; exposición a reducción o cancelación de la línea; riesgo de que el banco exija pago inmediato; dependencia crítica del banco para operar; deterioro de la relación bancaria.
**Metrics_To_Check:** Uso Promedio / Límite de Línea; Días de Uso Continuo de Línea; Intereses de Líneas / CFLO; Líneas Revolventes / Deuda Total; % del Tiempo con Saldo > 80%.
**Diagnostic_Questions:** ¿La línea de crédito es realmente revolvente o es capital de trabajo permanente? ¿Cuánto tiempo lleva la línea permanentemente utilizada? ¿Qué pasaría si el banco reduce o cancela la línea? ¿Hay otras fuentes de financiamiento disponibles? ¿Se ha solicitado convertir en préstamo a plazo?
**Recommended_Actions:** Solicitar conversión de parte de la línea en préstamo a plazo; reducir gradualmente la dependencia de la línea mejorando CFLO; buscar fuentes alternativas de financiamiento; negociar compromiso de reducir saldos con el banco; establecer meta de usar línea solo para estacionalidad.
**Severity_Level:** High
**Related_Patterns:** CFL-023, CFL-068, CFL-081, CFL-089, CFL-090

### CFL-023
**Pattern_Name:** Financiación de Largo Plazo para Capital de Trabajo
**Category:** Flujo Financiero
**Description:** La empresa utiliza deuda de largo plazo para financiar necesidades de capital de trabajo, lo que es estructuralmente ineficiente y puede indicar que el negocio no genera suficiente efectivo para su operación.
**Observable_Symptoms:** Préstamos a 3-5 años cuyo destino real es capital de trabajo; descalce entre plazo del préstamo y duración del activo financiado; la empresa usa deuda larga para cubrir déficit operativo; renovación constante de préstamos.
**Early_Warning_Signals:** Deuda de LP / NWC > 1.0; Deuda de LP en aumento pero activos fijos estables; préstamos de LP se agotan rápidamente en gastos operativos; porción corriente de deuda LP en aumento.
**Typical_Causes:** Incapacidad de generar CFLO para capital de trabajo; falta de acceso a financiamiento de corto plazo adecuado; crecimiento que exige más capital de trabajo; estructura financiera desalineada; mala planificación financiera.
**Business_Impact:** Costo financiero más alto que el necesario; descalce de plazos que aumenta riesgo de liquidez; menor flexibilidad financiera; uso ineficiente de capacidad de endeudamiento de LP; riesgo de incumplimiento por presión de cuotas.
**Metrics_To_Check:** Deuda LP / NWC; Deuda LP / Activos Fijos; Destino Real de Préstamos LP vs Declarado; CFLO / Servicio de Deuda LP; Porción Corriente / Deuda LP Total.
**Diagnostic_Questions:** ¿Por qué no se usa financiamiento de corto plazo para capital de trabajo? ¿El costo del financiamiento de LP es menor que alternativas de CP? ¿Hay activos fijos que respalden la deuda de LP? ¿Se puede reestructurar la deuda a plazos más cortos y menor costo?
**Recommended_Actions:** Reestructurar deuda: convertir LP en líneas de crédito revolventes; buscar financiamiento específico para capital de trabajo (factoraje, confirming); liberar activos fijos de garantías para respaldar deuda LP apropiada; mejorar CFLO para reducir necesidad de financiamiento externo.
**Severity_Level:** Medium
**Related_Patterns:** CFL-022, CFL-054, CFL-081, CFL-086

### CFL-024
**Pattern_Name:** Salidas Financieras Superan Entradas Financieras
**Category:** Flujo Financiero
**Description:** Los egresos por actividades financieras (pago de deuda, intereses, dividendos) superan consistentemente los ingresos financieros (nuevos préstamos, aportes de capital), indicando presión sobre la caja.
**Observable_Symptoms:** Pago de deuda e intereses que excede nuevo financiamiento obtenido; CFLO que debe cubrir la diferencia; dividendos pagados superan nuevo capital aportado; reducción de deuda pero a costa de caja operativa.
**Early_Warning_Signals:** Flujo de Caja Financiero Neto Negativo por 3+ períodos; Intereses / CFLO en aumento; Dividendos / CFLO > 0.3; la empresa consume caja pagando compromisos financieros; CFLO no cubre salidas financieras.
**Typical_Causes:** Proceso de desapalancamiento agresivo; CFLO insuficiente para cubrir compromisos financieros; dividendos no alineados con capacidad de pago; estructura de deuda con condiciones onerosas; concentración de vencimientos de deuda.
**Business_Impact:** Presión severa sobre la caja; posible necesidad de vender activos o renegociar; riesgo de incumplimiento de deuda; estrés financiero para la organización; limitación de crecimiento e inversión.
**Metrics_To_Check:** Flujo de Caja Financiero Neto; Cobertura de Servicio de Deuda; Intereses / CFLO; CFLO después de Servicio de Deuda; Relación Salidas Financieras / Entradas Financieras.
**Diagnostic_Questions:** ¿Cuánto tiempo puede la empresa mantener salidas financieras superiores a entradas? ¿Hay flexibilidad para renegociar pagos de deuda? ¿Se pueden reducir dividendos temporalmente? ¿Hay activos disponibles para generar efectivo de inversión? ¿Cuándo se normaliza el flujo financiero?
**Recommended_Actions:** Renegociar calendario de pagos de deuda (extender plazos); suspender dividendos temporalmente; buscar nuevos aportes de capital si es necesario; priorizar pago de deuda más cara primero; preparar proyecciones para identificar cuándo se normaliza.
**Severity_Level:** High
**Related_Patterns:** CFL-018, CFL-019, CFL-020, CFL-085, CFL-088

### CFL-025
**Pattern_Name:** Cobertura de Deuda Vía Efectivo de Operaciones
**Category:** Flujo Financiero
**Description:** La empresa paga el servicio de deuda (intereses + principal) exclusivamente con efectivo operativo, sin generar excedente, lo que la deja sin margen para imprevistos.
**Observable_Symptoms:** CFLO apenas cubre servicio de deuda; después de pagar deuda, no queda efectivo; la empresa no tiene capacidad de ahorro; cualquier desviación en CFLO genera problemas de pago.
**Early_Warning_Signals:** DSCR (CFLO / Servicio de Deuda) entre 1.0 y 1.2; CFLO Libre después de Deuda es cero o negativo; no hay margen para caídas de ventas o aumentos de costos; cualquier gasto imprevisto requiere nueva deuda.
**Typical_Causes:** Endeudamiento al límite de capacidad de pago; CFLO estructuralmente bajo; exceso de deuda contratada; falta de reservas de liquidez; prioridad absoluta al pago de deuda.
**Business_Impact:** Cero flexibilidad financiera; alta vulnerabilidad a shocks; imposibilidad de invertir en crecimiento; estrés permanente de caja; riesgo de incumplimiento ante cualquier desviación.
**Metrics_To_Check:** DSCR (CFLO / Servicio de Deuda); CFLO Libre (CFLO - Servicio de Deuda); CFLO / Intereses; Margen de Seguridad (CFLO - Servicio de Deuda) / Ventas; Ratio de Cobertura de Intereses.
**Diagnostic_Questions:** ¿Qué pasa si el CFLO cae 10%? ¿Se puede reducir el servicio de deuda (extender plazos)? ¿Hay fuentes alternativas de efectivo? ¿Se ha considerado renegociar la deuda para reducir cuotas? ¿Hay activos líquidos para emergencias?
**Recommended_Actions:** Renegociar deuda para extender plazos y reducir cuotas; construir reserva de efectivo de emergencia aunque sea pequeña; mejorar CFLO mediante gestión de capital de trabajo; considerar período de gracia para servicio de deuda; diversificar fuentes de ingresos.
**Severity_Level:** Critical
**Related_Patterns:** CFL-018, CFL-024, CFL-085, CFL-088


## Ciclo de Conversión de Efectivo

### CFL-026
**Pattern_Name:** CCC en Aumento Constante
**Category:** Ciclo de Conversión de Efectivo
**Description:** El Ciclo de Conversión de Efectivo (CCC) muestra una tendencia creciente sostenida, lo que indica que la empresa tarda cada vez más en convertir sus operaciones en efectivo.
**Observable_Symptoms:** El tiempo entre pagar a proveedores y cobrar a clientes se alarga; necesidad creciente de capital de trabajo; presión sobre líneas de crédito; quejas de áreas comerciales sobre restricciones de crédito.
**Early_Warning_Signals:** CCC aumentando 5+ días por año; incremento en Días de Inventario (DPI); incremento en Días de Cuentas por Cobrar (CPP); reducción en Días de Cuentas por Pagar (DPP); relación CCC / Plazo de Crédito Bancario en aumento.
**Typical_Causes:** Política de crédito laxa para impulsar ventas; acumulación de inventario por mala gestión de demanda; proveedores exigen plazos más cortos; clientes que pagan cada vez más tarde; falta de integración entre áreas comercial, operaciones y finanzas.
**Business_Impact:** Mayor necesidad de capital de trabajo; menor rentabilidad por mayor inversión en NWC; tensión de caja; menor capacidad de crecimiento; deterioro de ratios de liquidez.
**Metrics_To_Check:** CCC (Días de Cobro + Días de Inventario - Días de Pago); Tendencia de CCC (12 meses); Componentes del CCC por separado; CCC por Segmento / Línea de Negocio; CCC / Ciclo Operativo Bruto.
**Diagnostic_Questions:** ¿Qué componente del CCC está empeorando? ¿Hay diferencias significativas por línea de negocio? ¿La política de crédito es consistente con la estrategia comercial? ¿Se monitorea el CCC mensualmente? ¿Hay incentivos para reducir el CCC?
**Recommended_Actions:** Monitorear CCC mensualmente con desglose por componente; establecer metas de reducción de CCC; implementar políticas de crédito más estrictas; optimizar niveles de inventario; negociar plazos más largos con proveedores; alinear incentivos comerciales con objetivos de CCC.
**Severity_Level:** Medium
**Related_Patterns:** CFL-027, CFL-028, CFL-029, CFL-030, CFL-054

### CFL-027
**Pattern_Name:** CCC Superior al Promedio del Sector
**Category:** Ciclo de Conversión de Efectivo
**Description:** El CCC de la empresa es significativamente mayor que el promedio de su industria, indicando ineficiencia relativa en la gestión del capital de trabajo.
**Observable_Symptoms:** La empresa necesita más capital de trabajo que sus competidores; dificultad para ofrecer condiciones comerciales competitivas; quejas de clientes por políticas de cobro más estrictas que la competencia; proveedores prefieren a la competencia por mejores condiciones de pago.
**Early_Warning_Signals:** CCC 15+ días mayor que el benchmark sectorial; diferencia creciente vs competidores; Días de Cobro mayores que el promedio del sector; Días de Inventario mayores que el promedio; Días de Pago menores que el promedio del sector.
**Typical_Causes:** Procesos de cobranza ineficientes; política de crédito más laxa que la competencia; gestión de inventario deficiente; menor poder de negociación con proveedores; falta de integración tecnológica (ERP, automatización).
**Business_Impact:** Desventaja competitiva en costos financieros; menor rentabilidad; menor capacidad de inversión; desventaja comercial (no puede ofrecer mejores condiciones); percepción de riesgo por parte de bancos y proveedores.
**Metrics_To_Check:** CCC vs Benchmark Sectorial; Diferencia en Días (positiva o negativa); Componentes del CCC vs Benchmark; Posición en el Ranking Sectorial; Tendencia de la Diferencia.
**Diagnostic_Questions:** ¿Cuál es el CCC promedio del sector? ¿En qué componente específico está la mayor brecha? ¿Hay mejores prácticas del sector que se puedan adoptar? ¿La empresa tiene desventajas estructurales (tamaño, poder de negociación)? ¿Se ha evaluado la adopción de tecnología para mejorar?
**Recommended_Actions:** Benchmarking de componentes del CCC vs mejores prácticas del sector; implementar mejores prácticas identificadas; invertir en tecnología para mejorar cobranzas e inventarios; considerar alianzas estratégicas para mejorar poder de negociación con proveedores.
**Severity_Level:** Medium
**Related_Patterns:** CFL-026, CFL-029, CFL-030, CFL-031

### CFL-028
**Pattern_Name:** Días de Inventario Prolongados
**Category:** Ciclo de Conversión de Efectivo
**Description:** Los días de inventario (DPI) son excesivos y crecientes, inmovilizando efectivo en stock que no se rota con la suficiente rapidez.
**Observable_Symptoms:** Almacenes llenos con producto terminado o materia prima; rotación de inventario decreciente; productos obsoletos o vencidos; costos de almacenamiento crecientes; quejas del área comercial por falta de espacio o variedad.
**Early_Warning_Signals:** DPI aumentando 10+ días año a año; Rotación de Inventario en descenso; Inventario / Ventas en aumento; productos con más de 6 meses en stock; faltantes y excedentes simultáneos.
**Typical_Causes:** Mala planificación de la demanda; compras excesivas por descuento por volumen; falta de coordinación entre compras y ventas; productos con demanda estacional o cambiante; sistema de gestión de inventario inadecuado.
**Business_Impact:** Efectivo inmovilizado en inventario que no genera retorno; costos de almacenamiento, seguros y obsolescencia; riesgo de pérdida por deterioro o cambio de moda; menor capacidad de respuesta a cambios del mercado.
**Metrics_To_Check:** DPI; Rotación de Inventario (Ventas / Inventario Promedio); Inventario / Ventas; % de Inventario Obsoleto; Costo de Mantener Inventario; Cobertura de Inventario (días de venta).
**Diagnostic_Questions:** ¿Qué productos concentran el exceso de inventario? ¿Hay inventario obsoleto o de baja rotación? ¿El sistema de planificación de demanda es adecuado? ¿Se evalúa el costo de mantener inventario vs el descuento por volumen? ¿Hay procesos de revisión periódica de inventario?
**Recommended_Actions:** Implementar sistema de gestión de inventario (Justo a Tiempo); eliminar productos de baja rotación; realizar inventarios físicos frecuentes; mejorar planificación de demanda; establecer niveles máximos y mínimos por producto; considerar dropshipping o producción bajo pedido.
**Severity_Level:** Medium
**Related_Patterns:** CFL-026, CFL-027, CFL-031, CFL-054, CFL-059

### CFL-029
**Pattern_Name:** Días de Cuentas por Cobrar Elevados
**Category:** Ciclo de Conversión de Efectivo
**Description:** Los días de cuentas por cobrar (CPP) son excesivos, indicando que la empresa tarda mucho en cobrar a sus clientes, inmovilizando efectivo en cuentas por cobrar.
**Observable_Symptoms:** Cartera de cuentas por cobrar creciente más rápido que ventas; clientes que pagan con retraso crónico; esfuerzo de cobranza intensivo; provisiones por incobrables crecientes; descalce entre plazos de cobro y pago.
**Early_Warning_Signals:** CPP aumentando 5+ días año a año; CPP > 60 días (dependiendo del sector); Cuentas por Cobrar / Ventas en aumento; % de cartera vencida creciente; edad de la cartera empeorando.
**Typical_Causes:** Política de crédito laxa para ganar mercado; clientes con problemas financieros; procesos de cobranza ineficientes; falta de seguimiento sistemático; descuentos por pronto pago insuficientes o mal diseñados.
**Business_Impact:** Mayor necesidad de capital de trabajo; riesgo de incobrabilidad creciente; efectivo inmovilizado que no genera retorno; menor capacidad de pago a proveedores; tensión de caja permanente.
**Metrics_To_Check:** CPP; Rotación de Cuentas por Cobrar; % de Cartera Vencida; Edad de la Cartera (aging); Provisiones / Cuentas por Cobrar; Eficiencia de Cobranza (Cobrado / Facturado).
**Diagnostic_Questions:** ¿Qué clientes concentran las cuentas por cobrar vencidas? ¿La política de crédito es consistente con la estrategia comercial? ¿Hay procesos de cobranza preventiva? ¿Se evalúa el riesgo crediticio de clientes nuevos? ¿Hay incentivos para la cobranza oportuna?
**Recommended_Actions:** Implementar proceso de cobranza preventiva y seguimiento; segmentar clientes por riesgo crediticio; ajustar plazos de crédito según riesgo; ofrecer descuentos financieramente atractivos por pronto pago; automatizar recordatorios de pago; considerar factoraje selectivo.
**Severity_Level:** Medium
**Related_Patterns:** CFL-026, CFL-027, CFL-035, CFL-037, CFL-042, CFL-054

### CFL-030
**Pattern_Name:** Días de Cuentas por Pagar Comprimidos
**Category:** Ciclo de Conversión de Efectivo
**Description:** La empresa paga a sus proveedores en plazos muy cortos, reduciendo su capacidad de financiamiento operativo y aumentando su necesidad de capital de trabajo.
**Observable_Symptoms:** Plazos de pago muy cortos vs condiciones de mercado; pagos al contado o en pocos días; proveedores no ofrecen crédito; la empresa no aprovecha el financiamiento de proveedores; presión de caja por pagos frecuentes.
**Early_Warning_Signals:** DPP (Días de Pago) < 30 días o menor que el promedio del sector; DPP decreciente; DPP < CPP + DPI (descalce); falta de crédito comercial de proveedores; pagos al contado como norma.
**Typical_Causes:** Bajo poder de negociación con proveedores; proveedores que exigen pago anticipado; falta de historial crediticio con proveedores; compras de emergencia sin negociación; dependencia de proveedor único o monopólico.
**Business_Impact:** Mayor necesidad de capital de trabajo; menor CCC (efecto espejo); desventaja vs competidores con mejores plazos; presión de caja; menor flexibilidad financiera.
**Metrics_To_Check:** DPP; Rotación de Cuentas por Pagar; DPP vs Promedio del Sector; DPP / CPP; Descalce (DPP vs CPP + DPI).
**Diagnostic_Questions:** ¿Por qué los plazos de pago son tan cortos? ¿Hay proveedores dispuestos a otorgar crédito? ¿Se ha negociado activamente con proveedores? ¿Hay alternativas (confirming, financiamiento de proveedores)? ¿El costo del crédito de proveedores es competitivo?
**Recommended_Actions:** Negociar plazos más largos con proveedores actuales; buscar nuevos proveedores con mejores condiciones; implementar confirming para mejorar plazos; consolidar compras para ganar poder de negociación; pagar justo a tiempo (no anticipado) a menos que haya descuento atractivo.
**Severity_Level:** Low
**Related_Patterns:** CFL-026, CFL-027, CFL-031, CFL-054, CFL-083

### CFL-031
**Pattern_Name:** CCC Negativo (Ventaja de Caja)
**Category:** Ciclo de Conversión de Efectivo
**Description:** La empresa opera con CCC negativo, lo que significa que cobra a sus clientes antes de pagar a sus proveedores, generando una ventaja estructural de caja.
**Observable_Symptoms:** La empresa genera efectivo al crecer; el crecimiento se autofinancia; proveedores financian las operaciones; baja necesidad de capital de trabajo; el negocio tiene caja positiva incluso con crecimiento.
**Early_Warning_Signals:** CCC < 0 días; CPP + DPI < DPP; la empresa tiene efectivo neto positivo consistentemente; crecimiento genera más caja; el negocio puede crecer sin financiamiento externo.
**Typical_Causes:** Modelo de negocio con pago anticipado de clientes; plazos de pago a proveedores muy largos; inventario mínimo o rotación ultrarrápida; ventas al contado o con tarjeta; negocios de servicio sin inventario.
**Business_Impact:** Ventaja competitiva significativa; capacidad de crecer sin financiamiento; generación de caja natural; menor riesgo de liquidez; mayor capacidad de inversión.
**Metrics_To_Check:** CCC (negativo); Días de Efectivo Generado; CFLO / Crecimiento de Ventas; Caja Generada por Crecimiento; Capacidad de Autofinanciamiento.
**Diagnostic_Questions:** ¿El CCC negativo es estructural (modelo de negocio) o coyuntural? ¿Se puede mantener con crecimiento? ¿Hay riesgo de que proveedores exijan plazos más cortos? ¿Se puede mejorar aún más? ¿El CCC negativo está siendo gestionado o es solo resultado del modelo?
**Recommended_Actions:** Mantener y monitorear el CCC negativo como ventaja competitiva; no deteriorar la ventaja con malas prácticas; usar el excedente de caja para inversiones estratégicas; negociar con proveedores manteniendo plazos; invertir el efectivo generado para maximizar retorno.
**Severity_Level:** Low (beneficio)
**Related_Patterns:** CFL-026, CFL-030, CFL-058, CFL-062

### CFL-032
**Pattern_Name:** CCC Financiado con Deuda Corto Plazo
**Category:** Ciclo de Conversión de Efectivo
**Description:** La empresa financia la mayor parte de su CCC con deuda de corto plazo, haciéndola vulnerable a cambios en condiciones crediticias y aumentando el riesgo de refinanciación.
**Observable_Symptoms:** Líneas de crédito corto plazo siempre utilizadas; el monto de deuda CP se correlaciona con el CCC; cualquier extensión del CCC requiere más deuda; alta sensibilidad a tasas de interés de CP; renovación constante de créditos.
**Early_Warning_Signals:** Deuda CP / CCC > 0.8; Deuda CP / Deuda Total > 0.5; Intereses de Deuda CP / CFLO en aumento; dependencia de líneas revolventes; el banco es el principal financiador del capital de trabajo.
**Typical_Causes:** Falta de acceso a financiamiento de LP; crecimiento que excede capacidad de autofinanciamiento; márgenes insuficientes para generar CFLO; política de crédito laxa que alarga CPP; subestimación del costo del riesgo de refinanciación.
**Business_Impact:** Exposición a riesgo de tasa de interés; vulnerabilidad a restricción de crédito; costo financiero elevado; estrés de refinanciación constante; riesgo de iliquidez si se corta la línea.
**Metrics_To_Check:** Deuda CP / CCC; Deuda CP / Deuda Total; Costo de Deuda CP vs LP; Cobertura de Intereses; Dependencia de Líneas Revolventes.
**Diagnostic_Questions:** ¿Qué porcentaje del CCC está financiado con deuda CP? ¿Cuál es el costo de esta deuda? ¿Hay financiamiento de LP disponible? ¿Qué pasa si la línea de crédito se reduce? ¿Se puede reducir el CCC para disminuir la necesidad de financiamiento?
**Recommended_Actions:** Reducir el CCC mediante mejor gestión de cobranzas e inventarios; buscar financiamiento de LP para parte del NWC; diversificar fuentes de financiamiento; considerar factoraje o confirming como alternativas; establecer línea de crédito comprometida.
**Severity_Level:** High
**Related_Patterns:** CFL-022, CFL-026, CFL-054, CFL-081, CFL-086

### CFL-033
**Pattern_Name:** Mejora Artificial del CCC por Descuentos Agresivos
**Category:** Ciclo de Conversión de Efectivo
**Description:** La empresa mejora su CCC ofreciendo descuentos agresivos por pronto pago que pueden estar destruyendo valor, ya que el costo del descuento supera el beneficio de la reducción del CCC.
**Observable_Symptoms:** Alta proporción de clientes tomando descuentos por pronto pago; margen bruto comprimido; descuentos financieros crecientes como % de ventas; mejora en días de cobro pero deterioro de márgenes.
**Early_Warning_Signals:** Costo del Descuento (tasa implícita) > Costo de Capital; Descuentos / Ventas en aumento; margen neto decreciente con CPP mejorando; clientes que antes pagaban a término ahora toman descuento.
**Typical_Causes:** Política de descuentos no evaluada financieramente; necesidad desesperada de efectivo; falta de alternativas de financiamiento; cultura de descuentos no cuestionada; medición de desempeño enfocada solo en CCC.
**Business_Impact:** Destrucción de valor aunque el CCC mejore; menor rentabilidad neta; percepción de debilidad financiera; dependencia de descuentos para mantener flujo; guerra de descuentos con competidores.
**Metrics_To_Check:** Costo Efectivo del Descuento (tasa anualizada); Descuentos / Ventas; Margen Neto Ajustado por Descuentos; CCC Ajustado por Costo de Descuento; Relación Costo del Descuento vs Costo de Capital.
**Diagnostic_Questions:** ¿Cuál es la tasa efectiva anual del descuento ofrecido? ¿Es menor que el costo de otras fuentes de financiamiento? ¿Se ha evaluado el impacto en el margen neto? ¿Clientes actuales pagarían igual sin descuento? ¿Hay alternativas más baratas para acelerar cobro?
**Recommended_Actions:** Evaluar financieramente la política de descuentos; reducir descuentos a niveles financieramente justificables; buscar fuentes de financiamiento más baratas que los descuentos; segmentar clientes; reemplazar descuentos con cobranza más efectiva.
**Severity_Level:** Medium
**Related_Patterns:** CFL-008, CFL-029, CFL-038, CFL-040

### CFL-034
**Pattern_Name:** CCC Asimétrico entre Líneas de Negocio
**Category:** Ciclo de Conversión de Efectivo
**Description:** El CCC varía significativamente entre diferentes líneas de negocio, productos o segmentos de clientes, y la empresa no gestiona estas diferencias, perdiendo oportunidades de optimización.
**Observable_Symptoms:** Algunas líneas de negocio generan efectivo rápidamente mientras otras lo consumen; la empresa no diferencia condiciones comerciales por segmento; falta de visibilidad del CCC por unidad de negocio; decisiones tomadas con CCC promedio que no refleja la realidad.
**Early_Warning_Signals:** Diferencia de CCC entre líneas > 30 días; líneas con CCC positivo y negativo coexistiendo; falta de reportes de CCC por segmento; una línea de negocio financia a otra; clientes con condiciones homogéneas pero comportamientos heterogéneos.
**Typical_Causes:** Falta de segmentación en políticas comerciales; sistemas de información que no desglosan CCC; cultura de "tratar a todos por igual"; desconocimiento de la rentabilidad por cliente/segmento; falta de incentivos diferenciados.
**Business_Impact:** Oportunidades perdidas de optimización; líneas rentables contablemente pero no de caja; subsidio cruzado de clientes; decisiones subóptimas de mix de ventas; tensión de caja por segmentos ineficientes.
**Metrics_To_Check:** CCC por Línea de Negocio / Segmento; CCC por Cliente (Top 20); Diferencia Máxima de CCC entre Segmentos; Margen de Contribución Ajustado por CCC por Segmento; ROA por Segmento Ajustado por CCC.
**Diagnostic_Questions:** ¿Hay visibilidad del CCC por línea de negocio? ¿Qué segmentos generan caja y cuáles la consumen? ¿Las condiciones comerciales reflejan el riesgo y costo de cada segmento? ¿Hay clientes que no son rentables considerando su CCC? ¿Se puede incentivar la venta de segmentos con mejor CCC?
**Recommended_Actions:** Implementar reporting de CCC por línea de negocio; segmentar políticas de crédito por tipo de cliente; ajustar precios o condiciones según el CCC de cada segmento; incentivar comercialmente la venta de productos con mejor CCC; desincentivar o rediseñar segmentos con CCC muy alto.
**Severity_Level:** Medium
**Related_Patterns:** CFL-026, CFL-027, CFL-029, CFL-031


## Cobranzas

### CFL-035
**Pattern_Name:** Días de Cobro en Aumento
**Category:** Cobranzas
**Description:** Los días promedio de cobro (CPP) muestran una tendencia creciente sostenida, indicando que los clientes tardan cada vez más en pagar, deteriorando el flujo de caja.
**Observable_Symptoms:** El tiempo entre facturación y cobro se alarga; quejas del área de tesorería por falta de efectivo; la cartera de cuentas por cobrar crece más rápido que las ventas; seguimiento de cobranza cada vez más intensivo.
**Early_Warning_Signals:** CPP aumentando 5+ días respecto al año anterior; CPP superando el plazo de crédito otorgado; % de cartera vencida en aumento; clientes que antes pagaban a tiempo ahora se retrasan.
**Typical_Causes:** Política de crédito laxa para impulsar ventas; deterioro de la situación financiera de los clientes; falta de proceso de cobranza sistemático; departamento de cobranza con recursos insuficientes; competencia que ofrece mejores plazos.
**Business_Impact:** Mayor inversión en capital de trabajo; tensión de caja permanente; aumento de riesgo de incobrabilidad; necesidad de financiamiento externo para cubrir el descalce; menor rentabilidad por mayor costo financiero.
**Metrics_To_Check:** CPP (tendencia 12 meses); % de Cartera Vencida por tramos (30, 60, 90+ días); Eficiencia de Cobranza (Cobrado / Facturado del período); Rotación de Cuentas por Cobrar; Días de Cobro por Segmento de Clientes.
**Diagnostic_Questions:** ¿En qué segmento de clientes se concentra el aumento de días de cobro? ¿Hay clientes nuevos con peor comportamiento de pago? ¿Se han relajado las condiciones de crédito? ¿El proceso de cobranza es proactivo o reactivo? ¿Hay incentivos para la cobranza?
**Recommended_Actions:** Implementar proceso de cobranza preventiva (recordatorios antes del vencimiento); segmentar clientes por riesgo y ajustar condiciones; automatizar seguimiento de cobranza; establecer política de corte de crédito por mora; ofrecer descuentos financieramente sostenibles por pronto pago.
**Severity_Level:** Medium
**Related_Patterns:** CFL-026, CFL-029, CFL-036, CFL-037, CFL-042

### CFL-036
**Pattern_Name:** Concentración de Deudores
**Category:** Cobranzas
**Description:** Un pequeño número de clientes concentra la mayor parte de las cuentas por cobrar, generando un riesgo significativo de impacto en el flujo de caja si alguno de ellos retrasa o no paga.
**Observable_Symptoms:** Cliente(s) representan > 25% de cuentas por cobrar; mora o retraso de un cliente grande impacta severamente la caja; la empresa evita presionar a clientes grandes por miedo a perderlos; falta de diversificación de la cartera.
**Early_Warning_Signals:** Top 3 clientes > 50% de cuentas por cobrar; un solo cliente > 30% de cuentas por cobrar; mora concentrada en cliente grande; cliente grande con problemas financieros conocidos; ventas concentradas en pocos clientes.
**Typical_Causes:** Dependencia de pocos clientes grandes; estrategia de ventas enfocada en cuentas clave; sector con alta concentración natural (gobierno, grandes empresas); falta de esfuerzo comercial en diversificación; clientes grandes que imponen condiciones.
**Business_Impact:** Riesgo severo de iliquidez si un cliente grande no paga; pérdida de poder de negociación en cobranza; vulnerabilidad ante quiebra de cliente importante; CFLO volátil y poco predecible.
**Metrics_To_Check:** Concentración de Cuentas por Cobrar (Top 1, 3, 5); % de Cuentas por Cobrar sobre Total; Índice de Herfindahl de Cartera; Correlación CFLO vs Pagos de Cliente Principal; Días de Cobro por Cliente Grande.
**Diagnostic_Questions:** ¿Qué pasaría con el flujo de caja si el cliente principal retrasa su pago 60 días? ¿Hay seguro de crédito para los clientes grandes? ¿Se está diversificando activamente la base de clientes? ¿Los contratos con clientes grandes protegen los intereses de cobro?
**Recommended_Actions:** Diversificar base de clientes activamente; contratar seguro de crédito para clientes concentrados; negociar pagos parciales o hitos con clientes grandes; monitorear salud financiera de clientes grandes; mantener reserva de efectivo equivalente a 1-2 ciclos de pago del cliente principal.
**Severity_Level:** High
**Related_Patterns:** CFL-009, CFL-029, CFL-035, CFL-037, CFL-042, CFL-045

### CFL-037
**Pattern_Name:** Morosidad Creciente en Cartera
**Category:** Cobranzas
**Description:** El porcentaje de la cartera de cuentas por cobrar que está vencida aumenta consistentemente, indicando deterioro en la calidad crediticia de los clientes o en la efectividad de la cobranza.
**Observable_Symptoms:** Aumento en el saldo de cuentas por cobrar vencidas; clientes que antes pagaban ahora se retrasan; aumento en provisiones por incobrables; quejas del área de cobranza por falta de recursos; más cuentas pasan a cobranza judicial.
**Early_Warning_Signals:** % de Cartera Vencida > 10% del total; aumento en el ratio de morosidad por 3+ meses consecutivos; deterioro en la calidad de la cartera por tramos de edad; Provisiones / Cuentas por Cobrar en aumento; más clientes en categoría de riesgo alto.
**Typical_Causes:** Relajación de políticas de crédito para impulsar ventas; deterioro económico general que afecta a los clientes; entrada en segmentos de clientes de mayor riesgo; procesos de cobranza ineficientes; falta de verificación de crédito al incorporar clientes.
**Business_Impact:** Mayor inversión en capital de trabajo; pérdidas por incobrables crecientes; deterioro del CFLO; necesidad de más recursos para cobranza; impacto en rentabilidad por provisiones.
**Metrics_To_Check:** % de Cartera Vencida (total y por tramos); Ratio de Morosidad (Cartera Vencida / Cartera Total); Provisiones / Cuentas por Cobrar; Castigos por Incobrables / Ventas; Tasa de Recuperación de Cartera Vencida.
**Diagnostic_Questions:** ¿Qué clientes están contribuyendo más al aumento de la morosidad? ¿Hay un patrón común entre los clientes morosos? ¿Se están aprobando créditos a clientes sin la debida verificación? ¿El proceso de cobranza es oportuno y efectivo? ¿Se han endurecido las políticas de crédito?
**Recommended_Actions:** Endurecer políticas de aprobación de crédito; intensificar gestión de cobranza preventiva y correctiva; segmentar clientes por riesgo y ajustar condiciones; implementar scoring crediticio para nuevos clientes; establecer topes de exposición por cliente; considerar venta de cartera morosa.
**Severity_Level:** High
**Related_Patterns:** CFL-029, CFL-035, CFL-036, CFL-040, CFL-042, CFL-045

### CFL-038
**Pattern_Name:** Descuentos por Pronto Pago como Condición de Venta
**Category:** Cobranzas
**Description:** Los descuentos por pronto pago se han convertido en una condición esperada por los clientes para comprar, erosionando el margen y distorsionando la verdadera dinámica de cobranza.
**Observable_Symptoms:** Prácticamente todos los clientes toman el descuento por pronto pago; el descuento es visto como "parte del precio"; clientes que pagan a término son la excepción; el margen neto está comprimido vs el margen bruto; dificultad para eliminar o reducir descuentos.
**Early_Warning_Signals:** > 80% de clientes toman descuento por pronto pago; Descuentos / Ventas > 3%; clientes nuevos exigen descuento desde el inicio; el margen neto es significativamente menor que el margen bruto; los descuentos no se revisan periódicamente.
**Typical_Causes:** Cultura de descuentos arraigada en la empresa; necesidad histórica de efectivo que llevó a abusar de descuentos; competidores que también ofrecen descuentos agresivos; percepción de que sin descuento no se vende; falta de análisis del costo real del descuento.
**Business_Impact:** Erosión permanente del margen; menor rentabilidad por cada venta; dificultad para eliminar la práctica; percepción de debilidad comercial; guerra de descuentos con competidores.
**Metrics_To_Check:** Descuentos / Ventas (tendencia); % de Clientes que Toman Descuento; Tasa Efectiva Anual del Descuento; Margen Neto vs Margen Bruto; Elasticidad de la Demanda al Descuento.
**Diagnostic_Questions:** ¿Qué porcentaje de clientes tomaría descuento si se redujera? ¿Se ha intentado eliminar o reducir descuentos? ¿Cuál fue el resultado? ¿El descuento es realmente necesario para vender o es una costumbre? ¿Se ha calculado el costo anual total de los descuentos?
**Recommended_Actions:** Reducir gradualmente el porcentaje de descuento; segmentar: eliminar descuento para clientes que pagan igual sin él; comunicar el cambio como "mejora en condiciones comerciales"; diferenciar precio con y sin descuento (no descuento sobre precio base); evaluar si el descuento se puede reemplazar por otros beneficios.
**Severity_Level:** Medium
**Related_Patterns:** CFL-008, CFL-033, CFL-037, CFL-040

### CFL-039
**Pattern_Name:** Cobranza Judicial Frecuente
**Category:** Cobranzas
**Description:** La empresa recurre con frecuencia a instancias judiciales o legales para cobrar a sus clientes morosos, indicando problemas graves en la selección de clientes o en la gestión de cobranza preventiva.
**Observable_Symptoms:** Abogados o estudios jurídicos externos manejando cobranzas; demandas judiciales por cobro recurrentes; costos legales crecientes como % de ventas; clientes que pagan solo ante presión judicial; provisión para incobrables alta.
**Early_Warning_Signals:** Costos Legales de Cobranza / Ventas en aumento; % de Cartera en Cobranza Judicial > 5%; más de 2 demandas por cobro al año; clientes que repiten mora luego de acuerdo judicial; tiempo de recuperación de cartera judicial > 12 meses.
**Typical_Causes:** Política de crédito laxa sin verificación adecuada; clientes seleccionados sin análisis de riesgo; ventas a clientes con historial de mora conocido; falta de proceso de cobranza preventiva; cultura de "vender primero, cobrar después".
**Business_Impact:** Costos legales elevados que erosionan márgenes; desgaste organizacional; relaciones comerciales dañadas; imagen negativa en el mercado; baja tasa de recuperación efectiva.
**Metrics_To_Check:** Costos Legales de Cobranza / Ventas; % de Cartera en Cobranza Judicial; Tasa de Recuperación Judicial vs Extrajudicial; Tiempo Promedio de Cobranza Judicial; Frecuencia de Casos Judiciales.
**Diagnostic_Questions:** ¿Hay un patrón común entre los clientes que terminan en cobranza judicial? ¿Se realiza verificación crediticia antes de vender? ¿Hay un proceso de cobranza preventiva antes de llegar a instancia judicial? ¿Se han evaluado alternativas antes de la vía judicial? ¿La cobranza judicial es realmente costo-efectiva?
**Recommended_Actions:** Fortalecer proceso de verificación crediticia previa; implementar cobranza preventiva con múltiples etapas; evaluar costo-beneficio de la cobranza judicial vs castigo directo; considerar venta de cartera morosa; endurecer políticas de crédito para segmentos de alto riesgo.
**Severity_Level:** Medium
**Related_Patterns:** CFL-035, CFL-037, CFL-040, CFL-042

### CFL-040
**Pattern_Name:** Incobrabilidad Fuera del Rango de la Industria
**Category:** Cobranzas
**Description:** El nivel de incobrabilidad (cuentas incobrables / ventas) de la empresa excede significativamente el rango normal de su industria, indicando problemas en la selección de clientes o gestión de crédito.
**Observable_Symptoms:** Castigos por incobrables recurrentes y significativos; provisiones que sistemáticamente se materializan; comparación con el sector muestra desventaja clara; el equipo comercial se queja de restricciones de crédito pero la incobrabilidad sigue alta.
**Early_Warning_Signals:** Incobrables / Ventas > 2x el promedio del sector; tendencia creciente en castigos; provisiones que regularmente son insuficientes (se necesitan castigos adicionales); clientes nuevos tienen mayor tasa de incobrabilidad.
**Typical_Causes:** Política de crédito demasiado permisiva; falta de segmentación de riesgo; presión comercial por metas de ventas sin considerar riesgo crediticio; clientes de baja calidad; falta de sistemas de scoring crediticio.
**Business_Impact:** Pérdidas directas que erosionan rentabilidad; mayor necesidad de capital de trabajo; CFLO deteriorado por menores cobros; prima de riesgo implícita en precios que puede hacer menos competitiva a la empresa.
**Metrics_To_Check:** Incobrables / Ventas (vs benchmark sectorial); Provisiones / Incobrables Reales; Castigos / Cuentas por Cobrar Promedio; Tasa de Incobrabilidad por Segmento de Clientes.
**Diagnostic_Questions:** ¿Cuál es la tasa de incobrabilidad del sector? ¿En qué segmento de clientes se concentran las pérdidas? ¿Se ajustan las condiciones de crédito según el riesgo del cliente? ¿Hay presión comercial por vender a clientes de alto riesgo? ¿Se revisan los límites de crédito periódicamente?
**Recommended_Actions:** Implementar scoring crediticio; segmentar clientes por riesgo y ajustar condiciones; establecer límites de exposición por cliente; vincular compensación comercial a calidad de cartera (no solo a ventas); considerar seguros de crédito; endurecer políticas de aprobación.
**Severity_Level:** High
**Related_Patterns:** CFL-035, CFL-037, CFL-039, CFL-042, CFL-045

### CFL-041
**Pattern_Name:** Facturación Electrónica con Rechazos Recurrentes
**Category:** Cobranzas
**Description:** La empresa experimenta un alto índice de rechazos o discrepancias en la facturación electrónica, lo que retrasa los cobros y genera ineficiencias administrativas.
**Observable_Symptoms:** Facturas electrónicas rechazadas por datos incorrectos; clientes que objetan facturas recurrentemente; ciclos de facturación que se alargan por correcciones; discrepancias entre lo facturado y lo acordado; atrasos en cobro por facturas no aceptadas.
**Early_Warning_Signals:** Tasa de Rechazo de Facturas > 5%; tiempo entre emisión y aceptación de factura > 10 días; quejas recurrentes de clientes sobre facturación; facturas que requieren 2+ correcciones; diferencias entre pedido y factura frecuentes.
**Typical_Causes:** Procesos de facturación descoordinados con áreas comerciales y operativas; errores en datos de cliente (RFC, condiciones fiscales); discrepancias entre precios acordados y facturados; falta de verificación previa al envío; sistemas de facturación no integrados.
**Business_Impact:** Retraso en el inicio del plazo de cobro; aumento de costos administrativos; relaciones tensas con clientes por errores; deterioro de CPP por días no contados; posible pérdida de descuentos por pronto pago.
**Metrics_To_Check:** Tasa de Rechazo de Facturas; Tiempo Promedio entre Emisión y Aceptación; Número de Correcciones por Factura; Costo Administrativo por Factura Rechazada; Días de Cobro Ajustados por Rechazos.
**Diagnostic_Questions:** ¿Cuáles son las causas más frecuentes de rechazo de facturas? ¿Hay un proceso de pre-validación antes de enviar? ¿Los datos maestros de clientes están actualizados? ¿Hay comunicación entre áreas comercial y facturación? ¿Se mide el impacto de rechazos en los días de cobro?
**Recommended_Actions:** Automatizar validación de datos antes de emisión; implementar doble verificación (automatizada + manual) antes de enviar; mantener datos maestros de clientes actualizados; coordinar con clientes sus requisitos específicos de facturación; medir y publicar tasa de rechazos para crear conciencia.
**Severity_Level:** Low
**Related_Patterns:** CFL-035, CFL-042

### CFL-042
**Pattern_Name:** Clientes que Pagan Siempre con Retraso
**Category:** Cobranzas
**Description:** Un grupo de clientes paga sistemáticamente con retraso respecto a los plazos acordados, generando un descalce crónico entre las condiciones pactadas y la realidad de cobranza.
**Observable_Symptoms:** Ciertos clientes siempre pagan 10-30 días después del vencimiento; los plazos reales de cobro son mayores que los facturados; el equipo comercial conoce el patrón pero no lo corrige; seguimiento especial constante para estos clientes; el CPP reportado no refleja los plazos facturados.
**Early_Warning_Signals:** Clientes con desviación constante de pago > 10 días; diferencia entre CPP y plazo facturado > 15 días; clientes que no responden a recordatorios; el patrón de pago tardío es consistente (no esporádico); más del 20% de clientes pagan sistemáticamente tarde.
**Typical_Causes:** Falta de consecuencias por pago tardío (no se cobran intereses, no se corta crédito); cultura permisiva con clientes importantes; procesos de cobranza reactivos sin seguimiento; poder de negociación del cliente que impone sus plazos; condiciones contractuales no enforceables.
**Business_Impact:** CPP real mayor que el nominal; necesidad de más capital de trabajo; desviación de presupuesto de caja; imposibilidad de planificar flujos con precisión; normalización del mal comportamiento de pago.
**Metrics_To_Check:** Diferencia CPP Real vs Plazo Facturado; % de Clientes con Pago Sistemáticamente Tardío; Días Promedio de Retraso por Cliente; Impacto en CCC del Retraso Sistemático; Tasa de Cumplimiento de Plazos por Cliente.
**Diagnostic_Questions:** ¿Por qué estos clientes no pagan a tiempo? ¿Hay consecuencias por el retraso? ¿Se han renegociado los plazos para reflejar la realidad? ¿El equipo comercial tiene incentivos para hacer cumplir los plazos? ¿Se puede segmentar a estos clientes con condiciones diferentes?
**Recommended_Actions:** Re-negociar plazos formales con estos clientes para reflejar la realidad; implementar cobro automático de intereses por mora; establecer política de corte de crédito por retraso recurrente; ajustar precios para clientes con mal comportamiento de pago; escalar a Dirección cuando un cliente grande paga sistemáticamente tarde.
**Severity_Level:** Medium
**Related_Patterns:** CFL-029, CFL-035, CFL-037, CFL-040

### CFL-043
**Pattern_Name:** Descuentos no Documentados por Cobranza Anticipada
**Category:** Cobranzas
**Description:** La empresa ofrece descuentos por cobranza anticipada que no están formalmente documentados ni evaluados financieramente, generando erosión de margen sin control.
**Observable_Symptoms:** Descuentos que se negocian caso por caso sin política formal; falta de registro contable de los descuentos; aprobaciones verbales de descuentos; el área comercial otorga descuentos sin consultar a finanzas; inconsistencia en descuentos entre clientes similares.
**Early_Warning_Signals:** Descuentos no registrados en factura; diferencias entre valor facturado y cobrado; el área financiera descubre descuentos después del cobro; falta de política de descuentos por pronto pago; clientes que negocian descuentos adicionales.
**Typical_Causes:** Falta de proceso formal de descuentos; cultura de "arreglar" con cada cliente; necesidad urgente de efectivo que lleva a decisiones improvisadas; área comercial con autonomía sin control; sistemas contables que no registran descuentos por separado.
**Business_Impact:** Erosión de margen no controlada; distorsión de rentabilidad real por cliente; imposibilidad de evaluar efectividad de la política; clientes que esperan descuentos; riesgo de fraude o favoritismo.
**Metrics_To_Check:** Descuentos No Documentados / Ventas; Diferencia entre Precio Facturado y Cobrado; % de Operaciones con Descuento No Documentado; Costo Anual Estimado de Descuentos Informales; Variabilidad de Descuentos entre Clientes Similares.
**Diagnostic_Questions:** ¿Hay una política formal de descuentos documentada? ¿Qué porcentaje de descuentos se otorga sin documentación? ¿Quién autoriza los descuentos? ¿Se registran todos los descuentos contablemente? ¿Se evalúa el costo-beneficio de los descuentos antes de otorgarlos?
**Recommended_Actions:** Implementar política formal de descuentos por pronto pago; registrar todos los descuentos contablemente por separado; centralizar autorización de descuentos en Finanzas; evaluar financieramente cada esquema de descuento; auditar periódicamente descuentos otorgados.
**Severity_Level:** Medium
**Related_Patterns:** CFL-008, CFL-033, CFL-038, CFL-040

### CFL-044
**Pattern_Name:** Factoraje como Única Alternativa de Cobro
**Category:** Cobranzas
**Description:** La empresa utiliza el factoraje (venta de facturas) como la única forma de cobrar a sus clientes, indicando que sus políticas de crédito y cobranza convencionales no funcionan.
**Observable_Symptoms:** La mayoría de las ventas a crédito se venden a una factora; el costo del factoraje se traslada al cliente o se absorbe en el margen; la empresa no tiene proceso de cobranza directa; los clientes saben que sus facturas se venden; dependencia total del factoraje para liquidez.
**Early_Warning_Signals:** Factoraje > 50% de las ventas a crédito; Costo de Factoraje / Ventas en aumento; la empresa no puede cobrar directamente a los clientes; clientes que se quejan de ser contactados por la factora; factoraje cubre déficit operativo, no solo estacional.
**Typical_Causes:** Política de crédito muy laxa que genera cartera de baja calidad; falta de capacidad interna de cobranza; necesidad urgente de efectivo que justifica el costo; clientes con bajo rating crediticio que solo compran si se financia la factura; incapacidad de acceder a otras fuentes de financiamiento.
**Business_Impact:** Alto costo financiero que erosiona márgenes; pérdida de relación directa con clientes en cobranza; dependencia de la factora; señal de debilidad financiera para el mercado; dificultad para salir del esquema.
**Metrics_To_Check:** Factoraje / Ventas a Crédito; Costo de Factoraje / Ventas; % de Clientes Factorados; Costo Efectivo del Factoraje (tasa anualizada); Dependencia de Factoraje para Liquidez.
**Diagnostic_Questions:** ¿Por qué la empresa no puede cobrar directamente? ¿Se ha evaluado el costo real del factoraje vs beneficios? ¿Hay un plan para reducir la dependencia del factoraje? ¿Los clientes tienen alternativas de pago directo? ¿Se puede mejorar la cobranza interna?
**Recommended_Actions:** Desarrollar capacidad interna de cobranza gradualmente; reducir dependencia de factoraje; evaluar costo del factoraje vs beneficio de liquidez; segmentar: usar factoraje solo para clientes de alto riesgo; mejorar políticas de crédito para reducir necesidad de factoraje; buscar fuentes de financiamiento más baratas.
**Severity_Level:** Medium
**Related_Patterns:** CFL-008, CFL-038, CFL-077, CFL-081

### CFL-045
**Pattern_Name:** Deterioro en Calidad de Cartera por Crecimiento Acelerado
**Category:** Cobranzas
**Description:** El crecimiento acelerado de ventas se ha logrado relajando las políticas de crédito, incorporando clientes de menor calidad crediticia y deteriorando la cartera de cuentas por cobrar.
**Observable_Symptoms:** Crecimiento de ventas acompañado de crecimiento desproporcionado de cuentas por cobrar; nuevos clientes tienen peor comportamiento de pago; aumento en provisiones y castigos; el equipo comercial prioriza volumen sobre calidad crediticia.
**Early_Warning_Signals:** Crecimiento de Cuentas por Cobrar > Crecimiento de Ventas; % de Cartera Vencida de Clientes Nuevos > % de Cartera Vencida de Clientes Antiguos; Días de Cobro de Clientes Nuevos > Días de Cobro de Clientes Antiguos; Provisiones / Ventas de Clientes Nuevos en aumento.
**Typical_Causes:** Presión por crecimiento que lleva a relajar políticas; incentivos comerciales basados solo en ventas; entrada a segmentos de mercado de menor calidad; falta de evaluación crediticia de nuevos clientes; competencia que ofrece crédito fácil.
**Business_Impact:** Crecimiento ilusorio que genera pérdidas futuras; deterioro de la calidad de activos; mayor necesidad de capital de trabajo; erosión de rentabilidad por castigos y provisiones; riesgo de espiral de relajación de crédito.
**Metrics_To_Check:** Crecimiento de Ventas vs Crecimiento de Cuentas por Cobrar; % de Cartera Vencida (Clientes Nuevos vs Antiguos); Días de Cobro (Clientes Nuevos vs Antiguos); Provisiones / Ventas (Clientes Nuevos); Tasa de Incobrabilidad por Cohorte de Clientes.
**Diagnostic_Questions:** ¿Se está creciendo con clientes de calidad o solo en volumen? ¿Los incentivos comerciales consideran la calidad de cobro? ¿Se evalúa crediticiamente a los nuevos clientes? ¿Cuál es la tasa de incobrabilidad de los clientes incorporados en el último año? ¿El crecimiento está siendo rentable después de ajustar por pérdidas crediticias?
**Recommended_Actions:** Mantener estándares de crédito incluso en crecimiento; ajustar incentivos comerciales para incluir calidad de cobro; segmentar nuevos clientes por riesgo y ajustar condiciones; monitorear cohortes de clientes por comportamiento de pago; revisar límites de crédito periódicamente; no crecer a costa de calidad de cartera.
**Severity_Level:** High
**Related_Patterns:** CFL-002, CFL-029, CFL-035, CFL-036, CFL-040


## Pagos

### CFL-046
**Pattern_Name:** Pagos Anticipados a Proveedores sin Contraprestación
**Category:** Pagos
**Description:** La empresa realiza pagos anticipados a proveedores sin obtener descuentos u otros beneficios que justifiquen la salida anticipada de efectivo, inmovilizando caja innecesariamente.
**Observable_Symptoms:** Pagos a proveedores antes de la fecha de vencimiento sin descuento; órdenes de compra que requieren pago anticipado; falta de política de pagos; el área de compras paga por adelantado por costumbre; descalce entre ciclo de pago y ciclo de cobro.
**Early_Warning_Signals:** Pagos Anticipados / Compras Totales en aumento; DPP efectivo menor al plazo negociado; falta de registro de descuentos por pronto pago; pagos realizados antes de la recepción de mercadería; proveedores que no exigen pago anticipado pero reciben pagos tempranos.
**Typical_Causes:** Falta de control de tesorería sobre el calendario de pagos; cultura de "pagar apenas llega la factura"; procesos de pago no programados; área de compras no coordinada con tesorería; percepción errónea de que pagar anticipado mejora la relación con proveedores.
**Business_Impact:** Mayor necesidad de capital de trabajo; efectivo inmovilizado que no genera retorno; menor capacidad de respuesta ante imprevistos; descalce financiero innecesario; pérdida de oportunidad de usar ese efectivo productivamente.
**Metrics_To_Check:** DPP Efectivo vs DPP Negociado; Pagos Anticipados / Compras Totales; Diferencia entre Fecha de Pago y Fecha de Vencimiento; Costo de Oportunidad de Pagos Anticipados; % de Pagos Realizados Antes de Vencimiento sin Descuento.
**Diagnostic_Questions:** ¿Se paga a los proveedores antes de la fecha de vencimiento sin razón? ¿Hay una política de pagos definida? ¿El área de tesorería controla el calendario de pagos? ¿Se evalúa el costo de oportunidad de pagar anticipado? ¿Hay proveedores que ofrecen descuentos por pronto pago?
**Recommended_Actions:** Establecer política de pagos: pagar siempre en fecha de vencimiento; centralizar autorización de pagos en tesorería; implementar calendario de pagos; negociar descuentos por pronto pago si se va a pagar anticipado; programar pagos automáticos en fecha de vencimiento.
**Severity_Level:** Low
**Related_Patterns:** CFL-030, CFL-050, CFL-053

### CFL-047
**Pattern_Name:** Proveedor Único que Impone Condiciones de Pago
**Category:** Pagos
**Description:** Un proveedor dominante impone condiciones de pago desfavorables (pago anticipado, plazos cortos, penalidades por retraso), limitando la capacidad de la empresa de gestionar su flujo de caja.
**Observable_Symptoms:** Plazos de pago más cortos con el proveedor principal que con otros; pagos anticipados exigidos por un proveedor clave; falta de poder de negociación para mejorar condiciones; dependencia operativa del proveedor; el proveedor conoce su poder y lo utiliza.
**Early_Warning_Signals:** Proveedor único > 30% de compras; condiciones de pago significativamente peores que el promedio del mercado; incremento unilateral de precios o reducción de plazos; quejas del área de compras sobre la relación; falta de alternativas de abastecimiento.
**Typical_Causes:** Dependencia de insumo crítico sin sustitutos; relación de largo plazo no formalizada; concentración de compras en un proveedor; proveedor con gran poder de mercado; falta de estrategia de abastecimiento.
**Business_Impact:** Menor flexibilidad en gestión de caja; presión sobre el capital de trabajo; vulnerabilidad ante cambios en condiciones del proveedor; riesgo operativo si el proveedor corta el suministro; desventaja competitiva por condiciones desfavorables.
**Metrics_To_Check:** Concentración de Compras (Top 1, 3); DPP del Proveedor Principal vs Promedio; Condiciones de Pago del Proveedor Principal vs Mercado; Dependencia Operativa del Proveedor; Costo Implícito de las Condiciones de Pago.
**Diagnostic_Questions:** ¿Hay alternativas reales al proveedor principal? ¿Se ha intentado negociar mejores condiciones? ¿Hay sustitutos para el insumo crítico? ¿Se puede integrar verticalmente esa provisión? ¿El contrato con el proveedor protege los intereses de la empresa?
**Recommended_Actions:** Desarrollar fuentes alternativas de suministro; negociar condiciones de pago basadas en volumen o lealtad; considerar integración vertical hacia atrás; consolidar compras para tener más poder de negociación; buscar sustitutos al insumo crítico; formalizar relación con contratos que protejan a ambas partes.
**Severity_Level:** High
**Related_Patterns:** CFL-030, CFL-053, CFL-083

### CFL-048
**Pattern_Name:** Pago de Sobrefacturación o Duplicidades
**Category:** Pagos
**Description:** La empresa paga facturas por montos incorrectos (sobrefacturación) o paga dos veces la misma factura (duplicidad), generando salidas de efectivo no justificadas.
**Observable_Symptoms:** Diferencias entre pedido y factura recurrentes; facturas duplicadas pagadas; ajustes contables frecuentes por pagos incorrectos; reclamaciones a proveedores por cobros indebidos; recuperaciones de efectivo por pagos erróneos.
**Early_Warning_Signals:** Número de Ajustes por Pagos Incorrectos; Pagos Duplicados / Pagos Totales; Reclamos a Proveedores / Facturas; Tiempo entre Pago y Detección del Error > 30 días; Diferencias entre PO y Factura > 2% en múltiples casos.
**Typical_Causes:** Falta de proceso de verificación de facturas contra pedidos; sistemas contables sin control de duplicados; facturas aprobadas sin revisión por personal no capacitado; volumen alto de facturas que impide revisión adecuada; procesos manuales propensos a error.
**Business_Impact:** Salidas de efectivo no justificadas; deterioro de relación con proveedores por reclamos; costos administrativos de corrección; posible pérdida de descuentos por pagos tardíos por estar en ajustes; riesgo de fraude.
**Metrics_To_Check:** % de Pagos con Error (monto); Pagos Duplicados / Pagos Totales; Tiempo de Detección de Errores; Costo Administrativo de Corrección; Recuperaciones por Pagos Indebidos.
**Diagnostic_Questions:** ¿Hay un proceso de verificación de facturas contra pedidos/contratos? ¿El sistema contable detecta facturas duplicadas automáticamente? ¿Quién aprueba las facturas antes del pago? ¿Se realizan auditorías periódicas de pagos? ¿Hay controles de segregación de funciones en pagos?
**Recommended_Actions:** Implementar proceso de verificación de facturas (3-way match: PO, recepción, factura); automatizar detección de duplicados; establecer niveles de aprobación según monto; segregar funciones (quien aprueba no paga); auditar pagos periódicamente; implementar sistema de gestión de facturas electrónicas.
**Severity_Level:** Medium
**Related_Patterns:** CFL-046, CFL-051

### CFL-049
**Pattern_Name:** Concentración de Pagos en Ventana Corta
**Category:** Pagos
**Description:** La empresa concentra la mayoría de sus pagos a proveedores en un período muy corto del mes, generando picos de tensión de caja que podrían evitarse con una programación más distribuida.
**Observable_Symptoms:** Todos los pagos se concentran en la primera semana del mes; fin de mes con caja desahogada pero principios de mes con tensión; picos en sobregiros o uso de líneas coincidiendo con fechas de pago; proveedores que preguntan por fechas de pago específicas.
**Early_Warning_Signals:** > 60% de pagos concentrados en 5 días del mes; Desviación Estándar de Pagos Diarios alta; Sobregiros recurrentes en fechas de pago; Uso de Línea de Crédito correlacionado con calendario de pagos; Saldo de Caja con patrón de fin de mes alto, principio bajo.
**Typical_Causes:** Política de pagos no programada; pago de todas las facturas al recibirlas; ciclos de facturación de proveedores concentrados; falta de coordinación entre compras y tesorería; calendario de pagos no distribuido.
**Business_Impact:** Picos de tensión de caja innecesarios; mayor uso de sobregiros o líneas de crédito; posible imagen de iliquidez si se concentran pagos; estrés en el área de tesorería; imposibilidad de negociar descuentos por pronto pago.
**Metrics_To_Check:** % de Pagos en los 5 Días Pico; Desviación Estándar de Pagos Diarios; Correlación entre Pagos y Uso de Sobregiro; Saldo de Caja Mínimo vs Máximo durante el Mes; Costo Financiero del Patrón de Pagos.
**Diagnostic_Questions:** ¿Se puede distribuir los pagos a lo largo del mes? ¿Los proveedores aceptarían fechas de pago alternativas? ¿Hay una política de pagos por semana? ¿El área de compras puede negociar fechas de facturación distribuidas? ¿Se ha evaluado el costo financiero de la concentración actual?
**Recommended_Actions:** Establecer calendario de pagos semanal (no mensual); negociar con proveedores fechas de facturación distribuidas; programar pagos automáticos distribuidos; mantener colchón de caja para cubrir picos de pagos; consolidar pagos para mejorar eficiencia sin concentrar en pocos días.
**Severity_Level:** Low
**Related_Patterns:** CFL-046, CFL-062, CFL-064

### CFL-050
**Pattern_Name:** Uso Excesivo de Cheques Diferidos
**Category:** Pagos
**Description:** La empresa utiliza cheques diferidos (post-datados) como forma habitual de pago, generando costos administrativos y riesgos operativos, además de indicar posibles problemas de liquidez.
**Observable_Symptoms:** Alta proporción de pagos con cheques diferidos; proveedores que se quejan de recibir cheques; costos de emisión y administración de cheques; cheques que se entregan sin fondos suficientes en la fecha; seguimiento manual de fechas de vencimiento de cheques.
**Early_Warning_Signals:** Cheques Diferidos / Pagos Totales > 30%; Cheques Devueltos / Cheques Emitidos en aumento; Costos Administrativos de Cheques / Pagos Totales; proveedores que rechazan cheques y piden transferencia; fechas de cheques que no coinciden con disponibilidad de caja.
**Typical_Causes:** Falta de acceso a medios de pago electrónicos; cultura de pago tradicional no actualizada; necesidad de diferir pagos sin costo explícito; falta de integración bancaria; control manual de tesorería.
**Business_Impact:** Costos administrativos elevados; riesgo de cheques sin fondos (imagen, penalidades); ineficiencia operativa; imposibilidad de centralizar y automatizar pagos; exposición a fraudes o extravíos.
**Metrics_To_Check:** Cheques Diferidos / Pagos Totales; Costo Administrativo por Cheque; Tasa de Cheques Devueltos; Tiempo de Procesamiento de Cheques vs Transferencias; % de Proveedores que Prefieren Transferencia.
**Diagnostic_Questions:** ¿Hay medios de pago electrónicos disponibles? ¿Los proveedores prefieren transferencia? ¿Cuál es el costo administrativo de emitir y administrar cheques? ¿Se han evaluado alternativas como transferencias electrónicas? ¿Hay un plan de migración a pagos electrónicos?
**Recommended_Actions:** Migrar a pagos electrónicos (transferencias, débito directo); implementar plataforma de pagos automatizada; negociar con proveedores cambio a transferencia; eliminar gradualmente el uso de cheques; establecer política de pagos solo electrónicos para nuevas operaciones.
**Severity_Level:** Low
**Related_Patterns:** CFL-046, CFL-049, CFL-053, CFL-067

### CFL-051
**Pattern_Name:** Pagos Recurrentes por Servicios No Utilizados
**Category:** Pagos
**Description:** La empresa mantiene pagos recurrentes por suscripciones, licencias, seguros o servicios que ya no utiliza o no necesita, generando salidas de efectivo innecesarias.
**Observable_Symptoms:** Suscripciones de software no utilizadas; licencias de sobra; seguros duplicados; membresías activas no utilizadas; servicios contratados que nadie usa; facturas recurrentes que no se revisan.
**Early_Warning_Signals:** Número de Suscripciones Activas vs Usuarios Reales; Pagos Recurrentes / Gastos Administrativos en aumento; Falta de revisión periódica de servicios contratados; Servicios sin uso en los últimos 3 meses; Facturas recurrentes sin orden de compra asociada.
**Typical_Causes:** Falta de revisión periódica de gastos recurrentes; suscripciones contratadas por empleados que ya no están; servicios acumulados sin consolidar; falta de proceso de aprobación de renovaciones; desconocimiento de lo que realmente se paga.
**Business_Impact:** Egresos innecesarios que erosionan el CFLO; efecto acumulativo significativo en el tiempo; recursos que podrían destinarse a inversiones productivas; falta de control sobre gastos recurrentes; posible duplicidad de servicios.
**Metrics_To_Check:** Gastos en Servicios No Utilizados / Gastos Totales; Número de Servicios Activos sin Uso; Costo Anual de Suscripciones No Utilizadas; % de Renovaciones Automáticas Revisadas; Relación Servicios Contratados vs Utilizados.
**Diagnostic_Questions:** ¿Se revisan periódicamente los servicios contratados? ¿Hay un inventario de todas las suscripciones y servicios recurrentes? ¿Hay algún proceso de aprobación para renovaciones? ¿Cada servicio tiene un responsable que confirme su necesidad? ¿Se pueden consolidar servicios similares?
**Recommended_Actions:** Realizar auditoría de todos los pagos recurrentes; cancelar servicios no utilizados; consolidar servicios similares para obtener mejores precios; establecer proceso de revisión trimestral de gastos recurrentes; asignar responsable por cada servicio contratado; implementar política de aprobación anual de renovaciones.
**Severity_Level:** Low
**Related_Patterns:** CFL-048, CFL-064

### CFL-052
**Pattern_Name:** Proveedores Cortados por Falta de Pago
**Category:** Pagos
**Description:** La empresa ha sido suspendida por uno o más proveedores críticos debido a impagos recurrentes, afectando la operación y obligando a buscar alternativas más caras o de menor calidad.
**Observable_Symptoms:** Suspensión de suministro por parte de proveedores; necesidad de comprar a proveedores alternativos más caros; condiciones de pago cada vez más estrictas (pago anticipado, contado); lista de proveedores que ya no venden a crédito; llamadas de cobranza de proveedores.
**Early_Warning_Signals:** Proveedores que exigen pago anticipado; proveedores que reducen límites de crédito; quejas de proveedores por atrasos; proveedores que dejan de cotizar; aumento en pagos al contado.
**Typical_Causes:** CFLO insuficiente para cubrir obligaciones con proveedores; mala gestión de liquidez; extensión excesiva de plazos de pago; disputas no resueltas con proveedores; priorización de otros pagos sobre proveedores.
**Business_Impact:** Interrupción de suministro que afecta producción/ventas; mayores costos de compra por alternativas más caras; pérdida de descuentos y crédito comercial; deterioro de relaciones comerciales; imagen negativa en el mercado.
**Metrics_To_Check:** Días de Pago Reales vs Acordados; Proveedores con Crédito Suspendido / Proveedores Totales; % de Compras al Contado vs Crédito; Diferencia de Precio entre Proveedor Habitual y Alternativo; Tiempo de Suspensión de Proveedores.
**Diagnostic_Questions:** ¿Cuántos proveedores han suspendido el crédito? ¿La falta de pago es por falta de efectivo o por disputas? ¿Hay proveedores alternativos disponibles? ¿Cuál es el sobrecosto de comprar a proveedores alternativos? ¿Hay un plan para regularizar la situación con proveedores?
**Recommended_Actions:** Priorizar pago a proveedores críticos; negociar planes de regularización de deuda; buscar proveedores alternativos mientras se regulariza; mejorar gestión de liquidez para evitar impagos; establecer comunicación proactiva con proveedores sobre fechas de pago; considerar factoring de cuentas por cobrar para liberar efectivo.
**Severity_Level:** Critical
**Related_Patterns:** CFL-001, CFL-053, CFL-062, CFL-067, CFL-085

### CFL-053
**Pattern_Name:** Aplazamiento de Pagos como Fuente de Liquidez
**Category:** Pagos
**Description:** La empresa utiliza el retraso sistemático en el pago a proveedores como fuente de financiamiento, extendiendo los plazos más allá de lo acordado y dañando relaciones comerciales.
**Observable_Symptoms:** Pagos a proveedores consistentemente después de la fecha acordada; proveedores que reclaman por atrasos; extensión de plazos sin autorización formal; uso de proveedores como "banco"; aumento en cuentas por pagar vencidas.
**Early_Warning_Signals:** DPP Real > DPP Acordado por 15+ días; % de Cuentas por Pagar Vencidas en aumento; Quejas de Proveedores por atrasos; Proveedores que exigen cambio a contado; Proveedores que dejan de vender.
**Typical_Causes:** CFLO insuficiente para cubrir pagos a tiempo; falta de liquidez estructural; estrés de caja permanente; cultura de pagar tarde como "normal"; falta de consecuencias por pagos tardíos.
**Business_Impact:** Deterioro de relaciones con proveedores; pérdida de crédito comercial; eventual corte de suministro; sobrecostos por compras de emergencia o penalidades; imagen negativa en el mercado; imposibilidad de negociar mejores condiciones futuras.
**Metrics_To_Check:** DPP Real vs DPP Acordado; % de Cuentas por Pagar Vencidas; Quejas de Proveedores / Proveedores Totales; Proveedores Perdidos por Impago / Año; Costo Implícito del Financiamiento con Proveedores (penalidades, sobreprecios).
**Diagnostic_Questions:** ¿Cuántos días, en promedio, se paga después del vencimiento? ¿Hay proveedores que ya no venden por esta práctica? ¿Cuál es el costo implícito (mayores precios, penalidades) de pagar tarde? ¿Hay un plan para normalizar los plazos de pago? ¿Se ha comunicado la situación a los proveedores?
**Recommended_Actions:** Regularizar pagos con proveedores; renegociar plazos formalmente si se necesitan más días; buscar fuentes alternativas de liquidez (no proveedores); priorizar pago a proveedores críticos; establecer política de pago en fecha; comunicar proactivamente a proveedores si habrá retrasos.
**Severity_Level:** Medium
**Related_Patterns:** CFL-030, CFL-047, CFL-052, CFL-062, CFL-085


## Necesidad de Capital de Trabajo

### CFL-054
**Pattern_Name:** NWC en Crecimiento Desproporcionado
**Category:** Necesidad de Capital de Trabajo
**Description:** El Capital de Trabajo Neto (NWC) crece a un ritmo significativamente mayor que las ventas, absorbiendo cada vez más efectivo para mantener el mismo nivel de operación.
**Observable_Symptoms:** Incremento en NWC > Crecimiento de Ventas; la empresa necesita cada vez más capital de trabajo para operar; presión sobre líneas de crédito; el CFLO se destina principalmente a financiar NWC; rentabilidad no se traduce en efectivo.
**Early_Warning_Signals:** NWC / Ventas en aumento; Incremento NWC / Incremento Ventas > 0.5 (según sector); Días de Cobro + Días de Inventario aumentando; Rotación de Capital de Trabajo en descenso; CFLO / NWC en caída.
**Typical_Causes:** Política de crédito laxa; acumulación de inventario; clientes que pagan cada vez más tarde; crecimiento desordenado sin control de capital de trabajo; mezcla de ventas hacia productos con mayor requerimiento de NWC.
**Business_Impact:** Creciente necesidad de financiamiento; rentabilidad diluida por costo de financiar NWC; menor CFLO disponible para otros fines; límite al crecimiento por restricción de capital de trabajo; riesgo de iliquidez.
**Metrics_To_Check:** NWC / Ventas; Incremento NWC / Incremento Ventas; Rotación de Capital de Trabajo (Ventas / NWC); CFLO / NWC; Diferencia entre Crecimiento de Ventas y Crecimiento de NWC.
**Diagnostic_Questions:** ¿Qué componentes del NWC están creciendo desproporcionadamente? ¿El incremento de NWC está generando mayor rentabilidad? ¿Hay segmentos de negocio con mayor requerimiento de NWC? ¿Se puede reducir el NWC sin afectar ventas? ¿Hay políticas que incentiven la eficiencia del NWC?
**Recommended_Actions:** Establecer metas de eficiencia de NWC por segmento; implementar políticas de cobro e inventario más estrictas; revisar condiciones de pago con proveedores; monitorear NWC mensualmente con desglose; vincular compensación a objetivos de NWC.
**Severity_Level:** High
**Related_Patterns:** CFL-002, CFL-006, CFL-026, CFL-055, CFL-060

### CFL-055
**Pattern_Name:** NWC Financiado con Deuda de Corto Plazo
**Category:** Necesidad de Capital de Trabajo
**Description:** La empresa financia la totalidad o la mayor parte de su NWC con deuda de corto plazo, exponiéndose a riesgos de tasas de interés y disponibilidad de crédito.
**Observable_Symptoms:** Líneas de crédito CP siempre utilizadas; deuda CP correlacionada con NWC; el NWC no se financia con proveedores (pasivos CP) sino con bancos; alto costo financiero como % de ventas; refinanciación constante de CP.
**Early_Warning_Signals:** Deuda CP / NWC > 0.7; Intereses de Deuda CP / Ventas en aumento; Deuda CP / Deuda Total > 0.5; NWC sin financiamiento de proveedores (cuentas por pagar bajas); DPP muy bajo vs CPP.
**Typical_Causes:** Bajo financiamiento de proveedores (plazos cortos); crecimiento de NWC que excede autofinanciamiento; falta de acceso a deuda de LP; márgenes insuficientes para generar CFLO; política de crédito laxa.
**Business_Impact:** Alto costo financiero; exposición a restricción de crédito; riesgo de refinanciación constante; estrés de caja; menor rentabilidad neta por intereses elevados.
**Metrics_To_Check:** Deuda CP / NWC; Deuda CP / Deuda Total; Costo de Deuda CP; Intereses / Ventas; DPP vs CPP; NWC Financiado con Proveedores vs Bancos.
**Diagnostic_Questions:** ¿Qué porcentaje del NWC está financiado con deuda CP? ¿Cuál es el costo anual de esa deuda? ¿Qué pasa si la línea de crédito se reduce? ¿Se puede aumentar el financiamiento de proveedores? ¿Hay alternativas de financiamiento de LP?
**Recommended_Actions:** Reducir NWC para disminuir necesidad de financiamiento; aumentar plazos de pago a proveedores; buscar deuda de LP para financiar NWC estructural; diversificar fuentes de financiamiento; mejorar CFLO para autofinanciar NWC.
**Severity_Level:** High
**Related_Patterns:** CFL-022, CFL-032, CFL-054, CFL-081, CFL-086

### CFL-056
**Pattern_Name:** Capex Financiado con Capital de Trabajo
**Category:** Necesidad de Capital de Trabajo
**Description:** La empresa utiliza recursos del capital de trabajo para financiar inversiones en activos fijos (Capex), desviando fondos necesarios para la operación y generando estrés de caja.
**Observable_Symptoms:** El NWC se reduce temporalmente cuando hay Capex; pagos a proveedores se retrasan durante períodos de inversión; el CFLO operativo no alcanza para Capex; cuentas por pagar se acumulan durante proyectos de inversión; la empresa "aprieta" el capital de trabajo para hacer espacio para inversiones.
**Early_Warning_Signals:** Correlación entre Capex y Reducción de NWC; Cuentas por Pagar aumentan durante períodos de Capex; CPP se alarga durante proyectos de inversión; DPP se acorta después de inversiones (para recuperar liquidez); CFLO Libre después de Capex negativo.
**Typical_Causes:** CFLO insuficiente para financiar Capex; falta de financiamiento específico para inversiones; planificación financiera deficiente; urgencia de inversión que lleva a decisiones improvisadas; falta de disciplina en separar financiamiento operativo y de inversión.
**Business_Impact:** Deterioro de la operación por falta de capital de trabajo; tensión de caja con proveedores; mayor costo de financiamiento; riesgo de interrupción operativa; menor rentabilidad de la inversión por el costo adicional.
**Metrics_To_Check:** Capex vs CFLO; Variación de NWC vs Capex; DPP antes, durante y después de inversiones; CFLO Libre; Relación (NWC + Capex) / CFLO.
**Diagnostic_Questions:** ¿El Capex se financia con CFLO o con deuda? ¿La empresa mantiene su capital de trabajo durante períodos de inversión? ¿Hay un presupuesto separado para Capex? ¿Se han evaluado otras fuentes de financiamiento para inversiones? ¿El costo del desvío de NWC se considera en la decisión de inversión?
**Recommended_Actions:** Financiar Capex con fuentes específicas (deuda LP, leasing, aportes de capital); no desviar recursos de capital de trabajo para inversiones; planificar inversiones con anticipación; mantener NWC objetivo incluso durante inversiones; considerar arrendamiento operativo como alternativa.
**Severity_Level:** High
**Related_Patterns:** CFL-011, CFL-012, CFL-015, CFL-054, CFL-085

### CFL-057
**Pattern_Name:** Descalce entre Ciclo Operativo y Financiero
**Category:** Necesidad de Capital de Trabajo
**Description:** Existe un descalce estructural entre el ciclo operativo (comprar-producir-vender-cobrar) y el ciclo financiero (disponibilidad de fondos para pagar), generando tensiones crónicas de caja.
**Observable_Symptoms:** La empresa necesita efectivo para pagar antes de cobrar; descalce permanente entre ingresos y egresos; tensiones de caja recurrentes a pesar de rentabilidad; el negocio requiere financiamiento continuo para cubrir el gap; el ciclo operativo es más largo que el financiero.
**Early_Warning_Signals:** Ciclo Operativo (Días de Inventario + Días de Cobro) > Ciclo Financiero (Días de Pago + Días de Financiamiento); DPP < DPI + CPP; Necesidad de financiamiento estructural; CCC positivo y creciente; la empresa siempre necesita capital de trabajo externo.
**Typical_Causes:** Plazos de pago a proveedores más cortos que ciclo de cobro; inventario con rotación lenta; clientes que pagan a largo plazo; falta de financiamiento de proveedores; modelo de negocio con descalce estructural (manufactura, construcción).
**Business_Impact:** Necesidad permanente de capital de trabajo; tensión crónica de caja; dependencia de financiamiento externo; menor rentabilidad por costos financieros; limitación al crecimiento.
**Metrics_To_Check:** Ciclo Operativo vs Ciclo Financiero; Diferencia en Días; NWC / Ventas; CCC; Necesidad de Financiamiento Estructural; Rotación de Capital de Trabajo.
**Diagnostic_Questions:** ¿Cuál es la brecha en días entre el ciclo operativo y el financiero? ¿Se puede acortar el ciclo operativo? ¿Se puede alargar el ciclo financiero? ¿Hay financiamiento específico para cubrir este descalce? ¿Otras empresas del sector tienen el mismo descalce?
**Recommended_Actions:** Acortar ciclo operativo (mejorar cobranzas, reducir inventario); alargar ciclo financiero (negociar plazos con proveedores); implementar financiamiento que cubra el descalce (factoraje, confirming); evaluar si el modelo de negocio debe ajustarse; establecer línea de crédito permanente para cubrir el gap estructural.
**Severity_Level:** High
**Related_Patterns:** CFL-026, CFL-030, CFL-054, CFL-060, CFL-085

### CFL-058
**Pattern_Name:** NWC Negativo (Overtrading)
**Category:** Necesidad de Capital de Trabajo
**Description:** La empresa opera con NWC negativo (pasivo corriente > activo corriente), indicando que financia sus activos de corto plazo con pasivos de corto plazo de manera agresiva, lo que puede ser sostenible solo si el ciclo de efectivo es muy rápido.
**Observable_Symptoms:** Pasivo corriente consistentemente mayor que activo corriente; ratio de liquidez < 1.0; la empresa opera con "caja negativa" (descubierto); crecimiento requiere más financiamiento; proveedores financian la operación; alta rotación de efectivo.
**Early_Warning_Signals:** NWC < 0; Liquidez Corriente < 1.0; Prueba Ácida < 0.5; DPP > CPP + DPI; Crecimiento requiere más deuda de CP; dependencia de líneas de crédito.
**Typical_Causes:** Modelo de negocio con alta rotación (supermercados, retail de rápido movimiento); crecimiento acelerado que consume caja; márgenes muy bajos que requieren alto volumen; financiamiento agresivo con proveedores; mala gestión de capital de trabajo.
**Business_Impact:** Alta vulnerabilidad a shocks de liquidez; riesgo de insolvencia técnica; dependencia crítica de proveedores y bancos; imposibilidad de crecer sin más financiamiento; estrés permanente de caja.
**Metrics_To_Check:** NWC (valor negativo); Liquidez Corriente; Prueba Ácida; CCC; DPP vs CPP + DPI; Dependencia de Financiamiento CP.
**Diagnostic_Questions:** ¿El NWC negativo es estructural (modelo de negocio) o es señal de estrés? ¿La empresa puede mantener el NWC negativo sin incumplir obligaciones? ¿Hay suficiente margen de seguridad? ¿Qué pasa si un proveedor exige pago anticipado? ¿Los accionistas están preparados para un eventual aporte de capital?
**Recommended_Actions:** Si es estructural (supermercados, etc.): mantener gestión eficiente de pagos y cobros. Si es por estrés: buscar capitalización; renegociar deuda; mejorar márgenes; vender activos no estratégicos; reducir crecimiento.
**Severity_Level:** High
**Related_Patterns:** CFL-031, CFL-054, CFL-057, CFL-085, CFL-086

### CFL-059
**Pattern_Name:** Rotación de Inventario Lenta que Inmoviliza Caja
**Category:** Necesidad de Capital de Trabajo
**Description:** La rotación de inventario es lenta, inmovilizando una parte significativa del capital de trabajo en stock que no se convierte en efectivo rápidamente.
**Observable_Symptoms:** Niveles de inventario altos en relación a ventas; productos que pasan mucho tiempo en almacén; costos de almacenamiento crecientes; rotación de inventario baja respecto al sector; faltantes y excedentes coexistiendo.
**Early_Warning_Signals:** Días de Inventario (DPI) > 60 días (dependiendo del sector); Rotación de Inventario en descenso; Inventario / Activo Corriente > 50%; Inventario / Ventas en aumento; productos obsoletos o con baja rotación.
**Typical_Causes:** Mala planificación de demanda; compras excesivas por descuento por volumen; falta de coordinación compras-ventas; producción no alineada con demanda; sistema de gestión de inventario inadecuado; sobrestock de seguridad por temor a desabastecimiento.
**Business_Impact:** Efectivo inmovilizado que no genera retorno; costos de almacenamiento, seguros, obsoletos; menor rentabilidad sobre activos; menor capacidad de respuesta a cambios; riesgo de pérdida por deterioro.
**Metrics_To_Check:** Días de Inventario (DPI); Rotación de Inventario; Inventario / Ventas; % de Inventario Obsoleto o de Baja Rotación; Costo de Mantener Inventario / Ventas; Cobertura de Inventario (días de venta cubiertos).
**Diagnostic_Questions:** ¿Cuántos días de venta tiene la empresa en inventario? ¿Qué productos tienen la rotación más lenta? ¿Hay inventario obsoleto que deba castigarse? ¿El sistema de planificación de demanda es confiable? ¿Se evalúa el costo financiero de mantener inventario?
**Recommended_Actions:** Implementar gestión de inventario justo a tiempo; eliminar o reducir productos de baja rotación; mejorar planificación de demanda con datos históricos y estacionalidad; establecer niveles máximos de inventario; negociar con proveedores entregas más frecuentes y en menores cantidades; considerar dropshipping.
**Severity_Level:** Medium
**Related_Patterns:** CFL-028, CFL-054, CFL-057, CFL-060

### CFL-060
**Pattern_Name:** Crecimiento de Ventas sin Financiamiento de NWC
**Category:** Necesidad de Capital de Trabajo
**Description:** La empresa crece en ventas sin haber asegurado el financiamiento necesario para el capital de trabajo adicional que ese crecimiento requiere, generando estrés de caja.
**Observable_Symptoms:** Crecimiento de ventas acompañado de estrés de caja; la empresa vende más pero tiene menos efectivo; necesidad urgente de financiamiento para cubrir operaciones; atrasos en pagos a proveedores cuando crecen las ventas; paradoja de "crecer hasta quebrar".
**Early_Warning_Signals:** Crecimiento de Ventas > 20% sin incremento proporcional en línea de crédito; Incremento NWC / Incremento Ventas no presupuestado; la empresa no proyectó el NWC del crecimiento; solicitudes de crédito de último momento para cubrir operaciones; proveedores comienzan a quejarse.
**Typical_Causes:** Planificación financiera deficiente; enfoque solo en crecimiento de ingresos sin considerar impacto en caja; desconocimiento de la relación entre crecimiento y NWC; falta de integración entre plan comercial y financiero; optimismo excesivo sobre la capacidad de autofinanciamiento.
**Business_Impact:** Crecimiento insostenible; crisis de liquidez; posibilidad de incumplimiento con proveedores; necesidad de financiamiento de emergencia más caro; eventual freno forzado al crecimiento.
**Metrics_To_Check:** Incremento NWC Proyectado vs Real; Crecimiento de Ventas vs Crecimiento de Línea de Crédito; NWC / Ventas (real vs presupuestado); CFLO vs Crecimiento de NWC; Días de Cobro, Inventario y Pago vs Presupuesto.
**Diagnostic_Questions:** ¿Se proyectó el NWC necesario para el crecimiento? ¿Hay una línea de crédito comprometida para financiar el crecimiento? ¿Se puede ajustar la velocidad de crecimiento a la disponibilidad de financiamiento? ¿Hay segmentos de crecimiento con menor requerimiento de NWC? ¿Se ha considerado el factoraje para financiar el crecimiento?
**Recommended_Actions:** Proyectar NWC para el crecimiento esperado; asegurar línea de crédito antes de crecer; priorizar crecimiento en segmentos con menor requerimiento de NWC; ajustar velocidad de crecimiento a disponibilidad de financiamiento; implementar factoraje o confirming para financiar el crecimiento.
**Severity_Level:** High
**Related_Patterns:** CFL-002, CFL-006, CFL-054, CFL-057, CFL-085

### CFL-061
**Pattern_Name:** Estacionalidad que Exige Picos de NWC
**Category:** Necesidad de Capital de Trabajo
**Description:** La estacionalidad del negocio genera picos predecibles de necesidad de capital de trabajo que la empresa no planifica, causando tensiones de caja recurrentes en las mismas épocas del año.
**Observable_Symptoms:** Tensión de caja en las mismas épocas cada año; picos de uso de líneas de crédito en períodos predecibles; acumulación de inventario antes de temporada alta seguida de estrés de caja; pagos atrasados en ciertos meses del año; necesidad estacional de financiamiento.
**Early_Warning_Signals:** Patrón estacional en NWC; Uso de Línea de Crédito con picos estacionales; DPP se acorta en temporada baja; Sobregiros recurrentes en mismos meses; Dificultad para pagar a proveedores en post-temporada.
**Typical_Causes:** Falta de planificación financiera estacional; acumulación de inventario antes de temporada sin financiamiento asegurado; concentración de ventas en pocos meses; compras estacionales no coordinadas con tesorería; falta de líneas de crédito estacionales.
**Business_Impact:** Estrés de caja recurrente; mayor costo financiero por financiamiento estacional de emergencia; imposibilidad de aprovechar descuentos por volumen en compras estacionales; relaciones tensas con proveedores en temporada baja.
**Metrics_To_Check:** NWC por Mes / Trimestre; Patrón de Uso de Línea de Crédito; Variación Estacional de DPP y CPP; Pico de NWC vs NWC Promedio; Costo Financiero de la Estacionalidad.
**Diagnostic_Questions:** ¿Se proyecta el NWC estacional con anticipación? ¿Hay una línea de crédito específica para estacionalidad? ¿Se puede nivelar la producción/compras para reducir picos? ¿Los proveedores ofrecen financiamiento estacional? ¿Se han evaluado alternativas como factoring estacional?
**Recommended_Actions:** Elaborar proyección de NWC mensual con 12 meses de anticipación; contratar línea de crédito estacional comprometida; negociar con proveedores plazos extendidos en temporada alta; considerar factoring de cuentas por cobrar post-temporada; nivelar producción/compras para reducir picos.
**Severity_Level:** Medium
**Related_Patterns:** CFL-054, CFL-057, CFL-060, CFL-069, CFL-072, CFL-075


## Tensiones de Caja

### CFL-062
**Pattern_Name:** Sobregiro Bancario Recurrente
**Category:** Tensiones de Caja
**Description:** La empresa incurre en sobregiros bancarios (descubiertos en cuenta corriente) de manera recurrente, indicando que la caja no alcanza para cubrir las obligaciones a su vencimiento.
**Observable_Symptoms:** Cuenta corriente frecuentemente en números rojos; comisiones por sobregiro recurrentes en el estado de cuenta; llamadas del banco por sobregiros; uso del sobregiro como fuente habitual de financiamiento; necesidad de cubrir el descubierto con el primer ingreso del día siguiente.
**Early_Warning_Signals:** Sobregiros en más de 3 días al mes; Comisiones por Sobregiro / Gastos Bancarios > 20%; el sobregiro se usa como "línea de crédito"; la empresa no puede mantener saldo positivo; incremento en frecuencia de sobregiros.
**Typical_Causes:** CFLO insuficiente para cubrir egresos; descalce entre ingresos y egresos; mala planificación de tesorería; capital de trabajo insuficiente; falta de colchón de caja.
**Business_Impact:** Altos costos financieros (comisiones, intereses punitorios); deterioro de la relación bancaria; imagen de mala gestión financiera; riesgo de que el banco cancele la facilidad; estrés permanente.
**Metrics_To_Check:** Días con Sobregiro / Mes; Monto Promedio de Sobregiro; Comisiones por Sobregiro / Mes; Costo Anual del Sobregiro; Frecuencia de Sobregiros (tendencia).
**Diagnostic_Questions:** ¿Con qué frecuencia ocurren los sobregiros? ¿Son por descalce temporal o por déficit estructural? ¿Se ha solicitado una línea de crédito formal en lugar de usar sobregiro? ¿Hay un presupuesto de caja semanal? ¿Se puede reducir la frecuencia mejorando la planificación?
**Recommended_Actions:** Solicitar línea de crédito formal en lugar de sobregiro; mejorar proceso de presupuesto de caja semanal; mantener colchón de caja mínimo; reprogramar pagos para alinearlos con ingresos; establecer alertas de saldo mínimo; reducir la dependencia del sobregiro gradualmente.
**Severity_Level:** Medium
**Related_Patterns:** CFL-064, CFL-066, CFL-067, CFL-068, CFL-085

### CFL-063
**Pattern_Name:** Caja Cero al Cierre de Mes
**Category:** Tensiones de Caja
**Description:** La empresa llega sistemáticamente a saldo de caja cero o casi cero al cierre de cada mes, sin colchón para imprevistos ni capacidad de ahorro.
**Observable_Symptoms:** Los primeros días del mes son críticos para conseguir efectivo; cualquier gasto imprevisto genera sobregiro; imposibilidad de aprovechar oportunidades que requieren efectivo; el ciclo mensual de caja termina siempre en cero; la empresa vive "al día".
**Early_Warning_Signals:** Saldo de Caja al Cierre de Mes < 1 día de ventas; Patrón consistente de caja cero a fin de mes; Caja Mínima Mensual consistentemente cercana a cero; Dependencia de ingreso del primer día del mes para cubrir pagos; Ausencia de colchón de efectivo.
**Typical_Causes:** CFLO apenas cubre gastos; capital de trabajo insuficiente; falta de disciplina de ahorro; crecimiento que consume todo el efectivo disponible; gastos fijos muy altos en relación a ingresos.
**Business_Impact:** Alta vulnerabilidad a cualquier imprevisto; imposibilidad de aprovechar oportunidades; estrés constante para la gestión; deterioro de relaciones con proveedores si algún pago se retrasa; riesgo de iliquidez.
**Metrics_To_Check:** Saldo de Caja Mínimo del Mes; Saldo de Caja al Cierre; Días de Caja (saldo / gasto diario promedio); Frecuencia de Saldo Cero; Capacidad de Absorción de Imprevistos (días de caja).
**Diagnostic_Questions:** ¿Cuántos días de gasto cubre el saldo de caja mínimo del mes? ¿Hay algún mes en que el saldo sea positivo? ¿Se puede reducir la velocidad de salida de efectivo en los últimos días del mes? ¿Hay algún margen para diferir gastos no esenciales? ¿Se ha considerado abrir una cuenta de reserva?
**Recommended_Actions:** Establecer meta de saldo de caja mínimo (ej. 5 días de gastos); reducir gastos para generar excedente de caja; diferir gastos no esenciales a principios del mes siguiente; separar una cuenta para reserva de efectivo; reprogramar pagos para evitar el pico de fin de mes.
**Severity_Level:** High
**Related_Patterns:** CFL-062, CFL-064, CFL-066, CFL-085

### CFL-064
**Pattern_Name:** Descuadre entre Presupuesto de Caja y Realidad
**Category:** Tensiones de Caja
**Description:** Existe una brecha significativa y recurrente entre el presupuesto de caja proyectado y el flujo de caja real, indicando problemas en la planificación financiera o en la ejecución.
**Observable_Symptoms:** Proyecciones de caja que no se cumplen; diferencias sistemáticas entre lo presupuestado y lo real; ajustes de último minuto para cubrir déficits no previstos; falta de confianza en las proyecciones; decisiones tomadas con información desactualizada.
**Early_Warning_Signals:** Desviación Presupuesto de Caja vs Real > 20% en múltiples períodos; Proyecciones siempre optimistas (ingresos sobrestimados, egresos subestimados); revisión constante del presupuesto a la baja; falta de actualización de proyecciones; el equipo no utiliza el presupuesto para tomar decisiones.
**Typical_Causes:** Proyecciones basadas en supuestos irreales; falta de actualización de datos; ingresos volátiles e impredecibles; egresos no controlados; falta de integración entre áreas; presupuesto no revisado periódicamente.
**Business_Impact:** Decisiones basadas en información incorrecta; falta de anticipación a problemas de caja; crisis recurrentes no previstas; imposibilidad de planificar inversiones; desconfianza en la gestión financiera.
**Metrics_To_Check:** Desviación Presupuesto vs Real (ingresos, egresos, saldo); Precisión del Pronóstico de Caja (Forecast Accuracy); Error Absoluto Medio (MAE) de Proyecciones; % de Meses con Desviación > 20%; Tasa de Actualización de Proyecciones.
**Diagnostic_Questions:** ¿Los supuestos de las proyecciones son realistas? ¿Se actualizan las proyecciones con datos reales semanalmente? ¿Hay un proceso de revisión de desviaciones? ¿Las áreas comerciales y operativas participan en las proyecciones? ¿Se documentan las causas de las desviaciones?
**Recommended_Actions:** Mejorar proceso de elaboración de presupuesto de caja; actualizar proyecciones semanalmente con datos reales; involucrar a todas las áreas en las proyecciones; implementar rolling forecast (12 meses rodantes); analizar y documentar desviaciones; usar escenarios pesimista, realista y optimista.
**Severity_Level:** Medium
**Related_Patterns:** CFL-062, CFL-063, CFL-066, CFL-085

### CFL-065
**Pattern_Name:** Uso de Caja de Otras Empresas del Grupo
**Category:** Tensiones de Caja
**Description:** La empresa utiliza fondos de otras empresas del mismo grupo económico para cubrir sus déficits operativos, generando dependencia y posibles problemas legales/fiscales.
**Observable_Symptoms:** Transferencias regulares entre empresas del grupo; una empresa actúa como "banco" del grupo; préstamos entre partes relacionadas sin documentación formal; diferencias en saldos de cuentas entre compañías; falta de interés en las transacciones intragrupo.
**Early_Warning_Signals:** Saldos a Favor / en Contra de Partes Relacionadas en aumento; Transacciones Intragrupo sin contrato; Diferencias en conciliaciones entre empresas; Intereses no cobrados/pagados en préstamos intragrupo; Una empresa del grupo siempre pide fondos a otra.
**Typical_Causes:** CFLO insuficiente de una empresa que se cubre con otra del grupo; falta de acceso a financiamiento externo; estructura de grupo sin separación financiera; planificación fiscal agresiva; falta de gestión independiente de cada empresa.
**Business_Impact:** Dependencia de otras empresas del grupo; riesgos fiscales (precios de transferencia); problemas legales (préstamos entre partes no documentados); falta de transparencia financiera; arrastre de problemas de una empresa a otra.
**Metrics_To_Check:** Saldos Intragrupo / Patrimonio Neto; Préstamos Intragrupo / Deuda Total; Intereses Intragrupo No Documentados; Frecuencia de Transferencias Intragrupo; % de Déficit Financiado por Grupo.
**Diagnostic_Questions:** ¿Están documentadas las transacciones intragrupo? ¿Se cobran/pagan intereses de mercado? ¿Hay un contrato formal de préstamo? ¿La empresa podría sobrevivir sin el apoyo del grupo? ¿Hay exposición fiscal por precios de transferencia?
**Recommended_Actions:** Regularizar toda transacción intragrupo con contratos formales; establecer tasas de interés de mercado; formalizar préstamos intragrupo; buscar financiamiento externo para reducir dependencia intragrupo; evaluar si la empresa es viable sin el apoyo del grupo.
**Severity_Level:** Medium
**Related_Patterns:** CFL-021, CFL-068, CFL-085, CFL-090

### CFL-066
**Pattern_Name:** Falta de Holgura para Imprevistos
**Category:** Tensiones de Caja
**Description:** La empresa no tiene ningún colchón de efectivo para enfrentar gastos imprevistos, lo que la hace extremadamente vulnerable a cualquier evento inesperado.
**Observable_Symptoms:** Cualquier gasto no presupuestado genera sobregiro; no hay reserva de efectivo; la empresa no puede aprovechar oportunidades que requieren efectivo inmediato; cualquier imprevisto (reparación, multa, gasto legal) genera crisis; se depende de financiamiento de emergencia.
**Early_Warning_Signals:** Días de Caja (Efectivo / Gasto Diario Promedio) < 5; Saldo de Caja < 1% de Ventas Anuales; No existe cuenta separada para imprevistos; Cualquier gasto imprevisto requiere nuevo financiamiento; Historial de múltiples emergencias financieras.
**Typical_Causes:** CFLO insuficiente para acumular reservas; cultura de "gastar todo lo que se genera"; falta de prioridad a la creación de reservas; dueños que retiran todo el efectivo disponible; crecimiento que consume todo el excedente.
**Business_Impact:** Alta vulnerabilidad a shocks; imposibilidad de aprovechar oportunidades; estrés constante; riesgo de iliquidez ante el menor imprevisto; imagen de inestabilidad.
**Metrics_To_Check:** Días de Caja (Efectivo / Gasto Diario); Ratio de Reserva (Efectivo / Ventas); Tamaño de Fondo de Emergencia vs Riesgos Identificados; Frecuencia de Imprevistos que Requieren Financiamiento.
**Diagnostic_Questions:** ¿Cuántos días de gasto cubre el efectivo disponible? ¿Cuáles son los principales riesgos de imprevistos? ¿Se ha considerado crear un fondo de emergencia? ¿Hay voluntad de los dueños para acumular reservas? ¿Qué pasaría si ocurre un imprevisto de $X?
**Recommended_Actions:** Establecer política de fondo de emergencia (mínimo 3-6 meses de gastos); separar cuenta bancaria exclusiva para reservas; destinar un % fijo del CFLO a reservas antes de cualquier otro uso; reducir gastos para liberar efectivo para reservas; priorizar la creación de colchón sobre otros usos del efectivo.
**Severity_Level:** High
**Related_Patterns:** CFL-062, CFL-063, CFL-064, CFL-085

### CFL-067
**Pattern_Name:** Cheques Devueltos por Falta de Fondos
**Category:** Tensiones de Caja
**Description:** La empresa emite cheques que son devueltos por falta de fondos, indicando serios problemas de liquidez y generando costos adicionales, penalidades y daño reputacional.
**Observable_Symptoms:** Cheques devueltos con frecuencia; proveedores que ya no aceptan cheques; costos por comisiones de cheques devueltos; inclusiones en centrales de riesgo (Veraz, Equifax); llamadas de proveedores por cheques rebotados.
**Early_Warning_Signals:** Cheques Devueltos / Cheques Emitidos > 5%; Comisiones por Cheques Devueltos / Gastos Bancarios > 10%; Proveedores que rechazan cheques; Inclusión en centrales de deudores; Aumento en número de cheques devueltos mes a mes.
**Typical_Causes:** CFLO insuficiente para cubrir pagos comprometidos; mala planificación de tesorería; emisión de cheques sin verificar saldo; extensión excesiva de pagos con cheques diferidos; sobreestimación de ingresos futuros.
**Business_Impact:** Costos financieros por comisiones e intereses; daño reputacional con proveedores; inclusión en centrales de riesgo que limita acceso a crédito; posible pérdida de proveedores; implicancias legales (cheque sin fondo puede ser delito).
**Metrics_To_Check:** Tasa de Cheques Devueltos; Costo Anual de Cheques Devueltos (comisiones + intereses); Proveedores Afectados; Tiempo para Regularizar Cheques Devueltos; Frecuencia de Inclusiones en Centrales de Riesgo.
**Diagnostic_Questions:** ¿Con qué frecuencia se devuelven cheques? ¿Hay un patrón (días del mes, proveedores específicos)? ¿Se verifica el saldo antes de emitir cheques? ¿Se ha considerado eliminar el uso de cheques? ¿Hay un plan para evitar cheques sin fondos?
**Recommended_Actions:** Suspender emisión de cheques hasta regularizar liquidez; migrar a pagos electrónicos (transferencias); implementar verificación de saldo antes de emitir; establecer proceso de aprobación de cheques; negociar con proveedores medios de pago alternativos; regularizar situación en centrales de riesgo.
**Severity_Level:** Critical
**Related_Patterns:** CFL-050, CFL-052, CFL-062, CFL-085, CFL-089

### CFL-068
**Pattern_Name:** Dependencia de Adelantos de Clientes para Operar
**Category:** Tensiones de Caja
**Description:** La empresa depende de los adelantos o anticipos de clientes para cubrir sus gastos operativos, indicando que no genera suficiente efectivo por sí misma para operar.
**Observable_Symptoms:** La empresa necesita el anticipo del cliente para comprar insumos o producir; si los clientes no adelantan, la operación se detiene; los anticipos se utilizan para gastos corrientes, no para proyectos específicos; estructura de negocio basada en prepago forzoso; tensión cuando un cliente no adelanta.
**Early_Warning_Signals:** Anticipos de Clientes / CFLO > 0.5; Sin anticipos, la empresa no puede operar; anticipos creciendo más que ventas; ejecución de proyectos retrasada vs anticipos cobrados; clientes que se quejan de tener que adelantar.
**Typical_Causes:** CFLO estructuralmente insuficiente; capital de trabajo negativo; modelo de negocio con descalce severo; falta de acceso a financiamiento; mala gestión de liquidez.
**Business_Impact**: Dependencia peligrosa de la buena voluntad de clientes; imposibilidad de escalar sin más anticipos; percepción de debilidad financiera; clientes que presionan por descuentos a cambio de anticipos; riesgo de no poder ejecutar lo cobrado.
**Metrics_To_Check:** Anticipos de Clientes / CFLO; Anticipos / Ventas; Dependencia de Anticipos para Operar; Capacidad de Operar sin Anticipos; % de Clientes que Adelantan.
**Diagnostic_Questions:** ¿Qué pasa si los clientes dejan de adelantar? ¿Se puede operar sin anticipos? ¿Los anticipos se utilizan para proyectos específicos o para gastos generales? ¿Hay una política formal de anticipos? ¿Los clientes están cómodos con el esquema de adelantos?
**Recommended_Actions:** Reducir gradualmente la dependencia de anticipos; buscar financiamiento alternativo para capital de trabajo; mejorar CFLO para cubrir gastos sin anticipos; formalizar política de anticipos (descuentos, condiciones); construir colchón de caja para eliminar la dependencia.
**Severity_Level:** Critical
**Related_Patterns:** CFL-004, CFL-021, CFL-058, CFL-062, CFL-085


## Estacionalidad

### CFL-069
**Pattern_Name:** Pico de Caja Estacional no Planificado
**Category:** Estacionalidad
**Description:** La empresa experimenta picos de caja (excedentes) durante ciertas épocas del año que no planifica ni gestiona, perdiendo oportunidades de invertir el efectivo excedente.
**Observable_Symptoms:** Excedentes de caja en ciertos meses seguidos de déficits en otros; efectivo ocioso sin rendimiento en períodos de alta liquidez; falta de inversión temporal del excedente; compras impulsivas cuando hay efectivo disponible; patrón estacional no gestionado.
**Early_Warning_Signals:** Variación estacional en saldo de caja > 50%; Excedentes de caja > 3 meses de gasto en temporada alta; Sin inversión temporal del excedente; Patrón de "gastar cuando hay" en lugar de planificar; Diferencia entre caja máxima y mínima anual muy alta.
**Typical_Causes:** Falta de planificación financiera estacional; desconocimiento de opciones de inversión de corto plazo; cultura de "gastar lo que hay"; falta de previsión de los meses de déficit; dueños que retiran el excedente sin planificar.
**Business_Impact:** Oportunidad perdida de generar rendimiento sobre excedentes; derroche en períodos de abundancia; déficit severo en temporada baja; imposibilidad de nivelar el flujo de caja anual; desbalance financiero.
**Metrics_To_Check:** Variación Estacional de Caja (máx - mín); Excedente de Caja Promedio en Temporada Alta; Rendimiento de Excedentes (intereses ganados / excedente promedio); Duración del Excedente (días); Correlación entre Excedente y Gastos Discrecionales.
**Diagnostic_Questions:** ¿Se identifican los períodos de excedente de caja con anticipación? ¿Se invierte el excedente temporalmente? ¿Hay un plan para usar el excedente para cubrir déficits futuros? ¿Los dueños retiran el excedente sin considerar la temporada baja? ¿Se ha evaluado constituir un fondo de reserva?
**Recommended_Actions:** Elaborar proyección de caja anual con estacionalidad; crear fondo de reserva con excedentes de temporada alta; invertir excedentes temporales en instrumentos de corto plazo; planificar el uso del excedente para cubrir déficits futuros; evitar decisiones de gasto impulsivas en períodos de abundancia.
**Severity_Level:** Low
**Related_Patterns:** CFL-061, CFL-070, CFL-075, CFL-076

### CFL-070
**Pattern_Name:** Valle de Caja Estacional Recurrente
**Category:** Estacionalidad
**Description:** La empresa experimenta valles de caja (déficits) recurrentes en las mismas épocas del año debido a la estacionalidad del negocio, sin tener una estrategia planificada para enfrentarlos.
**Observable_Symptoms:** Tensión de caja en los mismos meses cada año; sobregiros recurrentes en temporada baja; pagos atrasados a proveedores en ciertos meses; dependencia de líneas de crédito en períodos predecibles; estrés estacional documentado pero no resuelto.
**Early_Warning_Signals:** Patrón de déficit en mismos meses año tras año; Uso de Línea de Crédito con picos en misma época; Sobregiros recurrentes en temporada baja; Caja negativa o muy baja en ciertos meses; el equipo sabe que "enero y febrero son críticos" pero no planifica.
**Typical_Causes:** Falta de planificación financiera estacional; no se constituyen reservas en temporada alta; gastos fijos constantes vs ingresos variables; falta de línea de crédito estacional; cultura reactiva en lugar de preventiva.
**Business_Impact:** Estrés de caja recurrente y predecible; mayor costo financiero por financiamiento estacional de emergencia; deterioro de relaciones con proveedores en temporada baja; imposibilidad de aprovechar oportunidades; fatiga organizacional.
**Metrics_To_Check:** Déficit de Caja en Temporada Baja (promedio); Duración del Valle de Caja (días); Costo Financiero de la Estacionalidad; Uso de Línea de Crédito en Temporada Baja; Diferencia entre Caja en Temporada Alta vs Baja.
**Diagnostic_Questions:** ¿Se proyecta el déficit estacional con anticipación? ¿Hay una línea de crédito comprometida para la temporada baja? ¿Se constituyen reservas en temporada alta? ¿Se pueden ajustar gastos en temporada baja? ¿Hay alternativas para generar ingresos en temporada baja?
**Recommended_Actions:** Constituir reserva de efectivo en temporada alta para cubrir temporada baja; contratar línea de crédito estacional comprometida; reducir gastos fijos o ajustarlos a la estacionalidad; diversificar ingresos para generar flujo en temporada baja; elaborar plan de caja anual con 12 meses rodantes.
**Severity_Level:** Medium
**Related_Patterns:** CFL-061, CFL-069, CFL-071, CFL-075, CFL-076

### CFL-071
**Pattern_Name:** Inventario Estacional Financiado con Deuda Corto Plazo
**Category:** Estacionalidad
**Description:** La empresa financia la acumulación de inventario estacional con deuda de corto plazo sin haber asegurado las condiciones, exponiéndose a riesgo de tasa y disponibilidad.
**Observable_Symptoms:** Acumulación de inventario antes de temporada alta financiada con líneas CP; pico de deuda CP correlacionado con compras estacionales; incertidumbre sobre la tasa de interés del financiamiento; solicitudes de crédito de último momento; ansiedad por si se renueva la línea.
**Early_Warning_Signals:** Deuda CP / Inventario Estacional > 0.8; Pico de Uso de Línea de Crédito coincide con compras estacionales; Costo de Financiamiento de Inventario Estacional no presupuestado; Dependencia de aprobación de crédito para compras estacionales; Compras estacionales condicionadas a disponibilidad de crédito.
**Typical_Causes:** Falta de planificación de compras estacionales; no se asegura financiamiento con anticipación; capital de trabajo insuficiente para cubrir estacionalidad; desconocimiento del costo total del financiamiento; compras estacionales no coordinadas con tesorería.
**Business_Impact:** Riesgo de no poder comprar inventario estacional si se corta la línea; mayor costo financiero por financiamiento de emergencia; estrés de caja adicional; posible pérdida de ventas por falta de stock; margen estacional erosionado por costo financiero.
**Metrics_To_Check:** Deuda CP / Inventario Estacional; Costo de Financiamiento de Inventario Estacional; Uso de Línea de Crédito en Temporada de Compras; Diferencia entre Costo Real y Presupuestado de Financiamiento; Tiempo de Aseguramiento de Financiamiento vs Compra.
**Diagnostic_Questions:** ¿Se asegura el financiamiento antes de hacer las compras estacionales? ¿El costo del financiamiento está presupuestado? ¿Hay alternativas de financiamiento si una línea se corta? ¿Se puede negociar con proveedores plazos que cubran el ciclo estacional? ¿Se evalúa el costo financiero en la decisión de compra estacional?
**Recommended_Actions:** Contratar línea de crédito estacional comprometida con anticipación; negociar con proveedores plazos extendidos para compras estacionales; presupuestar el costo financiero del inventario estacional; considerar confirming para financiar compras estacionales; diversificar fuentes de financiamiento estacional.
**Severity_Level:** Medium
**Related_Patterns:** CFL-022, CFL-061, CFL-070, CFL-072, CFL-081

### CFL-072
**Pattern_Name:** Compras Estacionales sin Línea de Crédito
**Category:** Estacionalidad
**Description:** La empresa realiza compras estacionales significativas sin tener una línea de crédito comprometida para financiarlas, arriesgándose a no poder pagar o a hacerlo en condiciones desfavorables.
**Observable_Symptoms:** Compras estacionales financiadas con sobregiros o descubiertos; solicitudes de crédito de último momento para cubrir compras; proveedores que no cobran a tiempo por falta de financiamiento; estrés de caja post-compra estacional; uso de fondos destinados a otros fines.
**Early_Warning_Signals:** Compras Estacionales > Línea de Crédito Disponible; Necesidad de Financiamiento de Emergencia para Compras; Proveedores pagan tarde por falta de fondos; Desvío de fondos de otras obligaciones; Dependencia de aprobación de crédito para liberar compras.
**Typical_Causes:** Falta de planificación financiera estacional; crecimiento de compras estacionales no anticipado; deterioro de relación bancaria que reduce líneas disponibles; dueños que no quieren endeudarse hasta que es urgente; optimismo excesivo sobre la capacidad de pago.
**Business_Impact:** Riesgo de no poder comprar inventario estacional; compras en condiciones desfavorables (precios más altos, menor volumen); tensiones con proveedores; desvío de fondos de otras obligaciones; estrés financiero.
**Metrics_To_Check:** Compras Estacionales vs Línea de Crédito Disponible; % de Compras Estacionales sin Financiamiento Asegurado; Costo de Financiamiento de Emergencia vs Planificado; Proveedores Afectados por Falta de Pago; Tiempo de Aseguramiento de Financiamiento.
**Diagnostic_Questions:** ¿Hay una línea de crédito comprometida para las compras estacionales? ¿Se gestiona el financiamiento antes de hacer las compras? ¿Hay alternativas si la línea actual no alcanza? ¿Se puede negociar con proveedores financiamiento directo? ¿El volumen de compras está alineado con la capacidad financiera?
**Recommended_Actions:** Gestionar línea de crédito estacional con 2-3 meses de anticipación; negociar con proveedores plazos extendidos para compras estacionales; ajustar volumen de compras a la capacidad financiera disponible; considerar financiamiento alternativo (factoraje, confirming, proveedores); mantener relación bancaria activa incluso cuando no se necesita crédito.
**Severity_Level:** High
**Related_Patterns:** CFL-061, CFL-070, CFL-071, CFL-081, CFL-089

### CFL-073
**Pattern_Name:** Contratación Temporal sin Presupuesto de Caja
**Category:** Estacionalidad
**Description:** La empresa contrata personal temporal para temporada alta sin haber presupuestado el impacto en el flujo de caja, generando estrés financiero cuando llegan los pagos de sueldos y cargas sociales.
**Observable_Symptoms:** Contratación temporal de última hora sin planificación; los costos de personal temporal no estaban en el presupuesto de caja; después de la temporada alta, la caja queda peor que antes; descalce entre el momento del gasto (sueldos semanales) y el ingreso (cobro diferido); incumplimiento de obligaciones laborales.
**Early_Warning_Signals:** Costo de Personal Temporal / Presupuesto de Caja > 20%; Desviación entre gasto real y presupuestado en personal temporal; Pagos de sueldos que generan sobregiros; Falta de provisión para cargas sociales y SAC; Contratación sin orden de compra ni aprobación de finanzas.
**Typical_Causes:** Falta de coordinación entre área operativa y financiera; urgencia operativa que lleva a contratar sin planificar; desconocimiento del costo total de la contratación temporal; presupuesto no actualizado con necesidades reales; cultura de "primero contratar, después vemos".
**Business_Impact:** Estrés de caja no previsto; posible incumplimiento de obligaciones laborales; relación tensa con empleados temporales; imposibilidad de repetir la contratación al año siguiente; desprestigio como empleador.
**Metrics_To_Check:** Costo Real de Personal Temporal vs Presupuestado; % de Desviación en Costos de Personal Estacional; Impacto en Caja de Personal Temporal; Cobertura de Provisiones Laborales; Frecuencia de Contratación sin Presupuesto.
**Diagnostic_Questions:** ¿Se presupuesta el costo total de la contratación temporal antes de contratar? ¿Hay una orden de compra aprobada por finanzas? ¿Se considera el momento de pago de sueldos vs momento de cobro? ¿Se provisionan las cargas sociales y SAC? ¿El área operativa coordina con finanzas antes de contratar?
**Recommended_Actions:** Incluir contratación temporal en el presupuesto de caja estacional; coordinar entre operaciones y finanzas antes de contratar; provisionar todos los costos laborales (sueldos, cargas, SAC, indemnizaciones); ajustar momento de contratación a disponibilidad de caja; considerar alternativas (tercerización, horas extra) que puedan tener mejor impacto de caja.
**Severity_Level:** Medium
**Related_Patterns:** CFL-061, CFL-064, CFL-070, CFL-075

### CFL-074
**Pattern_Name:** Campaña Comercial sin Evaluación de Impacto de Caja
**Category:** Estacionalidad
**Description:** La empresa lanza campañas comerciales (descuentos, promociones, bonificaciones) sin evaluar el impacto en el flujo de caja, priorizando el volumen sobre la liquidez.
**Observable_Symptoms:** Campañas que generan mucho volumen pero poco efectivo; promociones que ofrecen plazos de pago extendidos; descuentos agresivos que comprimen margen y CFLO; la caja no mejora a pesar del éxito comercial de la campaña; el área comercial lanza campañas sin consultar a finanzas.
**Early_Warning_Signals:** Ventas en campaña crecen pero CFLO no mejora; Plazos de cobro se alargan durante campañas; Descuentos en campaña > Margen de Contribución; Costo de la Campaña vs CFLO Generado no evaluado; Área comercial no consulta a finanzas antes de lanzar.
**Typical_Causes:** Falta de integración entre comercial y finanzas; incentivos comerciales basados solo en volumen; cultura de "vender a cualquier costo"; desconocimiento del impacto de caja de las campañas; presión de la competencia que lleva a imitar campañas sin análisis.
**Business_Impact:** Crecimiento de ventas sin mejora de caja; deterioro de márgenes; mayor necesidad de capital de trabajo; esfuerzo comercial que no genera valor; recursos desperdiciados en campañas inefectivas.
**Metrics_To_Check:** CFLO Generado por Campaña vs Costo; Incremento de Ventas vs Incremento de Cuentas por Cobrar; Margen de Contribución Neto de Campaña; Impacto en CCC de la Campaña; ROI de la Campaña en términos de Caja.
**Diagnostic_Questions:** ¿Se evalúa el impacto de caja de cada campaña antes de lanzarla? ¿Hay un proceso de aprobación de campañas que incluya a finanzas? ¿Los incentivos comerciales consideran el resultado de caja? ¿Las campañas ofrecen plazos de pago que deterioran el CCC? ¿Se hace un análisis post-campaña de impacto en caja?
**Recommended_Actions:** Establecer proceso de aprobación de campañas que incluya evaluación de impacto en caja; diseñar campañas que mejoren el flujo (pago anticipado, descuento por pronto pago); medir ROI de campañas en términos de caja (no solo ventas); alinear incentivos comerciales con objetivos de caja; revisar periodicamente efectividad de campañas.
**Severity_Level:** Medium
**Related_Patterns:** CFL-002, CFL-006, CFL-007, CFL-033, CFL-061

### CFL-075
**Pattern_Name:** Descalce Estacional entre Ingresos y Egresos
**Category:** Estacionalidad
**Description:** Existe un descalce temporal entre el momento en que la empresa recibe ingresos (estacionales) y el momento en que debe realizar sus principales egresos, generando tensiones de caja predecibles.
**Observable_Symptoms:** Los egresos importantes (impuestos, sueldos, compras) ocurren en momentos diferentes a los ingresos; picos de gasto no coinciden con picos de ingreso; necesidad de financiamiento en meses específicos; patrón de descalce que se repite cada año; planificación tributaria que no considera estacionalidad.
**Early_Warning_Signals:** Correlación negativa entre ingresos y egresos mensuales; Egresos importantes (impuestos, aguinaldo) en meses de baja estacionalidad; Necesidad de financiamiento en meses predecibles post-temporada; Diferencia entre mes de ingreso y mes de egreso de fondos; Patrón consistente año a año.
**Typical_Causes:** Calendario fiscal no alineado con ciclo de negocio; obligaciones laborales (SAC, vacaciones) en meses de baja actividad; compras estacionales que deben hacerse antes de la temporada de ingresos; inversiones planificadas sin considerar ciclo de caja; falta de planificación financiera anual.
**Business_Impact:** Tensiones de caja recurrentes y predecibles; necesidad de financiamiento estructural para cubrir descalce; mayor costo financiero; imposibilidad de aprovechar descuentos por pago anticipado de impuestos; estrés organizacional.
**Metrics_To_Check:** Descalce Mensual (Ingresos - Egresos); Meses de Déficit y Superávit; Correlación Ingresos vs Egresos Mensuales; Necesidad de Financiamiento por Descalce; Costo Financiero del Descalce.
**Diagnostic_Questions:** ¿Se proyecta el descalce entre ingresos y egresos con 12 meses de anticipación? ¿Se pueden reprogramar algunos egresos para alinearlos con ingresos? ¿Hay opciones de pago fraccionado de impuestos? ¿Se pueden negociar fechas de pago con proveedores? ¿Hay financiamiento específico para cubrir el descalce?
**Recommended_Actions:** Elaborar presupuesto de caja anual identificando descalces; negociar calendarios de pago con proveedores y autoridades fiscales; constituir fondos de reserva en meses de superávit; contratar línea de crédito para cubrir meses de descalce; evaluar si se pueden ajustar ciclos de producción/ventas.
**Severity_Level:** Medium
**Related_Patterns:** CFL-061, CFL-069, CFL-070, CFL-071, CFL-076

### CFL-076
**Pattern_Name:** Efecto Estacional en Ratios de Liquidez
**Category:** Estacionalidad
**Description:** Los ratios de liquidez (liquidez corriente, prueba ácida) varían significativamente según la estacionalidad, y evaluarlos en el momento equivocado puede dar una impresión distorsionada de la salud financiera.
**Observable_Symptoms:** Ratios de liquidez que fluctúan drásticamente según la fecha de evaluación; la empresa parece líquida en ciertos meses e ilíquida en otros; análisis financiero que no considera estacionalidad; comparaciones injustas con períodos anteriores sin ajuste estacional; decisiones basadas en ratios de un mes atípico.
**Early_Warning_Signals:** Variación de Liquidez Corriente > 50% entre meses; Prueba Ácida que pasa de > 1.0 a < 0.5 según el mes; Ratios calculados en fecha de cierre no representativos; Diferencia entre ratio promedio y ratio puntual significativa; Falta de ajuste estacional en análisis financiero.
**Typical_Causes:** Acumulación de inventario estacional que infla activo corriente; cobranza concentrada post-temporada que infla caja; pagos estacionales que reducen pasivo corriente; fecha de cierre contable en momento atípico del ciclo; falta de ajuste estacional en análisis.
**Business_Impact:** Decisiones basadas en información distorsionada; aparente mejora o deterioro de liquidez que es solo estacional; dificultad para evaluar la tendencia real; aprobación o rechazo de crédito basado en ratios no representativos; percepción errónea de la salud financiera.
**Metrics_To_Check:** Liquidez Corriente Mensual (12 meses); Prueba Ácida Mensual (12 meses); Variación Estacional de Ratios; Ratio Ajustado por Estacionalidad; Diferencia entre Ratio de Cierre y Ratio Promedio Anual.
**Diagnostic_Questions:** ¿Se analizan los ratios de liquidez en diferentes momentos del año? ¿Se ajustan los ratios por estacionalidad? ¿La fecha de cierre contable es representativa del ciclo normal? ¿Se comparan períodos equivalentes año contra año? ¿Los prestamistas conocen la estacionalidad del negocio?
**Recommended_Actions:** Calcular y monitorear ratios de liquidez mensualmente; ajustar análisis por estacionalidad; presentar a prestamistas la información estacional para evitar malentendidos; comparar siempre mismo mes vs año anterior; usar promedios móviles de 12 meses para tendencia.
**Severity_Level:** Low
**Related_Patterns:** CFL-069, CFL-070, CFL-075, CFL-085


## Financiamiento Operativo

### CFL-077
**Pattern_Name:** Factoraje como Fuente Permanente de Caja
**Category:** Financiamiento Operativo
**Description:** La empresa utiliza el factoraje (venta de facturas) como fuente permanente y principal de caja, no como herramienta ocasional, indicando dependencia estructural de este costo financiero.
**Observable_Symptoms:** Factoraje utilizado todos los meses sin excepción; el volumen de factoraje es estable o creciente; el costo de factoraje es un gasto recurrente significativo; la empresa no puede operar sin factoraje; los clientes saben que sus facturas se venden.
**Early_Warning_Signals:** Factoraje / Ventas > 30% de forma permanente; Costo de Factoraje / EBITDA > 10%; la empresa no ha reducido su dependencia de factoraje en 2+ años; Factoraje utilizado para cubrir déficit operativo, no solo estacional; Incapacidad de operar sin factoraje.
**Typical_Causes:** CFLO insuficiente para cubrir necesidades operativas; falta de acceso a financiamiento bancario tradicional; política de crédito laxa que genera cartera que solo se puede factorizar; clientes de baja calidad crediticia; incapacidad de cobrar directamente.
**Business_Impact:** Alto costo financiero permanente; erosión de márgenes; dependencia de la factora; señal de debilidad financiera; dificultad para salir del esquema; menor rentabilidad neta.
**Metrics_To_Check:** Factoraje / Ventas (tendencia); Costo de Factoraje / Ventas; Costo de Factoraje / EBITDA; Dependencia de Factoraje para Liquidez; Tasa Efectiva Anual del Factoraje; % de Clientes Factorados.
**Diagnostic_Questions:** ¿Por qué la empresa no puede acceder a financiamiento bancario tradicional? ¿Se ha evaluado el costo real del factoraje vs otras alternativas? ¿Hay un plan para reducir la dependencia? ¿Se puede mejorar la cobranza interna para reducir necesidad de factoraje? ¿Los clientes están satisfechos con el esquema?
**Recommended_Actions:** Desarrollar capacidad de cobranza interna; mejorar políticas de crédito para reducir necesidad de factoraje; buscar alternativas de financiamiento más baratas; reducir gradualmente el volumen factorizado; segmentar: factorizar solo clientes de alto riesgo; mejorar CFLO para reducir dependencia.
**Severity_Level:** Medium
**Related_Patterns:** CFL-008, CFL-044, CFL-078, CFL-081, CFL-082

### CFL-078
**Pattern_Name:** Confirmación como Extensión de Plazos
**Category:** Financiamiento Operativo
**Description:** La empresa utiliza confirming (financiamiento de proveedores a través del banco) para extender artificialmente sus plazos de pago más allá de lo razonable, trasladando el costo a los proveedores.
**Observable_Symptoms:** Plazos de pago muy largos (90-120 días) sostenidos por confirming; proveedores que se quejan de los plazos; el costo del confirming se descuenta del pago al proveedor; proveedores que aumentan precios para compensar; el confirming se usa como regla, no como excepción.
**Early_Warning_Signals:** Plazos de Pago > 90 días sostenidos con confirming; Proveedores que descuentan el costo del confirming en precios; Quejas de proveedores por plazos excesivos; Costo del Confirming / Compras en aumento; Proveedores que dejan de vender por plazos.
**Typical_Causes:** Necesidad de financiamiento operativo; cultura de "estirar pagos al máximo"; falta de empatía con proveedores; poder de negociación que permite imponer condiciones; tesorería que busca optimizar DPP sin considerar relaciones.
**Business_Impact:** Deterioro de relaciones con proveedores; sobrecosto implícito (proveedores ajustan precios); riesgo de perder proveedores clave; imagen negativa en el mercado; eventual dificultad para encontrar proveedores.
**Metrics_To_Check:** DPP vs Promedio del Sector; Costo Implícito del Confirming (diferencia de precio); Proveedores Perdidos por Plazos / Año; Quejas de Proveedores por Plazos; Tasa de Descuento del Confirming.
**Diagnostic_Questions:** ¿Los proveedores ajustan precios por los plazos de pago? ¿Cuál es el costo implícito total de los plazos extendidos? ¿Hay proveedores que han dejado de vender por los plazos? ¿Se ha evaluado el impacto en la relación con proveedores? ¿Hay una política de plazos máximos por tipo de proveedor?
**Recommended_Actions:** Revisar política de plazos de pago; segmentar proveedores: plazos más cortos para estratégicos; evaluar el costo implícito de plazos largos vs beneficio; negociar plazos razonables que no deterioren la relación; considerar alternativas de financiamiento que no afecten a proveedores.
**Severity_Level:** Low
**Related_Patterns:** CFL-030, CFL-047, CFL-053, CFL-083

### CFL-079
**Pattern_Name:** Descuento de Cesión de Créditos sin Recurso
**Category:** Financiamiento Operativo
**Description:** La empresa cede créditos sin recurso (la factora asume el riesgo de incobrabilidad), lo que puede indicar que su cartera es de baja calidad o que busca mejorar sus ratios financieros.
**Observable_Symptoms:** Cese de créditos sin recurso de forma habitual; prima de riesgo alta en las operaciones; la factora tiene criterios de selección estrictos; clientes que no califican para cesión sin recurso se venden con recurso; mejora de ratios de balance (menos cuentas por cobrar, menos deuda).
**Early_Warning_Signals:** Cesión sin Recurso / Ventas a Crédito > 20%; Prima de Riesgo > 2% del valor de la factura; Factora rechaza clientes por riesgo crediticio; Baja calidad de cartera reflejada en condiciones; Operaciones sin recurso reemplazan a cobranza directa.
**Typical_Causes:** Cartera de clientes de baja calidad crediticia; necesidad de mejorar ratios financieros (balance); falta de capacidad de cobranza interna; estrategia de transferir riesgo de crédito; clientes con historial de incumplimiento.
**Business_Impact:** Mayor costo financiero (prima de riesgo); dependencia de la factora para gestión de crédito; pérdida de control sobre relación con clientes; posible señal de debilidad; menor margen por costo de la operación.
**Metrics_To_Check:** Cesión sin Recurso / Ventas a Crédito; Prima de Riesgo Promedio; % de Clientes Rechazados por Factora; Costo Total de Cesión sin Recurso vs Beneficio; Diferencia de Costo vs Cesión con Recurso.
**Diagnostic_Questions:** ¿Por qué se ceden créditos sin recurso? ¿El costo es menor que tener cobranza interna? ¿Los clientes saben que sus facturas se ceden? ¿Se ha evaluado mejorar la cobranza interna en lugar de ceder? ¿Hay alternativas más baratas?
**Recommended_Actions:** Evaluar si es más barato mejorar cobranza interna que ceder sin recurso; segmentar: ceder sin recurso solo clientes de alto riesgo; desarrollar capacidad de evaluación crediticia para reducir necesidad de cesión; buscar alternativas de financiamiento; negociar mejores condiciones con la factora.
**Severity_Level:** Low
**Related_Patterns:** CFL-044, CFL-077, CFL-081, CFL-082

### CFL-080
**Pattern_Name:** Leasing Operativo como Financiamiento Encubierto
**Category:** Financiamiento Operativo
**Description:** La empresa utiliza leasing operativo como forma de financiamiento encubierto para activos que deberían comprarse, generando un costo mayor a largo plazo y ocultando deuda en el balance.
**Observable_Symptoms:** Leasing de activos que son críticos y de larga duración; renovación constante de contratos de leasing; el costo total del leasing excede el precio de compra del activo; falta de activos fijos propios en el balance; cuotas de leasing elevadas que presionan el CFLO.
**Early_Warning_Signals:** Leasing Operativo / Activos Fijos Totales > 50%; Cuotas de Leasing / CFLO > 10%; Activos críticos en leasing sin opción de compra; Contratos de leasing que se renuevan automáticamente; Costo Total del Leasing > Precio de Compra + Financiamiento.
**Typical_Causes**: Falta de capital para comprar activos; restricciones de deuda (covenants) que impiden más endeudamiento; ventajas fiscales del leasing; cultura de "no ser dueño de activos"; falta de evaluación del costo total del leasing vs compra.
**Business_Impact:** Mayor costo a largo plazo; CFLO comprometido por cuotas de leasing; falta de activos propios que limitan garantías; deuda oculta que distorsiona análisis financiero; dependencia del leasing para operar.
**Metrics_To_Check:** Leasing Operativo / Activos Fijos Totales; Cuotas de Leasing / CFLO; Costo Total del Leasing vs Precio de Compra; Duración del Leasing vs Vida Útil del Activo; Endeudamiento Ajustado por Leasing.
**Diagnostic_Questions:** ¿Se ha evaluado la opción de compra vs leasing? ¿El costo total del leasing es menor que comprar con financiamiento? ¿Los activos en leasing son críticos para la operación? ¿Hay opción de compra al final del contrato? ¿El leasing oculta el verdadero nivel de endeudamiento?
**Recommended_Actions:** Evaluar compra de activos críticos con financiamiento vs leasing; negociar opciones de compra en contratos de leasing; renegociar cuotas de leasing a la baja; considerar si ciertos activos conviene comprarlos (larga vida útil); transparentar el leasing como deuda en análisis financieros.
**Severity_Level:** Medium
**Related_Patterns:** CFL-011, CFL-015, CFL-056, CFL-086

### CFL-081
**Pattern_Name:** Línea de Sobregiro como Capital de Trabajo
**Category:** Financiamiento Operativo
**Description:** La empresa utiliza la línea de sobregiro (descubierto en cuenta corriente) como fuente permanente de capital de trabajo, lo que es extremadamente caro y riesgoso.
**Observable_Symptoms:** Sobregiro utilizado permanentemente; el saldo deudor de cuenta corriente nunca se regulariza; altas comisiones e intereses por sobregiro; el banco llama periódicamente por el uso del sobregiro; la empresa no puede mantener saldo positivo.
**Early_Warning_Signals:** Sobregiro > 30 días consecutivos; Intereses y Comisiones de Sobregiro / Gastos Bancarios > 30%; Uso del Sobregiro como % del Límite > 80%; el sobregiro es la principal fuente de financiamiento; el banco solicita regularización.
**Typical_Causes:** Falta de línea de crédito formal; CFLO insuficiente; mala planificación de tesorería; falta de acceso a financiamiento más barato; descalce estructural entre cobros y pagos.
**Business_Impact:** Costo financiero extremadamente alto; riesgo de que el banco cancele la facilidad; deterioro de relación bancaria; imposibilidad de planificar; señal de mala gestión financiera.
**Metrics_To_Check:** Sobregiro Promedio / Mes; Costo Anual del Sobregiro (intereses + comisiones); Días de Uso Continuo del Sobregiro; Sobregiro / Ventas; Diferencia de Costo vs Línea de Crédito Formal.
**Diagnostic_Questions:** ¿Por qué no se solicita una línea de crédito formal? ¿Cuál es el costo anual del sobregiro? ¿Se ha evaluado el ahorro de convertir el sobregiro en préstamo? ¿El banco está cómodo con el uso actual? ¿Hay alternativas de financiamiento?
**Recommended_Actions:** Solicitar línea de crédito formal para reemplazar sobregiro; negociar con el banco mejores condiciones; implementar presupuesto de caja semanal; mantener colchón de caja para evitar sobregiros; considerar factoring como alternativa para reducir necesidad de sobregiro.
**Severity_Level:** High
**Related_Patterns:** CFL-022, CFL-062, CFL-067, CFL-082, CFL-085

### CFL-082
**Pattern_Name:** Descuento de Pagarés como Rutina
**Category:** Financiamiento Operativo
**Description:** La empresa descuenta pagarés (documentos) de manera rutinaria como su principal fuente de financiamiento, indicando dependencia del descuento de documentos para operar.
**Observable_Symptoms:** Descuento de pagarés todos los meses sin excepción; el banco descuenta documentos automáticamente; la empresa no puede operar sin descuento; los pagarés descontados son de clientes habituales; el costo del descuento es un gasto recurrente significativo.
**Early_Warning_Signals:** Pagarés Descontados / Ventas a Crédito > 40%; Costo de Descuento / Ventas en aumento; Descuento utilizado para cubrir déficit operativo (no solo estacional); la empresa descuenta documentos de todos los clientes; Dependencia del Banco para descontar.
**Typical_Causes:** CFLO insuficiente; falta de acceso a otras fuentes de financiamiento; cultura de financiarse con descuento de documentos; clientes que solo aceptan pagarés; política de crédito basada en documentos.
**Business_Impact:** Alto costo financiero recurrente; dependencia del banco para descontar; riesgo de que el banco rechace documentos; exposición a cambios en tasa de descuento; menor margen por costo financiero.
**Metrics_To_Check:** Pagarés Descontados / Ventas a Crédito; Costo de Descuento / Ventas; Tasa de Descuento Efectiva Anual; Dependencia del Descuento para Liquidez; % de Documentos Rechazados por el Banco.
**Diagnostic_Questions:** ¿Por qué la empresa no puede acceder a otras fuentes de financiamiento? ¿Se ha evaluado el costo real del descuento vs otras alternativas? ¿Hay clientes que pagan a término sin necesidad de pagaré? ¿Se puede reducir la dependencia del descuento mejorando cobranzas? ¿El banco ha rechazado documentos alguna vez?
**Recommended_Actions:** Buscar alternativas de financiamiento más baratas; mejorar cobranza directa para reducir necesidad de descuento; segmentar: descontar solo documentos de clientes de alto riesgo; negociar mejores tasas de descuento con el banco; reducir gradualmente el volumen descontado.
**Severity_Level:** Medium
**Related_Patterns:** CFL-022, CFL-044, CFL-077, CFL-081

### CFL-083
**Pattern_Name:** Financiamiento de Proveedores como Única Fuente
**Category:** Financiamiento Operativo
**Description:** La empresa depende exclusivamente del crédito comercial de proveedores como fuente de financiamiento, sin acceso a financiamiento bancario, lo que limita su capacidad de gestión de caja.
**Observable_Symptoms:** Cuentas por pagar son la principal (o única) fuente de financiamiento; no hay deuda bancaria; los proveedores financian la operación; plazos de pago extendidos al máximo; la empresa no califica para crédito bancario.
**Early_Warning_Signals:** Cuentas por Pagar / Pasivo Total > 70%; No hay deuda bancaria en el balance; Proveedores son la única fuente de financiamiento; DPP > 90 días; Proveedores comienzan a restringir crédito; Quejas de proveedores por plazos.
**Typical_Causes:** Falta de acceso a financiamiento bancario (historial crediticio, garantías insuficientes); mala relación bancaria; el negocio no califica para crédito formal; cultura de financiarse con proveedores; costo implícito no evaluado.
**Business_Impact:** Límite al crecimiento (solo se puede crecer hasta donde los proveedores financien); riesgo de que un proveedor corte el crédito; deterioro de relaciones con proveedores; sobrecosto implícito (mayores precios); vulnerabilidad ante cambios en condiciones de proveedores.
**Metrics_To_Check:** Cuentas por Pagar / Pasivo Total; Cuentas por Pagar / Ventas; DPP; Costo Implícito del Financiamiento de Proveedores (diferencia de precio vs contado); Acceso a Fuentes Alternativas de Financiamiento.
**Diagnostic_Questions:** ¿Por qué la empresa no accede a financiamiento bancario? ¿Se ha evaluado el costo implícito del financiamiento de proveedores? ¿Hay algún plan para obtener crédito bancario? ¿Los proveedores están cómodos con el nivel actual de financiamiento? ¿Qué pasa si un proveedor clave reduce el crédito?
**Recommended_Actions:** Desarrollar relación bancaria (abrir cuentas, usar productos básicos); construir historial crediticio; buscar garantías para acceder a crédito formal; diversificar fuentes de financiamiento; evaluar el costo real del financiamiento de proveedores vs bancario; negociar con proveedores condiciones más estables.
**Severity_Level:** Medium
**Related_Patterns:** CFL-030, CFL-047, CFL-053, CFL-078, CFL-089

### CFL-084
**Pattern_Name:** Deuda con Garantía de Flujo Futuro
**Category:** Financiamiento Operativo
**Description:** La empresa toma deuda garantizada con flujos de efectivo futuros (contratos, cuentas por cobrar futuras, flujo de proyectos), comprometiendo ingresos que aún no se han generado.
**Observable_Symptoms:** Préstamos garantizados con contratos futuros; cesión de derechos de cobro futuros; deuda que se paga con un porcentaje de ventas futuras; la empresa compromete flujos que aún no existen; estructura de deuda atada a desempeño futuro.
**Early_Warning_Signals:** Deuda Garantizada con Flujo Futuro / Deuda Total > 30%; Incumplimiento de Proyecciones de Flujo; Covenants ligados a flujo futuro que se activan; Renegociación de condiciones por flujo menor al esperado; Presión por generar el flujo prometido.
**Typical_Causes:** Falta de garantías tradicionales (activos fijos, avales); necesidad de financiamiento sin colateral; confianza excesiva en proyecciones de flujo; presión de prestamistas por garantías; estructura de financiamiento innovadora pero riesgosa.
**Business_Impact:** Presión por generar flujo para cumplir con la garantía; riesgo de incumplimiento si el flujo no se materializa; pérdida de control sobre ingresos futuros; menor flexibilidad operativa; posible default técnico.
**Metrics_To_Check:** Deuda con Garantía de Flujo Futuro / Deuda Total; Proyección de Flujo vs Real; Cobertura de Deuda con Flujo Real; Incumplimiento de Covenants; % de Ingresos Futuros Comprometidos.
**Diagnostic_Questions:** ¿Las proyecciones de flujo futuro son realistas? ¿Qué pasa si el flujo no se materializa según lo proyectado? ¿Hay margen de seguridad en las proyecciones? ¿Se ha evaluado el costo de esta estructura vs alternativas? ¿Hay covenants que puedan activarse?
**Recommended_Actions:** Proyectar flujos de manera conservadora; mantener margen de seguridad en proyecciones; diversificar fuentes de financiamiento; negociar covenants flexibles; monitorear cumplimiento de proyecciones mensualmente; buscar alternativas de financiamiento con garantías tradicionales.
**Severity_Level:** Medium
**Related_Patterns:** CFL-018, CFL-024, CFL-085, CFL-092


## Riesgo de Iliquidez

### CFL-085
**Pattern_Name:** Quiebra Técnica por Falta de Liquidez
**Category:** Riesgo de Iliquidez
**Description:** La empresa es técnicamente solvente (patrimonio neto positivo) pero no tiene liquidez para pagar sus obligaciones de corto plazo, lo que puede llevar a una cesación de pagos.
**Observable_Symptoms:** Activos > Pasivos (solvencia contable) pero no hay efectivo para pagar; imposibilidad de pagar obligaciones inmediatas a pesar de tener activos; activos ilíquidos (inventario, maquinaria, propiedades) que no se pueden convertir rápidamente en efectivo; proveedores y empleados sin cobrar; el negocio tiene valor pero no efectivo.
**Early_Warning_Signals:** Liquidez Corriente < 1.0 con Patrimonio Neto Positivo; Prueba Ácida < 0.5; Activos Corrientes compuestos principalmente por inventario y cuentas por cobrar; Diferencia significativa entre activo corriente líquido y pasivo corriente; CFLO insuficiente para cubrir pasivo corriente.
**Typical_Causes:** Crecimiento excesivo que consume toda la liquidez; acumulación de inventario y cuentas por cobrar; falta de gestión de capital de trabajo; descalce de plazos; inversiones en activos fijos que inmovilizaron la caja.
**Business_Impact:** Posible cesación de pagos a pesar de tener un negocio viable; necesidad de liquidar activos a precios de remate; pérdida de valor para accionistas; riesgo de concurso preventivo o quiebra; daño reputacional.
**Metrics_To_Check:** Liquidez Corriente; Prueba Ácida; CFLO / Pasivo Corriente; Días de Caja; Diferencia entre Patrimonio Neto y Liquidez; Activos Líquidos / Pasivo Corriente.
**Diagnostic_Questions:** ¿Cuánto efectivo inmediato tiene la empresa vs sus obligaciones de corto plazo? ¿Qué activos se pueden liquidar rápidamente para generar efectivo? ¿Hay acceso a financiamiento de emergencia? ¿Se puede negociar una espera con acreedores? ¿La empresa es viable en el mediano plazo?
**Recommended_Actions:** Gestión de emergencia de liquidez: vender activos no estratégicos, negociar espera con acreedores, buscar capitalización urgente; mejorar conversión de activos a efectivo (cobrar, vender inventario); reestructurar deuda de corto a largo plazo; considerar concurso preventivo si es necesario; implementar plan de liquidez de emergencia.
**Severity_Level:** Critical
**Related_Patterns:** CFL-001, CFL-058, CFL-062, CFL-086, CFL-088, CFL-089

### CFL-086
**Pattern_Name:** Descalce de Plazos entre Activos y Pasivos
**Category:** Riesgo de Iliquidez
**Description:** Existe un descalce entre los plazos de vencimiento de los activos (lentos en convertirse en efectivo) y los pasivos (exigibles en corto plazo), generando riesgo de iliquidez.
**Observable_Symptoms:** Activos de largo plazo financiados con pasivos de corto plazo; vencimientos de deuda concentrados en el corto plazo mientras los activos tardan en generar efectivo; necesidad de refinanciar constantemente; tensión de caja recurrente; el negocio es solvente en el largo plazo pero ilíquido en el corto.
**Early_Warning_Signals:** Pasivo Corriente / Activo Corriente > 1.0; Deuda CP / Activos Líquidos > 1.0; Diferencia entre Plazo Promedio de Activos y Pasivos; Activos Fijos / Pasivo CP (descalce); Renovación constante de deuda CP.
**Typical_Causes:** Financiamiento inadecuado (deuda corta para activos largos); crecimiento acelerado sin estructura financiera adecuada; falta de acceso a financiamiento de LP; decisiones financieras sin considerar plazos; presión de prestamistas por garantías que lleva a deuda CP.
**Business_Impact:** Riesgo permanente de iliquidez; dependencia de refinanciación constante; exposición a cambios en condiciones crediticias; estrés de gestión; posible default técnico.
**Metrics_To_Check:** Ratio de Liquidez Corriente; Prueba Ácida; Deuda CP / Deuda Total; Plazo Promedio de Activos vs Pasivos; Diferencia de Plazos (años); Activos Fijos / Pasivo LP.
**Diagnostic_Questions:** ¿Los activos de largo plazo están financiados con deuda de largo plazo? ¿Hay activos que generan efectivo antes de que venzan los pasivos? ¿Se puede extender el plazo de la deuda? ¿Hay activos líquidos para cubrir descalces? ¿Se puede vender activos de LP para pagar deuda CP?
**Recommended_Actions:** Reestructurar deuda: convertir CP en LP; vender activos de lenta rotación para pagar deuda CP; alinear plazos de financiamiento con plazos de activos; mantener colchón de activos líquidos; establecer política de financiamiento: activos LP -> pasivos LP.
**Severity_Level:** Critical
**Related_Patterns:** CFL-032, CFL-055, CFL-058, CFL-085, CFL-088

### CFL-087
**Pattern_Name:** Ratio de Liquidez Ácida en Caída
**Category:** Riesgo de Iliquidez
**Description:** El ratio de liquidez ácida (activo corriente - inventario / pasivo corriente) muestra una tendencia decreciente sostenida, indicando deterioro en la capacidad de la empresa para pagar obligaciones de corto plazo sin depender de la venta de inventario.
**Observable_Symptoms:** Prueba ácida disminuyendo trimestre a trimestre; la empresa depende cada vez más de vender inventario para pagar deudas; activos líquidos (caja, cuentas por cobrar) no cubren pasivo corriente; tensión de caja creciente; proveedores exigen garantías.
**Early_Warning_Signals:** Prueba Ácida < 1.0 y decreciente; Tendencia de Prueba Ácida a la baja por 4+ trimestres; Prueba Ácida < 0.5; Relación Caja + Cuentas por Cobrar / Pasivo Corriente en descenso; Diferencia creciente entre liquidez corriente y ácida (por inventario).
**Typical_Causes:** Acumulación de inventario que no se vende; aumento de deuda de corto plazo; cuentas por cobrar que no se cobran; CFLO insuficiente; crecimiento financiado con deuda CP.
**Business_Impact:** Deterioro de la capacidad de pago inmediato; mayor riesgo de incumplimiento; dificultad para obtener crédito; percepción de riesgo por proveedores y bancos; eventual iliquidez.
**Metrics_To_Check:** Prueba Ácida (tendencia 12 meses); Caja + Cuentas por Cobrar / Pasivo Corriente; Diferencia entre Liquidez Corriente y Prueba Ácida; CFLO / Pasivo Corriente; Días de Caja.
**Diagnostic_Questions:** ¿Qué componente de la prueba ácida está empeorando (caja, cuentas por cobrar, pasivo corriente)? ¿El deterioro es por aumento de deuda CP o por reducción de activos líquidos? ¿Hay activos líquidos adicionales disponibles? ¿Se puede convertir inventario en efectivo rápidamente? ¿Hay acceso a financiamiento de emergencia?
**Recommended_Actions:** Reducir pasivo corriente (pagar deuda CP con activos LP); aumentar activos líquidos (cobrar, vender inventario); convertir deuda CP en LP; mejorar CFLO; establecer meta de prueba ácida mínima; monitorear mensualmente.
**Severity_Level:** High
**Related_Patterns:** CFL-085, CFL-086, CFL-088, CFL-089

### CFL-088
**Pattern_Name:** Concentración de Vencimientos de Deuda
**Category:** Riesgo de Iliquidez
**Description:** Los vencimientos de deuda de la empresa se concentran en un período corto (mismo mes, mismo trimestre), generando un pico de exigibilidad que la caja no puede cubrir.
**Observable_Symptoms:** Varios préstamos vencen en el mismo período; pico de pagos de deuda concentrado; necesidad de refinanciar múltiples deudas simultáneamente; tensión de caja en fechas de vencimiento; solicitudes de refinanciación de varios bancos a la vez.
**Early_Warning_Signals:** > 30% de la deuda total vence en un trimestre; Concentración de Vencimientos en un período < 3 meses; Diferencia entre vencimientos mensuales máxima y mínima > 3x; Renovación de múltiples líneas en misma fecha; Dependencia de refinanciación simultánea.
**Typical_Causes:** Falta de planificación de estructura de deuda; contratación de préstamos sin considerar perfil de vencimientos; refinanciaciones que no escalonan vencimientos; crecimiento desordenado del endeudamiento; falta de gestión activa del pasivo.
**Business_Impact:** Riesgo de no poder pagar todos los vencimientos simultáneamente; presión sobre la caja en períodos específicos; dependencia de refinanciación múltiple; mayor poder de negociación del banco; posible default técnico si no se renueva.
**Metrics_To_Check:** Perfil de Vencimientos (trimestral/anual); % de Deuda que Vence en Próximos 3 Meses; Concentración de Vencimientos (máximo mensual / promedio mensual); Vencimientos / CFLO Mensual; Vencimientos / Caja Disponible.
**Diagnostic_Questions:** ¿Cuándo vencen las principales obligaciones de deuda? ¿Hay concentración de vencimientos en algún período? ¿Se puede escalonar los vencimientos? ¿Hay capacidad de pago sin refinanciar? ¿Qué pasa si los bancos no renuevan?
**Recommended_Actions:** Escalonar vencimientos de deuda; negociar con bancos para distribuir pagos; mantener línea de crédito contingente para cubrir picos de vencimiento; preparar plan de contingencia si no se renueva; no concentrar vencimientos en misma fecha; gestionar activamente el perfil de vencimientos.
**Severity_Level:** High
**Related_Patterns:** CFL-018, CFL-019, CFL-024, CFL-085, CFL-086, CFL-090

### CFL-089
**Pattern_Name:** Pérdida de Líneas de Crédito
**Category:** Riesgo de Iliquidez
**Description:** La empresa pierde líneas de crédito o líneas existentes no son renovadas, reduciendo drásticamente su acceso a financiamiento y generando riesgo de iliquidez.
**Observable_Symptoms:** Bancos que no renuevan líneas; reducción de límites de crédito; nuevas condiciones más estrictas; llamadas del banco solicitando reducción de exposición; dificultad para abrir nuevas líneas en otros bancos; dependencia de cada vez menos fuentes de financiamiento.
**Early_Warning_Signals:** Líneas no renovadas / Líneas Totales; Reducción de Límites de Crédito; Bancos que exigen garantías adicionales; Aumento de tasas en renovaciones; Dificultad para abrir nuevas líneas; Dependencia de líneas existentes en aumento.
**Typical_Causes:** Deterioro de situación financiera de la empresa; incumplimientos previos; cambio en política de riesgo del banco; concentración de deuda en pocos bancos; falta de relación bancaria activa.
**Business_Impact:** Reducción drástica de acceso a financiamiento; riesgo de iliquidez si no se reemplazan las líneas; necesidad de buscar financiamiento más caro; posible default si no se encuentran alternativas; deterioro de operaciones.
**Metrics_To_Check:** Líneas de Crédito Disponibles / Líneas Totales; Número de Bancos con Líneas Activas; Límites de Crédito (tendencia); Tasa de Renovación de Líneas; Dependencia de cada Banco (% de deuda total).
**Diagnostic_Questions:** ¿Por qué se perdieron las líneas? ¿Hay alternativas en otros bancos? ¿Se puede reemplazar la capacidad de crédito perdida? ¿La empresa puede operar con menos crédito? ¿Se está trabajando activamente en diversificar fuentes de financiamiento?
**Recommended_Actions:** Diversificar fuentes de financiamiento; mantener relación con múltiples bancos; mejorar situación financiera para recuperar acceso; buscar alternativas no bancarias (factoraje, confirming, proveedores); preparar plan de contingencia para reducción de crédito.
**Severity_Level:** Critical
**Related_Patterns:** CFL-022, CFL-081, CFL-083, CFL-085, CFL-090

### CFL-090
**Pattern_Name:** Dependencia de Refinanciación para Continuar Operando
**Category:** Riesgo de Iliquidez
**Description:** La empresa necesita refinanciar su deuda para continuar operando, lo que significa que sin nueva deuda no puede pagar la existente ni mantener sus operaciones.
**Observable_Symptoms:** Sin refinanciación, la empresa no puede pagar; el CFLO no cubre servicio de deuda; la empresa necesita "nueva deuda para pagar la vieja"; los prestamistas son clave para la supervivencia; nerviosismo en fechas de renovación.
**Early_Warning_Signals:** Relación CFLO / Servicio de Deuda < 1.0; Nueva Deuda necesaria para pagar Deuda Existente; Dependencia de Aprobación de Renovación; Sin refinanciación, la empresa no puede pagar; Prestamistas expresan dudas sobre renovación.
**Typical_Causes:** CFLO insuficiente para servir deuda; apalancamiento excesivo; deuda contratada a plazos muy cortos; negocio con baja generación de caja; mala estructura financiera.
**Business_Impact:** Riesgo existencial si un prestamista no renueva; dependencia total de la banca; imposibilidad de planificar a largo plazo; estrés permanente; eventual default si se corta el crédito.
**Metrics_To_Check:** CFLO / Servicio de Deuda; Deuda / CFLO; CFLO Libre (después de servicio de deuda); Dependencia de Refinanciación (% de deuda que necesita renovarse); Tasa de Renovación Histórica.
**Diagnostic_Questions:** ¿La empresa podría pagar su deuda si los bancos no refinancian? ¿Cuánto tiempo puede operar sin nueva deuda? ¿Hay activos líquidos para pagar deuda? ¿Hay fuentes alternativas de financiamiento? ¿Los accionistas pueden aportar capital?
**Recommended_Actions:** Reducir dependencia de refinanciación: mejorar CFLO, vender activos, capitalizar; diversificar fuentes de financiamiento; extender plazos de deuda; construir reserva de efectivo; preparar plan de contingencia para no renovación.
**Severity_Level:** Critical
**Related_Patterns:** CFL-018, CFL-019, CFL-085, CFL-088, CFL-089

### CFL-091
**Pattern_Name:** Erosión de la Caja por Resultados Negativos
**Category:** Riesgo de Iliquidez
**Description:** La empresa consume su caja de manera sostenida debido a resultados operativos negativos (pérdidas), reduciendo progresivamente su colchón de liquidez.
**Observable_Symptoms:** Caja disminuye período a período; pérdidas operativas consistentes; el negocio quema efectivo; reducción de activos líquidos; necesidad de financiamiento para cubrir pérdidas.
**Early_Warning_Signals:** CFLO negativo consistente; Caja (Efectivo) con tendencia decreciente; Resultado Neto Negativo por 2+ trimestres; Días de Caja en descenso; CFLO negativo más grande que la caja disponible.
**Typical_Causes:** Pérdidas operativas recurrentes; márgenes negativos; costos fijos superiores a ingresos; modelo de negocio no viable; gastos fuera de control.
**Business_Impact:** Agotamiento del colchón de liquidez; eventual iliquidez total; necesidad de capitalización o cierre; pérdida de valor para accionistas; camino hacia la insolvencia.
**Metrics_To_Check:** Saldo de Caja (tendencia); Resultado Neto (tendencia); CFLO; Días de Caja; Tasa de Consumo de Caja (Cash Burn Rate); Tiempo hasta Caja Cero (Runway).
**Diagnostic_Questions:** ¿A qué velocidad se consume la caja? ¿Cuánto tiempo queda antes de quedarse sin efectivo? ¿Hay un plan para revertir las pérdidas? ¿Se pueden reducir costos drásticamente? ¿Los accionistas están dispuestos a capitalizar?
**Recommended_Actions:** Urgente: reducir costos drásticamente; buscar capitalización de accionistas; evaluar viabilidad del negocio; si no es viable, considerar cierre ordenado; si es viable, implementar plan de reestructuración; monitorear caja semanalmente.
**Severity_Level:** Critical
**Related_Patterns:** CFL-001, CFL-007, CFL-010, CFL-085, CFL-093

### CFL-092
**Pattern_Name:** Covenant Financiero que se Activa por Iliquidez
**Category:** Riesgo de Iliquidez
**Description:** Un covenant (cláusula contractual) financiero se activa debido al deterioro de la liquidez, dando al prestamista el derecho de exigir pago anticipado o modificar condiciones.
**Observable_Symptoms:** Covenant de liquidez (ej. liquidez corriente mínima) incumplido; banco notifica incumplimiento de covenant; renegociación forzada de condiciones de deuda; amenaza de aceleración de pago; necesidad de waiver del banco.
**Early_Warning_Signals:** Ratios de Covenant cerca del límite; Covenant de Liquidez Corriente o Prueba Ácida en riesgo; Multas o penalidades por incumplimiento; Bancos solicitan información financiera más frecuente; Renegociación de condiciones.
**Typical_Causes:** Deterioro de liquidez no anticipado; covenants mal diseñados (demasiado ajustados); falta de monitoreo de covenants; crecimiento que deteriora ratios; desconocimiento de las cláusulas del contrato.
**Business_Impact:** Riesgo de aceleración de pago de deuda; renegociación forzada en condiciones desfavorables; mayores tasas de interés; pérdida de flexibilidad financiera; posible default técnico.
**Metrics_To_Check:** Ratios de Covenant Actuales vs Límites; Margen de Seguridad (ratio actual - límite del covenant); Frecuencia de Incumplimientos; Número de Waivers Solicitados; Costo de Renegociación por Covenant.
**Diagnostic_Questions:** ¿Se monitorean los covenants activamente? ¿Qué tan cerca están los ratios actuales de los límites? ¿Qué pasa si se incumple un covenant? ¿Hay margen de negociación con el banco? ¿Se puede modificar el covenant para dar más holgura?
**Recommended_Actions:** Monitorear covenants mensualmente con proyecciones; mantener margen de seguridad sobre límites; negociar covenants más flexibles; comunicar proactivamente al banco si hay riesgo de incumplimiento; preparar plan de contingencia si se activa.
**Severity_Level:** High
**Related_Patterns:** CFL-018, CFL-024, CFL-085, CFL-087, CFL-088

### CFL-093
**Pattern_Name:** Iliquidez Oculta por Partidas No Monetarias
**Category:** Riesgo de Iliquidez
**Description:** La empresa parece tener liquidez en sus estados financieros, pero parte de sus activos corrientes son partidas no monetarias (inventario de lenta rotación, créditos fiscales, cuentas por cobrar de dudoso cobro) que no se convertirán en efectivo en el corto plazo.
**Observable_Symptoms:** Liquidez corriente aparentemente saludable pero problemas de caja reales; activo corriente inflado por partidas no líquidas; dificultad para convertir activos corrientes en efectivo; diferencia entre liquidez contable y liquidez real; sorpresa cuando se necesita efectivo y no está disponible.
**Early_Warning_Signals:** Prueba Ácida significativamente menor que Liquidez Corriente; Activo Corriente compuesto por > 50% de inventario y créditos fiscales; Cuentas por Cobrar con alta morosidad; Créditos Fiscales de difícil recuperación; Diferencia entre Caja Real y Activo Corriente Líquido.
**Typical_Causes:** Acumulación de inventario de lenta rotación; créditos fiscales generados por pérdidas o estructura tributaria; cuentas por cobrar de clientes morosos; falta de castigo de activos de dudosa realización; maquillaje de balances.
**Business_Impact:** Percepción errónea de liquidez; decisiones equivocadas basadas en ratios; sorpresas desagradables cuando se necesita efectivo; imposibilidad de pagar obligaciones a pesar de "activo corriente" suficiente.
**Metrics_To_Check:** Liquidez Corriente vs Prueba Ácida; Activos Líquidos / Activo Corriente; % de Activo Corriente No Monetario; Créditos Fiscales / Activo Corriente; Calidad de Cuentas por Cobrar (% vencida); Tiempo de Conversión a Efectivo de Activos Corrientes.
**Diagnostic_Questions:** ¿Cuánto del activo corriente es realmente convertible en efectivo en 30 días? ¿Hay inventario de baja rotación o cuentas por cobrar vencidas? ¿Los créditos fiscales son realmente recuperables? ¿Se han castigado activos de dudosa realización? ¿La liquidez real es menor que la contable?
**Recommended_Actions:** Depurar activo corriente: castigar inventario obsoleto y cuentas incobrables; gestionar activamente recuperación de créditos fiscales; mejorar calidad de cuentas por cobrar; separar en reportes activos líquidos vs no líquidos; evaluar liquidez real (no solo contable).
**Severity_Level:** High
**Related_Patterns:** CFL-028, CFL-029, CFL-037, CFL-058, CFL-085
