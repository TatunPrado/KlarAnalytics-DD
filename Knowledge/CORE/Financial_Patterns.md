# Financial Patterns — SME Knowledge Base

> Base de conocimiento para que agentes de IA detecten patrones financieros relevantes en PyMEs: liquidez, solvencia, rentabilidad, endeudamiento, capital de trabajo, estructura de costos, EBITDA, márgenes, ROA, ROE, punto de equilibrio, apalancamiento, productividad financiera y crecimiento rentable.

---

## Categorías cubiertas

| # | Categoría | Patrones |
|---|-----------|----------|
| 1 | Liquidity | 10 |
| 2 | Solvency | 10 |
| 3 | Profitability | 10 |
| 4 | Indebtedness | 10 |
| 5 | Working Capital | 10 |
| 6 | Cost Structure | 10 |
| 7 | EBITDA | 10 |
| 8 | Margins | 11 |
| 9 | ROA | 8 |
| 10 | ROE | 8 |
| 11 | Break-Even Point | 7 |
| 12 | Leverage | 8 |
| 13 | Financial Productivity | 9 |
| 14 | Profitable Growth | 12 |
| **Total** | | **133** |

---

## Liquidity

### FIN-001
**Pattern_Name:** Chronic Negative Working Capital
**Category:** Liquidity
**Description:** La empresa opera consistentemente con capital de trabajo negativo, financiando operaciones con proveedores y pasivos de corto plazo.
**Observable_Symptoms:** Proveedores cobran antes de que la empresa cobre a sus clientes; uso constante de sobregiros; pagos atrasados a proveedores.
**Early_Warning_Signals:** Current ratio <1.0 sostenido; días de pago a proveedores extendiéndose; dependencia de líneas de crédito para operar.
**Typical_Causes:** Crecimiento no financiado; ciclos de conversión de efectivo largos; mala gestión de cuentas por cobrar.
**Business_Impact:** Riesgo de quiebra técnica si proveedores cortan crédito; estrés constante de caja; incapacidad para invertir.
**Metrics_To_Check:** Current ratio; Quick ratio; Días de cobro, pago e inventario; Ciclo de conversión de efectivo.
**Diagnostic_Questions:** ¿Cuántos días pasan entre que pagas a proveedores y cobras a clientes? ¿Tienes suficiente caja para cubrir 30 días de operaciones?
**Recommended_Actions:** Acelerar cobro (descuentos por pronto pago, factoring); negociar plazos mayores con proveedores; reducir días de inventario.
**Severity_Level:** Critical
**Related_Patterns:** FIN-005, FIN-031, FIN-041

### FIN-002
**Pattern_Name:** Cash Conversion Cycle Explosion
**Category:** Liquidity
**Description:** El ciclo de conversión de efectivo se ha alargado peligrosamente (90+ días) por combinación de cobros lentos, inventario alto y pagos rápidos.
**Observable_Symptoms:** Caja cada vez más ajustada a pesar de ventas estables; necesidad creciente de financiamiento; quejas de falta de liquidez.
**Early_Warning_Signals:** CCC aumentando trimestre a trimestre; días de cobro >60; días de inventario >90.
**Typical_Causes:** Clientes que pagan tarde; falta de política de crédito; inventario obsoleto acumulado; proveedores con plazos cortos.
**Business_Impact:** Capital de trabajo consume todo el flujo; necesidad de deuda para operar; rentabilidad se destruye por costos financieros.
**Metrics_To_Check:** CCC = Días inventario + Días cobro - Días pago; tendencia trimestral del CCC; participación en P&L de gastos financieros.
**Diagnostic_Questions:** ¿Cuánto tiempo pasa desde que pagas materia prima hasta que cobras al cliente? ¿Este ciclo se está alargando?
**Recommended_Actions:** Reducir días de cobro (cobranza preventiva, descuentos); reducir inventario (just-in-time, venta de obsoleto); extender plazos con proveedores.
**Severity_Level:** Critical
**Related_Patterns:** FIN-001, FIN-031, FIN-041

### FIN-003
**Pattern_Name:** Overtrading (Growth Without Liquidity)
**Category:** Liquidity
**Description:** La empresa crece en ventas tan rápido que la liquidez no alcanza para financiar el capital de trabajo requerido.
**Observable_Symptoms:** Ventas suben pero la caja empeora; proveedores presionando por pago; sobregiro bancario al límite; dueño inyectando capital personal.
**Early_Warning_Signals:** Crecimiento de ventas >30% sin acceso a financiamiento; capital de trabajo creciendo más que las ventas; uso de deuda de corto plazo para financiar crecimiento.
**Typical_Causes:** Crecimiento acelerado sin planificación financiera; clientes que pagan a 60-90 días mientras se paga a proveedores a 30; falta de capital de trabajo disponible.
**Business_Impact:** Crecimiento no rentable; posible quiebra por iliquidez (crecer hasta morir); dilución de dueños si se busca inversión urgente.
**Metrics_To_Check:** Tasa de crecimiento de ventas vs capital de trabajo; Ratio capital de trabajo / ventas; Días de caja disponible.
**Diagnostic_Questions:** ¿El crecimiento de ventas está mejorando o empeorando tu caja? ¿Tienes suficiente capital de trabajo para financiar el crecimiento proyectado?
**Recommended_Actions:** Frenar crecimiento hasta asegurar financiamiento; buscar línea de crédito revolving; negociar mejores plazos con clientes y proveedores.
**Severity_Level:** Critical
**Related_Patterns:** FIN-001, FIN-002, FIN-127

### FIN-004
**Pattern_Name:** False Liquidity (Undrawn Credit Lines)
**Category:** Liquidity
**Description:** La empresa reporta liquidez adecuada pero depende de líneas de crédito no utilizadas que podrían ser revocadas o no renovadas.
**Observable_Symptoms:** Caja reportada incluye líneas de crédito disponibles; el negocio no sobreviviría sin acceso a deuda; renovación de líneas genera ansiedad.
**Early_Warning_Signals:** Líneas de crédito representan >50% de la liquidez reportada; covenants bancarios cerca de incumplirse; banco pide garantías adicionales.
**Typical_Causes:** Cultura de depender de deuda para operar; falta de capital de trabajo propio; reporting financiero que infla liquidez.
**Business_Impact:** Si el banco revoca la línea, la empresa quiebra en semanas; falsa sensación de seguridad; decisiones de inversión basadas en liquidez ficticia.
**Metrics_To_Check:** Liquidez real (caja + inversiones líquidas) vs liquidez reportada (incluyendo líneas); % de línea de crédito utilizada históricamente; covenants bancarios.
**Diagnostic_Questions:** ¿Qué % de tu liquidez es caja real vs líneas de crédito? ¿Podrías operar 90 días sin acceso a deuda?
**Recommended_Actions:** Reducir dependencia de deuda de corto plazo; fortalecer capital de trabajo; mantener caja real equivalente a 60 días de gastos.
**Severity_Level:** Critical
**Related_Patterns:** FIN-001, FIN-003, FIN-041

### FIN-005
**Pattern_Name:** Current Ratio Deterioration
**Category:** Liquidity
**Description:** El ratio de liquidez corriente (activo corriente/pasivo corriente) ha disminuido consistentemente por debajo de 1.5 y sigue bajando.
**Observable_Symptoms:** Dificultad creciente para pagar obligaciones de corto plazo; proveedores exigen pago anticipado; uso recurrente de sobregiros.
**Early_Warning_Signals:** Current ratio <1.5 y decreciente; quick ratio <0.8; pasivo corriente creciendo más rápido que activo corriente.
**Typical_Causes:** Pérdidas recurrentes que consumen capital de trabajo; crecimiento financiado con pasivo de corto plazo; distribución excesiva de dividendos.
**Business_Impact:** Riesgo de insolvencia técnica; deterioro de relaciones con proveedores; costo financiero alto por deuda de corto plazo.
**Metrics_To_Check:** Current ratio histórico; Quick ratio; Capital de trabajo neto; Evolución de pasivo corriente.
**Diagnostic_Questions:** ¿Tu activo corriente cubre adecuadamente tus obligaciones de corto plazo? ¿El ratio ha empeorado en los últimos períodos?
**Recommended_Actions:** Reducir pasivo corriente (renegociar plazos, convertir deuda CP a LP); aumentar activo corriente (cobrar más rápido, vender inventario lento).
**Severity_Level:** High
**Related_Patterns:** FIN-001, FIN-002, FIN-006

### FIN-006
**Pattern_Name:** Negative Cash Flow from Operations
**Category:** Liquidity
**Description:** La empresa genera flujo de efectivo operativo negativo de forma recurrente, consumiendo caja en lugar de generarla.
**Observable_Symptoms:** La empresa necesita financiamiento externo para operar mensualmente; utilidades contables positivas pero flujo de caja negativo; dueño confundido sobre a dónde va el dinero.
**Early_Warning_Signals:** CFO negativo por >2 trimestres consecutivos; utilidad neta positiva pero CFO negativo; crecimiento de cuentas por cobrar mayor al crecimiento de ventas.
**Typical_Causes:** Crecimiento no financiado; clientes que no pagan; inventario que no rota; gastos operativos que crecen más que ingresos.
**Business_Impact:** Dependencia perpetua de deuda o capital; imposibilidad de crecer sin financiamiento externo; eventual insolvencia.
**Metrics_To_Check:** CFO; CFO / Utilidad Neta; CFO / Ventas; CFO / Deuda Total.
**Diagnostic_Questions:** ¿Tu negocio genera efectivo o lo consume? ¿Tus utilidades contables se convierten en efectivo?
**Recommended_Actions:** Diagnosticar causas del CFO negativo (cobranza, inventario, rentabilidad, crecimiento); implementar plan de generación de caja; reducir gastos; mejorar cobranza.
**Severity_Level:** Critical
**Related_Patterns:** FIN-003, FIN-005, FIN-056

### FIN-007
**Pattern_Name:** Liquidity Hoarding (Excessive Cash)
**Category:** Liquidity
**Description:** La empresa mantiene niveles de caja excesivos (20%+ de activos totales) que no generan rentabilidad, sacrificando retorno.
**Observable_Symptoms:** Grandes saldos en cuentas corrientes sin rendimiento; dueño prefiere caja antes que invertir; oportunidades de inversión perdidas.
**Early_Warning_Signals:** Caja >15% de activos totales consistentemente; ROA bajo por exceso de activos no productivos; sin inversiones en crecimiento o mejora.
**Typical_Causes:** Fundador con aversión al riesgo; trauma financiero previo; falta de oportunidades de inversión; desconfianza en el sistema financiero.
**Business_Impact:** Rentabilidad sub-óptima; destrucción de valor por inflación; oportunidades de crecimiento perdidas; rendimientos muy por debajo del costo de capital.
**Metrics_To_Check:** Caja / Activos totales; Caja / Ventas mensuales; ROA vs WACC; Rentabilidad de la caja.
**Diagnostic_Questions:** ¿Cuántos meses de gastos tienes en caja? ¿Ese exceso está generando algún rendimiento? ¿Podrías invertir parte en el negocio con mejor retorno?
**Recommended_Actions:** Establecer política de caja objetivo (3-6 meses de gastos); invertir excesos en instrumentos de renta fija de corto plazo; evaluar inversiones en el negocio con VAN positivo.
**Severity_Level:** Medium
**Related_Patterns:** FIN-008, FIN-071, FIN-101

### FIN-008
**Pattern_Name:** Liquidity Mismatch in Asset-Liability Structure
**Category:** Liquidity
**Description:** La empresa financia activos de largo plazo (inversiones fijas) con pasivos de corto plazo, creando un descalce de plazos.
**Observable_Symptoms:** Necesidad constante de refinanciar deudas de corto plazo para activos que generan retorno a largo plazo; estrés recurrente en fechas de vencimiento.
**Early_Warning_Signals:** Activos fijos financiados con pasivo corriente; relación deuda LP / activos fijos <0.5; vencimientos de deuda concentrados en <12 meses para activos con vida útil >5 años.
**Typical_Causes:** Falta de acceso a crédito de largo plazo; crecimiento apresurado; mala estructuración financiera; presión de bancos por garantías.
**Business_Impact:** Riesgo de refinanciamiento; vulnerabilidad a cambios en tasas de interés; ciclo perpetuo de estrés de caja.
**Metrics_To_Check:** Deuda CP / Deuda Total; Activos fijos / Pasivo LP; Calce de plazos (gap analysis).
**Diagnostic_Questions:** ¿Estás financiando maquinaria o infraestructura con deuda que vence antes de que esos activos generen retorno?
**Recommended_Actions:** Reestructurar deuda: convertir corto plazo en largo plazo; alinear plazos de deuda con vida útil de activos; buscar leasing o financiamiento específico.
**Severity_Level:** High
**Related_Patterns:** FIN-005, FIN-041, FIN-053

### FIN-009
**Pattern_Name:** Checking Account Trap
**Category:** Liquidity
**Description:** La empresa usa la cuenta corriente bancaria como indicador de liquidez, sin hacer proyección de flujo de caja, operando a ciegas.
**Observable_Symptoms:** Decisiones basadas en saldo disponible hoy; sorpresas de falta de fondos; cheques rebotados; pagos atrasados no intencionales.
**Early_Warning_Signals:** Sin proyección de flujo de caja a 30-60-90 días; sobregiros frecuentes; dueño revisa saldo a diario con ansiedad.
**Typical_Causes:** Falta de sofisticación financiera; cultura reactiva; dueño operativo sin tiempo para planificar; ausencia de herramientas de gestión.
**Business_Impact:** Falta de visibilidad lleva a decisiones sub-óptimas; costos por intereses moratorios y cargos; relaciones tensas con proveedores.
**Metrics_To_Check:** Diferencia entre saldo proyectado y real; frecuencia de sobregiros; costo de cargos bancarios.
**Diagnostic_Questions:** ¿Tienes una proyección de caja a 30-60-90 días? ¿O solo miras el saldo de hoy?
**Recommended_Actions:** Implementar proyección de flujo de caja semanal con rolling 13 semanas; revisar semanalmente; capacitar al equipo en gestión de caja.
**Severity_Level:** High
**Related_Patterns:** FIN-001, FIN-002, FIN-010

### FIN-010
**Pattern_Name:** Hidden Cash Drains
**Category:** Liquidity
**Description:** Existen salidas de caja no obvias que drenan liquidez sin que la empresa las identifique: gastos bancarios, comisiones, intereses punitorios, retiros personales, pagos duplicados.
**Observable_Symptoms:** Caja que se desvanece sin explicación clara; dueño no sabe por qué no sobra dinero; ganancias contables no se reflejan en caja.
**Early_Warning_Signals:** Diferencia sistemática entre flujo proyectado y real; gastos bancarios creciendo; retiros personales no contabilizados; suscripciones olvidadas.
**Typical_Causes:** Falta de control de tesorería; gastos hormiga no monitoreados; mezcla de finanzas personales y empresariales; comisiones bancarias no negociadas.
**Business_Impact:** Pérdida de liquidez evitable; rentabilidad menor a la real; falsa sensación de que el negocio no genera efectivo.
**Metrics_To_Check:** Gastos bancarios como % de ingresos; diferencia entre EBITDA y CFO; conciliación mensual de todas las salidas.
**Diagnostic_Questions:** ¿Revisas cada salida de tu cuenta bancaria? ¿Sabes exactamente a dónde se fue el efectivo del último mes?
**Recommended_Actions:** Hacer auditoría de gastos bancarios y suscripciones; separar finanzas personales y empresariales; implementar conciliación bancaria semanal; negociar comisiones con bancos.
**Severity_Level:** Medium
**Related_Patterns:** FIN-006, FIN-009, FIN-041
---

## Solvency

### FIN-011
**Pattern_Name:** Negative Equity (Liabilities Exceed Assets)
**Category:** Solvency
**Description:** El patrimonio neto es negativo: las deudas totales superan el valor de los activos, indicando insolvencia estructural.
**Observable_Symptoms:** Balance con patrimonio negativo; empresa opera con deuda mayor que sus activos; ninguna entidad financiera otorga crédito sin garantías personales.
**Early_Warning_Signals:** Razón de endeudamiento >1.0; patrimonio neto decreciente por pérdidas acumuladas; capital de trabajo negativo persistente.
**Typical_Causes:** Pérdidas recurrentes no capitalizadas; distribución excesiva de dividendos; inversiones fallidas no provisionadas; pasivos ocultos.
**Business_Impact:** Empresa técnicamente en quiebra; imposibilidad de obtener crédito; dueños deben inyectar capital o liquidar; riesgo de concurso preventivo.
**Metrics_To_Check:** Patrimonio neto; Ratio deuda/patrimonio; Tendencia del patrimonio; Resultados acumulados.
**Diagnostic_Questions:** ¿Tu patrimonio neto es positivo? ¿Cuánto vale realmente la empresa después de pagar todas las deudas?
**Recommended_Actions:** Capitalización de deuda (conversión en patrimonio); inyección de capital de accionistas; acuerdo con acreedores; considerar reestructuración judicial o liquidación ordenada.
**Severity_Level:** Critical
**Related_Patterns:** FIN-012, FIN-014, FIN-042

### FIN-012
**Pattern_Name:** Debt Service Coverage Ratio < 1.0
**Category:** Solvency
**Description:** La empresa no genera suficiente EBITDA para cubrir los pagos de intereses y amortizaciones de deuda.
**Observable_Symptoms:** Dificultad para pagar cuotas de créditos; refinanciación constante de deudas; uso de caja de operación para pagar deuda.
**Early_Warning_Signals:** DSCR <1.1; EBITDA cubre intereses pero no amortizaciones; necesidad de nueva deuda para pagar deuda existente.
**Typical_Causes:** Excesivo endeudamiento; caída de EBITDA; inversiones que no generan retorno esperado; aumento de tasas de interés.
**Business_Impact:** Incumplimiento de covenants bancarios; pérdida de garantías; ejecución de deuda; eventual quiebra.
**Metrics_To_Check:** DSCR = EBITDA / (Intereses + Amortizaciones de capital); Cobertura de intereses (EBITDA / Intereses); EBITDA / Deuda total.
**Diagnostic_Questions:** ¿Tu EBITDA cubre todas tus obligaciones financieras del año? ¿Cuánto margen tienes antes de incumplir?
**Recommended_Actions:** Incrementar EBITDA (reducir costos, mejorar precios); reestructurar deuda (extender plazos, reducir tasas); vender activos no estratégicos para reducir deuda.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-042, FIN-056

### FIN-013
**Pattern_Name:** Debt Covenant Imminent Breach
**Category:** Solvency
**Description:** La empresa está cerca de incumplir los covenants (cláusulas contractuales) de sus créditos bancarios, lo que podría gatillar aceleración de pagos.
**Observable_Symptoms:** Área financiera dedicada a reportar a bancos; comunicación tensa con ejecutivos de cuenta; búsqueda de waivers y exenciones.
**Early_Warning_Signals:** Ratios financieros cercanos a límites covenant; banco solicita información adicional; auditoría externa requerida por el banco.
**Typical_Causes:** Endeudamiento al límite; caída de EBITDA; crecimiento de deuda por encima de lo pactado; cambio en políticas contables.
**Business_Impact:** Aceleración de deuda; ejecución de garantías; pérdida de control del negocio; quiebra.
**Metrics_To_Check:** Distancia a covenants (EBITDA/Intereses, Deuda Neta/EBITDA, etc.); Historial de cumplimiento; Comunicaciones con bancos.
**Diagnostic_Questions:** ¿Conoces los covenants de tus créditos? ¿A qué distancia estás de incumplirlos?
**Recommended_Actions:** Negociar waivers antes del incumplimiento; renegociar covenants menos restrictivos; reducir deuda o aumentar EBITDA.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-012, FIN-042

### FIN-014
**Pattern_Name:** Technical Insolvency (Liabilities > Fair Value of Assets)
**Category:** Solvency
**Description:** Aunque el balance muestre patrimonio positivo, el valor de mercado de los activos es menor que las deudas al considerar deterioros, obsolescencia o sobrevaloración contable.
**Observable_Symptoms:** Activos en libros sobrevalorados; inventario que no se vende al valor registrado; maquinaria obsoleta valorada a costo histórico.
**Early_Warning_Signals:** Activos con más de 5 años sin revaluación; inventario de lenta rotación valorado a costo; goodwill o intangibles significativos.
**Typical_Causes:** Falta de deterioro contable; activos que perdieron valor de mercado; maquinaria obsoleta; créditos incobrables no provisionados.
**Business_Impact:** Patrimonio real negativo; empresa no vendible al valor en libros; riesgo de insolvencia si se liquidan activos.
**Metrics_To_Check:** Valor de mercado vs valor en libros de activos principales; % de inventario obsoleto; % de cuentas por cobrar vencidas no provisionadas.
**Diagnostic_Questions:** ¿Cuánto valen realmente tus activos si los vendieras hoy? ¿Tus activos en libros reflejan su valor real?
**Recommended_Actions:** Realizar deterioro de activos (impairment) para tener balance realista; vender activos improductivos; capitalizar pérdidas.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-042, FIN-071

### FIN-015
**Pattern_Name:** Zombie Company (Generational Insolvency)
**Category:** Solvency
**Description:** La empresa genera apenas suficiente efectivo para pagar intereses pero no para reducir deuda ni reinvertir, condenada a existir sin crecer.
**Observable_Symptoms:** EBITDA apenas cubre intereses; no hay capex; deuda no se reduce; dueño sobrevive pero no prospera.
**Early_Warning_Signals:** Cobertura de intereses entre 1.0 y 1.5 por años; deuda estable (no se reduce); sin inversión en activos fijos ni I+D.
**Typical_Causes:** Excesiva deuda heredada; negocio maduro en declive; falta de reinversión; márgenes comprimidos estructuralmente.
**Business_Impact:** Estancamiento perpetuo; exposición a cualquier shock externo; empresa pierde valor real por inflación; imposibilidad de atraer inversión o talento.
**Metrics_To_Check:** Cobertura de intereses; Capex / Depreciación; Crecimiento de ingresos vs inflación; Deuda neta / EBITDA.
**Diagnostic_Questions:** ¿Tu empresa genera suficiente efectivo para crecer y reducir deuda, o solo para sobrevivir? ¿Cuánto hace que no inviertes?
**Recommended_Actions:** Reestructuración de deuda agresiva; considerar venta o fusión para salir del círculo vicioso; turnaround operativo radical.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-012, FIN-015

