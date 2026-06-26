# Risk_Patterns.md

**File:** Risk_Patterns.md
**Description:** Patrones de riesgo empresarial para PyMEs — diagnóstico de riesgos financieros, operativos, legales, tributarios, tecnológicos, reputacionales, estratégicos, comerciales, de proveedores y de talento humano.
**Total Patterns:** 128 (RSK-001 a RSK-128)
**Categories:** 10
**Version:** 1.0

---

## Summary Table

| Category | Pattern IDs | Count | Description |
|---|---|---|---|
| Riesgo Financiero | RSK-001 a RSK-013 | 13 | Riesgos relacionados con liquidez, solvencia, rentabilidad y estructura financiera |
| Riesgo Operativo | RSK-014 a RSK-026 | 13 | Riesgos en procesos, sistemas, infraestructura y operaciones del día a día |
| Riesgo Legal | RSK-027 a RSK-038 | 12 | Riesgos por incumplimiento normativo, contratos y litigios |
| Riesgo Tributario | RSK-039 a RSK-049 | 11 | Riesgos derivados de obligaciones fiscales y planificación tributaria |
| Riesgo Tecnológico | RSK-050 a RSK-062 | 13 | Riesgos de TI, ciberseguridad, infraestructura tecnológica y datos |
| Riesgo Reputacional | RSK-063 a RSK-074 | 12 | Riesgos que afectan la percepción de la marca y la confianza de los stakeholders |
| Riesgo Estratégico | RSK-075 a RSK-092 | 18 | Riesgos en la dirección estratégica, modelo de negocio y toma de decisiones |
| Riesgo Comercial | RSK-093 a RSK-105 | 13 | Riesgos en ventas, mercado, demanda y relación con clientes |
| Riesgo Proveedores | RSK-106 a RSK-117 | 12 | Riesgos en la cadena de suministro y dependencia de proveedores |
| Riesgo Talento | RSK-118 a RSK-128 | 11 | Riesgos en gestión de personas, retención, clima laboral y sucesión |

---

# Patrones de Riesgo

## Riesgo Financiero

### RSK-001
**Pattern_Name:** Liquidez Insuficiente
**Category:** Riesgo Financiero
**Description:** La empresa no dispone de efectivo suficiente para cubrir sus obligaciones de corto plazo, arriesgando su continuidad operativa y solvencia.
**Typical_Causes:** Ventas estacionales no anticipadas; crecimiento acelerado sin capital de trabajo; descalce de plazos entre activos y pasivos; exceso de inventario; clientes que pagan tarde.
**Observable_Symptoms:** Dificultad para pagar nómina; proveedores exigen pago anticipado; cheques devueltos; uso recurrente de sobregiros; retraso en pago de impuestos.
**Early_Warning_Signals:** Razón circulante < 1.2; prueba ácida < 0.8; días de caja < 15; aumento de cuentas por pagar vencidas; disminución de línea de crédito disponible.
**Business_Impact:** Incumplimiento de obligaciones; pérdida de descuentos por pronto pago; deterioro de relación con proveedores; riesgo de quiebra técnica; costos financieros elevados.
**Severity_Level:** Critical
**Metrics_To_Check:** Razón circulante; prueba ácida; días de caja; capital de trabajo neto; ciclo de conversión de efectivo.
**Diagnostic_Questions:** ¿Cuántos días de caja tiene la empresa? ¿Puede pagar sus obligaciones de los próximos 30 días? ¿Usa sobregiros recurrentemente? ¿Los clientes pagan a tiempo?
**Recommended_Actions:** Mejorar cobranzas; negociar plazos con proveedores; reducir inventario; establecer línea de crédito comprometida; realizar proyección de caja a 13 semanas; vender activos no estratégicos.
**Related_Patterns:** RSK-002, RSK-003, RSK-006, RSK-008, RSK-010

### RSK-002
**Pattern_Name:** Endeudamiento Excesivo
**Category:** Riesgo Financiero
**Description:** La empresa tiene un nivel de deuda que compromete su capacidad de generar flujo para cubrir el servicio de la misma, aumentando el riesgo de insolvencia.
**Typical_Causes:** Crecimiento financiado con deuda; malas cosechas de utilidades; exceso de confianza en apalancamiento; falta de planificación financiera; reinversión insuficiente de utilidades.
**Observable_Symptoms:** La mayoría de las utilidades se destinan al pago de intereses; dificultad para obtener nuevo financiamiento; los bancos piden más garantías; la deuda crece más que el EBITDA.
**Early_Warning_Signals:** Relación deuda/patrimonio > 2.0; cobertura de intereses < 2.0; EBITDA insuficiente para servicio de deuda; deuda neta/EBITDA > 4.0; renovaciones constantes de deuda de corto plazo.
**Business_Impact:** Alto gasto financiero que erosiona rentabilidad; menor capacidad de inversión; riesgo de default; pérdida de control en decisiones por covenants; quiebra técnica.
**Severity_Level:** Critical
**Metrics_To_Check:** Relación deuda/patrimonio; cobertura de intereses; deuda neta/EBITDA; apalancamiento financiero; perfil de vencimientos.
**Diagnostic_Questions:** ¿Cuánto representa la deuda respecto al patrimonio? ¿Las utilidades cubren los intereses? ¿Puede la empresa pagar la deuda en los próximos 12 meses? ¿Los covenants están cómodos?
**Recommended_Actions:** Reducir apalancamiento; renegociar plazos y tasas; aumentar patrimonio con aportes de socios; generar flujo para pagar deuda; evitar nuevo endeudamiento no productivo; considerar venta de activos.
**Related_Patterns:** RSK-001, RSK-003, RSK-006, RSK-008, RSK-010

### RSK-003
**Pattern_Name:** Concentración de Ingresos en Pocos Clientes
**Category:** Riesgo Financiero
**Description:** Un alto porcentaje de los ingresos depende de un número reducido de clientes, exponiendo a la empresa a un riesgo material si alguno se pierde.
**Typical_Causes:** Estrategia comercial orientada a cuentas grandes; incapacidad para diversificar cartera; producto/servicio muy específico para pocos clientes; barreras de entrada a otros segmentos.
**Observable_Symptoms:** Un cliente representa > 30% de las ventas; los 3 principales clientes suman > 60%; el equipo comercial se enfoca solo en cuentas grandes; cada cliente perdido impacta significativamente.
**Early_Warning_Signals:** % de ingresos del mayor cliente > 25%; % de ingresos de top 3 > 50%; cartera de clientes no crece; pérdida de un cliente genera crisis; nuevos clientes no compensan los perdidos.
**Business_Impact:** Alta volatilidad en ingresos; poder de negociación del cliente sobre precios; riesgo de quiebra si se pierde el cliente principal; dificultad para planificar inversiones.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos del mayor cliente; % de ingresos del top 3; índice de concentración (HHI); rotación de clientes; antigüedad de la relación con cada cliente.
**Diagnostic_Questions:** ¿Qué % de ingresos representa el mayor cliente? ¿Qué pasaría si se pierde? ¿Hay dependencia de algún sector? ¿La cartera está diversificada? ¿Hay plan para diversificar?
**Recommended_Actions:** Desarrollar programa de diversificación de clientes; establecer límite máximo por cliente; crear oferta para segmentos adyacentes; fortalecer relación con clientes medianos; adquirir cartera de clientes.
**Related_Patterns:** RSK-004, RSK-009, RSK-093, RSK-094, RSK-098

### RSK-004
**Pattern_Name:** Deterioro de Rentabilidad
**Category:** Riesgo Financiero
**Description:** La rentabilidad de la empresa se reduce de manera sostenida por aumento de costos, presión en precios o mix de ventas desfavorable, erosionando el margen.
**Typical_Causes:** Competencia agresiva en precios; aumento de costos de insumos no trasladable a precios; mix de ventas hacia productos de menor margen; ineficiencias operativas; gastos fijos crecientes.
**Observable_Symptoms:** Márgenes decrecientes trimestre a trimestre; utilidad neta se reduce aunque las ventas crecen; descuentos excesivos para mantener volumen; dificultad para cubrir gastos fijos.
**Early_Warning_Signals:** Margen bruto en descenso por 3 trimestres consecutivos; margen neto < 3%; EBITDA margin decreciente; gastos operativos crecen más que ventas; punto de equilibrio sube.
**Business_Impact:** Menor generación de caja; incapacidad para invertir; desmotivación de socios; dificultad para pagar deuda; posible descapitalización; pérdida de valor de la empresa.
**Severity_Level:** High
**Metrics_To_Check:** Margen bruto; margen EBITDA; margen neto; tendencia de márgenes; punto de equilibrio; gastos operativos/ventas.
**Diagnostic_Questions:** ¿El margen bruto viene cayendo? ¿Los costos crecen más que las ventas? ¿Se pueden trasladar aumentos de costos a precios? ¿El mix de ventas está empeorando? ¿Los gastos fijos están controlados?
**Recommended_Actions:** Analizar rentabilidad por producto/cliente; reducir costos variables; optimizar mix de ventas; ajustar precios; eliminar líneas no rentables; renegociar con proveedores; implementar programa de eficiencia.
**Related_Patterns:** RSK-001, RSK-005, RSK-006, RSK-009, RSK-010

### RSK-005
**Pattern_Name:** Alta Dependencia de Financiamiento de Corto Plazo
**Category:** Riesgo Financiero
**Description:** La empresa financia activos de largo plazo con pasivos de corto plazo, generando un descalce de plazos que expone a riesgo de refinanciación constante.
**Typical_Causes:** Falta de acceso a crédito de largo plazo; urgencia de financiamiento; mala estructuración financiera; crecimiento no planificado; desconocimiento de finanzas corporativas.
**Observable_Symptoms:** La empresa renueva préstamos de corto plazo constantemente; usa sobregiros para inversiones fijas; paga tasas altas por financiamiento de largo plazo con instrumentos cortos; incertidumbre sobre renovación.
**Early_Warning_Signals:** Pasivo corriente / pasivo total > 60%; deuda de corto plazo financia activos fijos; renovaciones de crédito cada 90 días; tasa de interés efectiva alta; covenants ajustados.
**Business_Impact:** Riesgo de no renovación de líneas; tasas de interés más altas; estrés financiero permanente; imposibilidad de planificar inversiones; mayor exposición a cambios en tasas.
**Severity_Level:** High
**Metrics_To_Check:** Pasivo corriente / pasivo total; deuda CP / deuda total; relación activos LP / pasivos CP; tasa de interés efectiva; perfil de vencimientos.
**Diagnostic_Questions:** ¿Qué % de la deuda es de corto plazo? ¿Se financia activo fijo con deuda de corto plazo? ¿Las líneas de crédito son revolventes? ¿Hay certeza de renovación? ¿Cuál es el costo de la deuda?
**Recommended_Actions:** Reestructurar deuda: convertir CP en LP; buscar financiamiento de LP para activos fijos; fortalecer patrimonio; mejorar perfil de vencimientos; negociar líneas comprometidas.
**Related_Patterns:** RSK-001, RSK-002, RSK-006, RSK-008, RSK-010

### RSK-006
**Pattern_Name:** Estacionalidad Financiera no Gestionada
**Category:** Riesgo Financiero
**Description:** La empresa enfrenta fluctuaciones estacionales significativas en ingresos y gastos que no son adecuadamente anticipadas, generando déficits de caja en períodos bajos.
**Typical_Causes:** Negocio con marcada estacionalidad (turismo, agricultura, retail); falta de planificación financiera estacional; ausencia de reservas; descalce entre ciclos de ingreso y gasto.
**Observable_Symptoms:** La caja es abundante en temporada alta y escasa en temporada baja; se acumulan deudas en temporada baja; dificultad para pagar gastos fijos en meses flojos; estrés financiero recurrente.
**Early_Warning_Signals:** Variación de ingresos > 40% entre meses; caja mínima en temporada baja < 10% de caja máxima; uso de deuda para cubrir temporada baja; patrón de 3-4 meses de déficit cada año.
**Business_Impact:** Estrés financiero recurrente; imposibilidad de planificar; costos financieros por financiar temporada baja; riesgo de impago en meses malos; desmotivación del equipo.
**Severity_Level:** Medium
**Metrics_To_Check:** Variación de ingresos mensual; caja máxima vs mínima; meses de déficit; costo de financiamiento estacional; rentabilidad por temporada.
**Diagnostic_Questions:** ¿La empresa tiene temporadas marcadas? ¿Cómo se financia en temporada baja? ¿Hay reservas para meses flojos? ¿Los gastos fijos se ajustan? ¿Se planifica la estacionalidad?
**Recommended_Actions:** Crear fondo de reserva en temporada alta; negociar financiamiento estacional anticipado; diversificar ingresos con productos contra-cíclicos; ajustar gastos variables en temporada baja; proyectar flujo anual.
**Related_Patterns:** RSK-001, RSK-003, RSK-009, RSK-010, RSK-096

### RSK-007
**Pattern_Name:** Riesgo Cambiario no Cubierto
**Category:** Riesgo Financiero
**Description:** La empresa tiene exposición significativa a fluctuaciones del tipo de cambio (ingresos o costos en moneda extranjera) sin cobertura adecuada, afectando su rentabilidad y flujo de caja.
**Typical_Causes:** Importación de insumos sin cobertura; ventas en moneda extranjera; deuda en USD con ingresos en moneda local; falta de políticas de cobertura; desconocimiento de instrumentos financieros.
**Observable_Symptoms:** Resultados financieros volátiles por tipo de cambio; márgenes que cambian con el TC; dificultad para presupuestar; deuda en USD crece en moneda local; costos de insumos importados impredecibles.
**Early_Warning_Signals:** Exposición neta en USD > 30% del EBITDA; costos importados > 40% del costo total; deuda en USD no cubierta; volatilidad del TC afecta resultados; no hay instrumentos de cobertura.
**Business_Impact:** Rentabilidad volátil; imposibilidad de presupuestar con certeza; riesgo de pérdidas cambiarias significativas; dificultad para fijar precios; impacto en flujo de caja.
**Severity_Level:** High
**Metrics_To_Check:** Exposición neta en USD; % de costos importados; % de ingresos en USD; cobertura de TC; sensibilidad de EBITDA a variación del TC.
**Diagnostic_Questions:** ¿La empresa tiene ingresos o costos en moneda extranjera? ¿Hay deuda en USD? ¿Está cubierta la exposición? ¿Cómo afecta el TC al margen? ¿Hay política de cobertura cambiaria?
**Recommended_Actions:** Cubrir exposición con forwards/opciones; calzar ingresos y costos en misma moneda; endeudarse en moneda de ingresos; mantener cuentas en USD; establecer política de cobertura; diversificar mercados.
**Related_Patterns:** RSK-004, RSK-006, RSK-008, RSK-010, RSK-013

### RSK-008
**Pattern_Name:** Riesgo de Tasas de Interés
**Category:** Riesgo Financiero
**Description:** La empresa tiene deuda a tasa variable que expone sus resultados a fluctuaciones en las tasas de interés, incrementando el costo financiero cuando las tasas suben.
**Typical_Causes:** Deuda contratada a tasa variable; falta de cobertura de tasas; desconocimiento del riesgo; financiamiento sin asesoría; ausencia de política financiera.
**Observable_Symptoms:** El gasto financiero varía significativamente con cambios en tasas; presupuesto de intereses es incierto; las utilidades caen cuando suben las tasas; dificultad para proyectar flujo.
**Early_Warning_Signals:** Deuda a tasa variable / deuda total > 50%; gasto financiero varía > 20% con cambios de 1% en tasas; cobertura de intereses ajustada; sin swaps ni caps; alta sensibilidad a tasas.
**Business_Impact:** Mayor costo financiero en ciclos alcistas; menor rentabilidad; estrés de flujo de caja; dificultad para presupuestar; posible incumplimiento de covenants.
**Severity_Level:** Medium
**Metrics_To_Check:** % deuda a tasa variable; sensibilidad de gasto financiero a +1% de tasas; cobertura de intereses en escenario de tasas altas; perfil de vencimientos; covenants.
**Diagnostic_Questions:** ¿Qué % de la deuda es a tasa variable? ¿Cuánto subiría el gasto financiero si las tasas suben 2%? ¿Hay cobertura? ¿Los covenants consideran subida de tasas? ¿Se ha presupuestado?
**Recommended_Actions:** Convertir deuda variable a fija; contratar swaps/caps de tasas; diversificar fuentes de financiamiento; mantener colchón de cobertura de intereses > 2.5x; modelar sensibilidad a tasas.
**Related_Patterns:** RSK-001, RSK-002, RSK-005, RSK-007, RSK-010

### RSK-009
**Pattern_Name:** Concentración Sectorial o Geográfica
**Category:** Riesgo Financiero
**Description:** La empresa depende excesivamente de un solo sector económico o región geográfica, exponiéndola a riesgos idiosincráticos de ese sector o zona.
**Typical_Causes:** Negocio fundado en un sector específico; falta de diversificación; ventajas competitivas locales; desconocimiento de otros mercados; barreras de entrada a nuevas regiones.
**Observable_Symptoms:** Todos los clientes son del mismo sector/región; una crisis sectorial afecta a toda la cartera; no hay ventas fuera de la región; la economía local determina el desempeño; dificultad para expandirse.
**Early_Warning_Signals:** 100% de ingresos de un sector; ingresos de una sola región > 80%; correlación alta entre desempeño y ciclo sectorial; sin presencia en otros sectores/regiones; crecimiento limitado por tamaño del mercado.
**Business_Impact:** Alta vulnerabilidad a ciclos sectoriales; imposibilidad de compensar crisis local con otras regiones; crecimiento limitado; riesgo de desaparición del sector; dependencia de políticas locales.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos por sector; % de ingresos por región; correlación con ciclo sectorial; concentración geográfica; crecimiento potencial por expansión.
**Diagnostic_Questions:** ¿La empresa depende de un solo sector? ¿Una crisis sectorial la afectaría gravemente? ¿Hay presencia en otras regiones? ¿Hay plan de diversificación? ¿El mercado local es suficiente?
**Recommended_Actions:** Desarrollar estrategia de diversificación sectorial; expandir geográficamente; adquirir empresas en otros sectores; desarrollar productos para nuevos mercados; crear alianzas en otras regiones.
**Related_Patterns:** RSK-003, RSK-004, RSK-006, RSK-093, RSK-094

### RSK-010
**Pattern_Name:** Insuficiencia de Capital de Trabajo
**Category:** Riesgo Financiero
**Description:** La empresa no cuenta con capital de trabajo suficiente para financiar su ciclo operativo normal, afectando su capacidad para operar y crecer.
**Typical_Causes:** Crecimiento acelerado no financiado; ciclos de conversión de efectivo largos; baja rentabilidad; mala gestión de inventarios y cuentas por cobrar; distribución de utilidades excesiva.
**Observable_Symptoms:** Proveedores no cobrados a tiempo; falta de materiales por no pagar; descuentos perdidos; crecimiento limitado por falta de capital; uso de proveedores como fuente de financiamiento.
**Early_Warning_Signals:** Capital de trabajo neto negativo; ciclo de conversión de efectivo > 60 días; días de inventario crecientes; días de cobro > días de pago; rotación de proveedores lenta.
**Business_Impact:** Operaciones restringidas; incapacidad para aprovechar oportunidades; pérdida de proveedores; descuentos perdidos; crecimiento limitado; estrés financiero permanente.
**Severity_Level:** Critical
**Metrics_To_Check:** Capital de trabajo neto; ciclo de conversión de efectivo; días de inventario; días de cuentas por cobrar; días de cuentas por pagar.
**Diagnostic_Questions:** ¿El capital de trabajo es suficiente para las operaciones? ¿Cuántos días tarda en convertir inventario en efectivo? ¿Los proveedores financian las operaciones? ¿Hay estrés de caja?
**Recommended_Actions:** Reducir ciclo de conversión de efectivo; mejorar cobranzas; negociar plazos con proveedores; optimizar inventarios; aportar capital de socios; buscar financiamiento de capital de trabajo.
**Related_Patterns:** RSK-001, RSK-002, RSK-003, RSK-005, RSK-006

### RSK-011
**Pattern_Name:** Riesgo de Fraude Financiero Interno
**Category:** Riesgo Financiero
**Description:** La empresa carece de controles internos suficientes para prevenir o detectar fraudes financieros cometidos por empleados, socios o terceros, exponiéndola a pérdidas económicas.
**Typical_Causes:** Falta de segregación de funciones; confianza excesiva en personal clave; ausencia de auditoría interna; controles débiles; cultura de "familia" que relaja controles; rotación de personal en finanzas.
**Observable_Symptoms:** Diferencias en conciliaciones no explicadas; pagos a proveedores no registrados; gastos sin respaldo; inventarios con diferencias; empleados con acceso sin supervisión.
**Early_Warning_Signals:** Una sola persona maneja todo el ciclo de pagos; conciliaciones no se hacen regularmente; diferencias contables no investigadas; gastos fuera de lo normal sin explicación; quejas de clientes sobre cobros no registrados.
**Business_Impact:** Pérdidas financieras directas; deterioro de confianza; costos de investigación; daño reputacional; posible acción legal; impacto en resultados.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de diferencias en conciliaciones; % de gastos sin respaldo; rotación en finanzas; antigüedad del personal de finanzas; resultados de auditorías.
**Diagnostic_Questions:** ¿Hay segregación de funciones en finanzas? ¿Una sola persona puede emitir y cobrar cheques? ¿Se hacen conciliaciones periódicas? ¿Hay auditoría interna o externa? ¿Los controles son adecuados?
**Recommended_Actions:** Implementar segregación de funciones; establecer controles duales; realizar auditorías sorpresa; automatizar procesos financieros; crear canal de denuncias; rotar funciones periódicamente.
**Related_Patterns:** RSK-012, RSK-019, RSK-031, RSK-033, RSK-040

### RSK-012
**Pattern_Name:** Información Financiera No Confiable
**Category:** Riesgo Financiero
**Description:** Los estados financieros y reportes gerenciales no reflejan la realidad económica de la empresa debido a errores contables, retrasos o manipulación, afectando la toma de decisiones.
**Typical_Causes:** Contabilidad llevada sin criterios técnicos; sistemas contables inadecuados; personal no calificado; cierres contables tardíos; presión por mostrar resultados; falta de revisión independiente.
**Observable_Symptoms:** Cierres contables toman más de 30 días; diferencias entre reportes; la gerencia no confía en los números; discrepancias con el banco; inventarios contables vs físicos no coinciden; decisiones basadas en intuición.
**Early_Warning_Signals:** Cierre contable > 15 días; diferencias en conciliaciones bancarias no resueltas; ajustes contables recurrentes; estados financieros no auditados; contador externo sin certificación.
**Business_Impact:** Malas decisiones por información errónea; problemas con bancos y entidades; riesgo fiscal; desconfianza de socios; imposibilidad de acceder a financiamiento; fraudes no detectados.
**Severity_Level:** High
**Metrics_To_Check:** Días para cierre contable; número de ajustes post-cierre; diferencias en conciliaciones; antigüedad de cuentas no conciliadas; % de confianza de la gerencia en los reportes.
**Diagnostic_Questions:** ¿Los estados financieros están al día? ¿Se hacen cierres mensuales? ¿La gerencia confía en los números? ¿Hay diferencias entre contabilidad y realidad? ¿Hay contador titulado?
**Recommended_Actions:** Implementar sistema contable robusto; contratar contador certificado; estandarizar procesos contables; realizar cierres mensuales; auditar estados financieros; capacitar al personal de contabilidad.
**Related_Patterns:** RSK-011, RSK-013, RSK-019, RSK-040, RSK-041

### RSK-013
**Pattern_Name:** Riesgo de Descalce de Plazos Financieros
**Category:** Riesgo Financiero
**Description:** Existe un descalce entre los plazos de los activos y pasivos de la empresa, generando riesgo de liquidez cuando los pasivos de corto plazo vencen antes de que los activos se conviertan en efectivo.
**Typical_Causes:** Financiamiento inadecuado; crecimiento no planificado; plazos de clientes más largos que de proveedores; inversiones en activo fijo con deuda de corto plazo; falta de gestión de plazos.
**Observable_Symptoms:** Dificultad para pagar obligaciones de corto plazo con activos disponibles; renovaciones constantes de deuda; estrés de caja recurrente; descalce evidente en el balance.
**Early_Warning_Signals:** Razón circulante < 1.0; prueba ácida < 0.5; activo corriente no cubre pasivo corriente; descalce > 30 días entre activos y pasivos; capital de trabajo negativo.
**Business_Impact:** Riesgo de default técnico; costos financieros elevados; tensión con acreedores; imposibilidad de aprovechar oportunidades; posible quiebra por iliquidez.
**Severity_Level:** Critical
**Metrics_To_Check:** Razón circulante; prueba ácida; capital de trabajo; brecha de plazos; perfil de vencimientos vs realización de activos.
**Diagnostic_Questions:** ¿Hay descalce entre lo que se cobra y lo que se paga? ¿Los activos de corto plazo cubren los pasivos de corto plazo? ¿Se financia LP con CP? ¿Hay gestión de plazos?
**Recommended_Actions:** Calzar plazos de activos y pasivos; financiar LP con LP y CP con CP; mejorar ciclo de conversión de efectivo; negociar plazos con proveedores; reducir plazos de cobro.
**Related_Patterns:** RSK-001, RSK-002, RSK-005, RSK-008, RSK-010

## Riesgo Operativo

### RSK-014
**Pattern_Name:** Dependencia de Personas Clave en Operaciones
**Category:** Riesgo Operativo
**Description:** La operación depende críticamente de una o pocas personas cuyo conocimiento, habilidades o relaciones no están documentados ni transferidos, generando alto riesgo si se ausentan o renuncian.
**Typical_Causes:** Falta de documentación de procesos; cultura de "héroe"; retención de conocimiento como poder; ausencia de plan de sucesión; alta especialización no transferida.
**Observable_Symptoms:** Solo una persona sabe cómo hacer ciertas tareas; cuando esa persona falta, la operación se detiene; procesos no documentados; renuencia a compartir conocimiento; rotación causa crisis operativas.
**Early_Warning_Signals:** Procesos críticos sin documentar; funciones sin respaldo; % de tareas que solo una persona sabe hacer > 20%; vacaciones no tomadas; tiempo de reemplazo > 2 semanas.
**Business_Impact:** Parálisis operativa si la persona falta; pérdida de clientes; errores costosos; tiempo y costo de reemplazo alto; vulnerabilidad estratégica.
**Severity_Level:** Critical
**Metrics_To_Check:** % de procesos críticos documentados; % de funciones con respaldo; tiempo de reemplazo; rotación en posiciones clave; brecha de conocimiento.
**Diagnostic_Questions:** ¿Qué pasaría si el operador clave no viene mañana? ¿Los procesos están documentados? ¿Hay respaldo para cada función crítica? ¿El conocimiento está distribuido? ¿Hay plan de sucesión?
**Recommended_Actions:** Documentar todos los procesos críticos; crear manuales operativos; implementar rotación de funciones; designar respaldos; grabar procedimientos; establecer plan de sucesión.
**Related_Patterns:** RSK-018, RSK-023, RSK-118, RSK-119, RSK-124

