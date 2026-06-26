# Strategy_Patterns.md

**File:** Strategy_Patterns.md
**Description:** Patrones de estrategia corporativa para PyMEs — diagnóstico y formulación estratégica basados en Porter, Martin, McKinsey, BCG, Bain, EOS y Scaling Up.
**Total Patterns:** 132 (STR-001 a STR-132)
**Categories:** 11
**Version:** 1.0

---

## Summary Table

| Category | Pattern IDs | Count | Description |
|---|---|---|---|
| Crecimiento | STR-001 a STR-012 | 12 | Estrategias y problemas de crecimiento orgánico |
| Diversificación | STR-013 a STR-024 | 12 | Expansión a nuevos productos, mercados o negocios |
| Posicionamiento | STR-025 a STR-036 | 12 | Propuesta de valor, segmentación y diferenciación |
| Ventajas Competitivas | STR-037 a STR-048 | 12 | Fuentes de ventaja y erosión competitiva |
| Innovación | STR-049 a STR-060 | 12 | Estrategia de innovación, I+D y disrupción |
| Expansión | STR-061 a STR-072 | 12 | Crecimiento geográfico, de capacidad o canales |
| Internacionalización | STR-073 a STR-084 | 12 | Entrada y operación en mercados internacionales |
| Fusiones y Adquisiciones | STR-085 a STR-096 | 12 | M&A, integración y sinergias |
| Asignación de Recursos | STR-097 a STR-108 | 12 | Capital, talento y tiempo en iniciativas estratégicas |
| Prioridades Estratégicas | STR-109 a STR-120 | 12 | Enfoque, trade-offs y concentración estratégica |
| Ejecución Estratégica | STR-121 a STR-132 | 12 | Implementación, seguimiento y cascada de objetivos |

---

# Patrones de Estrategia

## Crecimiento

### STR-001
**Pattern_Name:** Crecimiento por Debajo del Potencial de Mercado
**Category:** Crecimiento
**Description:** La empresa crece a una tasa inferior a la del mercado en el que participa, perdiendo participación sistemáticamente y dejando oportunidades sin capturar.
**Typical_Causes:** Falta de ambición estratégica; capacidad limitada; inversión insuficiente; ejecución comercial débil; producto no competitivo.
**Observable_Symptoms:** El mercado crece más que la empresa; participación decreciente; competidores capturan el crecimiento; metas moderadas; conformismo.
**Early_Warning_Signals:** Crecimiento empresa < crecimiento mercado por 2+ años; pérdida de market share > 1% anual; gap de crecimiento vs competidores > 5%.
**Business_Impact:** Pérdida de relevancia; menor economía de escala; presión competitiva; menores ingresos futuros; eventual marginación.
**Severity_Level:** Critical
**Metrics_To_Check:** Tasa de crecimiento empresa vs mercado; market share; CAGR relativo; gap de crecimiento.
**Diagnostic_Questions:** ¿La empresa crece al ritmo del mercado? ¿Está perdiendo participación? ¿Los competidores crecen más? ¿Hay potencial no aprovechado?
**Recommended_Actions:** Elevar ambición de crecimiento; invertir en capacidad; fortalecer propuesta de valor; capturar cuota agresivamente; monitorear market share.
**Related_Patterns:** STR-005, STR-006, STR-009, STR-033, STR-109

### STR-002
**Pattern_Name:** Crecimiento No Rentable
**Category:** Crecimiento
**Description:** La empresa crece en ingresos pero no en utilidades, generando más volumen sin rentabilidad proporcional, deteriorando el negocio al escalar.
**Typical_Causes:** Descuentos agresivos para ganar volumen; costos fijos crecen más que ingresos; mix de ventas hacia productos de bajo margen; ineficiencias al escalar.
**Observable_Symptoms:** Ventas suben, utilidades bajan; margen decreciente con crecimiento; más trabajo para igual ganancia; desesperación por volumen.
**Early_Warning_Signals:** Margen neto decreciente 3+ trimestres con ventas crecientes; EBITDA/ventas en descenso; punto de equilibrio sube más que ventas.
**Business_Impact:** Empresa "grande pero pobre"; menor rentabilidad sobre capital; flujo de caja débil; insostenibilidad; menor valor empresarial.
**Severity_Level:** Critical
**Metrics_To_Check:** Margen neto vs crecimiento; EBITDA margin trend; ROIC; ventas vs utilidad neta.
**Diagnostic_Questions:** ¿El crecimiento es rentable? ¿Las utilidades crecen con las ventas? ¿Hay descuentos excesivos? ¿El costo de crecer es sostenible?
**Recommended_Actions:** Priorizar rentabilidad sobre volumen; revisar pricing; optimizar mix de ventas; controlar costos de crecimiento; abandonar clientes no rentables.
**Related_Patterns:** STR-001, STR-004, STR-009, STR-098, STR-110

### STR-003
**Pattern_Name:** Crecimiento sin Infraestructura
**Category:** Crecimiento
**Description:** La empresa crece sin desarrollar la infraestructura (procesos, sistemas, talento, capacidad) necesaria para soportar el nuevo tamaño, generando caos operativo.
**Typical_Causes:** Crecimiento reactivo; falta de planificación; subestimación de necesidades; priorizar ventas sobre operaciones; optimismo.
**Observable_Symptoms:** La operación se vuelve caótica al crecer; calidad cae; plazos se alargan; errores aumentan; empleados desbordados; clientes insatisfechos.
**Early_Warning_Signals:** Crecimiento de ventas > 30% sin aumento de capacidad; quejas de calidad crecientes; rotación aumenta; horas extra se disparan.
**Business_Impact:** Caos operativo; pérdida de calidad; clientes insatisfechos; daño reputacional; crisis de crecimiento; posible colapso.
**Severity_Level:** Critical
**Metrics_To_Check:** Crecimiento vs inversión en infraestructura; capacidad utilizada; incidencia de errores; satisfacción de clientes; rotación.
**Diagnostic_Questions:** ¿La infraestructura soporta el crecimiento? ¿Hay inversión en capacidad? ¿La calidad se mantiene? ¿El equipo está desbordado?
**Recommended_Actions:** Invertir en infraestructura antes de crecer; planificar crecimiento; fortalecer procesos; contratar talento; sistemas; escalar gradualmente.
**Related_Patterns:** STR-001, STR-002, STR-008, STR-061, STR-107

### STR-004
**Pattern_Name:** Dependencia del Crecimiento de un Solo Cliente
**Category:** Crecimiento
**Description:** El crecimiento de la empresa depende en gran medida de un único cliente grande, exponiéndola a un riesgo extremo si ese cliente reduce su demanda o se pierde.
**Typical_Causes:** Estrategia de "cuenta ancla"; falta de diversificación; cliente grande exige exclusividad; incapacidad para atraer otros clientes.
**Observable_Symptoms:** Un cliente representa la mayor parte del crecimiento; sin ese cliente, la empresa no crece; el cliente tiene poder de negociación excesivo.
**Early_Warning_Signals:** % de crecimiento atribuible al principal cliente > 60%; concentración de ingresos > 30% en un cliente; dependencia de relación personal.
**Business_Impact:** Vulnerabilidad extrema; poder del cliente sobre precios; riesgo existencial si se pierde; imposibilidad de planificar.
**Severity_Level:** Critical
**Metrics_To_Check:** % de crecimiento del mayor cliente; % de ingresos concentrados; índice de concentración; poder de negociación del cliente.
**Diagnostic_Questions:** ¿El crecimiento depende de un cliente? ¿Qué pasa si se reduce? ¿Hay diversificación? ¿El cliente tiene poder sobre la empresa?
**Recommended_Actions:** Diversificar base de clientes; limitar dependencia; desarrollar nuevas cuentas; fortalecer relación sin dependencia; planificar mitigación.
**Related_Patterns:** STR-001, STR-005, STR-009, STR-014, STR-034

### STR-005
**Pattern_Name:** Crecimiento por Adquisición de Clientes No Rentables
**Category:** Crecimiento
**Description:** La empresa crece adquiriendo clientes cuyo costo de adquisición supera el valor de vida, generando crecimiento ilusorio que destruye valor.
**Typical_Causes:** Falta de análisis CAC vs LTV; presión por crecer; marketing ineficiente; targeting incorrecto; descuentos excesivos para atraer.
**Observable_Symptoms:** Muchos clientes nuevos pero baja rentabilidad; CAC alto y creciente; clientes no repiten; bajo LTV; esfuerzo comercial no reditúa.
**Early_Warning_Signals:** CAC > LTV en 12 meses; payback period > 18 meses; % de clientes que repiten < 20%; CAC creciente.
**Business_Impact:** Crecimiento destructor de valor; quema de caja; rentabilidad negativa; insostenibilidad; dependencia de financiación externa.
**Severity_Level:** Critical
**Metrics_To_Check:** CAC; LTV; ratio LTV/CAC; payback period; tasa de retención; rentabilidad por cliente.
**Diagnostic_Questions:** ¿El costo de adquirir clientes es menor que su valor? ¿Los clientes nuevos son rentables? ¿Cuánto tardan en pagar su adquisición? ¿Repiten?
**Recommended_Actions:** Medir CAC y LTV rigurosamente; optimizar targeting; mejorar retención; reducir CAC; abandonar segmentos no rentables.
**Related_Patterns:** STR-002, STR-004, STR-009, STR-098, STR-110

### STR-006
**Pattern_Name:** Crecimiento por Copia de Competidores
**Category:** Crecimiento
**Description:** La empresa crece imitando a competidores en lugar de desarrollar su propia estrategia, resultando en un crecimiento reactivo sin diferenciación sostenible.
**Typical_Causes:** Falta de estrategia propia; miedo a innovar; falta de confianza; cultura de imitación; aversión al riesgo.
**Observable_Symptoms:** La empresa siempre sigue al competidor; lanza copias tardías; no hay iniciativa propia; diferenciación nula; siempre un paso atrás.
**Early_Warning_Signals:** % de iniciativas que son reacción a competidores > 60%; % de innovación propia < 10%; tiempo de reacción > 6 meses; imitación.
**Business_Impact:** Diferenciación nula; competencia por precio; márgenes reducidos; siempre reactivo; liderazgo ausente; vulnerabilidad estratégica.
**Severity_Level:** High
**Metrics_To_Check:** % de iniciativas propias vs reactivas; time-to-market de imitaciones; diferenciación percibida; margen relativo a competidores.
**Diagnostic_Questions:** ¿La empresa lidera o sigue? ¿Copia o innova? ¿Tiene estrategia propia? ¿Se diferencia? ¿Reacciona o anticipa?
**Recommended_Actions:** Desarrollar estrategia propia; invertir en innovación; dejar de mirar al competidor; enfocarse en el cliente; construir diferenciación real.
**Related_Patterns:** STR-001, STR-009, STR-025, STR-037, STR-049

### STR-007
**Pattern_Name:** Crecimiento sin Modelo de Negocio Escalable
**Category:** Crecimiento
**Description:** El modelo de negocio requiere incrementos proporcionales de recursos para crecer (no escalable), haciendo que cada unidad adicional de ingreso cueste casi lo mismo que genera.
**Typical_Causes:** Negocio basado en servicios intensivos en personas; falta de apalancamiento tecnológico; proceso artesanal; modelo no estandarizado.
**Observable_Symptoms:** Para crecer 20% hay que contratar 20% más personal; márgenes no mejoran con escala; ineficiencias persistentes; apalancamiento operativo nulo.
**Early_Warning_Signals:** % de gastos variables vs fijos > 70%; margen incremental similar al margen actual; ROIC no mejora con crecimiento.
**Business_Impact:** Escalabilidad limitada; crecimiento poco rentable; límite al tamaño; competidores con modelos escalables ganan; menor valoración.
**Severity_Level:** High
**Metrics_To_Check:** Apalancamiento operativo; margen incremental; ROIC; % de costos variables; productividad por empleado al crecer.
**Diagnostic_Questions:** ¿El modelo es escalable? ¿Cada peso de ingreso extra requiere casi un peso de costo? ¿Hay apalancamiento? ¿La rentabilidad mejora con escala?
**Recommended_Actions:** Buscar apalancamiento tecnológico; estandarizar; automatizar; crear productos escalables; revisar modelo de negocio; franquiciar.
**Related_Patterns:** STR-002, STR-003, STR-009, STR-049, STR-107

### STR-008
**Pattern_Name:** Crecimiento Apalancado Excesivamente
**Category:** Crecimiento
**Description:** La empresa financia su crecimiento principalmente con deuda, generando un alto riesgo financiero si el crecimiento se desacelera o no genera el retorno esperado.
**Typical_Causes:** Falta de capital propio; impaciencia por crecer; disponibilidad de crédito; subestimación de riesgos; optimismo en proyecciones.
**Observable_Symptoms:** Deuda crece con el crecimiento; servicio de deuda consume caja; covenants ajustados; vulnerabilidad a desaceleración.
**Early_Warning_Signals:** Deuda/EBITDA > 4x; cobertura de intereses < 2x; crecimiento financiado con deuda > 60%; apalancamiento creciente.
**Business_Impact:** Riesgo financiero alto; vulnerabilidad a shocks; menor flexibilidad; costo financiero elevado; posible default.
**Severity_Level:** High
**Metrics_To_Check:** Deuda/EBITDA; cobertura de intereses; % de crecimiento financiado con deuda; apalancamiento.
**Diagnostic_Questions:** ¿El crecimiento se financia con deuda? ¿El nivel de deuda es sostenible? ¿Hay margen ante desaceleración? ¿Los covenants están cómodos?
**Recommended_Actions:** Balancear deuda con capital; buscar inversores; generar caja; crecer a ritmo sostenible; reducir apalancamiento.
**Related_Patterns:** STR-002, STR-003, STR-009, STR-098, STR-107

### STR-009
**Pattern_Name:** Crecimiento sin Estrategia de Salida o Reinversión
**Category:** Crecimiento
**Description:** La empresa crece sin definir cómo capturará valor del crecimiento (salida, dividendos, reinversión), generando incertidumbre sobre el propósito del crecimiento.
**Typical_Causes:** Falta de visión de largo plazo; dueños sin acuerdo; "crecer por crecer"; no planificación estratégica; modelo de negocio sin definición de salida.
**Observable_Symptoms:** Se crece pero no se sabe para qué; no hay plan de salida; dueños no acuerdan si reinvertir o distribuir; conflictos sobre uso de utilidades.
**Early_Warning_Signals:** Sin definición de propósito del crecimiento; sin plan de salida; % de utilidades reinvertidas no definido; desacuerdo entre socios.
**Business_Impact:** Crecimiento sin dirección; conflictos entre socios; decisiones inconsistentes; posible parálisis; pérdida de oportunidades de salida.
**Severity_Level:** Medium
**Metrics_To_Check:** % de utilidades reinvertidas; claridad del plan de salida; alineación de socios; horizonte de inversión.
**Diagnostic_Questions:** ¿Para qué se crece? ¿Hay plan de salida? ¿Los socios están alineados? ¿Se reinvierte o distribuye? ¿Hay acuerdo sobre el propósito?
**Recommended_Actions:** Definir propósito del crecimiento; alinear socios; crear plan de salida o reinversión; establecer política de dividendos; comunicar.
**Related_Patterns:** STR-001, STR-002, STR-008, STR-098, STR-110

### STR-010
**Pattern_Name:** Crecimiento por Precios Bajos sin Ventaja en Costos
**Category:** Crecimiento
**Description:** La empresa crece compitiendo por precio sin tener una estructura de costos que lo soporte, erosionando márgenes y generando pérdidas a largo plazo.
**Typical_Causes:** Estrategia de precio bajo sin base; presión competitiva; falta de diferenciación; desesperación por volumen; subestimación de costos.
**Observable_Symptoms:** Precios por debajo de competidores; márgenes muy ajustados; volumen alto, utilidad baja; clientes sensibles al precio.
**Early_Warning_Signals:** Margen bruto < promedio sectorial; elasticidad precio alta; % de clientes que compran solo por precio > 60%; sin ventaja de costos.
**Business_Impact:** Rentabilidad insuficiente; insostenibilidad; guerra de precios; dificultad para invertir; dependencia de volumen; baja valoración.
**Severity_Level:** Critical
**Metrics_To_Check:** Margen bruto vs sector; estructura de costos vs competidores; % de clientes precio-sensibles; elasticidad precio.
**Diagnostic_Questions:** ¿Se compite por precio? ¿Hay ventaja de costos real? ¿El margen es saludable? ¿Los clientes son leales o solo buscan precio?
**Recommended_Actions:** Desarrollar ventaja en costos; diferenciar para reducir sensibilidad precio; segmentar; abandonar segmentos no rentables; mejorar eficiencia.
**Related_Patterns:** STR-002, STR-006, STR-037, STR-040, STR-043

### STR-011
**Pattern_Name:** Crecimiento sin Métricas de Performance
**Category:** Crecimiento
**Description:** La empresa crece sin medir indicadores clave de desempeño estratégico, operando a ciegas sin saber si el crecimiento es saludable o problemático.
**Typical_Causes:** Falta de cultura de métricas; desconocimiento; informalidad; liderazgo reactivo; ausencia de KPIs.
**Observable_Symptoms:** No se miden márgenes por línea; no hay CAC/LTV; no se conoce rentabilidad por cliente; no hay dashboard; decisiones sin datos.
**Early_Warning_Signals:** % de decisiones basadas en datos < 30%; sin dashboard estratégico; % de KPIs clave medidos < 30%; informalidad métrica.
**Business_Impact:** Crecimiento a ciegas; problemas no detectados; imposibilidad de corregir rumbo; decisiones subjetivas; eficiencia subóptima.
**Severity_Level:** High
**Metrics_To_Check:** % de KPIs estratégicos medidos; % de decisiones basadas en datos; existencia de dashboard; periodicidad de revisión.
**Diagnostic_Questions:** ¿Se miden indicadores de crecimiento? ¿Hay dashboard? ¿Las decisiones se basan en datos? ¿Se conoce la rentabilidad por cliente?
**Recommended_Actions:** Implementar dashboard estratégico; definir KPIs clave (crecimiento, rentabilidad, eficiencia); revisar mensualmente; capacitar en uso de datos.
**Related_Patterns:** STR-002, STR-004, STR-005, STR-098, STR-121

### STR-012
**Pattern_Name:** Crecimiento sin Cultura Organizacional Escalable
**Category:** Crecimiento
**Description:** La empresa crece sin desarrollar una cultura que soporte el nuevo tamaño, diluyendo los valores, la cohesión y la identidad a medida que se incorporan más personas.
**Typical_Causes:** Falta de atención a cultura; contratación masiva sin integrar; liderazgo no gestiona cultura; crecimiento diluye valores.
**Observable_Symptoms:** Los nuevos empleados no comparten los valores; la cultura se diluye; falta de cohesión; comportamiento inconsistente; "ya no es como antes".
**Early_Warning_Signals:** % de nuevos empleados que identifican valores < 30%; eNPS decreciente con crecimiento; rotación aumenta; quejas sobre pérdida de cultura.
**Business_Impact:** Pérdida de identidad cultural; desalineación; rotación; dificultad para integrar; pérdida de ventajas culturales; clima deteriorado.
**Severity_Level:** High
**Metrics_To_Check:** eNPS por antigüedad; % de adherence a valores; rotación post-crecimiento; encuesta de cultura.
**Diagnostic_Questions:** ¿La cultura se mantiene al crecer? ¿Los nuevos empleados comparten valores? ¿Hay cohesión? ¿Se gestiona la cultura activamente?
**Recommended_Actions:** Definir y comunicar cultura explícitamente; integrar cultura en selección y onboarding; líderes como guardianes culturales; medir cultura.
**Related_Patterns:** STR-003, STR-009, STR-028, STR-036, STR-132

## Diversificación

### STR-013
**Pattern_Name:** Diversificación sin Competencias Centrales
**Category:** Diversificación
**Description:** La empresa se diversifica hacia negocios donde carece de competencias, conocimiento o ventajas, compitiendo en desventaja desde el inicio.
**Typical_Causes:** Oportunidad percibida; imitación; exceso de confianza; falta de análisis; subestimación de requerimientos.
**Observable_Symptoms:** El nuevo negocio no despega; falta conocimiento del sector; errores costosos; no hay ventaja competitiva; resultados pobres.
**Early_Warning_Signals:** % de nuevos negocios rentables < 30%; gap de competencias en nuevo negocio > 50%; tiempo para alcanzar rentabilidad > 3 años.
**Business_Impact:** Pérdida de inversión; distracción del negocio principal; daño reputacional; costos de oportunidad; fracaso estratégico.
**Severity_Level:** Critical
**Metrics_To_Check:** % de diversificaciones exitosas; retorno sobre capital invertido; tiempo a rentabilidad; brecha de competencias.
**Diagnostic_Questions:** ¿La empresa tiene competencias para el nuevo negocio? ¿Hay ventaja real? ¿Se investigó el sector? ¿Hay planes de aprendizaje?
**Recommended_Actions:** Diversificar hacia áreas de fortaleza; adquirir competencias; asociarse con quien las tenga; hacer pilotos; validar supuestos.
**Related_Patterns:** STR-014, STR-017, STR-022, STR-037, STR-049

### STR-014
**Pattern_Name:** Diversificación por Oportunidad no por Estrategia
**Category:** Diversificación
**Description:** La empresa se diversifica en nuevos negocios porque "surge la oportunidad" sin un marco estratégico, resultando en iniciativas dispersas sin sinergia.
**Typical_Causes:** Cultura oportunista; falta de estrategia; dueño que no dice que no; falta de disciplina estratégica; sesgo de "todo lo que brilla es oro".
**Observable_Symptoms:** Negocios diversos sin conexión; recursos dispersos; sin foco; el dueño diversifica por oportunidad; no hay criterios claros.
**Early_Warning_Signals:** % de negocios no relacionados > 50%; sin criterios de diversificación; iniciativas sin análisis estratégico; recursos atomizados.
**Business_Impact:** Falta de foco; recursos diluidos; sinergias nulas; dificultad de gestión; fracaso en múltiples frentes; pérdida de rumbo.
**Severity_Level:** High
**Metrics_To_Check:** % de negocios relacionados vs no relacionados; ROIC por negocio; sinergias entre negocios; concentración de recursos.
**Diagnostic_Questions:** ¿La diversificación responde a una estrategia? ¿Los negocios están relacionados? ¿Hay sinergias? ¿Hay criterios de diversificación? ¿Hay foco?
**Recommended_Actions:** Definir criterios de diversificación; evaluar cada iniciativa contra estrategia; buscar negocios relacionados o con ventaja; decir no.
**Related_Patterns:** STR-013, STR-016, STR-019, STR-022, STR-109

### STR-015
**Pattern_Name:** Canibalización entre Líneas de Negocio
**Category:** Diversificación
**Description:** Las nuevas líneas de negocio canibalizan las ventas de las existentes, sin generar crecimiento neto real, solo trasladando ingresos internamente.
**Typical_Causes:** Segmentación pobre; propuestas de valor superpuestas; falta de diferenciación entre líneas; crecimiento interno descoordinado.
**Observable_Symptoms:** Nueva línea crece a costa de la existente; ventas totales no aumentan; clientes migran internamente; conflicto entre equipos.
**Early_Warning_Signals:** % de ventas nuevas que provienen de canibalización > 40%; crecimiento neto < crecimiento bruto; conflictos entre líneas.
**Business_Impact:** Crecimiento ilusorio; recursos duplicados; conflictos internos; rentabilidad general no mejora; distracción.
**Severity_Level:** High
**Metrics_To_Check:** % de canibalización; crecimiento neto vs bruto; rentabilidad incremental; satisfacción de clientes por línea.
**Diagnostic_Questions:** ¿Las nuevas líneas canibalizan las existentes? ¿Hay crecimiento neto? ¿Hay diferenciación entre líneas? ¿Los segmentos son distintos?
**Recommended_Actions:** Diferenciar claramente las propuestas de valor; segmentar mercados; coordinar internally; considerar separar marcas; medir canibalización.
**Related_Patterns:** STR-014, STR-018, STR-025, STR-028, STR-030

### STR-016
**Pattern_Name:** Sobrediversificación y Pérdida de Foco
**Category:** Diversificación
**Description:** La empresa se diversifica en exceso, operando en demasiados negocios sin recursos suficientes para cada uno, perdiendo foco y competitividad.
**Typical_Causes:** Dueño quiere abarcar mucho; falta de disciplina; miedo a oportunidades perdidas; falta de priorización; ego.
**Observable_Symptoms:** Muchos negocios, ninguno excelente; recursos diluidos; falta de masa crítica en cada uno; gestión compleja; resultados mediocres.
**Early_Warning_Signals:** Número de líneas de negocio > capacidad de gestión; % de negocios con posición competitiva líder < 20%; ROIC promedio bajo.
**Business_Impact:** Falta de foco; competitividad débil en todos los frentes; complejidad de gestión; recursos insuficientes; rendimiento inferior.
**Severity_Level:** High
**Metrics_To_Check:** Número de líneas de negocio; % de negocios líderes en su mercado; ROIC por línea; concentración de ingresos en top 3.
**Diagnostic_Questions:** ¿Hay demasiados negocios? ¿Hay masa crítica en cada uno? ¿Alguno es líder? ¿Los recursos están muy dispersos? ¿Hay foco?
**Recommended_Actions:** Concentrar recursos en negocios clave; vender o cerrar negocios no estratégicos; simplificar portafolio; recuperar foco.
**Related_Patterns:** STR-014, STR-017, STR-020, STR-098, STR-109