### FIN-016
**Pattern_Name:** Balloon Payment Maturity Wall
**Category:** Solvency
**Description:** La empresa tiene vencimientos de deuda concentrados en un período corto sin capacidad de pago proyectada.
**Observable_Symptoms:** Ansiedad creciente a medida que se acercan vencimientos; equipo financiero dedicado a refinanciar; búsqueda urgente de nuevos créditos.
**Early_Warning_Signals:** Más del 40% de la deuda total vence en los próximos 12 meses; sin línea de crédito comprometida; perfil de vencimientos no diversificado.
**Typical_Causes:** Deuda estructurada con bullet payment; créditos de corto plazo para proyectos largos; falta de planificación financiera.
**Business_Impact:** Riesgo de refinanciamiento; si el banco no renueva, default; negociación en posición de debilidad.
**Metrics_To_Check:** Perfil de vencimientos de deuda; % de deuda que vence en 12 meses; fuentes de refinanciamiento identificadas.
**Diagnostic_Questions:** ¿Tienes un calendario de vencimientos de deuda? ¿Sabes cómo pagarás cada vencimiento? ¿Tienes compromisos de refinanciamiento?
**Recommended_Actions:** Diversificar perfil de vencimientos; adelantar refinanciamiento (no esperar al vencimiento); estructurar deuda con amortizaciones graduales.
**Severity_Level:** High
**Related_Patterns:** FIN-008, FIN-012, FIN-042

### FIN-017
**Pattern_Name:** Contingent Liability Blindness
**Category:** Solvency
**Description:** La empresa tiene pasivos contingentes significativos (juicios laborales, fiscales, avales) no registrados que pueden materializarse y destruir el patrimonio.
**Observable_Symptoms:** Juicios laborales o fiscales en curso; avales otorgados a terceros; garantías cruzadas con otras empresas; contingencias no reveladas.
**Early_Warning_Signals:** Juicios laborales/fiscales activos sin provisión; avales a terceros sin contrapartida; garantías personales del dueño significativas.
**Typical_Causes:** Falta de asesoría legal preventiva; cultura de no provisionar; avales otorgados sin análisis de riesgo; exposición fiscal no gestionada.
**Business_Impact:** Materialización de contingencia puede llevar a insolvencia; el dueño pierde patrimonio personal; empresa no vendible hasta resolver.
**Metrics_To_Check:** Provisiones por contingencias vs ingresos; cantidad de juicios activos; exposición máxima estimada; garantías personales.
**Diagnostic_Questions:** ¿Tienes juicios activos? ¿Están provisionados? ¿Qué avales o garantías has otorgado? ¿Cuál sería el impacto si se materializan?
**Recommended_Actions:** Identificar y cuantificar todas las contingencias; provisionar adecuadamente; resolver judicial o extrajudicialmente; implementar programa de compliance laboral y fiscal.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-014, FIN-042

### FIN-018
**Pattern_Name:** Personal Guarantee Overexposure
**Category:** Solvency
**Description:** El dueño ha otorgado garantías personales por deudas de la empresa que exceden su patrimonio personal.
**Observable_Symptoms:** Dueño avala personalmente todos los créditos; patrimonio personal comprometido; imposibilidad de separar riesgo personal y empresarial.
**Early_Warning_Signals:** Garantías personales > 2x el patrimonio personal del dueño; empresa con covenants ajustados; dueño con activos personales como colateral.
**Typical_Causes:** Bancos exigen garantías personales en PyMEs; falta de separación legal; empresa sin historial crediticio propio.
**Business_Impact:** Si la empresa quiebra, el dueño pierde todo su patrimonio personal; decisiones empresariales condicionadas por miedo personal; imposibilidad de retiro.
**Metrics_To_Check:** Garantías personales vs patrimonio personal del dueño; Empresa como % del riesgo total del dueño.
**Diagnostic_Questions:** ¿Cuánto de tu patrimonio personal está en riesgo por la empresa? ¿Podrías sobrevivir financieramente si la empresa quebrara?
**Recommended_Actions:** Reducir deuda con garantías personales; construir crédito corporativo independiente; limitar nuevas garantías personales; considerar separación societaria.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-017, FIN-042

### FIN-019
**Pattern_Name:** Hidden Liabilities from Related Parties
**Category:** Solvency
**Description:** La empresa tiene pasivos no registrados con partes relacionadas: préstamos de accionistas, empresas vinculadas, familiares, que pueden exigirse en cualquier momento.
**Observable_Symptoms:** Deudas con accionistas sin documentar; préstamos de familiares sin plazo ni interés; falta de formalidad en cuentas corrientes mercantiles.
**Early_Warning_Signals:** Cuentas por pagar a accionistas significativas sin vencimiento; partidas de balance poco claras; asambleas de accionistas sin resolución de préstamos.
**Typical_Causes:** Informalidad en la gestión financiera; cultura de préstamos familiares; falta de asesoría legal-contable.
**Business_Impact:** Pasivos ocultos que pueden exigirse inesperadamente; conflictos familiares; falsa solvencia reportada; problemas en due diligence.
**Metrics_To_Check:** Cuentas por pagar a accionistas y relacionados; % de deuda con partes relacionadas; documentación de préstamos.
**Diagnostic_Questions:** ¿Hay préstamos de accionistas o familiares a la empresa? ¿Están documentados? ¿Tienen plazo e interés definido?
**Recommended_Actions:** Documentar y formalizar todas las deudas con partes relacionadas; establecer plazos, intereses y condiciones; considerar capitalización de deuda.
**Severity_Level:** Medium
**Related_Patterns:** FIN-011, FIN-014, FIN-042

### FIN-020
**Pattern_Name:** Debt Acceleration Risk from Cross-Default
**Category:** Solvency
**Description:** Los contratos de deuda contienen cláusulas cross-default que pueden acelerar todas las deudas si se incumple una sola obligación.
**Observable_Symptoms:** Varios créditos con el mismo banco o vinculados; incumplimiento de un crédito amenaza todo el resto; banco tiene poder de ejecución general.
**Early_Warning_Signals:** Contratos con cross-default clause; todas las deudas con una sola entidad financiera; concentración de riesgo en un banco.
**Typical_Causes:** Financiamiento concentrado en un banco; contratos estándar con cross-default; falta de diversificación de fuentes de financiamiento.
**Business_Impact:** Incumplimiento menor puede acelerar toda la deuda; pérdida total de control de la empresa; quiebra desencadenada por un evento pequeño.
**Metrics_To_Check:** Existencia de cross-default en contratos; concentración de deuda por entidad; % de deuda con cross-default.
**Diagnostic_Questions:** ¿Tus contratos de deuda tienen cláusulas cross-default? ¿Si incumples un crédito, se acelera toda la deuda?
**Recommended_Actions:** Diversificar fuentes de financiamiento; negociar eliminación o limitación de cross-default; monitorear cumplimiento de todos los contratos.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-013, FIN-042
---

## Profitability

### FIN-021
**Pattern_Name:** Revenue Growth with Profit Decline
**Category:** Profitability
**Description:** La empresa crece en ventas pero la utilidad neta disminuye, indicando problemas de rentabilidad marginal.
**Observable_Symptoms:** Ventas subiendo pero ganancias planas o cayendo; dueño frustrado porque vende más y gana menos; esfuerzo creciente sin recompensa.
**Early_Warning_Signals:** Margen neto decreciente; crecimiento de gastos operativos > crecimiento de ventas; costo de ventas como % de ingresos aumentando.
**Typical_Causes:** Descuentos agresivos para crecer; estructura de costos fijos alta; mezcla de productos hacia menor margen; ineficiencias operativas.
**Business_Impact:** Crecimiento destruye valor; empresa cada vez más vulnerable; eventualmente pérdidas a pesar de altas ventas.
**Metrics_To_Check:** Margen neto histórico; Spread entre crecimiento de ingresos y crecimiento de costos; Margen incremental por unidad de crecimiento.
**Diagnostic_Questions:** ¿Cada peso adicional vendido genera más o menos ganancia que el anterior? ¿Estás creciendo rentablemente?
**Recommended_Actions:** Analizar rentabilidad por cliente/línea; ajustar precios; controlar gastos comerciales; mejorar eficiencia operativa.
**Severity_Level:** Critical
**Related_Patterns:** FIN-002, FIN-056, FIN-127

### FIN-022
**Pattern_Name:** Negative Operating Leverage
**Category:** Profitability
**Description:** Los costos fijos crecen más rápido que las ventas, haciendo que cada unidad adicional vendida sea menos rentable.
**Observable_Symptoms:** Gastos de estructura (administración, alquileres, sueldos fijos) creciendo sin aumento proporcional de ventas; punto de equilibrio subiendo.
**Early_Warning_Signals:** Gastos operativos fijos / Ventas > 30% y creciente; Punto de equilibrio aumentando; nuevas contrataciones sin aumento de productividad.
**Typical_Causes:** Contrataciones excesivas en áreas administrativas; inversiones en estructura antes que en ventas; falta de disciplina en gastos fijos.
**Business_Impact:** Caída de ventas golpea más fuerte por alto apalancamiento operativo; márgenes comprimidos; dificultad para ajustar costos rápido.
**Metrics_To_Check:** Gastos fijos operativos / Ventas; Punto de equilibrio en unidades; Apalancamiento operativo (DOL).
**Diagnostic_Questions:** ¿Tus costos fijos están creciendo más que tus ventas? ¿Qué pasa si las ventas caen 20% con estos costos fijos?
**Recommended_Actions:** Congelar contrataciones administrativas; tercerizar funciones fijas; convertir costos fijos en variables donde sea posible.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-081

### FIN-023
**Pattern_Name:** Profit Erosion by Inflation
**Category:** Profitability
**Description:** La empresa no traslada la inflación a sus precios, erosionando silenciosamente la rentabilidad real.
**Observable_Symptoms:** Márgenes que bajan lentamente sin causa aparente; misma utilidad nominal pero menor poder adquisitivo; dueño nota que el dinero rinde menos.
**Early_Warning_Signals:** Inflación acumulada >15% sin ajuste de precios; margen bruto disminuyendo tendencialmente; costos subiendo más que precios.
**Typical_Causes:** Miedo a perder clientes; contratos de largo plazo sin indexación; falta de proceso de revisión de precios; mercado competitivo.
**Business_Impact:** Erosión progresiva de rentabilidad; empresa trabaja cada vez más por menos; puede pasar de rentable a pérdida sin notarlo.
**Metrics_To_Check:** Diferencia entre inflación acumulada y ajuste de precios; Margen bruto real (ajustado por inflación); EBITDA real.
**Diagnostic_Questions:** ¿Tus precios suben al mismo ritmo que tus costos? ¿Cuánto hace que no ajustas precios por inflación?
**Recommended_Actions:** Indexar precios a inflación automáticamente; revisar precios mensualmente en alta inflación; incluir cláusulas de ajuste en contratos.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-101

### FIN-024
**Pattern_Name:** Fixed Cost Bleed (High SG&A)
**Category:** Profitability
**Description:** Los gastos de administración y ventas (SG&A) son desproporcionadamente altos respecto al estándar de la industria, consumiendo el margen bruto.
**Observable_Symptoms:** Equipo administrativo grande para el volumen; estructura corporativa pesada; gastos de representación y viajes elevados.
**Early_Warning_Signals:** SG&A >30% de ingresos; SG&A creciendo más que ventas; múltiples capas gerenciales; gastos discrecionales sin control.
**Typical_Causes:** Exceso de personal administrativo; cultura de gastos sin control; dueño con estilo de vida cargado a la empresa; falta de presupuesto y control.
**Business_Impact:** Márgenes netos bajos o negativos a pesar de buen margen bruto; empresa no competitiva; imposibilidad de invertir en crecimiento.
**Metrics_To_Check:** SG&A / Ventas; SG&A por empleado; Comparación con benchmark de industria; Gastos discrecionales / Ventas.
**Diagnostic_Questions:** ¿Tu estructura administrativa es proporcional a tu tamaño? ¿Podrías reducir SG&A en 20% sin afectar ventas?
**Recommended_Actions:** Reducir personal administrativo; implementar presupuesto cero (zero-based budgeting); eliminar gastos discrecionales no esenciales.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-022, FIN-056

### FIN-025
**Pattern_Name:** Product Mix Deterioration
**Category:** Profitability
**Description:** La mezcla de productos/servicios se ha desplazado hacia opciones de menor margen, reduciendo la rentabilidad agregada aunque las ventas totales se mantengan.
**Observable_Symptoms:** Mismos ingresos totales pero menor ganancia; clientes comprando más productos baratos; equipo de ventas incentivado a vender lo fácil (bajo margen).
**Early_Warning_Signals:** Margen bruto total decreciente con ingresos estables; % de ventas de productos de alto margen disminuyendo; descuentos promedios creciendo.
**Typical_Causes:** Competencia empuja precios a la baja; equipo comercial sin incentivos de margen; entrada a segmentos de menor valor; falta de innovación en productos premium.
**Business_Impact:** Rentabilidad estructuralmente más baja; necesidad de vender más para igualar ganancia; espiral de commoditización.
**Metrics_To_Check:** Margen bruto por línea de producto; % de ventas de productos premium vs básicos; Margen bruto ponderado.
**Diagnostic_Questions:** ¿Estás vendiendo más productos de bajo margen que antes? ¿Tus incentivos comerciales consideran margen o solo volumen?
**Recommended_Actions:** Revisar incentivos comerciales para priorizar margen; rediseñar mix de productos hacia mayor valor; eliminar productos de bajo margen.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-081

### FIN-026
**Pattern_Name:** Negative Contribution Margin Products
**Category:** Profitability
**Description:** La empresa mantiene productos/líneas con margen de contribución negativo que destruyen valor con cada venta.
**Observable_Symptoms:** Productos que se venden pero al calcular costos variables completos dejan pérdida; equipo insiste en mantenerlos por tradición o volumen.
**Early_Warning_Signals:** Margen de contribución <0 para ciertos SKUs; productos que requieren descuentos profundos para venderse; costos variables > precio de venta.
**Typical_Causes:** Fijación de precios incorrecta; costos variables no identificados; subvención cruzada no intencional; inercia comercial.
**Business_Impact:** Cada venta de esos productos agrava las pérdidas; recursos asignados ineficientemente; rentabilidad agregada sub-óptima.
**Metrics_To_Check:** Margen de contribución por SKU/línea; % de productos con margen de contribución negativo; Costo variable total vs precio.
**Diagnostic_Questions:** ¿Todos tus productos dejan un margen positivo después de costos variables? ¿Sabes cuáles son tus productos más y menos rentables?
**Recommended_Actions:** Eliminar productos con margen de contribución negativo; aumentar precio o reducir costo variable; reemplazar con alternativas rentables.
**Severity_Level:** Critical
**Related_Patterns:** FIN-021, FIN-025, FIN-081

### FIN-027
**Pattern_Name:** EBITDA Margin Compression
**Category:** Profitability
**Description:** El margen EBITDA se ha comprimido consistentemente durante varios períodos, señal de deterioro competitivo o estructural.
**Observable_Symptoms:** Margen EBITDA cayendo año a año; dueño nota que rinde menos; presión constante sobre precios y costos.
**Early_Warning_Signals:** Margen EBITDA disminuyendo >1% anual por 3+ años; EBITDA creciendo menos que ingresos; competidores con márgenes estables.
**Typical_Causes:** Aumento de costos no trasladado a precios; entrada de nuevos competidores; pérdida de eficiencia; mix de producto desfavorable.
**Business_Impact:** Menor generación de caja; menos capacidad de inversión; empresa menos valiosa (múltiplos más bajos); vulnerabilidad creciente.
**Metrics_To_Check:** Margen EBITDA histórico; EBITDA / Ventas; Benchmark de margen EBITDA vs industria; Tendencia de últimos 5 años.
**Diagnostic_Questions:** ¿Tu margen EBITDA ha bajado en los últimos años? ¿Sabes por qué? ¿Es un problema de precios, costos o mix?
**Recommended_Actions:** Diagnosticar causas (precios, costos, mix); implementar plan de recuperación de margen; considerar reposicionamiento estratégico.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-081

### FIN-028
**Pattern_Name:** One-Time Gain Dependency
**Category:** Profitability
**Description:** La utilidad neta se sostiene artificialmente con ingresos no recurrentes (venta de activos, juicios ganados, subvenciones), ocultando pérdidas operativas.
**Observable_Symptoms:** Utilidad neta positiva pero resultado operativo negativo; ventas de activos recurrentes; ingresos extraordinarios cada año.
**Early_Warning_Signals:** Resultados extraordinarios >30% de la utilidad neta; venta de activos fijos para generar caja; subsidios o ayudas gubernamentales significativos.
**Typical_Causes:** Negocio principal no rentable; necesidad de mostrar resultados; dependencia de eventos no recurrentes.
**Business_Impact:** La verdadera rentabilidad del negocio es negativa; cuando se agoten los activos o subsidios, la quiebra es inevitable; empresa no sostenible.
**Metrics_To_Check:** Resultado operativo vs utilidad neta; % de utilidad de ingresos no recurrentes; EBITDA ajustado (excluyendo one-offs).
**Diagnostic_Questions:** ¿Tu utilidad neta viene de la operación o de eventos extraordinarios? ¿Qué pasa si no puedes vender activos este año?
**Recommended_Actions:** Separar y reportar ingresos recurrentes vs no recurrentes; enfocar en alcanzar rentabilidad operativa; considerar cierre si el negocio no es viable.
**Severity_Level:** Critical
**Related_Patterns:** FIN-006, FIN-021, FIN-056

### FIN-029
**Pattern_Name:** SG&A Growing Ahead of Revenue
**Category:** Profitability
**Description:** Los gastos de estructura crecen sistemáticamente más que los ingresos, indicando pérdida de eficiencia y control de gastos.
**Observable_Symptoms:** Cada año se gasta más en administración y ventas como % de ingresos; nuevas contrataciones sin aumento de productividad; estructura sobredimensionada.
**Early_Warning_Signals:** Crecimiento SG&A > crecimiento Revenue por >2 años consecutivos; ratio SG&A/Revenue aumentando; headcount administrativo creciendo más que headcount operativo.
**Typical_Causes:** Falta de disciplina presupuestaria; crecimiento de personal sin criterio; duplicación de funciones; beneficios excesivos.
**Business_Impact:** Márgenes operativos comprimidos; necesita cada vez más ingresos para cubrir estructura; punto de equilibrio sube peligrosamente.
**Metrics_To_Check:** SG&A / Revenue; Crecimiento SG&A vs Revenue; Gasto por empleado administrativo.
**Diagnostic_Questions:** ¿Tus gastos de administración crecen al mismo ritmo que tus ventas? ¿Podrías mantener el mismo nivel de servicio con menos estructura?
**Recommended_Actions:** Implementar zero-based budgeting; congelar contrataciones no críticas; renegociar contratos de servicios; revisar procesos para eliminar redundancias.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-024, FIN-027

### FIN-030
**Pattern_Name:** Low Value-Add Revenue Mix
**Category:** Profitability
**Description:** La empresa genera ingresos predominantemente de actividades de bajo valor agregado (intermediación, commodities, servicios básicos), limitando la rentabilidad estructural.
**Observable_Symptoms:** Márgenes bajos en toda la industria; competencia por precio feroz; dificultad para diferenciarse; clientes ven el producto como commodity.
**Early_Warning_Signals:** Margen bruto <20% estructural; imposibilidad de aumentar precios; todos los competidores tienen márgenes similares; baja inversión en I+D.
**Typical_Causes:** Modelo de negocio de intermediación o bajo valor agregado; falta de innovación; barreras de entrada bajas que commoditizan el mercado.
**Business_Impact:** Rentabilidad limitada estructuralmente; crecimiento requiere gran escala; vulnerabilidad a nuevos entrantes de bajo costo.
**Metrics_To_Check:** Margen bruto; Margen EBITDA; Valor agregado por empleado; % de ingresos de productos/servicios diferenciados.
**Diagnostic_Questions:** ¿Qué valor agregado real ofreces además del producto en sí? ¿Podrías moverte a un eslabón de mayor valor en la cadena?
**Recommended_Actions:** Agregar servicios de valor alrededor del producto commodity; migrar a nichos de mayor valor; invertir en diferenciación e innovación.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-025, FIN-027
---

## Indebtedness

### FIN-031
**Pattern_Name:** Debt Overhang (Liability Burden)
**Category:** Indebtedness
**Description:** La empresa tiene un nivel de deuda tan alto que cualquier inversión o mejora beneficia principalmente a los acreedores, desincentivando la inversión.
**Observable_Symptoms:** Dueño evitando nuevas inversiones aunque tengan buen retorno; toda la caja extra va a pagar deuda; falta de motivación para mejorar.
**Early_Warning_Signals:** Deuda Neta / EBITDA > 5x; Cobertura de intereses < 2x; dueño expresa frustración por trabajar para los bancos.
**Typical_Causes:** Deuda acumulada de años de pérdidas; compras apalancadas; inversiones fallidas; excesiva distribución de dividendos previa.
**Business_Impact:** Estancamiento estratégico; falta de inversión; pérdida de competitividad; eventual default por no poder innovar.
**Metrics_To_Check:** Deuda Neta / EBITDA; Cobertura de intereses; % de EBITDA destinado a servicio de deuda; ROIC vs costo de deuda.
**Diagnostic_Questions:** ¿Cuántos años de EBITDA necesitas para pagar toda tu deuda? ¿Te queda algo para reinvertir después de pagar deuda?
**Recommended_Actions:** Reestructuración de deuda (reducción de capital, extensión de plazos); considerar venta de activos no estratégicos; inyección de capital.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-012, FIN-042

### FIN-032
**Pattern_Name:** Excessive Short-Term Debt
**Category:** Indebtedness
**Description:** La empresa depende excesivamente de deuda de corto plazo para financiar operaciones y activos de largo plazo.
**Observable_Symptoms:** Constante renovación de créditos a 30-90 días; estrés antes de cada vencimiento; altos costos financieros por tasas de corto plazo.
**Early_Warning_Signals:** Deuda corto plazo > 50% de deuda total; deuda CP creciendo más que deuda LP; uso de sobregiros como financiamiento permanente.
**Typical_Causes:** Falta de acceso a crédito de largo plazo; mala estructuración financiera; crecimiento rápido no planificado.
**Business_Impact:** Alta vulnerabilidad a cambios de tasas; riesgo de refinanciamiento constante; costos financieros más altos que con deuda LP.
**Metrics_To_Check:** Deuda CP / Deuda Total; Deuda CP / EBITDA; Costo financiero promedio ponderado.
**Diagnostic_Questions:** ¿Qué % de tu deuda es de corto plazo? ¿Podrías convertir parte en deuda de largo plazo?
**Recommended_Actions:** Convertir deuda CP en LP; consolidar deudas; buscar financiamiento específico por activo (leasing, hipotecario).
**Severity_Level:** High
**Related_Patterns:** FIN-008, FIN-012, FIN-041