### RSK-015
**Pattern_Name:** Falta de Plan de Continuidad de Negocio
**Category:** Riesgo Operativo
**Description:** La empresa no tiene un plan documentado para mantener operaciones críticas durante y después de una interrupción significativa (desastre natural, incendio, pandemia, falla tecnológica).
**Typical_Causes:** Subestimación de riesgos; falta de recursos; "nunca ha pasado"; prioridad a operación diaria; desconocimiento de estándares; empresa pequeña cree que no lo necesita.
**Observable_Symptoms:** No hay plan documentado para emergencias; no se sabe qué hacer si la planta se quema; los datos no están respaldados en otra ubicación; no hay alternativas de operación.
**Early_Warning_Signals:** Sin BCP ni DRP; backups no probados; sin sitio alternativo; sin contactos de emergencia documentados; sin seguro de interrupción de negocio.
**Business_Impact:** Pérdida total de operaciones por tiempo indeterminado; pérdida de clientes; costos de recuperación altos; posible quiebra; daño reputacional irreparable.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de BCP/DRP; RPO y RTO definidos; frecuencia de pruebas; % de sistemas con respaldo; cobertura de seguro.
**Diagnostic_Questions:** ¿Hay plan de continuidad? ¿Los datos están respaldados fuera del sitio? ¿Se han probado los backups? ¿Qué pasa si la oficina principal no está disponible? ¿Hay seguro de interrupción?
**Recommended_Actions:** Desarrollar BCP (Business Continuity Plan); crear DRP (Disaster Recovery Plan); respaldar datos en nube/offsite; probar planes trimestralmente; contratar seguro de interrupción; designar equipo de crisis.
**Related_Patterns:** RSK-016, RSK-022, RSK-050, RSK-052, RSK-060

### RSK-016
**Pattern_Name:** Obsolescencia de Maquinaria y Equipos
**Category:** Riesgo Operativo
**Description:** La empresa opera con maquinaria, equipos o tecnología obsoleta que reduce su competitividad, eficiencia y capacidad de producción, con alto riesgo de fallas.
**Typical_Causes:** Falta de inversión en reposición; priorizar distribución de utilidades sobre reinversión; desconocimiento de tecnología disponible; ciclos de vida de equipo no gestionados; flujo de caja insuficiente.
**Observable_Symptoms:** Equipos con fallas frecuentes; mantenimiento correctivo constante; tecnología muy por detrás de la competencia; baja velocidad de producción; calidad inconsistente.
**Early_Warning_Signals:** Edad promedio de equipos > 10 años; costo de mantenimiento > 30% del valor del equipo; paradas no planificadas > 10% del tiempo; eficiencia global de equipos (OEE) < 60%; repuestos difíciles de conseguir.
**Business_Impact:** Baja productividad; calidad deficiente; mayores costos de mantenimiento; pérdida de competitividad; imposibilidad de producir ciertos productos; accidentes laborales.
**Severity_Level:** High
**Metrics_To_Check:** Edad promedio de equipos; OEE; % de paradas no planificadas; costo de mantenimiento/valor del equipo; disponibilidad de repuestos.
**Diagnostic_Questions:** ¿Cuándo se invirtió por última vez en maquinaria? ¿Cuál es la edad promedio de los equipos? ¿Las fallas son frecuentes? ¿La tecnología está actualizada? ¿La competencia tiene mejor equipo?
**Recommended_Actions:** Elaborar plan de reposición de equipos; presupuestar CAPEX anual; evaluar lease vs compra; implementar mantenimiento preventivo; calcular ROI de nuevas tecnologías; considerar venta de equipos obsoletos.
**Related_Patterns:** RSK-015, RSK-017, RSK-021, RSK-050, RSK-053

### RSK-017
**Pattern_Name:** Mantenimiento Preventivo Deficiente
**Category:** Riesgo Operativo
**Description:** La empresa no realiza mantenimiento preventivo de manera sistemática, operando con un enfoque reactivo que genera paradas no planificadas y costos mayores.
**Typical_Causes:** Cultura de "si funciona no lo arregles"; falta de recursos; desconocimiento de técnicas de mantenimiento; prioridad a producción sobre mantenimiento; personal no capacitado.
**Observable_Symptoms:** Paradas de producción por fallas; reparaciones de emergencia constantes; costos de mantenimiento crecientes; equipos que fallan en el peor momento; no hay programa de mantenimiento.
**Early_Warning_Signals:** % de mantenimiento correctivo > 60% del total; MTBF decreciente; MTTR creciente; sin plan maestro de mantenimiento; frecuencia de fallas aumenta.
**Business_Impact:** Pérdida de producción; costos de reparación mayores; vida útil reducida de equipos; calidad inconsistente; riesgo de accidentes; incumplimiento de plazos.
**Severity_Level:** High
**Metrics_To_Check:** % mantenimiento correctivo vs preventivo; MTBF; MTTR; disponibilidad de equipos; costo de mantenimiento/ventas.
**Diagnostic_Questions:** ¿Hay programa de mantenimiento preventivo? ¿Se sigue? ¿Qué % del mantenimiento es correctivo? ¿Las fallas son predecibles? ¿Se lleva registro de MTBF y MTTR?
**Recommended_Actions:** Implementar programa de mantenimiento preventivo; crear plan maestro con frecuencias; capacitar al equipo; usar CMMS; pasar a mantenimiento predictivo; medir y mejorar KPIs de mantenimiento.
**Related_Patterns:** RSK-016, RSK-018, RSK-021, RSK-022, RSK-053

### RSK-018
**Pattern_Name:** Rotación de Personal Operativo
**Category:** Riesgo Operativo
**Description:** Alta rotación del personal operativo que afecta la continuidad, calidad y eficiencia de las operaciones, incrementando costos de selección, capacitación y curvas de aprendizaje.
**Typical_Causes:** Salarios no competitivos; mal clima laboral; falta de desarrollo; liderazgo deficiente; condiciones de trabajo duras; mejor oferta de competencia.
**Observable_Symptoms:** Constante entrada y salida de personal; nuevos empleados en entrenamiento permanente; errores de personal nuevo; carga extra sobre empleados antiguos; áreas con personal temporal.
**Early_Warning_Signals:** Rotación anual > 30%; antigüedad promedio < 2 años; % de personal con menos de 1 año > 30%; vacantes difíciles de cubrir; aumento de quejas de clientes atribuidas a personal nuevo.
**Business_Impact:** Costos de selección y capacitación; baja productividad; errores y defectos; sobrecarga de empleados antiguos; pérdida de conocimiento; clima laboral deteriorado.
**Severity_Level:** High
**Metrics_To_Check:** Tasa de rotación mensual/anual; antigüedad promedio; tiempo para cubrir vacantes; costo de rotación por empleado; % de personal en período de prueba.
**Diagnostic_Questions:** ¿Cuál es la tasa de rotación? ¿Por qué se va el personal? ¿Los salarios son competitivos? ¿Hay plan de retención? ¿La rotación afecta la operación?
**Recommended_Actions:** Mejorar compensaciones; implementar programa de onboarding; crear plan de carrera; realizar entrevistas de salida; mejorar condiciones laborales; fortalecer liderazgo; medir clima laboral.
**Related_Patterns:** RSK-014, RSK-023, RSK-118, RSK-119, RSK-120

### RSK-019
**Pattern_Name:** Controles Internos Débiles
**Category:** Riesgo Operativo
**Description:** La empresa carece de controles internos adecuados en sus procesos operativos, aumentando el riesgo de errores, fraudes, ineficiencias y pérdidas no detectadas.
**Typical_Causes:** Empresa familiar con poca formalidad; falta de personal especializado; cultura de confianza excesiva; crecimiento sin actualización de controles; ausencia de auditoría.
**Observable_Symptoms:** Procesos sin supervisión; acceso sin restricciones a sistemas; aprobaciones no documentadas; diferencias en inventarios; pagos sin autorización; no hay segregación de funciones.
**Early_Warning_Signals:** Ausencia de políticas documentadas; una persona controla todo un proceso; conciliaciones no periódicas; diferencias no investigadas; sin matriz de riesgos y controles.
**Business_Impact:** Pérdidas por fraude; errores no detectados; multas regulatorias; información financiera no confiable; ineficiencias operativas; desconfianza de stakeholders.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de hallazgos de auditoría; % de procesos con controles documentados; tiempo de detección de errores; número de diferencias no investigadas; % de cumplimiento de políticas.
**Diagnostic_Questions:** ¿Hay políticas documentadas? ¿Hay segregación de funciones en procesos críticos? ¿Se hacen auditorías? ¿Los controles son efectivos? ¿Hay canal de denuncias?
**Recommended_Actions:** Documentar políticas y procedimientos; implementar segregación de funciones; crear matriz de riesgos y controles; realizar auditorías periódicas; automatizar controles; establecer canal de denuncias.
**Related_Patterns:** RSK-011, RSK-012, RSK-014, RSK-022, RSK-031

### RSK-020
**Pattern_Name:** Capacidad de Producción Insuficiente
**Category:** Riesgo Operativo
**Description:** La empresa no tiene capacidad de producción suficiente para atender la demanda actual o proyectada, perdiendo ventas y participación de mercado.
**Typical_Causes:** Crecimiento de demanda no anticipado; falta de inversión en capacidad; cuellos de botella no resueltos; planificación deficiente; equipos obsoletos o lentos.
**Observable_Symptoms:** Pedidos rechazados por falta de capacidad; tiempos de entrega se alargan; la producción no da abasto; se terceriza sin control; clientes insatisfechos por demoras.
**Early_Warning_Signals:** Utilización de capacidad > 90% sostenido; lead time creciente; backlog creciente; pérdida de ventas por capacidad; horas extra recurrentes.
**Business_Impact:** Pérdida de ventas; clientes insatisfechos; participación de mercado decreciente; crecimiento limitado; estrés operativo; costos extra por horas extra y tercerización.
**Severity_Level:** High
**Metrics_To_Check:** % de utilización de capacidad; backlog; lead time; % de ventas perdidas por capacidad; horas extra/ventas.
**Diagnostic_Questions:** ¿La producción está al límite? ¿Se rechazan pedidos por capacidad? ¿El lead time está creciendo? ¿Hay cuellos de botella? ¿Se puede aumentar capacidad?
**Recommended_Actions:** Invertir en nueva capacidad; eliminar cuellos de botella; optimizar procesos; implementar turnos adicionales; tercerizar estratégicamente; mejorar planificación de la producción.
**Related_Patterns:** RSK-016, RSK-021, RSK-024, RSK-053, RSK-095

### RSK-021
**Pattern_Name:** Procesos No Estandarizados
**Category:** Riesgo Operativo
**Description:** Los procesos operativos se ejecutan de manera diferente según la persona, turno o situación, generando variabilidad en calidad, tiempos y costos.
**Typical_Causes:** Falta de documentación de procesos; capacitación insuficiente; cultura de "cada quien hace como sabe"; rotación de personal; procesos evolucionan sin control.
**Observable_Symptoms:** El mismo proceso se hace diferente según quién lo ejecute; resultados variables; errores recurrentes; dificultad para capacitar; calidad inconsistente; cada turno deja el área diferente.
**Early_Warning_Signals:** Variabilidad en tiempo de ciclo > 30%; defectos variables entre turnos/operadores; quejas de clientes por inconsistencia; ausencia de procedimientos escritos; % de procesos estandarizados < 30%.
**Business_Impact:** Calidad inconsistente; errores y retrabajo; dificultad para escalar; alta dependencia de personas; costos variables; imposibilidad de mejorar procesos.
**Severity_Level:** High
**Metrics_To_Check:** % de procesos estandarizados; variabilidad en tiempo de ciclo; variabilidad en calidad; cumplimiento de procedimientos; tiempo de capacitación.
**Diagnostic_Questions:** ¿Los procesos están documentados? ¿Se siguen los procedimientos? ¿Hay variabilidad entre turnos? ¿La calidad es consistente? ¿Es fácil capacitar a nuevos empleados?
**Recommended_Actions:** Documentar procesos estándar; implementar instructivos de trabajo; capacitar al personal; auditar cumplimiento; crear manual de operaciones; establecer indicadores de cumplimiento.
**Related_Patterns:** RSK-014, RSK-018, RSK-022, RSK-024, RSK-025

### RSK-022
**Pattern_Name:** Incumplimiento de Normativas de Seguridad y Salud Ocupacional
**Category:** Riesgo Operativo
**Description:** La empresa no cumple con las normativas de seguridad y salud en el trabajo, exponiendo a los empleados a riesgos de accidentes y a la empresa a sanciones y litigios.
**Typical_Causes:** Falta de cultura de seguridad; desconocimiento de normativa; falta de recursos; prioridad a producción sobre seguridad; ausencia de programa de seguridad.
**Observable_Symptoms:** Accidentes laborales recurrentes; condiciones inseguras; equipo de protección no usado; falta de señalización; ausencia de capacitación en seguridad; no hay brigadas de emergencia.
**Early_Warning_Signals:** Tasa de accidentalidad > promedio sectorial; días perdidos por accidentes; multas o infracciones; condiciones inseguras identificadas y no corregidas; sin comité de seguridad.
**Business_Impact:** Accidentes graves; demandas laborales; multas de autoridades; cierre temporal de operaciones; daño reputacional; costos de compensación; prima de seguro alta.
**Severity_Level:** Critical
**Metrics_To_Check:** Tasa de accidentalidad; días perdidos por accidentes; % de cumplimiento de normativa; número de condiciones inseguras; inversión en seguridad/empleado.
**Diagnostic_Questions:** ¿Hay programa de seguridad? ¿Se cumplen las normas? ¿Hay accidentes recurrentes? ¿El equipo de protección se usa? ¿Hay capacitación en seguridad?
**Recommended_Actions:** Implementar sistema de gestión de seguridad; capacitar al personal; proveer EPP; crear comité de seguridad; realizar inspecciones periódicas; establecer metas de seguridad; contratar seguro adecuado.
**Related_Patterns:** RSK-015, RSK-017, RSK-019, RSK-029, RSK-031

### RSK-023
**Pattern_Name:** Pérdida de Conocimiento Organizacional
**Category:** Riesgo Operativo
**Description:** La empresa pierde conocimiento crítico cuando empleados se jubilan, renuncian o son despedidos, sin que ese conocimiento haya sido documentado o transferido.
**Typical_Causes:** Falta de gestión del conocimiento; cultura de "conocimiento es poder"; rotación de personal; ausencia de procesos de documentación; falta de mentoring.
**Observable_Symptoms:** Cuando alguien se va, la operación se resiente; nuevos empleados cometen errores que ya se habían resuelto; no hay manuales; se reinventa la rueda constantemente.
**Early_Warning_Signals:** Antigüedad promedio alta en puestos clave; conocimiento no documentado; sin plan de sucesión; sin programa de mentoring; rotación de personal con mucha experiencia.
**Business_Impact:** Pérdida de eficiencia; errores recurrentes; dependencia de pocas personas; costo de curvas de aprendizaje; pérdida de ventajas competitivas; riesgo de fuga de know-how a competencia.
**Severity_Level:** High
**Metrics_To_Check:** % de conocimiento documentado; antigüedad promedio; tiempo de integración de nuevos empleados; % de funciones con respaldo; rotación de personal clave.
**Diagnostic_Questions:** ¿El conocimiento crítico está documentado? ¿Qué pasa cuando un empleado clave se va? ¿Hay manuales? ¿Hay programa de mentoring? ¿Se realiza transferencia de conocimiento periódicamente?
**Recommended_Actions:** Implementar sistema de gestión del conocimiento; documentar procesos y lecciones aprendidas; crear manuales; establecer programa de mentoring; grabar procedimientos; realizar rotación de funciones.
**Related_Patterns:** RSK-014, RSK-018, RSK-023, RSK-118, RSK-124

### RSK-024
**Pattern_Name:** Subcontratación No Gestionada
**Category:** Riesgo Operativo
**Description:** La empresa terceriza partes críticas de su operación sin control adecuado, exponiéndose a riesgos de calidad, plazos, dependencia y fuga de conocimiento.
**Typical_Causes:** Búsqueda de reducción de costos; falta de capacidad interna; enfoque en core business; urgencia; desconocimiento de riesgos de tercerización.
**Observable_Symptoms:** Problemas de calidad con servicios tercerizados; retrasos atribuibles a terceros; quejas de clientes por servicios subcontratados; dependencia de un tercero sin alternativa.
**Early_Warning_Signals:** % de procesos tercerizados > 40%; sin SLA con terceros; sin evaluación de proveedores; calidad de terceros inferior a la interna; sin plan B para subcontratación.
**Business_Impact:** Calidad inconsistente; incumplimiento de plazos; dependencia estratégica de terceros; fuga de conocimiento; costos ocultos; daño reputacional por acciones de terceros.
**Severity_Level:** Medium
**Metrics_To_Check:** % de procesos tercerizados; cumplimiento de SLA por terceros; calidad de servicios tercerizados; número de proveedores externos; % de dependencia de un solo tercero.
**Diagnostic_Questions:** ¿Qué procesos están tercerizados? ¿Hay SLA documentados? ¿Se evalúa el desempeño de terceros? ¿Hay alternativas? ¿La calidad de terceros es aceptable?
**Recommended_Actions:** Establecer SLA claros con terceros; evaluar desempeño periódicamente; mantener alternativas; no tercerizar procesos críticos sin supervisión; desarrollar capacidad interna gradualmente.
**Related_Patterns:** RSK-020, RSK-021, RSK-106, RSK-107, RSK-112

### RSK-025
**Pattern_Name:** Gestión de Inventarios Ineficiente
**Category:** Riesgo Operativo
**Description:** La empresa no gestiona adecuadamente sus inventarios, resultando en excesos que inmovilizan capital o faltantes que interrumpen la operación.
**Typical_Causes:** Falta de sistema de gestión de inventarios; pronósticos deficientes; compras no planificadas; rotación de personal de inventarios; ausencia de políticas de inventario.
**Observable_Symptoms:** Faltantes de materiales que detienen producción; exceso de ciertos productos; inventario ocioso; diferencias entre inventario físico y contable; productos vencidos u obsoletos.
**Early_Warning_Signals:** Rotación de inventario baja; días de inventario > 60; faltantes recurrentes; precisión de inventario < 95%; % de inventario obsoleto > 10%.
**Business_Impact:** Capital inmovilizado; pérdidas por obsolescencia; paradas de producción; ventas perdidas por falta de stock; costos de almacenamiento; diferencias contables.
**Severity_Level:** High
**Metrics_To_Check:** Rotación de inventario; días de inventario; precisión de inventario; % de inventario obsoleto; nivel de servicio de inventario.
**Diagnostic_Questions:** ¿Se quedan sin stock frecuentemente? ¿Hay mucho inventario que no rota? ¿El inventario físico coincide con el contable? ¿Hay productos vencidos? ¿Se usa algún sistema de gestión?
**Recommended_Actions:** Implementar sistema de gestión de inventarios; clasificar ABC; establecer políticas de stock; mejorar pronósticos; realizar conteos cíclicos; reducir lotes de compra; eliminar obsoletos.
**Related_Patterns:** RSK-010, RSK-016, RSK-020, RSK-026, RSK-109

### RSK-026
**Pattern_Name:** Riesgo de Sobreproducción
**Category:** Riesgo Operativo
**Description:** La empresa produce más de lo que la demanda requiere, generando inventarios excesivos, costos de almacenamiento, riesgo de obsolescencia y capital inmovilizado.
**Typical_Causes:** Producción contra pronóstico en lugar de contra pedido; lotes económicos mal calculados; cultura de "mantener las máquinas ocupadas"; falta de coordinación ventas-producción; incentivos a producir volumen.
**Observable_Symptoms:** Inventario de producto terminado crece; bodegas llenas; productos se quedan en inventario mucho tiempo; descuentos para liquidar excesos; producción sigue aunque haya inventario.
**Early_Warning_Signals:** Rotación de producto terminado baja; inventario de PT crece más que ventas; producción > ventas sostenidamente; espacio de almacenamiento insuficiente; % de producto terminado en inventario > 30% de ventas.
**Business_Impact:** Capital inmovilizado; costos de almacenamiento; riesgo de obsolescencia; descuentos para liquidar; menor rentabilidad; espacio ocupado innecesariamente.
**Severity_Level:** Medium
**Metrics_To_Check:** Rotación de producto terminado; producción vs ventas; días de inventario de PT; % de inventario obsoleto; costo de almacenamiento/ventas.
**Diagnostic_Questions:** ¿Se produce contra pedido o contra pronóstico? ¿El inventario de PT crece? ¿Hay productos obsoletos en inventario? ¿Se producen lotes grandes por eficiencia? ¿Las ventas consumen la producción?
**Recommended_Actions:** Producir contra pedido (make-to-order); reducir tamaño de lotes; alinear producción con ventas; implementar pull system; revisar políticas de producción; eliminar incentivos a producir volumen.
**Related_Patterns:** RSK-010, RSK-020, RSK-025, RSK-095, RSK-096


## Riesgo Legal

### RSK-027
**Pattern_Name:** Incumplimiento Contractual
**Category:** Riesgo Legal
**Description:** La empresa no cumple con las obligaciones establecidas en contratos con clientes, proveedores, socios o empleados, exponiéndose a demandas, penalidades y daño reputacional.
**Typical_Causes:** Contratos mal redactados o ambiguos; falta de revisión legal; desconocimiento de obligaciones; incapacidad operativa para cumplir; cultura de "contrato es un papel".
**Observable_Symptoms:** Quejas de clientes sobre incumplimiento; proveedores reclaman penalidades; disputas contractuales frecuentes; contratos estándar sin revisar; cláusulas ambiguas.
**Early_Warning_Signals:** Número de disputas contractuales > 3 al año; multas por incumplimiento; quejas formales de contrapartes; contratos sin revisión legal; cláusulas ambiguas o contradictorias.
**Business_Impact:** Demandas y costos legales; penalidades; pérdida de clientes; daño reputacional; relaciones comerciales deterioradas; pagos de indemnizaciones.
**Severity_Level:** High
**Metrics_To_Check:** Número de disputas contractuales; % de contratos con revisión legal; tiempo de resolución de disputas; costo de litigios/ventas; cumplimiento de hitos contractuales.
**Diagnostic_Questions:** ¿Los contratos son revisados por un abogado? ¿Se cumplen las obligaciones contractuales? ¿Hay disputas recurrentes? ¿Las cláusulas son claras? ¿Hay penalidades?
**Recommended_Actions:** Revisar todos los contratos con abogado; estandarizar cláusulas; capacitar al equipo en obligaciones contractuales; cumplir hitos; mantener registro de contratos; negociar antes de incumplir.
**Related_Patterns:** RSK-028, RSK-030, RSK-031, RSK-032, RSK-038

### RSK-028
**Pattern_Name:** Ausencia de Contratos Formales
**Category:** Riesgo Legal
**Description:** La empresa opera acuerdos verbales o informales con clientes, proveedores, empleados o socios, sin documentación contractual que establezca derechos y obligaciones.
**Typical_Causes:** Cultura de confianza y palabra; informalidad en la gestión; ahorro en costos legales; urgencia por empezar; desconocimiento de riesgos legales; tradición familiar.
**Observable_Symptoms:** Acuerdos verbales con proveedores; clientes sin contrato firmado; empleados sin contrato laboral; términos no documentados; disputas "porque no se acordó así".
**Early_Warning_Signals:** % de clientes con contrato < 50%; % de proveedores con contrato < 50%; acuerdos verbales > 30% de transacciones; disputas por malentendidos; reclamos sin sustento documental.
**Business_Impact:** Imposibilidad de hacer valer derechos; disputas y litigios; incapacidad de cobrar; incumplimiento laboral; riesgos fiscales; vulnerabilidad ante contrapartes.
**Severity_Level:** High
**Metrics_To_Check:** % de clientes con contrato; % de proveedores con contrato; % de empleados con contrato; número de disputas sin contrato; antigüedad de contratos.
**Diagnostic_Questions:** ¿Todos los clientes tienen contrato? ¿Los proveedores tienen órdenes de compra firmadas? ¿Hay contratos laborales? ¿Se documentan los acuerdos? ¿Hay disputas por falta de contrato?
**Recommended_Actions:** Formalizar todos los acuerdos comerciales; crear contratos estándar; implementar órdenes de compra; contratar asesoría legal; documentar todos los términos; capacitar al equipo.
**Related_Patterns:** RSK-027, RSK-029, RSK-030, RSK-032, RSK-033

### RSK-029
**Pattern_Name:** Riesgo Laboral y Demandas de Empleados
**Category:** Riesgo Legal
**Description:** La empresa enfrenta riesgo de demandas laborales por incumplimiento de obligaciones con empleados, incluyendo condiciones de trabajo, beneficios, despidos y seguridad social.
**Typical_Causes:** Contratos laborales mal redactados; falta de pago de beneficios; despidos sin causa justificada; incumplimiento de seguridad social; desconocimiento de normativa laboral.
**Observable_Symptoms:** Empleados reclaman beneficios no pagados; demandas laborales frecuentes; inspecciones del ministerio de trabajo; rotación alta y reclamos post-salida; liquidaciones mal calculadas.
**Early_Warning_Signals:** Número de demandas laborales > 1 al año; reclamos de empleados sobre condiciones; inspecciones laborales; % de cumplimiento de obligaciones laborales < 80%; quejas informales recurrentes.
**Business_Impact:** Costos de indemnizaciones; multas laborales; daño reputacional; clima laboral deteriorado; desgaste de la gerencia; tiempo dedicado a litigios.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de demandas laborales; % de cumplimiento de obligaciones laborales; costo de litigios laborales/ventas; rotación post-demanda; tiempo de resolución.
**Diagnostic_Questions:** ¿Se cumplen todas las obligaciones laborales? ¿Hay demandas laborales? ¿Los contratos están en regla? ¿Se pagan todos los beneficios? ¿Las liquidaciones son correctas?
**Recommended_Actions:** Cumplir normativa laboral; contratar asesoría laboral; mantener contratos actualizados; pagar beneficios según ley; documentar despidos; realizar auditorías laborales periódicas.
**Related_Patterns:** RSK-019, RSK-022, RSK-027, RSK-031, RSK-118

### RSK-030
**Pattern_Name:** Riesgo de Propiedad Intelectual
**Category:** Riesgo Legal
**Description:** La empresa no protege adecuadamente su propiedad intelectual (marcas, patentes, secretos comerciales) o infringe derechos de terceros, exponiéndose a litigios y pérdida de activos intangibles.
**Typical_Causes:** Desconocimiento de PI; falta de recursos para registro; cultura de "no pasa nada"; ausencia de acuerdos de confidencialidad; desarrollo sin verificar derechos de terceros.
**Observable_Symptoms:** Competidores copian productos sin consecuencia; empleados usan software sin licencia; no hay marcas registradas; secretos comerciales no protegidos; acuerdos verbales de confidencialidad.
**Early_Warning_Signals:** Marcas no registradas; ausencia de NDA con empleados y terceros; uso de software sin licencia; productos fácilmente copiables; desarrollo sin búsqueda de anterioridad.
**Business_Impact:** Pérdida de ventaja competitiva; demanda por infracción; costos de litigio; imposibilidad de accionar contra infractores; pérdida de activos intangibles; multas por uso ilegal de software.
**Severity_Level:** High
**Metrics_To_Check:** Número de marcas/patentes registradas; % de empleados con NDA; % de software licenciado; número de disputas de PI; inversión en protección de PI.
**Diagnostic_Questions:** ¿Las marcas están registradas? ¿Hay patentes? ¿Los empleados firman NDA? ¿El software tiene licencia? ¿Los secretos comerciales están protegidos?
**Recommended_Actions:** Registrar marcas y patentes; implementar NDA para empleados y terceros; auditar licencias de software; documentar secretos comerciales; realizar búsquedas de anterioridad; contratar abogado de PI.
**Related_Patterns:** RSK-027, RSK-028, RSK-032, RSK-038, RSK-075