### STR-017
**Pattern_Name:** Diversificación sin Plan de Integración
**Category:** Diversificación
**Description:** La empresa se diversifica (orgánicamente o por adquisición) sin planificar cómo integrar el nuevo negocio con las operaciones existentes, generando ineficiencias.
**Typical_Causes:** Subestimación de integración; falta de planificación; enfoque solo en el "deal"; cultura de "cada negocio por su lado".
**Observable_Symptoms:** El nuevo negocio opera en silo; no hay sinergias; duplicidad de funciones; ineficiencias; integración lenta o nula.
**Early_Warning_Signals:** % de sinergias capturadas < 30%; tiempo de integración > 2 años; duplicidad de funciones; falta de coordinación.
**Business_Impact:** Sinergias no materializadas; ineficiencias; costos duplicados; valor no capturado; fracaso de la diversificación.
**Severity_Level:** High
**Metrics_To_Check:** % de sinergias capturadas; tiempo de integración; costos de integración vs ahorros; eficiencia operativa post-diversificación.
**Diagnostic_Questions:** ¿Hay plan de integración? ¿Se capturan sinergias? ¿Hay duplicidad? ¿La integración avanza? ¿Hay coordinación?
**Recommended_Actions:** Desarrollar plan de integración detallado; asignar responsable; identificar y capturar sinergias; integrar funciones clave; medir avance.
**Related_Patterns:** STR-013, STR-014, STR-016, STR-085, STR-092

### STR-018
**Pattern_Name:** Extensión de Marca sin Coherencia
**Category:** Diversificación
**Description:** La empresa extiende su marca a productos/servicios muy diferentes sin coherencia con el posicionamiento original, confundiendo clientes y diluyendo la marca.
**Typical_Causes:** Deseo de aprovechar marca; falta de análisis; subestimación del valor de marca; estrategia de marca pobre.
**Observable_Symptoms:** Clientes confundidos con la extensión; la nueva línea no encaja; marca se diluye; posicionamiento se debilita; ventas por debajo de expectativas.
**Early_Warning_Signals:** % de clientes que entienden la extensión < 30%; % de rechazo por incoherencia; dilución de marca principal; confusión.
**Business_Impact:** Dilución de marca; pérdida de posicionamiento; confusión del cliente; fracaso de la extensión; daño a marca principal.
**Severity_Level:** High
**Metrics_To_Check:** Reconocimiento de extensión; coherencia percibida; impacto en marca principal; ventas de extensión.
**Diagnostic_Questions:** ¿La extensión de marca tiene coherencia? ¿Los clientes la entienden? ¿La marca principal se diluye? ¿Hay riesgo de dañar la marca?
**Recommended_Actions:** Evaluar coherencia de extensión con marca; usar marcas separadas si es necesario; investigar percepción; mantener posicionamiento claro.
**Related_Patterns:** STR-015, STR-025, STR-028, STR-031, STR-073

### STR-019
**Pattern_Name:** Diversificación por Huida del Negocio Principal
**Category:** Diversificación
**Description:** La empresa se diversifica para escapar de problemas en el negocio principal (mercado maduro, baja rentabilidad) en lugar de arreglarlos, creando negocios nuevos sin resolver los viejos.
**Typical_Causes:** Evitación de problemas difíciles; falta de innovación en core; desgaste; búsqueda de "pastos más verdes"; complejidad del negocio principal.
**Observable_Symptoms:** Se invierte en nuevos negocios mientras el core se descuida; los problemas del core no se resuelven; el core sigue deteriorándose.
**Early_Warning_Signals:** Inversión en nuevos negocios > inversión en core; core perdiendo competitividad; % de tiempo gerencial dedicado a core < 30%.
**Business_Impact:** Core se debilita; nuevos negocios no compensan; ambos frentes débiles; pérdida de competitividad general; posible crisis.
**Severity_Level:** Critical
**Metrics_To_Check:** Inversión en core vs nuevos negocios; rentabilidad del core; % de atención gerencial al core; salud del negocio principal.
**Diagnostic_Questions:** ¿La diversificación es para huir del core? ¿Se está descuidando el negocio principal? ¿Los problemas del core se están resolviendo?
**Recommended_Actions:** Resolver problemas del core antes de diversificar; invertir en revitalizar core; equilibrar atención; considerar si el core es rescatable.
**Related_Patterns:** STR-013, STR-014, STR-016, STR-033, STR-049

### STR-020
**Pattern_Name:** Portafolio de Negocios sin Matriz Estratégica
**Category:** Diversificación
**Description:** La empresa no utiliza herramientas de portafolio (BCG, GE-McKinsey) para evaluar sus unidades de negocio, asignando recursos sin criterio de potencial y posición.
**Typical_Causes:** Desconocimiento; falta de planificación; cultura de "tratar todos por igual"; ausencia de análisis de portafolio.
**Observable_Symptoms:** Todos los negocios reciben recursos similares; no se identifican "estrellas" ni "vacas"; no hay decisiones de desinversión; inercia.
**Early_Warning_Signals:** Sin matriz de portafolio; % de recursos asignados sin análisis; % de negocios con estrategia diferenciada < 30%; inercia.
**Business_Impact:** Recursos mal asignados; oportunidades perdidas; negocios malos mantienen inversión; buenos negocios subinvertidos; rentabilidad subóptima.
**Severity_Level:** High
**Metrics_To_Check:** % de recursos asignados con análisis de portafolio; % de negocios con estrategia clara; ROIC por unidad.
**Diagnostic_Questions:** ¿Se analiza el portafolio de negocios? ¿Hay matriz BCG o similar? ¿Los recursos se asignan según potencial? ¿Hay decisiones de desinversión?
**Recommended_Actions:** Implementar análisis de portafolio (BCG, GE-McKinsey); clasificar negocios; asignar recursos según estrategia; desinvertir en negocios débiles.
**Related_Patterns:** STR-016, STR-017, STR-098, STR-100, STR-109

### STR-021
**Pattern_Name:** Sinergias no Capturadas entre Unidades
**Category:** Diversificación
**Description:** Las diferentes unidades de negocio operan de forma independiente sin capturar sinergias potenciales (compras, clientes, conocimiento), perdiendo eficiencias.
**Typical_Causes:** Silos; falta de incentivos a colaboración; cultura independiente; falta de integración; medición por unidad sin visión global.
**Observable_Symptoms:** Unidades compran por separado; comparten clientes pero no coordinan; conocimiento no fluye; duplicidad de funciones.
**Early_Warning_Signals:** % de sinergias potenciales capturadas < 20%; % de compras consolidadas < 30%; % de clientes compartidos sin coordinación.
**Business_Impact:** Ineficiencias; costos más altos; oportunidades de cross-selling perdidas; duplicidad; menor rentabilidad global.
**Severity_Level:** High
**Metrics_To_Check:** % de sinergias capturadas; ahorros por sinergias; % de cross-selling; eficiencia operativa global.
**Diagnostic_Questions:** ¿Hay sinergias entre unidades? ¿Se compran juntos? ¿Se comparten clientes? ¿Hay duplicidad? ¿Hay incentivos a colaborar?
**Recommended_Actions:** Identificar sinergias potenciales; crear incentivos a colaboración; centralizar compras; integrar CRM; medir y recompensar sinergias.
**Related_Patterns:** STR-014, STR-016, STR-017, STR-085, STR-092

### STR-022
**Pattern_Name:** Diversificación en Negocios Regulados sin Expertise
**Category:** Diversificación
**Description:** La empresa se diversifica hacia sectores altamente regulados (salud, finanzas, alimentos) sin conocimiento del marco regulatorio, exponiéndose a sanciones y fracasos.
**Typical_Causes:** Oportunidad percibida; subestimación de regulación; falta de asesoría; optimismo; desconocimiento del sector.
**Observable_Symptoms:** Incumplimientos regulatorios; multas; retrasos por permisos; costos de cumplimiento no presupuestados; fracaso del nuevo negocio.
**Early_Warning_Signals:** % de requisitos regulatorios identificados < 40%; sin asesoría regulatoria; multas; retrasos por permisos.
**Business_Impact:** Multas; sanciones; cierre del negocio; pérdida de inversión; daño reputacional; distracción gerencial.
**Severity_Level:** Critical
**Metrics_To_Check:** % de cumplimiento regulatorio en nuevo negocio; multas; costos de cumplimiento vs presupuesto; tiempo de obtención de permisos.
**Diagnostic_Questions:** ¿Se conoce la regulación del sector? ¿Hay asesoría? ¿Se presupuestaron costos de cumplimiento? ¿Hay multas?
**Recommended_Actions:** Investigar marco regulatorio antes de diversificar; contratar asesoría especializada; presupuestar cumplimiento; evaluar viabilidad regulatoria.
**Related_Patterns:** STR-013, STR-014, STR-032, STR-073, STR-077

### STR-023
**Pattern_Name:** Diversificación sin Análisis de Barreras de Entrada
**Category:** Diversificación
**Description:** La empresa ingresa a nuevos negocios sin evaluar las barreras de entrada, enfrentando obstáculos insuperables que impiden competir efectivamente.
**Typical_Causes:** Falta de análisis; subestimación; exceso de confianza; no investigación de mercado; optimismo.
**Observable_Symptoms:** Dificultad para entrar; costos de entrada mayores a los previstos; competidores establecidos bloquean; resultados por debajo de lo esperado.
**Early_Warning_Signals:** % de barreras identificadas < 30%; sobrecosto de entrada > 50%; % de mercado capturado < 10% del objetivo; tiempo de entrada duplicado.
**Business_Impact:** Fracaso de entrada; pérdida de inversión; distracción; daño reputacional; costos irrecuperables.
**Severity_Level:** High
**Metrics_To_Check:** % de barreras identificadas; costo real vs presupuestado; tiempo de entrada; market share capturado; ROI del nuevo negocio.
**Diagnostic_Questions:** ¿Se evaluaron las barreras de entrada? ¿Son superables? ¿Hay costos ocultos? ¿Los competidores establecidos tienen ventajas insalvables?
**Recommended_Actions:** Evaluar barreras de entrada (capital, regulación, marcas, tecnología); planificar mitigación; considerar alianzas; si son insalvables, no entrar.
**Related_Patterns:** STR-013, STR-014, STR-022, STR-037, STR-073

### STR-024
**Pattern_Name:** Diversificación sin Capacidad de Gestión
**Category:** Diversificación
**Description:** La dirección no tiene la capacidad ni el ancho de banda para gestionar múltiples negocios, descuidando la operación y la estrategia de cada uno.
**Typical_Causes:** Dueño que abarca mucho; falta de delegación; equipo directivo pequeño; ausencia de gerentes por unidad; sobreconfianza.
**Observable_Symptoms:** Negocios descuidados; decisiones lentas; falta de atención; directivos desbordados; calidad de gestión cae; resultados mediocres.
**Early_Warning_Signals:** Número de unidades de negocio por directivo > 4; % de tiempo del dueño por unidad < 15%; quejas de falta de atención.
**Business_Impact:** Mala gestión de todos los negocios; resultados mediocres; oportunidades perdidas; fracaso de diversificación; desgaste directivo.
**Severity_Level:** High
**Metrics_To_Check:** Unidades de negocio por directivo; % de tiempo de atención por unidad; satisfacción con gestión por unidad; ROIC por unidad.
**Diagnostic_Questions:** ¿La dirección tiene capacidad para gestionar todos los negocios? ¿Hay gerentes por unidad? ¿Hay suficiente atención? ¿Están desbordados?
**Recommended_Actions:** Delegar gestión de unidades; contratar gerentes por negocio; simplificar portafolio; concentrar recursos; equilibrar capacidad directiva.
**Related_Patterns:** STR-013, STR-016, STR-024, STR-078, STR-109

## Posicionamiento

### STR-025
**Pattern_Name:** Propuesta de Valor Genérica o Poco Diferenciada
**Category:** Posicionamiento
**Description:** La empresa no tiene una propuesta de valor clara ni diferenciada, siendo percibida como "una más" y compitiendo únicamente por precio o disponibilidad.
**Typical_Causes:** Falta de definición estratégica; imitación; commodity sin diferenciación; no investigación de cliente; ausencia de posicionamiento.
**Observable_Symptoms:** Clientes no distinguen a la empresa; "son todos iguales"; compran por precio; la empresa no sabe por qué deberían preferirla.
**Early_Warning_Signals:** % de clientes que diferencian la propuesta < 30%; elasticidad precio alta; NPS bajo; sin propuesta de valor documentada.
**Business_Impact:** Competencia por precio; bajos márgenes; baja lealtad; commodity sin diferenciación; vulnerabilidad competitiva; crecimiento limitado.
**Severity_Level:** Critical
**Metrics_To_Check:** Diferenciación percibida; elasticidad precio; NPS; % de compras por precio; % de clientes que recomiendan.
**Diagnostic_Questions:** ¿Los clientes diferencian a la empresa? ¿Por qué deberían preferirla? ¿Hay propuesta de valor clara? ¿Se compite solo por precio?
**Recommended_Actions:** Definir propuesta de valor única; investigar clientes; diferenciar en servicio, calidad o experiencia; comunicar diferenciación.
**Related_Patterns:** STR-028, STR-033, STR-037, STR-040, STR-043

### STR-026
**Pattern_Name:** Posicionamiento Inconsistente entre Canales
**Category:** Posicionamiento
**Description:** El posicionamiento de la marca varía según el canal, mercado o segmento, generando confusión en los clientes y dilución de la identidad.
**Typical_Causes:** Falta de lineamientos de marca; descentralización de marketing; canales no coordinados; estrategia de marca débil.
**Observable_Symptoms:** Mensaje diferente en cada canal; clientes reciben señales mixtas; la marca se percibe diferente según dónde se vea; inconsistencia.
**Early_Warning_Signals:** % de canales con mensaje consistente < 40%; % de clientes que perciben inconsistencia > 30%; desalineación de comunicación.
**Business_Impact:** Confusión de marca; posicionamiento débil; pérdida de claridad; menor efectividad de marketing; clientes no retienen identidad.
**Severity_Level:** High
**Metrics_To_Check:** % de canales alineados; consistencia percibida; reconocimiento de marca; efectividad de comunicación.
**Diagnostic_Questions:** ¿El posicionamiento es consistente en todos los canales? ¿El mensaje es el mismo? ¿Los clientes reciben señales claras?
**Recommended_Actions:** Definir lineamientos de marca; centralizar estrategia de posicionamiento; capacitar canales; auditar consistencia.
**Related_Patterns:** STR-025, STR-028, STR-030, STR-031, STR-074

### STR-027
**Pattern_Name:** Segmentación de Mercado Inexistente o Incorrecta
**Category:** Posicionamiento
**Description:** La empresa no segmenta su mercado o lo hace incorrectamente, tratando a todos los clientes por igual y perdiendo oportunidades de adaptar su propuesta.
**Typical_Causes:** Desconocimiento; enfoque masivo; falta de datos; "nuestro producto es para todos"; comodidad; falta de análisis.
**Observable_Symptoms:** Estrategia única para todos; clientes muy diversos con necesidades distintas; falta de foco; recursos de marketing dispersos.
**Early_Warning_Signals:** % de ingresos de segmentos definidos < 30%; sin segmentación documentada; % de clientes en segmentos no rentables > 40%.
**Business_Impact:** Recursos mal asignados; propuesta no optimizada; oportunidades de nicho perdidas; clientes no atendidos adecuadamente; ineficiencia.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos por segmento; % de segmentos con estrategia diferenciada; rentabilidad por segmento; % de mercado no atendido.
**Diagnostic_Questions:** ¿Hay segmentación? ¿Los segmentos tienen estrategias distintas? ¿Todos reciben lo mismo? ¿Hay segmentos no atendidos?
**Recommended_Actions:** Segmentar mercado (geográfica, demográfica, conductual); adaptar propuesta por segmento; priorizar segmentos más rentables.
**Related_Patterns:** STR-025, STR-029, STR-033, STR-035, STR-038

### STR-028
**Pattern_Name:** Marca Débil o Poco Reconocida
**Category:** Posicionamiento
**Description:** La marca tiene bajo reconocimiento y recordación en el mercado, limitando su capacidad de atraer clientes, cobrar premium y generar lealtad.
**Typical_Causes:** Falta de inversión en marca; estrategia de marca débil; comunicación inconsistente; producto commodity; presupuesto insuficiente.
**Observable_Symptoms:** La marca no es conocida; clientes no la recuerdan; no hay reconocimiento espontáneo; bajo top of mind; dificultad para atraer.
**Early_Warning_Signals:** % de reconocimiento de marca < 30%; % de top of mind < 10%; % de clientes que llegan por marca < 20%; sin inversión en marca.
**Business_Impact:** Dificultad para atraer clientes; menor poder de precio; baja lealtad; costos de adquisición más altos; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** Reconocimiento de marca; top of mind; % de clientes por marca; inversión en marca/ventas; NPS.
**Diagnostic_Questions:** ¿La marca es conocida? ¿Los clientes la recuerdan? ¿Hay inversión en marca? ¿Tiene poder de atracción? ¿Es top of mind?
**Recommended_Actions:** Invertir en construcción de marca; estrategia de comunicación; publicidad; PR; marketing digital; consistencia; diferenciación.
**Related_Patterns:** STR-025, STR-026, STR-031, STR-040, STR-043

### STR-029
**Pattern_Name:** Targeting Incorrecto o No Rentable
**Category:** Posicionamiento
**Description:** La empresa dirige sus esfuerzos a segmentos de clientes que no son los más rentables o con menor potencial, desperdiciando recursos en segmentos equivocados.
**Typical_Causes:** Falta de análisis de rentabilidad por segmento; inercia histórica; targeting por volumen no por valor; comodidad.
**Observable_Symptoms:** Los segmentos que más atención reciben no son los más rentables; se invierte en clientes de bajo valor; los rentables están desatendidos.
**Early_Warning_Signals:** % de recursos invertidos en segmentos rentables < 40%; % de ingresos de segmentos objetivo < 50%; rentabilidad decreciente.
**Business_Impact:** Recursos mal asignados; rentabilidad subóptima; segmentos valiosos desatendidos; inversión en clientes no rentables.
**Severity_Level:** Critical
**Metrics_To_Check:** Rentabilidad por segmento; % de recursos por segmento; % de ingresos de segmentos prioritarios; ROI de marketing por segmento.
**Diagnostic_Questions:** ¿Se invierte en los segmentos correctos? ¿Los más rentables reciben más atención? ¿Hay segmentos no rentables que reciben muchos recursos?
**Recommended_Actions:** Analizar rentabilidad por segmento; priorizar segmentos de alto valor; reducir inversión en segmentos no rentables; reasignar recursos.
**Related_Patterns:** STR-027, STR-033, STR-035, STR-098, STR-110

### STR-030
**Pattern_Name:** Posicionamiento Premium sin Sustento
**Category:** Posicionamiento
**Description:** La empresa se posiciona como premium sin ofrecer calidad, servicio o experiencia que justifique el precio, generando expectativas incumplidas y clientes insatisfechos.
**Typical_Causes:** Deseo de márgenes altos; sobreestimación de la propuesta; falta de inversión en calidad; desconexión entre marketing y operación.
**Observable_Symptoms:** Precios altos pero calidad media; clientes se sienten estafados; reseñas negativas; brecha entre promesa y entrega; quejas.
**Early_Warning_Signals:** % de clientes que perciben valor por precio < 40%; % de quejas sobre relación precio-calidad; gap promesa-realidad > 30%.
**Business_Impact:** Insatisfacción; daño reputacional; pérdida de clientes; fracaso del posicionamiento premium; necesidad de bajar precios.
**Severity_Level:** Critical
**Metrics_To_Check:** % de clientes que perciben valor por precio; NPS; % de quejas por precio; gap promesa-realidad; calidad percibida.
**Diagnostic_Questions:** ¿La calidad justifica el precio premium? ¿Los clientes perciben valor? ¿Hay brecha entre promesa y realidad? ¿La operación soporta el posicionamiento?
**Recommended_Actions:** Alinear calidad con posicionamiento; mejorar producto/servicio; cerrar brecha promesa-realidad; si no se puede, ajustar posicionamiento.
**Related_Patterns:** STR-025, STR-028, STR-033, STR-040, STR-043

### STR-031
**Pattern_Name:** Estrategia de Marca sin Diferenciación Emocional
**Category:** Posicionamiento
**Description:** La marca se posiciona solo en atributos funcionales (precio, calidad, rapidez) sin conectar emocionalmente con el cliente, generando baja lealtad y conexión.
**Typical_Causes:** Estrategia funcional; falta de propósito de marca; desconocimiento de branding emocional; producto commodity; ausencia de storytelling.
**Observable_Symptoms:** Clientes compran por conveniencia no por preferencia; baja lealtad; fácil reemplazo; no hay defensores de marca; relación transaccional.
**Early_Warning_Signals:** % de clientes que recomiendan < 20%; % de compras emocionales vs funcionales < 20%; NPS bajo; sin propósito de marca.
**Business_Impact:** Baja lealtad; competencia por precio; clientes reemplazables; sin defensores; vulnerabilidad competitiva; menor valor de marca.
**Severity_Level:** High
**Metrics_To_Check:** % de recomendación; NPS; % de lealtad emocional; % de clientes defensores; conexión con marca.
**Diagnostic_Questions:** ¿La marca conecta emocionalmente? ¿Los clientes son leales o solo transaccionales? ¿Hay propósito de marca? ¿Hay defensores?
**Recommended_Actions:** Desarrollar propósito de marca; crear storytelling; conectar emocionalmente; construir comunidad; marketing aspiracional.
**Related_Patterns:** STR-025, STR-028, STR-030, STR-040, STR-043

### STR-032
**Pattern_Name:** Posicionamiento en Segmento de Bajo Crecimiento
**Category:** Posicionamiento
**Description:** La empresa está posicionada en un segmento de mercado estancado o en declive, limitando su potencial de crecimiento y enfrentando una competencia intensa por un mercado que se reduce.
**Typical_Causes:** Inercia; falta de análisis de tendencias; apego al segmento original; desconocimiento; resistencia a cambiar.
**Observable_Symptoms:** El segmento no crece; competencia intensa por participación; márgenes comprimidos; dificultad para crecer; perspectivas limitadas.
**Early_Warning_Signals:** Crecimiento del segmento < PIB; % de mercado en declive > 30%; márgenes decrecientes; competidores saliendo; dificultad para crecer.
**Business_Impact:** Crecimiento limitado; rentabilidad comprimida; futuro incierto; necesidad de reposicionamiento; inversión en segmento equivocado.
**Severity_Level:** High
**Metrics_To_Check:** Crecimiento del segmento; tamaño del mercado; tendencia de márgenes; % de competidores saliendo; potencial de crecimiento.
**Diagnostic_Questions:** ¿El segmento está creciendo? ¿Hay futuro? ¿Los márgenes se comprimen? ¿Hay competidores saliendo? ¿Es momento de reposicionarse?
**Recommended_Actions:** Reposicionarse en segmentos de crecimiento; diversificar; innovar para revitalizar segmento; considerar salida gradual.
**Related_Patterns:** STR-025, STR-027, STR-033, STR-049, STR-073

### STR-033
**Pattern_Name:** Falta de Análisis de la Competencia
**Category:** Posicionamiento
**Description:** La empresa no analiza sistemáticamente a sus competidores, desconociendo sus estrategias, fortalezas, debilidades y movimientos, operando en un vacío competitivo.
**Typical_Causes:** Arrogancia; falta de recursos; desconocimiento; cultura de "concentrarse en nosotros"; falta de inteligencia competitiva.
**Observable_Symptoms:** Movimientos de competidores toman por sorpresa; no se conoce el posicionamiento relativo; falta de benchmarking; decisiones desinformadas.
**Early_Warning_Signals:** Sin análisis de competidores; % de movimientos de competidores anticipados < 20%; sin benchmarking; información desactualizada.
**Business_Impact:** Decisiones estratégicas desinformadas; sorpresas competitivas; pérdida de posicionamiento; reacción tardía; desventaja.
**Severity_Level:** High
**Metrics_To_Check:** % de competidores analizados; % de movimientos anticipados; frecuencia de análisis; % de decisiones informadas por inteligencia competitiva.
**Diagnostic_Questions:** ¿Se analiza a los competidores? ¿Se anticipan sus movimientos? ¿Hay benchmarking? ¿Se conoce el posicionamiento relativo?
**Recommended_Actions:** Implementar inteligencia competitiva; analizar competidores regularmente; benchmarking; monitorear cambios; compartir inteligencia.
**Related_Patterns:** STR-025, STR-037, STR-038, STR-039, STR-043