### FIN-033
**Pattern_Name:** Leverage Creep (Silent Debt Accumulation)
**Category:** Indebtedness
**Description:** La deuda aumenta gradualmente en cada período sin que la empresa lo note conscientemente, normalizando niveles de endeudamiento cada vez más altos.
**Observable_Symptoms:** Deuda total creciendo cada año; dueño se acostumbra a niveles de deuda crecientes; nueva deuda se toma para pagar gastos operativos.
**Early_Warning_Signals:** Deuda total creciendo año a año; ratio Deuda/Patrimonio aumentando gradualmente; nuevas líneas de crédito solicitadas sin análisis.
**Typical_Causes:** Gastos operativos crecientes no cubiertos por ingresos; capital de trabajo insuficiente; falta de monitoreo sistemático de endeudamiento.
**Business_Impact:** Normalización de niveles de riesgo crecientes; eventual sobreendeudamiento que se vuelve insostenible; default gradual.
**Metrics_To_Check:** Deuda Total / EBITDA; Deuda Total / Patrimonio; Tasa de crecimiento de deuda vs tasa de crecimiento de ingresos.
**Diagnostic_Questions:** ¿Tu deuda total es más alta que hace 2 años? ¿Sabes exactamente por qué aumentó? ¿Los nuevos créditos son para operación o para inversión?
**Recommended_Actions:** Establecer política de endeudamiento máximo (Deuda/EBITDA < 3x); monitorear mensualmente; planificar amortización de deuda.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-031, FIN-042

### FIN-034
**Pattern_Name:** Debt-Funded Distribution
**Category:** Indebtedness
**Description:** La empresa distribuye dividendos o retira capital mientras mantiene niveles de deuda elevados, descapitalizando el negocio.
**Observable_Symptoms:** Dueño retira utilidades mientras la empresa tiene deuda significativa; dividendos se pagan con nuevo endeudamiento; patrimonio neto no crece.
**Early_Warning_Signals:** Dividendos pagados > Utilidad Neta; Deuda aumentando mientras se distribuyen dividendos; patrimonio neto estable o decreciente con utilidades positivas.
**Typical_Causes:** Dueño prioriza su retorno sobre la salud financiera; falta de política de dividendos; presión personal del dueño por liquidez.
**Business_Impact:** Capital de trabajo insuficiente; necesidad de más deuda; empresa descapitalizada; riesgo de insolvencia.
**Metrics_To_Check:** Dividendos / Utilidad Neta; Dividendos / Flujo de Caja Libre; Deuda Neta / EBITDA vs política de dividendos.
**Diagnostic_Questions:** ¿Estás distribuyendo dividendos mientras la deuda crece? ¿Podrías reducir dividendos para fortalecer el balance?
**Recommended_Actions:** Establecer política de dividendos vinculada a niveles de deuda; retener utilidades hasta alcanzar estructura de capital saludable.
**Severity_Level:** High
**Related_Patterns:** FIN-011, FIN-031, FIN-042

### FIN-035
**Pattern_Name:** Foreign Currency Debt Exposure
**Category:** Indebtedness
**Description:** La empresa tiene deuda en moneda extranjera (USD, EUR) mientras sus ingresos son mayoritariamente en moneda local, generando riesgo cambiario.
**Observable_Symptoms:** Miedo a devaluaciones; impacto significativo en resultados por tipo de cambio; gastos financieros que varían sin explicación operativa.
**Early_Warning_Signals:** Deuda en USD > 30% de deuda total con ingresos 100% en moneda local; cobertura cambiaria inexistente; sensibilidad del EBITDA al tipo de cambio.
**Typical_Causes:** Tasas de interés más bajas en USD; créditos internacionales disponibles; falta de asesoría en gestión de riesgo cambiario.
**Business_Impact:** Devaluación puede duplicar la deuda en moneda local; resultados financieros volátiles; riesgo de insolvencia por shock cambiario.
**Metrics_To_Check:** Deuda en moneda extranjera / Deuda total; % de ingresos en moneda extranjera; Exposure cambiaria neta.
**Diagnostic_Questions:** ¿Tienes deuda en dólares y facturas en moneda local? ¿Qué pasa si tu moneda se devalúa 50%?
**Recommended_Actions:** Convertir deuda a moneda local o generar ingresos en la misma moneda de la deuda; contratar cobertura cambiaria (forwards, swaps).
**Severity_Level:** Critical
**Related_Patterns:** FIN-031, FIN-042, FIN-053

### FIN-036
**Pattern_Name:** Debt Maturity Concentration
**Category:** Indebtedness
**Description:** Toda la deuda vence en un período similar, creando un muro de refinanciamiento que pone presión extrema en la caja.
**Observable_Symptoms:** Picos de vencimientos en ciertos meses; estrés antes de fechas de pago concentradas; refinanciación apresurada.
**Early_Warning_Signals:** >40% de deuda con vencimiento en 12 meses; vencimientos no escalonados; falta de compromisos de refinanciamiento anticipados.
**Typical_Causes:** Créditos tomados simultáneamente; falta de planificación de perfil de vencimientos; financiamiento de corto plazo para proyectos largos.
**Business_Impact:** Riesgo de no poder refinanciar todo al mismo tiempo; poder de negociación reducido; posible default técnico.
**Metrics_To_Check:** Perfil de vencimientos por año; % de deuda que vence en 12 meses; Vencimientos concentrados en período < 3 meses.
**Diagnostic_Questions:** ¿Tienes vencimientos de deuda concentrados? ¿Qué pasa si no puedes refinanciar todo a la vez?
**Recommended_Actions:** Escalonar vencimientos; iniciar refinanciamiento con anticipación; diversificar fuentes de financiamiento.
**Severity_Level:** High
**Related_Patterns:** FIN-008, FIN-016, FIN-042

### FIN-037
**Pattern_Name:** Trade Credit Dependency
**Category:** Indebtedness
**Description:** La empresa financia sus operaciones principalmente mediante deuda comercial (proveedores), usando plazos extendidos como fuente de financiamiento.
**Observable_Symptoms:** Proveedores presionando por pago; plazos de pago extendidos más allá de lo normal; dependencia crítica de la paciencia de proveedores.
**Early_Warning_Signals:** Días de pago a proveedores > 90; cuentas por pagar creciendo más que compras; proveedores exigen pago anticipado o contado.
**Typical_Causes:** Falta de acceso a crédito bancario; capital de trabajo insuficiente; crecimiento no financiado; cultura de pagar tarde.
**Business_Impact:** Relaciones tensas con proveedores; riesgo de corte de suministro; costo implícito alto (descuentos perdidos, sobreprecios); reputación dañada.
**Metrics_To_Check:** Días de pago; Cuentas por pagar / Compras; % de proveedores que exigen pago anticipado; Costo implícito de financiamiento comercial.
**Diagnostic_Questions:** ¿Estás usando a tus proveedores como banco? ¿Cuánto te cuesta en descuentos perdidos y sobreprecios?
**Recommended_Actions:** Regularizar pagos a proveedores; obtener financiamiento bancario formal; negociar descuentos por pronto pago.
**Severity_Level:** High
**Related_Patterns:** FIN-001, FIN-031, FIN-041

### FIN-038
**Pattern_Name:** Debt Spiral (Paying Debt with More Debt)
**Category:** Indebtedness
**Description:** La empresa toma nueva deuda para pagar deuda existente, entrando en un ciclo de endeudamiento creciente sin resolver el problema subyacente.
**Observable_Symptoms:** Refinanciación constante de deudas vencidas; deuda total creciendo a pesar de pagos; nunca se reduce el capital.
**Early_Warning_Signals:** Cada nuevo crédito es para pagar uno anterior; deuda total aumenta o se mantiene sin reducir; gastos financieros creciendo.
**Typical_Causes:** EBITDA insuficiente para pagar deuda; falta de reestructuración real; negación del problema de insolvencia.
**Business_Impact:** Deuda crece exponencialmente por intereses; eventual colapso; pérdida de garantías y patrimonio personal.
**Metrics_To_Check:** Deuda neta / EBITDA tendencia; Préstamos nuevos para pagar deuda / Total préstamos nuevos; % de EBITDA destinado a intereses.
**Diagnostic_Questions:** ¿Estás pidiendo nuevos préstamos para pagar los anteriores? ¿Tu deuda total está bajando o subiendo?
**Recommended_Actions:** Detener la espiral: reestructuración integral; considerar concurso preventivo; inyección de capital; venta de activos.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-031, FIN-042

### FIN-039
**Pattern_Name:** Guarantee Depletion
**Category:** Indebtedness
**Description:** La empresa ha agotado su capacidad de otorgar garantías reales (hipotecas, prendas) para obtener crédito, limitando el acceso a financiamiento.
**Observable_Symptoms:** Bancos rechazan solicitudes de crédito por falta de garantías; dueño ofrece garantías personales cada vez más; activos libres de gravamen ya no existen.
**Early_Warning_Signals:** % de activos gravados > 70%; todas las propiedades hipotecadas; sin activos libres para nuevas garantías.
**Typical_Causes:** Endeudamiento excesivo previo; crecimiento financiado con deuda garantizada; falta de activos propios.
**Business_Impact:** Imposibilidad de obtener crédito nuevo; dependencia de fuentes informales o caras; restricción al crecimiento.
**Metrics_To_Check:** Activos gravados / Activos totales; % de propiedades hipotecadas; Capacidad de garantía remanente.
**Diagnostic_Questions:** ¿Qué activos libres de gravamen te quedan? ¿Podrías obtener un crédito nuevo si lo necesitaras?
**Recommended_Actions:** Liberar garantías mediante pago de deudas; buscar financiamiento no garantizado (factoring, leasing); mejorar perfil crediticio para crédito sin garantía.
**Severity_Level:** High
**Related_Patterns:** FIN-031, FIN-041, FIN-042

### FIN-040
**Pattern_Name:** Pyramid Debt Structure
**Category:** Indebtedness
**Description:** La empresa tiene una estructura de deuda piramidal (una deuda garantiza otra), creando riesgo sistémico de colapso.
**Observable_Symptoms:** Deudas cruzadas entre empresas del grupo; garantías en cadena; estructura societaria compleja para ocultar endeudamiento real.
**Early_Warning_Signals:** Deudas de empresas vinculadas con garantías de la operativa; consolidación de deuda de grupo no disponible; estructura de holding/deuda opaca.
**Typical_Causes:** Expansión mediante endeudamiento en múltiples vehículos; búsqueda de apalancamiento máximo; falta de transparencia financiera.
**Business_Impact:** Caída de una empresa arrastra a todo el grupo; riesgo sistémico; acreedores pueden ejecutar garantías cruzadas.
**Metrics_To_Check:** Deuda consolidada del grupo; Garantías entre empresas vinculadas; % de deuda con garantías cruzadas.
**Diagnostic_Questions:** ¿Tus empresas tienen deudas que se garantizan entre sí? ¿Si una empresa cae, arrastra a las demás?
**Recommended_Actions:** Simplificar estructura de deuda y garantías; desvincular financieramente las empresas del grupo; reducir endeudamiento consolidado.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-031, FIN-042
---

## Working Capital

### FIN-041
**Pattern_Name:** Working Capital Absorption by Growth
**Category:** Working Capital
**Description:** El crecimiento de ventas consume todo el efectivo disponible en forma de mayor capital de trabajo, generando paradoja de crecer y tener menos caja.
**Observable_Symptoms:** Cada nuevo cliente grande empeora la caja; necesidad de financiamiento para cubrir capital de trabajo; ventas suben, caja baja.
**Early_Warning_Signals:** Capital de trabajo creciendo más que ventas; CFO negativo en períodos de crecimiento; Días de cobro o inventario aumentando.
**Typical_Causes:** Ventas a crédito sin financiamiento; inventario necesario para crecer; proveedores no extienden plazos.
**Business_Impact:** Crecimiento no sostenible sin financiamiento; riesgo de iliquidez; necesidad de deuda o capital.
**Metrics_To_Check:** Capital de trabajo / Ventas; Variación de capital de trabajo / Variación de ventas; CFO.
**Diagnostic_Questions:** ¿Cuánto capital de trabajo adicional necesita cada  de crecimiento en ventas? ¿De dónde sacarás ese efectivo?
**Recommended_Actions:** Financiar crecimiento con deuda de largo plazo o capital; mejorar eficiencia de capital de trabajo (cobrar más rápido, menos inventario).
**Severity_Level:** Critical
**Related_Patterns:** FIN-001, FIN-003, FIN-042

### FIN-042
**Pattern_Name:** Receivables Aging Crisis
**Category:** Working Capital
**Description:** Las cuentas por cobrar están envejeciendo peligrosamente, con una porción creciente en mora severa (>90 días) que puede volverse incobrable.
**Observable_Symptoms:** Clientes que pagan cada vez más tarde; cuentas vencidas creciendo; equipo de cobranza desbordado; provisiones insuficientes.
**Early_Warning_Signals:** Días de cobro > 60 y aumentando; % de cuentas > 90 días > 15% del total; rotación de cuentas por cobrar decreciente.
**Typical_Causes:** Falta de política de crédito formal; clientes sin evaluación crediticia; cobranza reactiva en lugar de preventiva; ventas a clientes sin capacidad de pago.
**Business_Impact:** Capital de trabajo inmovilizado; necesidad de deuda para operar; pérdidas por incobrables; CFO negativo.
**Metrics_To_Check:** Días de cobro promedio; % de cuentas > 90 días; Rotación de cuentas por cobrar; Provisión de incobrables / Ventas.
**Diagnostic_Questions:** ¿Cuántos días tardan tus clientes en pagar en promedio? ¿Qué % de tus cuentas por cobrar tiene más de 90 días?
**Recommended_Actions:** Implementar política de crédito con límites y scoring; fortalecer cobranza preventiva (llamadas antes del vencimiento); ofrecer descuentos por pronto pago; factoring selectivo.
**Severity_Level:** Critical
**Related_Patterns:** FIN-001, FIN-002, FIN-041

### FIN-043
**Pattern_Name:** Obsolete Inventory Accumulation
**Category:** Working Capital
**Description:** La empresa acumula inventario de lenta rotación u obsoleto que consume capital de trabajo y espacio, además de deteriorarse.
**Observable_Symptoms:** Inventario que no se vende desde hace meses; bodegas llenas de productos que ya no se producen; necesidad de espacio adicional.
**Early_Warning_Signals:** Días de inventario > 90 y creciendo; rotación de inventario decreciente; % de inventario con más de 1 año sin movimiento.
**Typical_Causes:** Falta de gestión de inventario; compras por lote sin demanda confirmada; cambios de producto no comunicados a producción; sobreestimación de demanda.
**Business_Impact:** Capital de trabajo inmovilizado; costos de almacenamiento; riesgo de obsolescencia total; pérdidas por castigo de inventario.
**Metrics_To_Check:** Días de inventario; Rotación de inventario; % de inventario obsoleto; Castigo de inventario / Ventas.
**Diagnostic_Questions:** ¿Cuánto tiempo tarda en venderse tu inventario? ¿Qué % de tu inventario tiene más de 1 año sin moverse?
**Recommended_Actions:** Liquidar inventario obsoleto (descuentos, remates, donaciones); implementar sistema de gestión de inventario just-in-time; revisar política de compras.
**Severity_Level:** High
**Related_Patterns:** FIN-002, FIN-041, FIN-044

### FIN-044
**Pattern_Name:** Negative Operating Cycle
**Category:** Working Capital
**Description:** La empresa opera con ciclo operativo negativo (cobra antes de pagar), pero no lo gestiona para maximizar el beneficio de caja.
**Observable_Symptoms:** Caja positiva consistente; clientes pagan rápido, proveedores esperan; pero la empresa no invierte el excedente productivamente.
**Early_Warning_Signals:** CCC negativo; caja creciente no invertida; sin estrategia para el excedente de caja.
**Typical_Causes:** Modelo de negocio con ciclo negativo (retail, supermercados, algunos servicios); falta de cultura de inversión de excedentes.
**Business_Impact:** Oportunidad perdida de generar retorno sobre el excedente de caja; inflación erosiona el poder de compra de la caja.
**Metrics_To_Check:** CCC; Caja generada por ciclo operativo; Rentabilidad de caja excedente.
**Diagnostic_Questions:** ¿Cuánto efectivo genera tu ciclo operativo? ¿Estás invirtiendo ese excedente para que rinda?
**Recommended_Actions:** Invertir excedentes en instrumentos de corto plazo; usar el float para financiar crecimiento; optimizar aún más el ciclo.
**Severity_Level:** Medium
**Related_Patterns:** FIN-001, FIN-007, FIN-041

### FIN-045
**Pattern_Name:** Supplier Advance Payments
**Category:** Working Capital
**Description:** La empresa paga por adelantado a proveedores (por exigencia o costumbre), inmovilizando capital de trabajo innecesariamente.
**Observable_Symptoms:** Pagos anticipados a proveedores; falta de poder de negociación; capital de trabajo inmovilizado en anticipos.
**Early_Warning_Signals:** Anticipos a proveedores como % de compras > 20%; proveedores que exigen pago anticipado (por riesgo crediticio); días de anticipo creciendo.
**Typical_Causes:** Proveedores con poder de negociación; historial de pago irregular; importaciones que requieren anticipo; falta de alternativas de abastecimiento.
**Business_Impact:** Capital de trabajo inmovilizado; riesgo de pérdida si el proveedor no entrega; menor rentabilidad por costo de capital inmovilizado.
**Metrics_To_Check:** Anticipos a proveedores / Compras totales; Días de anticipo; Costo de capital inmovilizado en anticipos.
**Diagnostic_Questions:** ¿Estás pagando por adelantado a proveedores? ¿Podrías negociar plazos? ¿Sabes cuánto te cuesta ese anticipo?
**Recommended_Actions:** Negociar plazos con proveedores (aunque sea parcial); diversificar fuentes de abastecimiento; evaluar si el anticipo es realmente necesario.
**Severity_Level:** Medium
**Related_Patterns:** FIN-001, FIN-037, FIN-041

### FIN-046
**Pattern_Name:** Working Capital Efficiency Below Industry
**Category:** Working Capital
**Description:** La empresa utiliza más capital de trabajo por unidad de venta que el promedio de la industria, indicando ineficiencia en gestión de cobro, inventario o pago.
**Observable_Symptoms:** Capital de trabajo alto para el nivel de ventas; sensación de que el dinero está atado; comparación desfavorable con competidores.
**Early_Warning_Signals:** Capital de trabajo / Ventas > industry benchmark; Días de cobro, inventario o pago peores que el promedio; rentabilidad menor por inmovilización.
**Typical_Causes:** Procesos ineficientes; falta de tecnología; mala gestión de cobranza; inventario excesivo.
**Business_Impact:** Rentabilidad menor por costo de capital inmovilizado; menos efectivo disponible para crecer; desventaja competitiva.
**Metrics_To_Check:** Capital de trabajo / Ventas; Días de cobro, inventario y pago vs benchmark; Rotación de capital de trabajo.
**Diagnostic_Questions:** ¿Cómo se comparan tus días de cobro, inventario y pago con los de tu industria? ¿Dónde estás peor?
**Recommended_Actions:** Benchmarking con industria; implementar mejoras en el área peor rankeada (cobro, inventario o pago); establecer metas trimestrales de mejora.
**Severity_Level:** Medium
**Related_Patterns:** FIN-001, FIN-002, FIN-041

### FIN-047
**Pattern_Name:** Cash-to-Cash Cycle Variance
**Category:** Working Capital
**Description:** El ciclo de conversión de efectivo es extremadamente volátil de mes a mes, imposibilitando la planificación financiera.
**Observable_Symptoms:** Algunos meses sobra caja, otros falta; imposibilidad de proyectar; equipo financiero siempre apagando incendios.
**Early_Warning_Signals:** Desviación estándar del CCC > 30% del promedio mensual; cobros y pagos irregulares; picos de caja seguidos de valles profundos.
**Typical_Causes:** Clientes con pagos muy irregulares; estacionalidad extrema en ventas; proveedores con plazos variables; falta de programa de pagos fijos.
**Business_Impact:** Dificultad para planificar; necesidad de mantener colchón de caja excesivo; estrés financiero recurrente.
**Metrics_To_Check:** Desviación estándar del CCC; Rango de variación de caja mensual; Volatilidad de días de cobro.
**Diagnostic_Questions:** ¿Tu flujo de caja es predecible mes a mes? ¿Cuánta variación tiene tu ciclo de efectivo?
**Recommended_Actions:** Estabilizar cobros (cobranza programada, descuentos por pago puntual); estabilizar pagos (calendario fijo de pagos a proveedores); mantener colchón de liquidez.
**Severity_Level:** Medium
**Related_Patterns:** FIN-001, FIN-002, FIN-009

### FIN-048
**Pattern_Name:** Factoring Dependency Cycle
**Category:** Working Capital
**Description:** La empresa depende del factoring como fuente permanente de financiamiento, cediendo una parte significativa del margen en costos financieros.
**Observable_Symptoms:** Uso constante de factoring para operar; costo de factoring como % de ventas elevado; clientes notan que la empresa factoriza.
**Early_Warning_Signals:** Factoring > 30% de ventas; costo de factoring / Ventas > 3%; uso de factoring para gastos operativos recurrentes (no para crecimiento).
**Typical_Causes:** Capital de trabajo insuficiente; clientes que pagan tarde; falta de acceso a crédito bancario tradicional.
**Business_Impact:** Margen neto erosionado por costo financiero; dependencia de la línea de factoring; si el factor corta el servicio, crisis de liquidez.
**Metrics_To_Check:** Volumen de factoring / Ventas; Costo de factoring / Ventas; % de capital de trabajo financiado con factoring.
**Diagnostic_Questions:** ¿Estás usando factoring de forma permanente o solo puntual? ¿Cuánto de tu margen se va en costos de factoring?
**Recommended_Actions:** Reducir dependencia de factoring; mejorar cobranza para reducir necesidad; buscar financiamiento alternativo más barato (línea de crédito, descuento de cheques).
**Severity_Level:** High
**Related_Patterns:** FIN-001, FIN-003, FIN-042