### RSK-031
**Pattern_Name:** Exposición a Litigios y Juicios
**Category:** Riesgo Legal
**Description:** La empresa está expuesta a litigios de diversa naturaleza (comerciales, laborales, civiles) que consumen recursos, tiempo gerencial y pueden resultar en condenas significativas.
**Typical_Causes:** Incumplimiento de obligaciones; contratos mal redactados; falta de asesoría legal; cultura confrontacional; riesgos no gestionados proactivamente.
**Observable_Symptoms:** La empresa tiene juicios en curso; reuniones recurrentes con abogados; provisiones por litigios; gastos legales significativos; la gerencia se distrae con pleitos.
**Early_Warning_Signals:** Número de litigios activos > 2; gastos legales/ventas > 1%; tiempo gerencial dedicado a litigios > 10%; provisiones por litigios > 5% del patrimonio; litigios que se acumulan.
**Business_Impact:** Costos legales significativos; distracción gerencial; condenas económicas; daño reputacional; imposibilidad de acceder a crédito; embargos; cierre de operaciones.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de litigios activos; gastos legales/ventas; provisiones por litigios; tiempo gerencial dedicado; antigüedad de litigios; tasa de éxito en litigios.
**Diagnostic_Questions:** ¿Cuántos juicios tiene la empresa? ¿Hay provisiones para contingencias? ¿La gerencia dedica mucho tiempo a litigios? ¿Se gestionan los riesgos legalmente? ¿Hay abogado de confianza?
**Recommended_Actions:** Prevenir litigios mediante cumplimiento; resolver disputas extrajudicialmente; contratar asesoría legal proactiva; provisionar contingencias; implementar políticas de cumplimiento; resolver conflictos rápidamente.
**Related_Patterns:** RSK-027, RSK-029, RSK-030, RSK-033, RSK-038

### RSK-032
**Pattern_Name:** Incumplimiento de Normativa Sectorial
**Category:** Riesgo Legal
**Description:** La empresa no cumple con regulaciones específicas de su sector (salud, alimentos, construcción, financiero, etc.), exponiéndose a sanciones, multas o cierre.
**Typical_Causes:** Desconocimiento de normativa; falta de recursos para cumplir; cambios regulatorios no monitoreados; ausencia de función de compliance; prioridad a operación sobre regulación.
**Observable_Symptoms:** Autoridades realizan inspecciones; multas sectoriales recurrentes; requisitos regulatorios no cumplidos; licencias vencidas; certificaciones perdidas; productos no合规.
**Early_Warning_Signals:** Inspecciones de autoridades; multas sectoriales; % de cumplimiento regulatorio < 80%; licencias próximas a vencer; cambios normativos no implementados.
**Business_Impact:** Multas significativas; cierre temporal o definitivo; pérdida de licencias; daño reputacional; imposibilidad de operar; costos de remediación; pérdida de clientes que exigen cumplimiento.
**Severity_Level:** Critical
**Metrics_To_Check:** % de cumplimiento regulatorio; número de multas; estado de licencias; frecuencia de inspecciones; tiempo de respuesta a cambios normativos.
**Diagnostic_Questions:** ¿Se cumple la normativa sectorial? ¿Las licencias están vigentes? ¿Se monitorean cambios regulatorios? ¿Hay inspecciones recientes? ¿Hay función de compliance?
**Recommended_Actions:** Designar responsable de compliance; monitorear cambios regulatorios; mantener licencias al día; implementar auditorías de cumplimiento; capacitar al personal; contratar asesoría especializada.
**Related_Patterns:** RSK-027, RSK-031, RSK-033, RSK-038, RSK-039

### RSK-033
**Pattern_Name:** Riesgo de Corrupción y Soborno
**Category:** Riesgo Legal
**Description:** La empresa enfrenta riesgo de actos de corrupción, soborno o prácticas antiéticas por parte de empleados, agentes o socios, con graves consecuencias legales y reputacionales.
**Typical_Causes:** Falta de políticas anticorrupción; cultura de "así se hacen las cosas"; presión por resultados; controles débiles; intermediarios sin supervisión; operaciones en países de alto riesgo.
**Observable_Symptoms:** Pagos a funcionarios sin justificación; comisiones inusuales a intermediarios; contratos sin transparencia; reportes de gastos sin respaldo; rumores de prácticas cuestionables.
**Early_Warning_Signals:** Sin código de ética; sin política anticorrupción; pagos en efectivo frecuentes; intermediarios sin contrato; donaciones sin control; operaciones en países con alta percepción de corrupción.
**Business_Impact:** Procesos penales; multas millonarias; inhabilitación para contratar con el Estado; daño reputacional irreparable; pérdida de socios; cárcel para directivos.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de políticas anticorrupción; % de empleados capacitados en ética; número de denuncias; % de intermediarios evaluados; transacciones en efectivo.
**Diagnostic_Questions:** ¿Hay código de ética? ¿Hay política anticorrupción? ¿Se capacita al personal? ¿Hay canal de denuncias? ¿Se auditan los pagos a intermediarios?
**Recommended_Actions:** Implementar código de ética y política anticorrupción; capacitar al personal; establecer canal de denuncias; auditar pagos sospechosos; debida diligencia de intermediarios; cero tolerancia.
**Related_Patterns:** RSK-011, RSK-019, RSK-031, RSK-038, RSK-067

### RSK-034
**Pattern_Name:** Contratos con Cláusulas Abusivas o Desfavorables
**Category:** Riesgo Legal
**Description:** La empresa firma contratos con cláusulas que la perjudican significativamente, ya sea por desconocimiento, asimetría de poder o falta de negociación, exponiéndola a pérdidas.
**Typical_Causes:** Asimetría de poder con grandes clientes/proveedores; falta de revisión legal; urgencia por cerrar el trato; contratos estándar de la contraparte sin negociar; desconocimiento de implicaciones.
**Observable_Symptoms:** Cláusulas que favorecen a la contraparte; penalidades desproporcionadas; plazos muy ajustados; responsabilidades ilimitadas; indemnizaciones excesivas; imposibilidad de terminar el contrato.
**Early_Warning_Signals:** Contratos sin negociar; ausencia de revisión legal; cláusulas leoninas; penalidades > 20% del contrato; obligaciones unilaterales; plazos irracionales.
**Business_Impact:** Pérdidas por penalidades; imposibilidad de salir del contrato; responsabilidades excesivas; costos inesperados; desventaja competitiva; litigios.
**Severity_Level:** High
**Metrics_To_Check:** % de contratos con revisión legal; número de cláusulas desfavorables; % de contratos negociados; penalidades pagadas; costos por cláusulas abusivas.
**Diagnostic_Questions:** ¿Los contratos son revisados por abogados? ¿Se negocian las cláusulas? ¿Hay cláusulas que perjudican a la empresa? ¿Las penalidades son proporcionales? ¿Se pueden renegociar?
**Recommended_Actions:** Revisar todos los contratos con abogado; negociar cláusulas desfavorables; establecer contrato estándar propio; capacitar en negociación; evitar contratos con desequilibrio excesivo.
**Related_Patterns:** RSK-027, RSK-028, RSK-031, RSK-035, RSK-038

### RSK-035
**Pattern_Name:** Riesgo por Garantías y Avales Otorgados
**Category:** Riesgo Legal
**Description:** La empresa ha otorgado garantías o avales a terceros (clientes, proveedores, socios) que podrían ejecutarse en caso de incumplimiento, generando pérdidas financieras significativas.
**Typical_Causes:** Confianza excesiva en terceros; presión para cerrar negocios; falta de evaluación de riesgo de contraparte; desconocimiento de implicaciones; garantías cruzadas sin control.
**Observable_Symptoms:** Garantías otorgadas sin límite; avales a terceros sin respaldo; no se monitorean las garantías; el banco ejecuta garantías por incumplimiento de terceros.
**Early_Warning_Signals:** Garantías/avales > 30% del patrimonio; sin evaluación de contraparte; garantías sin plazo definido; terceros con problemas financieros; garantías no registradas contablemente.
**Business_Impact:** Pérdidas por ejecución de garantías; deterioro de relación bancaria; impacto en capacidad de endeudamiento; riesgo de insolvencia; litigios con terceros.
**Severity_Level:** High
**Metrics_To_Check:** Garantías otorgadas/patrimonio; % de garantías con evaluación de riesgo; número de garantías ejecutadas; plazo promedio de garantías; contrapartes con garantía vigente.
**Diagnostic_Questions:** ¿Qué garantías ha otorgado la empresa? ¿Hay límites? ¿Se evalúa el riesgo de la contraparte? ¿Las garantías están registradas? ¿Hay monitoreo?
**Recommended_Actions:** Establecer política de garantías; limitar garantías a % del patrimonio; evaluar riesgo de contraparte; registrar todas las garantías; monitorear situación de terceros; exigir contra-garantías.
**Related_Patterns:** RSK-027, RSK-031, RSK-034, RSK-038, RSK-108

### RSK-036
**Pattern_Name:** Riesgo Regulatorio por Cambios Legales
**Category:** Riesgo Legal
**Description:** La empresa está expuesta a cambios en leyes y regulaciones (laborales, tributarias, ambientales, sectoriales) que pueden afectar su operación, costos o modelo de negocio.
**Typical_Causes:** Falta de monitoreo legal; ausencia de asesoría legal permanente; sector altamente regulado; cambios políticos que afectan regulación; desconocimiento de proyectos de ley.
**Observable_Symptoms:** Cambios legales toman a la empresa por sorpresa; necesidad de ajustar operación rápidamente; costos inesperados por nuevas regulaciones; multas por incumplimiento de nuevas normas.
**Early_Warning_Signals:** Sin suscripción a servicios de actualización legal; sin abogado externo; sector con alta frecuencia de cambios regulatorios; proyectos de ley que afectan a la empresa no monitoreados.
**Business_Impact:** Costos inesperados de cumplimiento; necesidad de cambiar modelo de negocio; multas por desactualización; pérdida de ventajas competitivas; inversiones forzadas.
**Severity_Level:** Medium
**Metrics_To_Check:** Número de cambios regulatorios que afectan a la empresa; tiempo de respuesta a cambios; costo de cumplimiento regulatorio/ventas; % de cumplimiento; multas por desactualización.
**Diagnostic_Questions:** ¿Se monitorean los cambios legales? ¿Hay asesoría legal permanente? ¿Los cambios regulatorios toman a la empresa desprevenida? ¿Hay costos inesperados? ¿El sector es muy regulado?
**Recommended_Actions:** Suscribirse a servicios de actualización legal; mantener asesoría legal permanente; participar en asociaciones sectoriales; anticipar cambios regulatorios; modelar impacto de cambios potenciales.
**Related_Patterns:** RSK-032, RSK-038, RSK-039, RSK-075, RSK-077

### RSK-037
**Pattern_Name:** Riesgo Ambiental y de Sostenibilidad
**Category:** Riesgo Legal
**Description:** La empresa incumple normativas ambientales o no gestiona adecuadamente su impacto ambiental, exponiéndose a multas, sanciones, cierre de operaciones y daño reputacional.
**Typical_Causes:** Desconocimiento de normativa ambiental; falta de recursos para cumplimiento; procesos productivos contaminantes; ausencia de gestión ambiental; prioridad a producción sobre ambiente.
**Observable_Symptoms:** Multas ambientales; quejas de la comunidad; inspecciones de autoridades ambientales; residuos no gestionados adecuadamente; procesos sin permisos ambientales.
**Early_Warning_Signals:** Sin licencia ambiental; multas ambientales recurrentes; % de cumplimiento ambiental < 60%; quejas de vecinos; ausencia de política ambiental; residuos sin disposición adecuada.
**Business_Impact:** Multas significativas; cierre temporal o definitivo; daño reputacional; costos de remediación; pérdida de clientes que exigen sostenibilidad; litigios con comunidades.
**Severity_Level:** High
**Metrics_To_Check:** % de cumplimiento ambiental; número de multas; licencias ambientales vigentes; inversión en gestión ambiental/ventas; huella de carbono.
**Diagnostic_Questions:** ¿Se cumple la normativa ambiental? ¿Hay licencias ambientales? ¿Hay residuos sin gestionar? ¿Hay quejas de la comunidad? ¿Hay política ambiental?
**Recommended_Actions:** Obtener licencias ambientales; implementar sistema de gestión ambiental; tratar residuos adecuadamente; capacitar al personal; monitorear cumplimiento; certificar ISO 14001; relacionarse con comunidad.
**Related_Patterns:** RSK-022, RSK-032, RSK-036, RSK-038, RSK-068

### RSK-038
**Pattern_Name:** Falta de Asesoría Legal Permanente
**Category:** Riesgo Legal
**Description:** La empresa no cuenta con asesoría legal permanente o la que tiene es insuficiente para cubrir todas las áreas de exposición legal del negocio.
**Typical_Causes:** Ahorro en costos legales; percepción de que "no pasa nada"; desconocimiento de exposición legal; contratación de abogado solo para emergencias; cultura de informalidad.
**Observable_Symptoms:** Se consulta al abogado solo cuando hay demanda; contratos no revisados; decisiones sin análisis legal; multas que pudieron evitarse; litigios que se pudieron prevenir.
**Early_Warning_Signals:** Sin abogado de confianza; contratos sin revisión legal; litigios que se pudieron prevenir; multas recurrentes; decisiones comerciales sin input legal; % de temas con cobertura legal < 30%.
**Business_Impact:** Litigios evitables; multas; contratos desfavorables; decisiones sin análisis de riesgo; costos legales de emergencia mayores; exposición a riesgos no identificados.
**Severity_Level:** Medium
**Metrics_To_Check:** Cobertura legal (áreas cubiertas); % de contratos revisados; número de litigios evitables; gasto legal preventivo vs reactivo; horas de asesoría legal/mes.
**Diagnostic_Questions:** ¿Hay abogado de confianza? ¿Se revisan los contratos? ¿La asesoría legal es preventiva o solo reactiva? ¿Hay cobertura para todas las áreas? ¿Se consulta antes de decidir?
**Recommended_Actions:** Contratar asesoría legal permanente (interna o externa); establecer revisiones periódicas; capacitar al equipo en temas legales básicos; crear checklist de temas que requieren consulta legal.
**Related_Patterns:** RSK-027, RSK-031, RSK-032, RSK-036, RSK-039

## Riesgo Tributario

### RSK-039
**Pattern_Name:** Incumplimiento de Obligaciones Fiscales
**Category:** Riesgo Tributario
**Description:** La empresa no cumple con sus obligaciones tributarias sustanciales (declaración y pago de impuestos) en tiempo y forma, exponiéndose a multas, recargos y sanciones.
**Typical_Causes:** Falta de personal calificado; flujo de caja insuficiente; desconocimiento de calendario fiscal; desorganización administrativa; priorización de otros pagos sobre impuestos.
**Observable_Symptoms:** Declaraciones de impuestos presentadas tarde; multas por mora; pagos fraccionados o parciales; presión de contador por información; saldos a favor vs saldos en contra inexplicables.
**Early_Warning_Signals:** Multas tributarias recurrentes; % de declaraciones fuera de plazo > 20%; deuda tributaria acumulada; provisiones de impuestos incorrectas; diferencias en declaraciones.
**Business_Impact:** Multas y recargos; intereses moratorios; embargos de cuentas; cierre de establecimiento; imposibilidad de emitir facturas; responsabilidad penal de directivos.
**Severity_Level:** Critical
**Metrics_To_Check:** % de declaraciones en plazo; multas tributarias/ventas; deuda tributaria total; antigüedad de deuda tributaria; diferencias entre declaraciones estimadas y reales.
**Diagnostic_Questions:** ¿Se declaran y pagan los impuestos a tiempo? ¿Hay multas recurrentes? ¿La empresa debe impuestos? ¿El contador tiene la información a tiempo? ¿Hay provisiones adecuadas?
**Recommended_Actions:** Implementar calendario fiscal; asignar responsable de impuestos; provisionar impuestos mensualmente; automatizar declaraciones; priorizar pago de impuestos; contratar contador especializado.
**Related_Patterns:** RSK-001, RSK-012, RSK-040, RSK-041, RSK-042

### RSK-040
**Pattern_Name:** Planificación Tributaria Inexistente o Inadecuada
**Category:** Riesgo Tributario
**Description:** La empresa no realiza planificación tributaria, pagando más impuestos de los necesarios por desconocimiento de beneficios fiscales, o realizando planificación agresiva que expone a contingencias.
**Typical_Causes:** Falta de asesoría tributaria; cultura de "pagar lo que toca"; desconocimiento de incentivos; miedo a fiscalización; contador externo sin proactividad.
**Observable_Symptoms:** La empresa paga impuestos sin evaluar alternativas; no aprovecha deducciones disponibles; no conoce beneficios fiscales sectoriales; la tasa efectiva es mayor que la de competidores comparables.
**Early_Warning_Signals:** Tasa efectiva de impuesto > tasa nominal; % de gastos deducibles no aprovechados > 20%; sin revisión fiscal periódica; no se conoce el régimen fiscal óptimo; sin planificación anual.
**Business_Impact:** Mayor carga tributaria; menor rentabilidad; pérdida de competitividad; flujo de caja reducido; falta de previsión de contingencias fiscales.
**Severity_Level:** Medium
**Metrics_To_Check:** Tasa efectiva de impuesto; % de deducciones aprovechadas; ahorro fiscal por planificación; contingencias fiscales; cumplimiento de beneficios fiscales.
**Diagnostic_Questions:** ¿Hay planificación tributaria anual? ¿Se aprovechan todos los beneficios fiscales? ¿La tasa efectiva es razonable? ¿Hay revisión fiscal periódica? ¿Se comparan alternativas?
**Recommended_Actions:** Realizar planificación tributaria anual; contratar asesoría fiscal especializada; revisar régimen fiscal óptimo; aprovechar incentivos sectoriales; documentar posiciones fiscales.
**Related_Patterns:** RSK-012, RSK-039, RSK-041, RSK-042, RSK-044

### RSK-041
**Pattern_Name:** Contingencias por Fiscalización de Autoridades
**Category:** Riesgo Tributario
**Description:** La empresa está expuesta a fiscalizaciones de autoridades tributarias que pueden determinar diferencias a pagar, multas e intereses, afectando significativamente su flujo y resultados.
**Typical_Causes:** Incumplimientos formales; diferencias entre ingresos declarados y reales; gastos no deducibles deducidos; operaciones con partes relacionadas no justificadas; precios de transferencia no documentados.
**Observable_Symptoms:** Notificaciones de la autoridad tributaria; requerimientos de información; fiscalizaciones en curso; ajustes fiscales en ejercicios anteriores; diferencias no explicadas.
**Early_Warning_Signals:** Diferencias entre libros contables y declaraciones; notificaciones de la autoridad; % de contingencias fiscales/patrimonio > 10%; ejercicios anteriores con ajustes; fiscalizaciones recurrentes.
**Business_Impact:** Pago de impuestos omitidos; multas de hasta 100% del impuesto; intereses; costos de defensa; distracción gerencial; posible cierre; responsabilidad penal.
**Severity_Level:** High
**Metrics_To_Check:** Contingencias fiscales/patrimonio; número de fiscalizaciones; diferencias determinadas/multas; tiempo de resolución; provisiones para contingencias.
**Diagnostic_Questions:** ¿Hay fiscalizaciones en curso? ¿Hay diferencias entre contabilidad y declaraciones? ¿Las contingencias están provisionadas? ¿Se han pagado multas? ¿Hay asesoría tributaria?
**Recommended_Actions:** Mantener contabilidad al día y consistente con declaraciones; documentar posiciones fiscales; provisionar contingencias; responder requerimientos oportunamente; contratar asesoría especializada.
**Related_Patterns:** RSK-012, RSK-039, RSK-040, RSK-042, RSK-043

### RSK-042
**Pattern_Name:** Riesgo de Precios de Transferencia
**Category:** Riesgo Tributario
**Description:** La empresa realiza operaciones con partes relacionadas (nacionales o internacionales) sin documentar adecuadamente los precios de transferencia, exponiéndose a ajustes fiscales y multas.
**Typical_Causes:** Operaciones con empresas relacionadas; falta de asesoría en PT; ausencia de estudios de PT; contratos intragrupo sin sustancia económica; desconocimiento de normativa de PT.
**Observable_Symptoms:** Operaciones frecuentes con partes relacionadas; precios diferentes a los del mercado; no hay contratos intragrupo; no hay estudios de PT; márgenes inconsistentes.
**Early_Warning_Signals:** % de operaciones con partes relacionadas > 20%; sin estudio de PT actualizado; precios que difieren de mercado > 15%; pérdidas recurrentes en operaciones con relacionadas; sin documentación de PT.
**Business_Impact:** Ajustes fiscales; multas de hasta 100% del impuesto omitido; imposibilidad de deducir gastos; doble tributación; litigios fiscales; contingencias significativas.
**Severity_Level:** High
**Metrics_To_Check:** % de operaciones con partes relacionadas; % de precios dentro de rango de mercado; existencia de estudios de PT; contingencias por PT; cumplimiento de obligaciones formales de PT.
**Diagnostic_Questions:** ¿Hay operaciones con partes relacionadas? ¿Hay estudios de precios de transferencia? ¿Los precios son consistentes con mercado? ¿Hay documentación de PT? ¿Se cumplen obligaciones formales?
**Recommended_Actions:** Realizar estudios de precios de transferencia; documentar todas las operaciones con relacionadas; establecer contratos intragrupo; mantener precios de mercado; cumplir obligaciones formales.
**Related_Patterns:** RSK-039, RSK-040, RSK-041, RSK-043, RSK-044

### RSK-043
**Pattern_Name:** Riesgo de Beneficios Fiscales Perdidos
**Category:** Riesgo Tributario
**Description:** La empresa no aprovecha los beneficios fiscales, deducciones, exenciones o créditos fiscales a los que tiene derecho, pagando más impuestos de los legalmente requeridos.
**Typical_Causes:** Desconocimiento de beneficios disponibles; falta de asesoría fiscal; contabilidad que no captura información necesaria; falta de planificación; desorganización documental.
**Observable_Symptoms:** Beneficios fiscales no aplicados; deducciones no consideradas; créditos fiscales no utilizados; la empresa paga impuestos que podría evitar legalmente; competidores aprovechan beneficios que la empresa no.
**Early_Warning_Signals:** % de beneficios fiscales aplicados < 50%; tasa efectiva > tasa nominal; no hay revisión anual de beneficios disponibles; asesoría fiscal no proactiva; deducciones estándar sin optimizar.
**Business_Impact:** Mayor carga tributaria; menor rentabilidad; desventaja competitiva; flujo de caja reducido; menor capacidad de inversión.
**Severity_Level:** Medium
**Metrics_To_Check:** % de beneficios fiscales aplicados; ahorro fiscal potencial vs real; tasa efectiva de impuesto; % de deducciones optimizadas; cumplimiento de requisitos para beneficios.
**Diagnostic_Questions:** ¿Se aprovechan todos los beneficios fiscales disponibles? ¿La tasa efectiva es óptima? ¿Hay revisión anual de beneficios? ¿El asesor fiscal es proactivo? ¿Se cumplen requisitos para beneficios?
**Recommended_Actions:** Realizar revisión anual de beneficios fiscales aplicables; optimizar deducciones; mantener documentación de respaldo; contratar asesoría proactiva; capacitar al personal contable.
**Related_Patterns:** RSK-040, RSK-041, RSK-042, RSK-044, RSK-049

### RSK-044
**Pattern_Name:** Riesgo por Operaciones Informales
**Category:** Riesgo Tributario
**Description:** La empresa realiza operaciones sin facturación o documentación formal (ventas sin factura, compras informales, pagos en efectivo sin registro), exponiéndose a contingencias fiscales.
**Typical_Causes:** Competencia informal; presión de clientes para no facturar; cultura de efectivo; dificultad para emitir facturas; desconocimiento de riesgos; reducción de costos no documentados.
**Observable_Symptoms:** Ventas no facturadas; compras sin factura; diferencias entre ingresos reales y declarados; pagos en efectivo no registrados; ingresos en cuentas personales.
**Early_Warning_Signals:** % de ventas sin factura > 10%; % de compras sin factura > 15%; ingresos en cuentas personales; efectivo no depositado; diferencias significativas en declaraciones.
**Business_Impact:** Multas por omisión de ingresos; clausura; determinación presuntiva de ingresos; imposibilidad de deducir compras; riesgo penal (defraudación fiscal); pérdida de clientes formales.
**Severity_Level:** Critical
**Metrics_To_Check:** % de operaciones facturadas; % de compras con factura; diferencias entre ingresos reales y declarados; % de pagos en efectivo; contingencias estimadas por informalidad.
**Diagnostic_Questions:** ¿Se facturan todas las ventas? ¿Todas las compras tienen factura? ¿Hay operaciones en efectivo no registradas? ¿Los ingresos declarados coinciden con la realidad? ¿Hay presión de clientes para no facturar?
**Recommended_Actions:** Facturar todas las operaciones; formalizar compras; reducir uso de efectivo; implementar sistemas de facturación electrónica; capacitar al equipo; evaluar impacto de formalización plena.
**Related_Patterns:** RSK-011, RSK-028, RSK-039, RSK-041, RSK-045

### RSK-045
**Pattern_Name:** Riesgo de Pasivos Ocultos por Contingencias Fiscales
**Category:** Riesgo Tributario
**Description:** La empresa tiene contingencias fiscales no registradas ni provisionadas que pueden materializarse en el futuro, representando un pasivo oculto que afecta su situación financiera real.
**Typical_Causes:** Falta de revisión fiscal; posiciones fiscales agresivas; operaciones no formalizadas; desconocimiento de contingencias; ausencia de provisiones; no hay abogado fiscal.
**Observable_Symptoms:** No se conocen las contingencias fiscales; no hay provisiones para posibles ajustes; diferencias entre contabilidad y declaraciones; posiciones fiscales sin respaldo documental.
**Early_Warning_Signals:** Sin matriz de contingencias fiscales; posiciones fiscales agresivas sin documentar; sin provisiones para contingencias; ejercicios anteriores con diferencias; fiscalizaciones previas con ajustes.
**Business_Impact:** Pasivos no registrados que afectan el patrimonio; ajustes contables significativos; impacto en resultados de ejercicios futuros; problemas en venta de la empresa; afectación de garantías bancarias.
**Severity_Level:** High
**Metrics_To_Check:** Contingencias fiscales identificadas; provisiones para contingencias/patrimonio; % de contingencias provisionadas; antigüedad de las contingencias; posiciones fiscales agresivas.
**Diagnostic_Questions:** ¿Las contingencias fiscales están identificadas? ¿Están provisionadas? ¿Hay posiciones fiscales agresivas? ¿Se ha modelado el impacto de una fiscalización? ¿Hay asesoría fiscal?
**Recommended_Actions:** Identificar y documentar todas las contingencias fiscales; provisionar contingencias probables; revisar posiciones fiscales agresivas; realizar due diligence fiscal; mantener asesoría especializada.
**Related_Patterns:** RSK-039, RSK-040, RSK-041, RSK-042, RSK-044

### RSK-046
**Pattern_Name:** Riesgo de Omisión de Impuestos Indirectos
**Category:** Riesgo Tributario
**Description:** La empresa no gestiona adecuadamente impuestos indirectos (IVA, ISR retenciones, IEPS, impuestos locales) en sus operaciones, generando contingencias por omisión o error en su determinación.
**Typical_Causes:** Complejidad del régimen de impuestos indirectos; falta de capacitación; sistemas inadecuados; operaciones con tasas diferenciales; desconocimiento de exenciones y tasas aplicables.
**Observable_Symptoms:** Errores en determinación de IVA; retenciones no realizadas; diferencias en declaraciones de impuestos indirectos; proveedores sin CFDI; tasas incorrectas aplicadas.
**Early_Warning_Signals:** % de errores en declaraciones de IVA > 10%; retenciones no enteradas; diferencias en impuestos indirectos; multas por IVA; proveedores sin factura; tasas incorrectas.
**Business_Impact:** Multas y recargos; imposibilidad de acreditar IVA; devolución de impuestos rechazada; responsabilidad solidaria; clausura; contingencias significativas.
**Severity_Level:** High
**Metrics_To_Check:** % de errores en declaraciones de impuestos indirectos; % de retenciones enteradas a tiempo; % de proveedores con CFDI; multas por IVA/ventas; diferencias determinadas.
**Diagnostic_Questions:** ¿Se determinan correctamente los impuestos indirectos? ¿Se hacen las retenciones? ¿Los proveedores emiten CFDI? ¿Hay diferencias en declaraciones? ¿Hay capacitación en IVA?
**Recommended_Actions:** Capacitar al equipo en impuestos indirectos; implementar sistema que calcule automáticamente; revisar tasas aplicables; conciliar declaraciones mensualmente; automatizar retenciones.
**Related_Patterns:** RSK-039, RSK-040, RSK-041, RSK-044, RSK-049