### STR-034
**Pattern_Name:** Estrategia de Segmentación Única
**Category:** Posicionamiento
**Description:** La empresa utiliza la misma estrategia de marketing y propuesta de valor para todos los segmentos, sin adaptar su enfoque a las necesidades específicas de cada grupo.
**Typical_Causes:** Falta de segmentación; presupuesto limitado; estrategia masiva; desconocimiento; comodidad; creencia de "talla única".
**Observable_Symptoms:** El mismo mensaje para todos; clientes diversos reciben lo mismo; necesidades específicas no atendidas; efectividad limitada.
**Early_Warning_Signals:** % de segmentos con estrategia diferenciada < 20%; % de clientes que sienten que la oferta no es para ellos > 30%; baja conversión.
**Business_Impact:** Menor efectividad de marketing; clientes no se sienten comprendidos; oportunidades de nicho perdidas; rentabilidad subóptima.
**Severity_Level:** Medium
**Metrics_To_Check:** % de segmentos con estrategia diferenciada; efectividad por segmento; % de clientes objetivo alcanzados; ROI de marketing.
**Diagnostic_Questions:** ¿Se adapta la estrategia a cada segmento? ¿Todos reciben lo mismo? ¿Hay clientes desatendidos? ¿La efectividad varía por segmento?
**Recommended_Actions:** Desarrollar estrategias diferenciadas por segmento; adaptar mensaje, canal y oferta; priorizar segmentos de mayor potencial.
**Related_Patterns:** STR-027, STR-029, STR-033, STR-035, STR-074

### STR-035
**Pattern_Name:** Posicionamiento Atrapado en Medio (Stuck in the Middle)
**Category:** Posicionamiento
**Description:** La empresa intenta ser líder en costo y diferenciación simultáneamente sin lograr ninguna, quedando atrapada en una posición intermedia sin ventaja competitiva clara.
**Typical_Causes:** Falta de trade-offs estratégicos; querer complacer a todos; estrategia ambigua; falta de foco; no decidir.
**Observable_Symptoms:** La empresa no es la más barata ni la mejor; los clientes no saben por qué elegirla; precios medios, calidad media; sin identidad clara.
**Early_Warning_Signals:** % de clientes que identifican ventaja clara < 20%; precio relativo ni alto ni bajo; calidad relativa media; sin posicionamiento definido.
**Business_Impact:** Competencia desventajosa; sin clientes leales; márgenes medios; vulnerabilidad; crecimiento lento; falta de identidad estratégica.
**Severity_Level:** Critical
**Metrics_To_Check:** Posicionamiento relativo (precio vs calidad); % de clientes que identifican ventaja; margen relativo; claridad de estrategia.
**Diagnostic_Questions:** ¿La empresa es líder en costo, diferenciación o foco? ¿Tiene una ventaja clara? ¿Está atrapada en medio? ¿Hay trade-offs definidos?
**Recommended_Actions:** Elegir una estrategia genérica clara (liderazgo en costos, diferenciación o foco); hacer trade-offs; alinear toda la organización; comunicar.
**Related_Patterns:** STR-025, STR-030, STR-037, STR-040, STR-109

### STR-036
**Pattern_Name:** Estrategia de Posicionamiento no Comunicada Internamente
**Category:** Posicionamiento
**Description:** La estrategia de posicionamiento no se comunica ni se entiende dentro de la organización, por lo que el equipo no sabe cómo contribuir a ella ni qué decisiones tomar.
**Typical_Causes:** Falta de comunicación; estrategia en la cabeza del dueño; desconexión dirección-equipo; ausencia de cascada.
**Observable_Symptoms:** El equipo no sabe cuál es el posicionamiento; decisiones inconsistentes; acciones no alineadas con la estrategia; mensajes contradictorios.
**Early_Warning_Signals:** % de empleados que pueden describir el posicionamiento < 20%; % de decisiones alineadas con posicionamiento < 40%; inconsistencia.
**Business_Impact:** Desalineación organizacional; ejecución inconsistente; posicionamiento no se materializa; esfuerzos dispersos; estrategia en papel.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados que conocen el posicionamiento; % de decisiones alineadas; consistencia de ejecución; satisfacción con comunicación estratégica.
**Diagnostic_Questions:** ¿El equipo conoce el posicionamiento? ¿Las decisiones están alineadas? ¿La ejecución es consistente con la estrategia? ¿Se comunica?
**Recommended_Actions:** Comunicar posicionamiento a toda la organización; cascada de implicaciones por área; capacitar; decisiones consistentes.
**Related_Patterns:** STR-025, STR-028, STR-035, STR-046, STR-121

## Ventajas Competitivas

### STR-037
**Pattern_Name:** Ventaja Competitiva No Sostenible
**Category:** Ventajas Competitivas
**Description:** La ventaja competitiva actual es temporal (bajo precio, acceso a insumos, regulación favorable) y puede ser fácilmente replicada por competidores.
**Typical_Causes:** Ventaja basada en factores externos; falta de innovación; no inversión en barreras; commoditización; imitación fácil.
**Observable_Symptoms:** Competidores copian la ventaja; márgenes se comprimen; diferenciación se erosiona; la ventaja se desvanece.
**Early_Warning_Signals:** % de ventaja atribuible a factores sostenibles < 40%; tiempo para que competidores imiten < 12 meses; ventaja decreciente.
**Business_Impact:** Pérdida de competitividad; márgenes reducidos; necesidad de encontrar nueva ventaja; presión competitiva; erosión del negocio.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ventaja sostenible; tiempo de imitación; margen relativo; duración histórica de ventajas.
**Diagnostic_Questions:** ¿La ventaja es sostenible? ¿Los competidores pueden copiarla fácilmente? ¿Cuánto dura? ¿Hay barreras de imitación? ¿Se erosiona?
**Recommended_Actions:** Construir ventajas más profundas (marca, tecnología, red, escala); invertir en barreras; innovar continuamente; anticipar imitación.
**Related_Patterns:** STR-039, STR-040, STR-041, STR-043, STR-049

### STR-038
**Pattern_Name:** Ventaja Competitiva Basada solo en Precio
**Category:** Ventajas Competitivas
**Description:** La única ventaja competitiva de la empresa es el precio bajo, sin una estructura de costos que lo respalde sosteniblemente, generando una guerra de precios insostenible.
**Typical_Causes:** Falta de diferenciación; estrategia por defecto; presión competitiva; desesperación por volumen; competencia en commodity.
**Observable_Symptoms:** Clientes solo sensibles a precio; guerras de precios; márgenes mínimos; rentabilidad baja; alta elasticidad; clientes no leales.
**Early_Warning_Signals:** % de clientes que eligen por precio > 70%; margen bruto < 20%; % de descuentos sobre precio de lista > 30%; rotación de clientes alta.
**Business_Impact:** Rentabilidad insuficiente; insostenibilidad; imposibilidad de invertir; estrés financiero; dependencia de volumen; baja valoración.
**Severity_Level:** Critical
**Metrics_To_Check:** % de clientes por precio; margen bruto; elasticidad precio; lealtad de clientes; estructura de costos vs competidores.
**Diagnostic_Questions:** ¿La única ventaja es precio? ¿Hay ventaja de costos real? ¿Es sostenible? ¿Los clientes se irían por un precio menor?
**Recommended_Actions:** Desarrollar otras fuentes de diferenciación; buscar eficiencias de costos reales; segmentar; construir marca; reducir dependencia de precio.
**Related_Patterns:** STR-010, STR-025, STR-037, STR-039, STR-040

### STR-039
**Pattern_Name:** Erosión de Ventaja Competitiva por Falta de Inversión
**Category:** Ventajas Competitivas
**Description:** La empresa no invierte en mantener y renovar sus fuentes de ventaja competitiva, dejando que se deterioren frente a competidores que sí invierten.
**Typical_Causes:** Cortoplacismo; falta de visión; complacencia; ausencia de reinversión; priorizar distribución de utilidades.
**Observable_Symptoms:** La ventaja se debilita; competidores invierten y mejoran; la empresa se queda atrás; calidad o servicio declinan; pérdida de posicionamiento.
**Early_Warning_Signals:** Inversión en ventaja competitiva/ventas < 3%; % de ventaja perdida por falta de inversión; gap de inversión con competidores.
**Business_Impact:** Pérdida de competitividad; erosión de posicionamiento; menor participación; márgenes reducidos; necesidad de recuperación costosa.
**Severity_Level:** Critical
**Metrics_To_Check:** Inversión en ventaja competitiva; % de inversión vs competidores; % de ventaja mantenida; posición competitiva relativa.
**Diagnostic_Questions:** ¿Se invierte en mantener la ventaja? ¿Los competidores están invirtiendo más? ¿La ventaja se erosiona? ¿Hay complacencia?
**Recommended_Actions:** Reinvertir en fuentes de ventaja; presupuestar mantenimiento de posición competitiva; monitorear gap de inversión; no dormirse en laureles.
**Related_Patterns:** STR-037, STR-038, STR-041, STR-043, STR-078

### STR-040
**Pattern_Name:** Confusión entre Ventaja Competitiva y Capacidad
**Category:** Ventajas Competitivas
**Description:** La empresa confunde tener una capacidad (saber hacer algo) con tener una ventaja competitiva (hacerlo mejor que los competidores de forma sostenible).
**Typical_Causes:** Falta de análisis competitivo; autoengaño; confundir fortaleza interna con ventaja externa; no benchmarking.
**Observable_Symptoms:** La empresa cree tener ventaja pero el mercado no la reconoce; competidores igualan fácilmente; los clientes no perciben diferencia.
**Early_Warning_Signals:** % de clientes que reconocen la supuesta ventaja < 30%; % de competidores con capacidad similar > 60%; gap percepción vs realidad.
**Business_Impact:** Estrategia basada en falsa suposición; inversión en ventaja inexistente; vulnerabilidad real; posicionamiento débil.
**Severity_Level:** High
**Metrics_To_Check:** % de clientes que reconocen la ventaja; % de competidores con igual capacidad; durabilidad de la ventaja; posición competitiva real.
**Diagnostic_Questions:** ¿La supuesta ventaja es real? ¿Los clientes la perciben? ¿Los competidores pueden replicarla? ¿Hay evidencia de ventaja?
**Recommended_Actions:** Validar ventajas con clientes; benchmarking competitivo; ser honesto sobre capacidades; construir ventajas reales y percibidas.
**Related_Patterns:** STR-025, STR-033, STR-037, STR-039, STR-043

### STR-041
**Pattern_Name:** Ventaja Competitiva Basada en Personas Clave
**Category:** Ventajas Competitivas
**Description:** La ventaja competitiva depende de personas específicas (fundador, técnico, vendedor estrella) que si se van, la ventaja se pierde, siendo frágil y no institucional.
**Typical_Causes:** Conocimiento no documentado; falta de sistemas; cultura de "héroe"; procesos no estandarizados; dependencia personal.
**Observable_Symptoms:** Si la persona clave falta, la ventaja desaparece; clientes se van con la persona; conocimiento no transferido; vulnerabilidad.
**Early_Warning_Signals:** % de ventaja atribuible a personas clave > 50%; % de conocimiento documentado < 30%; tiempo de reemplazo > 3 meses.
**Business_Impact:** Vulnerabilidad extrema; riesgo existencial si la persona se va; imposibilidad de escalar; pérdida de clientes con la persona.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ventaja institucionalizada; % de conocimiento documentado; % de procesos estandarizados; dependencia de personas clave.
**Diagnostic_Questions:** ¿La ventaja depende de personas? ¿Se perdería si se van? ¿Está institucionalizada? ¿El conocimiento está documentado?
**Recommended_Actions:** Institucionalizar ventajas en procesos, sistemas y marca; documentar conocimiento; estandarizar; reducir dependencia de individuos.
**Related_Patterns:** STR-037, STR-038, STR-043, STR-079, STR-119

### STR-042
**Pattern_Name:** Falta de Benchmarking Competitivo
**Category:** Ventajas Competitivas
**Description:** La empresa no realiza benchmarking para comparar su desempeño y capacidades con competidores, desconociendo su posición competitiva relativa real.
**Typical_Causes:** Arrogancia; falta de recursos; desconocimiento; cultura de "mirar hacia adentro"; no priorización.
**Observable_Symptoms:** No se sabe cómo se compara la empresa con competidores; suposiciones sobre posición competitiva; sorpresas al descubrir gaps.
**Early_Warning_Signals:** Sin benchmarking regular; % de indicadores comparados con competidores < 20%; posición competitiva desconocida.
**Business_Impact:** Decisiones sin información competitiva; falsa percepción de posición; gaps no detectados; pérdida de competitividad inadvertida.
**Severity_Level:** High
**Metrics_To_Check:** % de indicadores con benchmarking; frecuencia de benchmarking; % de gaps conocidos; posición competitiva relativa.
**Diagnostic_Questions:** ¿Hay benchmarking? ¿Se conoce la posición competitiva real? ¿Hay gaps desconocidos? ¿Cómo se compara con competidores?
**Recommended_Actions:** Implementar benchmarking regular; identificar indicadores clave; comparar con mejores; establecer metas de superación.
**Related_Patterns:** STR-033, STR-037, STR-039, STR-040, STR-043

### STR-043
**Pattern_Name:** Falta de Identificación de Ventajas Competitivas Clave
**Category:** Ventajas Competitivas
**Description:** La empresa no ha identificado formalmente sus fuentes de ventaja competitiva, operando sin claridad sobre qué la hace única o superior en el mercado.
**Typical_Causes:** Falta de análisis estratégico; informalidad; equipo directivo sin formación estratégica; no uso de herramientas (VRIO, Porter).
**Observable_Symptoms:** No se pueden nombrar las ventajas competitivas; estrategia sin base; decisiones no apalancan ventajas; imitación.
**Early_Warning_Signals:** Sin análisis VRIO o similar; % de empleados que identifican ventajas < 30%; % de decisiones que apalancan ventajas < 20%.
**Business_Impact:** Estrategia sin fundamento; no apalancamiento de fortalezas; imitación; ventajas desaprovechadas; posicionamiento débil.
**Severity_Level:** High
**Metrics_To_Check:** % de ventajas identificadas; % de decisiones que las apalancan; % de empleados que las conocen; claridad estratégica.
**Diagnostic_Questions:** ¿Se han identificado las ventajas competitivas? ¿Son reales? ¿Se apalancan en decisiones? ¿El equipo las conoce?
**Recommended_Actions:** Realizar análisis VRIO; identificar ventajas reales; comunicarlas; apalancarlas en estrategia; protegerlas.
**Related_Patterns:** STR-025, STR-037, STR-039, STR-040, STR-109

### STR-044
**Pattern_Name:** Ventaja Competitiva no Apalancada Comercialmente
**Category:** Ventajas Competitivas
**Description:** La empresa tiene ventajas competitivas reales pero no las comunica ni explota comercialmente, perdiendo la oportunidad de diferenciarse y cobrar por ellas.
**Typical_Causes:** Falta de marketing; comunicación pobre; ventas no capacitadas; no traducir ventajas a beneficios; ventajas no visibles para el cliente.
**Observable_Symptoms:** Los clientes no conocen las ventajas de la empresa; la fuerza de ventas no las comunica; marketing no las destaca; se compite en igualdad.
**Early_Warning_Signals:** % de clientes que conocen las ventajas < 30%; % de materiales de venta que destacan ventajas < 40%; ventajas no comunicadas.
**Business_Impact:** Ventajas desaprovechadas; competencia en igualdad de condiciones; menor precio; menor cuota; crecimiento subóptimo.
**Severity_Level:** High
**Metrics_To_Check:** % de clientes que conocen ventajas; % de comunicación que destaca ventajas; precio relativo; reconocimiento de ventajas.
**Diagnostic_Questions:** ¿Los clientes conocen las ventajas? ¿Se comunican? ¿La fuerza de ventas las destaca? ¿Se capitalizan comercialmente?
**Recommended_Actions:** Traducir ventajas a beneficios para el cliente; capacitar ventas; comunicar en marketing; destacar en materiales; medir percepción.
**Related_Patterns:** STR-025, STR-028, STR-031, STR-037, STR-040

### STR-045
**Pattern_Name:** Erosión de Ventaja por Commoditización del Mercado
**Category:** Ventajas Competitivas
**Description:** El mercado tiende a la commoditización, donde las diferencias entre competidores se reducen y los clientes basan su decisión principalmente en precio.
**Typical_Causes:** Madurez del mercado; estandarización; baja innovación; imitación generalizada; falta de diferenciación sectorial.
**Observable_Symptoms:** Productos/servicios se perciben iguales; guerras de precios; márgenes comprimidos; lealtad baja; innovación escasa.
**Early_Warning_Signals:** % de clientes que perciben diferencias entre competidores < 30%; elasticidad precio alta; % de compras por precio > 60%; commoditización.
**Business_Impact:** Márgenes reducidos; competencia destructiva; rentabilidad baja; dificultad para diferenciarse; presión constante.
**Severity_Level:** Critical
**Metrics_To_Check:** % de clientes que perciben diferenciación; elasticidad precio; margen promedio del sector; tasa de innovación.
**Diagnostic_Questions:** ¿El mercado se está commoditizando? ¿Los clientes perciben diferencias? ¿Hay guerras de precios? ¿Se puede descommoditizar?
**Recommended_Actions:** Descommoditizar con servicio, experiencia o modelo de negocio; innovar; crear marca; segmentar; especializarse en nichos.
**Related_Patterns:** STR-037, STR-038, STR-043, STR-049, STR-051

### STR-046
**Pattern_Name:** Ventaja Competitiva no Conocida por la Organización
**Category:** Ventajas Competitivas
**Description:** Los empleados no conocen las ventajas competitivas de la empresa, por lo que sus decisiones y acciones diarias no las refuerzan ni las comunican.
**Typical_Causes:** Estrategia no comunicada; falta de cascada; desconexión dirección-operación; formación insuficiente; cultura débil.
**Observable_Symptoms:** Los empleados no saben qué hace única a la empresa; decisiones inconsistentes con las ventajas; no refuerzan la propuesta de valor.
**Early_Warning_Signals:** % de empleados que pueden nombrar ventajas < 20%; % de decisiones que las refuerzan < 30%; desconexión.
**Business_Impact:** Ventajas no se materializan en el día a día; ejecución inconsistente; clientes no experimentan la ventaja; desalineación.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados que conocen ventajas; % de decisiones alineadas; % de interacciones con clientes que refuerzan ventajas.
**Diagnostic_Questions:** ¿Los empleados conocen las ventajas competitivas? ¿Sus acciones las refuerzan? ¿Hay alineación? ¿Se comunican internamente?
**Recommended_Actions:** Comunicar ventajas a toda la organización; vincular con roles diarios; capacitar; medir alineación; celebrar refuerzo de ventajas.
**Related_Patterns:** STR-036, STR-043, STR-044, STR-046, STR-121

### STR-047
**Pattern_Name:** Dependencia de Ventaja Competitiva Regulatoria
**Category:** Ventajas Competitivas
**Description:** La ventaja competitiva se basa en protecciones regulatorias (licencias, permisos, barreras legales) que pueden desaparecer con cambios normativos.
**Typical_Causes:** Sector regulado; licencias exclusivas; protecciones gubernamentales; desconocimiento del riesgo regulatorio; falta de preparación.
**Observable_Symptoms:** Cambios regulatorios impactan severamente; la ventaja depende de permisos exclusivos; vulnerabilidad a reformas.
**Early_Warning_Signals:** % de ventaja basada en protección regulatoria > 50%; % de ingresos dependientes de licencias; cambios regulatorios en curso.
**Business_Impact:** Pérdida repentina de ventaja; caída de ingresos; necesidad de reinventarse; desventaja competitiva; posible quiebra.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ventaja regulatoria; % de ingresos dependientes; probabilidad de cambio regulatorio; plazo de protección.
**Diagnostic_Questions:** ¿La ventaja depende de regulación? ¿Es sostenible si cambia? ¿Hay plan para cuando desaparezca? ¿Se monitorean cambios regulatorios?
**Recommended_Actions:** Desarrollar ventajas no regulatorias; anticipar cambios; diversificar; construir marca y capacidades; monitorear regulación.
**Related_Patterns:** STR-036, STR-037, STR-039, STR-043, STR-077

### STR-048
**Pattern_Name:** Estrategia de Océano Rojo sin Diferenciación
**Category:** Ventajas Competitivas
**Description:** La empresa compite en un mercado saturado ("océano rojo") con muchos competidores, baja diferenciación y guerras de precios, sin buscar espacios de menor competencia.
**Typical_Causes:** Falta de innovación estratégica; imitación; conformismo; no exploración de océanos azules; estrategia reactiva.
**Observable_Symptoms:** Mercado lleno de competidores; guerras de precios; márgenes mínimos; poca diferenciación; clientes tienen mucho poder.
**Early_Warning_Signals:** Número de competidores > 10; % de margen bruto < 20%; elasticidad precio alta; % de clientes que rotan entre competidores > 40%.
**Business_Impact:** Márgenes reducidos; competencia destructiva; dificultad para crecer; estrés financiero; baja rentabilidad.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de competidores; margen bruto del sector; elasticidad precio; % de clientes leales; rentabilidad del sector.
**Diagnostic_Questions:** ¿Es un océano rojo? ¿Hay guerras de precios? ¿Se compite sin diferenciación? ¿Hay espacios de océano azul explorables?
**Recommended_Actions:** Aplicar estrategia de océano azul; innovar en valor; crear nuevo espacio de mercado; eliminar, reducir, incrementar, crear (ERRC).
**Related_Patterns:** STR-037, STR-038, STR-043, STR-049, STR-051


## Innovaci��n

### STR-049
**Pattern_Name:** Resistencia a la Innovaci��n
**Category:** Innovaci��n
**Description:** La empresa muestra resistencia cultural o directiva a la innovaci��n, prefiriendo mantener el status quo por miedo al riesgo o falta de visi��n, perdiendo oportunidades de mejora y crecimiento.
**Typical_Causes:** Cultura conservadora; miedo al fracaso; liderazgo que no fomenta innovaci��n; due��o con aversi��n al riesgo; ��xito pasado genera complacencia.
**Observable_Symptoms:** Las ideas nuevas son rechazadas; no hay presupuesto de innovaci��n; los empleados no proponen mejoras; se repiten siempre los mismos procesos.
**Early_Warning_Signals:** % de ideas implementadas < 5%; presupuesto de I+D < 1% de ventas; n��mero de iniciativas nuevas por a��o < 2; empleados no proponen.
**Business_Impact:** Obsolescencia competitiva; p��rdida de oportunidades; incapacidad de adaptarse; estancamiento; vulnerabilidad a disruptores.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ideas implementadas; inversi��n en innovaci��n/ventas; n��mero de nuevos productos/a��o; tiempo desde idea hasta implementaci��n.
**Diagnostic_Questions:** ��Hay resistencia a la innovaci��n? ��Se fomenta la generaci��n de ideas? ��Hay presupuesto de innovaci��n? ��El liderazgo apoya el cambio?
**Recommended_Actions:** Fomentar cultura de innovaci��n desde liderazgo; crear presupuesto de experimentaci��n; celebrar fracasos r��pidos; implementar sistema de ideas.
**Related_Patterns:** STR-037, STR-039, STR-048, STR-051, STR-056

### STR-050
**Pattern_Name:** Innovaci��n sin Conexi��n con Estrategia
**Category:** Innovaci��n
**Description:** La empresa invierte en innovaci��n sin alinearla con la estrategia general, generando iniciativas dispersas que no contribuyen a los objetivos estrat��gicos ni crean valor.
**Typical_Causes:** Falta de planificaci��n estrat��gica de innovaci��n; entusiasmo por novedades; innovaci��n como fin en s�� misma; desconexi��n entre ��reas.
**Observable_Symptoms:** Proyectos de innovaci��n que no se vinculan con objetivos estrat��gicos; recursos dispersos; resultados no capitalizables; falta de direcci��n.
**Early_Warning_Signals:** % de proyectos de innovaci��n alineados con estrategia < 30%; % de innovaciones que generan valor comercial < 20%; inversi��n sin direcci��n.
**Business_Impact:** Inversi��n desperdiciada; innovaci��n no genera ventaja competitiva; oportunidades perdidas; recursos mal asignados; frutos no capturados.
**Severity_Level:** High
**Metrics_To_Check:** % de proyectos alineados con estrategia; ROI de innovaci��n; % de innovaciones comercializadas; contribuci��n a objetivos estrat��gicos.
**Diagnostic_Questions:** ��La innovaci��n est�� alineada con la estrategia? ��Hay criterios de qu�� innovar? ��Los proyectos generan valor estrat��gico? ��Hay foco?
**Recommended_Actions:** Vincular innovaci��n con estrategia; definir ��reas prioritarias de innovaci��n; evaluar proyectos contra criterios estrat��gicos; detener proyectos no alineados.
**Related_Patterns:** STR-049, STR-051, STR-053, STR-056, STR-109

### STR-051
**Pattern_Name:** Innovaci��n Solo en Producto, No en Modelo de Negocio
**Category:** Innovaci��n
**Description:** La empresa solo innova en producto/servicio pero no en modelo de negocio (canales, pricing, procesos, propuesta de valor), perdiendo oportunidades de innovaci��n transformadora.
**Typical_Causes:** Visi��n tradicional de innovaci��n; enfoque en producto; falta de conocimiento de innovaci��n de modelo de negocio; sesgo de ingenier��a.
**Observable_Symptoms:** Innovaci��n se limita a productos; el modelo de negocio es el mismo desde hace a��os; oportunidades de innovaci��n en modelo no exploradas.
**Early_Warning_Signals:** % de innovaci��n en modelo de negocio < 10%; % de ingresos de nuevos modelos de negocio; tiempo sin cambiar modelo de negocio > 5 a��os.
**Business_Impact:** Oportunidades de innovaci��n transformadora perdidas; vulnerabilidad a disruptores de modelo de negocio; crecimiento sub��ptimo.
**Severity_Level:** High
**Metrics_To_Check:** % de innovaci��n en modelo de negocio; tiempo desde ��ltimo cambio de modelo; % de ingresos de nuevos modelos.
**Diagnostic_Questions:** ��Se innova solo en producto? ��Se explora innovaci��n en modelo de negocio? ��El modelo de negocio es el mismo desde hace a��os?
**Recommended_Actions:** Explorar innovaci��n en modelo de negocio (Business Model Canvas); experimentar con canales, pricing, propuesta de valor; estudiar disruptores.
**Related_Patterns:** STR-049, STR-050, STR-052, STR-053, STR-056