### FIN-049
**Pattern_Name:** Intercompany Working Capital Drain
**Category:** Working Capital
**Description:** Empresas del mismo grupo se financian entre sí mediante cuentas corrientes mercantiles sin plazos ni interés, drenando capital de trabajo de la operativa.
**Observable_Symptoms:** Cuentas por cobrar a vinculadas creciendo sin cobro; empresa operativa financia a otras del grupo sin retorno; falta de política de precios de transferencia.
**Early_Warning_Signals:** Cuentas por cobrar a relacionadas > 20% del total; sin interés ni plazo definido; crecimiento de saldos intercompany no explicado.
**Typical_Causes:** Estructura de grupo sin gestión financiera consolidada; una empresa genera caja y otra la consume; falta de disciplina financiera entre relacionadas.
**Business_Impact:** La empresa rentable subsidia a las no rentables; capital de trabajo insuficiente en la operativa; riesgo de arrastre si las vinculadas caen.
**Metrics_To_Check:** Cuentas por cobrar intercompany / Ventas; % de capital de trabajo absorbido por relacionadas; Plazos y tasas intercompany.
**Diagnostic_Questions:** ¿Tu empresa operativa está financiando a otras empresas del grupo? ¿Ese financiamiento tiene retorno? ¿Está documentado?
**Recommended_Actions:** Formalizar préstamos intercompany con plazos e interés; limitar el financiamiento a vinculadas; consolidar tesorería del grupo.
**Severity_Level:** High
**Related_Patterns:** FIN-019, FIN-041, FIN-042

### FIN-050
**Pattern_Name:** Working Capital Cannibalization by CAPEX
**Category:** Working Capital
**Description:** La empresa utiliza capital de trabajo (caja operativa) para financiar inversiones de largo plazo (CAPEX), descapitalizando la operación.
**Observable_Symptoms:** Inversiones en maquinaria o infraestructura mientras la caja operativa se resiente; proveedores presionan por pago después de una inversión grande.
**Early_Warning_Signals:** CAPEX financiado con caja operativa; capital de trabajo decreciente después de inversiones; aumento de deuda de corto plazo post-inversión.
**Typical_Causes:** Falta de financiamiento de largo plazo para inversiones; decisión de no endeudarse; urgencia de la inversión; mala planificación financiera.
**Business_Impact:** Operación descapitalizada; riesgo de iliquidez post-inversión; imposibilidad de aprovechar la nueva capacidad instalada por falta de capital de trabajo.
**Metrics_To_Check:** CAPEX / CFO; CAPEX financiado con caja operativa / CAPEX total; Variación de capital de trabajo post-CAPEX.
**Diagnostic_Questions:** ¿Estás usando caja de la operación para comprar activos fijos? ¿Tienes suficiente capital de trabajo después de la inversión?
**Recommended_Actions:** Financiar CAPEX con deuda de largo plazo, leasing o capital; mantener capital de trabajo separado del presupuesto de inversiones.
**Severity_Level:** High
**Related_Patterns:** FIN-003, FIN-008, FIN-041
---

## Cost Structure

### FIN-051
**Pattern_Name:** Variable Cost Pass-Through Inability
**Category:** Cost Structure
**Description:** La empresa no puede trasladar aumentos de costos variables a sus precios, comprimiendo márgenes cuando los insumos suben.
**Observable_Symptoms:** Cuando sube el costo de materia prima, los márgenes se comprimen; competidores reaccionan antes; la empresa espera y sufre.
**Early_Warning_Signals:** Correlación entre aumento de costos y caída de margen; desfase entre ajuste de costos y ajuste de precios; quejas de clientes ante intentos de subir precios.
**Typical_Causes:** Contratos de venta sin cláusulas de ajuste; mercado competitivo que no permite subir precios; producto commodity sin diferenciación.
**Business_Impact:** Márgenes volátiles y tendencialmente decrecientes; empresa siempre reacciona tarde a la inflación; rentabilidad depende de factores externos.
**Metrics_To_Check:** Correlación costo variable / precio de venta; Tiempo de ajuste de precios vs cambio de costos; Elasticidad precio de la demanda.
**Diagnostic_Questions:** ¿Puedes subir tus precios cuando tus costos suben? ¿Cuánto tiempo te lleva ajustar?
**Recommended_Actions:** Incluir cláusulas de ajuste automático en contratos; reducir power de negociación de clientes (diferenciación); cubrirse con futuros o forwards de insumos.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-081

### FIN-052
**Pattern_Name:** High Labor Cost Ratio
**Category:** Cost Structure
**Description:** Los costos laborales (sueldos + cargas sociales) representan un porcentaje excesivo de los ingresos, limitando la rentabilidad.
**Observable_Symptoms:** Nómina consume la mayor parte del ingreso; cada aumento salarial impacta fuertemente; difícil cubrir gastos no laborales.
**Early_Warning_Signals:** Costos laborales / Ventas > 40% (según industria); crecimiento de nómina > crecimiento de ventas; productividad por empleado decreciente.
**Typical_Causes:** Exceso de personal; sueldos por encima del mercado; baja productividad; ingresos insuficientes para la dotación.
**Business_Impact:** Márgenes bajos; cualquier obligación laboral adicional (aumento, aguinaldo) genera estrés de caja; dificultad para invertir.
**Metrics_To_Check:** Costos laborales / Ventas; Costos laborales / Gastos operativos totales; Ingreso por empleado; Margen de contribución por empleado.
**Diagnostic_Questions:** ¿Cuánto de tus ingresos se va en sueldos y cargas? ¿Estás en línea con tu industria? ¿Podrías producir lo mismo con menos personas?
**Recommended_Actions:** Revisar dotación vs productividad; automatizar procesos donde sea posible; tercerizar funciones no críticas; implementar esquemas de compensación variable.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-024, FIN-056

### FIN-053
**Pattern_Name:** Financial Cost Overload
**Category:** Cost Structure
**Description:** Los gastos financieros (intereses, comisiones, diferencias de cambio) consumen una porción excesiva del EBITDA.
**Observable_Symptoms:** Una parte significativa del EBITDA se va en pagar intereses; la empresa trabaja para los bancos; poco queda para reinversión o utilidades.
**Early_Warning_Signals:** Gastos financieros / EBITDA > 30%; Cobertura de intereses < 3x; gastos financieros creciendo más que EBITDA.
**Typical_Causes:** Endeudamiento excesivo; altas tasas de interés; deuda en moneda extranjera con devaluación; comisiones bancarias elevadas.
**Business_Impact:** Rentabilidad neta baja o negativa; imposibilidad de reinvertir; exposición a suba de tasas; círculo vicioso de deuda.
**Metrics_To_Check:** Gastos financieros / EBITDA; Cobertura de intereses; Gastos financieros / Ventas; Costo financiero promedio.
**Diagnostic_Questions:** ¿Qué % de tu EBITDA se va en gastos financieros? ¿Te queda suficiente para reinvertir y crecer?
**Recommended_Actions:** Reducir deuda; reestructurar deuda a menor tasa; negociar comisiones bancarias; considerar fuentes de financiamiento alternativas.
**Severity_Level:** High
**Related_Patterns:** FIN-031, FIN-035, FIN-042

### FIN-054
**Pattern_Name:** Cost Structure Rigidity
**Category:** Cost Structure
**Description:** La mayoría de los costos son fijos, impidiendo a la empresa ajustarse rápidamente a caídas en la demanda.
**Observable_Symptoms:** Incapacidad para reducir costos cuando caen las ventas; pérdidas profundas en meses malos; dueño siente que los costos no responden.
**Early_Warning_Signals:** Costos fijos > 60% de costos totales; punto de equilibrio alto; alta palanca operativa.
**Typical_Causes:** Personal fijo excesivo; alquileres y arriendos rígidos; estructura administrativa sobredimensionada; compromisos contractuales de largo plazo.
**Business_Impact:** Pérdidas amplificadas en caídas de ventas; dificultad para sobrevivir crisis; quiebra en recesiones moderadas.
**Metrics_To_Check:** Costos fijos / Costos totales; Punto de equilibrio (% de capacidad); Apalancamiento operativo (DOL).
**Diagnostic_Questions:** ¿Si tus ventas caen 20%, cuánto puedes reducir tus costos? ¿Tus costos se ajustan automáticamente o son rígidos?
**Recommended_Actions:** Convertir costos fijos en variables (outsourcing, personal variable, comisiones); renegociar contratos fijos; mantener estructura lean.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-056, FIN-081

### FIN-055
**Pattern_Name:** Hidden Costs of Poor Quality
**Category:** Cost Structure
**Description:** Los costos de mala calidad (retrabajo, devoluciones, garantías, pérdida de clientes) no se miden ni gestionan, pero erosionan significativamente la rentabilidad.
**Observable_Symptoms:** Retrabajo constante; devoluciones frecuentes; garantías ejecutadas; clientes insatisfechos; equipo apagando incendios de calidad.
**Early_Warning_Signals:** Costo de retrabajo / Ventas > 5%; devoluciones creciendo; reclamos de garantía aumentando; quejas recurrentes de clientes.
**Typical_Causes:** Falta de control de calidad; procesos no estandarizados; capacitación insuficiente; presión por producción sin calidad.
**Business_Impact:** Costos más altos que competidores; clientes insatisfechos; reputación dañada; rentabilidad menor a la potencial.
**Metrics_To_Check:** Costo de calidad total (prevención + evaluación + fallas); % de retrabajo; % de devoluciones; Costo de garantías.
**Diagnostic_Questions:** ¿Cuánto gastas en arreglar problemas que podrías haber prevenido? ¿Mides el costo de la mala calidad?
**Recommended_Actions:** Implementar sistema de gestión de calidad; medir costos de calidad; invertir en prevención (capacitación, procesos, control).
**Severity_Level:** Medium
**Related_Patterns:** FIN-024, FIN-056, FIN-060

### FIN-056
**Pattern_Name:** Operating Gearing Mismatch
**Category:** Cost Structure
**Description:** La estructura de costos tiene un apalancamiento operativo alto (muchos costos fijos, pocos variables), magnificando el impacto de cambios en ventas.
**Observable_Symptoms:** Cualquier cambio en ventas se amplifica en utilidades; meses buenos son muy buenos, meses malos son muy malos; alta volatilidad de resultados.
**Early_Warning_Signals:** DOL (Degree of Operating Leverage) > 3x; Costos fijos altos vs variables; gran variabilidad en utilidades.
**Typical_Causes:** Alta automatización con costos fijos; modelo de negocio intensivo en capital; estructura administrativa fija grande.
**Business_Impact:** Alta volatilidad de resultados; riesgo en caídas de ventas; empresas con DOL alto requieren gestión de riesgo activa.
**Metrics_To_Check:** DOL = % cambio en EBIT / % cambio en Ventas; Costos fijos / Costos variables; Punto de equilibrio (%).
**Diagnostic_Questions:** ¿Qué tan sensible es tu utilidad a cambios en ventas? Si las ventas caen 10%, ¿cuánto caería tu utilidad?
**Recommended_Actions:** Reducir apalancamiento operativo (convertir costos fijos en variables); mantener reservas para períodos bajos; diversificar ingresos.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-054, FIN-101

### FIN-057
**Pattern_Name:** Cost of Customer Acquisition Escalation
**Category:** Cost Structure
**Description:** El costo de adquirir clientes (CAC) está creciendo más rápido que el valor que cada cliente genera (LTV), haciendo la ecuación unitaria insostenible.
**Observable_Symptoms:** Cada vez es más caro conseguir un cliente; equipo de marketing y ventas creciendo sin aumento proporcional de ingresos; clientes nuevos valen menos.
**Early_Warning_Signals:** CAC / LTV > 30%; CAC creciendo más que el ticket promedio; tiempo de recuperación de CAC > 12 meses; canales de adquisición más caros.
**Typical_Causes:** Saturación de canales; competencia pujando por palabras clave; producto con baja diferenciación que requiere más esfuerzo de venta; mercado maduro.
**Business_Impact:** Rentabilidad decreciente; inversión en marketing no recuperable; necesidad de más capital para crecer; empresa no sostenible.
**Metrics_To_Check:** CAC; LTV; LTV/CAC ratio; Tiempo de recuperación de CAC; CAC por canal.
**Diagnostic_Questions:** ¿Cuánto cuesta adquirir un cliente nuevo? ¿Cuánto te deja en toda su vida? ¿Estás gastando más de lo debido en adquirir?
**Recommended_Actions:** Optimizar canales de adquisición; aumentar LTV (upsell, retención, precio); enfocar en segmentos de menor CAC; mejorar tasa de conversión.
**Severity_Level:** Critical
**Related_Patterns:** FIN-021, FIN-027, FIN-127

### FIN-058
**Pattern_Name:** High Break-Even Capacity
**Category:** Cost Structure
**Description:** La empresa necesita operar a >80% de su capacidad instalada para alcanzar el punto de equilibrio, dejando muy poco margen ante caídas.
**Observable_Symptoms:** Meses con baja actividad generan pérdidas profundas; cualquier problema operativo lleva a pérdidas; la empresa necesita estar siempre a plena capacidad.
**Early_Warning_Signals:** Punto de equilibrio > 80% de capacidad; alta relación costos fijos / costos totales; pérdidas en meses de baja demanda estacional.
**Typical_Causes:** Alta inversión en capacidad fija; costos fijos elevados; baja contribución marginal; industria intensiva en capital.
**Business_Impact:** Alta vulnerabilidad a caídas de demanda; cualquier parada técnica genera pérdidas; necesidad de desesperada de mantener volumen.
**Metrics_To_Check:** Punto de equilibrio (% de capacidad); Margen de seguridad (ventas actuales - punto de equilibrio); Apalancamiento operativo.
**Diagnostic_Questions:** ¿Qué % de tu capacidad necesitas vender para no perder dinero? ¿Cuánto margen tienes antes de caer en pérdidas?
**Recommended_Actions:** Reducir punto de equilibrio (bajar costos fijos, aumentar margen de contribución); diversificar ingresos para niveles bajos de capacidad.
**Severity_Level:** Critical
**Related_Patterns:** FIN-022, FIN-054, FIN-056

### FIN-059
**Pattern_Name:** Cost Allocation Distortion
**Category:** Cost Structure
**Description:** La empresa asigna costos indirectos de forma incorrecta (por ejemplo, solo sobre ventas), distorsionando la rentabilidad real de productos y clientes.
**Observable_Symptoms:** Productos que parecen rentables pero el negocio total no; decisiones basadas en rentabilidad distorsionada; sorpresas al cierre del año.
**Early_Warning_Signals:** Método de costeo basado solo en ventas o horas; sin costeo por actividad (ABC); diferencias entre rentabilidad estimada y real.
**Typical_Causes:** Falta de sistema de costeo; contabilidad genérica; simplicidad excesiva en asignación de costos; falta de capacidad analítica.
**Business_Impact:** Decisiones sub-óptimas sobre precios, mix y clientes; recursos asignados a productos que parecen rentables pero no lo son.
**Metrics_To_Check:** Método de costeo usado; Diferencia entre costeo tradicional y ABC; % de costos indirectos sobre costos totales.
**Diagnostic_Questions:** ¿Sabes cuánto le cuesta realmente a tu empresa producir cada producto o atender cada cliente? ¿Tu sistema de costos refleja la realidad?
**Recommended_Actions:** Implementar costeo basado en actividades (ABC); revisar asignación de costos indirectos periódicamente; capacitar al equipo en costos.
**Severity_Level:** Medium
**Related_Patterns:** FIN-024, FIN-025, FIN-061

### FIN-060
**Pattern_Name:** Input Price Volatility Exposure
**Category:** Cost Structure
**Description:** La empresa está expuesta a insumos con alta volatilidad de precio (commodities, energía, importados) sin mecanismos de cobertura.
**Observable_Symptoms:** Costos que varían fuertemente mes a mes; márgenes impredecibles; imposibilidad de presupuestar con precisión.
**Early_Warning_Signals:** Insumos con coeficiente de variación de precio > 20%; sin contratos de cobertura; insumos importados sin cobertura cambiaria; dependencia de pocos proveedores.
**Typical_Causes:** Materias primas commodities; energía como insumo significativo; importaciones sin cobertura; falta de cultura de cobertura.
**Business_Impact:** Rentabilidad volátil; presupuesto poco confiable; riesgo de márgenes negativos en picos de precios; dificultad para planificar.
**Metrics_To_Check:** % de costos en insumos volátiles; Coeficiente de variación de precio de insumos clave; % de cobertura contratada.
**Diagnostic_Questions:** ¿Qué insumos de tu negocio tienen precios muy volátiles? ¿Tienes algún mecanismo para cubrirte de esas fluctuaciones?
**Recommended_Actions:** Identificar insumos críticos volátiles; contratar coberturas (futuros, forwards, opciones); diversificar fuentes de abastecimiento; trasladar volatilidad a precios (cláusulas de ajuste).
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-051, FIN-053
---

## EBITDA

### FIN-061
**Pattern_Name:** EBITDA Add-Backs Distortion
**Category:** EBITDA
**Description:** La empresa reporta un EBITDA inflado mediante la inclusión de add-backs no recurrentes o no operativos que disfrazan la verdadera generación de caja operativa.
**Observable_Symptoms:** EBITDA reportado muy superior al EBITDA operativo real; ajustes recurrentes cada año; dueño presenta EBITDA optimista para venta o crédito.
**Early_Warning_Signals:** Add-backs > 15% del EBITDA reportado; ajustes por gastos personales del dueño; normalizaciones de gastos no recurrentes que sí se repiten.
**Typical_Causes:** Deseo de mostrar mejor resultado (para venta, crédito o inversores); falta de estándar en cálculo de EBITDA; inclusión de gastos personales como operativos.
**Business_Impact:** Decisiones basadas en EBITDA inflado; adquisiciones o créditos basados en números incorrectos; sorpresa cuando la caja real no acompaña.
**Metrics_To_Check:** EBITDA reportado vs EBITDA ajustado; Add-backs / EBITDA; EBITDA normalizado vs CFO; consistencia de add-backs año a año.
**Diagnostic_Questions:** ¿Tu EBITDA refleja la generación real de caja operativa? ¿Qué ajustes le estás haciendo? ¿Se repiten esos ajustes cada año?
**Recommended_Actions:** Reportar EBITDA con y sin ajustes; auditar add-backs; alinear EBITDA reportado con CFO; eliminar gastos personales de la empresa.
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-028, FIN-056

### FIN-062
**Pattern_Name:** EBITDA Margin Decline Trend
**Category:** EBITDA
**Description:** El margen EBITDA muestra una tendencia decreciente consistente durante 2-3 años, señal de deterioro competitivo o estructural.
**Observable_Symptoms:** Cada año el margen es un poco menor; dueño nota que rinde menos; inversiones no mejoran la rentabilidad.
**Early_Warning_Signals:** Margen EBITDA cayendo >0.5% anual por 3+ años; EBITDA creciendo menos que ingresos; gastos operativos creciendo más que ventas.
**Typical_Causes:** Aumento de costos no trasladado; presión competitiva en precios; mix de productos de menor margen; ineficiencias acumuladas.
**Business_Impact:** Menor valor de empresa (múltiplo EBITDA menor); menos caja para invertir; vulnerabilidad creciente; eventual pérdida operativa.
**Metrics_To_Check:** Margen EBITDA histórico (5 años); EBITDA / Ventas; Benchmark vs industria; Tendencia de gastos operativos / Ventas.
**Diagnostic_Questions:** ¿Tu margen EBITDA ha mejorado, empeorado o se ha mantenido en los últimos 3 años? ¿Sabes por qué?
**Recommended_Actions:** Diagnosticar causas del deterioro; implementar programa de recuperación de margen; revisar pricing, costos y mix.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-027, FIN-056

### FIN-063
**Pattern_Name:** EBITDA to CFO Divergence
**Category:** EBITDA
**Description:** Existe una brecha creciente y persistente entre el EBITDA y el flujo de caja operativo (CFO), indicando que las utilidades no se convierten en efectivo.
**Observable_Symptoms:** EBITDA positivo pero caja ajustada; empresa genera utilidad contable pero no efectivo; dueño no entiende por qué no hay dinero.
**Early_Warning_Signals:** CFO / EBITDA < 70% sostenidamente; brecha creciente entre EBITDA y CFO; crecimiento de capital de trabajo superior al crecimiento de ventas.
**Typical_Causes:** Crecimiento de cuentas por cobrar no financiado; acumulación de inventario; pago acelerado a proveedores; partidas no monetarias significativas.
**Business_Impact:** EBITDA no representa la generación de caja real; decisiones de inversión basadas en EBITDA pueden ser peligrosas; riesgo de iliquidez.
**Metrics_To_Check:** CFO / EBITDA; CFO / Utilidad Neta; Variación de capital de trabajo / EBITDA; Calidad del EBITDA.
**Diagnostic_Questions:** ¿Tu EBITDA se convierte en efectivo? ¿Qué % de tu EBITDA realmente llega a tu cuenta bancaria?
**Recommended_Actions:** Mejorar conversión de EBITDA a CFO (gestionar capital de trabajo); reportar EBITDA junto con CFO; investigar causas de la divergencia.
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-041, FIN-056

### FIN-064
**Pattern_Name:** EBITDA Not Covering Maintenance CAPEX
**Category:** EBITDA
**Description:** La empresa reporta EBITDA positivo pero no genera suficiente caja para cubrir el CAPEX de mantenimiento, consumiendo su base de activos.
**Observable_Symptoms:** Equipos envejecidos sin reemplazo; mantenimiento diferido; planta cada vez más obsoleta; necesidad creciente de reparaciones.
**Early_Warning_Signals:** CAPEX de mantenimiento / EBITDA > 50%; Depreciación > EBITDA; CAPEX < Depreciación por varios años; mantenimiento diferido acumulado.
**Typical_Causes:** EBITDA insuficiente; priorización de otros usos de caja; falta de conciencia sobre deterioro de activos; negación del deterioro.
**Business_Impact:** Pérdida de competitividad por activos obsoletos; averías y paradas de producción; accidentes laborales; eventual cierre por activos inservibles.
**Metrics_To_Check:** CAPEX de mantenimiento / EBITDA; CAPEX total / Depreciación; Edad promedio de activos fijos; Mantenimiento diferido estimado.
**Diagnostic_Questions:** ¿Tu EBITDA es suficiente para mantener tus activos en buen estado? ¿Estás invirtiendo lo necesario en mantenimiento y reposición?
**Recommended_Actions:** Presupuestar CAPEX de mantenimiento como gasto prioritario; calcular EBITDA después de CAPEX de mantenimiento (EBITDA - Maintenance CAPEX); planificar reposición de activos.
**Severity_Level:** Critical
**Related_Patterns:** FIN-006, FIN-056, FIN-071