### RSK-047
**Pattern_Name:** Riesgo por Dictamen Fiscal
**Category:** Riesgo Tributario
**Description:** La empresa está obligada a dictaminar sus estados financieros por parte de contador público registrado, pero no lo hace o lo hace deficientemente, generando riesgos fiscales y administrativos.
**Typical_Causes:** Desconocimiento de la obligación; ahorro en costos; falta de preparación; contabilidad desorganizada; ausencia de registros adecuados.
**Observable_Symptoms:** Empresa obligada a dictaminar no lo hace; dictámenes con salvedades; observaciones recurrentes; contabilidad no preparada para dictamen; plazos vencidos.
**Early_Warning_Signals:** Dictamen no presentado en plazo; obligación de dictaminar no identificada; observaciones recurrentes; contabilidad no auditada; diferencias significativas en dictamen.
**Business_Impact:** Multas por no dictaminar; presunción de ingresos no declarados; imposibilidad de acceder a ciertos beneficios; desconfianza de autoridades; contingencias fiscales.
**Severity_Level:** Medium
**Metrics_To_Check:** Cumplimiento de dictamen fiscal; % de observaciones recurrentes; plazo de presentación; diferencias determinadas; costos de dictamen.
**Diagnostic_Questions:** ¿La empresa está obligada a dictaminar? ¿Se presenta el dictamen en plazo? ¿Hay observaciones recurrentes? ¿El contador está preparado? ¿La contabilidad está lista?
**Recommended_Actions:** Determinar obligación de dictaminar; contratar contador público registrado; preparar contabilidad; atender observaciones; presentar en plazo; mantener registros ordenados.
**Related_Patterns:** RSK-012, RSK-039, RSK-040, RSK-041, RSK-049

### RSK-048
**Pattern_Name:** Riesgo de Multas y Recargos por Mora Fiscal
**Category:** Riesgo Tributario
**Description:** La empresa acumula multas y recargos por pago extemporáneo de impuestos, aumentando su carga tributaria y generando un pasivo creciente que afecta su flujo de caja.
**Typical_Causes:** Falta de flujo de caja; desorganización administrativa; desconocimiento de plazos; priorización de otros pagos; ausencia de calendario fiscal.
**Observable_Symptoms:** Multas recurrentes por mora; recargos que se acumulan; impuestos se pagan con retraso; la empresa no conoce el monto de multas acumuladas; proveedores presionan mientras impuestos esperan.
**Early_Warning_Signals:** Multas y recargos/ventas > 1%; % de impuestos pagados en plazo < 70%; deuda por multas creciente; pagos fraccionados; notificaciones de cobranza coactiva.
**Business_Impact:** Mayor carga tributaria; embargos; costos financieros por multas; recargos que incrementan deuda; imposibilidad de acceder a financiamiento; cierre de operaciones.
**Severity_Level:** High
**Metrics_To_Check:** Multas y recargos/ventas; % de impuestos pagados en plazo; deuda por multas; antigüedad de deuda tributaria; tendencia de mora.
**Diagnostic_Questions:** ¿Se pagan los impuestos a tiempo? ¿Hay multas acumuladas? ¿Los recargos son significativos? ¿Hay deuda tributaria? ¿Se ha considerado un plan de pagos?
**Recommended_Actions:** Priorizar pago de impuestos; implementar calendario fiscal; automatizar pagos; provisionar impuestos mensualmente; negociar planes de pago; reducir gastos para liberar flujo.
**Related_Patterns:** RSK-001, RSK-039, RSK-040, RSK-041, RSK-045

### RSK-049
**Pattern_Name:** Riesgo por Deficiencias en Facturación Electrónica
**Category:** Riesgo Tributario
**Description:** La empresa presenta deficiencias en la emisión, recepción o cancelación de comprobantes fiscales digitales (CFDI), generando riesgos de deducibilidad, acreditamiento y contingencias.
**Typical_Causes:** Sistemas de facturación inadecuados; falta de capacitación; procesos manuales; desconocimiento de requisitos fiscales; actualizaciones no implementadas.
**Observable_Symptoms:** Facturas con errores; cancelaciones incorrectas; complementos de pago no emitidos; facturas rechazadas por clientes; proveedores sin CFDI; inconsistencias en el sistema.
**Early_Warning_Signals:** % de facturas con errores > 5%; cancelaciones sin control; CFDI de nómina incorrectos; complementos de pago no emitidos; multas por incumplimiento de facturación.
**Business_Impact:** Imposibilidad de deducir gastos; IVA no acreditable; multas; rechazo de facturas por clientes; contingencias fiscales; problemas con proveedores.
**Severity_Level:** Medium
**Metrics_To_Check:** % de CFDI con errores; % de cancelaciones injustificadas; % de complementos de pago emitidos; multas por facturación/ventas; % de proveedores con CFDI válido.
**Diagnostic_Questions:** ¿El sistema de facturación es adecuado? ¿Hay errores frecuentes en CFDI? ¿Se emiten complementos de pago? ¿Los proveedores emiten CFDI? ¿Hay capacitación en facturación?
**Recommended_Actions:** Implementar sistema de facturación automatizado; capacitar al equipo; estandarizar procesos; conciliar facturación con contabilidad; mantener software actualizado; auditar CFDI periódicamente.
**Related_Patterns:** RSK-012, RSK-039, RSK-040, RSK-044, RSK-046

## Riesgo Tecnológico

### RSK-050
**Pattern_Name:** Vulnerabilidad de Ciberseguridad
**Category:** Riesgo Tecnológico
**Description:** La empresa carece de medidas adecuadas de ciberseguridad, exponiendo sus sistemas, datos y operaciones a ataques cibernéticos, ransomware, phishing y filtraciones de información.
**Typical_Causes:** Falta de inversión en seguridad; desconocimiento de riesgos; ausencia de políticas; software desactualizado; empleados no capacitados; ausencia de firewalls y antivirus.
**Observable_Symptoms:** Infecciones de malware recurrentes; correos de phishing llegan a empleados; sistemas lentos o comprometidos; accesos no autorizados; pérdida de datos; ataques de ransomware.
**Early_Warning_Signals:** Sin firewall corporativo; sin antivirus actualizado; sin políticas de seguridad; sin autenticación multifactor; empleados no capacitados; parches de seguridad no aplicados; sin backups.
**Business_Impact:** Pérdida de datos críticos; interrupción de operaciones; pago de rescates; fuga de información confidencial; daño reputacional; costos de recuperación; multas regulatorias.
**Severity_Level:** Critical
**Metrics_To_Check:** % de sistemas con antivirus actualizado; frecuencia de incidentes de seguridad; tiempo de detección de intrusiones; % de empleados capacitados; RPO y RTO.
**Diagnostic_Questions:** ¿Hay firewall y antivirus? ¿Los sistemas están actualizados? ¿Hay política de contraseñas? ¿Los empleados están capacitados en ciberseguridad? ¿Hay autenticación multifactor?
**Recommended_Actions:** Implementar firewall y antivirus corporativo; establecer política de seguridad; capacitar al personal; implementar autenticación multifactor; mantener sistemas actualizados; hacer backups offsite; contratar seguro cibernético.
**Related_Patterns:** RSK-015, RSK-051, RSK-052, RSK-058, RSK-060

### RSK-051
**Pattern_Name:** Pérdida de Datos Críticos
**Category:** Riesgo Tecnológico
**Description:** La empresa no cuenta con un sistema adecuado de respaldo y recuperación de datos, exponiéndose a la pérdida permanente de información crítica del negocio.
**Typical_Causes:** Falta de política de backups; backups no probados; almacenamiento en mismo sitio; ausencia de redundancia; desconocimiento de la importancia de los datos.
**Observable_Symptoms:** No se hacen backups regulares; los backups existen pero no se prueban; cuando se necesita recuperar, los datos no están; información perdida irreversiblemente.
**Early_Warning_Signals:** Sin política de backups; backups sin probar; frecuencia de backups > 7 días; backups en mismo sitio; RPO no definido; RTO no definido; sin almacenamiento externo/nube.
**Business_Impact:** Pérdida permanente de datos financieros, clientes, proveedores; interrupción prolongada de operaciones; imposibilidad de facturar; pérdida de información histórica; costos de reconstrucción.
**Severity_Level:** Critical
**Metrics_To_Check:** RPO (Recovery Point Objective); RTO (Recovery Time Objective); frecuencia de backups; % de backups probados exitosamente; % de datos críticos respaldados.
**Diagnostic_Questions:** ¿Se hacen backups regularmente? ¿Los backups se prueban? ¿Los datos críticos están respaldados fuera del sitio? ¿Se ha definido RPO y RTO? ¿Se puede recuperar de un desastre?
**Recommended_Actions:** Implementar política de backups 3-2-1 (3 copias, 2 medios, 1 offsite); probar restauración periódicamente; almacenar en nube y local; definir RPO/RTO; automatizar backups.
**Related_Patterns:** RSK-015, RSK-050, RSK-052, RSK-058, RSK-060

### RSK-052
**Pattern_Name:** Dependencia de Sistemas Críticos sin Redundancia
**Category:** Riesgo Tecnológico
**Description:** La empresa depende de sistemas de TI críticos (servidores, ERP, conectividad) que no tienen redundancia, generando interrupción total si fallan.
**Typical_Causes:** Falta de inversión en infraestructura; cultura de "si funciona no lo toques"; desconocimiento de riesgos; presupuesto de TI insuficiente; ausencia de arquitectura de alta disponibilidad.
**Observable_Symptoms:** Cuando el servidor falla, todo se detiene; no hay internet, no se puede trabajar; caídas del sistema detienen facturación; no hay plan alternativo; restauración toma días.
**Early_Warning_Signals:** Servidor único sin respaldo; sin conexión a internet redundante; sistemas sin alta disponibilidad; sin generador eléctrico/UPS; caídas recurrentes.
**Business_Impact:** Interrupción total de operaciones; pérdida de ventas; clientes insatisfechos; imposibilidad de facturar; pérdida de datos; costos de recuperación de emergencia.
**Severity_Level:** High
**Metrics_To_Check:** Disponibilidad de sistemas (uptime); MTBF de infraestructura; MTTR; % de sistemas con redundancia; tiempo de caída/mes.
**Diagnostic_Questions:** ¿Hay servidor de respaldo? ¿Hay conexión a internet redundante? ¿Qué pasa si el servidor principal falla? ¿Hay generador eléctrico? ¿Cuánto tiempo toma restaurar?
**Recommended_Actions:** Implementar redundancia de servidores; tener conexión a internet secundaria; usar servicios cloud para alta disponibilidad; instalar UPS/generador; documentar plan de recuperación.
**Related_Patterns:** RSK-015, RSK-050, RSK-051, RSK-053, RSK-060

### RSK-053
**Pattern_Name:** Obsolescencia de Software y Sistemas
**Category:** Riesgo Tecnológico
**Description:** La empresa utiliza software obsoleto, sin soporte ni actualizaciones, que limita su funcionalidad, seguridad y compatibilidad, aumentando riesgos operativos y de seguridad.
**Typical_Causes:** Falta de inversión en TI; resistencia al cambio; sistemas a medida sin mantenimiento; desconocimiento de nuevas versiones; costo percibido de actualización.
**Observable_Symptoms:** Software sin actualizaciones disponibles; sistemas que no se integran con otros; limitaciones funcionales; caídas frecuentes; falta de soporte del fabricante; inseguridad.
**Early_Warning_Signals:** Versiones de software sin soporte del fabricante; antigüedad del sistema > 5 años; sin actualizaciones en > 2 años; vulnerabilidades conocidas no parcheadas; incompatibilidad con formatos actuales.
**Business_Impact:** Vulnerabilidades de seguridad; pérdida de productividad; imposibilidad de integrarse con clientes/proveedores; costos altos de mantenimiento; pérdida de competitividad; migración forzosa costosa.
**Severity_Level:** High
**Metrics_To_Check:** Antigüedad de sistemas; % de software con soporte activo; % de sistemas actualizados; número de vulnerabilidades conocidas; costo de mantenimiento vs actualización.
**Diagnostic_Questions:** ¿El software está actualizado? ¿Tiene soporte del fabricante? ¿Hay versiones más nuevas? ¿Hay vulnerabilidades conocidas? ¿Los sistemas se integran bien?
**Recommended_Actions:** Evaluar estado de todos los sistemas; planificar actualizaciones; migrar a software moderno; considerar SaaS/cloud; presupuestar renovación tecnológica anual; eliminar sistemas obsoletos.
**Related_Patterns:** RSK-016, RSK-050, RSK-052, RSK-055, RSK-061

### RSK-054
**Pattern_Name:** Falta de Políticas de Acceso y Seguridad de la Información
**Category:** Riesgo Tecnológico
**Description:** La empresa no cuenta con políticas de acceso a sistemas y datos, permitiendo que personal no autorizado acceda a información sensible o realice cambios no autorizados.
**Typical_Causes:** Cultura de confianza; falta de personal de TI; crecimiento sin controles; desconocimiento de riesgos; resistencia a controles por comodidad.
**Observable_Symptoms:** Todos tienen acceso a todo; contraseñas compartidas; usuarios genéricos; personal que ya no trabaja en la empresa aún tiene acceso; información sensible disponible para todos.
**Early_Warning_Signals:** Sin política de accesos; usuarios compartidos; sin roles y permisos definidos; sin registro de accesos; ex empleados con acceso vigente; sin política de contraseñas.
**Business_Impact:** Fuga de información; modificaciones no autorizadas; fraudes; pérdida de datos; incumplimiento regulatorio; imposibilidad de auditar accesos; daño reputacional.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados con acceso a información sensible; número de usuarios compartidos; % de ex empleados con acceso; cumplimiento de política de contraseñas; incidentes de acceso no autorizado.
**Diagnostic_Questions:** ¿Hay política de accesos? ¿Los accesos están basados en roles? ¿Hay contraseñas compartidas? ¿Ex empleados aún tienen acceso? ¿Se auditan los accesos?
**Recommended_Actions:** Implementar política de accesos basada en roles; establecer control de acceso; usar autenticación individual; revisar accesos periódicamente; desactivar accesos de ex empleados; implementar logging.
**Related_Patterns:** RSK-050, RSK-051, RSK-056, RSK-058, RSK-059

### RSK-055
**Pattern_Name:** Falta de Integración entre Sistemas
**Category:** Riesgo Tecnológico
**Description:** Los sistemas de la empresa no están integrados, operando en silos que obligan a ingresar información múltiples veces, generando errores, retrabajo y pérdida de eficiencia.
**Typical_Causes:** Sistemas adquiridos en diferentes épocas sin planificación; falta de presupuesto para integración; resistencia al cambio; desconocimiento de soluciones de integración.
**Observable_Symptoms:** La misma información se ingresa en múltiples sistemas; datos inconsistentes entre sistemas; reportes requieren consolidación manual; interfaces manuales; errores por transcripción.
**Early_Warning_Signals:** Número de sistemas no integrados > 3; tiempo dedicado a ingresar datos en múltiples sistemas; % de datos que se ingresan más de una vez; errores de transcripción; reportes manuales.
**Business_Impact:** Ineficiencia operativa; errores de datos; retrabajo; falta de información en tiempo real; mala toma de decisiones; costos operativos altos; insatisfacción del equipo.
**Severity_Level:** High
**Metrics_To_Check:** Número de sistemas no integrados; % de datos ingresados múltiples veces; tiempo de consolidación de reportes; errores de integración; costo de interfaces manuales.
**Diagnostic_Questions:** ¿Los sistemas están integrados? ¿Se ingresa la misma información en varios sistemas? ¿Hay datos inconsistentes entre sistemas? ¿Los reportes requieren consolidación manual? ¿Hay interfaces automáticas?
**Recommended_Actions:** Implementar ERP integrado; desarrollar interfaces entre sistemas; usar middleware; eliminar sistemas redundantes; estandarizar datos; automatizar flujos de información.
**Related_Patterns:** RSK-053, RSK-056, RSK-057, RSK-061, RSK-062

### RSK-056
**Pattern_Name:** Falta de Backup y Disaster Recovery Plan
**Category:** Riesgo Tecnológico
**Description:** La empresa no tiene un plan de recuperación ante desastres (DRP) documentado y probado que permita restaurar operaciones de TI en un tiempo aceptable después de un incidente mayor.
**Typical_Causes:** Subestimación de riesgos; falta de recursos; desconocimiento; "nunca ha pasado"; ausencia de personal de TI.
**Observable_Symptoms:** No hay DRP documentado; no se sabe qué hacer si el data center se pierde; los backups existen pero no se han probado; no hay RPO/RTO definidos; no hay sitio alternativo.
**Early_Warning_Signals:** Sin DRP documentado; RPO/RTO no definidos; backups no probados; sin sitio alternativo; sin procedimientos de recuperación documentados; sin asignación de roles de recuperación.
**Business_Impact:** Tiempo de recuperación prolongado; pérdida de datos; interrupción extensa de operaciones; pérdida de clientes; costos de recuperación de emergencia; posible quiebra.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de DRP; RPO/RTO definidos; frecuencia de pruebas de DRP; % de sistemas cubiertos por DRP; tiempo de recuperación en pruebas.
**Diagnostic_Questions:** ¿Hay DRP documentado? ¿Se ha probado? ¿RPO y RTO están definidos? ¿Hay sitio alternativo? ¿El equipo sabe qué hacer en caso de desastre?
**Recommended_Actions:** Desarrollar DRP completo; definir RPO/RTO; probar DRP semestralmente; mantener sitio alternativo; documentar procedimientos; capacitar al equipo; mejorar basado en pruebas.
**Related_Patterns:** RSK-015, RSK-050, RSK-051, RSK-052, RSK-060

### RSK-057
**Pattern_Name:** Capacidad de TI Insuficiente
**Category:** Riesgo Tecnológico
**Description:** La infraestructura de TI (servidores, almacenamiento, red, ancho de banda) es insuficiente para soportar las operaciones actuales o el crecimiento proyectado, generando lentitud, caídas y limitaciones.
**Typical_Causes:** Falta de inversión en TI; crecimiento no anticipado; planificación de capacidad deficiente; adquisición de sistemas sin considerar infraestructura.
**Observable_Symptoms:** Sistemas lentos en horas pico; almacenamiento casi lleno; ancho de banda insuficiente; quejas de usuarios por rendimiento; caídas por sobrecarga; imposibilidad de crecer.
**Early_Warning_Signals:** Utilización de servidores > 80%; almacenamiento > 85%; ancho de banda casi saturado; tiempo de respuesta de sistemas > 3 segundos; quejas recurrentes de rendimiento.
**Business_Impact:** Baja productividad; frustración del equipo; imposibilidad de implementar nuevos sistemas; pérdida de ventas por sistemas lentos; costos de upgrade de emergencia.
**Severity_Level:** High
**Metrics_To_Check:** % de utilización de servidores; % de almacenamiento utilizado; ancho de banda utilizado/disponible; tiempo de respuesta de sistemas; número de incidentes por capacidad.
**Diagnostic_Questions:** ¿Los sistemas son rápidos? ¿Hay problemas de capacidad? ¿El almacenamiento está cerca del límite? ¿El ancho de banda es suficiente? ¿Se ha planificado la capacidad futura?
**Recommended_Actions:** Evaluar capacidad actual y proyectada; migrar a cloud para escalabilidad; invertir en infraestructura; implementar monitoreo de capacidad; planificar upgrades con anticipación.
**Related_Patterns:** RSK-052, RSK-053, RSK-055, RSK-060, RSK-061

### RSK-058
**Pattern_Name:** Exposición a Fraude Informático
**Category:** Riesgo Tecnológico
**Description:** La empresa está expuesta a fraudes informáticos como phishing, ingeniería social, suplantación de identidad o transferencias no autorizadas debido a controles tecnológicos deficientes.
**Typical_Causes:** Falta de autenticación multifactor; empleados no capacitados; procesos de pagos sin verificación; sistemas sin registro de auditoría; accesos sin control.
**Observable_Symptoms:** Correos de phishing llegan a empleados; intentos de suplantación; transferencias no autorizadas; accesos sospechosos; empleados reciben correos fraudulentos.
**Early_Warning_Signals:** Sin MFA; sin capacitación en phishing; procesos de pago sin doble verificación; sin logging de transacciones; incidentes de seguridad recurrentes; empleados caen en phishing.
**Business_Impact:** Pérdidas financieras por fraudes; fuga de información confidencial; daño reputacional; costos de investigación; tiempo de recuperación; responsabilidad legal.
**Severity_Level:** Critical
**Metrics_To_Check:** Número de incidentes de fraude; % de empleados capacitados; % de transacciones con doble verificación; tiempo de detección de fraudes; pérdidas por fraude/ventas.
**Diagnostic_Questions:** ¿Hay MFA implementado? ¿Los empleados están capacitados en ciberseguridad? ¿Los pagos requieren doble verificación? ¿Hay registro de auditoría? ¿Se han detectado fraudes?
**Recommended_Actions:** Implementar MFA en todos los sistemas críticos; capacitar al personal en seguridad; establecer doble verificación para pagos; implementar logging y monitoreo; simular phishing.
**Related_Patterns:** RSK-011, RSK-050, RSK-054, RSK-059, RSK-060

### RSK-059
**Pattern_Name:** Uso de Software No Licenciado o Pirata
**Category:** Riesgo Tecnológico
**Description:** La empresa utiliza software sin licencia o pirata, exponiéndose a riesgos legales, de seguridad y operativos, incluyendo multas, malware y falta de soporte.
**Typical_Causes:** Ahorro de costos; desconocimiento de licencias; falta de política de software; presión por reducir gastos; cultura de "todo gratis en internet".
**Observable_Symptoms:** Software instalado sin licencia; licencias vencidas; auditorías de software encuentran irregularidades; empleados instalan software sin autorización; falta de soporte técnico.
**Early_Warning_Signals:** % de software sin licencia > 10%; licencias no gestionadas; sin inventario de software; empleados con permisos de instalación; avisos de auditoría de proveedores.
**Business_Impact:** Multas por infracción de derechos de autor; malware y vulnerabilidades; sin soporte ni actualizaciones; responsabilidad penal; daño reputacional; costos de regularización.
**Severity_Level:** High
**Metrics_To_Check:** % de software licenciado; % de licencias vigentes; inventario de software actualizado; incidentes de seguridad por software pirata; multas/penalidades.
**Diagnostic_Questions:** ¿Todo el software tiene licencia? ¿Hay inventario de software? ¿Las licencias están vigentes? ¿Los empleados instalan software sin autorización? ¿Se audita el software?
**Recommended_Actions:** Realizar inventario de software; regularizar licencias; establecer política de software; bloquear instalaciones no autorizadas; presupuestar licencias anualmente; usar software open source donde posible.
**Related_Patterns:** RSK-030, RSK-050, RSK-053, RSK-054, RSK-060

### RSK-060
**Pattern_Name:** Falta de Gobierno de TI
**Category:** Riesgo Tecnológico
**Description:** La empresa carece de estructuras de gobierno de TI (políticas, comités, roles, procesos) que aseguren que la tecnología esté alineada con el negocio y los riesgos sean gestionados.
**Typical_Causes:** Desconocimiento de gobierno de TI; empresa pequeña cree que no lo necesita; falta de personal de TI calificado; tecnología vista como gasto no como inversión.
**Observable_Symptoms:** Decisiones de TI se toman sin criterio; no hay plan estratégico de TI; proyectos de TI sin priorización; incidentes recurrentes; sin presupuesto de TI; tecnología no alineada con negocio.
**Early_Warning_Signals:** Sin plan estratégico de TI; sin comité de TI; sin políticas de TI; sin presupuesto de TI formal; proyectos sin priorización; quejas recurrentes de TI.
**Business_Impact:** Inversiones en TI no alineadas; proyectos fallidos; riesgos no gestionados; ineficiencias; falta de control; imposibilidad de aprovechar tecnología para ventaja competitiva.
**Severity_Level:** Medium
**Metrics_To_Check:** Existencia de plan estratégico de TI; % de proyectos de TI exitosos; presupuesto de TI/ventas; cumplimiento de políticas de TI; nivel de satisfacción de usuarios de TI.
**Diagnostic_Questions:** ¿Hay plan estratégico de TI? ¿Hay políticas de TI? ¿Hay presupuesto de TI? ¿Las decisiones de TI son informadas? ¿La tecnología está alineada con el negocio?
**Recommended_Actions:** Establecer gobierno de TI; crear comité de TI; desarrollar plan estratégico de TI; definir políticas; asignar presupuesto; medir desempeño de TI; implementar mejores prácticas (ITIL, COBIT).
**Related_Patterns:** RSK-050, RSK-052, RSK-055, RSK-056, RSK-061

### RSK-061
**Pattern_Name:** Falta de Talento y Capacitación en TI
**Category:** Riesgo Tecnológico
**Description:** La empresa no cuenta con personal de TI calificado o el existente no tiene las habilidades necesarias para gestionar la tecnología actual, generando riesgos operativos y de seguridad.
**Typical_Causes:** Salarios no competitivos; dificultad para atraer talento TI; falta de inversión en capacitación; tecnología cambia rápido; subestimación de la complejidad TI.
**Observable_Symptoms:** Personal de TI desbordado; incidentes no resueltos; proyectos retrasados; tecnología mal administrada; falta de habilidades para sistemas actuales; dependencia de consultores externos.
**Early_Warning_Signals:** Personal de TI sin certificaciones; rotación en TI > 20%; tiempo de resolución de incidentes alto; % de tickets sin resolver; proyectos de TI retrasados; brecha de habilidades.
**Business_Impact:** Sistemas mal administrados; vulnerabilidades de seguridad; proyectos fallidos; dependencia de externos; costos altos de soporte; imposibilidad de innovar.
**Severity_Level:** High
**Metrics_To_Check:** % de personal de TI certificado; rotación en TI; tiempo de resolución de incidentes; % de proyectos a tiempo; brecha de habilidades; satisfacción de usuarios.
**Diagnostic_Questions:** ¿El personal de TI está calificado? ¿Hay brecha de habilidades? ¿Los incidentes se resuelven rápido? ¿Hay plan de capacitación? ¿Se retiene al talento TI?
**Recommended_Actions:** Invertir en capacitación TI; certificar al personal; mejorar compensaciones; crear plan de carrera; considerar outsourcing para habilidades especializadas; presupuestar capacitación anual.
**Related_Patterns:** RSK-050, RSK-053, RSK-055, RSK-057, RSK-060

### RSK-062
**Pattern_Name:** Dependencia de un Solo Proveedor de Tecnología
**Category:** Riesgo Tecnológico
**Description:** La empresa depende críticamente de un único proveedor de tecnología (ERP, nube, soporte, hardware), sin alternativas viables, generando riesgo de interrupción, aumentos de precio o quiebra del proveedor.
**Typical_Causes:** Contrato de largo plazo; sistemas propietarios; integración profunda; falta de planificación; decisión por precio sin considerar dependencia.
**Observable_Symptoms:** El proveedor aumenta precios y la empresa no puede cambiarse; caídas del proveedor afectan toda la operación; migrar sería muy costoso; el proveedor no tiene competencia directa.
**Early_Warning_Signals:** % de infraestructura en un solo proveedor cloud > 80%; ERP propietario sin alternativas; contrato de largo plazo sin cláusulas de salida; costos de migración prohibitivos; proveedor con problemas financieros.
**Business_Impact:** Aumentos de precio no negociables; interrupción si el proveedor falla; imposibilidad de cambiar; pérdida de datos si el proveedor quiebra; dependencia estratégica.
**Severity_Level:** High
**Metrics_To_Check:** % de dependencia del principal proveedor de TI; % de sistemas con alternativas viables; costo de migración; tiempo de migración; criticidad del proveedor.
**Diagnostic_Questions:** ¿Hay dependencia de un solo proveedor de TI? ¿Hay alternativas viables? ¿Cuánto costaría migrar? ¿El proveedor tiene problemas financieros? ¿Hay plan para reducir dependencia?
**Recommended_Actions:** Diversificar proveedores de TI; usar estándares abiertos; mantener opciones de respaldo; negociar cláusulas de salida; evaluar alternativas periódicamente; evitar锁定 tecnológico.
**Related_Patterns:** RSK-052, RSK-053, RSK-055, RSK-057, RSK-060