### STR-052
**Pattern_Name:** Falta de Proceso de Innovaci��n Sistem��tico
**Category:** Innovaci��n
**Description:** La innovaci��n ocurre de forma espor��dica y reactiva, sin un proceso sistem��tico que la fomente, capture y gestione, dependiendo de iniciativas individuales.
**Typical_Causes:** Falta de metodolog��a; informalidad; cultura de "ocurrencias"; no hay sistema de gesti��n de ideas; no hay etapa de evaluaci��n y desarrollo.
**Observable_Symptoms:** Innovaci��n depende de individuos; no hay pipeline de innovaci��n; las ideas se pierden; no hay seguimiento; procesos no definidos.
**Early_Warning_Signals:** Sin proceso de innovaci��n documentado; % de ideas capturadas < 20%; % de ideas evaluadas < 30%; sin responsable de innovaci��n.
**Business_Impact:** Innovaci��n no gestionada; ideas perdidas; dependencia de personas; innovaci��n reactiva; incapacidad de innovar consistentemente.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de proceso de innovaci��n; % de ideas capturadas; % de ideas evaluadas; n��mero de proyectos activos.
**Diagnostic_Questions:** ��Hay proceso sistem��tico de innovaci��n? ��Se capturan y eval��an ideas? ��Hay pipeline? ��Hay responsable? ��Es reactiva o proactiva?
**Recommended_Actions:** Implementar proceso de innovaci��n (generaci��n, evaluaci��n, desarrollo, lanzamiento); asignar responsable; crear comit�� de innovaci��n.
**Related_Patterns:** STR-049, STR-050, STR-053, STR-056, STR-104

### STR-053
**Pattern_Name:** Innovaci��n sin Protecci��n de Propiedad Intelectual
**Category:** Innovaci��n
**Description:** La empresa invierte en innovaci��n pero no protege los resultados mediante patentes, marcas o derechos de autor, permitiendo que competidores copien f��cilmente sus innovaciones.
**Typical_Causes:** Desconocimiento de PI; falta de asesor��a legal; recursos limitados; cultura de "compartir"; no priorizaci��n.
**Observable_Symptoms:** Competidores copian innovaciones; no hay barreras de imitaci��n; la empresa no tiene patentes ni marcas registradas; ventaja se erosiona.
**Early_Warning_Signals:** N��mero de patentes/marcas = 0; % de innovaciones sin protecci��n > 80%; tiempo de imitaci��n < 6 meses; copias en mercado.
**Business_Impact:** Ventaja de innovaci��n ef��mera; competidores se benefician sin invertir; p��rdida de retorno de inversi��n en I+D; desincentivo a innovar.
**Severity_Level:** High
**Metrics_To_Check:** N��mero de patentes y marcas; % de innovaciones protegidas; tiempo de imitaci��n; inversi��n en protecci��n de PI.
**Diagnostic_Questions:** ��Se protegen las innovaciones? ��Hay patentes o marcas? ��Los competidores pueden copiar f��cilmente? ��La ventaja de innovaci��n es sostenible?
**Recommended_Actions:** Evaluar patentabilidad de innovaciones; registrar marcas; asesorarse en PI; establecer pol��tica de protecci��n de innovaciones.
**Related_Patterns:** STR-037, STR-049, STR-051, STR-052, STR-056

### STR-054
**Pattern_Name:** Falta de Innovaci��n Abierta (Open Innovation)
**Category:** Innovaci��n
**Description:** La empresa solo innova internamente sin aprovechar fuentes externas (clientes, proveedores, startups, universidades), limitando su capacidad de innovaci��n y acceso a nuevas ideas.
**Typical_Causes:** Cultura de "inventado aqu��"; falta de conexiones externas; desconocimiento de open innovation; proteccionismo; falta de redes.
**Observable_Symptoms:** Toda innovaci��n es interna; no hay colaboraci��n con externos; se ignoran innovaciones de proveedores o clientes; baja tasa de innovaci��n.
**Early_Warning_Signals:** % de innovaciones con origen externo < 10%; n��mero de colaboraciones externas en innovaci��n = 0; % de I+D interna vs externa.
**Business_Impact:** Capacidad de innovaci��n limitada; sesgo interno; oportunidades externas perdidas; menor velocidad de innovaci��n; visi��n estrecha.
**Severity_Level:** Medium
**Metrics_To_Check:** % de innovaciones con origen externo; n��mero de colaboraciones; % de presupuesto en innovaci��n abierta.
**Diagnostic_Questions:** ��Se aprovechan fuentes externas de innovaci��n? ��Se colabora con clientes, proveedores o universidades? ��La innovaci��n es solo interna?
**Recommended_Actions:** Implementar open innovation; colaborar con startups, universidades, clientes; participar en ecosistemas de innovaci��n; usar crowdsourcing.
**Related_Patterns:** STR-049, STR-052, STR-053, STR-056, STR-058

### STR-055
**Pattern_Name:** Presupuesto de Innovaci��n Insuficiente o Inexistente
**Category:** Innovaci��n
**Description:** La empresa no asigna presupuesto espec��fico a innovaci��n o este es insuficiente, dependiendo de sobrantes o iniciativas no financiadas que rara vez se materializan.
**Typical_Causes:** Cortoplacismo; priorizaci��n de operaci��n; falta de compromiso con innovaci��n; desconocimiento de su importancia; restricciones financieras.
**Observable_Symptoms:** Innovaci��n se financia con "lo que sobra"; no hay presupuesto asignado; proyectos de innovaci��n se cancelan por falta de fondos; dependencia de caja.
**Early_Warning_Signals:** Presupuesto de I+D/ventas < 1%; % de proyectos de innovaci��n financiados < 30%; sin partida presupuestaria de innovaci��n.
**Business_Impact:** Innovaci��n insuficiente; incapacidad de desarrollar nuevas ventajas; obsolescencia; p��rdida de competitividad futura.
**Severity_Level:** High
**Metrics_To_Check:** Presupuesto de innovaci��n/ventas; % de proyectos financiados; inversi��n en I+D vs competidores; pipeline de innovaci��n.
**Diagnostic_Questions:** ��Hay presupuesto de innovaci��n? ��Es suficiente? ��Se financia solo con sobrantes? ��C��mo se compara con competidores? ��Hay pipeline?
**Recommended_Actions:** Asignar presupuesto espec��fico a innovaci��n; protegerlo de recortes; benchmarkear inversi��n; tratar innovaci��n como inversi��n, no gasto.
**Related_Patterns:** STR-049, STR-050, STR-052, STR-056, STR-104

### STR-056
**Pattern_Name:** Falta de M��tricas de Innovaci��n
**Category:** Innovaci��n
**Description:** La empresa no mide la efectividad de su inversi��n en innovaci��n, operando sin indicadores de input, proceso, output y resultado, lo que impide gestionarla adecuadamente.
**Typical_Causes:** Falta de cultura de medici��n; desconocimiento de m��tricas de innovaci��n; dificultad de medir; informalidad.
**Observable_Symptoms:** No se sabe cu��nto se invierte en innovaci��n ni qu�� retorno genera; no hay KPIs de innovaci��n; decisiones basadas en intuici��n.
**Early_Warning_Signals:** Sin m��tricas de innovaci��n; % de proyectos con ROI medido < 20%; sin reporte de innovaci��n; sin targets.
**Business_Impact:** Imposibilidad de gestionar innovaci��n; inversi��n no optimizada; decisiones sin datos; rendimiento desconocido; falta de accountability.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de m��tricas de innovaci��n; % de proyectos con ROI; pipeline de innovaci��n; % de ingresos de nuevos productos.
**Diagnostic_Questions:** ��Se mide la innovaci��n? ��Hay KPIs? ��Se conoce el ROI de innovaci��n? ��Hay targets? ��Se reporta?
**Recommended_Actions:** Definir m��tricas de innovaci��n (input: inversi��n, proceso: velocidad, output: nuevos productos, resultado: ROI); reportar regularmente.
**Related_Patterns:** STR-050, STR-052, STR-055, STR-104, STR-128

### STR-057
**Pattern_Name:** Innovaci��n Desconectada del Cliente
**Category:** Innovaci��n
**Description:** La empresa innova sin entender las necesidades reales del cliente, desarrollando productos o soluciones que el mercado no valora ni adopta, desperdiciando recursos.
**Typical_Causes:** Falta de investigaci��n de mercado; innovaci��n desde el laboratorio; sesgo interno; no validaci��n con clientes; arrogancia.
**Observable_Symptoms:** Nuevos productos no se venden; clientes no ven valor; innovaciones no adoptadas; dinero invertido sin retorno; fracasos de lanzamiento.
**Early_Warning_Signals:** % de nuevos productos con adopci��n < 20%; % de innovaciones validadas con clientes < 10%; ratio de fracaso > 70%.
**Business_Impact:** P��rdida de inversi��n; oportunidades perdidas; frustraci��n; descr��dito de innovaci��n; resistencia a innovar en el futuro.
**Severity_Level:** Critical
**Metrics_To_Check:** % de innovaciones validadas con clientes; tasa de adopci��n de nuevos productos; ROI de innovaci��n; % de fracasos.
**Diagnostic_Questions:** ��Las innovaciones responden a necesidades del cliente? ��Se validaron con clientes? ��El mercado adopta las innovaciones? ��Hay research?
**Recommended_Actions:** Implementar innovaci��n centrada en el cliente (Design Thinking); validar temprano con prototipos; investigar necesidades reales; testear antes de lanzar.
**Related_Patterns:** STR-049, STR-050, STR-051, STR-053, STR-059

### STR-058
**Pattern_Name:** Innovaci��n Solo Incremental, No Disruptiva
**Category:** Innovaci��n
**Description:** La empresa solo realiza innovaci��n incremental (mejoras menores) sin explorar innovaciones disruptivas que puedan transformar el mercado o crear nuevas categor��as.
**Typical_Causes:** Aversi��n al riesgo; enfoque en corto plazo; cultura de mejora continua sin exploraci��n; falta de visi��n disruptiva; recursos limitados.
**Observable_Symptoms:** Todas las innovaciones son peque��as mejoras; no hay innovaciones radicales; el mercado no cambia por la empresa; vulnerabilidad a disruptores externos.
**Early_Warning_Signals:** % de innovaci��n disruptiva < 5%; % de inversi��n en innovaci��n incremental > 90%; tiempo sin innovaci��n disruptiva > 5 a��os.
**Business_Impact:** Vulnerabilidad a disruptores; crecimiento limitado a mejoras marginales; oportunidades de transformaci��n perdidas; eventual obsolescencia.
**Severity_Level:** High
**Metrics_To_Check:** % de innovaci��n disruptiva vs incremental; % de inversi��n en exploraci��n; n��mero de innovaciones disruptivas por a��o.
**Diagnostic_Questions:** ��Hay innovaci��n disruptiva o solo incremental? ��Se explora lo radical? ��Hay proyectos de innovaci��n transformadora? ��Se est�� invirtiendo en exploraci��n?
**Recommended_Actions:** Balancear innovaci��n incremental y disruptiva (ambidiestr��a organizacional); asignar recursos a exploraci��n; crear unidad de innovaci��n disruptiva.
**Related_Patterns:** STR-049, STR-051, STR-054, STR-056, STR-059

### STR-059
**Pattern_Name:** Falta de Experimentaci��n R��pida
**Category:** Innovaci��n
**Description:** La empresa no realiza experimentos r��pidos para validar hip��tesis de innovaci��n, invirtiendo mucho tiempo y recursos en ideas no validadas que frecuentemente fracasan.
**Typical_Causes:** Cultura de an��lisis prolongado; falta de metodolog��a lean; miedo al fracaso; procesos pesados de aprobaci��n; no cultura de testeo.
**Observable_Symptoms:** Proyectos largos sin validaci��n temprana; grandes inversiones antes de saber si funciona; fracasos costosos; lentitud en innovaci��n.
**Early_Warning_Signals:** Tiempo desde idea hasta primer test > 6 meses; % de proyectos con validaci��n temprana < 20%; inversi��n antes de validar > 50% del total.
**Business_Impact:** Innovaci��n lenta; costos de fracaso elevados; oportunidades perdidas por velocidad; recursos malgastados en ideas no validadas.
**Severity_Level:** High
**Metrics_To_Check:** Tiempo hasta primer test; % de proyectos con validaci��n temprana; costo de fracasos; velocidad de experimentaci��n.
**Diagnostic_Questions:** ��Se experimenta r��pidamente? ��Se validan hip��tesis antes de invertir? ��Los fracasos son r��pidos y baratos? ��Hay cultura de testeo?
**Recommended_Actions:** Implementar metodolog��a Lean Startup; experimentos r��pidos y baratos; MVP; validar hip��tesis antes de escalar; fracasar r��pido y barato.
**Related_Patterns:** STR-049, ST-052, STR-053, STR-057, STR-058

### STR-060
**Pattern_Name:** Falta de Intraemprendimiento
**Category:** Innovaci��n
**Description:** La empresa no fomenta el intraemprendimiento, perdiendo la capacidad de retener y capitalizar el esp��ritu emprendedor de sus empleados para generar nuevos negocios.
**Typical_Causes:** Cultura jer��rquica; falta de incentivos; miedo a perder empleados; no hay programa de intraemprendimiento; burocracia.
**Observable_Symptoms:** Empleados emprendedores se van a crear sus propios negocios; ideas internas no se desarrollan; falta de nuevas iniciativas; talento no retenido.
**Early_Warning_Signals:** % de empleados emprendedores que se van > 20%; n��mero de nuevos negocios internos = 0; % de ideas internas implementadas < 5%.
**Business_Impact:** P��rdida de talento emprendedor; oportunidades de negocio perdidas; fuga de ideas; empleados no comprometidos; innovaci��n interna limitada.
**Severity_Level:** Medium
**Metrics_To_Check:** % de empleados emprendedores retenidos; n��mero de intraemprendimientos activos; % de ingresos de nuevos negocios internos.
**Diagnostic_Questions:** ��Se fomenta el intraemprendimiento? ��Los empleados emprendedores se quedan o se van? ��Hay programa de intraemprendimiento? ��Se capitalizan las ideas internas?
**Recommended_Actions:** Crear programa de intraemprendimiento; asignar tiempo y recursos; incentivar; permitir fallar; celebrar iniciativas internas.
**Related_Patterns:** STR-049, STR-050, STR-054, STR-058, STR-078


## Expansi��n

### STR-061
**Pattern_Name:** Expansi��n sin Capital Suficiente
**Category:** Expansi��n
**Description:** La empresa inicia un proceso de expansi��n (nuevas sucursales, geograf��as, capacidad) sin contar con el capital de trabajo necesario, generando problemas de liquidez y estr��s financiero.
**Typical_Causes:** Subestimaci��n de necesidades de capital; optimismo excesivo; falta de planificaci��n financiera; presi��n por crecer; ausencia de proyecciones.
**Observable_Symptoms:** La expansi��n consume caja r��pidamente; problemas de liquidez; retrasos en pagos; necesidad de financiamiento urgente; obras o proyectos detenidos.
**Early_Warning_Signals:** Capital de trabajo disponible / requerido < 0.8; desviaci��n de presupuesto de expansi��n > 20%; solicitudes de cr��dito urgentes; obras detenidas.
**Business_Impact:** Crisis de liquidez; expansi��n inconclusa; p��rdida de inversi��n; da��o reputacional con proveedores; riesgo de insolvencia.
**Severity_Level:** Critical
**Metrics_To_Check:** Capital disponible vs requerido; desviaci��n de presupuesto; d��as de caja proyectados; ratio de liquidez; ROI de expansi��n.
**Diagnostic_Questions:** ��Hay suficiente capital para la expansi��n? ��Se subestimaron las necesidades? ��Hay estr��s de caja? ��Se proyectaron escenarios?
**Recommended_Actions:** Proyectar necesidades de capital de expansi��n; asegurar financiamiento antes de empezar; planificar en etapas; mantener reservas.
**Related_Patterns:** STR-061, STR-063, STR-066, STR-098, STR-104

### STR-062
**Pattern_Name:** Expansi��n sin Plan Operativo Detallado
**Category:** Expansi��n
**Description:** La empresa expande sus operaciones sin un plan operativo detallado que cubra procesos, personal, sistemas y log��stica, generando caos operativo y mala experiencia de cliente.
**Typical_Causes:** Entusiasmo; falta de planificaci��n; subestimaci��n de la complejidad; cultura de "improvisar"; no experiencia en expansiones previas.
**Observable_Symptoms:** Caos en nuevas operaciones; procesos no definidos; personal no capacitado; sistemas no implementados; clientes insatisfechos; errores operativos.
**Early_Warning_Signals:** % de procesos documentados para expansi��n < 30%; % de personal capacitado antes de inicio < 50%; quejas de clientes en nuevas ubicaciones > 30%.
**Business_Impact:** Mala experiencia de cliente; costos operativos mayores; da��o reputacional; p��rdida de oportunidad; necesidad de corregir sobre la marcha.
**Severity_Level:** High
**Metrics_To_Check:** % de procesos documentados; % de personal capacitado; satisfacci��n de clientes en nuevas ubicaciones; eficiencia operativa.
**Diagnostic_Questions:** ��Hay plan operativo detallado? ��Los procesos est��n definidos? ��El personal est�� capacitado? ��Los sistemas est��n listos?
**Recommended_Actions:** Desarrollar plan operativo detallado; documentar procesos; capacitar personal; implementar sistemas antes de abrir; pilotar.
**Related_Patterns:** STR-061, STR-063, STR-067, STR-086, STR-092

### STR-063
**Pattern_Name:** Crecimiento por Apertura sin Estudios de Mercado Local
**Category:** Expansi��n
**Description:** La empresa abre nuevas sucursales o ubicaciones sin estudios de mercado locales adecuados, asumiendo que lo que funciona en un lugar funcionar�� igual en otro.
**Typical_Causes:** Arrogancia; falta de investigaci��n; presi��n por crecer; asumir homogeneidad; no invertir en estudios.
**Observable_Symptoms:** Nuevas ubicaciones no rinden como las originales; diferencias de mercado no anticipadas; adaptaciones forzadas; resultados por debajo de lo esperado.
**Early_Warning_Signals:** % de nuevas ubicaciones que alcanzan punto de equilibrio en plazo previsto < 40%; % de desviaci��n de ventas vs proyecci��n > 30%; cierres tempranos.
**Business_Impact:** Inversiones no rentables; p��rdida de capital; da��o reputacional; descr��dito del plan de expansi��n; retracci��n forzada.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ubicaciones que alcanzan punto de equilibrio; desviaci��n vs proyecci��n; ROI por ubicaci��n; tasa de cierre temprano.
**Diagnostic_Questions:** ��Se hizo estudio de mercado local? ��Se validaron supuestos? ��Las condiciones locales son diferentes? ��Hay demanda suficiente?
**Recommended_Actions:** Realizar estudios de mercado local antes de abrir; adaptar propuesta; validar con pilotos; no asumir que todo mercado es igual.
**Related_Patterns:** STR-027, STR-061, STR-062, STR-064, STR-067

### STR-064
**Pattern_Name:** Expansi��n Geogr��fica sin Cadena de Suministro Preparada
**Category:** Expansi��n
**Description:** La empresa se expande a nuevas regiones sin preparar su cadena de suministro, enfrentando problemas log��sticos, desabastecimiento, mayores costos y tiempos de entrega.
**Typical_Causes:** Subestimaci��n log��stica; enfoque solo en ventas; falta de planificaci��n de supply chain; no evaluaci��n de capacidad de abastecimiento local.
**Observable_Symptoms:** Desabastecimiento en nuevas ubicaciones; tiempos de entrega largos; costos log��sticos mayores; proveedores no preparados; calidad inconsistente.
**Early_Warning_Signals:** % de entregas a tiempo en nuevas ubicaciones < 60%; costo log��stico/ventas > 15% vs 8% en origen; rotura de stock > 10%.
**Business_Impact:** Mala experiencia de cliente; sobrecostos; p��rdida de ventas por desabastecimiento; da��o reputacional; ineficiencia operativa.
**Severity_Level:** High
**Metrics_To_Check:** % de entregas a tiempo; costo log��stico/ventas; % de rotura de stock; satisfacci��n de clientes en nuevas ubicaciones.
**Diagnostic_Questions:** ��La cadena de suministro est�� preparada? ��Hay capacidad de abastecimiento? ��Los costos log��sticos son competitivos? ��Hay desabastecimiento?
**Recommended_Actions:** Planificar cadena de suministro para expansi��n; evaluar proveedores locales; invertir en log��stica; dimensionar inventario; pilotar.
**Related_Patterns:** STR-061, STR-063, STR-066, STR-086, STR-092

### STR-065
**Pattern_Name:** Expansi��n que Canibaliza Operaciones Existentes
**Category:** Expansi��n
**Description:** La expansi��n territorial o de canales canibaliza las ventas de operaciones existentes en lugar de generar crecimiento neto, trasladando clientes en lugar de captar nuevos.
**Typical_Causes:** Proximidad geogr��fica entre ubicaciones; segmentos objetivo superpuestos; falta de diferenciaci��n entre canales; mala planificaci��n territorial.
**Observable_Symptoms:** Nuevas ubicaciones restan ventas a las existentes; ventas totales no crecen proporcionalmente; clientes se trasladan; conflictos entre canales.
**Early_Warning_Signals:** % de ventas nuevas que provienen de canibalizaci��n > 30%; crecimiento neto < 50% del crecimiento bruto; conflictos entre ubicaciones.
**Business_Impact:** Crecimiento ilusorio; inversi��n sin retorno real; conflictos internos; recursos desperdiciados; rentabilidad general no mejora.
**Severity_Level:** High
**Metrics_To_Check:** % de canibalizaci��n; crecimiento neto vs bruto; rentabilidad incremental; ventas comparables de ubicaciones existentes.
**Diagnostic_Questions:** ��La expansi��n canibaliza operaciones existentes? ��Hay crecimiento neto real? ��Los clientes son nuevos o se trasladan? ��Hay suficiente distancia entre ubicaciones?
**Recommended_Actions:** Evaluar impacto en operaciones existentes; planificar distancia entre ubicaciones; diferenciar canales; medir crecimiento neto antes de expandir.
**Related_Patterns:** STR-015, STR-061, STR-063, STR-067, STR-071

### STR-066
**Pattern_Name:** Expansi��n sin Equipo de Gesti��n Preparado
**Category:** Expansi��n
**Description:** La empresa expande operaciones sin contar con el equipo de gesti��n adecuado para las nuevas ubicaciones o unidades, delegando en personas sin experiencia o capacidad.
**Typical_Causes:** Falta de talento gerencial; apuro por expandir; subestimaci��n de necesidades de gesti��n; no desarrollo de liderazgo; promociones prematuras.
**Observable_Symptoms:** Nuevas ubicaciones con gerentes inexpertos; problemas de gesti��n; rotaci��n de gerentes; resultados pobres; falta de control.
**Early_Warning_Signals:** % de gerentes de nuevas ubicaciones con experiencia < 2 a��os; rotaci��n de gerentes > 30% anual; % de ubicaciones con p��rdidas.
**Business_Impact:** Mala gesti��n de nuevas operaciones; resultados pobres; p��rdida de inversi��n; problemas operativos y de personal; cierre de ubicaciones.
**Severity_Level:** High
**Metrics_To_Check:** Experiencia de gerentes; rotaci��n de gerentes; rentabilidad por ubicaci��n; % de ubicaciones con p��rdidas.
**Diagnostic_Questions:** ��Hay gerentes preparados para las nuevas ubicaciones? ��Tienen experiencia? ��Se desarroll�� liderazgo? ��La gesti��n es adecuada?
**Recommended_Actions:** Desarrollar pipeline de gerentes antes de expandir; capacitar; asignar gerentes experimentados a nuevas ubicaciones; mentor��a.
**Related_Patterns:** STR-061, STR-062, STR-063, STR-078, STR-086

### STR-067
**Pattern_Name:** Franquicias sin Control de Calidad
**Category:** Expansi��n
**Description:** La empresa expande mediante franquicias sin implementar sistemas de control de calidad efectivos, generando inconsistencia en la experiencia del cliente y da��o a la marca.
**Typical_Causes:** Falta de sistemas de calidad; capacitaci��n insuficiente; supervisi��n d��bil; crecimiento r��pido sin control; selecci��n laxa de franquiciados.
**Observable_Symptoms:** Variabilidad en calidad entre franquicias; clientes reportan experiencias inconsistentes; quejas recurrentes; franquicias que no siguen el modelo.
**Early_Warning_Signals:** % de franquicias que cumplen est��ndares < 60%; % de quejas por inconsistencia > 20%; n��mero de auditor��as/mes < 1; desviaci��n de est��ndares.
**Business_Impact:** Da��o a la marca; experiencia inconsistente; p��rdida de clientes; conflictos con franquiciados; devaluaci��n de la franquicia.
**Severity_Level:** Critical
**Metrics_To_Check:** % de cumplimiento de est��ndares; satisfacci��n de clientes por franquicia; n��mero de quejas; resultados de auditor��as.
**Diagnostic_Questions:** ��Hay control de calidad en franquicias? ��Los est��ndares se cumplen? ��La experiencia es consistente? ��Hay auditor��as regulares?
**Recommended_Actions:** Implementar sistema de control de calidad; auditor��as peri��dicas; capacitaci��n continua; manuales de operaci��n; incentivos al cumplimiento.
**Related_Patterns:** STR-061, STR-066, STR-069, STR-073, STR-086