### FIN-065
**Pattern_Name:** EBITDA Masking Interest Burden
**Category:** EBITDA
**Description:** La empresa tiene un EBITDA aparentemente saludable pero los intereses consumen la mayor parte, dejando poco para capex, deuda y utilidades.
**Observable_Symptoms:** EBITDA positivo pero utilidad neta baja o negativa; altos gastos financieros; dueño dice la empresa trabaja para los bancos.
**Early_Warning_Signals:** Cobertura de intereses < 2x; Gastos financieros / EBITDA > 40%; Utilidad neta significativamente menor que EBITDA.
**Typical_Causes:** Alto endeudamiento; altas tasas de interés; deuda en moneda extranjera; apalancamiento excesivo.
**Business_Impact:** EBITDA no refleja la rentabilidad disponible para el accionista; empresa no genera valor; imposibilidad de reinvertir.
**Metrics_To_Check:** Cobertura de intereses; Gastos financieros / EBITDA; EBITDA - Intereses; Deuda Neta / EBITDA.
**Diagnostic_Questions:** ¿Cuánto de tu EBITDA se va en intereses? ¿Te queda suficiente después de pagar deuda para crecer y distribuir?
**Recommended_Actions:** Reducir deuda para liberar EBITDA; reestructurar deuda a menor tasa; considerar si el negocio genera suficiente retorno sobre el capital invertido.
**Severity_Level:** High
**Related_Patterns:** FIN-012, FIN-031, FIN-053

### FIN-066
**Pattern_Name:** EBITDA Distortion by Lease Classification
**Category:** EBITDA
**Description:** La clasificación de arrendamientos (operativo vs financiero) distorsiona el EBITDA, haciendo que empresas con muchos arriendos operativos parezcan más rentables.
**Observable_Symptoms:** Empresa con muchos arriendos muestra EBITDA alto; al analizar el flujo de caja real, la historia es diferente; comparación con competidores es engañosa.
**Early_Warning_Signals:** Arriendos operativos significativos; diferencia entre EBITDA y EBITDAR; empresas comparables con diferente clasificación de arriendos.
**Typical_Causes:** Preferencia contable por arriendos operativos; falta de ajuste al comparar EBITDA; desconocimiento del impacto de IFRS 16.
**Business_Impact:** EBITDA no comparable entre empresas; decisiones basadas en EBITDA sobrestimado; valoración incorrecta de la empresa.
**Metrics_To_Check:** Arriendos operativos / EBITDA; EBITDAR (EBITDA + Arriendos); Diferencia entre EBITDA pre y post IFRS 16.
**Diagnostic_Questions:** ¿Tu EBITDA incluye beneficios de arrendamientos operativos? ¿Al compararte con competidores ajustas por diferencias de arrendamiento?
**Recommended_Actions:** Reportar EBITDAR junto con EBITDA; ajustar EBITDA por arriendos al comparar; considerar impacto de IFRS 16 en análisis.
**Severity_Level:** Medium
**Related_Patterns:** FIN-056, FIN-061, FIN-064

### FIN-067
**Pattern_Name:** EBITDA Not Covering Working Capital Needs
**Category:** EBITDA
**Description:** Aunque el EBITDA es positivo, las necesidades de capital de trabajo son tan altas que consumen todo el EBITDA generado.
**Observable_Symptoms:** EBITDA positivo pero caja no crece; necesidad constante de financiamiento; cada ciclo de venta consume efectivo.
**Early_Warning_Signals:** Variación de capital de trabajo / EBITDA > 50%; CFO < EBITDA consistentemente; CCC largo y creciente.
**Typical_Causes:** Crecimiento rápido no financiado; cobros muy lentos; inventarios elevados; pagos rápidos a proveedores.
**Business_Impact:** EBITDA es una métrica engañosa para este negocio; la empresa no genera efectivo libre; crecimiento consume caja.
**Metrics_To_Check:** EBITDA - Variación de capital de trabajo; CFO; EBITDA / Capital de trabajo invertido.
**Diagnostic_Questions:** ¿Cuánto de tu EBITDA se consume en capital de trabajo? ¿Qué queda después de financiar la operación?
**Recommended_Actions:** Medir EBITDA después de capital de trabajo; reducir necesidades de capital de trabajo; financiar capital de trabajo con deuda de LP.
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-041, FIN-063

### FIN-068
**Pattern_Name:** EBITDA Multiple Valuation Trap
**Category:** EBITDA
**Description:** El dueño valora su empresa basado en múltiplos EBITDA de mercado sin considerar que su EBITDA no es representativo (bajo margen, alta deuda, bajo crecimiento).
**Observable_Symptoms:** Dueño dice mi empresa vale X por EBITDA; al intentar vender, las ofertas son muy inferiores; frustración en procesos de venta.
**Early_Warning_Signals:** Margen EBITDA bajo (<10%); alto endeudamiento (Deuda/EBITDA > 4x); crecimiento bajo o negativo; concentración de clientes.
**Typical_Causes:** Desconocimiento de valoración; sobrevaloración del negocio; falta de asesoría profesional en venta.
**Business_Impact:** Incapacidad de vender la empresa al precio esperado; procesos de venta fallidos; frustración del dueño.
**Metrics_To_Check:** Múltiplo EBITDA implícito; EBITDA ajustado vs reportado; Deuda neta / EBITDA; Crecimiento histórico y proyectado.
**Diagnostic_Questions:** ¿Tu EBITDA es representativo de tu generación de caja sostenible? ¿Ajustaste por gastos personales, one-offs y capital de trabajo?
**Recommended_Actions:** Calcular EBITDA normalizado y sostenible; ajustar por gastos personales y no recurrentes; preparar la empresa para venta con anticipación.
**Severity_Level:** Medium
**Related_Patterns:** FIN-061, FIN-062, FIN-064

### FIN-069
**Pattern_Name:** EBITDA Positive, Negative Net Income
**Category:** EBITDA
**Description:** La empresa consistentemente reporta EBITDA positivo pero utilidad neta negativa, indicando que la depreciación, intereses o impuestos consumen toda la rentabilidad.
**Observable_Symptoms:** EBITDA positivo cada año pero pérdida neta; dueño destaca EBITDA como señal de salud; pero el negocio no genera ganancia real.
**Early_Warning_Signals:** Utilidad neta negativa por >2 años con EBITDA positivo; depreciación e intereses elevados; diferencia significativa entre EBITDA y utilidad neta.
**Typical_Causes:** Alta depreciación (industria intensiva en capital); alto endeudamiento con intereses elevados; estructura impositiva desfavorable.
**Business_Impact:** Empresa no genera valor para accionistas; no hay retorno sobre la inversión; insostenible a largo plazo (activos se deprecian y no se reponen).
**Metrics_To_Check:** EBITDA vs Utilidad Neta; Depreciación / EBITDA; Intereses / EBITDA; Tasa impositiva efectiva.
**Diagnostic_Questions:** ¿Tu empresa genera ganancia neta o solo EBITDA? ¿La depreciación e intereses consumen toda la rentabilidad operativa?
**Recommended_Actions:** Reducir deuda; optimizar estructura de capital; revisar política de inversiones (activos que no generan retorno); planificación fiscal.
**Severity_Level:** High
**Related_Patterns:** FIN-028, FIN-053, FIN-064

### FIN-070
**Pattern_Name:** EBITDA Growth Without Cash Generation
**Category:** EBITDA
**Description:** El EBITDA crece año a año pero la caja no aumenta, indicando que el crecimiento del EBITDA se basa en partidas no monetarias o se consume en capital de trabajo.
**Observable_Symptoms:** EBITDA subiendo pero caja estable o bajando; dueño no ve el efectivo del EBITDA; frustración con el desempeño financiero.
**Early_Warning_Signals:** EBITDA creciendo >10% anual pero caja plana; CFO / EBITDA decreciente; CAPEX o capital de trabajo consumiendo el crecimiento.
**Typical_Causes:** Crecimiento basado en ventas a crédito; acumulación de inventario; CAPEX excesivo para sostener crecimiento; partidas no monetarias creciendo.
**Business_Impact:** Crecimiento ilusorio; empresa vale menos de lo que sugiere el EBITDA; riesgo de iliquidez.
**Metrics_To_Check:** Caja vs EBITDA tendencia; CFO / EBITDA; CAPEX / EBITDA; Variación de capital de trabajo vs crecimiento EBITDA.
**Diagnostic_Questions:** ¿El crecimiento de tu EBITDA se refleja en tu cuenta bancaria? ¿A dónde se fue el efectivo del EBITDA adicional?
**Recommended_Actions:** Vincular compensación a CFO en lugar de EBITDA; mejorar calidad del EBITDA; gestionar capital de trabajo proporcionalmente al crecimiento.
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-063, FIN-067
---

## Margins

### FIN-071
**Pattern_Name:** Gross Margin Erosion by Input Costs
**Category:** Margins
**Description:** El margen bruto se reduce consistentemente porque los costos de insumos suben mas rapido que los precios de venta.
**Observable_Symptoms:** Margen bruto bajando ano a ano; materia prima mas cara; incapacidad de trasladar a precios.
**Early_Warning_Signals:** Margen bruto decreciente por >2 anos; costo de ventas como % de ingresos aumentando.
**Typical_Causes:** Dependencia de insumos commodities; poder de negociacion de proveedores; mercado competitivo.
**Business_Impact:** Rentabilidad estructuralmente decreciente; necesidad de aumentar volumen; eventual perdida operativa.
**Metrics_To_Check:** Margen bruto; Costo de ventas / Ventas; Inflacion de insumos vs ajuste de precios.
**Diagnostic_Questions:** Tu margen bruto es estable o esta cayendo? Puedes identificar que insumos presionan el margen?
**Recommended_Actions:** Buscar proveedores alternativos; redisenar producto; aumentar precios selectivamente.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-051, FIN-081
---

## Margins

### FIN-071
**Pattern_Name:** Gross Margin Erosion by Input Costs
**Category:** Margins
**Description:** El margen bruto se reduce porque los costos de insumos suben mas rapido que los precios de venta.
**Observable_Symptoms:** Margen bruto bajando; materia prima mas cara; incapacidad de trasladar a precios.
**Early_Warning_Signals:** Margen bruto decreciente por >2 anos; costo de ventas como % de ingresos aumentando.
**Typical_Causes:** Dependencia de insumos commodities; poder de proveedores; mercado competitivo.
**Business_Impact:** Rentabilidad estructuralmente decreciente; eventual perdida operativa.
**Metrics_To_Check:** Margen bruto; Costo de ventas / Ventas; Inflacion insumos vs ajuste precios.
**Diagnostic_Questions:** Tu margen bruto es estable o esta cayendo? Que insumos presionan el margen?
**Recommended_Actions:** Buscar proveedores alternativos; redisenar producto; aumentar precios.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-051, FIN-081

### FIN-072
**Pattern_Name:** Operating Margin Below Cost of Capital
**Category:** Margins
**Description:** El margen operativo (EBIT / Ventas) es inferior al WACC, indicando que la empresa destruye valor.
**Observable_Symptoms:** Empresa rentable contablemente pero no alcanza el costo de capital; dueño conforme con rentabilidad que en realidad es insuficiente.
**Early_Warning_Signals:** ROIC < WACC por varios anos; margen operativo inferior al costo de deuda; inversionistas no interesados.
**Typical_Causes:** Baja rentabilidad estructural; uso ineficiente de capital; exceso de activos; costo de capital alto.
**Business_Impact:** Empresa destruye valor aunque tenga utilidad contable; imposibilidad de atraer inversion; perdida de patrimonio real.
**Metrics_To_Check:** ROIC vs WACC; Margen operativo; EVA (Economic Value Added); Retorno sobre activos netos.
**Diagnostic_Questions:** Tu empresa genera mas de lo que cuesta el capital invertido? El retorno supera el costo de financiamiento?
**Recommended_Actions:** Mejorar eficiencia operativa; reducir base de activos; desinvertir en negocios con ROIC < WACC.
**Severity_Level:** Critical
**Related_Patterns:** FIN-056, FIN-071, FIN-101

### FIN-073
**Pattern_Name:** Net Margin Below Industry Average
**Category:** Margins
**Description:** El margen neto es consistentemente inferior al promedio de la industria.
**Observable_Symptoms:** Dueño nota que rinde menos que competidores similares; comparaciones desfavorables; dificultad para crecer.
**Early_Warning_Signals:** Margen neto < 50% del promedio de industria; margen neto decreciente mientras industria se mantiene.
**Typical_Causes:** Estructura de costos mas pesada; menor poder de fijacion de precios; ineficiencias operativas.
**Business_Impact:** Menor generacion de caja; menos capacidad de inversion; empresa menos valiosa.
**Metrics_To_Check:** Margen neto; Margen neto vs benchmark industria; Comparacion de estructura de costos.
**Diagnostic_Questions:** Como se compara tu margen neto con el de tu industria? Estas en el promedio, arriba o abajo?
**Recommended_Actions:** Benchmarking de costos y margenes; identificar brechas con la industria; implementar mejoras focalizadas.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-062

### FIN-074
**Pattern_Name:** Contribution Margin Below Variable Cost Threshold
**Category:** Margins
**Description:** El margen de contribucion (precio - costo variable) es insuficiente para cubrir los costos fijos al nivel actual de ventas.
**Observable_Symptoms:** Cada vez que bajan las ventas, se generan perdidas rapidamente; punto de equilibrio alto.
**Early_Warning_Signals:** Margen de contribucion unitario bajo; costos fijos altos en relacion al margen; punto de equilibrio > 70% de capacidad.
**Typical_Causes:** Precios bajos por competencia; costos variables altos; estructura de costos fijos pesada.
**Business_Impact:** Alta sensibilidad a cambios en ventas; cualquier caida genera perdidas; crecimiento requiere mucho volumen.
**Metrics_To_Check:** Margen de contribucion unitario; Relacion de contribucion (MC / Precio); Punto de equilibrio.
**Diagnostic_Questions:** Cuanto margen de contribucion te queda despues de los costos variables? Alcanza para cubrir los costos fijos?
**Recommended_Actions:** Aumentar margen de contribucion (subir precios, bajar costos variables); reducir costos fijos; aumentar volumen.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-054, FIN-081

### FIN-075
**Pattern_Name:** Price Erosion from Discounting
**Category:** Margins
**Description:** La empresa concede descuentos excesivos que erosionan el margen sin generar el volumen adicional necesario para compensar.
**Observable_Symptoms:** Descuentos frecuentes y significativos; clientes entrenados para esperar descuento; margen neto menor al esperado.
**Early_Warning_Signals:** Descuentos promedio > 10% de precio de lista; % de ventas con descuento > 50%; margen neto cayendo a pesar de volumen estable.
**Typical_Causes:** Presion de la competencia; cultura de descuentos; equipo de ventas sin control; falta de disciplina de precios.
**Business_Impact:** Margen menor; clientes devaluan el producto; dificultad para subir precios despues; guerra de precios.
**Metrics_To_Check:** Descuento promedio; % de ventas con descuento; Elasticidad precio de la demanda; Margen neto vs margen de lista.
**Diagnostic_Questions:** Que % de tus ventas tiene descuento? Realmente necesitas descontar para vender o es costumbre?
**Recommended_Actions:** Reducir frecuencia y profundidad de descuentos; empoderar a ventas con criterios de descuento; comunicar valor en lugar de precio.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-057, FIN-081

### FIN-076
**Pattern_Name:** Margin Recovery Failure After Crisis
**Category:** Margins
**Description:** La empresa redujo precios o aumento descuentos durante una crisis y no logro recuperar los margenes anteriores.
**Observable_Symptoms:** Margenes mas bajos que antes de la crisis; precios no volvieron a niveles originales; clientes resisten aumentos.
**Early_Warning_Signals:** Margen post-crisis no recupera nivel pre-crisis en >12 meses; clientes con precio congelado; descuentos de crisis se volvieron permanentes.
**Typical_Causes:** Clientes se acostumbraron a precios bajos; falta de estrategia de recuperacion; debilidad en negociacion.
**Business_Impact:** Rentabilidad permanentemente mas baja; perdida de valor de la empresa; dificultad para cubrir costos crecientes.
**Metrics_To_Check:** Margen actual vs margen pre-crisis; Tiempo desde inicio de crisis; % de clientes con precio reducido aun vigente.
**Diagnostic_Questions:** Tus margenes volvieron a los niveles previos a la ultima crisis? O los precios bajos se quedaron?
**Recommended_Actions:** Implementar plan de recuperacion de margenes; aumentar precio gradualmente; segmentar clientes para ajustes diferenciados.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-023, FIN-075

### FIN-077
**Pattern_Name:** Mix Shift Toward Low-Margin Products
**Category:** Margins
**Description:** Cambio en la mezcla de ventas hacia productos/servicios de menor margen, reduciendo el margen agregado.
**Observable_Symptoms:** Mismos ingresos pero menor ganancia; equipo vendiendo productos faciles (bajo margen); clientes comprando mas basico.
**Early_Warning_Signals:** Margen bruto total cayendo con ingresos estables; productos de alto margen pierden participacion; margen promedio ponderado decreciente.
**Typical_Causes:** Incentivos comerciales basados en volumen no en margen; entrada de competidores en segmento premium; cambio en preferencias de clientes.
**Business_Impact:** Rentabilidad decreciente a pesar de ventas estables; empresa trabaja mas por menos; erosion silenciosa de margen.
**Metrics_To_Check:** Margen ponderado; % de ventas de alto margen; Margen por canal/segmento.
**Diagnostic_Questions:** Esta cambiando la mezcla de productos hacia los de menor margen? Tus incentivos promueven margen o solo volumen?
**Recommended_Actions:** Alinear incentivos a margen; revitalizar productos de alto margen; considerar eliminar productos de bajo margen.
**Severity_Level:** High
**Related_Patterns:** FIN-025, FIN-071, FIN-081

### FIN-078
**Pattern_Name:** Margin Transparency Absence
**Category:** Margins
**Description:** La empresa no conoce el margen por producto, cliente o canal, gestionando la rentabilidad a ciegas.
**Observable_Symptoms:** Precios fijados por intuicion; no saben que productos son mas rentables; decisiones sin datos de margen.
**Early_Warning_Signals:** Falta de sistema de costeo por producto; margen solo se calcula agregado; precios basados en competencia o costo mas margen general.
**Typical_Causes:** Falta de sofisticacion financiera; ERP basico; cultura de gestion por ingresos no por margen.
**Business_Impact:** Decisiones suboptimas; productos no rentables no identificados; oportunidades de mejora de margen perdidas.
**Metrics_To_Check:** Existencia de margen por producto/cliente; Frecuencia de calculo de margen; Precision del sistema de costeo.
**Diagnostic_Questions:** Sabes el margen de cada producto que vendes? De cada cliente? De cada canal?
**Recommended_Actions:** Implementar sistema de costeo por producto; calcular margen por cliente y canal; revisar precios basado en datos de margen.
**Severity_Level:** High
**Related_Patterns:** FIN-059, FIN-061, FIN-081

### FIN-079
**Pattern_Name:** Gross Margin Expansion Without Net Margin
**Category:** Margins
**Description:** El margen bruto mejora pero el margen neto no, indicando que los gastos operativos crecen mas que la mejora del margen bruto.
**Observable_Symptoms:** Margen bruto subiendo pero utilidad neta estable o cayendo; eficiencia productiva que se pierde en estructura.
**Early_Warning_Signals:** Margen bruto mejorando, margen neto plano; SG&A creciendo mas que la mejora del margen bruto; beneficios de produccion consumidos por administracion.
**Typical_Causes:** Costos de estructura descontrolados; crecimiento de gastos de ventas; ineficiencias administrativas que absorben la mejora productiva.
**Business_Impact:** Esfuerzo en produccion no se refleja en resultado final; frustracion; perdida de oportunidad de mejorar rentabilidad real.
**Metrics_To_Check:** Margen bruto vs margen neto; SG&A / Ventas; Correlacion entre margen bruto y neto.
**Diagnostic_Questions:** La mejora en margen bruto se traduce en mayor utilidad neta? O se pierde en gastos operativos?
**Recommended_Actions:** Controlar gastos SG&A; vincular mejora de margen bruto a resultado neto; establecer metas de margen neto.
**Severity_Level:** Medium
**Related_Patterns:** FIN-024, FIN-029, FIN-056

### FIN-080
**Pattern_Name:** Margin Compression from Regulatory Costs
**Category:** Margins
**Description:** Nuevos costos regulatorios, impositivos o de compliance estan comprimiendo los margenes sin posibilidad de traslado a precios.
**Observable_Symptoms:** Nuevos impuestos o tasas; costos de compliance creciendo; margenes cayendo por factores externos no controlables.
**Early_Warning_Signals:** Nueva regulacion con costo significativo; margen cayendo en toda la industria por igual; capacidad limitada de trasladar a precios.
**Typical_Causes:** Cambios tributarios; nuevas regulaciones laborales o ambientales; mayores costos de formalizacion.
**Business_Impact:** Rentabilidad estructuralmente mas baja; desventaja frente a competidores informales; erosion progresiva.
**Metrics_To_Check:** Costos regulatorios / Ventas; Impacto de nueva regulacion en margen neto; Comparacion con industria.
**Diagnostic_Questions:** Nuevas regulaciones estan afectando tus margenes? Puedes trasladar esos costos a precios?
**Recommended_Actions:** Buscar eficiencias que compensen; evaluar alternativas para mitigar impacto (regimenes promocionales, reestructuracion); participar en discussion regulatoria.
**Severity_Level:** Medium
**Related_Patterns:** FIN-023, FIN-051, FIN-071
---

## ROA

### FIN-081
**Pattern_Name:** ROA Below Cost of Debt
**Category:** ROA
**Description:** El retorno sobre activos (ROA) es inferior al costo de la deuda, indicando que la empresa no genera suficiente retorno para justificar el financiamiento.
**Observable_Symptoms:** ROA bajo constante; intereses consumen gran parte del retorno de activos; la deuda no se justifica.
**Early_Warning_Signals:** ROA < tasa de interes promedio; ROA decreciente; apalancamiento no esta generando valor.
**Typical_Causes:** Activos improductivos; baja rentabilidad operativa; exceso de activos fijos; inversion en activos que no generan retorno.
**Business_Impact:** Endeudamiento destruye valor; empresa estaria mejor sin deuda; inversion en activos no se justifica.
**Metrics_To_Check:** ROA; ROA vs Costo de deuda; Rotacion de activos; Margen operativo.
**Diagnostic_Questions:** Tus activos generan mas de lo que cuesta financiarlos? El ROA supera la tasa de interes?
**Recommended_Actions:** Vender activos improductivos; mejorar eficiencia operativa; reducir deuda si ROA no la justifica.
**Severity_Level:** High
**Related_Patterns:** FIN-056, FIN-072, FIN-101