## Riesgo Reputacional

### RSK-063
**Pattern_Name:** Gestión Inadecuada de Redes Sociales y Opinión Pública
**Category:** Riesgo Reputacional
**Description:** La empresa no gestiona adecuadamente su presencia en redes sociales ni la percepción pública, exponiéndose a crisis reputacionales por comentarios negativos, reseñas o viralización de incidentes.
**Typical_Causes:** Falta de política de redes sociales; ausencia de community manager; no monitoreo de menciones; respuesta tardía a críticas; empleados sin lineamientos.
**Observable_Symptoms:** Reseñas negativas sin respuesta; crisis virales no gestionadas; comentarios negativos se acumulan; la empresa no sabe lo que se dice de ella; empleados publican sin criterio.
**Early_Warning_Signals:** Sin monitoreo de redes; reseñas negativas sin atender; % de reseñas negativas > 30%; tiempo de respuesta a quejas > 48 horas; sin política de redes sociales.
**Business_Impact:** Daño reputacional; pérdida de clientes; dificultad para atraer talento; impacto en ventas; desconfianza de stakeholders; crisis virales difíciles de controlar.
**Severity_Level:** High
**Metrics_To_Check:** % de reseñas negativas; tiempo de respuesta a quejas; Net Promoter Score (NPS); sentimiento en redes; número de crisis reputacionales.
**Diagnostic_Questions:** ¿Se monitorean las redes sociales? ¿Se responden las reseñas? ¿Hay política de redes? ¿Los empleados tienen lineamientos? ¿Se gestionan las crisis?
**Recommended_Actions:** Implementar monitoreo de redes; designar community manager; establecer política de redes sociales; capacitar empleados; crear plan de gestión de crisis; responder rápidamente a reseñas negativas.
**Related_Patterns:** RSK-064, RSK-065, RSK-066, RSK-069, RSK-074

### RSK-064
**Pattern_Name:** Falta de Gestión de Crisis Reputacional
**Category:** Riesgo Reputacional
**Description:** La empresa no tiene un plan de gestión de crisis reputacional para responder adecuadamente a incidentes que pueden dañar su imagen, empeorando el impacto de la crisis.
**Typical_Causes:** Desconocimiento de riesgos reputacionales; falta de recursos; confianza en que "nunca pasará"; no priorización; ausencia de función de comunicación.
**Observable_Symptoms:** Cuando hay una crisis, la empresa no sabe cómo responder; las declaraciones son contradictorias; no hay vocero designado; la crisis escala por mala gestión; la empresa queda a la defensiva.
**Early_Warning_Signals:** Sin plan de crisis; sin vocero designado; sin equipo de crisis; sin protocolo de comunicación; sin monitoreo de medios y redes.
**Business_Impact:** Daño reputacional prolongado; pérdida de clientes; caída de ventas; dificultad para atraer talento; desconfianza de inversores; costos de recuperación altos.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de plan de crisis; tiempo de respuesta inicial; % de crisis gestionadas exitosamente; impacto en ventas post-crisis; tiempo de recuperación reputacional.
**Diagnostic_Questions:** ¿Hay plan de crisis reputacional? ¿Hay vocero designado? ¿El equipo sabe cómo actuar en una crisis? ¿Se ha capacitado? ¿Se han enfrentado crisis antes?
**Recommended_Actions:** Desarrollar plan de gestión de crisis; designar vocero y equipo de crisis; capacitar al equipo; crear protocolos de comunicación; realizar simulacros; monitorear medios y redes.
**Related_Patterns:** RSK-063, RSK-065, RSK-066, RSK-069, RSK-074

### RSK-065
**Pattern_Name:** Insatisfacción Sistémica de Clientes
**Category:** Riesgo Reputacional
**Description:** La empresa tiene niveles crónicos de insatisfacción de clientes que, aunque no siempre se manifiestan en quejas formales, se difunden por boca a boca y redes sociales, dañando la reputación.
**Typical_Causes:** Problemas de calidad; servicio al cliente deficiente; incumplimiento de promesas; falta de medición de satisfacción; cultura no orientada al cliente.
**Observable_Symptoms:** Clientes se quejan informalmente; el boca a boca es negativo; reseñas en línea negativas; NPS bajo; clientes se van sin quejarse; la reputación es peor que la realidad.
**Early_Warning_Signals:** NPS < 20; % de reseñas negativas > 40%; tasa de retención de clientes decreciente; quejas informales recurrentes; CSAT < 70%.
**Business_Impact:** Pérdida de clientes; dificultad para atraer nuevos clientes; menor poder de fijación de precios; desventaja competitiva; costo de adquisición de clientes más alto.
**Severity_Level:** Critical
**Metrics_To_Check:** NPS; CSAT; % de reseñas negativas; tasa de retención; tasa de churn; número de quejas formales.
**Diagnostic_Questions:** ¿Se mide la satisfacción del cliente? ¿Cuál es el NPS? ¿Hay quejas recurrentes? ¿Los clientes recomiendan la empresa? ¿Se investiga por qué se van los clientes?
**Recommended_Actions:** Implementar medición de satisfacción (NPS, CSAT); investigar causas de insatisfacción; mejorar calidad; capacitar en servicio al cliente; crear programa de fidelización; actuar sobre feedback.
**Related_Patterns:** RSK-063, RSK-066, RSK-068, RSK-069, RSK-093

### RSK-066
**Pattern_Name:** Crisis por Producto o Servicio Defectuoso
**Category:** Riesgo Reputacional
**Description:** El lanzamiento o producción de un producto/servicio con defectos significativos genera una crisis reputacional que afecta la confianza de clientes y la marca.
**Typical_Causes:** Controles de calidad insuficientes; pruebas inadecuadas; presión por lanzar rápido; diseño deficiente; proveedores no controlados.
**Observable_Symptoms:** Devoluciones masivas; quejas de clientes; cobertura mediática negativa; recall de productos; clientes afectados; pérdida de confianza.
**Early_Warning_Signals:** Tasa de defectos en aumento; quejas de calidad recurrentes; devoluciones crecientes; pruebas de producto insuficientes; problemas reportados en beta.
**Business_Impact:** Costos de recall; pérdida de ventas; daño reputacional; demandas; pérdida de confianza del mercado; impacto en precio de acciones (si cotiza).
**Severity_Level:** Critical
**Metrics_To_Check:** Tasa de defectos; % de devoluciones; número de quejas de calidad; costo de recall/ventas; impacto en ventas post-crisis.
**Diagnostic_Questions:** ¿Hay controles de calidad? ¿Los productos se prueban antes de lanzar? ¿Hay devoluciones masivas? ¿Hay quejas de calidad? ¿Se gestionan los recalls?
**Recommended_Actions:** Fortalecer control de calidad; realizar pruebas exhaustivas antes de lanzar; establecer protocolo de recall; comunicar transparentemente; compensar clientes afectados; investigar causa raíz.
**Related_Patterns:** RSK-065, RSK-067, RSK-068, RSK-069, RSK-074

### RSK-067
**Pattern_Name:** Prácticas de Negocio Poco Éticas
**Category:** Riesgo Reputacional
**Description:** La empresa incurre en prácticas de negocio percibidas como poco éticas (publicidad engañosa, condiciones abusivas, explotación laboral), dañando su reputación y relaciones con stakeholders.
**Typical_Causes:** Presión por resultados; cultura organizacional permisiva; falta de código de ética; desconocimiento; competencia agresiva.
**Observable_Symptoms:** Clientes se sienten engañados; empleados denuncian malas prácticas; cobertura mediática negativa; ONGs critican a la empresa; proveedores se quejan de prácticas abusivas.
**Early_Warning_Signals:** Sin código de ética; publicidad cuestionable; condiciones laborales precarias; quejas de proveedores por prácticas abusivas; denuncias internas; críticas de la comunidad.
**Business_Impact:** Daño reputacional severo; pérdida de clientes; boicots; dificultad para contratar talento; multas regulatorias; desconfianza generalizada.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de código de ética; % de empleados capacitados; número de denuncias éticas; cobertura mediática negativa; % de clientes que confían en la empresa.
**Diagnostic_Questions:** ¿Hay código de ética? ¿Se capacita al personal? ¿Hay denuncias de prácticas cuestionables? ¿La empresa es percibida como ética? ¿Hay presión por resultados que lleva a malas prácticas?
**Recommended_Actions:** Implementar código de ética; capacitar al personal; establecer canal de denuncias; auditar prácticas; ser transparente; adoptar estándares de RSE; obtener certificaciones éticas.
**Related_Patterns:** RSK-033, RSK-065, RSK-066, RSK-069, RSK-074

### RSK-068
**Pattern_Name:** Impacto Ambiental o Social Negativo
**Category:** Riesgo Reputacional
**Description:** Las operaciones de la empresa generan impacto ambiental o social negativo percibido por la comunidad, activistas o reguladores, afectando su reputación y licencia social para operar.
**Typical_Causes:** Procesos contaminantes; falta de gestión ambiental; desinterés por la comunidad; ausencia de RSE; desconocimiento del impacto social.
**Observable_Symptoms:** Quejas de la comunidad; protestas; cobertura mediática negativa activista; ONGs en contra; autoridades investigan; dificultad para expandir operaciones.
**Early_Warning_Signals:** Sin política ambiental; quejas de vecinos; incidentes ambientales; sin relación con la comunidad; críticas en medios; empleados locales insatisfechos.
**Business_Impact:** Daño reputacional; boicots; multas ambientales; cierre de operaciones; dificultad para obtener permisos; pérdida de clientes; desconfianza de inversores.
**Severity_Level:** High
**Metrics_To_Check:** Número de incidentes ambientales; quejas de la comunidad; inversión en RSE/ventas; % de cumplimiento ambiental; cobertura mediática negativa.
**Diagnostic_Questions:** ¿Hay impacto ambiental negativo? ¿La comunidad está satisfecha? ¿Hay quejas o protestas? ¿Hay política de RSE? ¿Se gestiona el impacto social?
**Recommended_Actions:** Implementar gestión ambiental; reducir impacto; invertir en comunidad; establecer diálogo con stakeholders; reportar sostenibilidad; certificar ISO 14001; crear programa de RSE.
**Related_Patterns:** RSK-037, RSK-067, RSK-069, RSK-074, RSK-077

### RSK-069
**Pattern_Name:** Mala Gestión de Quejas y Reclamos
**Category:** Riesgo Reputacional
**Description:** La empresa no gestiona adecuadamente las quejas y reclamos de clientes, generando insatisfacción, boca a boca negativo y escalada a entidades regulatorias o medios.
**Typical_Causes:** Falta de proceso de quejas; personal no capacitado; cultura de "el cliente siempre se queja"; medición insuficiente; ausencia de sistema de gestión.
**Observable_Symptoms:** Quejas sin respuesta; clientes se quejan en redes porque no los atienden; mismos reclamos se repiten; clientes acuden a Profeco/Indecopi; quejas escalan a medios.
**Early_Warning_Signals:** Tiempo de respuesta a quejas > 48 horas; % de quejas resueltas en primer contacto < 50%; quejas recurrentes sobre mismos temas; % de quejas escaladas > 10%; NPS bajo.
**Business_Impact:** Daño reputacional; pérdida de clientes; multas regulatorias; costos de compensación; boca a boca negativo; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** Tiempo de respuesta a quejas; % de quejas resueltas en primer contacto; % de quejas escaladas; NPS; número de quejas recurrentes sobre mismo tema.
**Diagnostic_Questions:** ¿Hay proceso de gestión de quejas? ¿Se responden a tiempo? ¿Se resuelven en primer contacto? ¿Se analizan las causas raíz? ¿Los mismos problemas se repiten?
**Recommended_Actions:** Implementar sistema de gestión de quejas; capacitar al personal; establecer SLA de respuesta; analizar causas raíz; mejorar procesos basados en quejas; medir y mejorar CSAT.
**Related_Patterns:** RSK-063, RSK-065, RSK-066, RSK-074, RSK-093

### RSK-070
**Pattern_Name:** Falta de Transparencia en la Comunicación
**Category:** Riesgo Reputacional
**Description:** La empresa no comunica de manera transparente a sus stakeholders (clientes, empleados, inversores, comunidad) sobre sus prácticas, resultados o incidentes, generando desconfianza.
**Typical_Causes:** Cultura de opacidad; miedo a revelar debilidades; desconocimiento; "lo que no se sabe no duele"; falta de políticas de comunicación.
**Observable_Symptoms:** La empresa no publica información relevante; cuando hay incidentes, no comunica; stakeholders se enteran por terceros; rumores circulan; desconfianza general.
**Early_Warning_Signals:** Sin reportes a stakeholders; comunicación reactiva; rumores no gestionados; empleados no informados; clientes se enteran de cambios por medios no oficiales.
**Business_Impact:** Desconfianza de stakeholders; rumores dañinos; crisis mal gestionadas; pérdida de credibilidad; dificultad para atraer inversión; rotación de talento.
**Severity_Level:** Medium
**Metrics_To_Check:** Frecuencia de comunicación con stakeholders; % de incidentes comunicados proactivamente; nivel de confianza de stakeholders; cobertura mediática; rumores no gestionados.
**Diagnostic_Questions:** ¿La empresa comunica transparentemente? ¿Los stakeholders confían? ¿Se comunica proactivamente? ¿Hay política de comunicación? ¿Se gestionan los rumores?
**Recommended_Actions:** Desarrollar política de comunicación; comunicar proactivamente; ser transparente en resultados e incidentes; establecer canales de comunicación; capacitar voceros; reportar sostenibilidad.
**Related_Patterns:** RSK-064, RSK-067, RSK-069, RSK-074, RSK-077

### RSK-071
**Pattern_Name:** Riesgo por Asociación con Terceros Problemáticos
**Category:** Riesgo Reputacional
**Description:** La empresa se asocia (proveedores, socios, clientes, patrocinios) con terceros que tienen mala reputación o prácticas cuestionables, contaminando su propia imagen por asociación.
**Typical_Causes:** Debida diligencia insuficiente; presión por cerrar acuerdos; desconocimiento de reputación del tercero; falta de criterios de selección; enfoque solo en precio.
**Observable_Symptoms:** Proveedores con malas prácticas laborales; socios involucrados en escándalos; clientes con reputación dudosa; patrocinios controvertidos; críticas por asociación.
**Early_Warning_Signals:** Sin debida diligencia de terceros; proveedores sin evaluación reputacional; socios con antecedentes; clientes de alto riesgo; sin criterios éticos de selección.
**Business_Impact:** Daño reputacional por asociación; boicots; pérdida de clientes; investigaciones; costos de desvinculación; desconfianza de stakeholders.
**Severity_Level:** High
**Metrics_To_Check:** % de terceros con debida diligencia; número de incidentes con terceros; % de proveedores evaluados reputacionalmente; quejas por asociación.
**Diagnostic_Questions:** ¿Se evalúa la reputación de terceros? ¿Hay debida diligencia? ¿Los socios tienen buena reputación? ¿Los proveedores son éticos? ¿Hay criterios de selección reputacional?
**Recommended_Actions:** Implementar debida diligencia reputacional de terceros; establecer criterios éticos de selección; monitorear reputación de socios; desvincularse de terceros problemáticos; crear política de asociación.
**Related_Patterns:** RSK-067, RSK-068, RSK-070, RSK-074, RSK-106

### RSK-072
**Pattern_Name:** Vulnerabilidad a Fake News y Desinformación
**Category:** Riesgo Reputacional
**Description:** La empresa es vulnerable a campañas de desinformación o fake news que pueden dañar su reputación, especialmente en redes sociales y medios digitales.
**Typical_Causes:** Falta de monitoreo; ausencia de plan de respuesta; poca presencia digital; desconfianza preexistente; sector propenso a rumores.
**Observable_Symptoms:** Rumores falsos circulan sobre la empresa; información incorrecta en medios; la empresa no puede contrarrestar desinformación; empleados confundidos; clientes creen información falsa.
**Early_Warning_Signals:** Sin monitoreo de desinformación; sin capacidad de respuesta rápida; rumores no gestionados; baja credibilidad de la empresa; sector con alta desinformación.
**Business_Impact:** Daño reputacional; pérdida de ventas; desconfianza; tiempo y recursos para desmentir; impacto en empleados; costo de campañas de corrección.
**Severity_Level:** High
**Metrics_To_Check:** Tiempo de detección de desinformación; tiempo de respuesta; alcance de desinformación; % de stakeholders que creyeron información falsa; costo de corrección.
**Diagnostic_Questions:** ¿Se monitorea la desinformación? ¿Hay plan de respuesta? ¿La empresa tiene credibilidad para desmentir? ¿Se ha enfrentado fake news? ¿Hay capacidad de respuesta rápida?
**Recommended_Actions:** Implementar monitoreo de desinformación; crear plan de respuesta; fortalecer canales oficiales; construir credibilidad; responder rápidamente con hechos; capacitar voceros; aliarse con fact-checkers.
**Related_Patterns:** RSK-063, RSK-064, RSK-067, RSK-070, RSK-074

### RSK-073
**Pattern_Name:** Falta de Diferenciación y Propuesta de Valor Clara
**Category:** Riesgo Reputacional
**Description:** La empresa no tiene una propuesta de valor clara ni diferenciación en el mercado, siendo percibida como "una más" y teniendo dificultad para construir una marca sólida.
**Typical_Causes:** Estrategia de marca débil; falta de definición de propuesta de valor; imitación de competidores; ausencia de investigación de mercado; producto commodity.
**Observable_Symptoms:** Los clientes no distinguen a la empresa de la competencia; la marca no es reconocida; no hay razón clara para comprar; precio es el único factor de decisión; competidores son percibidos como mejores.
**Early_Warning_Signals:** Sin propuesta de valor documentada; marca no reconocida; % de compras por precio > 60%; sin diferenciación percibida; clientes no pueden explicar por qué compran.
**Business_Impact:** Competencia por precio; márgenes reducidos; baja lealtad de clientes; dificultad para atraer clientes; crecimiento limitado; vulnerabilidad a competidores.
**Severity_Level:** High
**Metrics_To_Check:** Reconocimiento de marca; % de compras por precio vs valor; NPS; diferenciación percibida; elasticidad precio de la demanda.
**Diagnostic_Questions:** ¿Los clientes distinguen a la empresa? ¿Hay propuesta de valor clara? ¿Por qué los clientes compran? ¿La marca es reconocida? ¿Hay diferenciación real?
**Recommended_Actions:** Definir propuesta de valor única; desarrollar estrategia de marca; investigar percepciones; diferenciar en servicio, calidad o innovación; comunicar diferenciación; construir marca.
**Related_Patterns:** RSK-065, RSK-069, RSK-074, RSK-075, RSK-093

### RSK-074
**Pattern_Name:** Ausencia de Programa de Responsabilidad Social Empresarial
**Category:** Riesgo Reputacional
**Description:** La empresa no cuenta con un programa de RSE, siendo percibida como indiferente a temas sociales y ambientales, lo que afecta su reputación especialmente entre clientes y talento joven.
**Typical_Causes:** Desconocimiento; falta de recursos; enfoque solo en rentabilidad; percepción de que RSE es solo para grandes empresas; ausencia de demanda de stakeholders.
**Observable_Symptoms:** La empresa no tiene iniciativas sociales; no reporta impacto; clientes preguntan por prácticas sostenibles; talento joven prefiere competidores con RSE; comunidad crítica.
**Early_Warning_Signals:** Sin política de RSE; sin iniciativas sociales; sin reporte de sostenibilidad; clientes preguntan por sostenibilidad; competidores tienen RSE; talento joven no se siente atraído.
**Business_Impact:** Pérdida de clientes sensibles a sostenibilidad; dificultad para atraer talento; desventaja competitiva; críticas de la comunidad; desinterés de inversores ESG.
**Severity_Level:** Medium
**Metrics_To_Check:** Existencia de programa de RSE; inversión en RSE/ventas; % de clientes que valoran la RSE; % de empleados orgullosos de la empresa; cobertura de RSE en medios.
**Diagnostic_Questions:** ¿Hay programa de RSE? ¿La empresa contribuye a la comunidad? ¿Los clientes valoran la sostenibilidad? ¿El talento joven se siente atraído? ¿Hay reporte de impacto?
**Recommended_Actions:** Implementar programa de RSE; identificar causas relevantes; involucrar al equipo; reportar impacto; comunicar iniciativas; obtener certificaciones; medir retorno reputacional.
**Related_Patterns:** RSK-037, RSK-067, RSK-068, RSK-071, RSK-077

## Riesgo Estratégico

### RSK-075
**Pattern_Name:** Estrategia de Negocio No Definida o Poco Clara
**Category:** Riesgo Estratégico
**Description:** La empresa no tiene una estrategia definida, documentada y comunicada, operando de manera reactiva sin dirección clara, objetivos ni planes para alcanzarlos.
**Typical_Causes:** Gerencia enfocada en operación diaria; falta de planificación; cultura de "improvisar"; equipo directivo sin experiencia estratégica; empresa familiar sin proceso estratégico.
**Observable_Symptoms:** No hay plan estratégico; las decisiones se toman según la coyuntura; no hay objetivos claros; el equipo no sabe hacia dónde va la empresa; se cambia de dirección constantemente.
**Early_Warning_Signals:** Sin plan estratégico documentado; sin misión/visión definidas; sin objetivos anuales; decisiones inconsistentes; falta de dirección; equipo desorientado.
**Business_Impact:** Recursos mal asignados; oportunidades perdidas; crecimiento subóptimo; falta de enfoque; equipo desmotivado; vulnerabilidad competitiva; imposibilidad de medir progreso.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de plan estratégico; % del equipo que conoce la estrategia; cumplimiento de objetivos; coherencia de decisiones; % de iniciativas estratégicas vs operativas.
**Diagnostic_Questions:** ¿Hay plan estratégico? ¿El equipo conoce la dirección? ¿Las decisiones son coherentes? ¿Hay objetivos claros? ¿Se mide el avance?
**Recommended_Actions:** Desarrollar plan estratégico; definir misión, visión y valores; establecer objetivos SMART; comunicar la estrategia; alinear iniciativas; realizar revisiones periódicas.
**Related_Patterns:** RSK-076, RSK-077, RSK-078, RSK-079, RSK-092

### RSK-076
**Pattern_Name:** Falta de Innovación y Adaptación al Cambio
**Category:** Riesgo Estratégico
**Description:** La empresa no innova ni se adapta a cambios del mercado, tecnología o preferencias de clientes, quedándose obsoleta frente a competidores más ágiles.
**Typical_Causes:** Conformismo; falta de inversión en I+D; cultura de "siempre lo hicimos así"; ausencia de monitoreo de tendencias; aversión al riesgo; cortoplacismo.
**Observable_Symptoms:** Los mismos productos por años; no hay nuevos lanzamientos; competidores innovan y la empresa no; clientes piden cosas que la empresa no ofrece; tecnología obsoleta; procesos anticuados.
**Early_Warning_Signals:** % de ingresos de productos nuevos < 10% (últimos 3 años); inversión en I+D/ventas < 1%; sin nuevos productos; imitación de competidores; resistencia al cambio.
**Business_Impact:** Pérdida de participación de mercado; obsolescencia; menor rentabilidad; clientes migran a competidores; incapacidad de atraer talento joven; desaparición gradual.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ingresos de productos nuevos; inversión en I+D/ventas; número de innovaciones implementadas; time-to-market; % de clientes que piden nuevas soluciones.
**Diagnostic_Questions:** ¿Cuándo fue el último lanzamiento? ¿Se invierte en innovación? ¿La empresa se adapta a cambios? ¿Los competidores innovan más? ¿Hay cultura de innovación?
**Recommended_Actions:** Crear área de innovación; invertir en I+D; fomentar cultura de innovación; monitorear tendencias; implementar procesos de innovación abierta; prototipar rápido; aprender del fracaso.
**Related_Patterns:** RSK-075, RSK-077, RSK-080, RSK-085, RSK-092

### RSK-077
**Pattern_Name:** Desalineación entre Estrategia y Ejecución
**Category:** Riesgo Estratégico
**Description:** Existe una brecha entre la estrategia definida y lo que realmente se ejecuta en el día a día, haciendo que los objetivos estratégicos no se materialicen.
**Typical_Causes:** Estrategia no comunicada; falta de cascada de objetivos; incentivos desalineados; cultura operativa sin conexión estratégica; falta de seguimiento.
**Observable_Symptoms:** El equipo no sabe cómo su trabajo contribuye a la estrategia; los proyectos no reflejan prioridades estratégicas; los incentivos premian lo operativo no lo estratégico; el día a día consume todo el tiempo.
**Early_Warning_Signals:** Objetivos estratégicos sin traducir a KPIs; % de empleados que conoce la estrategia < 30%; proyectos sin alineación estratégica; incentivos no alineados; reuniones sin conexión estratégica.
**Business_Impact:** Estrategia no se implementa; recursos mal asignados; resultados inferiores; frustración del equipo directivo; pérdida de oportunidades; falta de accountability.
**Severity_Level:** Critical
**Metrics_To_Check:** % de empleados que conoce la estrategia; % de proyectos alineados con estrategia; cumplimiento de objetivos estratégicos; % de tiempo dedicado a iniciativas estratégicas.
**Diagnostic_Questions:** ¿La estrategia se ejecuta? ¿El equipo sabe cómo contribuye? ¿Los proyectos reflejan la estrategia? ¿Los incentivos están alineados? ¿Hay seguimiento?
**Recommended_Actions:** Comunicar estrategia a toda la organización; cascada de objetivos (OKRs/KPIs); alinear incentivos; asignar recursos a iniciativas estratégicas; revisar avance periódicamente; liderar con el ejemplo.
**Related_Patterns:** RSK-075, RSK-078, RSK-079, RSK-084, RSK-092

### RSK-078
**Pattern_Name:** Cortoplacismo en la Toma de Decisiones
**Category:** Riesgo Estratégico
**Description:** La empresa toma decisiones enfocadas en resultados de corto plazo, sacrificando la sostenibilidad y crecimiento de largo plazo, generando problemas futuros.
**Typical_Causes:** Presión por resultados trimestrales; dueños que buscan dividendos inmediatos; falta de visión a largo plazo; incentivos cortoplacistas; ausencia de planificación estratégica.
**Observable_Symptoms:** Se recortan inversiones para mostrar utilidades; no se invierte en I+D; se descuida mantenimiento; se reduce calidad para bajar costos; rotación alta por falta de desarrollo; deuda crece.
**Early_Warning_Signals:** Inversión en CAPEX decreciente; I+D < 1% de ventas; mantenimiento postergado; quejas de calidad; rotación de talento; gasto en capacitación mínimo.
**Business_Impact:** Obsolescencia; pérdida de competitividad; fuga de talento; deterioro de activos; clientes insatisfechos; crisis futura por falta de inversión; menor valor de la empresa.
**Severity_Level:** High
**Metrics_To_Check:** CAPEX/ventas; inversión en I+D; inversión en mantenimiento; inversión en capacitación; % de decisiones con perspectiva > 3 años.
**Diagnostic_Questions:** ¿Se invierte para el futuro? ¿Se recortan inversiones para mostrar utilidades? ¿Hay visión de largo plazo? ¿Los incentivos fomentan el cortoplacismo? ¿Hay plan a 3-5 años?
**Recommended_Actions:** Balancear objetivos de corto y largo plazo; establecer incentivos de largo plazo; crear plan estratégico 3-5 años; presupuestar inversiones; educar a accionistas en visión de largo plazo.
**Related_Patterns:** RSK-075, RSK-076, RSK-079, RSK-081, RSK-092