### STR-068
**Pattern_Name:** Expansi��n Financiada con Deuda de Corto Plazo
**Category:** Expansi��n
**Description:** La empresa financia su expansi��n con deuda de corto plazo (cr��ditos comerciales, sobregiros), generando un descalce de plazos entre el financiamiento y el retorno de la inversi��n.
**Typical_Causes:** Falta de acceso a cr��dito de largo plazo; urgencia por expandir; mala estructuraci��n financiera; desconocimiento de riesgo de descalce; presi��n.
**Observable_Symptoms:** Pagos de deuda de corto plazo presionan la caja; la expansi��n a��n no genera retorno pero las cuotas vencen; refinanciaciones constantes; estr��s financiero.
**Early_Warning_Signals:** % de expansi��n financiada con deuda de corto plazo > 50%; descalce de plazos > 12 meses; ratio de cobertura de deuda < 1.2; refinanciaciones.
**Business_Impact:** Estr��s financiero; riesgo de default; incapacidad de pagar; p��rdida de inversi��n; posible quiebra por iliquidez.
**Severity_Level:** Critical
**Metrics_To_Check:** % de financiamiento de corto plazo; descalce de plazos; ratio de cobertura de deuda; costo financiero/ventas.
**Diagnostic_Questions:** ��La expansi��n se financia con deuda de corto plazo? ��Hay descalce? ��La caja soporta los pagos? ��Se puede reestructurar?
**Recommended_Actions:** Estructurar financiamiento de expansi��n con deuda de largo plazo; buscar inversionistas; leasing; project finance; evitar descalce.
**Related_Patterns:** STR-061, STR-063, STR-068, STR-098, STR-104

### STR-069
**Pattern_Name:** Expansi��n sin An��lisis de Competencia Local
**Category:** Expansi��n
**Description:** La empresa expande a nuevos mercados sin analizar adecuadamente a los competidores locales existentes, enfrentando una competencia m��s fuerte de lo anticipado.
**Typical_Causes:** Arrogancia competitiva; falta de investigaci��n; asumir que la f��rmula actual vence a cualquier competidor; subestimaci��n.
**Observable_Symptoms:** Competidores locales responden agresivamente; p��rdida de participaci��n; guerra de precios; dificultad para posicionarse; resultados menores.
**Early_Warning_Signals:** % de participaci��n de mercado capturada vs objetivo < 40%; reacci��n competitiva no anticipada; % de ventas por debajo de proyecci��n > 30%.
**Business_Impact:** P��rdida de inversi��n; retirada forzada; da��o reputacional; imposibilidad de competir; recursos desperdiciados.
**Severity_Level:** High
**Metrics_To_Check:** Participaci��n de mercado capturada; reacci��n competitiva; desviaci��n de ventas vs proyecci��n; rentabilidad en nuevo mercado.
**Diagnostic_Questions:** ��Se analiz�� la competencia local? ��Hay competidores fuertes? ��Pueden responder agresivamente? ��Hay barreras competitivas?
**Recommended_Actions:** Analizar competencia local en profundidad; anticipar respuestas; diferenciar propuesta; considerar adquisici��n de competidor local.
**Related_Patterns:** STR-033, STR-037, STR-063, STR-073, STR-074

### STR-070
**Pattern_Name:** Expansi��n que Diluye la Cultura Organizacional
**Category:** Expansi��n
**Description:** El crecimiento r��pido o la expansi��n a nuevas ubicaciones diluye la cultura organizacional, perdiendo los valores, pr��cticas y cohesi��n que hac��an exitosa a la empresa.
**Typical_Causes:** Falta de atenci��n a cultura; contrataciones masivas sin evaluar fit cultural; descentralizaci��n sin lineamientos; liderazgo debilitado.
**Observable_Symptoms:** Nuevos empleados no comparten valores; la cultura se debilita; conflictos; p��rdida de identidad; comportamiento inconsistente entre ubicaciones.
**Early_Warning_Signals:** % de nuevos empleados que identifican valores < 30%; % de ubicaciones con cultura distinta; rotaci��n de personal clave > 25%; conflictos.
**Business_Impact:** P��rdida de identidad; desalineaci��n; problemas de cohesi��n; deterioro de clima laboral; impacto en productividad y resultados.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados que identifican valores; rotaci��n; clima laboral por ubicaci��n; consistencia cultural.
**Diagnostic_Questions:** ��La expansi��n est�� diluyendo la cultura? ��Los nuevos empleados comparten valores? ��La cultura es consistente en todas las ubicaciones?
**Recommended_Actions:** Gestionar cultura activamente durante expansi��n; incorporar fit cultural en selecci��n; comunicar valores; liderazgo visible.
**Related_Patterns:** STR-078, STR-079, STR-082, STR-086, STR-121

### STR-071
**Pattern_Name:** Expansi��n por Moda o Presi��n Competitiva
**Category:** Expansi��n
**Description:** La empresa expande porque "todos lo hacen" o por presi��n competitiva, sin una decisi��n estrat��gica fundamentada, cayendo en una carrera sin sentido.
**Typical_Causes:** Presi��n de pares; imitaci��n; miedo a quedarse atr��s; falta de estrategia propia; arrastre del sector.
**Observable_Symptoms:** Expansi��n sin criterio claro; seguir al l��der sin an��lisis; decisiones reactivas; inversiones sin fundamento estrat��gico.
**Early_Warning_Signals:** % de decisiones de expansi��n basadas en an��lisis propio < 30%; % de expansiones que imitan a competidores > 50%; sin criterios claros.
**Business_Impact:** Inversiones no alineadas con estrategia; resultados pobres; imitaci��n sin diferenciaci��n; recursos desperdiciados; p��rdida de foco.
**Severity_Level:** High
**Metrics_To_Check:** % de decisiones basadas en an��lisis propio; % de expansiones reactivas; ROI de expansiones; alineaci��n con estrategia.
**Diagnostic_Questions:** ��La expansi��n responde a una estrategia propia o a presi��n externa? ��Se est�� imitando a competidores? ��Hay criterios claros?
**Recommended_Actions:** Fundamentar expansi��n en estrategia propia; no seguir modas; hacer an��lisis independiente; decir no si no hay fundamento.
**Related_Patterns:** STR-011, STR-049, STR-063, STR-069, STR-073

### STR-072
**Pattern_Name:** Expansi��n sin Plan de Salida o Contingencia
**Category:** Expansi��n
**Description:** La empresa expande sin considerar la posibilidad de fracaso ni tener un plan de salida o contingencia, arriesgando toda la empresa si la expansi��n no funciona.
**Typical_Causes:** Optimismo excesivo; falta de planificaci��n de riesgos; creencia en ��xito asegurado; no experiencia previa; sesgo de confirmaci��n.
**Observable_Symptoms:** Cuando la expansi��n falla, no hay plan; la empresa sufre p��rdidas significativas; imposibilidad de retirarse ordenadamente; da��o a todo el negocio.
**Early_Warning_Signals:** Sin plan de contingencia; % de inversi��n en expansi��n respecto a patrimonio > 50%; sin puntos de decisi��n; sin criterios de salida.
**Business_Impact:** P��rdida total de inversi��n; riesgo existencial; da��o colateral al negocio principal; imposibilidad de retroceder; crisis.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de plan de contingencia; % de inversi��n en riesgo / patrimonio; puntos de decisi��n definidos; criterios de salida.
**Diagnostic_Questions:** ��Hay plan de contingencia si la expansi��n falla? ��Se ha definido el riesgo m��ximo aceptable? ��Hay criterios para cancelar?
**Recommended_Actions:** Definir planes de contingencia; establecer hitos de decisi��n; limitar inversi��n m��xima en expansi��n; tener criterios de salida claros.
**Related_Patterns:** STR-061, STR-063, STR-068, STR-072, STR-098


## Internacionalizaci��n

### STR-073
**Pattern_Name:** Internacionalizaci��n sin Investigaci��n de Mercado
**Category:** Internacionalizaci��n
**Description:** La empresa inicia su proceso de internacionalizaci��n sin investigar adecuadamente los mercados objetivo (cultura, regulaci��n, competencia, demanda), cometiendo errores costosos.
**Typical_Causes:** Entusiasmo; subestimaci��n de diferencias; falta de recursos para investigaci��n; asumir que el mercado local es similar; apuro.
**Observable_Symptoms:** Producto/servicio no se adapta al mercado local; diferencias culturales no anticipadas; problemas regulatorios; demanda menor a la esperada.
**Early_Warning_Signals:** % de investigaci��n de mercado realizada < 30%; % de supuestos validados < 20%; errores evitables en los primeros 6 meses > 5.
**Business_Impact:** P��rdida de inversi��n; fracaso en el mercado; da��o reputacional; retirada forzada; desaliento para futura internacionalizaci��n.
**Severity_Level:** Critical
**Metrics_To_Check:** % de investigaci��n realizada; % de supuestos validados; desviaci��n de ventas vs proyecci��n; errores cometidos.
**Diagnostic_Questions:** ��Se investig�� el mercado objetivo? ��Se conocen las diferencias culturales? ��Se validaron supuestos? ��Hay demanda real?
**Recommended_Actions:** Invertir en investigaci��n de mercado internacional; contratar consultores locales; validar supuestos; no asumir; estudiar cultura.
**Related_Patterns:** STR-022, STR-027, STR-063, STR-074, STR-077

### STR-074
**Pattern_Name:** Adaptaci��n Insuficiente del Producto al Mercado Local
**Category:** Internacionalizaci��n
**Description:** La empresa no adapta su producto/servicio a las necesidades, preferencias o regulaciones del mercado local, ofreciendo exactamente lo mismo que en el mercado de origen.
**Typical_Causes:** Arrogancia; desconocimiento; falta de flexibilidad; econom��as de escala; presunci��n de universalidad.
**Observable_Symptoms:** Baja adopci��n del producto; clientes locales no conectan; quejas sobre caracter��sticas no adecuadas; producto no cumple regulaciones locales.
**Early_Warning_Signals:** % de clientes que reportan falta de adecuaci��n > 30%; % de ventas vs objetivo < 40%; % de caracter��sticas del producto que requieren adaptaci��n > 50%.
**Business_Impact:** Baja penetraci��n; p��rdida de inversi��n; producto rechazado; necesidad de retirarse o adaptarse forzosamente; cr��dito perdido.
**Severity_Level:** Critical
**Metrics_To_Check:** % de adecuaci��n del producto al mercado; % de ventas vs objetivo; % de quejas por adecuaci��n; tiempo de adaptaci��n.
**Diagnostic_Questions:** ��El producto est�� adaptado al mercado local? ��Cumple regulaciones? ��Responde a preferencias locales? ��Hay necesidad de adaptaci��n?
**Recommended_Actions:** Adaptar producto a mercado local (glocalizaci��n); investigar necesidades y regulaciones; flexibilizar; equilibrar estandarizaci��n y adaptaci��n.
**Related_Patterns:** STR-073, STR-075, STR-077, STR-080, STR-083

### STR-075
**Pattern_Name:** Internacionalizaci��n sin Socio Local
**Category:** Internacionalizaci��n
**Description:** La empresa intenta internacionalizarse sin un socio local que conozca el mercado, regulaciones, cultura y canales, enfrentando barreras dif��ciles de superar sola.
**Typical_Causes:** Deseo de control total; desconocimiento del valor del socio local; falta de red de contactos; desconfianza; subestimaci��n de complejidad.
**Observable_Symptoms:** Dificultad para navegar regulaciones; errores culturales; acceso limitado a canales; lentitud; costos mayores; falta de contactos.
**Early_Warning_Signals:** % de barreras de entrada superadas sin socio < 20%; tiempo de entrada > 2 a��os; errores por desconocimiento local > 5.
**Business_Impact:** Entrada lenta y costosa; errores evitables; menor penetraci��n; posible fracaso; oportunidad perdida por lentitud.
**Severity_Level:** High
**Metrics_To_Check:** % de barreras superadas; tiempo de entrada; errores por desconocimiento local; % de objetivos alcanzados.
**Diagnostic_Questions:** ��Se tiene un socio local? ��Se conoce el mercado? ��Las barreras son superables sin socio? ��Se necesita un partner?
**Recommended_Actions:** Buscar socio local (distribuidor, joint venture, agente); evaluar complementariedad; estructurar acuerdo beneficioso para ambos.
**Related_Patterns:** STR-073, STR-074, STR-077, STR-080, STR-085

### STR-076
**Pattern_Name:** Estrategia de Entrada Inadecuada
**Category:** Internacionalizaci��n
**Description:** La empresa elige un modo de entrada inadecuado (exportaci��n, joint venture, subsidiaria propia) para las condiciones del mercado objetivo, generando ineficiencias y riesgos.
**Typical_Causes:** Falta de an��lisis de modos de entrada; sesgo por modo familiar; imitaci��n de otras empresas; no evaluaci��n de riesgo/control.
**Observable_Symptoms:** El modo de entrada elegido no se ajusta al mercado; costos mayores a los previstos; problemas de control; conflictos con socios; alcance limitado.
**Early_Warning_Signals:** % de objetivos no alcanzados por modo de entrada inadecuado > 30%; conflictos con socios; costos > 120% de lo previsto; problemas de control.
**Business_Impact:** Ineficiencia; costos excesivos; conflictos; falta de control; resultados sub��ptimos; posible fracaso.
**Severity_Level:** High
**Metrics_To_Check:** Costo real vs presupuestado; % de objetivos alcanzados; nivel de conflicto; control sobre operaciones.
**Diagnostic_Questions:** ��El modo de entrada es adecuado para este mercado? ��Se evaluaron alternativas? ��Hay control suficiente? ��Los costos son los esperados?
**Recommended_Actions:** Evaluar modos de entrada (exportaci��n, licencia, joint venture, subsidiaria); seleccionar seg��n riesgo, control, inversi��n; ser flexible.
**Related_Patterns:** STR-073, STR-075, STR-077, STR-080, STR-085

### STR-077
**Pattern_Name:** Desconocimiento de Regulaciones Internacionales
**Category:** Internacionalizaci��n
**Description:** La empresa desconoce o subestima las regulaciones internacionales (aranceles, barreras no arancelarias, certificaciones, leyes laborales y fiscales), exponi��ndose a sanciones y multas.
**Typical_Causes:** Falta de asesor��a internacional; desconocimiento; subestimaci��n; apuro por exportar; no investigaci��n regulatoria.
**Observable_Symptoms:** Productos retenidos en aduana; multas por incumplimiento; costos regulatorios no presupuestados; retrasos; problemas legales.
**Early_Warning_Signals:** % de requisitos regulatorios identificados < 40%; multas o sanciones; % de productos retenidos en aduana > 10%; costos regulatorios > 120% de lo previsto.
**Business_Impact:** Multas; retrasos; p��rdida de productos; sobrecostos; da��o reputacional; posible prohibici��n de operar en el mercado.
**Severity_Level:** Critical
**Metrics_To_Check:** % de cumplimiento regulatorio; multas recibidas; % de retenci��n en aduana; costos regulatorios reales vs presupuesto.
**Diagnostic_Questions:** ��Se conocen las regulaciones del pa��s objetivo? ��Hay asesor��a? ��Se presupuestaron costos regulatorios? ��Hay incumplimientos?
**Recommended_Actions:** Investigar regulaciones del pa��s objetivo; contratar asesor��a internacional; certificar productos; presupuestar costos de cumplimiento.
**Related_Patterns:** STR-022, STR-073, STR-074, STR-076, STR-080

### STR-078
**Pattern_Name:** Internacionalizaci��n sin Equipo Internacional
**Category:** Internacionalizaci��n
**Description:** La empresa intenta internacionalizarse con el mismo equipo local, sin experiencia internacional, capacidades de idiomas o conocimiento de gesti��n intercultural.
**Typical_Causes:** Falta de inversi��n; subestimaci��n; confianza en capacidades existentes; no contrataci��n de talento internacional; presupuesto limitado.
**Observable_Symptoms:** Errores interculturales; problemas de comunicaci��n; negociaciones fallidas; equipo desbordado; decisiones lentas; falta de adaptaci��n.
**Early_Warning_Signals:** % de equipo con experiencia internacional < 10%; % de equipo con idiomas < 20%; errores interculturales; conflictos.
**Business_Impact:** Errores costosos; negociaciones fallidas; mala gesti��n internacional; p��rdida de oportunidades; fracaso en el mercado.
**Severity_Level:** High
**Metrics_To_Check:** % de equipo con experiencia internacional; % con idiomas; n��mero de errores interculturales; resultados internacionales.
**Diagnostic_Questions:** ��El equipo tiene experiencia internacional? ��Hay capacidades de idiomas? ��Se entiende la cultura local? ��Se necesita talento internacional?
**Recommended_Actions:** Contratar talento con experiencia internacional; capacitar en idiomas y cultura; formar equipo dedicado a internacional.
**Related_Patterns:** STR-073, STR-075, STR-079, STR-082, STR-086

### STR-079
**Pattern_Name:** Falta de Paciencia en Internacionalizaci��n
**Category:** Internacionalizaci��n
**Description:** La empresa espera resultados r��pidos de su proceso de internacionalizaci��n, abandonando prematuramente cuando los resultados no llegan en el corto plazo.
**Typical_Causes:** Expectativas irreales; cortoplacismo; falta de comprensi��n del tiempo de penetraci��n; presi��n de resultados; desesperaci��n.
**Observable_Symptoms:** Abandono de mercados antes de tiempo; cambios frecuentes de estrategia; expectativas no cumplidas; desaliento; ciclos de entrada-salida.
**Early_Warning_Signals:** Tiempo de permanencia en mercado < 2 a��os; % de mercados abandonados antes de alcanzar punto de equilibrio > 40%; cambio de estrategia anual.
**Business_Impact:** Inversiones perdidas; oportunidad no aprovechada; reputaci��n de inconstancia; desgaste del equipo; ciclos costosos de entrada y salida.
**Severity_Level:** High
**Metrics_To_Check:** Tiempo de permanencia promedio; % de mercados con punto de equilibrio alcanzado; paciencia de la direcci��n.
**Diagnostic_Questions:** ��Se esperan resultados demasiado r��pido? ��Hay paciencia para penetraci��n? ��Se abandona prematuramente? ��Las expectativas son realistas?
**Recommended_Actions:** Establecer expectativas realistas de tiempo de penetraci��n (3-5 a��os); medir progreso no solo resultados; compromiso sostenido.
**Related_Patterns:** STR-073, STR-076, STR-080, STR-082, STR-083

### STR-080
**Pattern_Name:** Subestimaci��n de Costos de Internacionalizaci��n
**Category:** Internacionalizaci��n
**Description:** La empresa subestima significativamente los costos reales de internacionalizaci��n (log��stica, aranceles, viajes, asesor��a, adaptaci��n), generando p��rdidas y falta de capital.
**Typical_Causes:** Falta de experiencia; optimismo; no presupuestar todos los costos; no considerar costos ocultos; mala planificaci��n financiera.
**Observable_Symptoms:** Costos reales muy superiores a los presupuestados; problemas de caja; necesidad de capital adicional; rentabilidad negativa en internacional.
**Early_Warning_Signals:** Desviaci��n de costos reales vs presupuesto > 40%; % de costos no presupuestados > 30%; necesidades de capital no previstas.
**Business_Impact:** P��rdidas; falta de capital; necesidad de financiamiento urgente; posible abandono; descr��dito del proyecto internacional.
**Severity_Level:** Critical
**Metrics_To_Check:** Desviaci��n de costos; % de costos no presupuestados; rentabilidad real vs proyectada; capital requerido adicional.
**Diagnostic_Questions:** ��Se presupuestaron todos los costos de internacionalizaci��n? ��Hay costos ocultos? ��Los costos reales superan el presupuesto? ��Hay capital suficiente?
**Recommended_Actions:** Presupuestar todos los costos (investigaci��n, viajes, asesor��a, aranceles, log��stica, adaptaci��n); agregar colch��n de contingencia del 30%.
**Related_Patterns:** STR-073, STR-077, STR-079, STR-083, STR-098

### STR-081
**Pattern_Name:** Estrategia de Precios Internacional Incorrecta
**Category:** Internacionalizaci��n
**Description:** La empresa utiliza la misma estrategia de precios del mercado local en mercados internacionales, sin considerar poder adquisitivo, competencia local, impuestos y costos log��sticos.
**Typical_Causes:** Falta de an��lisis de pricing internacional; simplificaci��n; no considerar elasticidad local; costos log��sticos no incorporados; competidores locales no analizados.
**Observable_Symptoms:** Precio demasiado alto para el mercado local (baja penetraci��n) o demasiado bajo (margen insuficiente); m��rgenes no rentables; quejas de precio.
**Early_Warning_Signals:** % de penetraci��n vs precio relativo fuera de rango; margen en internacional < 50% del margen local; elasticidad precio no considerada.
**Business_Impact:** Baja penetraci��n o p��rdidas; rentabilidad insuficiente; posicionamiento incorrecto; fracaso comercial.
**Severity_Level:** Critical
**Metrics_To_Check:** Precio relativo en mercado local; margen internacional vs local; penetraci��n esperada vs real; elasticidad precio local.
**Diagnostic_Questions:** ��La estrategia de precios es adecuada para el mercado local? ��Considera poder adquisitivo, competencia y costos? ��El margen es suficiente?
**Recommended_Actions:** Desarrollar estrategia de precios por mercado; considerar poder adquisitivo, competencia, aranceles, log��stica; adaptar precio localmente.
**Related_Patterns:** STR-010, STR-073, STR-074, STR-080, STR-083

### STR-082
**Pattern_Name:** Falta de Estrategia de Marca Global
**Category:** Internacionalizaci��n
**Description:** La empresa no define una estrategia de marca global (marca ��nica vs marcas locales, posicionamiento global vs local), generando confusi��n e inconsistencia en diferentes mercados.
**Typical_Causes:** Falta de planificaci��n de marca internacional; descentralizaci��n; inconsistencias; no definici��n de arquitectura de marca global.
**Observable_Symptoms:** Marca percibida diferente en cada mercado; conflictos de naming; posicionamiento inconsistente; p��rdida de econom��as de escala en marketing.
**Early_Warning_Signals:** % de mercados con posicionamiento de marca consistente < 30%; conflictos de marca registrada en otros pa��ses; % de marca global vs local.
**Business_Impact:** Inconsistencia de marca; p��rdida de econom��as de escala; confusi��n del cliente; conflictos legales de marca; menor valor de marca global.
**Severity_Level:** High
**Metrics_To_Check:** % de mercados con marca consistente; reconocimiento de marca global; conflictos de marca; inversi��n en marketing global vs local.
**Diagnostic_Questions:** ��Hay estrategia de marca global? ��La marca es consistente entre mercados? ��Hay conflictos de naming? ��Se aprovechan econom��as de escala de marca?
**Recommended_Actions:** Definir estrategia de marca global; decidir arquitectura de marca (monol��tica, endorsed, house of brands); registrar marca en todos los mercados.
**Related_Patterns:** STR-028, STR-031, STR-074, STR-078, STR-082

### STR-083
**Pattern_Name:** Internacionalizaci��n sin Plan de Salida
**Category:** Internacionalizaci��n
**Description:** La empresa ingresa a mercados internacionales sin definir condiciones o criterios de salida, quedando atrapada en mercados no rentables sin poder retirarse ordenadamente.
**Typical_Causes:** Optimismo; falta de planificaci��n de riesgos; no definici��n de criterios de �xito/fracaso; compromiso emocional; inversiones hundidas.
**Observable_Symptoms:** Mercados no rentables pero la empresa no se retira; p��rdidas recurrentes; recursos atrapados; imposibilidad de salir sin grandes p��rdidas.
**Early_Warning_Signals:** Sin criterios de salida definidos; % de mercados no rentables > 40%; tiempo en mercado no rentable > 2 a��os; compromiso emocional.
**Business_Impact:** P��rdidas recurrentes; recursos atrapados; distracci��n de mercados rentables; imposibilidad de salir ordenadamente.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de criterios de salida; % de mercados no rentables; tiempo en mercados no rentables; costo de salida.
**Diagnostic_Questions:** ��Hay criterios de salida definidos? ��Hay mercados no rentables que no se cierran? ��Se puede salir ordenadamente? ��Hay compromiso emocional?
**Recommended_Actions:** Definir criterios de salida antes de entrar (tiempo para punto de equilibrio, ROI m��nimo); revisar peri��dicamente; tener plan de salida.
**Related_Patterns:** STR-072, STR-073, STR-079, STR-080, STR-083