### FIN-082
**Pattern_Name:** Asset Turnover Decline
**Category:** ROA
**Description:** La rotacion de activos (ventas / activos totales) esta disminuyendo, indicando que la empresa genera menos ventas por cada peso invertido en activos.
**Observable_Symptoms:** Nuevas inversiones en activos no generan ventas proporcionales; activos creciendo mas que ventas; sensacion de activos ociosos.
**Early_Warning_Signals:** Rotacion de activos decreciente por >2 anos; CAPEX no acompanado de crecimiento de ventas; activos fijos creciendo mas que ingresos.
**Typical_Causes:** Sobreinversion en capacidad; activos ociosos; adquisiciones que no generaron sinergias; caida de ventas sin reduccion de activos.
**Business_Impact:** ROA decreciente; capital inmovilizado sin retorno; menor rentabilidad sobre capital invertido.
**Metrics_To_Check:** Rotacion de activos = Ventas / Activos totales; Rotacion de activos fijos; CAPEX / Ventas incrementales.
**Diagnostic_Questions:** Tus activos estan generando cada vez menos ventas por peso invertido? Hay activos ociosos o subutilizados?
**Recommended_Actions:** Vender o arrendar activos subutilizados; mejorar utilizacion de capacidad; no invertir sin demanda confirmada.
**Severity_Level:** High
**Related_Patterns:** FIN-064, FIN-081, FIN-101

### FIN-083
**Pattern_Name:** Excess Idle Assets
**Category:** ROA
**Description:** La empresa mantiene activos ociosos (terrenos, maquinaria, edificios) que no generan ingresos pero consumen recursos.
**Observable_Symptoms:** Maquinaria parada; espacios no utilizados; terrenos sin uso; activos que solo generan costos (mantenimiento, impuestos, seguridad).
**Early_Warning_Signals:** Capacidad instalada utilizada < 60%; activos fijos no operativos significativos; costos de mantenimiento de activos ociosos.
**Typical_Causes:** Sobreinversion pasada; cambios en proceso productivo; compras especulativas de terrenos; falta de decision sobre activos improductivos.
**Business_Impact:** ROA bajo por activos que no generan retorno; costos de mantener activos ociosos; capital inmovilizado.
**Metrics_To_Check:** % de capacidad utilizada; Activos ociosos / Activos totales; Costo de mantener activos ociosos.
**Diagnostic_Questions:** Que % de tus activos fijos esta realmente generando ingresos? Cuanto te cuesta mantener lo que no usas?
**Recommended_Actions:** Vender, arrendar o dar de baja activos ociosos; convertir activos no operativos en generadores de ingreso; no comprar sin plan de uso.
**Severity_Level:** Medium
**Related_Patterns:** FIN-081, FIN-082, FIN-101

### FIN-084
**Pattern_Name:** ROA Hiding Poor Operational Performance
**Category:** ROA
**Description:** El ROA se mantiene artificialmente por bajo nivel de activos (empresa descapitalizada) en lugar de buena rentabilidad operativa.
**Observable_Symptoms:** ROA parece saludable pero la empresa tiene baja rentabilidad; activos minimos; equipo obsoleto; falta de inversion.
**Early_Warning_Signals:** ROA >10% pero margen neto <3%; activos muy bajos para el nivel de ventas; falta de inversion en mantenimiento.
**Typical_Causes:** Empresa descapitalizada; activos subvaluados; falta de reinversion; modelo de negocio con pocos activos pero baja rentabilidad.
**Business_Impact:** ROA enganoso; empresa no genera suficiente rentabilidad sobre ventas; falta de activos limita crecimiento.
**Metrics_To_Check:** ROA vs Margen neto; Rotacion de activos; Intensidad de capital; CAPEX historico.
**Diagnostic_Questions:** Tu ROA es bueno por eficiencia operativa o porque tienes pocos activos? La empresa esta descapitalizada?
**Recommended_Actions:** Analizar ROA en conjunto con margen neto; invertir en activos si es necesario para crecer; no confiarse en ROA alto por baja base de activos.
**Severity_Level:** Medium
**Related_Patterns:** FIN-081, FIN-082, FIN-101

### FIN-085
**Pattern_Name:** Intangible Asset Overvaluation
**Category:** ROA
**Description:** Activos intangibles (goodwill, marcas, licencias) estan sobrevalorados en el balance, inflando la base de activos y reduciendo el ROA real.
**Observable_Symptoms:** Goodwill o intangibles significativos en el balance; ROA bajo por alta base de activos; dudas sobre el valor real de esos intangibles.
**Early_Warning_Signals:** Intangibles > 30% de activos totales; goodwill de adquisiciones no deteriorado; falta de impairment test.
**Typical_Causes:** Adquisiciones pagadas con prima; activacion excesiva de gastos; falta de deterioro contable.
**Business_Impact:** ROA subestimado si intangibles estan sobrevalorados; riesgo de impairment futuro que afecte patrimonio; balance no refleja realidad.
**Metrics_To_Check:** Intangibles / Activos totales; Goodwill / Patrimonio neto; ROA ajustado excluyendo intangibles.
**Diagnostic_Questions:** Tus activos intangibles estan realmente generando el valor que muestran en el balance? Pasaron pruebas de deterioro?
**Recommended_Actions:** Realizar impairment test; amortizar intangibles segun su vida util; reportar ROA con y sin intangibles.
**Severity_Level:** Medium
**Related_Patterns:** FIN-014, FIN-081, FIN-101

### FIN-086
**Pattern_Name:** ROA Below Inflation
**Category:** ROA
**Description:** El ROA es inferior a la tasa de inflacion, lo que significa que los activos estan perdiendo poder adquisitivo.
**Observable_Symptoms:** ROA positivo pero inferior a inflacion; el negocio no crece en terminos reales; patrimonio pierde valor de compra.
**Early_Warning_Signals:** ROA < inflacion anual; crecimiento nominal pero decrecimiento real; poder adquisitivo del patrimonio disminuyendo.
**Typical_Causes:** Baja rentabilidad operativa; exceso de activos; inflacion alta no reflejada en resultados.
**Business_Impact:** Empresa destruye valor real; patrimonio pierde poder de compra; accionistas no reciben retorno real.
**Metrics_To_Check:** ROA nominal vs inflacion; ROA real (ajustado por inflacion); Crecimiento real del patrimonio.
**Diagnostic_Questions:** Tu ROA supera la inflacion? Estas ganando o perdiendo poder adquisitivo?
**Recommended_Actions:** Mejorar ROA reduciendo activos o aumentando rentabilidad; invertir en activos con mejor retorno real; considerar distribucion de capital si no hay mejores oportunidades.
**Severity_Level:** High
**Related_Patterns:** FIN-023, FIN-081, FIN-101

### FIN-087
**Pattern_Name:** High ROA but Low Cash Flow
**Category:** ROA
**Description:** ROA alto pero flujo de caja bajo, indicando que la rentabilidad no se convierte en efectivo.
**Observable_Symptoms:** ROA saludable pero caja ajustada; utilidades contables no se reflejan en liquidez; confusion sobre la generacion de efectivo.
**Early_Warning_Signals:** ROA > 10% pero CFO / Activos < 5%; diferencia entre ROA y retorno de caja sobre activos; alta proporcion de ventas a credito.
**Typical_Causes:** Ventas a credito con cobro lento; acumulacion de inventario; activos no monetarios inflados; partidas contables no monetarias.
**Business_Impact:** ROA no representa la generacion de efectivo real; riesgo de iliquidez; decisiones basadas en ROA pueden ser peligrosas.
**Metrics_To_Check:** ROA; CFO / Activos; Diferencia entre ROA y retorno de caja; Calidad del ROA.
**Diagnostic_Questions:** Tu ROA se convierte en efectivo? Cuanto de ese retorno realmente llega a caja?
**Recommended_Actions:** Mejorar conversion de utilidades a efectivo; reducir capital de trabajo; reportar ROA en efectivo junto con ROA contable.
**Severity_Level:** Medium
**Related_Patterns:** FIN-006, FIN-063, FIN-081

### FIN-088
**Pattern_Name:** ROA Decline from Poor Capex Decisions
**Category:** ROA
**Description:** Nuevas inversiones de capital estan generando retornos inferiores al ROA existente, diluyendo el ROA general.
**Observable_Symptoms:** ROA general cayendo despues de nuevas inversiones; proyectos nuevos no rinden como los existentes; CAPEX sin el retorno esperado.
**Early_Warning_Signals:** ROA decreciente mientras CAPEX aumenta; retorno de nuevos proyectos < ROA actual; proyectos con VAN negativo o no calculado.
**Typical_Causes:** Falta de proceso de evaluacion de proyectos; presion por invertir sin analisis; optimismo en proyecciones; malas decisiones de asignacion de capital.
**Business_Impact:** Deterioro progresivo del ROA; destruccion de valor; capital mal asignado que podria haberse distribuido.
**Metrics_To_Check:** ROA tendencial vs CAPEX; Retorno sobre nuevas inversiones; Tasa de aceptacion de proyectos con VAN positivo.
**Diagnostic_Questions:** Tus nuevas inversiones estan generando el retorno esperado? El ROA esta cayendo por malas decisiones de CAPEX?
**Recommended_Actions:** Implementar proceso formal de evaluacion de inversiones (VAN, TIR, Payback); revisar proyectos en curso; parar inversiones con mal desempeno.
**Severity_Level:** High
**Related_Patterns:** FIN-064, FIN-081, FIN-082
---

## ROE

### FIN-089
**Pattern_Name:** ROE Below Risk-Free Rate
**Category:** ROE
**Description:** El retorno sobre patrimonio (ROE) es inferior a la tasa libre de riesgo (bonos del tesoro, depositos), indicando que el riesgo empresarial no se compensa.
**Observable_Symptoms:** Dueño podria ganar mas invirtiendo en un plazo fijo que en su propio negocio; riesgo alto con retorno bajo.
**Early_Warning_Signals:** ROE < tasa de plazo fijo o bono del tesoro; ROE bajo consistente; inversion alternativa rinde mas sin riesgo.
**Typical_Causes:** Baja rentabilidad operativa; exceso de patrimonio (poco apalancamiento); negocio maduro con poco retorno.
**Business_Impact:** El dueño estaria mejor liquidando la empresa e invirtiendo el capital en instrumentos sin riesgo; destruccion de valor.
**Metrics_To_Check:** ROE; Tasa libre de riesgo local; Diferencial ROE - Tasa libre de riesgo; ROE / Riesgo asumido.
**Diagnostic_Questions:** Tu negocio rinde mas que un plazo fijo? El riesgo que corres se compensa con el retorno?
**Recommended_Actions:** Considerar liquidacion o venta si ROE sistematicamente < tasa libre de riesgo; mejorar rentabilidad operativa; reducir patrimonio (distribuir, recomprar).
**Severity_Level:** Critical
**Related_Patterns:** FIN-072, FIN-101, FIN-127

### FIN-090
**Pattern_Name:** ROE Inflation by Excessive Debt
**Category:** ROE
**Description:** El ROE se ve inflado artificialmente por un alto nivel de endeudamiento, no por eficiencia operativa.
**Observable_Symptoms:** ROE alto pero deuda muy alta; si se desapalancara, el ROE seria bajo; riesgo financiero elevado.
**Early_Warning_Signals:** ROE > 30% con deuda / patrimonio > 2x; ROE ajustado por deuda es mucho menor; alto riesgo financiero.
**Typical_Causes:** Endeudamiento excesivo; apalancamiento financiero extremo; negocio con bajo ROA que se apalanca para mostrar ROE alto.
**Business_Impact:** ROE refleja riesgo financiero no eficiencia; si la deuda se encarece, el ROE colapsa; riesgo de insolvencia.
**Metrics_To_Check:** ROE; ROA; Deuda / Patrimonio; ROE ajustado (ROA x Apalancamiento); Descomposicion DuPont.
**Diagnostic_Questions:** Tu ROE alto viene de buena rentabilidad operativa o de mucho endeudamiento? Si reduciras deuda, el ROE seria bueno?
**Recommended_Actions:** Reducir apalancamiento si ROE se basa solo en deuda; analizar ROE con metodologia DuPont; comparar ROE con empresas de相似 estructura de capital.
**Severity_Level:** High
**Related_Patterns:** FIN-031, FIN-042, FIN-101

### FIN-091
**Pattern_Name:** ROE Consistent but Negative
**Category:** ROE
**Description:** El ROE es consistentemente negativo, indicando que la empresa destruye patrimonio de los accionistas de forma sistematica.
**Observable_Symptoms:** Perdidas anuales recurrentes; patrimonio neto decreciente; dueño inyectando capital para cubrir perdidas.
**Early_Warning_Signals:** ROE negativo por >2 anos consecutivos; patrimonio neto decreciente; perdidas acumuladas creciendo.
**Typical_Causes:** Negocio no rentable estructuralmente; costos superiores a ingresos; falta de adaptacion al mercado.
**Business_Impact:** Destruccion total del capital invertido; necesidad de inyecciones de capital constantes; eventual quiebra.
**Metrics_To_Check:** ROE; Patrimonio neto tendencia; Perdidas acumuladas / Patrimonio; Tiempo hasta patrimonio negativo.
**Diagnostic_Questions:** Cuantos anos llevas con ROE negativo? Cuanto patrimonio has perdido? El negocio tiene solucion?
**Recommended_Actions:** Turnaround radical (reduccion de costos, cambio de modelo); considerar cierre ordenado si no hay viabilidad; no seguir inyectando capital sin plan de recuperacion.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-028, FIN-056

### FIN-092
**Pattern_Name:** Low ROE from Excess Equity
**Category:** ROE
**Description:** El ROE es bajo porque la empresa tiene demasiado patrimonio (capital ocioso) para el nivel de operaciones.
**Observable_Symptoms:** Empresa con mucha caja y poco apalancamiento; bajo ROE a pesar de buena rentabilidad operativa; capital subutilizado.
**Early_Warning_Signals:** ROE < ROA; patrimonio / activos > 70% siendo la industria apalancada; exceso de caja o capital no invertido.
**Typical_Causes:** Falta de apalancamiento; exceso de capitalizacion; aversion al endeudamiento; dividendos no distribuidos.
**Business_Impact:** Retorno suboptimo para accionistas; capital ocioso que podria distribuirse; estructura de capital ineficiente.
**Metrics_To_Check:** ROE; ROA; Deuda / Patrimonio; Exceso de capital estimado.
**Diagnostic_Questions:** Tienes demasiado capital para el nivel de operaciones? Podrias distribuir parte y mejorar el ROE?
**Recommended_Actions:** Distribuir exceso de capital (dividendos, recompra de acciones); apalancar con deuda si es prudente; invertir capital ocioso en proyectos con retorno.
**Severity_Level:** Medium
**Related_Patterns:** FIN-007, FIN-089, FIN-101

### FIN-093
**Pattern_Name:** ROE Volatility Warning
**Category:** ROE
**Description:** El ROE es extremadamente volatil de un ano a otro, indicando inestabilidad en la rentabilidad o en la estructura de capital.
**Observable_Symptoms:** ROE muy alto un ano y negativo al siguiente; resultados impredecibles; dificultad para planificar.
**Early_Warning_Signals:** Desviacion estandar del ROE > 10% anual; ROE con cambios de signo frecuentes; alta sensibilidad a factores externos.
**Typical_Causes:** Negocio ciclico; apalancamiento financiero alto; eventos no recurrentes significativos; dependencia de pocos clientes o proyectos.
**Business_Impact:** Imposibilidad de planificar; alto riesgo para accionistas; dificultad para obtener financiamiento; empresa dificil de valorar.
**Metrics_To_Check:** Desviacion estandar del ROE (5 anos); Coeficiente de variacion del ROE; ROE ajustado por ciclicidad.
**Diagnostic_Questions:** Tu ROE es estable o cambia drasticamente de un ano a otro? Sabes por que?
**Recommended_Actions:** Reducir apalancamiento financiero; diversificar ingresos; estabilizar resultados; usar ROE promedio de ciclo en lugar de anual.
**Severity_Level:** High
**Related_Patterns:** FIN-056, FIN-090, FIN-101

### FIN-094
**Pattern_Name:** ROE Hiding Poor Operations
**Category:** ROE
**Description:** ROE aparentemente saludable que oculta una operacion deficiente gracias al apalancamiento excesivo.
**Observable_Symptoms:** ROE > 15% pero margen neto bajo; alta deuda; si se elimina el efecto del apalancamiento, la rentabilidad operativa es pobre.
**Early_Warning_Signals:** ROE > 15% con margen neto < 5%; Deuda / Patrimonio > 2x; ROA bajo (< 5%).
**Typical_Causes:** Alta dependencia de deuda; negocio con bajo ROA apalancado al maximo; riesgo financiero extremo.
**Business_Impact:** ROE enganoso; empresa vulnerable a suba de tasas o caida de ventas; el apalancamiento magnifica perdidas tambien.
**Metrics_To_Check:** ROE; ROA; Apalancamiento financiero; Descomposicion DuPont (ROE = ROA x Apalancamiento).
**Diagnostic_Questions:** Tu ROE es bueno por eficiencia operativa o por apalancamiento extremo? Si quitaras la deuda, el negocio seria rentable?
**Recommended_Actions:** Reducir apalancamiento; mejorar ROA (eficiencia operativa); no depender del endeudamiento para mostrar buen ROE.
**Severity_Level:** High
**Related_Patterns:** FIN-090, FIN-091, FIN-101

### FIN-095
**Pattern_Name:** ROE Not Covering Inflation
**Category:** ROE
**Description:** El ROE nominal es positivo pero inferior a la inflacion, erosionando el valor real del patrimonio.
**Observable_Symptoms:** Patrimonio neto nominal crece pero el poder adquisitivo baja; dueño gana en pesos pero pierde en poder de compra.
**Early_Warning_Signals:** ROE < inflacion anual; patrimonio real decreciente; crecimiento nominal que no alcanza la inflacion.
**Typical_Causes:** Baja rentabilidad en contexto inflacionario; capital ocioso sin rendimiento; falta de ajuste por inflacion en estados financieros.
**Business_Impact:** Perdida de poder adquisitivo de accionistas; el negocio no preserva capital; destruccion de valor real.
**Metrics_To_Check:** ROE nominal; ROE real (ROE - Inflacion); Patrimonio real ajustado por inflacion.
**Diagnostic_Questions:** Tu ROE supera la inflacion? El valor real de tu patrimonio esta creciendo o disminuyendo?
**Recommended_Actions:** Mejorar ROE real; invertir en activos que ajusten por inflacion; distribuir capital si no se puede obtener ROE > inflacion; indexar capital.
**Severity_Level:** High
**Related_Patterns:** FIN-023, FIN-086, FIN-089

### FIN-096
**Pattern_Name:** ROE vs Industry Gap Widening
**Category:** ROE
**Description:** La brecha entre el ROE de la empresa y el promedio de la industria se esta ampliando, indicando perdida de ventaja competitiva.
**Observable_Symptoms:** Competidores rinden mejor; dueño nota que se queda atras; rentabilidad inferior a pares.
**Early_Warning_Signals:** ROE de la empresa creciendo menos que la industria; brecha ROE propio vs industria > 5% y ampliandose; perdida de participacion de mercado.
**Typical_Causes:** Competidores invierten mas, innovan mejor o gestionan mas eficientemente; empresa pierde competitividad.
**Business_Impact:** Perdida de valor relativo; empresa menos atractiva para inversores; posible adquisicion por competidor.
**Metrics_To_Check:** ROE propio vs promedio industria; Tendencia de brecha; ROE de competidores comparables.
**Diagnostic_Questions:** Tu ROE se compara favorablemente con el de tu industria? La brecha se esta ampliando?
**Recommended_Actions:** Investigar causas de la brecha; implementar mejores practicas de la industria; considerar reestructuracion profunda.
**Severity_Level:** High
**Related_Patterns:** FIN-073, FIN-089, FIN-101
---

## Break-Even Point

### FIN-097
**Pattern_Name:** Break-Even Point Rising Faster Than Revenue
**Category:** Break-Even Point
**Description:** El punto de equilibrio aumenta mas rapido que los ingresos, haciendo que la empresa sea progresivamente mas vulnerable a caidas de ventas.
**Observable_Symptoms:** Cada vez se necesita vender mas para cubrir costos; margen de seguridad reduciendose; meses malos son peores.
**Early_Warning_Signals:** Punto de equilibrio creciendo > tasa de crecimiento de ventas; margen de seguridad decreciente; costos fijos aumentando mas que ingresos.
**Typical_Causes:** Aumento de costos fijos; expansion de estructura; contrataciones sin aumento de productividad.
**Business_Impact:** Mayor riesgo operativo; caidas de venta golpean mas fuerte; menor capacidad de sobrevivir crisis.
**Metrics_To_Check:** Punto de equilibrio en unidades y porcentaje; Margen de seguridad; Tendencia de costos fijos vs ingresos.
**Diagnostic_Questions:** Cuanto necesitas vender para cubrir costos cada mes? Ese numero esta subiendo? Tu margen de seguridad es suficiente?
**Recommended_Actions:** Reducir costos fijos; aumentar margen de contribucion; monitorear punto de equilibrio mensualmente.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-054, FIN-058

### FIN-098
**Pattern_Name:** Break-Even Point Unknown
**Category:** Break-Even Point
**Description:** La empresa no conoce su punto de equilibrio, operando sin saber el nivel minimo de ventas necesario para sobrevivir.
**Observable_Symptoms:** Dueño no sabe cuanto necesita vender para no perder; decisiones sin referencia; sorpresas de perdidas.
**Early_Warning_Signals:** Falta de calculo de punto de equilibrio; no se conoce el margen de contribucion; presupuesto sin referencia a punto de equilibrio.
**Typical_Causes:** Falta de sofisticacion financiera; contabilidad basica; dueño operativo sin formacion financiera.
**Business_Impact:** Operacion a ciegas; riesgo de operar por debajo del punto de equilibrio sin saberlo; decisiones sin informacion critica.
**Metrics_To_Check:** Conocimiento de punto de equilibrio por parte del dueño; Existencia de calculo documentado; Frecuencia de actualizacion.
**Diagnostic_Questions:** Sabes exactamente cuanto necesitas vender al mes para no perder dinero? Has calculado tu punto de equilibrio?
**Recommended_Actions:** Calcular punto de equilibrio en unidades y valor; actualizar mensualmente; incorporar en reporting gerencial.
**Severity_Level:** Critical
**Related_Patterns:** FIN-054, FIN-059, FIN-061