### RSK-079
**Pattern_Name:** Toma de Decisiones sin Datos ni Análisis
**Category:** Riesgo Estratégico
**Description:** Las decisiones estratégicas se toman basadas en intuición, corazonadas o presiones, sin respaldo de datos, análisis o información confiable, aumentando la probabilidad de error.
**Typical_Causes:** Cultura de "yo conozco el negocio"; falta de datos disponibles; ausencia de herramientas de análisis; gerencia con poca formación analítica; velocidad sobre precisión.
**Observable_Symptoms:** Decisiones importantes basadas en "corazonadas"; no se consultan datos; las justificaciones son subjetivas; errores recurrentes en decisiones; no hay análisis de alternativas.
**Early_Warning_Signals:** Sin KPIs para decisiones; % de decisiones basadas en datos < 30%; errores en decisiones estratégicas recurrentes; sin análisis de escenarios; procesos de decisión no documentados.
**Business_Impact:** Malas decisiones estratégicas; pérdida de oportunidades; errores costosos; resultados inconsistentes; falta de rigor; desconfianza en la gestión.
**Severity_Level:** High
**Metrics_To_Check:** % de decisiones basadas en datos; calidad de datos disponibles; número de errores estratégicos; existencia de procesos de decisión; % de decisiones con análisis de alternativas.
**Diagnostic_Questions:** ¿Las decisiones se basan en datos? ¿Hay información confiable disponible? ¿Se analizan alternativas? ¿Hay errores recurrentes? ¿Hay proceso de toma de decisiones?
**Recommended_Actions:** Implementar sistema de Business Intelligence; definir KPIs; capacitar en análisis de datos; establecer proceso de toma de decisiones; usar modelos de decisión; crear cultura data-driven.
**Related_Patterns:** RSK-012, RSK-075, RSK-078, RSK-082, RSK-092

### RSK-080
**Pattern_Name:** Estrategia de Crecimiento No Sostenible
**Category:** Riesgo Estratégico
**Description:** La empresa persigue un crecimiento acelerado sin la estructura, capital, procesos o talento para sostenerlo, generando problemas operativos, financieros y de calidad.
**Typical_Causes:** Ambición sin planificación; presión por crecimiento; falta de experiencia en escalar; subestimación de necesidades; financiamiento insuficiente.
**Observable_Symptoms:** Ventas crecen pero utilidades no; calidad se deteriora al crecer; equipo desbordado; procesos no escalan; clientes insatisfechos; flujo de caja negativo a pesar de crecimiento.
**Early_Warning_Signals:** Crecimiento de ventas > 30% sin aumento de capacidad; utilidad neta decreciente con ventas crecientes; rotación de personal aumenta; quejas de calidad; capital de trabajo negativo.
**Business_Impact:** Crisis de liquidez; pérdida de calidad; clientes insatisfechos; colapso operativo; daño reputacional; posible quiebra si el crecimiento se detiene.
**Severity_Level:** Critical
**Metrics_To_Check:** Crecimiento de ventas vs utilidad; rotación de personal; quejas de clientes; capital de trabajo; capacidad utilizada.
**Diagnostic_Questions:** ¿El crecimiento es rentable? ¿La operación soporta el crecimiento? ¿Hay suficiente capital de trabajo? ¿La calidad se mantiene? ¿El equipo está desbordado?
**Recommended_Actions:** Planificar crecimiento con recursos adecuados; asegurar financiamiento; fortalecer procesos y sistemas; contratar talento; controlar calidad; crecer a ritmo sostenible.
**Related_Patterns:** RSK-001, RSK-002, RSK-010, RSK-020, RSK-076

### RSK-081
**Pattern_Name:** Riesgo de Disrupción del Modelo de Negocio
**Category:** Riesgo Estratégico
**Description:** El modelo de negocio actual corre riesgo de ser disrumpido por nuevas tecnologías, competidores o cambios en el comportamiento del consumidor, amenazando su viabilidad futura.
**Typical_Causes:** Tecnología emergente; nuevos competidores digitales; cambio en preferencias; regulación; falta de innovación; no monitoreo del entorno.
**Observable_Symptoms:** Nuevos competidores crecen rápido; clientes migran a alternativas; el modelo tradicional pierde tracción; márgenes se comprimen; tecnología hace obsoleto el modelo.
**Early_Warning_Signals:** % de mercado perdido a nuevos competidores; ingresos de modelo tradicional decrecientes; nuevos players creciendo > 20% anual; clientes piden soluciones digitales; margen comprimido.
**Business_Impact:** Obsolescencia del negocio; pérdida de mercado; desaparición gradual; necesidad de transformación costosa; posible quiebra si no se adapta.
**Severity_Level:** Critical
**Metrics_To_Check:** % de mercado vs nuevos competidores; tendencia de ingresos; % de ingresos digitales; inversión en transformación; NPS vs nuevos competidores.
**Diagnostic_Questions:** ¿Hay riesgo de disrupción? ¿Nuevos competidores amenazan? ¿El modelo de negocio sigue siendo relevante? ¿Se está invirtiendo en transformación? ¿Los clientes están migrando?
**Recommended_Actions:** Monitorear tendencias de disrupción; invertir en innovación; transformar modelo de negocio; crear nuevas líneas de negocio; adquirir startups; desarrollar capacidades digitales.
**Related_Patterns:** RSK-075, RSK-076, RSK-080, RSK-085, RSK-092

### RSK-082
**Pattern_Name:** Falta de Monitoreo del Entorno Competitivo
**Category:** Riesgo Estratégico
**Description:** La empresa no monitorea sistemáticamente a sus competidores, el mercado, las tendencias y el entorno regulatorio, siendo sorprendida por cambios que afectan su posición competitiva.
**Typical_Causes:** Falta de proceso de inteligencia competitiva; arrogancia; recursos limitados; cultura de "concentrarse en lo nuestro"; desconocimiento de herramientas.
**Observable_Symptoms:** Movimientos de competidores toman por sorpresa; nuevos participantes no anticipados; cambios de mercado no previstos; la empresa reacciona tarde; decisiones basadas en información desactualizada.
**Early_Warning_Signals:** Sin sistema de monitoreo competitivo; sin análisis de competidores; % de cambios de mercado anticipados < 30%; información desactualizada; sin alertas de cambios.
**Business_Impact:** Decisiones estratégicas desinformadas; pérdida de participación; reacción tardía; oportunidades perdidas; amenazas no identificadas; ventaja competitiva erosionada.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de sistema de monitoreo; % de cambios anticipados; frecuencia de análisis competitivo; % de decisiones informadas por inteligencia competitiva.
**Diagnostic_Questions:** ¿Se monitorea a los competidores? ¿Se anticipan cambios? ¿La información del mercado está actualizada? ¿Hay proceso de inteligencia competitiva? ¿Las decisiones consideran el entorno?
**Recommended_Actions:** Implementar sistema de inteligencia competitiva; monitorear competidores, mercado y tendencias; usar herramientas de monitoreo; asignar responsable; compartir inteligencia con el equipo; revisar periódicamente.
**Related_Patterns:** RSK-075, RSK-076, RSK-079, RSK-081, RSK-092

### RSK-083
**Pattern_Name:** Falta de Plan de Sucesión de la Dirección
**Category:** Riesgo Estratégico
**Description:** La empresa no tiene un plan de sucesión para la dirección general o puestos clave, exponiéndose a una crisis de liderazgo si el titular se ausenta definitivamente.
**Typical_Causes:** Fundador/dueño no delega; falta de candidatos internos; cultura de "soy insustituible"; falta de planificación; empresa familiar sin separación de propiedad y gestión.
**Observable_Symptoms:** Nadie puede reemplazar al director general; no hay candidatos internos; si el fundador falta, la empresa se paraliza; no se ha discutido la sucesión; dependencia total del líder.
**Early_Warning_Signals:** Director general con más de 60 años sin sucesor; sin candidatos internos; sin plan de sucesión documentado; dependencia total de una persona; familia no preparada.
**Business_Impact:** Crisis de liderazgo; parálisis organizacional; pérdida de clientes y proveedores; conflictos familiares; posible quiebra; pérdida de valor de la empresa.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de plan de sucesión; % de puestos clave con sucesor identificado; tiempo para reemplazar director general; edad del director general; % de familia en dirección.
**Diagnostic_Questions:** ¿Hay plan de sucesión? ¿Quién reemplazaría al director general? ¿Hay candidatos internos? ¿El fundador ha preparado su sucesión? ¿La familia está preparada?
**Recommended_Actions:** Desarrollar plan de sucesión; identificar y desarrollar candidatos internos; establecer programa de mentoring; separar propiedad de gestión; considerar sucesión externa; documentar proceso.
**Related_Patterns:** RSK-014, RSK-023, RSK-075, RSK-084, RSK-124

### RSK-084
**Pattern_Name:** Conflictos de Interés entre Socios o Accionistas
**Category:** Riesgo Estratégico
**Description:** Existen conflictos de interés entre socios o accionistas que afectan la toma de decisiones estratégicas, la gobernanza y la operación de la empresa.
**Typical_Causes:** Falta de acuerdo de accionistas; visión diferente del negocio; intereses personales vs empresariales; distribución de utilidades no acordada; roles no definidos.
**Observable_Symptoms:** Desacuerdos frecuentes en juntas; decisiones bloqueadas; socios trabajan en diferentes direcciones; disputas por utilidades; socios quieren salir; falta de confianza.
**Early_Warning_Signals:** Sin acuerdo de accionistas; reuniones conflictivas; decisiones estratégicas postergadas; socios con intereses divergentes; rumores de disputas.
**Business_Impact:** Parálisis estratégica; imposibilidad de tomar decisiones; pérdida de oportunidades; salida de socios; disolución de la empresa; pérdida de valor.
**Severity_Level:** Critical
**Metrics_To_Check:** Existencia de acuerdo de accionistas; frecuencia de conflictos; tiempo para tomar decisiones estratégicas; % de socios alineados con la estrategia; rotación de socios.
**Diagnostic_Questions:** ¿Hay acuerdo de accionistas? ¿Los socios tienen visión compartida? ¿Hay conflictos frecuentes? ¿Se toman decisiones a tiempo? ¿Hay reglas claras de gobierno?
**Recommended_Actions:** Formalizar acuerdo de accionistas; establecer gobierno corporativo; definir roles y responsabilidades; crear mecanismos de resolución de conflictos; mediar con asesor externo; considerar recompra de participaciones.
**Related_Patterns:** RSK-075, RSK-077, RSK-083, RSK-085, RSK-092

### RSK-085
**Pattern_Name:** Riesgo de Salida de Socios o Fundadores
**Category:** Riesgo Estratégico
**Description:** La salida de un socio o fundador clave (por fallecimiento, incapacidad, retiro o conflicto) puede desestabilizar la empresa si no hay mecanismos contractuales y financieros previstos.
**Typical_Causes:** Falta de acuerdo de accionistas; ausencia de seguro de vida; dependencia de un socio; falta de planificación; empresa familiar sin protocolo.
**Observable_Symptoms:** No hay acuerdo de compra-venta entre socios; no se ha valorado la empresa para efectos de salida; no hay seguro de vida para socios; la salida de un socio causaría problemas financieros.
**Early_Warning_Signals:** Sin pacto de accionistas; sin seguro de vida para socios clave; sin acuerdo de compra-venta; socios mayores de 60 años; socios sin testamento; dependencia de un socio.
**Business_Impact:** Disputas legales; necesidad de vender la empresa; falta de liquidez para pagar a socios salientes; pérdida de control; paralización; conflictos familiares.
**Severity_Level:** High
**Metrics_To_Check:** Existencia de pacto de accionistas; existencia de seguro de vida para socios; % de socios con acuerdo de salida; edad promedio de socios; % de dependencia de cada socio.
**Diagnostic_Questions:** ¿Hay acuerdo de salida de socios? ¿Hay seguro de vida para socios? ¿La empresa sobreviviría a la salida de un socio? ¿Hay pacto de accionistas? ¿Se ha valorado la empresa?
**Recommended_Actions:** Formalizar pacto de accionistas con cláusulas de salida; contratar seguro de vida para socios; valorar la empresa periódicamente; establecer mecanismos de entrada y salida; crear protocolo familiar.
**Related_Patterns:** RSK-083, RSK-084, RSK-092, RSK-124, RSK-128

### RSK-086
**Pattern_Name:** Estrategia de Precios Incorrecta
**Category:** Riesgo Estratégico
**Description:** La empresa tiene una estrategia de precios que no refleja el valor entregado, la estructura de costos o la disposición a pagar del mercado, afectando rentabilidad o volumen.
**Typical_Causes:** Desconocimiento de costos; fijación de precios basada en competencia sin análisis; miedo a subir precios; falta de segmentación; estrategia de precio única para todos.
**Observable_Symptoms:** Precios muy por debajo del valor; descuentos constantes; clientes sensibles al precio; márgenes bajos; incapacidad de subir precios; precios no cubren costos.
**Early_Warning_Signals:** Margen bruto < promedio sectorial; elasticidad precio no calculada; precios no revisados en > 1 año; % de descuento sobre precio de lista > 20%; quejas de clientes sobre precios.
**Business_Impact:** Baja rentabilidad; guerra de precios; percepción de baja calidad; incapacidad de invertir; desvalorización de la marca; dificultad para crecer.
**Severity_Level:** High
**Metrics_To_Check:** Margen bruto; precio vs competencia; elasticidad precio; % de descuentos; rentabilidad por segmento de clientes.
**Diagnostic_Questions:** ¿Los precios reflejan el valor? ¿Cubren los costos? ¿Hay estrategia de precios? ¿Se segmentan los precios? ¿Se revisan periódicamente?
**Recommended_Actions:** Definir estrategia de precios basada en valor; segmentar clientes y ajustar precios; analizar costos reales; reducir descuentos; subir precios gradualmente; comunicar valor.
**Related_Patterns:** RSK-004, RSK-009, RSK-073, RSK-092, RSK-095

### RSK-087
**Pattern_Name:** Falta de Alianzas Estratégicas
**Category:** Riesgo Estratégico
**Description:** La empresa no desarrolla alianzas estratégicas que podrían potenciar su crecimiento, acceso a mercados, tecnología o capacidades, perdiendo oportunidades competitivas.
**Typical_Causes:** Cultura de "hacerlo todo solos"; desconfianza; falta de capacidad de negociación; desconocimiento de beneficios; falta de red de contactos.
**Observable_Symptoms:** La empresa opera completamente sola; oportunidades de colaboración no se aprovechan; competidores forman alianzas que la empresa no; los clientes piden soluciones que requieren socios.
**Early_Warning_Signals:** Número de alianzas activas = 0; % de ingresos de alianzas = 0; competidores con alianzas; oportunidades de colaboración identificadas no aprovechadas; sin proceso de búsqueda de alianzas.
**Business_Impact:** Crecimiento más lento; acceso limitado a tecnología; menor alcance geográfico; incapacidad de ofrecer soluciones completas; desventaja competitiva.
**Severity_Level:** Medium
**Metrics_To_Check:** Número de alianzas activas; % de ingresos de alianzas; % de objetivos alcanzados con alianzas; ROI de alianzas; satisfacción con alianzas.
**Diagnostic_Questions:** ¿Hay alianzas estratégicas? ¿Se aprovechan oportunidades de colaboración? ¿Los competidores tienen alianzas? ¿Hay capacidades que se podrían obtener mediante alianzas? ¿Hay proceso de búsqueda?
**Recommended_Actions:** Identificar potenciales aliados; desarrollar propuesta de valor para alianzas; establecer programa de alianzas; negociar acuerdos win-win; gestionar relaciones; medir resultados.
**Related_Patterns:** RSK-075, RSK-076, RSK-081, RSK-092, RSK-112

### RSK-088
**Pattern_Name:** Riesgo de Internacionalización o Expansión Geográfica
**Category:** Riesgo Estratégico
**Description:** La empresa expande sus operaciones a nuevos mercados geográficos sin la preparación adecuada, exponiéndose a riesgos culturales, regulatorios, operativos y financieros.
**Typical_Causes:** Oportunidad de mercado; presión por crecer; falta de investigación; subestimación de diferencias; falta de recursos para expansión.
**Observable_Symptoms:** Problemas en nuevo mercado adaptación de producto; regulaciones no anticipadas; diferencias culturales no gestionadas; costos mayores a los presupuestados; resultados por debajo de lo esperado.
**Early_Warning_Signals:** Sin investigación de mercado previa; sin plan de internacionalización; presupuesto insuficiente; sin equipo local; sin asesoría legal local; subestimación de diferencias culturales.
**Business_Impact:** Pérdidas en la inversión de expansión; daño reputacional; distracción del negocio principal; costos no recuperables; retiro forzoso del mercado.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos internacionales; ROI de expansión; % de objetivos cumplidos en nuevo mercado; costos de expansión vs presupuesto; tiempo para alcanzar break-even.
**Diagnostic_Questions:** ¿Hay plan de internacionalización? ¿Se investigó el mercado? ¿Se consideraron diferencias culturales/legales? ¿Hay presupuesto adecuado? ¿Hay equipo local?
**Recommended_Actions:** Desarrollar plan de internacionalización; investigar mercado; adaptar producto/servicio; establecer equipo local; asesoría legal y fiscal; presupuestar adecuadamente; considerar socios locales.
**Related_Patterns:** RSK-075, RSK-080, RSK-087, RSK-092, RSK-094

### RSK-089
**Pattern_Name:** Obsesión por el Competidor (Estrategia Reactiva)
**Category:** Riesgo Estratégico
**Description:** La empresa define su estrategia principalmente reaccionando a movimientos de competidores, perdiendo su propia dirección y diferenciación, siempre a la defensiva.
**Typical_Causes:** Complejo de inferioridad; falta de confianza en la propuesta de valor; líder sin visión propia; cultura de imitación; falta de análisis estratégico.
**Observable_Symptoms:** La empresa copia a competidores; reacciona a cada movimiento; no tiene iniciativa propia; siempre va detrás; los clientes no distinguen la diferencia.
**Early_Warning_Signals:** % de iniciativas que son reacción a competidores > 60%; sin iniciativas propias; imitación constante; clientes no diferencian; liderazgo reactivo.
**Business_Impact:** Pérdida de diferenciación; márgenes comprimidos; siempre un paso atrás; falta de dirección propia; vulnerabilidad a disrupción.
**Severity_Level:** Medium
**Metrics_To_Check:** % de iniciativas reactivas vs proactivas; diferenciación percibida; % de innovaciones propias; satisfacción del liderazgo con la dirección estratégica.
**Diagnostic_Questions:** ¿La estrategia es reactiva? ¿Se imita a competidores? ¿Hay iniciativa propia? ¿Los clientes diferencian? ¿El líder tiene visión propia?
**Recommended_Actions:** Definir estrategia propia basada en fortalezas; enfocarse en clientes no en competidores; innovar; construir diferenciación; dejar de reaccionar a todo; confiar en la propuesta de valor.
**Related_Patterns:** RSK-073, RSK-075, RSK-076, RSK-082, RSK-092

### RSK-090
**Pattern_Name:** Exceso de Confianza en el Negocio Actual
**Category:** Riesgo Estratégico
**Description:** La empresa está demasiado cómoda con su éxito actual y no anticipa cambios, asumiendo que el futuro será similar al pasado, sin prepararse para disrupciones.
**Typical_Causes:** Éxito prolongado; arrogancia; falta de humildad; ausencia de planificación de escenarios; cultura de "siempre funcionó".
**Observable_Symptoms:** La empresa no invierte en innovación; descarta amenazas; cree que está blindada; no monitorea cambios; dice "esto no nos pasará"; no se prepara para escenarios adversos.
**Early_Warning_Signals:** Sin análisis de escenarios; % de inversión en innovación bajo; amenazas identificadas no atendidas; % de ingresos de productos antiguos > 80%; cultura de complacencia.
**Business_Impact:** Vulnerabilidad a disrupción; pérdida de mercado; crisis cuando cambien las condiciones; falta de preparación; posible desaparición.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos de productos existentes; inversión en innovación; % de escenarios planificados; % de amenazas identificadas con plan de respuesta.
**Diagnostic_Questions:** ¿Hay complacencia? ¿Se invierte en innovación? ¿Se consideran escenarios adversos? ¿Hay preparación para cambios? ¿La empresa cree que es inmune?
**Recommended_Actions:** Fomentar humildad estratégica; planificar escenarios; invertir en innovación; monitorear señales de cambio; desafiar supuestos; crear cultura de anticipación.
**Related_Patterns:** RSK-075, RSK-076, RSK-078, RSK-081, RSK-092

### RSK-091
**Pattern_Name:** Mala Gestión de Proyectos Estratégicos
**Category:** Riesgo Estratégico
**Description:** La empresa ejecuta proyectos estratégicos sin metodología de gestión de proyectos, generando retrasos, sobrecostos, baja calidad y fracaso en la implementación.
**Typical_Causes:** Falta de metodología; recursos insuficientes; falta de liderazgo de proyectos; ausencia de seguimiento; proyectos sin patrocinador.
**Observable_Symptoms:** Proyectos se retrasan; sobrecostos frecuentes; alcance se reduce; proyectos no se completan; fracaso de iniciativas; falta de accountability.
**Early_Warning_Signals:** % de proyectos a tiempo < 50%; desviación de presupuesto > 20%; % de proyectos abandonados > 20%; sin metodología; sin Project Manager; sin comité de proyectos.
**Business_Impact:** Estrategia no implementada; recursos desperdiciados; fracaso de iniciativas clave; desmotivación; pérdida de oportunidades; costos no recuperables.
**Severity_Level:** High
**Metrics_To_Check:** % de proyectos a tiempo; desviación de presupuesto; % de proyectos completados; ROI de proyectos; satisfacción de stakeholders.
**Diagnostic_Questions:** ¿Hay metodología de proyectos? ¿Los proyectos se completan a tiempo y presupuesto? ¿Hay Project Manager? ¿Hay seguimiento? ¿Los proyectos estratégicos se implementan?
**Recommended_Actions:** Implementar metodología de gestión de proyectos (PMI, Agile); asignar Project Manager; establecer comité de proyectos; hacer seguimiento; capacitar al equipo; usar herramientas.
**Related_Patterns:** RSK-075, RSK-077, RSK-079, RSK-092, RSK-125

### RSK-092
**Pattern_Name:** Ausencia de Proceso de Revisión Estratégica Periódica
**Category:** Riesgo Estratégico
**Description:** La empresa no realiza revisiones periódicas de su estrategia, manteniendo el mismo plan aunque el entorno cambie, resultando en una estrategia desactualizada e irrelevante.
**Typical_Causes:** Falta de disciplina estratégica; cultura de "plan para cumplir"; gerencia ocupada; miedo a reconocer errores; proceso estratégico anual insuficiente.
**Observable_Symptoms:** El plan estratégico no se actualiza; los supuestos originales ya no son válidos; la empresa sigue haciendo lo mismo aunque el mercado cambió; no hay revisiones trimestrales.
**Early_Warning_Signals:** Plan estratégico no actualizado en > 1 año; sin revisiones periódicas; supuestos estratégicos desactualizados; % del plan aún relevante < 50%; cambios de entorno no incorporados.
**Business_Impact:** Estrategia irrelevante; recursos mal asignados; oportunidades perdidas; amenazas no atendidas; pérdida de dirección; fracaso estratégico.
**Severity_Level:** High
**Metrics_To_Check:** Frecuencia de revisión estratégica; % de plan actualizado; % de supuestos aún válidos; % de cambios de entorno incorporados; satisfacción con relevancia de la estrategia.
**Diagnostic_Questions:** ¿Se revisa la estrategia periódicamente? ¿El plan está actualizado? ¿Los supuestos siguen siendo válidos? ¿Se incorporan cambios del entorno? ¿La estrategia sigue siendo relevante?
**Recommended_Actions:** Establecer proceso de revisión estratégica trimestral; actualizar plan anualmente; monitorear supuestos; incorporar cambios; realizar análisis FODA periódico; ajustar curso.
**Related_Patterns:** RSK-075, RSK-077, RSK-078, RSK-079, RSK-082


## Riesgo Comercial

### RSK-093
**Pattern_Name:** Caída Sostenida de Ventas
**Category:** Riesgo Comercial
**Description:** La empresa experimenta una disminución sostenida en sus ventas por factores de mercado, competencia, producto o ejecución comercial, sin una estrategia efectiva de recuperación.
**Typical_Causes:** Pérdida de competitividad; cambios en preferencias; entrada de nuevos competidores; estrategia comercial débil; producto no renovado; fuerza de ventas ineficaz.
**Observable_Symptoms:** Ventas decrecientes trimestre a trimestre; pérdida de clientes; dificultad para alcanzar presupuesto; descuentos excesivos; la fuerza de ventas no cumple metas.
**Early_Warning_Signals:** Ventas decrecientes 3 trimestres consecutivos; % de cumplimiento de presupuesto < 80%; pérdida de clientes > 10% anual; participación de mercado decreciente; pipeline decreciente.
**Business_Impact:** Menor rentabilidad; problemas de flujo de caja; despidos; reducción de inversiones; posible cierre; pérdida de valor de la empresa.
**Severity_Level:** Critical
**Metrics_To_Check:** Tendencia de ventas; % de cumplimiento de presupuesto; % de pérdida de clientes; participación de mercado; pipeline de ventas.
**Diagnostic_Questions:** ¿Las ventas vienen cayendo? ¿Por qué? ¿Hay pérdida de clientes? ¿La competencia está ganando mercado? ¿Hay plan de recuperación?
**Recommended_Actions:** Investigar causas raíz; renovar estrategia comercial; mejorar producto; capacitar fuerza de ventas; diversificar canales; ajustar precios; lanzar campañas.
**Related_Patterns:** RSK-003, RSK-004, RSK-009, RSK-094, RSK-098

### RSK-094
**Pattern_Name:** Pérdida de Participación de Mercado
**Category:** Riesgo Comercial
**Description:** La empresa pierde participación de mercado frente a competidores, indicando que su propuesta de valor, precios o ejecución comercial son menos efectivos que los de la competencia.
**Typical_Causes:** Competidores más agresivos; falta de innovación; producto/servicio commodity; mala ejecución de ventas; falta de diferenciación; debilidad en marketing.
**Observable_Symptoms:** Los competidores crecen más rápido; la empresa pierde clientes importantes; nuevos competidores ganan espacio; la marca pierde relevancia; los clientes mencionan a competidores.
**Early_Warning_Signals:** Participación de mercado decreciente 2 años consecutivos; tasa de crecimiento menor que el mercado; nuevos competidores ganan share; % de clientes que consideran competidores > 30%.
**Business_Impact:** Menor visibilidad; menor poder de negociación; márgenes comprimidos; dificultad para atraer talento; posible salida del mercado; menor valor de la empresa.
**Severity_Level:** Critical
**Metrics_To_Check:** Participación de mercado; tasa de crecimiento vs mercado; % de clientes perdidos a competidores; posicionamiento de marca; NPS vs competidores.
**Diagnostic_Questions:** ¿La participación de mercado está cayendo? ¿Quién está ganando? ¿Por qué los clientes prefieren a competidores? ¿Hay plan para recuperar share? ¿La marca es relevante?
**Recommended_Actions:** Analizar ventajas competitivas; invertir en diferenciación; mejorar propuesta de valor; fortalecer marca; innovar; capturar clientes de competidores; mejorar ejecución.
**Related_Patterns:** RSK-003, RSK-073, RSK-075, RSK-093, RSK-098