### STR-084
**Pattern_Name:** Internacionalizaci��n sin Apoyo de la Organizaci��n
**Category:** Internacionalizaci��n
**Description:** La iniciativa de internacionalizaci��n no cuenta con el apoyo del resto de la organizaci��n, que prioriza el mercado local, dejando sin recursos ni atenci��n el proyecto internacional.
**Typical_Causes:** Estrategia no comunicada; falta de compromiso del liderazgo; prioridades locales; resistencia al cambio; cultura local-c��ntrica.
**Observable_Symptoms:** El equipo local no apoya la internacionalizaci��n; recursos no se asignan; la internacionalizaci��n es vista como distracci��n; conflictos.
**Early_Warning_Signals:** % de recursos asignados a internacional vs plan < 50%; % de gerentes locales que apoyan internacional < 30%; conflictos.
**Business_Impact:** Internacionalizaci��n sin recursos ni apoyo; fracaso; desgaste del equipo internacional; conflictos internos; oportunidad perdida.
**Severity_Level:** High
**Metrics_To_Check:** % de recursos asignados vs plan; % de apoyo del liderazgo; n��mero de conflictos; avance del plan de internacionalizaci��n.
**Diagnostic_Questions:** ��La organizaci��n apoya la internacionalizaci��n? ��Hay recursos suficientes? ��El equipo local prioriza el mercado local? ��Hay conflicto?
**Recommended_Actions:** Comunicar visi��n de internacionalizaci��n; asegurar compromiso del liderazgo; asignar recursos dedicados; incentivar apoyo; gestionar conflictos.
**Related_Patterns:** STR-036, STR-078, STR-082, STR-084, STR-121


## Fusiones y Adquisiciones

### STR-085
**Pattern_Name:** Due Diligence Insuficiente
**Category:** Fusiones y Adquisiciones
**Description:** La empresa realiza un proceso de due diligence superficial o incompleto antes de adquirir o fusionarse, descubriendo problemas ocultos (deudas, litigios, pasivos) despu��s del cierre.
**Typical_Causes:** Apuro por cerrar el trato; sobreconfianza; falta de experiencia; presi��n del vendedor; optimismo; recursos limitados.
**Observable_Symptoms:** Problemas descubiertos post-adquisici��n; pasivos no revelados; litigios ocultos; deudas no declaradas; resultados reales muy diferentes a los proyectados.
**Early_Warning_Signals:** % de due diligence realizado vs necesario < 50%; % de hallazgos post-cierre > 30%; desviaci��n de resultados reales vs proyectados > 40%.
**Business_Impact:** P��rdida de inversi��n; pasivos inesperados; litigios; sobreprecio pagado; fracaso de la operaci��n; da��o financiero.
**Severity_Level:** Critical
**Metrics_To_Check:** % de due diligence completado; n��mero de hallazgos post-cierre; desviaci��n de resultados; costos post-adquisici��n no previstos.
**Diagnostic_Questions:** ��El due diligence fue completo? ��Se descubrieron problemas despu��s? ��Se revisaron finanzas, legales, operaciones? ��Se usaron expertos externos?
**Recommended_Actions:** Realizar due diligence exhaustivo (financiero, legal, operativo, fiscal, laboral, tecnol��gico); contratar expertos; no apurarse; verificar todo.
**Related_Patterns:** STR-086, STR-087, STR-088, STR-092, STR-096

### STR-086
**Pattern_Name:** Integraci��n Post-Fusi��n Deficiente
**Category:** Fusiones y Adquisiciones
**Description:** Despu��s de la adquisici��n o fusi��n, el proceso de integraci��n es deficiente o inexistente, dejando las empresas operando en silos sin capturar sinergias ni eficiencias.
**Typical_Causes:** Falta de plan de integraci��n; subestimaci��n de complejidad; diferencias culturales; resistencia al cambio; falta de liderazgo.
**Observable_Symptoms:** Las empresas operan separadas; sinergias no se capturan; duplicidad de funciones; conflictos culturales; integraci��n lenta o nula.
**Early_Warning_Signals:** % de sinergias capturadas < 30%; tiempo de integraci��n > 2 a��os; rotaci��n de personal clave > 30%; conflictos.
**Business_Impact:** Sinergias no materializadas; ineficiencias; costos duplicados; p��rdida de talento; valor de la operaci��n no realizado.
**Severity_Level:** Critical
**Metrics_To_Check:** % de sinergias capturadas; tiempo de integraci��n; rotaci��n post-fusi��n; eficiencia operativa post-integraci��n.
**Diagnostic_Questions:** ��Hay plan de integraci��n? ��Se est��n capturando sinergias? ��Hay duplicidad? ��La integraci��n avanza seg��n lo planeado? ��Hay conflictos culturales?
**Recommended_Actions:** Desarrollar plan de integraci��n detallado antes del cierre; asignar responsable de integraci��n; capturar sinergias r��pidamente; gestionar cultura.
**Related_Patterns:** STR-085, STR-087, STR-089, STR-092, STR-096

### STR-087
**Pattern_Name:** Valoraci��n Incorrecta del Objetivo
**Category:** Fusiones y Adquisiciones
**Description:** La empresa valora incorrectamente el objetivo de adquisici��n, pagando un precio excesivo basado en supuestos demasiado optimistas o m��todos de valoraci��n inadecuados.
**Typical_Causes:** Falta de experiencia en valoraci��n; optimismo; sesgo emocional; presi��n por cerrar; m��todos incorrectos; sin asesor��a independiente.
**Observable_Symptoms:** Precio pagado muy superior al valor real; sinergias sobrevaloradas; proyecciones irreales; imposibilidad de recuperar inversi��n.
**Early_Warning_Signals:** Precio/EBITDA pagado > 2x el promedio del sector; % de sinergias proyectadas vs realistas; desviaci��n de proyecciones post-cierre.
**Business_Impact:** Sobreprecio pagado; imposibilidad de recuperar inversi��n; diluci��n de valor para accionistas; deterioro de goodwill; p��rdida.
**Severity_Level:** Critical
**Metrics_To_Check:** M��ltiplo pagado vs sector; % de sinergias reales vs proyectadas; ROI de la adquisici��n; deterioro de goodwill.
**Diagnostic_Questions:** ��La valoraci��n fue correcta? ��Se pag�� un precio justo? ��Las proyecciones eran realistas? ��Hubo asesor��a independiente? ��Hay deterioro?
**Recommended_Actions:** Utilizar m��todos de valoraci��n m��ltiples (DCF, m��ltiplos, transacciones comparables); obtener asesor��a independiente; ser conservador en proyecciones.
**Related_Patterns:** STR-085, STR-088, STR-090, STR-096, STR-104

### STR-088
**Pattern_Name:** Choque Cultural Post-Adquisici��n
**Category:** Fusiones y Adquisiciones
**Description:** Las diferencias culturales entre las empresas adquiriente y adquirida generan conflictos, rotaci��n de talento clave y p��rdida del valor de la adquisici��n.
**Typical_Causes:** No evaluaci��n de compatibilidad cultural; imposici��n de cultura; falta de integraci��n cultural; liderazgo insensible; diferencias no gestionadas.
**Observable_Symptoms:** Conflictos entre equipos; rotaci��n de personal clave de la adquirida; p��rdida de know-how; clima laboral negativo; resultados por debajo de lo esperado.
**Early_Warning_Signals:** Rotaci��n en adquirida post-cierre > 30% anual; % de conflictos reportados; % de empleados de adquirida insatisfechos > 40%; p��rdida de talento.
**Business_Impact:** P��rdida de talento y know-how; deterioro del valor de la adquisici��n; conflictos; baja productividad; fracaso de la integraci��n.
**Severity_Level:** Critical
**Metrics_To_Check:** Rotaci��n post-adquisici��n; % de conflictos; clima laboral; retenci��n de talento clave; productividad post-integraci��n.
**Diagnostic_Questions:** ��Se evalu�� la compatibilidad cultural? ��Hay conflictos culturales? ��Se est�� perdiendo talento? ��C��mo es el clima post-adquisici��n?
**Recommended_Actions:** Evaluar compatibilidad cultural pre-adquisici��n; planificar integraci��n cultural; respetar diferencias; retener talento clave; comunicar.
**Related_Patterns:** STR-085, STR-086, STR-089, STR-092, STR-096

### STR-089
**Pattern_Name:** Fusi��n por Ego sin Sinergias Reales
**Category:** Fusiones y Adquisiciones
**Description:** La fusi��n o adquisici��n se realiza por ego del due��o (crear un imperio, ganar prestigio) sin que existan sinergias reales que justifiquen la operaci��n.
**Typical_Causes:** Ego del fundador; af��n de protagonismo; deseo de tama��o por el tama��o; falta de an��lisis racional; presi��n de asesores.
**Observable_Symptoms:** No hay justificaci��n estrat��gica clara; sinergias no identificadas; operaci��n no mejora el negocio; resultados posteriores pobres.
**Early_Warning_Signals:** % de sinergias identificadas vs precio pagado < 10%; sin justificaci��n estrat��gica clara; operaci��n impulsada por el due��o sin an��lisis.
**Business_Impact:** P��rdida de inversi��n; distracci��n; falta de foco; recursos desperdiciados; no creaci��n de valor; posible fracaso.
**Severity_Level:** Critical
**Metrics_To_Check:** Sinergias identificadas vs precio; justificaci��n estrat��gica; ROI de la operaci��n; valor creado post-fusi��n.
**Diagnostic_Questions:** ��La fusi��n tiene justificaci��n estrat��gica? ��Hay sinergias reales? ��Se debe al ego del due��o? ��Crear�� valor? ��Hay an��lisis racional?
**Recommended_Actions:** Evaluar racionalmente cada operaci��n; separar ego de negocios; solo hacer operaciones con sinergias claras; involucrar asesores objetivos.
**Related_Patterns:** STR-085, STR-087, STR-088, STR-096, STR-109

### STR-090
**Pattern_Name:** Adquisici��n sin Plan de Retenci��n de Talento Clave
**Category:** Fusiones y Adquisiciones
**Description:** La empresa adquirente no implementa un plan de retenci��n para el talento clave de la empresa adquirida, perdiendo a las personas que generaban el valor de la adquisici��n.
**Typical_Causes:** Subestimaci��n; falta de plan; suposici��n de que se quedar��n; no ofrecer incentivos; choque cultural.
**Observable_Symptoms:** Talento clave de la adquirida se va; el know-how se pierde; el valor de la adquisici��n se diluye; resultados caen; arrepentimiento.
**Early_Warning_Signals:** % de talento clave retenido a 12 meses < 50%; rotaci��n de directivos de adquirida > 40%; salidas no planificadas.
**Business_Impact:** P��rdida del valor de la adquisici��n; fuga de conocimiento; clientes se van con el talento; imposibilidad de capturar sinergias.
**Severity_Level:** Critical
**Metrics_To_Check:** % de talento clave retenido; rotaci��n post-adquisici��n; satisfacci��n del talento adquirido; resultados de la adquirida.
**Diagnostic_Questions:** ��Hay plan de retenci��n de talento clave? ��Se est�� yendo el talento? ��Se ofrecen incentivos? ��Se identifica el talento cr��tico?
**Recommended_Actions:** Identificar talento clave antes del cierre; ofrecer paquetes de retenci��n (bonos, opciones, roles); plan de integraci��n personalizado.
**Related_Patterns:** STR-085, STR-086, STR-088, STR-092, STR-096

### STR-091
**Pattern_Name:** Endeudamiento Excesivo para Adquisici��n
**Category:** Fusiones y Adquisiciones
**Description:** La empresa se apalanca excesivamente para financiar la adquisici��n, asumiendo una deuda que compromete la salud financiera y limita la capacidad de inversi��n futura.
**Typical_Causes:** Falta de capital propio; presi��n por crecer; optimismo sobre sinergias; subestimaci��n de riesgos; mala estructuraci��n financiera.
**Observable_Symptoms:** Deuda muy alta post-adquisici��n; servicio de deuda consume caja; poca flexibilidad financiera; imposibilidad de invertir; estr��s.
**Early_Warning_Signals:** Deuda/EBITDA > 4x; cobertura de intereses < 2x; % de caja destinada a servicio de deuda > 50%; covenants en riesgo.
**Business_Impact:** Estr��s financiero; riesgo de default; falta de flexibilidad; imposibilidad de invertir; posible p��rdida de control; crisis.
**Severity_Level:** Critical
**Metrics_To_Check:** Deuda/EBITDA; cobertura de intereses; % de caja para deuda; cumplimiento de covenants; flexibilidad financiera.
**Diagnostic_Questions:** ��El nivel de deuda es sostenible? ��Hay suficiente caja para pagar? ��Los covenants est��n en riesgo? ��Hay flexibilidad? ��Qu�� pasa si las sinergias no se materializan?
**Recommended_Actions:** Limitar apalancamiento; mantener colch��n de caja; estructuraci��n financiera conservadora; proyectar escenarios adversos.
**Related_Patterns:** STR-068, STR-085, STR-087, STR-096, STR-104

### STR-092
**Pattern_Name:** Falta de Plan de Sinergias Post-Adquisici��n
**Category:** Fusiones y Adquisiciones
**Description:** La empresa adquiere sin tener un plan detallado de c��mo capturar las sinergias identificadas en la due diligence, dejando el valor de la operaci��n sin materializar.
**Typical_Causes:** Falta de planificaci��n; subestimaci��n de esfuerzo; equipos no preparados; no asignaci��n de responsables; ausencia de m��tricas.
**Observable_Symptoms:** Sinergias no se materializan; resultados post-adquisici��n por debajo de lo proyectado; no se identifican responsables; falta de seguimiento.
**Early_Warning_Signals:** % de sinergias capturadas vs plan < 30%; sin responsable de sinergias; sin KPIs de sinergias; % de proyectos de integraci��n retrasados.
**Business_Impact:** Valor de la operaci��n no realizado; sobreprecio efectivo pagado; resultados insatisfactorios; p��rdida de inversi��n.
**Severity_Level:** Critical
**Metrics_To_Check:** % de sinergias capturadas; % de proyectos de integraci��n en tiempo; ROI real vs proyectado; responsible asignado.
**Diagnostic_Questions:** ��Hay plan de captura de sinergias? ��Hay responsables? ��Se est��n materializando? ��Hay seguimiento? ��Hay KPIs?
**Recommended_Actions:** Desarrollar plan detallado de captura de sinergias; asignar responsables; establecer KPIs; trackear mensualmente; reportar avances.
**Related_Patterns:** STR-085, STR-086, STR-087, STR-092, STR-096

### STR-093
**Pattern_Name:** Adquisiciones No Relacionadas (Conglomerado sin Sentido)
**Category:** Fusiones y Adquisiciones
**Description:** La empresa adquiere negocios no relacionados con su core, sin capacidad de gesti��n ni sinergias, creando un conglomerado sin l��gica estrat��gica que destruye valor.
**Typical_Causes:** Ego; diversificaci��n sin criterio; oportunismo; falta de foco; deseo de crecimiento r��pido; subestimaci��n de complejidad.
**Observable_Symptoms:** Portafolio de negocios diversos sin relaci��n; falta de sinergias; gesti��n compleja; resultados mediocres; descuido del core.
**Early_Warning_Signals:** % de ingresos de negocios no relacionados > 30%; falta de sinergias entre unidades; ROIC de adquisiciones < costo de capital.
**Business_Impact:** Complejidad de gesti��n; falta de foco; recursos diluidos; p��rdida de valor; desempe��o inferior; posible fracaso.
**Severity_Level:** High
**Metrics_To_Check:** % de negocios relacionados vs no relacionados; ROIC por unidad; sinergias entre unidades; complejidad de gesti��n.
**Diagnostic_Questions:** ��Las adquisiciones est��n relacionadas con el core? ��Hay sinergias? ��Hay capacidad de gesti��n para negocios diversos? ��Tiene l��gica estrat��gica?
**Recommended_Actions:** Adquirir solo negocios relacionados o con sinergias claras; tener capacidad de gesti��n; evitar conglomerados sin l��gica.
**Related_Patterns:** STR-016, STR-020, STR-085, STR-089, STR-096

### STR-094
**Pattern_Name:** Proceso de Adquisici��n sin Disciplina
**Category:** Fusiones y Adquisiciones
**Description:** La empresa no tiene un proceso disciplinado de identificaci��n, evaluaci��n y ejecuci��n de adquisiciones, realizando operaciones apresuradas o mal evaluadas.
**Typical_Causes:** Falta de experiencia; procesos ad-hoc; improvisaci��n; presi��n; oportunismo; ausencia de pipeline de targets.
**Observable_Symptoms:** Operaciones mal estructuradas; decisiones apresuradas; due diligence incompleto; errores de ejecuci��n; resultados pobres.
**Early_Warning_Signals:** Sin proceso formal de M&A; % de operaciones con proceso completo < 30%; decisiones en < 1 mes; sin pipeline.
**Business_Impact:** Malas decisiones de inversi��n; errores costosos; p��rdida de oportunidades; resultados inconsistentes; fracasos.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de proceso formal; % de operaciones con proceso completo; tiempo de evaluaci��n; % de aciertos.
**Diagnostic_Questions:** ��Hay proceso disciplinado de M&A? ��Se eval��an sistem��ticamente? ��Las decisiones son apresuradas? ��Hay pipeline? ��Se aprende de errores?
**Recommended_Actions:** Implementar proceso formal de M&A (identificaci��n, screening, due diligence, negociaci��n, integraci��n); mantener pipeline; disciplinar.
**Related_Patterns:** STR-085, STR-087, STR-092, STR-096, STR-128

### STR-095
**Pattern_Name:** Confianza Excesiva en el Vendedor durante DD
**Category:** Fusiones y Adquisiciones
**Description:** La empresa adquirente conf��a excesivamente en la informaci��n proporcionada por el vendedor sin verificarla independientemente, descubriendo problemas despu��s del cierre.
**Typical_Causes:** Confianza ingenua; falta de escepticismo; relaci��n personal con vendedor; presi��n; pereza; no verificaci��n independiente.
**Observable_Symptoms:** Informaci��n del vendedor incorrecta; problemas no revelados; descubrimientos post-cierre; sensaci��n de enga��o; p��rdidas.
**Early_Warning_Signals:** % de informaci��n del vendedor verificada < 50%; % de hallazgos post-cierre no revelados > 20%; dependencia de datos del vendedor.
**Business_Impact:** P��rdida de inversi��n; pasivos ocultos; disputas legales; desconfianza; fracaso de la operaci��n.
**Severity_Level:** Critical
**Metrics_To_Check:** % de informaci��n verificada; n��mero de hallazgos post-cierre; disputas; % de datos del vendedor incorrectos.
**Diagnostic_Questions:** ��Se est�� confiando demasiado en el vendedor? ��Se verifica la informaci��n independientemente? ��Hay escepticismo? ��Se descubrieron problemas no revelados?
**Recommended_Actions:** Verificar toda la informaci��n del vendedor de forma independiente; mantener escepticismo profesional; contratar asesores externos.
**Related_Patterns:** STR-085, STR-087, STR-094, STR-096, STR-128

### STR-096
**Pattern_Name:** Falta de Learning Post-Adquisici��n
**Category:** Fusiones y Adquisiciones
**Description:** La empresa no realiza una revisi��n post-adquisici��n para aprender de la experiencia, repitiendo los mismos errores en operaciones posteriores.
**Typical_Causes:** Falta de cultura de aprendizaje; apuro por siguiente operaci��n; no documentaci��n; arrogancia; falta de procesos de revisi��n.
**Observable_Symptoms:** Errores se repiten en cada adquisici��n; no hay documentaci��n de lecciones aprendidas; mismo tipo de problemas recurrente; no mejora.
**Early_Warning_Signals:** Sin revisi��n post-adquisici��n; % de errores recurrentes > 50%; no documentaci��n de lecciones; equipo no mejora.
**Business_Impact:** Errores repetidos; ineficiencia; resultados sistem��ticamente peores; falta de mejora; cultura de no aprendizaje.
**Severity_Level:** Medium
**Metrics_To_Check:** Existencia de revisi��n post; % de errores recurrentes; documentaci��n de lecciones; mejora en resultados de adquisiciones.
**Diagnostic_Questions:** ��Se hace revisi��n post-adquisici��n? ��Se documentan lecciones? ��Los errores se repiten? ��Hay mejora en el tiempo?
**Recommended_Actions:** Realizar revisi��n post-adquisici��n sistem��tica; documentar lecciones aprendidas; compartir con equipo; ajustar procesos.
**Related_Patterns:** STR-085, STR-094, STR-095, STR-128, STR-132


## Asignaci��n de Recursos

### STR-097
**Pattern_Name:** Asignaci��n de Recursos sin Criterio Estrat��gico
**Category:** Asignaci��n de Recursos
**Description:** La empresa asigna recursos (capital, tiempo, talento) sin criterios estrat��gicos claros, bas��ndose en inercia hist��rica, presi��n o favoritismo, en lugar de prioridades estrat��gicas.
**Typical_Causes:** Falta de planificaci��n; presupuesto incremental; cultura de "siempre se hizo as��"; lobby interno; ausencia de criterios objetivos.
**Observable_Symptoms:** Recursos no siguen la estrategia; se financian proyectos sin valor estrat��gico; inercia en asignaci��n; recursos en ��reas equivocadas.
**Early_Warning_Signals:** % de recursos asignados seg��n criterios estrat��gicos < 30%; % de presupuesto en iniciativas estrat��gicas < 40%; desalineaci��n.
**Business_Impact:** Recursos malgastados; estrategia no ejecutada; oportunidades perdidas; eficiencia sub��ptima; resultados inferiores.
**Severity_Level:** Critical
**Metrics_To_Check:** % de recursos alineados con estrategia; % de presupuesto estrat��gico; ROI por asignaci��n; desviaci��n de plan estrat��gico.
**Diagnostic_Questions:** ��Los recursos se asignan seg��n estrategia? ��Hay criterios claros? ��Hay inercia hist��rica? ��Los proyectos estrat��gicos est��n financiados?
**Recommended_Actions:** Vincular asignaci��n de recursos a plan estrat��gico; establecer criterios objetivos; revisar peri��dicamente; eliminar gasto no estrat��gico.
**Related_Patterns:** STR-098, STR-099, STR-100, STR-104, STR-109

### STR-098
**Pattern_Name:** Sobredimensi��n de Estructura Fija
**Category:** Asignaci��n de Recursos
**Description:** La empresa mantiene una estructura de costos fijos sobredimensionada en relaci��n a sus ingresos, consumiendo recursos que deber����an destinarse a iniciativas estrat��gicas o crecimiento.
**Typical_Causes:** Crecimiento pasado que dej�� estructura; falta de ajuste en crisis; decisiones de personal sin criterio; gastos fijos no revisados.
**Observable_Symptoms:** Gastos fijos muy altos; estructura pesada; poca flexibilidad; recursos atrapados en costos fijos; dificultad para invertir.
**Early_Warning_Signals:** Gastos fijos/ventas > 30%; % de recursos disponibles para inversi��n < 10%; estructura no ajustada a ingresos actuales.
**Business_Impact:** Falta de flexibilidad; recursos consumidos por estructura; poca capacidad de inversi��n; rentabilidad comprimida; vulnerabilidad en ca��das.
**Severity_Level:** High
**Metrics_To_Check:** Gastos fijos/ventas; % de gastos discrecionales; flexibilidad de costos; margen de contribuci��n.
**Diagnostic_Questions:** ��La estructura es proporcional a los ingresos? ��Hay gastos fijos excesivos? ��Hay flexibilidad? ��Los recursos est��n atrapados en estructura?
**Recommended_Actions:** Revisar y optimizar estructura de costos fijos; tercerizar; hacer variable; ajustar a ingresos reales; liberar recursos para inversi��n.
**Related_Patterns:** STR-097, STR-100, STR-104, STR-105, STR-110

### STR-099
**Pattern_Name:** Subinversi��n en ��reas Estrat��gicas Clave
**Category:** Asignaci��n de Recursos
**Description:** La empresa no invierte lo suficiente en ��reas cr��ticas para su estrategia (tecnolog��a, marketing, talento, I+D), priorizando el corto plazo sobre el largo plazo.
**Typical_Causes:** Cortoplacismo; presi��n por resultados inmediatos; falta de visi��n; priorizar distribuci��n de utilidades; no entender la importancia de la inversi��n.
**Observable_Symptoms:** ��reas estrat��gicas con presupuesto insuficiente; se recorta inversi��n en momentos dif��ciles; falta de capacidades futuras; deterioro competitivo.
**Early_Warning_Signals:** Inversi��n en ��reas estrat��gicas/ventas < 5%; % de presupuesto recortado en ��reas estrat��gicas en crisis > 30%; gap de inversi��n vs competidores.
**Business_Impact:** P��rdida de competitividad futura; obsolescencia; incapacidad de crecer; dependencia de ventajas actuales; deterioro gradual.
**Severity_Level:** Critical
**Metrics_To_Check:** Inversi��n en ��reas estrat��gicas/ventas; % de presupuesto de largo plazo; gap vs competidores; % de ingresos de futuras capacidades.
**Diagnostic_Questions:** ��Se invierte lo suficiente en ��reas estrat��gicas? ��Hay cortoplacismo? ��C��mo se compara con competidores? ��Se protegen las inversiones estrat��gicas?
**Recommended_Actions:** Proteger inversiones estrat��gicas; presupuestar separado de operaci��n; benchmarkear inversi��n; educar sobre importancia de inversi��n de largo plazo.
**Related_Patterns:** STR-039, STR-055, STR-097, STR-098, STR-109