### FIN-099
**Pattern_Name:** Break-Even Analysis Absence
**Category:** Break-Even Point
**Description:** La empresa no utiliza analisis de punto de equilibrio para tomar decisiones de precios, inversiones o presupuesto.
**Observable_Symptoms:** Decisiones de precios sin considerar punto de equilibrio; inversiones sin calcular impacto en punto de equilibrio; presupuesto sin referencia.
**Early_Warning_Signals:** Nuevos proyectos sin analisis de punto de equilibrio; cambios de precio sin evaluar impacto en volumen necesario; expansion sin calcular nuevo punto de equilibrio.
**Typical_Causes:** Baja sofisticacion de gestion; falta de herramientas financieras; cultura de decision intuitiva.
**Business_Impact:** Decisiones suboptimas; riesgos no evaluados; perdidas evitables.
**Metrics_To_Check:** Uso de analisis de punto de equilibrio en decisiones; % de proyectos con analisis de punto de equilibrio.
**Diagnostic_Questions:** Usas el punto de equilibrio para tomar decisiones de precios, inversiones o presupuesto? O decis por intuicion?
**Recommended_Actions:** Incorporar analisis de punto de equilibrio en todas las decisiones comerciales y de inversion; capacitar al equipo en su uso.
**Severity_Level:** Medium
**Related_Patterns:** FIN-058, FIN-098, FIN-101

### FIN-100
**Pattern_Name:** High Fixed Cost Break-Even Vulnerability
**Category:** Break-Even Point
**Description:** Alto porcentaje de costos fijos genera un punto de equilibrio elevado que hace la empresa muy vulnerable a fluctuaciones de demanda.
**Observable_Symptoms:** Cualquier baja en ventas genera perdidas rapidamente; meses bajos son desastrosos; empresa necesita operar a maxima capacidad.
**Early_Warning_Signals:** Costos fijos > 50% de costos totales; punto de equilibrio > 70% de capacidad; alta volatilidad de resultados.
**Typical_Causes:** Estructura pesada de personal fijo; alquileres altos; deuda con cuotas fijas; procesos intensivos en capital.
**Business_Impact:** Alta vulnerabilidad a ciclos economicos; riesgo en temporada baja; perdidas profundas en recesion.
**Metrics_To_Check:** Punto de equilibrio (% de capacidad); Costos fijos / Costos totales; Margen de contribucion.
**Diagnostic_Questions:** Que % de tu capacidad necesitas vender para cubrir costos? Cuanto te sobra para absorber una caida de ventas?
**Recommended_Actions:** Convertir costos fijos en variables; reducir estructura; diversificar ingresos para suavizar estacionalidad.
**Severity_Level:** Critical
**Related_Patterns:** FIN-054, FIN-056, FIN-058

### FIN-101
**Pattern_Name:** Break-Even Not Updated for Inflation
**Category:** Break-Even Point
**Description:** El punto de equilibrio se calculo hace meses o anos y no se actualiza por inflacion de costos, dando una referencia erronea.
**Observable_Symptoms:** Punto de equilibrio calculado que ya no refleja la realidad; sorpresas de perdidas a pesar de ventas sobre el punto de equilibrio calculado.
**Early_Warning_Signals:** Punto de equilibrio no actualizado en > 6 meses; calculo con costos de periodo anterior; inflacion alta sin ajuste.
**Typical_Causes:** Falta de actualizacion periodica; calculo unico al inicio del ano; desconocimiento del impacto inflacionario.
**Business_Impact:** Decisiones basadas en referencia incorrecta; falsa sensacion de seguridad; perdidas no anticipadas.
**Metrics_To_Check:** Fecha del ultimo calculo; Diferencia entre punto de equilibrio calculado y real; Frecuencia de actualizacion.
**Diagnostic_Questions:** Cuando fue la ultima vez que actualizaste tu punto de equilibrio? Refleja los costos actuales?
**Recommended_Actions:** Actualizar punto de equilibrio mensualmente en contextos inflacionarios; automatizar calculo con costos reales.
**Severity_Level:** High
**Related_Patterns:** FIN-023, FIN-097, FIN-098

### FIN-102
**Pattern_Name:** Multi-Product Break-Even Complexity
**Category:** Break-Even Point
**Description:** La empresa tiene multiples productos con diferentes margenes y no calcula el punto de equilibrio considerando el mix, usando un promedio que distorsiona la realidad.
**Observable_Symptoms:** Algunos meses se vende mas pero se gana menos; punto de equilibrio calculado no coincide con la realidad; mix de ventas variado sin ajuste.
**Early_Warning_Signals:** Punto de equilibrio calculado con margen promedio; mix de ventas cambiante; diferencias entre punto de equilibrio presupuestado y real.
**Typical_Causes:** Complejidad de productos; falta de costeo por producto; simplificacion excesiva.
**Business_Impact:** Punto de equilibrio no confiable; decisiones basadas en informacion incorrecta; sorpresas de rentabilidad.
**Metrics_To_Check:** Metodo de calculo del punto de equilibrio; Variabilidad del mix de ventas; Precision del punto de equilibrio vs resultados reales.
**Diagnostic_Questions:** Tu punto de equilibrio considera los diferentes margenes de cada producto? O usas un promedio que puede enganar?
**Recommended_Actions:** Calcular punto de equilibrio por producto o segmento; usar margen de contribucion ponderado ajustado por mix proyectado; monitorear mix real vs presupuestado.
**Severity_Level:** Medium
**Related_Patterns:** FIN-025, FIN-059, FIN-077

### FIN-103
**Pattern_Name:** Break-Even Safety Margin Erosion
**Category:** Break-Even Point
**Description:** El margen de seguridad (ventas actuales - punto de equilibrio) se esta reduciendo peligrosamente.
**Observable_Symptoms:** Cualquier pequena caida en ventas ahora genera perdidas; antes se podia caer mas; nerviosismo del equipo ante bajas de venta.
**Early_Warning_Signals:** Margen de seguridad < 20% y decreciente; punto de equilibrio acercandose a ventas actuales; ventas estables pero punto de equilibrio subiendo.
**Typical_Causes:** Aumento de costos fijos; caida de ventas; reduccion de margen de contribucion.
**Business_Impact:** Alta vulnerabilidad a caidas de ventas; cualquier crisis menor lleva a perdidas; riesgo de quiebra.
**Metrics_To_Check:** Margen de seguridad absoluto y porcentual; Tendencia del margen; Ventas actuales / Punto de equilibrio.
**Diagnostic_Questions:** Cuanto pueden caer tus ventas antes de empezar a perder dinero? Ese colchon es suficiente?
**Recommended_Actions:** Aumentar margen de seguridad (subir ventas, bajar punto de equilibrio, mejorar margen de contribucion); monitorear mensualmente.
**Severity_Level:** Critical
**Related_Patterns:** FIN-097, FIN-098, FIN-100
---

## Leverage

### FIN-104
**Pattern_Name:** Financial Leverage Beyond Prudent Levels
**Category:** Leverage
**Description:** El apalancamiento financiero (deuda / patrimonio) excede niveles prudentes para la industria, aumentando el riesgo de insolvencia.
**Observable_Symptoms:** Deuda alta en relacion al patrimonio; ansiedad por vencimientos; dificultad para conseguir nuevo credito.
**Early_Warning_Signals:** Deuda / Patrimonio > 2x (o > industria); Deuda Neta / EBITDA > 4x; cobertura de intereses < 2x.
**Typical_Causes:** Crecimiento financiado con deuda; perdidas que reducen patrimonio; adquisiciones apalancadas; excesiva distribucion de dividendos.
**Business_Impact:** Alto riesgo financiero; vulnerabilidad a suba de tasas; dificultad para obtener financiamiento; riesgo de quiebra.
**Metrics_To_Check:** Deuda / Patrimonio; Deuda Neta / EBITDA; Cobertura de intereses; Apalancamiento financiero total.
**Diagnostic_Questions:** Cuantas veces tu deuda supera tu patrimonio? Estas en linea con tu industria?
**Recommended_Actions:** Reducir deuda; aumentar patrimonio (capitalizacion); refinanciar a mayores plazos; generar retention de utilidades.
**Severity_Level:** Critical
**Related_Patterns:** FIN-011, FIN-031, FIN-042

### FIN-105
**Pattern_Name:** Operating Leverage Too High
**Category:** Leverage
**Description:** El apalancamiento operativo es muy alto, magnificando el efecto de cambios en ventas sobre la utilidad.
**Observable_Symptoms:** Alta volatilidad en resultados; meses buenos muy buenos, meses malos muy malos; gran sensibilidad a cambios en ventas.
**Early_Warning_Signals:** DOL > 4x; costos fijos > 50% de costos totales; alta variabilidad en EBIT.
**Typical_Causes:** Alta proporcion de costos fijos; procesos intensivos en capital; estructura administrativa pesada.
**Business_Impact:** Resultados volatiles; alta sensibilidad a ciclos economicos; riesgo en caidas de ventas.
**Metrics_To_Check:** DOL = % cambio EBIT / % cambio Ventas; Costos fijos / Costos totales; Variabilidad de EBIT.
**Diagnostic_Questions:** Si tus ventas caen 10%, cuanto caeria tu utilidad? El apalancamiento operativo esta en niveles manejables?
**Recommended_Actions:** Convertir costos fijos en variables; diversificar ingresos; mantener reservas para ciclos bajos.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-056, FIN-100

### FIN-106
**Pattern_Name:** Combined Leverage Danger
**Category:** Leverage
**Description:** La combinacion de alto apalancamiento operativo y financiero crea un efecto multiplicador que puede destruir rapidamente el patrimonio.
**Observable_Symptoms:** Alta volatilidad de utilidad neta; cambios pequenos en ventas tienen gran impacto en resultado final; resultados extremos.
**Early_Warning_Signals:** DOL > 3x y DFL > 2x simultaneamente; apalancamiento combinado > 6x; alta variabilidad de ROE.
**Typical_Causes:** Industria intensiva en capital (alto DOL) combinada con alto endeudamiento (alto DFL); estructura de riesgo agresiva.
**Business_Impact:** Resultados extremadamente volatiles; riesgo de perdidas catastróficas en caidas de ventas; quiebra en recesion moderada.
**Metrics_To_Check:** DOL; DFL; DCL (Degree of Combined Leverage = DOL x DFL); Variabilidad de utilidad neta.
**Diagnostic_Questions:** Cual es el impacto combinado de tus costos fijos y tu deuda sobre la utilidad neta? Una caida de 10% en ventas que impacto tendria?
**Recommended_Actions:** Reducir al menos uno de los dos apalancamientos; si no se puede reducir DOL, reducir DFL y viceversa; mantener colchon de liquidez.
**Severity_Level:** Critical
**Related_Patterns:** FIN-056, FIN-090, FIN-105

### FIN-107
**Pattern_Name:** Negative Financial Leverage
**Category:** Leverage
**Description:** El ROA es inferior al costo de la deuda, por lo que el apalancamiento financiero esta destruyendo valor en lugar de potenciarlo.
**Observable_Symptoms:** ROA < tasa de interes; apalancamiento reduce el ROE en lugar de aumentarlo; deuda no genera valor.
**Early_Warning_Signals:** ROA < costo de deuda promedio; ROE < ROA; apalancamiento financiero negativo.
**Typical_Causes:** Baja rentabilidad operativa; deuda cara; inversion en activos que no generan el retorno esperado.
**Business_Impact:** Endeudamiento destruye valor; la empresa estaria mejor sin deuda; el riesgo financiero no se compensa.
**Metrics_To_Check:** ROA vs Costo de deuda; DFL; ROE vs ROA; Spread (ROA - Costo deuda).
**Diagnostic_Questions:** El ROA supera el costo de tu deuda? El endeudamiento esta mejorando o empeorando el retorno para los accionistas?
**Recommended_Actions:** Reducir deuda; mejorar ROA; reestructurar deuda a menor costo; considerar desapalancamiento.
**Severity_Level:** Critical
**Related_Patterns:** FIN-072, FIN-081, FIN-090

### FIN-108
**Pattern_Name:** Off-Balance Sheet Leverage
**Category:** Leverage
**Description:** La empresa tiene compromisos financieros fuera del balance (arriendos operativos, garantias, joint ventures) que aumentan su apalancamiento real.
**Observable_Symptoms:** Deuda en balance parece baja pero la empresa tiene compromisos significativos no registrados; apalancamiento real mayor al reportado.
**Early_Warning_Signals:** Arriendos operativos significativos; garantias otorgadas no registradas; compromisos de compra futuros.
**Typical_Causes:** Preferencia por mantener deuda fuera del balance; arriendos en lugar de compras; garantias a vinculadas.
**Business_Impact:** Apalancamiento real mayor al que parece; riesgos no reflejados en estados financieros; decisiones basadas en informacion incompleta.
**Metrics_To_Check:** Arriendos operativos / EBITDA; Garantias / Patrimonio; Apalancamiento ajustado incluyendo off-balance sheet.
**Diagnostic_Questions:** Que compromisos financieros tienes fuera del balance? Tu apalancamiento real es mayor al que muestran los estados financieros?
**Recommended_Actions:** Identificar y medir todo el apalancamiento off-balance sheet; reportar apalancamiento ajustado; considerar traer compromisos al balance.
**Severity_Level:** Medium
**Related_Patterns:** FIN-017, FIN-066, FIN-104

### FIN-109
**Pattern_Name:** Leverage Increase Without Profit Growth
**Category:** Leverage
**Description:** La empresa ha aumentado su endeudamiento (apalancamiento) pero no ha generado mayor rentabilidad, indicando que la deuda no se uso productivamente.
**Observable_Symptoms:** Deuda subiendo pero utilidad plana; inversiones financiadas con deuda que no rinden; apalancamiento creciente sin resultados.
**Early_Warning_Signals:** Deuda/EBITDA aumentando mientras EBITDA plano; nueva deuda sin mejora en rentabilidad; ROA decreciente con apalancamiento creciente.
**Typical_Causes:** Deuda utilizada para gastos operativos; inversiones fallidas; distribucion de dividendos con deuda; capital de trabajo mal gestionado.
**Business_Impact:** Endeudamiento sin retorno; mayor riesgo sin compensacion; espiral de deuda.
**Metrics_To_Check:** Deuda/EBITDA tendencia; EBITDA tendencia; ROIC; Uso de fondos de nueva deuda.
**Diagnostic_Questions:** Para que usaste la nueva deuda? Genero el retorno esperado? El aumento de apalancamiento se justifica?
**Recommended_Actions:** Detener nuevo endeudamiento hasta que exista plan de uso productivo; evaluar si activos financiados pueden venderse; reestructurar.
**Severity_Level:** High
**Related_Patterns:** FIN-031, FIN-033, FIN-104

### FIN-110
**Pattern_Name:** Leverage Concentration in Floating Rate Debt
**Category:** Leverage
**Description:** La mayoria de la deuda es a tasa variable, exponiendo a la empresa a riesgo de suba de tasas de interes.
**Observable_Symptoms:** Gastos financieros que suben cuando las tasas suben; resultados sensibles a politica monetaria; incertidumbre sobre costos financieros futuros.
**Early_Warning_Signals:** Deuda a tasa variable > 50% de deuda total; sin cobertura de tasa; gastos financieros volatiles.
**Typical_Causes:** Preferencia por tasas iniciales mas bajas; falta de oferta de tasa fija; desconocimiento del riesgo.
**Business_Impact:** Gastos financieros impredecibles; riesgo de aumento de costo de deuda; margenes comprimidos en contexto de suba de tasas.
**Metrics_To_Check:** Deuda tasa variable / Deuda total; Sensibilidad de gastos financieros a cambio de tasas; Cobertura de tasa.
**Diagnostic_Questions:** Que % de tu deuda es a tasa variable? Que pasaria si las tasas suben 5%? Puedes soportarlo?
**Recommended_Actions:** Convertir deuda variable a fija; contratar swaps de tasa; limitar exposicion a tasa variable; estresar flujo de caja con suba de tasas.
**Severity_Level:** High
**Related_Patterns:** FIN-035, FIN-053, FIN-104

### FIN-111
**Pattern_Name:** Undersized Leverage (Excessive Conservatism)
**Category:** Leverage
**Description:** La empresa tiene muy poca deuda en relacion a su capacidad de pago, perdiendo oportunidades de apalancamiento que mejorarian el ROE.
**Observable_Symptoms:** ROE bajo por exceso de patrimonio; empresa podria apalancarse mas y mejorar retorno; dueño averso a la deuda.
**Early_Warning_Signals:** Deuda / EBITDA < 0.5x; cobertura de intereses > 10x; ROE bajo con buena rentabilidad operativa.
**Typical_Causes:** Aversion al riesgo del dueño; malas experiencias previas con deuda; falta de understanding de apalancamiento.
**Business_Impact:** ROE suboptimo; retorno para accionistas menor al potencial; estructura de capital ineficiente.
**Metrics_To_Check:** Deuda/EBITDA; ROE vs ROE potencial con apalancamiento optimo; Capacidad de endeudamiento no utilizada.
**Diagnostic_Questions:** Estas dejando de crecer por no usar deuda? Podrias mejorar el ROE con apalancamiento moderado?
**Recommended_Actions:** Evaluar estructura de capital optima; considerar apalancamiento moderado si hay proyectos con VAN positivo; no sobre-apalancarse.
**Severity_Level:** Medium
**Related_Patterns:** FIN-007, FIN-092, FIN-101
---

## Financial Productivity

### FIN-112
**Pattern_Name:** Revenue Per Employee Decline
**Category:** Financial Productivity
**Description:** El ingreso por empleado esta disminuyendo, indicando perdida de productividad laboral.
**Observable_Symptoms:** Se contrata mas personal pero las ventas no crecen proporcionalmente; sensacion de que el equipo rinde menos.
**Early_Warning_Signals:** Revenue / Empleado decreciente por >2 anos; crecimiento de headcount > crecimiento de ingresos; productividad por debajo de benchmark.
**Typical_Causes:** Contrataciones excesivas; baja productividad del equipo; ventas planas con mas personal; mala gestion de recursos.
**Business_Impact:** Rentabilidad decreciente; estructura sobredimensionada; desventaja competitiva.
**Metrics_To_Check:** Revenue por empleado; EBITDA por empleado; Costo laboral / Revenue; Headcount / Ventas.
**Diagnostic_Questions:** Cuanto genera cada empleado en ingresos? Ese numero esta mejorando o empeorando?
**Recommended_Actions:** Revisar dotacion vs produccion; automatizar procesos; mejorar capacitacion; implementar metricas de productividad.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-024, FIN-052

### FIN-113
**Pattern_Name:** Asset Productivity Below Capacity
**Category:** Financial Productivity
**Description:** Los activos fijos estan siendo subutilizados, generando menos produccion o ingresos de los que podrian.
**Observable_Symptoms:** Maquinaria parada frequentemente; turnos de produccion no utilizados; espacios fisicos ociosos.
**Early_Warning_Signals:** Capacidad instalada utilizada < 70%; rotacion de activos fijos decreciente; horas maquina no utilizadas.
**Typical_Causes:** Sobreinversion en capacidad; caida de demanda; falta de planificacion de produccion; cuellos de botella en otras areas.
**Business_Impact:** ROA bajo; capital inmovilizado sin retorno; costos fijos por unidad altos.
**Metrics_To_Check:** % de capacidad utilizada; Rotacion de activos fijos; Produccion real / Produccion potencial.
**Diagnostic_Questions:** Que % de tu capacidad productiva estas usando? Podrias producir mas con los mismos activos?
**Recommended_Actions:** Mejorar planificacion de produccion; buscar clientes o productos para llenar capacidad; vender exceso de capacidad; tercerizar produccion excedente.
**Severity_Level:** Medium
**Related_Patterns:** FIN-081, FIN-082, FIN-083

### FIN-114
**Pattern_Name:** Working Capital Productivity Below Industry
**Category:** Financial Productivity
**Description:** La empresa genera menos ventas por cada peso invertido en capital de trabajo que el promedio de la industria.
**Observable_Symptoms:** Capital de trabajo alto para el nivel de ventas; dinero atado en cobranza e inventario; comparacion desfavorable.
**Early_Warning_Signals:** Ventas / Capital de trabajo < industry benchmark; dias de cobro e inventario mayores que el promedio; rentabilidad afectada por capital inmovilizado.
**Typical_Causes:** Gestion ineficiente de cobranza; inventario excesivo; plazos de pago generosos a clientes.
**Business_Impact:** Capital de trabajo improductivo; menor rentabilidad; menos efectivo disponible.
**Metrics_To_Check:** Ventas / Capital de trabajo; Rotacion de capital de trabajo; Benchmark de industria.
**Diagnostic_Questions:** Cuantas veces al ano tu capital de trabajo genera ventas? Como te comparas con la industria?
**Recommended_Actions:** Mejorar cobranza; reducir inventario; negociar plazos con proveedores; liberar capital de trabajo improductivo.
**Severity_Level:** Medium
**Related_Patterns:** FIN-041, FIN-046, FIN-050

### FIN-115
**Pattern_Name:** EBITDA per Employee Below Benchmark
**Category:** Financial Productivity
**Description:** El EBITDA generado por empleado es inferior al benchmark de la industria, indicando baja productividad de la fuerza laboral.
**Observable_Symptoms:** Equipo numeroso pero rentabilidad baja; comparacion desfavorable con competidores similares.
**Early_Warning_Signals:** EBITDA / Empleado < 70% del benchmark; crecimiento de headcount sin crecimiento de EBITDA; costo laboral / EBITDA alto.
**Typical_Causes:** Exceso de personal; baja calificacion; procesos ineficientes; falta de tecnologia.
**Business_Impact:** Rentabilidad por empleado baja; estructura ineficiente; desventaja competitiva en costos.
**Metrics_To_Check:** EBITDA por empleado; EBITDA / Costo laboral; Benchmark de industria.
**Diagnostic_Questions:** Cuanto EBITDA genera cada empleado? Estas en linea con tu industria?
**Recommended_Actions:** Mejorar procesos y productividad; invertir en tecnologia y capacitacion; revisar dotacion.
**Severity_Level:** High
**Related_Patterns:** FIN-022, FIN-052, FIN-112