### RSK-095
**Pattern_Name:** Pronósticos de Demanda Inexactos
**Category:** Riesgo Comercial
**Description:** La empresa realiza pronósticos de demanda sistemáticamente incorrectos, resultando en excesos o faltantes de inventario, ineficiencias y pérdidas de ventas.
**Typical_Causes:** Métodos de pronóstico inadecuados; falta de datos históricos; no incorporación de variables de mercado; ausencia de procesos de S&OP; sesgo optimista/pesimista.
**Observable_Symptoms:** Faltantes de inventario frecuentes; excesos de inventario; ventas perdidas por falta de stock; descuentos para liquidar excesos; el equipo no confía en los pronósticos.
**Early_Warning_Signals:** Error de pronóstico (MAPE) > 30%; % de faltantes > 10%; % de excesos > 20%; rotación de inventario baja; desviación entre pronóstico y real > 25%.
**Business_Impact:** Pérdida de ventas; capital inmovilizado; obsolescencia; descuentos; costos de almacenamiento; ineficiencia en producción; insatisfacción de clientes.
**Severity_Level:** High
**Metrics_To_Check:** MAPE; % de faltantes; % de excesos; rotación de inventario; precisión de pronóstico por línea.
**Diagnostic_Questions:** ¿Los pronósticos son precisos? ¿Hay faltantes o excesos frecuentes? ¿Se usa método de pronóstico? ¿Hay proceso S&OP? ¿Se ajustan los pronósticos?
**Recommended_Actions:** Mejorar método de pronóstico; incorporar datos de mercado; implementar S&OP; usar herramientas de forecasting; involucrar a ventas y marketing; revisar y ajustar periódicamente.
**Related_Patterns:** RSK-025, RSK-026, RSK-093, RSK-096, RSK-101

### RSK-096
**Pattern_Name:** Estacionalidad y Estacionalidad Inversa
**Category:** Riesgo Comercial
**Description:** La empresa enfrenta fluctuaciones estacionales marcadas en la demanda que no son gestionadas adecuadamente, con consecuencias en flujo de caja, inventarios y capacidad.
**Typical_Causes:** Negocio intrínsecamente estacional; falta de diversificación de productos; ausencia de productos contra-cíclicos; planificación deficiente.
**Observable_Symptoms:** Picos y valles marcados en ventas; inventario se acumula en temporada baja; capacidad ociosa en unos meses, insuficiente en otros; estrés de caja estacional.
**Early_Warning_Signals:** Variación de ventas > 50% entre meses; capacidad utilizada < 50% en temporada baja; inventario se duplica en temporada baja; flujo de caja negativo en temporada baja.
**Business_Impact:** Capital inmovilizado; capacidad ociosa; estrés financiero estacional; dificultad para mantener talento; costos de almacenamiento; descuentos para estimular demanda.
**Severity_Level:** Medium
**Metrics_To_Check:** Variación de ventas mensual; % de capacidad utilizada por mes; días de inventario por temporada; flujo de caja por temporada; rentabilidad por temporada.
**Diagnostic_Questions:** ¿La demanda es estacional? ¿Cómo se gestiona la temporada baja? ¿Hay productos contra-cíclicos? ¿La capacidad se ajusta? ¿Hay planificación estacional?
**Recommended_Actions:** Desarrollar productos contra-cíclicos; diversificar líneas de negocio; ajustar capacidad; planificar inventarios por temporada; crear programas de ventas en temporada baja; presupuestar estacionalidad.
**Related_Patterns:** RSK-006, RSK-025, RSK-095, RSK-097, RSK-104

### RSK-097
**Pattern_Name:** Canales de Distribución Ineficaces o Insuficientes
**Category:** Riesgo Comercial
**Description:** La empresa no cuenta con los canales de distribución adecuados para llegar a sus clientes objetivo, o los existentes son ineficaces, limitando su alcance y ventas.
**Typical_Causes:** Falta de análisis de canales; resistencia a nuevos canales (digital); relación conflictiva con distribuidores; canales tradicionales en declive; falta de inversión.
**Observable_Symptoms:** Clientes no encuentran los productos; quejas sobre disponibilidad; canales tradicionales pierden efectividad; canales digitales no desarrollados; distribuidores desmotivados.
**Early_Warning_Signals:** % de cobertura de clientes objetivo < 60%; % de ventas de canales en declive > 50%; sin canal digital; quejas de disponibilidad; distribuidores con baja rotación.
**Business_Impact:** Ventas perdidas; menor cobertura de mercado; dependencia de canales limitados; crecimiento limitado; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** % de cobertura de mercado; % de ventas por canal; efectividad de canales (costo/venta); % de clientes que encuentran el producto; satisfacción de distribuidores.
**Diagnostic_Questions:** ¿Los canales llegan a los clientes objetivo? ¿Hay canales digitales? ¿Los distribuidores son efectivos? ¿Hay conflictos de canal? ¿Se están desarrollando nuevos canales?
**Recommended_Actions:** Evaluar efectividad de canales; desarrollar canales digitales; optimizar mix de canales; capacitar distribuidores; resolver conflictos de canal; invertir en nuevos canales.
**Related_Patterns:** RSK-093, RSK-094, RSK-098, RSK-101, RSK-103

### RSK-098
**Pattern_Name:** Estrategia de Precios y Descuentos no Controlada
**Category:** Riesgo Comercial
**Description:** La empresa aplica descuentos y promociones sin control ni análisis de impacto en rentabilidad, erosionando el margen y creando expectativas de precios bajos permanentes.
**Typical_Causes:** Presión por volumen; falta de política de descuentos; fuerza de ventas con incentivos solo por volumen; clientes negocian descuentos; sin sistema de aprobación.
**Observable_Symptoms:** Descuentos frecuentes y sin criterio; márgenes se erosionan; clientes esperan descuento siempre; precio de venta se acerca al costo; la rentabilidad no acompaña al volumen.
**Early_Warning_Signals:** % de descuento sobre precio de lista > 25%; margen bruto decreciente con volumen creciente; % de ventas con descuento > 60%; sin política de descuentos; descuentos no autorizados.
**Business_Impact:** Márgenes reducidos; rentabilidad baja a pesar de volumen; guerra de precios; desvalorización de la marca; relación clientes basada en precio no en valor.
**Severity_Level:** High
**Metrics_To_Check:** % de descuento promedio; % de ventas con descuento; margen bruto; rentabilidad por cliente; elasticidad precio.
**Diagnostic_Questions:** ¿Hay política de descuentos? ¿Los descuentos se controlan? ¿La rentabilidad se erosiona? ¿Los clientes solo compran con descuento? ¿Los incentivos consideran margen?
**Recommended_Actions:** Establecer política de descuentos; crear matriz de autorización; alinear incentivos con rentabilidad; reducir frecuencia de descuentos; comunicar valor; segmentar clientes por precio.
**Related_Patterns:** RSK-004, RSK-086, RSK-093, RSK-094, RSK-101

### RSK-099
**Pattern_Name:** Fuerza de Ventas Ineficaz
**Category:** Riesgo Comercial
**Description:** La fuerza de ventas no está alcanzando los objetivos comerciales debido a falta de capacitación, incentivos inadecuados, mala gestión o perfil incorrecto.
**Typical_Causes:** Falta de capacitación; incentivos mal diseñados; mala selección de vendedores; falta de liderazgo; herramientas inadecuadas; procesos de venta no definidos.
**Observable_Symptoms:** Metas de ventas no se cumplen; rotación de vendedores alta; falta de disciplina en procesos; vendedores no saben vender el valor; reportes inexactos.
**Early_Warning_Signals:** % de cumplimiento de metas < 70%; rotación de vendedores > 30%; tiempo de capacitación insuficiente; pipeline inexistente; tasa de conversión < promedio sectorial.
**Business_Impact:** Ventas por debajo del potencial; costos de rotación; mala atención al cliente; pérdida de oportunidades; desmotivación del equipo.
**Severity_Level:** High
**Metrics_To_Check:** % de cumplimiento de metas; tasa de conversión; rotación de vendedores; ticket promedio; % de clientes nuevos vs cartera.
**Diagnostic_Questions:** ¿Los vendedores cumplen metas? ¿Hay capacitación? ¿Los incentivos son adecuados? ¿Hay proceso de ventas? ¿La rotación es alta?
**Recommended_Actions:** Capacitar a la fuerza de ventas; rediseñar incentivos; mejorar selección; implementar CRM; definir proceso de ventas; mejorar liderazgo; hacer acompañamiento en campo.
**Related_Patterns:** RSK-093, RSK-094, RSK-098, RSK-100, RSK-103

### RSK-100
**Pattern_Name:** CRM y Gestión de Clientes Deficiente
**Category:** Riesgo Comercial
**Description:** La empresa no utiliza un sistema CRM o lo usa deficientemente, perdiendo oportunidades de seguimiento, ventas cruzadas, retención y conocimiento del cliente.
**Typical_Causes:** Falta de inversión; resistencia al uso; CRM mal implementado; datos no actualizados; procesos no definidos; falta de capacitación.
**Observable_Symptoms:** No hay registro de interacciones con clientes; seguimiento manual; oportunidades se pierden; no se conoce el historial del cliente; ventas cruzadas no existen.
**Early_Warning_Signals:** Sin CRM implementado; % de datos de clientes incompletos > 40%; % de oportunidades registradas < 60%; sin historial de interacciones; sin automatización de seguimiento.
**Business_Impact:** Oportunidades perdidas; mala experiencia del cliente; falta de conocimiento del cliente; imposibilidad de segmentar; ventas cruzadas y upselling no realizados.
**Severity_Level:** Medium
**Metrics_To_Check:** % de datos de clientes completos; % de oportunidades registradas; tasa de conversión; % de ventas cruzadas; satisfacción de usuarios del CRM.
**Diagnostic_Questions:** ¿Hay CRM? ¿Se usa efectivamente? ¿Los datos están actualizados? ¿Se da seguimiento a oportunidades? ¿Se conoce al cliente?
**Recommended_Actions:** Implementar CRM adecuado; capacitar al equipo; definir procesos de uso; mantener datos actualizados; automatizar seguimiento; integrar con otros sistemas.
**Related_Patterns:** RSK-093, RSK-099, RSK-101, RSK-103, RSK-105

### RSK-101
**Pattern_Name:** Marketing y Publicidad Ineficaz
**Category:** Riesgo Comercial
**Description:** La empresa invierte en marketing y publicidad sin medir efectividad, en canales equivocados o con mensajes que no conectan, desperdiciando recursos y generando bajo retorno.
**Typical_Causes:** Falta de estrategia de marketing; sin medición de ROI; canales mal seleccionados; mensajes no diferenciados; ejecución amateur; presupuesto mal asignado.
**Observable_Symptoms:** El marketing no genera leads; costo de adquisición alto; campañas sin resultado medible; mismo presupuesto, menos resultados; la marca no es reconocida.
**Early_Warning_Signals:** CAC (Costo de Adquisición de Clientes) creciente; ROI de marketing < 2x; % de leads de marketing < 20% de ventas; sin métricas de marketing; campañas sin seguimiento.
**Business_Impact:** Recursos desperdiciados; bajo retorno de inversión; dificultad para atraer clientes; crecimiento limitado; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** CAC; ROI de marketing; % de leads de marketing; tasa de conversión de campañas; costo por lead.
**Diagnostic_Questions:** ¿Se mide el ROI de marketing? ¿Las campañas generan resultados? ¿Los canales son adecuados? ¿Hay estrategia de marketing? ¿El CAC es razonable?
**Recommended_Actions:** Definir estrategia de marketing; medir ROI de todas las campañas; optimizar canales; mejorar segmentación; invertir en canales efectivos; capacitar al equipo; usar herramientas de marketing digital.
**Related_Patterns:** RSK-093, RSK-094, RSK-098, RSK-100, RSK-105

### RSK-102
**Pattern_Name:** Obsolescencia de Producto o Servicio
**Category:** Riesgo Comercial
**Description:** El producto o servicio principal de la empresa está perdiendo relevancia en el mercado por cambios tecnológicos, preferencias del consumidor o nuevos competidores.
**Typical_Causes:** Falta de innovación; no inversión en I+D; desconocimiento de tendencias; resistencia a cambiar; producto en etapa de declive del ciclo de vida.
**Observable_Symptoms:** Ventas del producto estrella decrecen; clientes piden nuevas funcionalidades; alternativas en el mercado; producto percibido como anticuado; interés decreciente.
**Early_Warning_Signals:** % de ingresos de productos > 5 años sin cambios > 60%; ventas de producto estrella decreciendo; % de clientes que piden nuevas versiones > 30%; competidores más modernos.
**Business_Impact:** Pérdida de ingresos; participación de mercado decreciente; necesidad de reinventarse; costos de desarrollo de nuevos productos; posible desaparición.
**Severity_Level:** Critical
**Metrics_To_Check:** % de ingresos de productos nuevos; edad promedio de productos; tendencia de ventas por producto; % de productos en etapa de declive; inversión en I+D.
**Diagnostic_Questions:** ¿El producto está perdiendo relevancia? ¿Hay nuevos competidores con mejor oferta? ¿Se invierte en nuevos productos? ¿Los clientes piden cambios? ¿El producto está en etapa de declive?
**Recommended_Actions:** Renovar producto; invertir en I+D; desarrollar nuevos productos; escuchar al cliente; anticipar tendencias; retirar productos en declive; diversificar portafolio.
**Related_Patterns:** RSK-076, RSK-081, RSK-093, RSK-094, RSK-104

### RSK-103
**Pattern_Name:** Mala Experiencia del Cliente en el Proceso de Compra
**Category:** Riesgo Comercial
**Description:** La experiencia del cliente en el proceso de compra (desde la búsqueda hasta la post-venta) es deficiente, generando fricción, abandono y mala percepción de la marca.
**Typical_Causes:** Procesos no centrados en el cliente; falta de capacitación; sistemas poco amigables; políticas rígidas; falta de medición de experiencia.
**Observable_Symptoms:** Clientes abandonan el carrito; proceso de compra confuso; atención al cliente deficiente; quejas sobre el proceso; clientes no completan la compra.
**Early_Warning_Signals:** % de abandono de carrito > 70%; CSAT < 70%; % de clientes que no completan compra; quejas sobre proceso; NPS bajo.
**Business_Impact:** Ventas perdidas; clientes insatisfechos; pérdida de clientes potenciales; mala reputación; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** % de abandono de carrito; CSAT; % de clientes que completan compra; tiempo del proceso de compra; NPS del proceso.
**Diagnostic_Questions:** ¿El proceso de compra es fácil? ¿Hay abandono? ¿Los clientes se quejan del proceso? ¿Se ha medido la experiencia? ¿Hay fricciones?
**Recommended_Actions:** Mapear customer journey; identificar fricciones; simplificar proceso; capacitar al equipo; implementar mejoras basadas en feedback; medir experiencia.
**Related_Patterns:** RSK-065, RSK-069, RSK-093, RSK-097, RSK-100

### RSK-104
**Pattern_Name:** Portafolio de Productos No Diversificado
**Category:** Riesgo Comercial
**Description:** La empresa depende de un número reducido de productos o servicios para la mayoría de sus ingresos, exponiéndola a riesgos si alguno falla o declina.
**Typical_Causes:** Falta de desarrollo de productos; enfoque en producto estrella; recursos limitados; desconocimiento de oportunidades; aversión al riesgo.
**Observable_Symptoms:** Un producto representa > 50% de ingresos; no hay nuevos lanzamientos; portafolio pequeño; vulnerabilidad a cambios en producto principal; concentración de riesgo.
**Early_Warning_Signals:** % de ingresos del principal producto > 50%; número de productos < 5; % de ingresos de productos nuevos < 10%; portafolio no renovado en > 3 años.
**Business_Impact:** Alta vulnerabilidad; crecimiento limitado; riesgo de declive; poder de negociación de clientes reducido; imposibilidad de cross-selling.
**Severity_Level:** High
**Metrics_To_Check:** % de ingresos por producto; número de productos; % de ingresos de productos nuevos; rotación de productos; índice de concentración.
**Diagnostic_Questions:** ¿Hay concentración en pocos productos? ¿Se lanzan nuevos productos? ¿El portafolio es diverso? ¿Qué pasa si el producto principal falla? ¿Hay plan de diversificación?
**Recommended_Actions:** Desarrollar nuevos productos; diversificar portafolio; invertir en I+D; adquirir líneas de producto; retirar productos débiles; equilibrar portafolio.
**Related_Patterns:** RSK-003, RSK-009, RSK-076, RSK-093, RSK-102

### RSK-105
**Pattern_Name:** Estrategia de Post-Venta y Servicio al Cliente Deficiente
**Category:** Riesgo Comercial
**Description:** La empresa no ofrece un servicio post-venta adecuado, generando insatisfacción, pérdida de clientes y oportunidades de ventas adicionales.
**Typical_Causes:** Falta de inversión en servicio; personal no capacitado; procesos no definidos; enfoque solo en venta inicial; ausencia de medición.
**Observable_Symptoms:** Clientes insatisfechos con soporte; quejas post-venta; no hay seguimiento; bajas tasas de recompra; oportunidades de upselling perdidas.
**Early_Warning_Signals:** CSAT post-venta < 60%; % de reclamos post-venta > 20%; tasa de recompra < 20%; tiempo de respuesta a reclamos > 48 horas; sin programa de fidelización.
**Business_Impact:** Pérdida de clientes; baja retención; oportunidades de upselling perdidas; mala reputación; mayor costo de adquisición para reemplazar clientes perdidos.
**Severity_Level:** High
**Metrics_To_Check:** CSAT post-venta; % de reclamos; tasa de recompra; tiempo de respuesta; % de clientes en programa de fidelización.
**Diagnostic_Questions:** ¿Hay servicio post-venta? ¿Los clientes están satisfechos? ¿Hay seguimiento post-venta? ¿Se hace upselling? ¿Hay programa de fidelización?
**Recommended_Actions:** Implementar servicio post-venta estructurado; capacitar al equipo; establecer SLA; crear programa de fidelización; hacer seguimiento proactivo; medir satisfacción.
**Related_Patterns:** RSK-065, RSK-069, RSK-093, RSK-100, RSK-103

## Riesgo Proveedores

### RSK-106
**Pattern_Name:** Dependencia de un Único Proveedor
**Category:** Riesgo Proveedores
**Description:** La empresa depende de un solo proveedor para un insumo, material o servicio crítico, exponiéndose a riesgo de desabastecimiento, aumento de precios o quiebra del proveedor.
**Typical_Causes:** Relación histórica; especialización del proveedor; costo de cambio alto; falta de desarrollo de alternativas; comodidad.
**Observable_Symptoms:** Si el proveedor falla, la producción se detiene; el proveedor aumenta precios sin alternativa; el proveedor impone condiciones; no hay proveedores alternativos calificados.
**Early_Warning_Signals:** % de dependencia de un solo proveedor > 70%; sin alternativas calificadas; tiempo de reemplazo > 1 mes; proveedor con problemas financieros; sin plan de contingencia.
**Business_Impact:** Desabastecimiento; aumento de costos; condiciones desfavorables; parada de producción; pérdida de ventas; vulnerabilidad estratégica.
**Severity_Level:** Critical
**Metrics_To_Check:** % de dependencia del principal proveedor; número de proveedores alternativos; tiempo de reemplazo; % de insumos con un solo proveedor.
**Diagnostic_Questions:** ¿Hay dependencia de un solo proveedor? ¿Hay alternativas? ¿Cuánto tiempo tomaría reemplazarlo? ¿El proveedor tiene problemas? ¿Hay plan de contingencia?
**Recommended_Actions:** Desarrollar proveedores alternativos; mantener stock de seguridad; invertir en calificación de nuevos proveedores; negociar contratos de largo plazo; crear plan de contingencia.
**Related_Patterns:** RSK-062, RSK-107, RSK-108, RSK-109, RSK-112

### RSK-107
**Pattern_Name:** Calidad Inconsistente de Proveedores
**Category:** Riesgo Proveedores
**Description:** Los proveedores entregan insumos o servicios con calidad variable, afectando la calidad del producto final, generando retrabajo, devoluciones y clientes insatisfechos.
**Typical_Causes:** Falta de especificaciones claras; control de calidad insuficiente; proveedores no calificados; criterios de selección débiles; sin evaluación de desempeño.
**Observable_Symptoms:** Insumos con defectos; producto final inconsistente; devoluciones; retrabajo; quejas de clientes por calidad; proveedores no cumplen especificaciones.
**Early_Warning_Signals:** % de insumos rechazados > 5%; % de proveedores con calidad inconsistente > 20%; devoluciones por calidad de insumos crecientes; sin especificaciones documentadas.
**Business_Impact:** Calidad final inconsistente; retrabajo y desperdicios; clientes insatisfechos; devoluciones; costos de inspección; daño reputacional.
**Severity_Level:** High
**Metrics_To_Check:** % de insumos rechazados; % de proveedores con calidad inconsistente; PPM (partes por millón) defectuosas; costo de retrabajo por insumos; quejas de clientes por calidad.
**Diagnostic_Questions:** ¿La calidad de insumos es consistente? ¿Hay especificaciones claras? ¿Se evalúa a los proveedores? ¿Hay controles de calidad? ¿Los proveedores cumplen?
**Recommended_Actions:** Establecer especificaciones claras; implementar control de calidad; calificar proveedores; evaluar desempeño; trabajar con proveedores en mejora; diversificar fuentes.
**Related_Patterns:** RSK-106, RSK-108, RSK-109, RSK-110, RSK-112

### RSK-108
**Pattern_Name:** Riesgo de Desabastecimiento de Insumos Críticos
**Category:** Riesgo Proveedores
**Description:** La empresa enfrenta riesgo de desabastecimiento de insumos críticos por problemas de proveedores, logística, disponibilidad en el mercado o factores externos.
**Typical_Causes:** Proveedor único; falta de stock de seguridad; cadena de suministro global; logística deficiente; insumos escasos; no planificación.
**Observable_Symptoms:** Paradas de producción por falta de insumos; compras de emergencia a altos costos; clientes no atendidos; producción por debajo de capacidad; estrés en compras.
**Early_Warning_Signals:** Días de inventario de insumos críticos < 5; % de insumos con riesgo de desabastecimiento; frecuencia de faltantes; lead time de reposición > lead time de consumo.
**Business_Impact:** Parada de producción; pérdida de ventas; clientes insatisfechos; costos de compras de emergencia; daño reputacional; pérdida de participación de mercado.
**Severity_Level:** Critical
**Metrics_To_Check:** Días de inventario de insumos críticos; % de insumos con riesgo; frecuencia de faltantes; % de compras de emergencia; lead time de reposición.
**Diagnostic_Questions:** ¿Hay riesgo de desabastecimiento? ¿Hay stock de seguridad? ¿Los insumos críticos tienen alternativas? ¿La cadena de suministro es confiable? ¿Hay plan de contingencia?
**Recommended_Actions:** Mantener stock de seguridad de insumos críticos; desarrollar proveedores alternativos; monitorear lead times; mejorar planificación de compras; integrar cadena de suministro.
**Related_Patterns:** RSK-025, RSK-106, RSK-107, RSK-109, RSK-112

### RSK-109
**Pattern_Name:** Incremento de Costos de Insumos
**Category:** Riesgo Proveedores
**Description:** La empresa enfrenta aumentos significativos en los costos de insumos que no puede trasladar a precios, comprimiendo sus márgenes y rentabilidad.
**Typical_Causes:** Inflación de materias primas; dependencia de proveedores con poder de mercado; falta de contratos de precio fijo; commodities volátiles; sin cobertura.
**Observable_Symptoms:** Costos de insumos crecen más que los precios de venta; márgenes se comprimen; proveedores aumentan precios frecuentemente; no se puede trasladar a clientes.
**Early_Warning_Signals:** % de aumento de costos de insumos > inflación; margen bruto decreciente; % de insumos commodities > 40%; sin contratos de precio; sin cobertura de precios.
**Business_Impact:** Márgenes comprimidos; rentabilidad decreciente; necesidad de ajustar precios; pérdida de competitividad; posible pérdida si no se puede trasladar.
**Severity_Level:** High
**Metrics_To_Check:** Variación de costos de insumos; margen bruto; capacidad de trasladar precios; % de insumos con contrato de precio; cobertura de commodities.
**Diagnostic_Questions:** ¿Los costos de insumos están subiendo? ¿Se pueden trasladar a precios? ¿Hay contratos de precio fijo? ¿Se usa cobertura? ¿Los márgenes se comprimen?
**Recommended_Actions:** Negociar contratos de largo plazo con precios; diversificar proveedores; cubrir precios de commodities; buscar sustitutos; mejorar eficiencia para compensar; trasladar a precios.
**Related_Patterns:** RSK-004, RSK-007, RSK-106, RSK-107, RSK-112

### RSK-110
**Pattern_Name:** Proveedores sin Certificaciones o Estándares
**Category:** Riesgo Proveedores
**Description:** La empresa trabaja con proveedores que no cuentan con certificaciones de calidad, seguridad, ambientales o laborales, exponiéndose a riesgos reputacionales y operativos.
**Typical_Causes:** Selección por precio; falta de requisitos; desconocimiento; falta de auditoría; mercado con pocas opciones certificadas.
**Observable_Symptoms:** Proveedores sin ISO; condiciones laborales precarias; impacto ambiental no gestionado; calidad inconsistente; clientes auditores rechazan proveedores.
**Early_Warning_Signals:** % de proveedores certificados < 30%; sin requisitos de certificación; auditorías de clientes rechazan proveedores; incidentes con proveedores no certificados.
**Business_Impact:** Riesgo reputacional; calidad inconsistente; clientes rechazan productos; multas; dificultad para exportar; pérdida de negocios que exigen certificaciones.
**Severity_Level:** High
**Metrics_To_Check:** % de proveedores certificados; % de insumos de proveedores certificados; rechazos de clientes por proveedores; incidentes con proveedores no certificados.
**Diagnostic_Questions:** ¿Los proveedores tienen certificaciones? ¿Se exigen requisitos? ¿Los clientes auditan proveedores? ¿Hay incidentes con no certificados? ¿Hay plan de certificación?
**Recommended_Actions:** Establecer requisitos de certificación; auditar proveedores; apoyar certificación de proveedores clave; evaluar cumplimiento; sustituir proveedores no certificados.
**Related_Patterns:** RSK-107, RSK-108, RSK-111, RSK-112, RSK-113

### RSK-111
**Pattern_Name:** Riesgo de Concentración Geográfica de Proveedores
**Category:** Riesgo Proveedores
**Description:** Los proveedores clave están concentrados en una región geográfica, exponiendo a la empresa a riesgos de desabastecimiento por desastres naturales, conflictos o problemas logísticos regionales.
**Typical_Causes:** Cercanía geográfica; disponibilidad regional; costos logísticos; desconocimiento de riesgo; facilidad de relación.
**Observable_Symptoms:** Dependencia de proveedores de una región; problemas en esa región afectan toda la cadena; sin alternativas de otras regiones; concentración geográfica.
**Early_Warning_Signals:** % de proveedores en una sola región > 60%; sin alternativas de otras regiones; región con riesgo sísmico/climático/político; lead time de otras regiones muy largo.
**Business_Impact:** Desabastecimiento regional; parada de producción; aumento de costos de reposición; vulnerabilidad a desastres; dependencia regional.
**Severity_Level:** High
**Metrics_To_Check:** % de proveedores por región; % de insumos de región principal; tiempo de reemplazo de otras regiones; exposición a riesgos regionales.
**Diagnostic_Questions:** ¿Los proveedores están concentrados geográficamente? ¿Hay alternativas de otras regiones? ¿La región tiene riesgos? ¿Qué pasa si la región tiene problemas?
**Recommended_Actions:** Diversificar geográficamente proveedores; desarrollar proveedores en otras regiones; mantener stock de seguridad; evaluar riesgos geopolíticos; considerar nearshoring.
**Related_Patterns:** RSK-106, RSK-108, RSK-109, RSK-112, RSK-113