### STR-100
**Pattern_Name:** Falta de Zero-Based Budgeting
**Category:** Asignaci��n de Recursos
**Description:** La empresa elabora el presupuesto sobre la base del a��o anterior con ajustes incrementales, arrastrando gastos ineficientes y perpetuando asignaciones hist��ricas sin cuestionarlas.
**Typical_Causes:** Pereza presupuestaria; cultura de "siempre se hizo as��"; falta de revisi��n; evitar conflictos; comodidad.
**Observable_Symptoms:** Partidas presupuestarias que no se cuestionan; gastos hist��ricos perpetuados; ineficiencias no detectadas; falta de revisi��n cr��tica.
**Early_Warning_Signals:** % de presupuesto sin revisi��n cr��tica > 50%; % de gastos hist��ricos perpetuados > 40%; % de presupuesto con zero-based = 0%.
**Business_Impact:** Ineficiencias perpetuadas; recursos mal asignados; imposibilidad de redirigir fondos; gastos innecesarios; rentabilidad sub��ptima.
**Severity_Level:** High
**Metrics_To_Check:** % de presupuesto revisado desde cero; % de gastos hist��ricos; eficiencia del gasto; % de recursos liberados.
**Diagnostic_Questions:** ��El presupuesto se hace desde cero o es incremental? ��Se cuestionan los gastos hist��ricos? ��Hay ineficiencias perpetuadas?
**Recommended_Actions:** Implementar Zero-Based Budgeting peri��dicamente; justificar cada gasto desde cero; liberar recursos de actividades no esenciales.
**Related_Patterns:** STR-097, STR-098, STR-099, STR-104, STR-110

### STR-101
**Pattern_Name:** Asignaci��n de Talento a Proyectos Incorrectos
**Category:** Asignaci��n de Recursos
**Description:** La empresa asigna su mejor talento a proyectos de baja prioridad estrat��gica, mientras que iniciativas cr��ticas carecen de las personas adecuadas, desperdiciando capacidad.
**Typical_Causes:** Falta de priorizaci��n; no vinculaci��n talento-estrategia; pol��tica interna; asignaci��n por disponibilidad no por importancia.
**Observable_Symptoms:** Proyectos cr��ticos con personal inadecuado; proyectos secundarios con el mejor equipo; talento mal utilizado; cuellos de botella.
**Early_Warning_Signals:** % de talento clave en proyectos estrat��gicos < 40%; % de proyectos cr��ticos con personal adecuado < 50%; desalineaci��n.
**Business_Impact:** Estrategia no ejecutada por falta de talento adecuado; talento desperdiciado; proyectos cr��ticos retrasados; resultados sub��ptimos.
**Severity_Level:** High
**Metrics_To_Check:** % de talento clave en iniciativas estrat��gicas; % de proyectos cr��ticos con staffing adecuado; productividad del talento.
**Diagnostic_Questions:** ��El mejor talento est�� en los proyectos m��s importantes? ��Hay desalineaci��n? ��Los proyectos cr��ticos tienen el personal adecuado?
**Recommended_Actions:** Mapear talento clave y asignarlo a prioridades estrat��gicas; liberar talento de actividades de bajo valor; revisar asignaci��n trimestralmente.
**Related_Patterns:** STR-097, STR-099, STR-104, STR-109, STR-119

### STR-102
**Pattern_Name:** Exceso de Proyectos Simult��neos
**Category:** Asignaci��n de Recursos
**Description:** La empresa inicia demasiados proyectos simult��neamente sin recursos suficientes para todos, generando avances lentos, equipos sobrecargados y baja tasa de finalizaci��n.
**Typical_Causes:** Falta de priorizaci��n; entusiasmo; no decir no; presi��n de m��ltiples frentes; ausencia de capacidad real.
**Observable_Symptoms:** Muchos proyectos en curso, pocos terminados; equipos sobrecargados; avances lentos; proyectos abandonados; recursos diluidos.
**Early_Warning_Signals:** N��mero de proyectos activos > capacidad de ejecuci��n; % de proyectos completados a tiempo < 30%; % de recursos de PM > 100%.
**Business_Impact:** Baja tasa de finalizaci��n; recursos diluidos; estr��s del equipo; proyectos abandonados; inversi��n desperdiciada; resultados no materializados.
**Severity_Level:** High
**Metrics_To_Check:** N��mero de proyectos activos vs capacidad; % completados a tiempo; % de recursos comprometidos; WIP (work in progress).
**Diagnostic_Questions:** ��Hay demasiados proyectos simult��neos? ��Se completan los proyectos? ��Los equipos est��n sobrecargados? ��Hay priorizaci��n? ��Se dice no?
**Recommended_Actions:** Limitar WIP; priorizar estrictamente; decir no a proyectos no prioritarios; secuenciar iniciativas; liberar recursos antes de empezar nuevos.
**Related_Patterns:** STR-097, STR-101, STR-104, STR-109, STR-114

### STR-103
**Pattern_Name:** Falta de Seguimiento de ROI en Inversiones
**Category:** Asignaci��n de Recursos
**Description:** La empresa no realiza seguimiento del retorno de inversi��n de sus asignaciones de capital, desconociendo qu�� inversiones generan valor y cu��les destruyen.
**Typical_Causes:** Falta de sistemas; cultura de "invertir y olvidar"; no medici��n post-inversi��n; ausencia de KPIs; informalidad.
**Observable_Symptoms:** No se sabe qu�� inversiones rinden; se repiten inversiones fallidas; no hay aprendizaje; decisiones de inversi��n sin feedback.
**Early_Warning_Signals:** % de inversiones con seguimiento de ROI < 20%; % de inversiones repetidas fallidas; sin sistema de evaluaci��n post-inversi��n.
**Business_Impact:** Decisiones de inversi��n sin informaci��n; errores repetidos; capital mal asignado; rendimiento sub��ptimo; falta de accountability.
**Severity_Level:** High
**Metrics_To_Check:** % de inversiones con ROI medido; % de inversiones con revisi��n post; tasa de acierto en inversiones; ROI promedio.
**Diagnostic_Questions:** ��Se hace seguimiento del ROI de las inversiones? ��Se sabe qu�� inversiones funcionan? ��Hay revisi��n post-inversi��n?
**Recommended_Actions:** Implementar seguimiento de ROI de todas las inversiones significativas; revisar peri��dicamente; aprender de errores; ajustar criterios.
**Related_Patterns:** STR-097, STR-099, STR-104, STR-128, STR-132

### STR-104
**Pattern_Name:** Capital Atrapado en Activos No Estrat��gicos
**Category:** Asignaci��n de Recursos
**Description:** La empresa mantiene capital inmovilizado en activos no estrat��gicos (propiedades, equipos, inventarios) que podr����a liberarse para inversiones m��s productivas.
**Typical_Causes:** Apego a activos; falta de an��lisis de rotaci��n; subutilizaci��n; no considerar venta de activos no estrat��gicos; inercia.
**Observable_Symptoms:** Activos subutilizados; capital inmovilizado; baja rotaci��n de activos; dificultad para financiar iniciativas estrat��gicas; balance pesado.
**Early_Warning_Signals:** Rotaci��n de activos fijos < 2x; % de activos subutilizados > 20%; % de activos no estrat��gicos > 30%; capital disponible limitado.
**Business_Impact:** Capital improductivo; menor ROIC; falta de recursos para inversiones estrat��gicas; balance ineficiente; rentabilidad sub��ptima.
**Severity_Level:** High
**Metrics_To_Check:** Rotaci��n de activos fijos; % de activos no estrat��gicos; ROIC; % de activos subutilizados.
**Diagnostic_Questions:** ��Hay activos no estrat��gicos que atrapan capital? ��Est��n subutilizados? ��Se podr����an vender o alquilar? ��Liberar����a recursos valiosos?
**Recommended_Actions:** Identificar activos no estrat��gicos; evaluar venta, alquiler o leaseback; liberar capital para inversiones productivas; mejorar rotaci��n.
**Related_Patterns:** STR-098, STR-099, STR-100, STR-104, STR-110

### STR-105
**Pattern_Name:** Falta de Presupuesto de Capital Formal
**Category:** Asignaci��n de Recursos
**Description:** La empresa no tiene un proceso formal de presupuesto de capital (capex), realizando inversiones sin evaluaci��n, aprobaci��n ni seguimiento adecuados.
**Typical_Causes:** Informalidad; empresa peque��a; decisiones del due��o sin proceso; falta de disciplina financiera; urgencia.
**Observable_Symptoms:** Inversiones sin aprobaci��n formal; capex no presupuestado; decisiones unilaterales; falta de evaluaci��n; seguimiento inexistente.
**Early_Warning_Signals:** % de capex con proceso formal < 30%; % de inversiones sin aprobaci��n > 40%; sin presupuesto de capital anual.
**Business_Impact:** Malas decisiones de inversi��n; sobreinversi��n; falta de control; recursos malgastados; ausencia de disciplina financiera.
**Severity_Level:** High
**Metrics_To_Check:** % de capex con proceso formal; % de inversiones aprobadas; desviaci��n de presupuesto de capital; ROI de capex.
**Diagnostic_Questions:** ��Hay proceso formal de presupuesto de capital? ��Las inversiones se eval��an y aprueban? ��Hay seguimiento? ��Hay disciplina?
**Recommended_Actions:** Implementar proceso formal de capex; definir niveles de aprobaci��n; evaluar ROI; hacer seguimiento post-inversi��n.
**Related_Patterns:** STR-097, STR-099, STR-100, STR-103, STR-104

### STR-106
**Pattern_Name:** Asignaci��n de Recursos sin Evaluaci��n de Riesgos
**Category:** Asignaci��n de Recursos
**Description:** La empresa asigna recursos a proyectos e inversiones sin evaluar los riesgos asociados, exponi��ndose a p��rdidas significativas cuando los riesgos se materializan.
**Typical_Causes:** Falta de gesti��n de riesgos; optimismo; presi��n por invertir; desconocimiento; cultura de "a lo hecho, pecho".
**Observable_Symptoms:** Proyectos con riesgos no identificados; sorpresas negativas; p��rdidas no anticipadas; sobrecostos recurrentes; ausencia de planes de contingencia.
**Early_Warning_Signals:** % de proyectos con evaluaci��n de riesgos < 30%; % de proyectos con sobrecosto > 30%; sorpresas negativas frecuentes.
**Business_Impact:** P��rdidas no anticipadas; proyectos fracasados; recursos desperdiciados; falta de preparaci��n; resultados impredecibles.
**Severity_Level:** High
**Metrics_To_Check:** % de proyectos con evaluaci��n de riesgos; % de sobrecostos; n��mero de sorpresas negativas; efectividad de mitigaci��n.
**Diagnostic_Questions:** ��Se eval��an los riesgos antes de asignar recursos? ��Hay planes de contingencia? ��Hay sorpresas negativas frecuentes? ��Los sobrecostos son comunes?
**Recommended_Actions:** Incorporar evaluaci��n de riesgos en proceso de asignaci��n; identificar, valorar y mitigar; incluir contingencias; monitorear.
**Related_Patterns:** STR-097, STR-100, STR-103, STR-106, STR-128

### STR-107
**Pattern_Name:** Asignaci��n de Recursos Desconectada del Plan Estrat��gico
**Category:** Asignaci��n de Recursos
**Description:** El presupuesto anual y la asignaci��n de recursos se realizan de forma independiente al plan estrat��gico, generando una brecha entre lo que se dice y lo que se hace.
**Typical_Causes:** Silo entre planificaci��n y presupuesto; proceso presupuestario no vinculado; falta de cascada; cultura de "dos documentos".
**Observable_Symptoms:** Presupuesto no refleja prioridades estrat��gicas; proyectos estrat��gicos sin fondos; el plan estrat��gico y el presupuesto parecen de empresas distintas.
**Early_Warning_Signals:** % de iniciativas estrat��gicas con presupuesto asignado < 40%; % de presupuesto vinculado a plan < 30%; desconexi��n.
**Business_Impact:** Estrategia no ejecutable; recursos asignados a lo no estrat��gico; plan estrat��gico irrelevante; falta de credibilidad.
**Severity_Level:** Critical
**Metrics_To_Check:** % de iniciativas estrat��gicas presupuestadas; % de presupuesto vinculado a plan; ejecuci��n de plan estrat��gico.
**Diagnostic_Questions:** ��El presupuesto est�� vinculado al plan estrat��gico? ��Las iniciativas estrat��gicas tienen fondos? ��Hay coherencia entre ambos?
**Recommended_Actions:** Vincular proceso presupuestario al plan estrat��gico; presupuestar iniciativas estrat��gicas primero; cascada; revisar alineaci��n trimestralmente.
**Related_Patterns:** STR-097, STR-099, STR-105, STR-109, STR-121

### STR-108
**Pattern_Name:** Falta de Flexibilidad en Reasignaci��n de Recursos
**Category:** Asignaci��n de Recursos
**Description:** Una vez asignados, los recursos no se reasignan cuando cambian las prioridades o circunstancias, quedando atrapados en iniciativas que ya no son estrat��gicas.
**Typical_Causes:** Presupuesto r��gido; cultura de "no quitar recursos"; falta de revisiones peri��dicas; compromiso emocional con proyectos; pol��tica interna.
**Observable_Symptoms:** Proyectos obsoletos siguen recibiendo recursos; imposibilidad de redirigir fondos; rigidez; adaptaci��n lenta a cambios.
**Early_Warning_Signals:** % de recursos reasignados en el a��o < 10%; tiempo de reasignaci��n > 6 meses; % de proyectos obsoletos a��n financiados > 20%.
**Business_Impact:** Recursos atrapados en iniciativas obsoletas; imposibilidad de responder r��pidamente; ineficiencia; oportunidades perdidas.
**Severity_Level:** High
**Metrics_To_Check:** % de recursos reasignados; tiempo de reasignaci��n; % de proyectos obsoletos financiados; agilidad de asignaci��n.
**Diagnostic_Questions:** ��Los recursos se pueden reasignar flexiblemente? ��Hay revisiones peri��dicas? ��Proyectos obsoletos siguen recibiendo fondos? ��Hay rigidez?
**Recommended_Actions:** Revisar asignaci��n de recursos trimestralmente; cancelar proyectos obsoletos; crear presupuesto flexible; fomentar reasignaci��n din��mica.
**Related_Patterns:** STR-097, STR-098, STR-100, STR-107, STR-109


## Prioridades Estrat��gicas

### STR-109
**Pattern_Name:** Falta de Prioridades Estrat��gicas Claras
**Category:** Prioridades Estrat��gicas
**Description:** La empresa no tiene prioridades estrat��gicas claramente definidas y comunicadas, por lo que el equipo no sabe en qu�� enfocarse y los recursos se dispersan.
**Typical_Causes:** Estrategia ambigua; falta de decisi��n; querer abarcar mucho; no hacer trade-offs; liderazgo indeciso.
**Observable_Symptoms:** Equipo no sabe qu�� es prioritario; se hace de todo un poco; falta de foco; dispersi��n de recursos; avances lentos.
**Early_Warning_Signals:** % de empleados que pueden nombrar las 3 prioridades principales < 20%; % de proyectos alineados con prioridades < 30%; dispersi��n.
**Business_Impact:** Falta de foco; recursos diluidos; avance lento en todas las iniciativas; imposibilidad de destacar en algo; resultados mediocres.
**Severity_Level:** Critical
**Metrics_To_Check:** % de empleados que conocen prioridades; % de recursos alineados con prioridades; n��mero de prioridades (ideal 3-5).
**Diagnostic_Questions:** ��Hay prioridades estrat��gicas claras? ��El equipo las conoce? ��Se hacen trade-offs? ��Hay foco? ��Se dice no a lo no prioritario?
**Recommended_Actions:** Definir 3-5 prioridades estrat��gicas claras; comunicarlas insistentemente; alinear recursos; decir no a lo no prioritario; revisar trimestralmente.
**Related_Patterns:** STR-097, STR-107, STR-110, STR-114, STR-121

### STR-110
**Pattern_Name:** Todo es Prioritario (Nada lo Es)
**Category:** Prioridades Estrat��gicas
**Description:** La empresa declara todo como prioritario, diluyendo el concepto de prioridad y generando que nada reciba la atenci��n y recursos necesarios para avanzar significativamente.
**Typical_Causes:** Falta de decisi��n; no hacer trade-offs; liderazgo que no quiere excluir; cultura de "todo es importante"; evitar conflictos.
**Observable_Symptoms:** Larga lista de "prioridades"; equipos divididos entre m��ltiples frentes; avances lentos; frustraci��n; nada se termina.
**Early_Warning_Signals:** N��mero de prioridades declaradas > 10; % de empleados que no saben cu��l es la prioridad n��mero 1 > 50%; % de proyectos completados < 30%.
**Business_Impact:** Falta de foco real; recursos dispersos; imposibilidad de concentrar masa cr��tica; avances insuficientes; resultados mediocres.
**Severity_Level:** Critical
**Metrics_To_Check:** N��mero de prioridades; % de recursos concentrados en top 3; % de proyectos completados; velocidad de avance.
**Diagnostic_Questions:** ��Hay demasiadas prioridades? ��Se concentran recursos? ��Se avanza significativamente en algo? ��Se hacen trade-offs?
**Recommended_Actions:** Reducir prioridades a 3-5 m��ximo; concentrar recursos; decir no; proteger las prioridades verdaderas de la dispersi��n.
**Related_Patterns:** STR-102, STR-109, STR-114, STR-121, STR-126

### STR-111
**Pattern_Name:** Prioridades Cambiantes Constantemente
**Category:** Prioridades Estrat��gicas
**Description:** La empresa cambia sus prioridades con frecuencia, sin dar tiempo a que las iniciativas den resultados, generando inestabilidad, desgaste del equipo y baja ejecuci��n.
**Typical_Causes:** Liderazgo reactivo; falta de disciplina; cortoplacismo; presi��n externa; cambios de opini��n del due��o.
**Observable_Symptoms:** Lo que era prioritario ayer ya no lo es hoy; equipos frustrados; proyectos abandonados a medio camino; falta de constancia; escepticismo.
**Early_Warning_Signals:** Frecuencia de cambio de prioridades > 4 veces al a��o; % de proyectos abandonados antes de completar > 40%; desgaste del equipo.
**Business_Impact:** Proyectos no terminados; recursos desperdiciados; desgaste del equipo; desconfianza en la direcci��n; resultados no materializados.
**Severity_Level:** Critical
**Metrics_To_Check:** Frecuencia de cambios de prioridad; % de proyectos completados; % de proyectos abandonados; satisfacci��n del equipo.
**Diagnostic_Questions:** ��Las prioridades cambian constantemente? ��Se abandonan proyectos antes de ver resultados? ��Hay inestabilidad? ��Hay disciplina?
**Recommended_Actions:** Estabilizar prioridades; dar tiempo para que las iniciativas den resultados; proteger el proceso de cambios reactivos; disciplina.
**Related_Patterns:** STR-109, STR-110, STR-114, STR-121, STR-126

### STR-112
**Pattern_Name:** Prioridades No Comunicadas a la Organizaci��n
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas existen pero no se comunican efectivamente a toda la organizaci��n, por lo que los equipos no saben a qu�� darle prioridad en su d��a a d��a.
**Typical_Causes:** Estrategia en la cabeza del due��o; falta de cascada; comunicaci��n pobre; asumir que "todos saben"; desconexi��n.
**Observable_Symptoms:** Equipos trabajan en lo que creen importante; desalineaci��n; esfuerzos no coordinados; falta de direcci��n; decisiones inconsistentes.
**Early_Warning_Signals:** % de empleados que conocen las prioridades < 30%; % de decisiones alineadas con prioridades < 40%; descoordinaci��n.
**Business_Impact:** Desalineaci��n; esfuerzos dispersos; decisiones no alineadas; ejecuci��n inconsistente; estrategia no se materializa.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados que conocen prioridades; % de decisiones alineadas; consistencia de esfuerzos; efectividad de comunicaci��n.
**Diagnostic_Questions:** ��Las prioridades se comunican a toda la organizaci��n? ��Los equipos saben a qu�� darle prioridad? ��Hay cascada? ��Hay desalineaci��n?
**Recommended_Actions:** Comunicar prioridades en m��ltiples canales; cascada a todos los niveles; vincular con objetivos individuales; repetir constantemente.
**Related_Patterns:** STR-036, STR-109, STR-110, STR-121, STR-126

### STR-113
**Pattern_Name:** Prioridades sin Recursos Asignados
**Category:** Prioridades Estrat��gicas
**Description:** La empresa define prioridades estrat��gicas pero no les asigna los recursos necesarios (presupuesto, talento, tiempo), conden��ndolas al fracaso desde el inicio.
**Typical_Causes:** Falta de compromiso real; ilusi��n de priorizar sin costo; desconexi��n presupuesto-estrategia; falta de disciplina.
**Observable_Symptoms:** Prioridades declaradas no tienen presupuesto; proyectos estrat��gicos sin personal asignado; avance m��nimo; frustraci��n.
**Early_Warning_Signals:** % de prioridades con presupuesto asignado < 40%; % de prioridades con responsable asignado < 50%; avance de prioridades < 30% del plan.
**Business_Impact:** Prioridades no ejecutadas; p��rdida de credibilidad; frustraci��n del equipo; estrategia en papel; resultados no alcanzados.
**Severity_Level:** Critical
**Metrics_To_Check:** % de prioridades con recursos asignados; % de avance de prioridades; % de presupuesto estrat��gico ejecutado.
**Diagnostic_Questions:** ��Las prioridades tienen recursos asignados? ��Hay presupuesto y talento? ��Se est��n ejecutando? ��Hay avance real?
**Recommended_Actions:** Asignar recursos a cada prioridad antes de declararla; presupuestar; asignar responsables; monitorear avance; si no hay recursos, no priorizar.
**Related_Patterns:** STR-097, STR-099, STR-107, STR-109, STR-121

### STR-114
**Pattern_Name:** Falta de Trade-offs Estrat��gicos
**Category:** Prioridades Estrat��gicas
**Description:** La empresa evita hacer trade-offs estrat��gicos, intentando hacer todo y complacer a todos, diluyendo su estrategia y perdiendo la oportunidad de ser excelente en algo.
**Typical_Causes:** Miedo a excluir; querer complacer a todos; falta de decisi��n; no entender que estrategia es elegir qu�� no hacer; cultura de "s�� a todo".
**Observable_Symptoms:** La empresa intenta abarcar mucho; no destaca en nada; falta de diferenciaci��n; recursos diluidos; falta de foco.
**Early_Warning_Signals:** N��mero de segmentos servidos > capacidad; % de ingresos de actividades no focales > 30%; sin trade-offs declarados; falta de foco.
**Business_Impact:** Estrategia diluida; incapacidad de ser excelente en algo; recursos dispersos; falta de ventaja competitiva; resultados mediocres.
**Severity_Level:** Critical
**Metrics_To_Check:** N��mero de segmentos/actividades; % de ingresos focales; nivel de excelencia en actividad principal; claridad de trade-offs.
**Diagnostic_Questions:** ��Se hacen trade-offs estrat��gicos? ��Se elige qu�� no hacer? ��La empresa intenta abarcar demasiado? ��Hay foco? ��Se dice no?
**Recommended_Actions:** Definir trade-offs estrat��gicos claros; elegir qu�� no hacer; comunicar trade-offs; alinear toda la organizaci��n; proteger el foco.
**Related_Patterns:** STR-035, STR-109, STR-110, STR-116, STR-121

### STR-115
**Pattern_Name:** Prioridades No Revisadas Peri��dicamente
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas se definen una vez al a��o y no se revisan hasta el a��o siguiente, perdiendo la capacidad de adaptarse a cambios del entorno.
**Typical_Causes:** Presupuesto anual r��gido; falta de agilidad; planificaci��n tradicional; no revisiones peri��dicas; burocracia.
**Observable_Symptoms:** Prioridades desactualizadas; entorno cambi�� y las prioridades no; falta de adaptaci��n; irrelevancia; oportunidades perdidas.
**Early_Warning_Signals:** Frecuencia de revisi��n de prioridades < 4 veces al a��o; % de prioridades desactualizadas > 30%; desalineaci��n con entorno.
**Business_Impact:** Prioridades irrelevantes; falta de adaptaci��n; oportunidades perdidas; recursos asignados a lo que ya no importa.
**Severity_Level:** High
**Metrics_To_Check:** Frecuencia de revisi��n de prioridades; % de prioridades actualizadas; tiempo de respuesta a cambios; agilidad.
**Diagnostic_Questions:** ��Las prioridades se revisan peri��dicamente? ��Est��n actualizadas? ��Reflejan el entorno actual? ��Hay agilidad para cambiar?
**Recommended_Actions:** Revisar prioridades trimestralmente; ajustar seg��n cambios del entorno; mantener proceso din��mico; equilibrar consistencia y adaptaci��n.
**Related_Patterns:** STR-109, STR-111, STR-114, STR-121, STR-128