### FIN-116
**Pattern_Name:** Asset Base Growing Faster Than Revenue
**Category:** Financial Productivity
**Description:** La base de activos crece mas rapido que los ingresos, indicando decreciente productividad del capital.
**Observable_Symptoms:** Se invierte en activos pero las ventas no crecen al mismo ritmo; ROA decreciente; sensacion de que las inversiones no rinden.
**Early_Warning_Signals:** Crecimiento de activos > crecimiento de ingresos por >2 anos; rotacion de activos decreciente; CAPEX / Ventas incrementales alto.
**Typical_Causes:** Sobreinversion; proyectos sin retorno esperado; compras no planificadas; capacidad ociosa.
**Business_Impact:** Menor eficiencia del capital; ROA decreciente; destruccion de valor.
**Metrics_To_Check:** Crecimiento de activos vs crecimiento de ingresos; Rotacion de activos; CAPEX / Ventas incrementales.
**Diagnostic_Questions:** Tus activos crecen al mismo ritmo que tus ventas? Cada peso invertido en activos genera mas o menos ventas que antes?
**Recommended_Actions:** Frenar inversion hasta mejorar utilizacion; vender activos improductivos; evaluar retorno de inversiones recientes.
**Severity_Level:** High
**Related_Patterns:** FIN-081, FIN-082, FIN-088

### FIN-117
**Pattern_Name:** Low Value Added per Employee
**Category:** Financial Productivity
**Description:** El valor agregado por empleado (ventas - costo de insumos) es bajo, indicando poca contribucion economica por persona.
**Observable_Symptoms:** Muchas personas para poca transformacion; procesos con baja tecnologia; productos de bajo valor agregado.
**Early_Warning_Signals:** Valor agregado por empleado < benchmark; alta proporcion de costo de insumos en ventas; margen bruto bajo.
**Typical_Causes:** Modelo de negocios de bajo valor agregado; procesos manuales; poca inversion en tecnologia; falta de calificacion.
**Business_Impact:** Dificultad para pagar salarios competitivos; baja rentabilidad; vulnerabilidad a competidores de bajo costo.
**Metrics_To_Check:** Valor agregado por empleado = (Ventas - Insumos) / Empleados; Margen bruto; Productividad laboral.
**Diagnostic_Questions:** Cuanto valor economico agrega cada empleado? Podrias aumentarlo con tecnologia o capacitacion?
**Recommended_Actions:** Automatizar procesos de bajo valor; capacitar al personal; migrar a productos/servicios de mayor valor agregado.
**Severity_Level:** High
**Related_Patterns:** FIN-030, FIN-052, FIN-112

### FIN-118
**Pattern_Name:** Receivables to Sales Ratio Growing
**Category:** Financial Productivity
**Description:** La relacion entre cuentas por cobrar y ventas esta creciendo, indicando que cada vez se tarda mas en cobrar o se vende mas a credito.
**Observable_Symptoms:** Cuentas por cobrar creciendo mas que ventas; mayor inversion en credito; caja cada vez mas ajustada.
**Early_Warning_Signals:** Cuentas por cobrar / Ventas mensuales > 2x y creciendo; dias de cobro extendiendose; plazo de credito a clientes aumentando.
**Typical_Causes:** Politica de credito mas laxa para impulsar ventas; clientes con problemas de pago; cobranza deficiente.
**Business_Impact:** Capital de trabajo inmovilizado; mayor riesgo de incobrables; necesidad de financiamiento para cubrir el descalce.
**Metrics_To_Check:** Cuentas por cobrar / Ventas; Dias de cobro; Rotacion de cuentas por cobrar.
**Diagnostic_Questions:** Tus cuentas por cobrar crecen al mismo ritmo que las ventas? O estan creciendo mas? Por que?
**Recommended_Actions:** Endurecer politicas de credito; fortalecer cobranza; ofrecer descuentos por pronto pago; considerar factoring para reducir exposicion.
**Severity_Level:** High
**Related_Patterns:** FIN-002, FIN-041, FIN-042

### FIN-119
**Pattern_Name:** Cash Flow Productivity Gap
**Category:** Financial Productivity
**Description:** Diferencia creciente entre la productividad medida contablemente (ROA, ROE) y la generacion de efectivo real.
**Observable_Symptoms:** Buenos indicadores contables pero caja ajustada; utilidades que no se convierten en efectivo; ROA y ROE no se reflejan en liquidez.
**Early_Warning_Signals:** CFO / Net Income < 0.7 sostenido; diferencia creciente entre ROA y CFO/Activos; capital de trabajo absorbiendo efectivo.
**Typical_Causes:** Crecimiento de cuentas por cobrar; acumulacion de inventario; partidas contables no monetarias; resultados basados en devengado no percibido.
**Business_Impact:** Rendimiento contable no representa la realidad de caja; riesgo de iliquidez; decisiones basadas en metricas enganosas.
**Metrics_To_Check:** CFO / Net Income; ROA vs CFO/Activos; Calidad del resultado (CFO / EBITDA).
**Diagnostic_Questions:** Tus utilidades contables se convierten en efectivo? Hay brecha entre la rentabilidad contable y la generacion de caja?
**Recommended_Actions:** Mejorar conversion de resultados a efectivo (gestionar capital de trabajo); medir y reportar rentabilidad en efectivo.
**Severity_Level:** High
**Related_Patterns:** FIN-006, FIN-063, FIN-087

### FIN-120
**Pattern_Name:** Investment Productivity Decline
**Category:** Financial Productivity
**Description:** Nuevas inversiones estan generando retornos decrecientes, indicando que las oportunidades de inversion rentables se estan agotando.
**Observable_Symptoms:** Cada nueva inversion rinde menos que la anterior; necesidad de invertir mas para mismo retorno; proyectos con TIR decreciente.
**Early_Warning_Signals:** ROIC decreciente con nuevas inversiones; TIR de proyectos bajando; tasa de aceptacion de proyectos disminuyendo.
**Typical_Causes:** Agotamiento de oportunidades en el mercado; saturacion del negocio principal; falta de innovacion; malas decisiones de inversion.
**Business_Impact:** Destruccion de valor; necesidad de buscar nuevas areas de crecimiento; estancamiento.
**Metrics_To_Check:** ROIC tendencial; TIR promedio de nuevos proyectos; CAPEX / EBITDA incremental.
**Diagnostic_Questions:** Tus inversiones mas recientes estan rindiendo tanto como las anteriores? Se estan agotando las buenas oportunidades?
**Recommended_Actions:** Evaluar rigurosamente nuevos proyectos; considerar distribuir capital si no hay buenas oportunidades; explorar nuevos mercados o modelos de negocio.
**Severity_Level:** Medium
**Related_Patterns:** FIN-081, FIN-088, FIN-101
---

## Profitable Growth

### FIN-121
**Pattern_Name:** Growth Without Margin Improvement
**Category:** Profitable Growth
**Description:** La empresa crece en ingresos pero los margenes no mejoran, indicando que el crecimiento no genera eficiencias de escala.
**Observable_Symptoms:** Ventas suben pero margen EBITDA no mejora; no se ven economias de escala; crecimiento no rentable.
**Early_Warning_Signals:** Crecimiento de ingresos > 10% anual pero margen EBITDA plano; gastos operativos creciendo al mismo ritmo que ventas; sin apalancamiento operativo positivo.
**Typical_Causes:** Crecimiento acompanado de aumento proporcional de costos; modelo de negocio sin economias de escala; falta de apalancamiento operativo.
**Business_Impact:** Crecimiento no genera valor adicional; empresa no se vuelve mas rentable al crecer; esfuerzo sin recompensa.
**Metrics_To_Check:** Margen EBITDA tendencial vs crecimiento de ingresos; Apalancamiento operativo; Gastos operativos / Ventas.
**Diagnostic_Questions:** Al crecer, tus margenes mejoran? Estas aprovechando economias de escala?
**Recommended_Actions:** Identificar y capturar economias de escala; racionalizar gastos al crecer; asegurar que el crecimiento genere apalancamiento operativo positivo.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-056, FIN-127

### FIN-122
**Pattern_Name:** Unprofitable Customer Acquisition
**Category:** Profitable Growth
**Description:** La empresa adquiere clientes cuyo valor de vida (LTV) es menor que el costo de adquisicion (CAC).
**Observable_Symptoms:** Muchos clientes nuevos pero rentabilidad no mejora; alto gasto en marketing sin retorno; clientes que se van antes de recuperar inversion.
**Early_Warning_Signals:** LTV / CAC < 3x; tiempo de recuperacion de CAC > 18 meses; churn alto en clientes nuevos; CAC creciente.
**Typical_Causes:** Competencia elevando costos de adquisicion; producto con baja retencion; precio insuficiente para recuperar CAC; targeting ineficiente.
**Business_Impact:** Cada nuevo cliente destruye valor; crecimiento mata la rentabilidad; necesidad de inversion constante.
**Metrics_To_Check:** LTV / CAC; Tiempo de recuperacion de CAC; Churn rate; CAC por canal.
**Diagnostic_Questions:** Cada nuevo cliente te deja mas dinero del que gastaste en adquirirlo? Cuanto tiempo tardas en recuperar la inversion?
**Recommended_Actions:** Mejorar retencion (aumentar LTV); optimizar canales de adquisicion (reducir CAC); aumentar precios; enfocar en segmentos con mejor LTV/CAC.
**Severity_Level:** Critical
**Related_Patterns:** FIN-003, FIN-057, FIN-127

### FIN-123
**Pattern_Name:** Growth Consuming All Free Cash Flow
**Category:** Profitable Growth
**Description:** El crecimiento consume todo el flujo de caja libre, impidiendo reducir deuda, distribuir dividendos o acumular reservas.
**Observable_Symptoms:** Flujo de caja libre consistentemente bajo o negativo a pesar de rentabilidad; todo el efectivo se reinvierte en crecer; dueño nunca ve efectivo.
**Early_Warning_Signals:** Flujo de caja libre < 0 sostenido; FCF / EBITDA < 20%; CAPEX y capital de trabajo consumiendo todo el EBITDA.
**Typical_Causes:** Crecimiento intensivo en capital; aumento de capital de trabajo mayor al EBITDA; reinversion total de utilidades.
**Business_Impact:** Dependencia de financiamiento externo; imposibilidad de reducir deuda; dueño no recibe retorno de su inversion.
**Metrics_To_Check:** FCF; FCF / EBITDA; CAPEX + Var. Capital de trabajo / EBITDA; Tasa de reinversion.
**Diagnostic_Questions:** Cuanto flujo de caja libre genera tu empresa despues de financiar el crecimiento? Te queda algo para distribuir o reducir deuda?
**Recommended_Actions:** Moderar ritmo de crecimiento para generar FCF positivo; financiar crecimiento con deuda de LP o capital; priorizar proyectos con mejor retorno.
**Severity_Level:** High
**Related_Patterns:** FIN-003, FIN-041, FIN-064

### FIN-124
**Pattern_Name:** Growth Through Price Reductions
**Category:** Profitable Growth
**Description:** El crecimiento de volumen se logra principalmente mediante reducciones de precio, que erosionan el margen y pueden hacer el crecimiento no rentable.
**Observable_Symptoms:** Volumen subiendo pero margen por unidad bajando; descuentos frecuentes; precio promedio decreciente.
**Early_Warning_Signals:** Crecimiento de volumen > crecimiento de ingresos; precio promedio por unidad decreciente; elasticidad precio alta.
**Typical_Causes:** Competencia agresiva; estrategia de participacion de mercado via precio; producto commoditizado; falta de diferenciacion.
**Business_Impact:** Crecimiento ilusorio en valor; margenes comprimidos; guerras de precio que nadie gana.
**Metrics_To_Check:** Precio promedio / unidad; Crecimiento de volumen vs crecimiento de ingresos; Margen por unidad.
**Diagnostic_Questions:** Tus precios estan bajando para crecer? El aumento de volumen compensa la caida de margen?
**Recommended_Actions:** Diferenciar producto para reducir elasticidad precio; competir en valor no en precio; buscar segmentos donde el precio no sea determinante.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-075, FIN-077

### FIN-125
**Pattern_Name:** Growth Masking Operational Decline
**Category:** Profitable Growth
**Description:** El crecimiento de ingresos oculta un deterioro operativo que se hace visible solo cuando se analizan los margenes y la eficiencia.
**Observable_Symptoms:** Ventas subiendo pero margenes y rentabilidad por unidad bajando; indicadores operativos empeorando; problemas ocultos por el volumen.
**Early_Warning_Signals:** Margen bruto unitario decreciente; eficiencia operativa empeorando; rentabilidad por cliente decreciente.
**Typical_Causes:** Crecimiento en segmentos de menor margen; mayor complejidad operativa sin gestion; ineficiencias que crecen con el volumen.
**Business_Impact:** Crecimiento no sostenible; problemas se agravan con el tiempo; cuando el crecimiento se detenga, los problemas seran evidentes.
**Metrics_To_Check:** Margen unitario; Eficiencia operativa; Rentabilidad por cliente/segmento; Costos de complejidad.
**Diagnostic_Questions:** Si analizas la rentabilidad por unidad, esta mejorando o empeorando? El crecimiento esta escondiendo problemas operativos?
**Recommended_Actions:** Analizar rentabilidad unitaria; mejorar eficiencia operativa antes de seguir creciendo; asegurar que el crecimiento sea rentable en todos los niveles.
**Severity_Level:** High
**Related_Patterns:** FIN-021, FIN-025, FIN-056

### FIN-126
**Pattern_Name:** Growth-Stage Cash Flow Crisis
**Category:** Profitable Growth
**Description:** La empresa atraviesa una fase de crecimiento donde el flujo de caja es sistematicamente negativo, requiriendo financiamiento externo.
**Observable_Symptoms:** Caja negativa a pesar de buenas ventas; necesidad de inyecciones de capital; crecimiento que consume efectivo.
**Early_Warning_Signals:** FCF negativo por >2 anos; crecimiento financiado con deuda de CP; aumento de capital de trabajo > EBITDA.
**Typical_Causes:** Descalce entre cobros y pagos en fase de crecimiento; inversion en inventario y cuentas por cobrar; CAPEX de expansion.
**Business_Impact:** Dependencia de financiamiento externo; dilucion de accionistas; riesgo de iliquidez si se corta el financiamiento.
**Metrics_To_Check:** FCF; Burn rate; Months of runway; Capital de trabajo vs crecimiento.
**Diagnostic_Questions:** Cuanto efectivo estas quemando por mes? Cuanto tiempo puedes sostener este ritmo sin financiamiento adicional?
**Recommended_Actions:** Proyectar flujo de caja a 12-24 meses; asegurar financiamiento antes de necesitarlo; considerar desacelerar crecimiento si no hay financiamiento asegurado.
**Severity_Level:** High
**Related_Patterns:** FIN-003, FIN-041, FIN-123

### FIN-127
**Pattern_Name:** Revenue Growth but Negative Unit Economics
**Category:** Profitable Growth
**Description:** La empresa crece en ingresos totales pero cada unidad vendida (producto, cliente, transaccion) es economicamente negativa.
**Observable_Symptoms:** Ventas totales subiendo pero perdidas creciendo; mas ventas = mas perdidas; necesidad de mas capital para financiar crecimiento.
**Early_Warning_Signals:** Margen de contribucion unitario negativo; LTV / CAC < 1x; crecimiento de perdidas mayor al crecimiento de ingresos.
**Typical_Causes:** Precios por debajo del costo total; modelo de negocio no viable; objetivo de crecimiento a cualquier costo; subsidio cruzado no intencional.
**Business_Impact:** Crecimiento acelera la quiebra; cada nuevo cliente empeora la situacion; modelo de negocio no sostenible.
**Metrics_To_Check:** Margen de contribucion unitario; LTV / CAC; Margen neto; Economia unitaria por producto/cliente.
**Diagnostic_Questions:** Cada unidad que vendes es rentable? O estas perdiendo dinero con cada venta y esperando recuperar con volumen?
**Recommended_Actions:** Detener crecimiento inmediatamente; arreglar economia unitaria (subir precios, bajar costos); solo crecer cuando la unidad economica sea positiva.
**Severity_Level:** Critical
**Related_Patterns:** FIN-021, FIN-057, FIN-058

### FIN-128
**Pattern_Name:** Growth Without Scalable Infrastructure
**Category:** Profitable Growth
**Description:** La empresa crece sin invertir en sistemas, procesos y personas, generando caos operativo que amenaza la calidad del servicio.
**Observable_Symptoms:** Errores operativos frecuentes; clientes insatisfechos; empleados sobrepasados; procesos que no escalan.
**Early_Warning_Signals:** Crecimiento > 20% sin inversion en sistemas; quejas de clientes aumentando; rotacion de empleados; retrabajo creciente.
**Typical_Causes:** Enfoque exclusivo en ventas sin invertir en operaciones; cultura de apagar incendios; falta de vision sistemica.
**Business_Impact:** Calidad se degrada; clientes se van; crecimiento no sostenible; colapso operativo.
**Metrics_To_Check:** NPS / Satisfaccion de clientes; Tasa de errores operativos; Rotacion de empleados; Inversion en sistemas / Crecimiento.
**Diagnostic_Questions:** Tu infraestructura operativa esta preparada para soportar el crecimiento? Los procesos escalan?
**Recommended_Actions:** Invertir en sistemas y procesos proporcionalmente al crecimiento; contratar talento gerencial antes de necesitarlo; no crecer mas rapido que la capacidad operativa.
**Severity_Level:** High
**Related_Patterns:** FIN-039, FIN-112, FIN-126

### FIN-129
**Pattern_Name:** Profitable Growth Capacity Assessment Missing
**Category:** Profitable Growth
**Description:** La empresa no evalua si el crecimiento proyectado es rentable, creciendo por crecer sin analisis de viabilidad economica.
**Observable_Symptoms:** Crecimiento sin plan financiero; no se evalua el retorno de nuevas inversiones; crecimiento por presion competitiva.
**Early_Warning_Signals:** Ausencia de proyecciones financieras de crecimiento; falta de analisis de economia unitaria; decisiones de expansion sin VAN o TIR.
**Typical_Causes:** Cultura de growth at all costs; falta de sofisticacion financiera; dueño impulsivo; presion del mercado.
**Business_Impact:** Crecimiento no rentable que destruye valor; sorpresas de perdidas; necesidad de financiamiento imprevisto.
**Metrics_To_Check:** Existencia de proyecciones financieras; Proyectos con evaluacion economica; % de crecimiento con VAN positivo.
**Diagnostic_Questions:** Has proyectado el impacto financiero de tu plan de crecimiento? Sabes si crecer va a mejorar o empeorar tu situacion financiera?
**Recommended_Actions:** Modelar financieramente el crecimiento antes de ejecutarlo; evaluar economia unitaria; establecer KPIs de rentabilidad del crecimiento.
**Severity_Level:** High
**Related_Patterns:** FIN-003, FIN-121, FIN-127

### FIN-130
**Pattern_Name:** Sustainable Growth Rate Exceeded
**Category:** Profitable Growth
**Description:** La empresa crece a una tasa superior a su tasa de crecimiento sostenible (SGR), generando tension financiera.
**Observable_Symptoms:** Crecimiento rapido pero tension de caja; necesidad constante de financiamiento; proveedores presionando.
**Early_Warning_Signals:** Crecimiento real > SGR calculada; crecimiento > ROE x (1 - ratio de dividendos); financiamiento externo creciendo mas que ventas.
**Typical_Causes:** Crecimiento acelerado no planificado; falta de capital para financiar crecimiento; optimismo excesivo.
**Business_Impact:** Riesgo de iliquidez por crecer muy rapido; necesidad de financiamiento forzoso; posible colapso.
**Metrics_To_Check:** SGR = ROE x (1 - Dividend Payout Ratio); Crecimiento real vs SGR; Financiamiento externo / Crecimiento.
**Diagnostic_Questions:** Cual es tu tasa de crecimiento sostenible sin necesidad de nuevo capital? Estas creciendo por encima?
**Recommended_Actions:** Moderar crecimiento al nivel sostenible; aumentar ROE o retener utilidades para aumentar SGR; conseguir capital de crecimiento.
**Severity_Level:** High
**Related_Patterns:** FIN-003, FIN-041, FIN-126

### FIN-131
**Pattern_Name:** Growth Strategy Without Exit Plan
**Category:** Profitable Growth
**Description:** La empresa crece sin una estrategia clara de salida o generacion de valor para los accionistas, atrapando el capital.
**Observable_Symptoms:** Dueño invierte todo en crecer sin saber como recuperar su inversion; crecimiento no se traduce en liquidez para accionistas.
**Early_Warning_Signals:** Sin plan de salida; reinversion total de utilidades; dueño no recibe dividendos ni puede vender; empresa no preparada para venta.
**Typical_Causes:** Falta de planificacion estrategica; dueño emocionalmente atado; crecimiento como fin en si mismo.
**Business_Impact:** Dueño tiene todo su patrimonio atado; imposibilidad de retirarse; empresa crece pero el dueño no materializa valor.
**Metrics_To_Check:** Dividendos / Utilidad Neta; Plan de salida documentado; Interes de compradores potenciales; Preparacion para due diligence.
**Diagnostic_Questions:** Cual es tu plan para recuperar el valor que estas generando? Como los accionistas van a materializar el valor creado?
**Recommended_Actions:** Desarrollar plan de salida (venta, fusion, IPO, transicion familiar, dividendos); preparar empresa para ser vendible; balancear crecimiento con distribucion.
**Severity_Level:** Medium
**Related_Patterns:** FIN-034, FIN-086, FIN-089

### FIN-132
**Pattern_Name:** Growth Trajectory Unsustainable
**Category:** Profitable Growth
**Description:** La trayectoria actual de crecimiento no es sostenible financieramente en el mediano plazo dados los recursos disponibles.
**Observable_Symptoms:** Crecimiento que requiere cada vez mas capital; margenes que no mejoran con escala; dependencia de financiamiento externo creciente.
**Early_Warning_Signals:** Tasa de crecimiento > 2x la tasa de crecimiento de la industria; necesidad de capital > EBITDA; relacion deuda/EBITDA empeorando.
**Typical_Causes:** Crecimiento insostenible por falta de capital, mercado limitado o modelo de negocio no escalable; falta de realismo.
**Business_Impact:** Eventual colapso por falta de financiamiento; crisis cuando el crecimiento se detenga; empresa sobredimensionada.
**Metrics_To_Check:** Tasa de crecimiento vs SGR; Deuda/EBITDA tendencia; Capital requerido para crecer; TAM vs ventas actuales.
**Diagnostic_Questions:** Tu ritmo de crecimiento es sostenible con los recursos actuales? Cuanto tiempo mas puedes mantener este ritmo?
**Recommended_Actions:** Moderar crecimiento; asegurar financiamiento de LP; validar que el mercado soporte el crecimiento proyectado; revisar supuestos del plan de crecimiento.
**Severity_Level:** Critical
**Related_Patterns:** FIN-003, FIN-126, FIN-130