### RSK-112
**Pattern_Name:** Gestión de Proveedores No Estructurada
**Category:** Riesgo Proveedores
**Description:** La empresa no tiene un proceso estructurado de gestión de proveedores (selección, evaluación, desarrollo, monitoreo), operando con relaciones no gestionadas que generan riesgos.
**Typical_Causes:** Falta de área de compras; informalidad; cultura de "proveedor de confianza"; recursos limitados; desconocimiento.
**Observable_Symptoms:** Proveedores no evaluados; sin criterios de selección; relaciones informales; problemas recurrentes con proveedores; no hay seguimiento de desempeño.
**Early_Warning_Signals:** Sin base de datos de proveedores; sin evaluación de desempeño; sin criterios de selección; % de proveedores evaluados < 20%; sin contrato formal.
**Business_Impact:** Calidad inconsistente; incumplimiento; sobreprecios; dependencia; riesgos no identificados; falta de trazabilidad.
**Severity_Level:** High
**Metrics_To_Check:** % de proveedores evaluados; % con contrato; % con KPIs; % calificados; rotación de proveedores.
**Diagnostic_Questions:** ¿Hay proceso de gestión de proveedores? ¿Se evalúan? ¿Hay criterios de selección? ¿Se monitorea desempeño? ¿Hay área de compras?
**Recommended_Actions:** Implementar sistema de gestión de proveedores; definir criterios de selección; evaluar periódicamente; segmentar proveedores; desarrollar proveedores clave; formalizar relaciones.
**Related_Patterns:** RSK-106, RSK-107, RSK-108, RSK-110, RSK-113

### RSK-113
**Pattern_Name:** Falta de Plan de Contingencia en Cadena de Suministro
**Category:** Riesgo Proveedores
**Description:** La empresa no tiene planes de contingencia para su cadena de suministro ante interrupciones, dejándola sin respuesta ante crisis de desabastecimiento.
**Typical_Causes:** Falta de planificación; subestimación de riesgos; confianza en proveedores; recursos limitados; no priorización.
**Observable_Symptoms:** Cuando un proveedor falla, no hay plan B; se compra de emergencia al precio que sea; la producción se detiene; no hay alternativas identificadas.
**Early_Warning_Signals:** Sin plan de contingencia; % de insumos con plan B < 30%; tiempo de respuesta ante crisis > 1 semana; mismo proveedor sin alternativa.
**Business_Impact:** Parada de producción; pérdida de ventas; costos de emergencia; daño reputacional; pérdida de clientes.
**Severity_Level:** Critical
**Metrics_To_Check:** % de insumos críticos con plan de contingencia; tiempo de activación del plan; % de cobertura del plan; frecuencia de activación.
**Diagnostic_Questions:** ¿Hay plan de contingencia? ¿Qué pasa si un proveedor crítico falla? ¿Hay alternativas identificadas? ¿Se ha probado el plan? ¿Hay stock de seguridad?
**Recommended_Actions:** Desarrollar plan de contingencia; identificar alternativas; mantener stock de seguridad; probar plan; establecer alertas tempranas; diversificar proveedores.
**Related_Patterns:** RSK-106, RSK-108, RSK-111, RSK-112, RSK-117

### RSK-114
**Pattern_Name:** Riesgo de Proveedores con Problemas Financieros
**Category:** Riesgo Proveedores
**Description:** Proveedores clave presentan problemas financieros que pueden llevar a su quiebra o incumplimiento, afectando la cadena de suministro de la empresa.
**Typical_Causes:** Falta de monitoreo financiero; selección sin análisis; relación de largo plazo sin revisión; proveedor pequeño sin respaldo.
**Observable_Symptoms:** Proveedores solicitan pagos anticipados; retrasos en entregas; calidad decreciente; rumores de problemas; proveedor reduce operaciones.
**Early_Warning_Signals:** Proveedor sin liquidez; solicita pagos anticipados; retrasos frecuentes; calidad decreciente; personal del proveedor se reduce; noticias de problemas.
**Business_Impact:** Desabastecimiento; pérdida de calidad; costos de reemplazo; parada de producción; costos legales; relaciones dañadas.
**Severity_Level:** High
**Metrics_To_Check:** % de proveedores con monitoreo financiero; % de proveedores en riesgo; % de pagos anticipados; retrasos atribuibles a problemas financieros.
**Diagnostic_Questions:** ¿Se monitorea la salud financiera de proveedores? ¿Algún proveedor clave tiene problemas? ¿Solicitan pagos anticipados? ¿Hay retrasos? ¿Hay alternativas?
**Recommended_Actions:** Monitorear salud financiera de proveedores; diversificar; reducir exposición; negociar garantías; establecer alertas; tener alternativas listas.
**Related_Patterns:** RSK-106, RSK-108, RSK-112, RSK-113, RSK-115

### RSK-115
**Pattern_Name:** Incumplimiento de Plazos por Proveedores
**Category:** Riesgo Proveedores
**Description:** Los proveedores no cumplen con los plazos de entrega acordados, afectando la planificación de producción y el cumplimiento con clientes finales.
**Typical_Causes:** Proveedores sin capacidad; logística deficiente; falta de penalidades; procesos no estandarizados; mala planificación del proveedor.
**Observable_Symptoms:** Entregas tardías; producción detenida por falta de insumos; clientes afectados; penalidades por retraso; estrés en planificación.
**Early_Warning_Signals:** % de entregas a tiempo < 85%; retrasos frecuentes de mismos proveedores; impacto en producción; quejas de planificación; sin penalidades en contratos.
**Business_Impact:** Producción retrasada; clientes insatisfechos; penalidades; pérdida de ventas; daño reputacional; costos de urgencia.
**Severity_Level:** High
**Metrics_To_Check:** % de entregas a tiempo; % de proveedores con cumplimiento < 90%; retraso promedio; impacto en producción; penalidades pagadas por proveedores.
**Diagnostic_Questions:** ¿Los proveedores cumplen plazos? ¿Hay retrasos frecuentes? ¿Se penalizan? ¿Se monitorea el cumplimiento? ¿Hay consecuencias?
**Recommended_Actions:** Establecer SLA con penalidades; monitorear cumplimiento; evaluar y calificar; desarrollar proveedores; tener alternativas; mejorar comunicación.
**Related_Patterns:** RSK-106, RSK-108, RSK-112, RSK-113, RSK-116

### RSK-116
**Pattern_Name:** Falta de Trazabilidad en Cadena de Suministro
**Category:** Riesgo Proveedores
**Description:** La empresa no tiene trazabilidad sobre el origen y condiciones de los insumos que compra, exponiéndose a riesgos legales, de calidad y reputacionales.
**Typical_Causes:** Cadena de suministro larga; falta de sistemas; proveedores no colaboran; desconocimiento; ausencia de requisitos.
**Observable_Symptoms:** No se conoce el origen de los insumos; trazabilidad manual; imposibilidad de identificar lotes problemáticos; clientes piden trazabilidad; reclamos no se pueden rastrear.
**Early_Warning_Signals:** Sin sistema de trazabilidad; % de insumos trazables < 50%; tiempo para rastrear un lote > 1 día; clientes exigen trazabilidad; reclamos no rastreables.
**Business_Impact:** Imposibilidad de identificar causas de defectos; reclamos no gestionables; multas regulatorias; pérdida de clientes que exigen trazabilidad; riesgos reputacionales.
**Severity_Level:** High
**Metrics_To_Check:** % de insumos trazables; tiempo de trazabilidad; % de reclamos rastreables; cumplimiento de requisitos de clientes; inversión en trazabilidad.
**Diagnostic_Questions:** ¿Hay trazabilidad? ¿Se puede rastrear el origen de un insumo? ¿Los clientes exigen trazabilidad? ¿Se pueden identificar lotes problemáticos? ¿Hay sistema de trazabilidad?
**Recommended_Actions:** Implementar sistema de trazabilidad; exigir a proveedores; etiquetar lotes; registrar origen; capacitar al equipo; auditar trazabilidad.
**Related_Patterns:** RSK-107, RSK-110, RSK-112, RSK-113, RSK-117

### RSK-117
**Pattern_Name:** Falta de Evaluación de Riesgos en Cadena de Suministro
**Category:** Riesgo Proveedores
**Description:** La empresa no evalúa los riesgos en su cadena de suministro (geopolíticos, climáticos, financieros, operativos), siendo sorprendida por interrupciones evitables.
**Typical_Causes:** Desconocimiento; falta de recursos; cadena simple; no priorización; confianza.
**Observable_Symptoms:** Interrupciones sorpresivas; no se anticipan problemas; impactos no previstos; reacción siempre reactiva; mismos problemas recurrentes.
**Early_Warning_Signals:** Sin evaluación de riesgos; % de riesgos identificados < 30%; interrupciones recurrentes; sin plan de mitigación; matriz de riesgos inexistente.
**Business_Impact:** Interrupciones no anticipadas; costos de emergencia; desabastecimiento; pérdida de clientes; ventajas competitivas perdidas.
**Severity_Level:** High
**Metrics_To_Check:** % de riesgos identificados; % con plan de mitigación; número de interrupciones; tiempo de respuesta; costo de interrupciones/ventas.
**Diagnostic_Questions:** ¿Se evalúan riesgos de cadena? ¿Hay interrupciones recurrentes? ¿Se anticipan problemas? ¿Hay matriz de riesgos? ¿Hay plan de mitigación?
**Recommended_Actions:** Evaluar riesgos de cadena de suministro; crear matriz de riesgos; establecer monitoreo; desarrollar planes de mitigación; revisar periódicamente; diversificar.
**Related_Patterns:** RSK-106, RSK-108, RSK-111, RSK-113, RSK-116

## Riesgo Talento

### RSK-118
**Pattern_Name:** Dificultad para Atraer Talento Clave
**Category:** Riesgo Talento
**Description:** La empresa tiene dificultad para atraer profesionales calificados para posiciones clave, limitando su capacidad de crecimiento, innovación y competitividad.
**Typical_Causes:** Salarios no competitivos; marca empleador débil; ubicación; falta de propuesta de valor; proceso de selección ineficaz; empresas competidoras más atractivas.
**Observable_Symptoms:** Vacantes difíciles de cubrir; candidatos rechazan ofertas; tiempo de contratación largo; candidatos de baja calidad; la empresa no es conocida como empleador.
**Early_Warning_Signals:** Tiempo para cubrir vacantes clave > 90 días; % de ofertas rechazadas > 30%; calidad de candidatos decreciente; sin marca empleador; rotación alta en posiciones difíciles.
**Business_Impact:** Falta de talento clave; crecimiento limitado; sobrecarga de empleados actuales; proyectos retrasados; dependencia de consultores; desventaja competitiva.
**Severity_Level:** Critical
**Metrics_To_Check:** Tiempo para cubrir vacantes; % de ofertas aceptadas; calidad de candidatos; % de vacantes clave cubiertas; satisfacción con contrataciones.
**Diagnostic_Questions:** ¿Es difícil atraer talento? ¿Las ofertas se rechazan? ¿El tiempo de contratación es largo? ¿La empresa es atractiva como empleador? ¿Hay propuesta de valor?
**Recommended_Actions:** Mejorar compensaciones; desarrollar marca empleador; mejorar proceso de selección; ofrecer desarrollo; crear EVP (Employee Value Proposition); flexibilidad laboral.
**Related_Patterns:** RSK-018, RSK-119, RSK-120, RSK-122, RSK-124

### RSK-119
**Pattern_Name:** Rotación de Talento Clave
**Category:** Riesgo Talento
**Description:** La empresa pierde empleados clave (gerentes, técnicos especializados, vendedores estrella) con alta frecuencia, perdiendo conocimiento, relaciones y capacidad operativa.
**Typical_Causes:** Salarios no competitivos; falta de desarrollo; mal clima laboral; liderazgo deficiente; mejores oportunidades externas; falta de reconocimiento.
**Observable_Symptoms:** Empleados clave renuncian; pérdida de conocimiento; clientes se van con empleados; proyectos afectados; curva de aprendizaje constante; desmotivación del equipo.
**Early_Warning_Signals:** Rotación de talento clave > 15%; % de empleados con más de 5 años decreciente; salidas no planificadas; sin entrevistas de salida; pérdida de clientes post-salida.
**Business_Impact:** Pérdida de conocimiento crítico; interrupción operativa; costos de reemplazo; pérdida de clientes; desmotivación del equipo; impacto en resultados.
**Severity_Level:** Critical
**Metrics_To_Check:** Rotación de talento clave; % de retención; antigüedad promedio; costo de rotación; % de salidas voluntarias.
**Diagnostic_Questions:** ¿Hay rotación de talento clave? ¿Por qué se van? ¿Hay plan de retención? ¿Se hace entrevistas de salida? ¿El clima laboral es bueno?
**Recommended_Actions:** Implementar programa de retención; mejorar compensaciones; crear plan de carrera; fortalecer liderazgo; reconocer logros; medir clima laboral; realizar entrevistas de salida.
**Related_Patterns:** RSK-018, RSK-118, RSK-120, RSK-122, RSK-124

### RSK-120
**Pattern_Name:** Clima Laboral Tóxico o Desmotivador
**Category:** Riesgo Talento
**Description:** El clima laboral en la empresa es negativo, con baja moral, conflictos, estrés o desmotivación, afectando productividad, retención y calidad del trabajo.
**Typical_Causes:** Liderazgo autoritario; favoritismo; falta de reconocimiento; comunicación deficiente; carga excesiva de trabajo; conflictos no resueltos.
**Observable_Symptoms:** Baja moral; chismes y rumores; conflictos entre áreas; ausentismo; rotación alta; empleados desmotivados; baja productividad; resistencia al cambio.
**Early_Warning_Signals:** Ausentismo > 5%; rotación > 30%; % de empleados insatisfechos > 30% (encuesta); conflictos frecuentes; quejas formales; absentismo.
**Business_Impact:** Baja productividad; rotación alta; errores; calidad deficiente; dificultad para atraer talento; pérdida de conocimiento; clima negativo afecta resultados.
**Severity_Level:** Critical
**Metrics_To_Check:** Ausentismo; rotación; % de satisfacción laboral; número de conflictos; % de empleados comprometidos; productividad.
**Diagnostic_Questions:** ¿El clima laboral es positivo? ¿Hay conflictos? ¿Los empleados están motivados? ¿Hay reconocimiento? ¿El liderazgo es efectivo?
**Recommended_Actions:** Medir clima laboral; mejorar comunicación; capacitar líderes; resolver conflictos; reconocer logros; promover equilibrio vida-trabajo; crear programa de bienestar.
**Related_Patterns:** RSK-018, RSK-119, RSK-122, RSK-123, RSK-127

### RSK-121
**Pattern_Name:** Falta de Desarrollo y Capacitación del Talento
**Category:** Riesgo Talento
**Description:** La empresa no invierte en capacitación y desarrollo de sus empleados, resultando en habilidades desactualizadas, baja productividad y dificultad para retener talento.
**Typical_Causes:** Falta de presupuesto; enfoque en corto plazo; desconocimiento; cultura de "ya saben"; falta de plan de desarrollo.
**Observable_Symptoms:** Empleados con habilidades desactualizadas; errores por falta de conocimiento; nuevos métodos no se adoptan; empleados estancados; rotación por falta de desarrollo.
**Early_Warning_Signals:** % de empleados capacitados < 30%; inversión en capacitación/ventas < 0.5%; sin plan de desarrollo; % de empleados con habilidades desactualizadas; rotación alta por falta de desarrollo.
**Business_Impact:** Baja productividad; calidad deficiente; incapacidad de adoptar nuevas tecnologías; rotación por estancamiento; desventaja competitiva; dificultad para innovar.
**Severity_Level:** High
**Metrics_To_Check:** Inversión en capacitación/empleado; % de empleados capacitados anualmente; % de habilidades actualizadas; retorno de capacitación; satisfacción con desarrollo.
**Diagnostic_Questions:** ¿Se invierte en capacitación? ¿Hay plan de desarrollo? ¿Las habilidades están actualizadas? ¿Los empleados tienen oportunidades de crecimiento? ¿Hay presupuesto?
**Recommended_Actions:** Crear plan de capacitación anual; presupuestar desarrollo; identificar brechas de habilidades; ofrecer programas de desarrollo; medir efectividad; certificar al personal.
**Related_Patterns:** RSK-118, RSK-119, RSK-122, RSK-124, RSK-127

### RSK-122
**Pattern_Name:** Falta de Plan de Carrera y Crecimiento
**Category:** Riesgo Talento
**Description:** La empresa no ofrece oportunidades claras de crecimiento profesional, generando desmotivación y fuga de talento que busca desarrollo en otras organizaciones.
**Typical_Causes:** Organización plana; falta de políticas de desarrollo; desconocimiento; cultura de "crecer es salir"; gerencia insegura; cortoplacismo.
**Observable_Symptoms:** Empleados no ven futuro; rotación de empleados con potencial; no hay promociones internas; talento joven se va; empleados se estancan.
**Early_Warning_Signals:** % de promociones internas < 20%; % de empleados que ven futuro < 40%; rotación de alto potencial > 20%; antigüedad promedio de empleados que se van < 2 años.
**Business_Impact:** Pérdida de talento con potencial; dificultad para atraer jóvenes; desmotivación; falta de sucesores; estancamiento; dependencia de contratación externa.
**Severity_Level:** High
**Metrics_To_Check:** % de promociones internas; % de empleados con plan de carrera; rotación de alto potencial; % de puestos cubiertos internamente; satisfacción con desarrollo.
**Diagnostic_Questions:** ¿Hay plan de carrera? ¿Se promueve internamente? ¿Los empleados ven futuro? ¿Se retiene talento con potencial? ¿Hay desarrollo profesional?
**Recommended_Actions:** Crear planes de carrera; promover internamente; establecer programas de desarrollo; identificar alto potencial; ofrecer rotación; capacitar gerentes en desarrollo de equipos.
**Related_Patterns:** RSK-118, RSK-119, RSK-121, RSK-124, RSK-127

### RSK-123
**Pattern_Name:** Ausentismo y Presentismo Laboral
**Category:** Riesgo Talento
**Description:** La empresa enfrenta niveles altos de ausentismo (faltas) o presentismo (empleados presentes pero no productivos por salud, desmotivación o estrés), afectando la productividad.
**Typical_Causes:** Clima laboral negativo; estrés; salud ocupacional deficiente; liderazgo pobre; falta de motivación; condiciones laborales duras.
**Observable_Symptoms:** Faltas frecuentes; empleados en el trabajo pero no rinden; bajas por enfermedad; cansancio generalizado; baja productividad a pesar de horario completo.
**Early_Warning_Signals:** Ausentismo > 5%; % de presentismo estimado > 10%; bajas por estrés; rotación alta; clima laboral negativo; productividad decreciente con misma dotación.
**Business_Impact:** Baja productividad; sobrecarga a empleados presentes; costos de reemplazo; calidad inconsistente; clima laboral deteriorado; costos de salud.
**Severity_Level:** High
**Metrics_To_Check:** Tasa de ausentismo; % de presentismo; productividad por empleado; días perdidos por enfermedad; costo de ausentismo.
**Diagnostic_Questions:** ¿Hay ausentismo alto? ¿Los empleados presentes rinden? ¿Hay estrés? ¿Las condiciones laborales son adecuadas? ¿Se mide productividad?
**Recommended_Actions:** Mejorar clima laboral; implementar programa de bienestar; reducir estrés; mejorar condiciones; reconocer logros; flexibilidad laboral; atención a salud mental.
**Related_Patterns:** RSK-120, RSK-121, RSK-122, RSK-125, RSK-127

### RSK-124
**Pattern_Name:** Falta de Plan de Sucesión para Posiciones Críticas
**Category:** Riesgo Talento
**Description:** La empresa no tiene identificados ni desarrollados sucesores para posiciones críticas (gerencia, técnicos especializados), exponiéndose a crisis si el titular se ausenta o renuncia.
**Typical_Causes:** Falta de previsión; creencia de que "nadie es insustituible"; gerencia no prioriza; falta de candidatos; cultura de no compartir conocimiento.
**Observable_Symptoms:** No hay quién reemplace a un gerente si renuncia; posiciones críticas sin respaldo; transiciones traumáticas; nuevo gerente no está preparado.
**Early_Warning_Signals:** % de posiciones críticas con sucesor < 30%; sin programa de desarrollo de sucesores; rotación en posiciones críticas; edad avanzada de titulares; sin plan documentado.
**Business_Impact:** Crisis de sucesión; pérdida de conocimiento; interrupción operativa; pérdida de clientes; conflictos internos; caída de productividad.
**Severity_Level:** Critical
**Metrics_To_Check:** % de posiciones críticas con sucesor; % con plan de desarrollo; tiempo para reemplazar; rotación en posiciones críticas; satisfacción con transiciones.
**Diagnostic_Questions:** ¿Hay sucesores identificados? ¿Se desarrollan? ¿Qué pasa si un gerente renuncia? ¿Hay plan de sucesión? ¿Las posiciones críticas tienen respaldo?
**Recommended_Actions:** Identificar posiciones críticas; desarrollar sucesores; implementar mentoring; documentar conocimiento; establecer plan de sucesión; revisar periódicamente.
**Related_Patterns:** RSK-014, RSK-023, RSK-083, RSK-119, RSK-122

### RSK-125
**Pattern_Name:** Brecha de Habilidades Digitales y Tecnológicas
**Category:** Riesgo Talento
**Description:** La plantilla laboral carece de las habilidades digitales y tecnológicas necesarias para operar eficientemente en el entorno actual, limitando la productividad y la transformación digital.
**Typical_Causes:** Falta de capacitación; perfiles tradicionales; baja atracción de talento digital; resistencia al cambio; inversión insuficiente.
**Observable_Symptoms:** Empleados no saben usar herramientas digitales; procesos manuales por desconocimiento; resistencia a nuevos sistemas; baja adopción de tecnología; errores por falta de habilidades.
**Early_Warning_Signals:** % de empleados con habilidades digitales básicas < 50%; % de adopción de herramientas < 60%; resistencia a cambios tecnológicos; quejas sobre sistemas; brecha de habilidades.
**Business_Impact:** Baja productividad; transformación digital lenta; desventaja competitiva; errores; dependencia de externos; imposibilidad de aprovechar tecnología.
**Severity_Level:** High
**Metrics_To_Check:** % de empleados con habilidades digitales; % de adopción de herramientas; inversión en capacitación digital; productividad digital; satisfacción con herramientas.
**Diagnostic_Questions:** ¿Los empleados tienen habilidades digitales? ¿Se adoptan las herramientas? ¿Hay brecha? ¿Se capacita en habilidades digitales? ¿La transformación digital avanza?
**Recommended_Actions:** Evaluar brecha de habilidades; capacitar en habilidades digitales; contratar talento digital; promover cultura digital; invertir en herramientas; acompañar cambio.
**Related_Patterns:** RSK-055, RSK-057, RSK-061, RSK-121, RSK-127

### RSK-126
**Pattern_Name:** Falta de Diversidad e Inclusión
**Category:** Riesgo Talento
**Description:** La empresa carece de diversidad en su plantilla (género, edad, cultura, experiencia), limitando la innovación, la comprensión de mercados diversos y exponiéndose a riesgos reputacionales.
**Typical_Causes:** Sesgos en selección; cultura homogénea; falta de políticas de inclusión; liderazgo no diverso; desconocimiento de beneficios; sector tradicional.
**Observable_Symptoms:** Equipo homogéneo; falta de perspectivas diversas; dificultad para entender ciertos mercados; quejas de discriminación; ambiente excluyente.
**Early_Warning_Signals:** % de diversidad bajo en todos los niveles; sin política de diversidad; % de denuncias de discriminación; sin metas de inclusión; equipo homogéneo.
**Business_Impact:** Innovación limitada; menor comprensión de clientes diversos; riesgo reputacional; dificultad para atraer talento diverso; posibles demandas; sesgo en decisiones.
**Severity_Level:** Medium
**Metrics_To_Check:** % de diversidad en plantilla; % en gerencia; % de denuncias; existencia de política de inclusión; % de satisfacción de grupos diversos.
**Diagnostic_Questions:** ¿Hay diversidad en el equipo? ¿Hay política de inclusión? ¿Hay sesgos en selección? ¿Se promueve la diversidad? ¿Hay ambiente inclusivo?
**Recommended_Actions:** Implementar política de diversidad; capacitar en sesgos inconscientes; diversificar fuentes de reclutamiento; establecer metas; crear comité de inclusión; medir diversidad.
**Related_Patterns:** RSK-067, RSK-068, RSK-120, RSK-122, RSK-127

### RSK-127
**Pattern_Name:** Estrategia de Compensación No Competitiva
**Category:** Riesgo Talento
**Description:** La estructura de compensación (salarios, beneficios, incentivos) no es competitiva frente al mercado, dificultando la atracción y retención de talento calificado.
**Typical_Causes:** Falta de estudios salariales; cultura de pagar lo mínimo; desconocimiento del mercado; falta de recursos; estructura rígida.
**Observable_Symptoms:** Ofertas rechazadas por salario; rotación hacia competidores que pagan mejor; empleados se quejan del salario; beneficios por debajo del mercado; dificultad para atraer.
**Early_Warning_Signals:** Salarios por debajo del mercado en posiciones clave; % de ofertas rechazadas por salario > 30%; rotación hacia competidores; % de empleados insatisfechos con compensación > 40%.
**Business_Impact:** Dificultad para atraer talento; rotación alta; baja moral; productividad reducida; pérdida de talento clave; desventaja competitiva.
**Severity_Level:** High
**Metrics_To_Check:** Competitividad salarial (% vs mercado); % de ofertas rechazadas; % de empleados satisfechos con compensación; rotación por salario; costo de reposición.
**Diagnostic_Questions:** ¿Los salarios son competitivos? ¿Se rechazan ofertas por salario? ¿Los empleados se van por mejor paga? ¿Hay estudio salarial? ¿Los beneficios son adecuados?
**Recommended_Actions:** Realizar estudio salarial; ajustar compensaciones; mejorar beneficios; implementar incentivos variables; comunicar total compensation; revisar periódicamente.
**Related_Patterns:** RSK-118, RSK-119, RSK-120, RSK-122, RSK-124

### RSK-128
**Pattern_Name:** Conflictos Generacionales y de Cultura Organizacional
**Category:** Riesgo Talento
**Description:** La empresa enfrenta conflictos entre generaciones (Baby Boomers, Gen X, Millennials, Gen Z) o entre culturas (familia vs profesionales, locales vs foráneos) que afectan la cohesión y productividad.
**Typical_Causes:** Falta de integración; comunicación deficiente; diferencias en valores y expectativas; liderazgo no preparado; ausencia de cultura organizacional definida.
**Observable_Symptoms:** Fricción entre empleados de diferentes generaciones; resistencia a nuevas formas de trabajo; quejas sobre "los jóvenes" o "los antiguos"; falta de colaboración; reuniones improductivas.
**Early_Warning_Signals:** Conflictos entre generaciones; % de empleados que sienten que no encajan > 30%; rotación diferenciada por generación; quejas sobre cultura; falta de colaboración.
**Business_Impact:** Baja productividad; rotación; clima laboral negativo; pérdida de talento joven o senior; incapacidad de atraer diversidad generacional; estancamiento.
**Severity_Level:** Medium
**Metrics_To_Check:** % de conflictos generacionales; rotación por generación; % de satisfacción por grupo; % de colaboración intergeneracional; NPS de clima.
**Diagnostic_Questions:** ¿Hay conflictos generacionales? ¿La cultura organizacional está definida? ¿Las generaciones colaboran? ¿Hay integración? ¿El liderazgo gestiona la diversidad?
**Recommended_Actions:** Definir cultura organizacional; fomentar integración; capacitar en liderazgo inclusivo; crear programas de mentoring inverso; celebrar diversidad; comunicar valores compartidos.
**Related_Patterns:** RSK-084, RSK-120, RSK-122, RSK-126, RSK-127