### STR-116
**Pattern_Name:** Prioridades No Traducidas a Objetivos Individuales
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas no se traducen en objetivos individuales, por lo que los empleados no ven c��mo su trabajo contribuye a las prioridades de la empresa.
**Typical_Causes:** Falta de cascada; sistema de objetivos no vinculado; desconexi��n HR-estrategia; falta de alineaci��n.
**Observable_Symptoms:** Empleados no saben c��mo su trabajo contribuye a las prioridades; objetivos individuales no alineados; falta de sentido de contribuci��n.
**Early_Warning_Signals:** % de empleados con objetivos vinculados a prioridades < 30%; % de empleados que ven su contribuci��n < 40%; desalineaci��n.
**Business_Impact:** Falta de alineaci��n; empleados no enfocados en lo que importa; esfuerzo no dirigido; menor ejecuci��n; desconexi��n.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados con objetivos vinculados a prioridades; % que ven su contribuci��n; alineaci��n de esfuerzos.
**Diagnostic_Questions:** ��Las prioridades se traducen a objetivos individuales? ��Los empleados ven su contribuci��n? ��Hay alineaci��n? ��El sistema de objetivos est�� vinculado?
**Recommended_Actions:** Cascada de objetivos (OKRs o similar); vincular objetivos individuales a prioridades; comunicar contribuci��n; revisar alineaci��n.
**Related_Patterns:** STR-109, STR-112, STR-121, STR-127, STR-128

### STR-117
**Pattern_Name:** Prioridades Sin Due��o o Responsable
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas no tienen un responsable asignado que rinda cuentas por su avance, generando falta de accountability y ejecuci��n inconsistente.
**Typical_Causes:** Falta de asignaci��n de responsabilidad; cultura de responsabilidad compartida (que es responsabilidad de nadie); evitar accountability individual.
**Observable_Symptoms:** Nadie es responsable del avance de las prioridades; todos asumen que "alguien" lo har��; falta de seguimiento; avance lento.
**Early_Warning_Signals:** % de prioridades con responsable asignado < 30%; % de prioridades con avance reportado < 40%; falta de ownership.
**Business_Impact:** Falta de accountability; ejecuci��n inconsistente; nadie impulsa; prioridades no avanzan; estrategia no se ejecuta.
**Severity_Level:** High
**Metrics_To_Check:** % de prioridades con responsable; % de avance reportado; cumplimiento de compromisos; ownership.
**Diagnostic_Questions:** ��Cada prioridad tiene un responsable? ��Hay accountability? ��Alguien impulsa el avance? ��Se reporta el progreso?
**Recommended_Actions:** Asignar un responsable por cada prioridad estrat��gica; dar autoridad y recursos; medir avance; rendici��n de cuentas peri��dica.
**Related_Patterns:** STR-109, STR-113, STR-121, STR-126, STR-127

### STR-118
**Pattern_Name:** Prioridades sin M��tricas de ��xito
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas no tienen m��tricas claras de ��xito, por lo que no se puede determinar objetivamente si se est��n logrando o no.
**Typical_Causes:** Falta de definici��n de KPIs; cultura de "sentir" en lugar de medir; estrategia vaga; falta de rigor.
**Observable_Symptoms:** No se puede decir si una prioridad se logr�� o no; evaluaci��n subjetiva; discusiones sobre avance; falta de claridad.
**Early_Warning_Signals:** % de prioridades con KPIs definidos < 30%; % de prioridades con meta cuantitativa < 20%; evaluaci��n subjetiva.
**Business_Impact:** Imposibilidad de medir avance; evaluaciones subjetivas; falta de accountability; direcci��n sin datos; resultados ambiguos.
**Severity_Level:** High
**Metrics_To_Check:** % de prioridades con KPIs; % con metas cuantitativas; % de avance medible; objetividad de evaluaci��n.
**Diagnostic_Questions:** ��Cada prioridad tiene m��tricas de ��xito? ��Se puede medir objetivamente el avance? ��Hay metas cuantitativas? ��C��mo se sabe si se logr��?
**Recommended_Actions:** Definir KPIs y metas para cada prioridad; medibles, espec��ficos, con plazo; trackear y reportar; ajustar si es necesario.
**Related_Patterns:** STR-109, STR-115, STR-117, STR-121, STR-128

### STR-119
**Pattern_Name:** Prioridades no Integradas con la Cultura
**Category:** Prioridades Estrat��gicas
**Description:** Las prioridades estrat��gicas no se integran con la cultura organizacional, generando conflicto entre lo que la empresa dice priorizar y lo que la cultura realmente valora y recompensa.
**Typical_Causes:** Cultura no alineada con estrategia; falta de coherencia; valores no actualizados; sistema de incentivos desconectado.
**Observable_Symptoms:** La cultura premia comportamientos contrarios a las prioridades; conflicto entre lo que se dice y lo que se hace; incoherencia.
**Early_Warning_Signals:** % de comportamientos recompensados que apoyan prioridades < 30%; % de valores alineados con prioridades < 40%; incoherencia percibida.
**Business_Impact:** Ejecuci��n inconsistente; conflicto cultura-estrategia; comportamientos no alineados; dificultad para implementar prioridades.
**Severity_Level:** High
**Metrics_To_Check:** % de comportamientos recompensados alineados; % de valores alineados; coherencia percibida; consistencia.
**Diagnostic_Questions:** ��La cultura apoya las prioridades? ��Los incentivos est��n alineados? ��Hay coherencia entre lo que se dice y se premia? ��Hay conflicto?
**Recommended_Actions:** Alinear cultura con prioridades; ajustar valores, incentivos y comportamientos; comunicar coherencia; liderar con el ejemplo.
**Related_Patterns:** STR-078, STR-079, STR-109, STR-116, STR-121

### STR-120
**Pattern_Name:** Prioridades Externas vs Internas Desbalanceadas
**Category:** Prioridades Estrat��gicas
**Description:** La empresa se enfoca excesivamente en prioridades externas (ventas, clientes, crecimiento) descuidando las internas (cultura, procesos, sistemas, talento), generando desequilibrio.
**Typical_Causes:** Sesgo comercial; cortoplacismo; presi��n de resultados; falta de visi��n de largo plazo; no entender interdependencia.
**Observable_Symptoms:** La empresa crece pero los procesos internos colapsan; cultura se deteriora; sistemas obsoletos; talento insuficiente; desbalance.
**Early_Warning_Signals:** % de atenci��n/recursos a prioridades internas < 20%; satisfacci��n de empleados baja; procesos colapsando; crecimiento insostenible.
**Business_Impact:** Crecimiento insostenible; colapso operativo; p��rdida de talento; problemas de calidad; crisis interna mientras externa parece bien.
**Severity_Level:** High
**Metrics_To_Check:** % de recursos a internas vs externas; satisfacci��n empleados; eficiencia operativa; capacidad de soportar crecimiento.
**Diagnostic_Questions:** ��Hay equilibrio entre prioridades internas y externas? ��Se descuida la operaci��n interna por crecer? ��El crecimiento es sostenible?
**Recommended_Actions:** Balancear prioridades internas y externas; invertir en procesos, sistemas y talento; asegurar que la casa est�� en orden.
**Related_Patterns:** STR-078, STR-098, STR-109, STR-119, STR-121


## Ejecuci��n Estrat��gica

### STR-121
**Pattern_Name:** Brecha entre Estrategia y Ejecuci��n
**Category:** Ejecuci��n Estrat��gica
**Description:** Existe una brecha significativa entre lo que la estrategia dice y lo que realmente se ejecuta, siendo una de las principales causas de fracaso estrat��gico en PyMEs.
**Typical_Causes:** Falta de cascada; comunicaci��n deficiente; prioridades no operacionalizadas; falta de accountability; recursos no asignados.
**Observable_Symptoms:** La estrategia no se traduce en acciones concretas; el d��a a d��a no refleja la estrategia; resultados no alineados con el plan.
**Early_Warning_Signals:** % de iniciativas estrat��gicas en ejecuci��n < 40%; % de empleados que vinculan su trabajo a estrategia < 30%; desalineaci��n.
**Business_Impact:** Estrategia no implementada; resultados no alcanzados; p��rdida de credibilidad; recursos desperdiciados; fracaso estrat��gico.
**Severity_Level:** Critical
**Metrics_To_Check:** % de iniciativas estrat��gicas ejecut��ndose; % de avance de plan estrat��gico; % de empleados alineados.
**Diagnostic_Questions:** ��Hay brecha entre estrategia y ejecuci��n? ��La estrategia se traduce en acciones? ��El d��a a d��a refleja la estrategia? ��Se ejecuta el plan?
**Recommended_Actions:** Cerrar brecha con cascada de objetivos; asignar recursos y responsables; reuniones de seguimiento peri��dicas; accountability.
**Related_Patterns:** STR-109, STR-113, STR-117, STR-126, STR-127

### STR-122
**Pattern_Name:** Falta de Ritmo de Revisi��n Estrat��gica
**Category:** Ejecuci��n Estrat��gica
**Description:** La empresa no tiene un ritmo regular de revisi��n de la ejecuci��n estrat��gica (reuniones peri��dicas de seguimiento), dejando que la estrategia se desv��e sin correcci��n.
**Typical_Causes:** Falta de disciplina; cultura de "reuni��n solo si hay problema"; no establecer calendario; priorizar operativo sobre estrat��gico.
**Observable_Symptoms:** No hay reuniones de revisi��n de estrategia; se revisa solo cuando hay problemas; desviaciones no corregidas; seguimiento inexistente.
**Early_Warning_Signals:** Frecuencia de revisi��n de estrategia < 1 vez al mes; % de desviaciones corregidas < 30%; sin agenda de revisi��n; improvisaci��n.
**Business_Impact:** Desviaciones no corregidas; estrategia se pierde; ejecuci��n sin control; correcciones tard��as; resultados no alcanzados.
**Severity_Level:** Critical
**Metrics_To_Check:** Frecuencia de revisiones; % de desviaciones corregidas; tiempo de correcci��n; efectividad de seguimiento.
**Diagnostic_Questions:** ��Hay ritmo de revisi��n estrat��gica? ��Se revisa regularmente? ��Las desviaciones se corrigen a tiempo? ��Hay disciplina de seguimiento?
**Recommended_Actions:** Establecer ritmo de revisi��n (semanal t��ctico, mensual estrat��gico, trimestral de plan); agenda fija; reportes; accountability.
**Related_Patterns:** STR-115, STR-121, STR-126, STR-127, STR-128

### STR-123
**Pattern_Name:** Ejecuci��n sin Responsables Claros
**Category:** Ejecuci��n Estrat��gica
**Description:** Las iniciativas estrat��gicas no tienen responsables claramente asignados, diluyendo la responsabilidad y generando que nadie impulse activamente su avance.
**Typical_Causes:** Falta de asignaci��n; cultura de responsabilidad grupal; evitar accountability individual; falta de disciplina; ambig��edad.
**Observable_Symptoms:** Iniciativas sin due��o; nadie presiona por avance; se asume que "alguien lo har��"; avance lento; seguimiento difuso.
**Early_Warning_Signals:** % de iniciativas con responsable asignado < 40%; % de iniciativas con avance reportado < 30%; ambig��edad.
**Business_Impact:** Falta de impulso; ejecuci��n lenta; nadie rinde cuentas; iniciativas estancadas; estrategia no se materializa.
**Severity_Level:** Critical
**Metrics_To_Check:** % de iniciativas con responsable; % con avance reportado; velocidad de ejecuci��n; cumplimiento de plazos.
**Diagnostic_Questions:** ��Cada iniciativa tiene un responsable claro? ��Hay ownership? ��Alguien impulsa activamente? ��Hay rendici��n de cuentas?
**Recommended_Actions:** Asignar un responsable por cada iniciativa; dar autoridad; medir avance; rendici��n de cuentas; reemplazar si no funciona.
**Related_Patterns:** STR-117, STR-121, STR-122, STR-126, STR-127

### STR-124
**Pattern_Name:** Falta de Plan de Acci��n Detallado
**Category:** Ejecuci��n Estrat��gica
**Description:** La estrategia no se desglosa en planes de acci��n detallados con pasos, plazos y responsables, quedando en un nivel de generalidad que no permite la ejecuci��n.
**Typical_Causes:** Estrategia vaga; falta de planificaci��n; pereza; cultura de "ya veremos"; no metodolog��a de ejecuci��n.
**Observable_Symptoms:** Plan estrat��gico sin acciones concretas; no hay pasos definidos; plazos inexistentes; imposibilidad de ejecutar; ambig��edad.
**Early_Warning_Signals:** % de iniciativas con plan de acci��n detallado < 30%; % con plazos definidos < 40%; % con responsables < 50%; vaguedad.
**Business_Impact:** Imposibilidad de ejecutar; estrategia no operacionalizada; confusi��n; falta de avance; fracaso de implementaci��n.
**Severity_Level:** Critical
**Metrics_To_Check:** % de iniciativas con plan de acci��n; % con plazos; % con responsables; nivel de detalle de planes.
**Diagnostic_Questions:** ��Hay planes de acci��n detallados? ��Se sabe qui��n hace qu�� y cu��ndo? ��Los pasos est��n definidos? ��Hay plazos?
**Recommended_Actions:** Desglosar estrategia en planes de acci��n detallados; definir pasos, plazos y responsables; usar metodolog��as (OKR, EOS, Scrum).
**Related_Patterns:** STR-121, STR-122, STR-123, STR-126, STR-127

### STR-125
**Pattern_Name:** Falta de Accountability en Ejecuci��n
**Category:** Ejecuci��n Estrat��gica
**Description:** No existe una cultura de accountability donde las personas rindan cuentas por el cumplimiento de sus compromisos estrat��gicos, generando incumplimiento sistem��tico.
**Typical_Causes:** Cultura de "no pasa nada"; falta de consecuencias; liderazgo permisivo; evitar conflictos; no sistema de seguimiento.
**Observable_Symptoms:** Compromisos no se cumplen; no hay consecuencias; excusas frecuentes; falta de presi��n; baja ejecuci��n; normalizaci��n del incumplimiento.
**Early_Warning_Signals:** % de compromisos cumplidos a tiempo < 50%; % de personas con incumplimiento recurrente > 30%; falta de consecuencias.
**Business_Impact:** Incumplimiento sistem��tico; estrategia no ejecutada; p��rdida de credibilidad; baja exigencia; resultados inferiores.
**Severity_Level:** Critical
**Metrics_To_Check:** % de compromisos cumplidos a tiempo; % de personas con cumplimiento consistente; consecuencias aplicadas; nivel de exigencia.
**Diagnostic_Questions:** ��Hay cultura de accountability? ��Se cumplen los compromisos? ��Hay consecuencias por incumplimiento? ��Se normaliza el no cumplir?
**Recommended_Actions:** Establecer cultura de accountability; consecuencias claras; seguimiento riguroso; liderazgo ejemplar; reconocer cumplimiento.
**Related_Patterns:** STR-117, STR-121, STR-122, STR-123, STR-127

### STR-126
**Pattern_Name:** Falta de Reuniones de Ejecuci��n Efectivas
**Category:** Ejecuci��n Estrat��gica
**Description:** Las reuniones de seguimiento de la ejecuci��n son inefectivas: sin agenda, sin datos, sin decisi��n, sin accountability, perdiendo tiempo sin generar avance.
**Typical_Causes:** Falta de metodolog��a; cultura de reuni��n improductiva; liderazgo que no estructura; no formaci��n; ausencia de sistema.
**Observable_Symptoms:** Reuniones largas sin conclusi��n; sin agenda; mismos temas cada semana; falta de decisi��n; sin seguimiento de acuerdos.
**Early_Warning_Signals:** Duraci��n de reuniones sin avance; % de reuniones con agenda < 40%; % con decisiones tomadas < 30%; % con seguimiento de acuerdos < 20%.
**Business_Impact:** Tiempo perdido; falta de avance; frustraci��n; decisiones no tomadas; ejecuci��n sin impulso; resultados no alcanzados.
**Severity_Level:** High
**Metrics_To_Check:** Efectividad de reuniones; % con agenda; % con decisiones; % con seguimiento de acuerdos; satisfacci��n del equipo.
**Diagnostic_Questions:** ��Las reuniones de seguimiento son efectivas? ��Hay agenda? ��Se toman decisiones? ��Se hace seguimiento de acuerdos? ��Generan avance?
**Recommended_Actions:** Metodolog��a de reuni��n efectiva (EOS level 10, Scrum); agenda previa; datos; decisiones; seguimiento; timeboxing.
**Related_Patterns:** STR-122, STR-123, STR-125, STR-127, STR-128

### STR-127
**Pattern_Name:** Falta de Sistema de Seguimiento de Metas
**Category:** Ejecuci��n Estrat��gica
**Description:** La empresa no cuenta con un sistema formal de seguimiento de metas (OKRs, Balanced Scorecard, dashboard), por lo que el progreso estrat��gico no es visible ni medible.
**Typical_Causes:** Falta de herramientas; informalidad; desconocimiento; cultura de "sentir" vs medir; no priorizaci��n.
**Observable_Symptoms:** No hay visibilidad del avance estrat��gico; se depende de la memoria; falta de datos; imposibilidad de corregir a tiempo; discusiones subjetivas.
**Early_Warning_Signals:** Sin sistema de seguimiento; % de metas con tracking < 20%; % de decisiones basadas en datos < 30%; informalidad.
**Business_Impact:** Falta de visibilidad; correcciones tard��as; evaluaci��n subjetiva; imposibilidad de gestionar; resultados no alcanzados.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de sistema de seguimiento; % de metas con tracking; frecuencia de actualizaci��n; % de decisiones basadas en datos.
**Diagnostic_Questions:** ��Hay sistema de seguimiento de metas? ��El avance estrat��gico es visible? ��Se puede medir el progreso? ��Hay datos para decidir?
**Recommended_Actions:** Implementar sistema de seguimiento (OKRs, Balanced Scorecard, dashboard); definir KPIs; actualizar peri��dicamente; visible para todos.
**Related_Patterns:** STR-118, STR-121, STR-122, STR-126, STR-128

### STR-128
**Pattern_Name:** Ejecuci��n sin Aprendizaje y Mejora Continua
**Category:** Ejecuci��n Estrat��gica
**Description:** La empresa ejecuta su estrategia pero no realiza ciclos de aprendizaje y mejora, repitiendo errores y perdiendo la oportunidad de refinar continuamente la ejecuci��n.
**Typical_Causes:** Falta de cultura de aprendizaje; no retrospectivas; no an��lisis post-mortem; apuro por seguir adelante; arrogancia.
**Observable_Symptoms:** Errores se repiten; no se documentan lecciones; mismos problemas una y otra vez; falta de mejora en ejecuci��n.
**Early_Warning_Signals:** % de errores recurrentes > 40%; sin retrospectivas; % de lecciones aplicadas < 20%; falta de mejora en KPIs de ejecuci��n.
**Business_Impact:** Errores repetidos; ineficiencia; ejecuci��n no mejora; aprendizaje desperdiciado; resultados sistem��ticamente sub��ptimos.
**Severity_Level:** High
**Metrics_To_Check:** % de errores recurrentes; frecuencia de retrospectivas; % de lecciones aplicadas; mejora en KPIs de ejecuci��n.
**Diagnostic_Questions:** ��Se aprende de la ejecuci��n? ��Hay retrospectivas? ��Los errores se repiten? ��Se documentan y aplican lecciones? ��Hay mejora continua?
**Recommended_Actions:** Implementar ciclos de aprendizaje (retrospectivas, post-mortems, after action reviews); documentar lecciones; aplicar mejoras; medir progreso.
**Related_Patterns:** STR-096, STR-115, STR-121, STR-122, STR-127

### STR-129
**Pattern_Name:** Ejecuci��n Sin Alineaci��n de Incentivos
**Category:** Ejecuci��n Estrat��gica
**Description:** Los incentivos y compensaciones no est��n alineados con la ejecuci��n de la estrategia, premiando comportamientos contrarios a los objetivos estrat��gicos.
**Typical_Causes:** Sistema de compensaci��n desactualizado; desconexi��n RH-estrategia; incentivos solo financieros; no considerar comportamientos estrat��gicos.
**Observable_Symptoms:** Los incentivos premian lo contrario a la estrategia; empleados act��an en funci��n de lo que se les paga, no de lo que la estrategia requiere.
**Early_Warning_Signals:** % de incentivos alineados con estrategia < 30%; % de comportamientos estrat��gicos recompensados < 20%; desalineaci��n.
**Business_Impact:** Comportamientos contrarios a la estrategia; ejecuci��n inconsistente; dificultad para implementar cambios; resultados no alineados.
**Severity_Level:** Critical
**Metrics_To_Check:** % de incentivos alineados con estrategia; % de comportamientos estrat��gicos recompensados; percepci��n de alineaci��n.
**Diagnostic_Questions:** ��Los incentivos est��n alineados con la estrategia? ��Se premia lo que la estrategia necesita? ��Hay incentivos que contradicen la estrategia?
**Recommended_Actions:** Alinear sistema de incentivos con objetivos estrat��gicos; revisar bonos, comisiones y reconocimientos; medir comportamientos estrat��gicos.
**Related_Patterns:** STR-116, STR-119, STR-121, STR-125, STR-127

### STR-130
**Pattern_Name:** Exceso de An��lisis, Poca Acci��n (Par��lisis por An��lisis)
**Category:** Ejecuci��n Estrat��gica
**Description:** La empresa dedica demasiado tiempo al an��lisis, planificaci��n y reuni��n, sin avanzar en la ejecuci��n concreta, generando un desbalance entre pensar y hacer.
**Typical_Causes:** Perfeccionismo; miedo a equivocarse; cultura de "analizar hasta el cansancio"; falta de sesgo a la acci��n; liderazgo indeciso.
**Observable_Symptoms:** Muchas reuniones, pocas acciones; an��lisis interminables; proyectos que no arrancan; "an��lisis-par��lisis"; frustraci��n.
**Early_Warning_Signals:** Ratio tiempo an��lisis/ejecuci��n > 3:1; % de proyectos en fase de an��lisis > 50%; % de decisiones no ejecutadas > 30%.
**Business_Impact:** Lentitud; oportunidades perdidas; baja ejecuci��n; frustraci��n; resultados no materializados; desventaja competitiva por velocidad.
**Severity_Level:** High
**Metrics_To_Check:** Ratio an��lisis/ejecuci��n; % de proyectos en an��lisis; % de decisiones ejecutadas; velocidad de ejecuci��n.
**Diagnostic_Questions:** ��Hay exceso de an��lisis? ��Se ejecuta lo suficiente? ��Hay sesgo a la acci��n? ��Se toman decisiones y se act��a? ��Hay par��lisis por an��lisis?
**Recommended_Actions:** Balancear an��lisis y acci��n; sesgo a la acci��n; plazos para decidir; experimentar; aceptar "suficientemente bueno" para avanzar.
**Related_Patterns:** STR-121, STR-122, STR-124, STR-126, STR-132

### STR-131
**Pattern_Name:** Ejecuci��n Dependiente del Due��o
**Category:** Ejecuci��n Estrat��gica
**Description:** La ejecuci��n de la estrategia depende del due��o, que debe estar involucrado en cada decisi��n y acci��n, creando un cuello de botella que ralentiza todo el proceso.
**Typical_Causes:** Falta de delegaci��n; centralismo; equipo sin autonom��a; due��o no conf��a; cultura de "preguntar al jefe".
**Observable_Symptoms:** Due��o es cuello de botella; decisiones se atascan; equipo no decide; dependencia total; ejecuci��n lenta; due��o agotado.
**Early_Warning_Signals:** % de decisiones que requieren al due��o > 70%; tiempo de decisi��n > 3 d��as; % de iniciativas que avanzan sin due��o < 20%.
**Business_Impact:** Lentitud; cuello de botella; dependencia; imposibilidad de escalar; due��o agotado; equipo no empoderado.
**Severity_Level:** Critical
**Metrics_To_Check:** % de decisiones sin due��o; tiempo de decisi��n; % de iniciativas aut��nomas; satisfacci��n del equipo con autonom��a.
**Diagnostic_Questions:** ��La ejecuci��n depende del due��o? ��Es cuello de botella? ��El equipo tiene autonom��a? ��Se delega efectivamente? ��Se puede escalar?
**Recommended_Actions:** Delegar ejecuci��n; empoderar equipo; dar autoridad para decidir; due��o enfocarse en estrat��gico; sistemas y procesos.
**Related_Patterns:** STR-078, STR-117, STR-121, STR-123, STR-125

### STR-132
**Pattern_Name:** Falta de Revisi��n Post-Ejecuci��n (After Action Review)
**Category:** Ejecuci��n Estrat��gica
**Description:** La empresa no realiza after action reviews o retrospectivas despu��s de completar iniciativas estrat��gicas, perdiendo la oportunidad de capturar aprendizaje y mejorar.
**Typical_Causes:** Falta de cultura de aprendizaje; apuro por siguiente iniciativa; no metodolog��a; arrogancia; desconocimiento.
**Observable_Symptoms:** Mismos errores en cada proyecto; no se documenta aprendizaje; equipo no reflexiona; mejora no sistem��tica; conocimiento no retenido.
**Early_Warning_Signals:** % de proyectos con after action review < 20%; % de errores recurrentes > 40%; % de lecciones documentadas < 10%.
**Business_Impact:** Errores repetidos; aprendizaje perdido; ejecuci��n no mejora; conocimiento no retenido; ineficiencia sistem��tica.
**Severity_Level:** High
**Metrics_To_Check:** % de proyectos con after action review; % de errores recurrentes; % de lecciones aplicadas; mejora en ejecuci��n.
**Diagnostic_Questions:** ��Se hacen after action reviews? ��Se aprende de cada iniciativa? ��Los errores se repiten? ��Se documentan y aplican lecciones?
**Recommended_Actions:** Implementar after action reviews en cada iniciativa importante; documentar lecciones; compartir; aplicar mejoras; cerrar ciclo.
**Related_Patterns:** STR-096, STR-128, STR-129, STR-130, STR-131
