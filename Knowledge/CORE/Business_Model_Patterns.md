# Business Model Patterns — SME Knowledge Base

> Base de conocimiento para identificar fortalezas, debilidades, dependencias y oportunidades de mejora en modelos de negocio de PyMEs.

---

## Categorías cubiertas

| # | Categoría | Patrones |
|---|-----------|----------|
| 1 | Revenue Streams | 8 |
| 2 | Diversification | 7 |
| 3 | Customer Concentration | 7 |
| 4 | Supplier Dependency | 7 |
| 5 | Scalability | 7 |
| 6 | Differentiation | 8 |
| 7 | Recurrence | 7 |
| 8 | Margins | 7 |
| 9 | Vertical Integration | 6 |
| 10 | Distribution Channels | 6 |
| 11 | Competitive Advantages | 7 |
| 12 | Entry Barriers | 6 |
| 13 | Founder Dependency | 6 |
| 14 | Model Maturity | 6 |
| **Total** | | **95** |

---

## Revenue Streams

### BMP-001
**Pattern_Name:** Single Revenue Stream Dependency
**Category:** Revenue Streams
**Description:** La empresa depende de una única línea de ingresos (un producto, servicio o canal) para >80% de su facturación.
**Observable_Symptoms:** Caídas puntuales en ventas impactan directamente la caja; pánico cuando un cliente grande amenaza con irse; toda la organización gira en torno a un solo producto.
**Early_Warning_Signals:** Intentos fallidos de lanzar nuevos productos; presupuesto de I+D concentrado en una sola línea; más del 70% del revenue viene de una misma categoría.
**Typical_Causes:** Fundador con expertise en un solo rubro; crecimiento orgánico no diversificado; miedo a canibalizar el producto estrella.
**Business_Impact:** Riesgo existencial si el mercado se contrae; vulnerabilidad total ante disrupción tecnológica; poder de negociación nulo con clientes.
**Metrics_To_Check:** % de ingresos del top-1 producto/servicio; correlación revenue total vs revenue producto estrella (R² >0.9 es alerta).
**Diagnostic_Questions:** ¿Qué pasaría si el producto estrella desapareciera mañana? ¿Cuánto tiempo podrías sobrevivir? ¿Qué % de tus ingresos viene de un solo SKU o servicio?
**Recommended_Actions:** Crear un roadmap de diversificación con 3 nuevas líneas en 12 meses; asignar al menos 20% del equipo a innovación fuera del core; usar el producto estrella como funnel hacia servicios complementarios.
**Severity_Level:** Critical
**Related_Patterns:** BMP-002, BMP-011, BMP-096

### BMP-002
**Pattern_Name:** Multiple Low-Margin Revenue Streams
**Category:** Revenue Streams
**Description:** La empresa opera decenas de líneas de ingreso, pero todas con márgenes bajos, generando alta complejidad operativa sin retorno proporcional.
**Observable_Symptoms:** Equipo disperso en demasiados frentes; catálogo extenso pero pocos productos rentables; quejas constantes de \"esto es mucho trabajo para poco margen\".
**Early_Warning_Signals:** Incremento de SKUs sin mejora en rentabilidad agregada; horas hombre consumidas en productos de bajo margen; rotura de stock en lo rentable, sobrestock en lo marginal.
**Typical_Causes:** Mentalidad de \"mientras más vendamos mejor\"; falta de análisis de rentabilidad por línea; incapacidad para decir que no a oportunidades.
**Business_Impact:** Costos operativos ocultos erosionan el margen neto; dificultad para escalar porque la complejidad crece más rápido que el revenue; confusión estratégica.
**Metrics_To_Check:** Margen neto por SKU/línea; % de líneas que aportan <5% del revenue total; ratio ingresos/complejidad operativa.
**Diagnostic_Questions:** ¿Cuántas líneas de producto tienes? ¿Cuántas son realmente rentables después de asignar costos indirectos? ¿Podrías cancelar el 30% de tus SKUs sin perder clientes clave?
**Recommended_Actions:** Realizar ABC costing por línea; eliminar bottom 20% de líneas por rentabilidad; concentrar esfuerzos en las líneas con mejor relación margen-esfuerzo.
**Severity_Level:** High
**Related_Patterns:** BMP-023, BMP-024, BMP-051

### BMP-003
**Pattern_Name:** Passive Income Absence
**Category:** Revenue Streams
**Description:** El modelo de negocio genera ingresos solo cuando el equipo está activamente trabajando (puro \"tiempo por dinero\"), sin componentes pasivos o recurrentes.
**Observable_Symptoms:** Dueño y empleados facturan por hora/día; cuando alguien se enferma no hay ingreso; vacaciones = cero facturación.
**Early_Warning_Signals:** Resistencia a modelos de suscripción o retainer; todos los ingresos son project-based; el equipo está siempre a capacidad máxima.
**Typical_Causes:** Modelo de servicios puros; falta de activos digitales o productos escalables; mentalidad artesanal.
**Business_Impact:** Techo de ingresos bajo (limitado por horas disponibles); valor de reventa de la empresa mínimo; burnout crónico del equipo.
**Metrics_To_Check:** % de ingresos recurrentes o pasivos sobre total; ratio ingresos/empleado; horas facturables vs horas totales.
**Diagnostic_Questions:** ¿Generas dinero mientras duermes? ¿Cuánto vale tu empresa si mañana no trabajas? ¿Qué % de tus ingresos no requiere tu presencia activa?
**Recommended_Actions:** Crear oferta de retainer/suscripción; empaquetar conocimiento en activos digitales (cursos, plantillas, software); identificar servicios recurrentes dentro del portafolio actual.
**Severity_Level:** High
**Related_Patterns:** BMP-034, BMP-035, BMP-036

### BMP-004
**Pattern_Name:** High-Volume Low-Value Trap
**Category:** Revenue Streams
**Description:** La empresa genera grandes volúmenes de transacciones de bajo valor unitario, requiriendo escala masiva para ser rentable.
**Observable_Symptoms:** Grandes equipos de ventas para tickets pequeños; costos de adquisición cercanos al valor de vida del cliente; procesos altamente transaccionales.
**Early_Warning_Signals:** CAC >30% del LTV; alta rotación en equipo comercial por comisiones bajas; clientes que compran una vez y no repiten.
**Typical_Causes:** Competencia por precio; mercado commoditizado; falta de upselling/cross-selling.
**Business_Impact:** Cualquier incremento en costos fijos destruye rentabilidad; difícil invertir en mejora de producto; vulnerabilidad ante nuevos entrantes con mejor tecnología.
**Metrics_To_Check:** Ticket promedio; CAC:LTV ratio; margen neto por transacción; customer churn rate.
**Diagnostic_Questions:** ¿Cuánto gastas para adquirir un cliente vs cuánto te deja? ¿Podrías sobrevivir con la mitad de las transacciones? ¿Tus mejores clientes son los que más compran o los que más valor aportan?
**Recommended_Actions:** Segmentar clientes por valor y crear oferta premium; implementar bundling para incrementar ticket promedio; reducir costos transaccionales vía automatización.
**Severity_Level:** High
**Related_Patterns:** BMP-023, BMP-024, BMP-051

### BMP-005
**Pattern_Name:** Low-Volume High-Value Niche
**Category:** Revenue Streams
**Description:** Modelo con pocas transacciones pero de altísimo valor unitario, generando dependencia de pocos deals grandes.
**Observable_Symptoms:** Ciclos de venta largos (>6 meses); pipeline con pocas oportunidades; ingresos \"montaña rusa\" mes a mes.
**Early_Warning_Signals:** Más de 50% del revenue anual proviene de <5 transacciones; pipeline coverage ratio <3x; deals cerrados concentrados en Q4.
**Typical_Causes:** Mercado de nicho pequeño; producto/servicio de alto costo; modelo de proyecto llave en mano.
**Business_Impact:** Alta volatilidad de ingresos; dificultad para planificar inversiones; presión extrema en el cierre de cada deal.
**Metrics_To_Check:** Número de transacciones anuales; ticket promedio; meses sin cierre de deals; pipeline coverage ratio.
**Diagnostic_Questions:** ¿Cuántos deals cerraste el trimestre pasado? ¿Qué pasa si pierdes los 3 deals más grandes del pipeline? ¿Tu modelo puede sostener 2 meses sin cierres?
**Recommended_Actions:** Crear líneas de menor ticket que generen ingresos más frecuentes; diversificar verticales de nicho; estandarizar parte de la oferta para acortar ciclos de venta.
**Severity_Level:** High
**Related_Patterns:** BMP-001, BMP-011, BMP-012

### BMP-006
**Pattern_Name:** Revenue-Expense Currency Mismatch
**Category:** Revenue Streams
**Description:** La empresa genera ingresos en una moneda (generalmente local) pero tiene costos significativos en otra moneda (USD, EUR), creando riesgo cambiario estructural.
**Observable_Symptoms:** Márgenes que fluctúan sin explicación operativa; pánico cada vez que el tipo de cambio se mueve; planificación financiera imposible a largo plazo.
**Early_Warning_Signals:** Costos de insumos importados >30% de estructura de costos; ingresos 100% en moneda local; contratos de venta sin cláusulas de ajuste cambiario.
**Typical_Causes:** Materia prima importada; deuda en moneda extranjera; software/servicios internacionales; franquicias con regalías en USD.
**Business_Impact:** Márgenes pueden desaparecer de la noche a la mañana por devaluación; desventaja competitiva si competidores tienen costos en moneda local; dificultad para proyectar resultados.
**Metrics_To_Check:** % costos en moneda extranjera; % ingresos en moneda extranjera; exposure cambiaria neta mensual.
**Diagnostic_Questions:** ¿Qué pasa si tu moneda se devalúa 30%? ¿Tus contratos tienen cláusulas de ajuste? ¿Has considerado facturar en USD a clientes locales?
**Recommended_Actions:** Indexar precios a inflación/tipo de cambio; generar ingresos en la misma moneda de los costos; usar instrumentos de cobertura cambiaria; negociar contratos en USD con proveedores locales.
**Severity_Level:** High
**Related_Patterns:** BMP-023, BMP-024, BMP-056

### BMP-007
**Pattern_Name:** Seasonal Revenue Peaks
**Category:** Revenue Streams
**Description:** Los ingresos se concentran en períodos específicos del año (Navidad, temporada escolar, verano, cosecha), con meses de baja o nula facturación.
**Observable_Symptoms:** Contrataciones masivas temporales; flujo de caja negativo 6-8 meses al año; estrés operativo en temporada alta; personal ocioso en temporada baja.
**Early_Warning_Signals:** >60% de ingresos en <4 meses del año; incapacidad para retener talento fuera de temporada; descapitalización recurrente.
**Typical_Causes:** Modelo ligado a estacionalidad natural del mercado; falta de productos/servicios complementarios fuera de temporada; cultura de \"vive el momento\" sin planificación.
**Business_Impact:** Capital de trabajo ineficiente (activos ociosos parte del año); dificultad para retener talento clave; presión de caja en meses bajos.
**Metrics_To_Check:** Porcentaje de ingresos por mes; ratio mes pico / mes valle; costo de mantener capacidad ociosa durante meses bajos.
**Diagnostic_Questions:** ¿Qué haces los 6 meses que no es temporada alta? ¿Tienes reservas de capital para cubrir los meses valle? ¿Puedes crear una línea de negocio contra-cíclica?
**Recommended_Actions:** Desarrollar oferta contra-cíclica; implementar modelo de suscripción con pagos distribuidos; usar temporada alta para financiar innovación fuera de temporada; crear alianzas con negocios de estacionalidad opuesta.
**Severity_Level:** Medium
**Related_Patterns:** BMP-003, BMP-011, BMP-034

### BMP-008
**Pattern_Name:** Phantom Revenue (High Gross, Low Net)
**Category:** Revenue Streams
**Description:** La empresa muestra ingresos brutos altos que impresionan externamente, pero los márgenes netos son extremadamente bajos o negativos.
**Observable_Symptoms:** Dueño orgulloso del \"volumen de ventas\" pero siempre sin dinero; descuentos agresivos para cerrar deals; costos operativos que crecen al mismo ritmo que las ventas.
**Early_Warning_Signals:** Margen neto <5% sostenidamente; revenue creciendo pero ganancias planas o decrecientes; alto % de ingresos destinado a descuentos y devoluciones.
**Typical_Causes:** Guerras de precios en el mercado; estructura de costos fijos alta; falta de diferenciación real; obsesión del fundador con \"ser el más grande\".
**Business_Impact:** Crecimiento no rentable destruye valor; incapacidad para invertir en mejora; quiebra por aumento marginal de costos; empresa no vendible.
**Metrics_To_Check:** Margen neto vs margen bruto; ratio revenue/ganancia neta; costo de descuentos sobre revenue total.
**Diagnostic_Questions:** ¿Cuánto dinero realmente te queda después de todos los gastos? ¿Si dejaras de crecer en volumen, serías más rentable? ¿Tus clientes te elegirían si subieras 10% los precios?
**Recommended_Actions:** Frenar crecimiento no rentable; rediseñar estructura de costos; reposicionar marca hacia valor en lugar de precio; eliminar descuentos que no estén justificados por LTV.
**Severity_Level:** Critical
**Related_Patterns:** BMP-004, BMP-023, BMP-024

### BMP-009
**Pattern_Name:** Grant / Subsidy Dependency
**Category:** Revenue Streams
**Description:** La empresa depende de subsidios, grants o programas gubernamentales para una porción significativa de sus ingresos.
**Observable_Symptoms:** Ingresos atados a calendarios de desembolso público; equipo dedicado a postular a fondos; ansiedad recurrente cuando se acercan cambios de gobierno.
**Early_Warning_Signals:** >30% de ingresos de fuentes no comerciales; rentabilidad negativa sin subsidios; producto/servicio que no tiene demanda real de mercado.
**Typical_Causes:** Modelo de negocio diseñado para captar fondos en lugar de resolver problemas de mercado; sector con alta disponibilidad de subsidios (tech, agricultura, cultura).
**Business_Impact:** Empresa no validada por el mercado; riesgo político y burocrático; distorsión estratégica (innovas para el grant, no para el cliente).
**Metrics_To_Check:** % de ingresos de fuentes no comerciales; rentabilidad sin subsidios; % de tiempo del equipo dedicado a gestión de fondos.
**Diagnostic_Questions:** ¿Tu negocio sobreviviría sin ningún subsidio? ¿Tus clientes pagarían el precio real de tu producto? ¿Estás construyendo negocio o empleo disfrazado?
**Recommended_Actions:** Diversificar hacia ingresos comerciales reales; usar subsidios solo para I+D no recurrente; validar demanda de mercado antes de depender de fondos públicos.
**Severity_Level:** Critical
**Related_Patterns:** BMP-001, BMP-011, BMP-096

---

## Diversification

### BMP-011
**Pattern_Name:** Single-Industry Concentration
**Category:** Diversification
**Description:** La empresa opera en una sola industria o vertical, sin exposición a otros sectores que puedan compensar ciclos económicos.
**Observable_Symptoms:** Cuando al sector le va bien, a la empresa le va bien; cuando al sector le va mal, la empresa sufre desproporcionadamente; todo el vocabulario interno es de una sola industria.
**Early_Warning_Signals:** >90% de ingresos de una sola industria; equipo sin experiencia en otros sectores; red de contactos 100% concentrada en un rubro.
**Typical_Causes:** Fundador con expertise profundo en un sector; éxito temprano que refuerza la especialización; pereza estratégica para explorar nuevos verticales.
**Business_Impact:** Riesgo sistémico (recesión sectorial = quiebra); dependencia de regulaciones específicas; dificultad para pivotear si el sector se disrumpe.
**Metrics_To_Check:** % de ingresos por industria; correlación ingresos empresa vs PIB sectorial; concentración HHI de industrias atendidas.
**Diagnostic_Questions:** ¿Tu negocio depende de la salud de una sola industria? ¿Qué pasaría si esa industria se contrae 30%? ¿Tienes clientes en al menos 3 sectores distintos?
**Recommended_Actions:** Identificar 2 industrias adyacentes donde tu propuesta de valor sea relevante; desarrollar casos de uso específicos para esas industrias; hacer prospección comercial en nuevos verticales.
**Severity_Level:** High
**Related_Patterns:** BMP-001, BMP-012, BMP-096

### BMP-012
**Pattern_Name:** Customer Concentration (Single Client Dependency)
**Category:** Diversification
**Description:** Un solo cliente representa más del 30-40% de los ingresos totales, generando dependencia extrema.
**Observable_Symptoms:** Trato especial al cliente grande; ansiedad antes de cada renovación de contrato; decisiones estratégicas condicionadas por lo que \"quiere el cliente grande\".
**Early_Warning_Signals:** Un cliente supera el 25% de ingresos; solicitudes de ese cliente consumen >30% del tiempo del equipo; el cliente comienza a desarrollar capacidades internas.
**Typical_Causes:** Cuenta ganada temprano que creció mucho; falta de fuerza comercial para diversificar; modelo de negocio construido alrededor de un ancla.
**Business_Impact:** Cliente grande gana poder de negociación extremo (puede bajar precios, exigir más); riesgo existencial si el cliente se va; empresa difícil de vender.
**Metrics_To_Check:** % de ingresos del top-1, top-3 y top-5 clientes; índice Herfindahl de concentración de clientes; % de margen bruto del top cliente vs promedio.
**Diagnostic_Questions:** ¿Qué pasa si tu cliente más grande se va mañana? ¿Cuánto tiempo te llevaría reemplazar ese ingreso? ¿Tu cliente grande lo sabe?
**Recommended_Actions:** Establecer política de no más de 20% por cliente; crear plan de diversificación de cartera; construir relación con múltiples contactos dentro del cliente grande; desarrollar producto que sirva a mercado más amplio.
**Severity_Level:** Critical
**Related_Patterns:** BMP-001, BMP-011, BMP-013

### BMP-013
**Pattern_Name:** Geographic Concentration
**Category:** Diversification
**Description:** Todos los ingresos provienen de una sola región geográfica, ciudad o incluso barrio, sin exposición a otros mercados.
**Observable_Symptoms:** Clientes locales; marca desconocida fuera de la zona; operación 100% presencial en una ubicación.
**Early_Warning_Signals:** Desastres naturales o políticos locales paralizan el negocio; economía local en declive; nuevos competidores locales saturando el mercado.
**Typical_Causes:** Modelo presencial; falta de capacidad logística; miedo a expandirse; producto con demanda muy local.
**Business_Impact:** Riesgo ante crisis local; techo de crecimiento bajo; imposibilidad de aprovechar economías de escala.
**Metrics_To_Check:** % de ingresos por región geográfica; crecimiento del mercado local vs otros mercados; penetración en mercado local vs saturación estimada.
**Diagnostic_Questions:** ¿Podrías vender tu producto en otra ciudad/país? ¿Cuánto mercado total disponible tienes en tu región actual? ¿Qué necesitarías para abrir una segunda ubicación?
**Recommended_Actions:** Desarrollar canal de ventas digital/remoto; probar expansión a una región adyacente con perfil demográfico similar; buscar socios/distribuidores en otras regiones.
**Severity_Level:** High
**Related_Patterns:** BMP-001, BMP-011, BMP-029

### BMP-014
**Pattern_Name:** Adjacent Market White Space
**Category:** Diversification
**Description:** Existen mercados adyacentes claros donde la propuesta de valor actual podría aplicarse, pero la empresa no los ha explorado sistemáticamente.
**Observable_Symptoms:** Rechazo sistemático a oportunidades fuera del core; frases como \"eso no es lo nuestro\"; equipo comercial que solo llama al mismo perfil de cliente.
**Early_Warning_Signals:** Competidores entrando a mercados que podrían ser tuyos; clientes preguntando si ofreces X (que no ofreces); equipo de ventas con quota baja porque mercado core está saturado.
**Typical_Causes:** Visión limitada del fundador; cultura interna aversa al riesgo; falta de proceso de innovación estructurado.
**Business_Impact:** Crecimiento limitado a tasa de mercado core; vulnerabilidad cuando mercado core se contrae; pérdida de oportunidades de first-mover en adyacentes.
**Metrics_To_Check:** % de ingresos fuera del mercado original; número de verticales atendidas; tasa de crecimiento en nuevos segmentos vs core.
**Diagnostic_Questions:** ¿Quién más podría beneficiarse de tu producto/servicio? ¿Qué otras industrias tienen problemas similares? ¿Qué competidores de otros sectores están entrando a tu espacio?
**Recommended_Actions:** Realizar ejercicio de \"jobs to be done\" para identificar mercados adyacentes; asignar 20% de capacidad comercial a prospección en nuevas verticales; crear versión simplificada del producto para entrar a nuevo segmento.
**Severity_Level:** Medium
**Related_Patterns:** BMP-011, BMP-029, BMP-060

### BMP-015
**Pattern_Name:** Over-Diversification (Conglomerate Trap)
**Category:** Diversification
**Description:** La empresa opera en múltiples rubros no relacionados, diluyendo foco, recursos y capacidades.
**Observable_Symptoms:** Equipo pequeño atendiendo negocios muy distintos; fundador cambiando de \"sombrero\" constantemente; dificultad para explicar \"a qué se dedica la empresa\".
**Early_Warning_Signals:** Más de 3 líneas de negocio no relacionadas con menos de 5 personas; inversiones en rubros donde no hay expertise interno; rentabilidad inferior al promedio en cada rubro individual.
**Typical_Causes:** Mentalidad de \"no poner todos los huevos en la misma canasta\" mal entendida; oportunidades que aparecen y se toman sin análisis estratégico; falta de disciplina para decir que no.
**Business_Impact:** Ineficiencia operativa (no hay economía de escala ni aprendizaje compartido); ventaja competitiva débil en cada rubro; dificultad de gestión para el fundador.
**Metrics_To_Check:** Rentabilidad por unidad de negocio; % de ingresos del negocio principal; sinergias reales entre líneas de negocio.
**Diagnostic_Questions:** ¿Tus líneas de negocio comparten clientes, canales o capacidades? ¿En cuántos rubros eres realmente competitivo? ¿Qué línea eliminarías si pudieras?
**Recommended_Actions:** Definir core business y concentrar recursos allí; vender o cerrar líneas no estratégicas sin sinergias; crear unidad de negocio independiente solo si tiene masa crítica.
**Severity_Level:** High
**Related_Patterns:** BMP-002, BMP-011, BMP-049

### BMP-016
**Pattern_Name:** Product Line Cannibalization
**Category:** Diversification
**Description:** Nuevos productos lanzados por la empresa compiten directamente con sus propios productos existentes, sin estrategia de transición.
**Observable_Symptoms:** Equipo comercial confundido sobre qué vender; clientes preguntando diferencias entre productos de la misma empresa; canibalización de ventas del producto estrella.
**Early_Warning_Signals:** Lanzamiento de nuevo producto sin plan de retiro del anterior; dos productos compitiendo por el mismo presupuesto del cliente; inventario del producto antiguo creciendo.
**Typical_Causes:** Falta de roadmap de producto; innovación incremental mal gestionada; renuencia a discontinuar productos legacy.
**Business_Impact:** Dilución de márgenes; confusión de marca en el mercado; costos de mantener productos redundantes.
**Metrics_To_Check:** Tasa de canibalización (ventas perdidas del producto A vs ganadas del B); margen combinado antes y después del lanzamiento.
**Diagnostic_Questions:** ¿Tu nuevo producto le quita ventas a tu producto existente o a la competencia? ¿Tienes una estrategia clara de transición para clientes de productos anteriores? ¿Sabes cuándo retirar un producto?
**Recommended_Actions:** Definir segmentos de mercado distintos para cada producto; planificar sunset de productos legacy antes de lanzar reemplazo; entrenar al equipo comercial en diferenciación de propuestas.
**Severity_Level:** Medium
**Related_Patterns:** BMP-002, BMP-049, BMP-052

### BMP-017
**Pattern_Name:** Long Tail Absence
**Category:** Diversification
**Description:** La empresa solo vende productos/servicios populares (blockbusters), ignorando el potencial de ingresos agregados de productos de nicho de baja rotación pero alto margen.
**Observable_Symptoms:** Catálogo pequeño enfocado en hits; clientes buscando variedad que la empresa no ofrece; inventario limitado a lo que \"vende mucho\".
**Early_Warning_Signals:** Clientes recurren a competidores para necesidades complementarias; rotación de inventario baja en productos de alto margen; quejas de \"no encontré lo que buscaba\".
**Typical_Causes:** Modelo minorista tradicional; miedo a inventario de baja rotación; falta de plataforma digital para ofrecer catálogo extenso.
**Business_Impact:** Pérdida de ventas complementarias; ticket promedio menor al potencial; posición competitiva débil frente a marketplaces.
**Metrics_To_Check:** % de ingresos de productos de baja rotación; ticket promedio; tasa de cumplimiento de búsquedas de clientes.
**Diagnostic_Questions:** ¿Cuántos productos de nicho podrías ofrecer sin incrementar significativamente tus costos? ¿Qué buscan tus clientes que no encuentren en tu catálogo? ¿Tienes la capacidad de ofrecer variedad sin inventario?
**Recommended_Actions:** Implementar modelo de marketplace/drop-shipping para productos de nicho; usar datos de búsqueda de clientes para expandir catálogo; crear plataforma que permita a terceros ofrecer variedad.
**Severity_Level:** Medium
**Related_Patterns:** BMP-002, BMP-029, BMP-030

### BMP-018
**Pattern_Name:** Customer-Channel Concentration
**Category:** Diversification
**Description:** Dependencia excesiva de un solo canal de adquisición de clientes (Google Ads, Instagram, un solo vendedor, una referencia).
**Observable_Symptoms:** Pánico cuando el costo del canal sube; equipo comercial dependiente de una sola fuente de leads; algoritmo del canal controla el destino del negocio.
**Early_Warning_Signals:** >60% de leads nuevos vienen de un solo canal; CAC del canal principal aumentando consistentemente; cambios en política del canal afectan directamente las ventas.
**Typical_Causes:** Éxito temprano en un canal que genera pereza para explorar otros; falta de expertise en marketing multicanal; presupuesto limitado para testar nuevos canales.
**Business_Impact:** Riesgo alto si el canal cambia algoritmo o política; poder de negociación del canal sobre la empresa; vulnerabilidad si el canal desaparece.
**Metrics_To_Check:** % de nuevos clientes por canal; CAC por canal; concentración HHI de canales; tendencia de CAC en cada canal.
**Diagnostic_Questions:** ¿Qué pasaría si tu principal canal de adquisición dejara de funcionar mañana? ¿Cuántos canales distintos te generan al menos 10% de leads cada uno? ¿Has probado al menos 3 canales nuevos en el último año?
**Recommended_Actions:** Implementar estrategia de canales múltiples con meta de no más de 40% por canal; asignar presupuesto para testar nuevos canales cada trimestre; construir canales orgánicos (SEO, referidos, contenido) como contrapeso.
**Severity_Level:** High
**Related_Patterns:** BMP-001, BMP-012, BMP-028
---

## Customer Concentration

### BMP-019
**Pattern_Name:** Single Buyer Dominance
**Category:** Customer Concentration
**Description:** Patrón extremo de concentración donde un solo comprador representa >50% de los ingresos, ejerciendo poder de monopsonio.
**Observable_Symptoms:** El cliente grande impone condiciones, plazos y precios; la empresa acepta márgenes negativos \"para mantener la cuenta\"; el cliente grande tiene acceso a información financiera de la empresa.
**Early_Warning_Signals:** Cliente solicita auditorías constantes; exige descuentos crecientes; comienza a desarrollar capacidades internas para reemplazar a la empresa.
**Typical_Causes:** Contrato ancla firmado en los inicios; sector con alta concentración de compradores (retail, gobierno, automotriz); falta de fuerza comercial para diversificar.
**Business_Impact:** El cliente grande controla efectivamente el negocio; margen comprimido al mínimo; riesgo existencial si el cliente se integra verticalmente o cambia de proveedor.
**Metrics_To_Check:** % de ingresos y margen del top cliente; % de capacidad productiva dedicada al top cliente; duración promedio de contratos.
**Diagnostic_Questions:** ¿Tu cliente más grande sabe que es indispensable para ti? ¿Has rechazado oportunidades por no poder servir a ese cliente? ¿Cuánto de tu margen sacrificas por retenerlo?
**Recommended_Actions:** Diversificar cartera agresivamente (meta: <25% en 18 meses); diversificar contactos dentro del cliente para no depender de una sola persona; construir producto/servicio que reduzca el poder de negociación del comprador.
**Severity_Level:** Critical
**Related_Patterns:** BMP-012, BMP-020, BMP-096

### BMP-020
**Pattern_Name:** Mass-Market Vanilla Customers
**Category:** Customer Concentration
**Description:** Base de clientes amplia pero sin segmentación: todos son tratados igual, sin diferenciación por valor, necesidades o comportamiento.
**Observable_Symptoms:** Precio único para todos; comunicación genérica; mismo nivel de servicio para el cliente que compra una vez que para el que compra mensualmente.
**Early_Warning_Signals:** Clientes grandes insatisfechos porque reciben el mismo trato que los pequeños; clientes pequeños subsidiados por la atención a todos; tasa de conversión de cliente regular a cliente premium muy baja.
**Typical_Causes:** Falta de CRM y segmentación; mentalidad de \"todos los clientes son iguales\"; equipo pequeño sin capacidad de personalización.
**Business_Impact:** Sub-optimización de rentabilidad (clientes de alto valor no explotados, clientes de bajo valor consumen recursos); dificultad para retener clientes estratégicos; marca posicionada como genérica.
**Metrics_To_Check:** % de ingresos por segmento de clientes; margen neto por segmento; tasa de retención diferenciada por segmento.
**Diagnostic_Questions:** ¿Tus clientes más rentables reciben un trato diferente? ¿Sabes cuánto vale cada cliente individualmente? ¿Podrías identificar tu top 20% de clientes sin mirar una lista?
**Recommended_Actions:** Implementar segmentación basada en valor (LTV, frecuencia, margen); crear niveles de servicio diferenciados; desarrollar programa de clientes estratégicos con atención dedicada.
**Severity_Level:** Medium
**Related_Patterns:** BMP-012, BMP-024, BMP-051

### BMP-021
**Pattern_Name:** Narrow Target Market
**Category:** Customer Concentration
**Description:** Segmento de clientes extremadamente específico y pequeño, limitando severamente el mercado total disponible.
**Observable_Symptoms:** Todos los clientes se conocen entre sí; mercado geográfico muy pequeño; crecimiento estancado porque \"ya no hay más clientes\".
**Early_Warning_Signals:** Tasa de penetración de mercado >40%; prospección comercial ya no encuentra nuevos leads; facturación plana por más de 2 años.
**Typical_Causes:** Nicho demasiado específico; producto diseñado para un perfil muy concreto; falta de adaptabilidad para servir segmentos adyacentes.
**Business_Impact:** Techo de crecimiento duro; inversión en marketing con retornos decrecientes; vulnerabilidad si el nicho se contrae.
**Metrics_To_Check:** TAM, SAM, SOM; tasa de penetración actual; crecimiento del mercado objetivo vs crecimiento de la empresa.
**Diagnostic_Questions:** ¿Cuántos clientes potenciales quedan en tu mercado actual? ¿Podrías servir a un segmento más amplio con ajustes menores? ¿Tu producto resuelve un problema que solo existe en tu nicho?
**Recommended_Actions:** Identificar segmentos adyacentes con necesidades similares; ajustar propuesta de valor para mercados más amplios; desarrollar versión genérica del producto.
**Severity_Level:** High
**Related_Patterns:** BMP-005, BMP-011, BMP-014

### BMP-022
**Pattern_Name:** High-Churn Customer Base
**Category:** Customer Concentration
**Description:** La empresa pierde clientes a una tasa alta (>20-30% anual) y debe reemplazarlos constantemente solo para mantener el ingreso.
**Observable_Symptoms:** Equipo de ventas siempre \"llenando el balde roto\"; esfuerzo comercial enfocado en nuevos clientes sin trabajar retención; clientes que se van sin dar feedback.
**Early_Warning_Signals:** Tasa de churn >15% anual; ratio customer lifetime shortening; NPS bajo o en declive; número de clientes estable pero esfuerzo comercial creciente.
**Typical_Causes:** Producto/servicio con baja adherencia; falta de engagement post-venta; competidores ofreciendo mejor propuesta; onboarding deficiente.
**Business_Impact:** CAC alto (recuperación lenta); crecimiento requiere inversión desproporcionada en marketing; base de clientes inestable; baja rentabilidad a largo plazo.
**Metrics_To_Check:** Churn rate mensual/anual; LTV; ratio LTV:CAC; tiempo promedio de retención; NPS.
**Diagnostic_Questions:** ¿Cuánto tiempo en promedio un cliente se queda contigo? ¿Sabes por qué se van los clientes? ¿Cuánto inviertes en retención vs adquisición?
**Recommended_Actions:** Implementar programa de onboarding robusto; crear hitos de engagement en los primeros 90 días; establecer sistema de detección temprana de churn (uso, quejas, pagos); mejorar experiencia post-venta.
**Severity_Level:** High
**Related_Patterns:** BMP-035, BMP-036, BMP-037

### BMP-023
**Pattern_Name:** Low-Income Customer Base
**Category:** Customer Concentration
**Description:** La empresa atiende predominantemente a clientes de bajo poder adquisitivo, con alta sensibilidad al precio y baja lealtad.
**Observable_Symptoms:** Quejas constantes por precio; clientes que se van por diferencias mínimas; tickets promedio muy bajos; alta rotación de clientes.
**Early_Warning_Signals:** Elasticidad precio de la demanda >1.5; churn alto correlacionado con pequeños aumentos de precio; dificultad para aumentar precios sin perder clientes.
**Typical_Causes:** Posicionamiento en segmento low-cost no intencional; falta de oferta para segmentos más altos; entrada al mercado por precio.
**Business_Impact:** Márgenes estrechos y comprimidos; poca lealtad de cliente; dificultad para invertir en mejora; cliente no perdona errores.
**Metrics_To_Check:** Ticket promedio; elasticidad precio; margen neto; tasa de churn ante cambios de precio.
**Diagnostic_Questions:** ¿Tus clientes te elegirían si fueras 20% más caro? ¿Puedes segmentar tu oferta para atender también a clientes de mayor poder adquisitivo? ¿Estás compitiendo por precio o por valor?
**Recommended_Actions:** Crear línea premium o versión mejorada del producto; segmentar oferta por nivel de servicio; educar al mercado sobre valor en lugar de precio.
**Severity_Level:** High
**Related_Patterns:** BMP-004, BMP-022, BMP-024

### BMP-024
**Pattern_Name:** Unprofitable Customer Segment
**Category:** Customer Concentration
**Description:** Un segmento significativo de clientes (>20%) no es rentable después de asignar todos los costos, pero la empresa no lo identifica ni actúa.
**Observable_Symptoms:** Equipo ocupado atendiendo clientes que dejan poco margen; quejas de \"clientes difíciles\"; recursos consumidos en cuentas pequeñas.
**Early_Warning_Signals:** Costo de servicio > margen bruto para ciertos clientes; horas de soporte desproporcionadas para ingresos generados; clientes que compran con descuentos profundos.
**Typical_Causes:** Falta de costeo por cliente; miedo a perder volumen (aunque no rentable); política de \"el cliente siempre tiene razón\" sin límites.
**Business_Impact:** Subvención cruzada de clientes no rentables por los rentables; distorsión en asignación de recursos; rentabilidad general baja por arrastre.
**Metrics_To_Check:** Margen neto por cliente/segmento; costo de servicio como % del ingreso por cliente; Pareto de rentabilidad (80/20).
**Diagnostic_Questions:** ¿Sabes exactamente qué clientes te generan pérdidas? ¿Has calculado el costo total de servir a cada segmento? ¿Estás dispuesto a perder clientes no rentables?
**Recommended_Actions:** Implementar costeo por cliente (activity-based costing); establecer precio mínimo o volumen mínimo para servicio; redirigir clientes no rentables a canales de bajo costo o descontinuar relación; renegociar condiciones.
**Severity_Level:** High
**Related_Patterns:** BMP-008, BMP-020, BMP-023

### BMP-025
**Pattern_Name:** Missing Recurring Revenue from Existing Customers
**Category:** Customer Concentration
**Description:** La empresa tiene una base de clientes establecida pero no extrae ingresos recurrentes de ella (venta única, sin post-venta, sin consumibles).
**Observable_Symptoms:** Cliente compra una vez y no se vuelve a saber; no hay oferta de mantención, consumibles o suscripción; esfuerzo comercial siempre en buscar nuevos clientes.
**Early_Warning_Signals:** Bajo ratio de ingresos post-venta / venta inicial; clientes comprando consumibles o servicios complementarios de la competencia; sin programa de post-venta.
**Typical_Causes:** Modelo de negocio transaccional puro; falta de producto/servicio post-venta; cultura de \"vender y olvidar\".
**Business_Impact:** LTV bajo; CAC alto porque hay que reponer clientes constantemente; base de clientes sub-monetizada.
**Metrics_To_Check:** % de clientes que repiten compra; ingresos recurrentes como % del total; ratio de ingresos post-venta / venta inicial.
**Diagnostic_Questions:** ¿Qué podría comprar un cliente después de su primera compra? ¿Tienes consumibles, mantenimiento o actualizaciones para ofrecer? ¿Tus clientes le compran a la competencia después de comprarte a ti?
**Recommended_Actions:** Identificar necesidades post-venta del cliente; crear oferta de consumibles, mantenimiento o suscripción; implementar programa de fidelización con beneficios escalonados.
**Severity_Level:** Medium
**Related_Patterns:** BMP-003, BMP-034, BMP-036
---

## Supplier Dependency

### BMP-026
**Pattern_Name:** Single Supplier Dependency
**Category:** Supplier Dependency
**Description:** La empresa depende de un solo proveedor para un insumo crítico, sin alternativas viables a corto plazo.
**Observable_Symptoms:** Pánico cuando el proveedor tiene problemas; el proveedor dicta plazos, precios y condiciones; no hay producto si el proveedor no entrega.
**Early_Warning_Signals:** Proveedor único para un insumo sin sustituto; concentración de compras >70% en un proveedor; proveedor con problemas financieros o laborales conocidos.
**Typical_Causes:** Insumo altamente especializado; relación de largo plazo que generó dependencia; costo de cambio de proveedor muy alto; pereza para calificar alternativas.
**Business_Impact:** Riesgo de desabastecimiento total; proveedor puede subir precios unilateralmente; empresa no tiene poder de negociación.
**Metrics_To_Check:** % de compras concentradas en top-1 proveedor; lead time del proveedor; inventario de seguridad en días; % de insumos críticos con un solo proveedor.
**Diagnostic_Questions:** ¿Qué pasa si tu proveedor principal cierra mañana? ¿Cuánto tiempo puedes operar sin su insumo? ¿Has calificado proveedores alternativos recientemente?
**Recommended_Actions:** Calificar al menos 2 proveedores alternativos; mantener inventario de seguridad equivalente a 60-90 días; desarrollar capacidad interna parcial del insumo crítico.
**Severity_Level:** Critical
**Related_Patterns:** BMP-027, BMP-028, BMP-100

### BMP-027
**Pattern_Name:** Supplier Oligopoly Exposure
**Category:** Supplier Dependency
**Description:** El mercado de proveedores está concentrado en pocos actores, limitando severamente las opciones de abastecimiento.
**Observable_Symptoms:** Mismos precios entre proveedores (colusión tácita); condiciones de pago uniformes; imposibilidad de negociar.
**Early_Warning_Signals:** Los 3 principales proveedores representan >90% del mercado; aumentos de precio sincronizados; condiciones estandarizadas sin excepción.
**Typical_Causes:** Barreras de entrada altas en la industria proveedora; insumo commoditizado controlado por pocos; integración vertical en la cadena.
**Business_Impact:** Costos difíciles de reducir; traslado de aumentos a clientes puede ser inviable; presión sobre márgenes estructural.
**Metrics_To_Check:** HHI del mercado de proveedores; % de aumento de precios de proveedores vs inflación; % de insumos en mercado oligopólico.
**Diagnostic_Questions:** ¿Cuántos proveedores realmente diferentes puedes elegir? ¿Los proveedores coordinan precios entre sí? ¿Podrías fabricar tú mismo el insumo?
**Recommended_Actions:** Explorar integración vertical hacia atrás; desarrollar proveedores alternativos; estandarizar especificaciones para ampliar base de proveedores.
**Severity_Level:** High
**Related_Patterns:** BMP-026, BMP-040, BMP-041

### BMP-028
**Pattern_Name:** Supplier-to-Customer Role Overlap
**Category:** Supplier Dependency
**Description:** Un proveedor clave es también competidor o cliente, creando conflictos de interés y dependencia estratégica peligrosa.
**Observable_Symptoms:** Información sensible compartida con un actor que podría competirte; decisiones limitadas por lo que pensará el proveedor.
**Early_Warning_Signals:** Proveedor comienza a ofrecer productos/servicios similares a los tuyos; proveedor adquiere a competidores; solicitudes de información más allá de lo necesario.
**Typical_Causes:** Cadena de valor con integración parcial; ecosistema donde los roles no están claramente definidos.
**Business_Impact:** Riesgo de apropiación de conocimiento; limitaciones estratégicas auto-impuestas; posible corte de suministro si te conviertes en amenaza.
**Metrics_To_Check:** % de insumos de proveedores competidores; % de ventas a clientes competidores; overlap de actividades en la cadena de valor.
**Diagnostic_Questions:** ¿Tu proveedor podría reemplazarte en el mercado? ¿Qué información sensible compartes con él? ¿Tienes alternativas si decide competirte directamente?
**Recommended_Actions:** Reducir dependencia de proveedores competidores; blindar información estratégica; acelerar desarrollo de capacidades internas o proveedores alternativos.
**Severity_Level:** Critical
**Related_Patterns:** BMP-026, BMP-040, BMP-041

### BMP-029
**Pattern_Name:** Geographic Supplier Concentration
**Category:** Supplier Dependency
**Description:** Los proveedores clave están concentrados en una región geográfica, exponiendo la cadena a riesgos geopolíticos.
**Observable_Symptoms:** Ansiedad ante noticias de la región proveedora; disrupción recurrente por eventos climáticos, políticos o logísticos; lead times largos e impredecibles.
**Early_Warning_Signals:** >50% de insumos críticos de una sola región; proveedores en países con riesgo político alto; dependencia de rutas logísticas únicas.
**Typical_Causes:** Insumo solo disponible en ciertas regiones; relación histórica con proveedores de un país; costos más bajos en esa región.
**Business_Impact:** Riesgo de desabastecimiento por eventos fuera de control; aumento de costos logísticos imprevistos; necesidad de inventarios de seguridad más altos.
**Metrics_To_Check:** Concentración geográfica de proveedores; lead time promedio y desviación estándar; % de insumos de regiones de alto riesgo.
**Diagnostic_Questions:** ¿Qué pasa si el puerto principal se cierra? ¿Tienes proveedores alternativos en otras regiones? ¿Tu inventario cubre disrupciones de 3 meses?
**Recommended_Actions:** Diversificar geográficamente base de proveedores; mantener inventario de seguridad equivalente a lead time máximo histórico + 30 días; evaluar nearshoring.
**Severity_Level:** High
**Related_Patterns:** BMP-026, BMP-030, BMP-100

### BMP-030
**Pattern_Name:** Just-in-Time Over-Optimization
**Category:** Supplier Dependency
**Description:** La empresa optimizó tanto su inventario (JIT) que no tiene margen ante cualquier disrupción en la cadena de suministro.
**Observable_Symptoms:** Cero inventario de seguridad; pánico si un camión se retrasa 24 horas; producción paralizada por falta de un componente menor.
**Early_Warning_Signals:** Rotación de inventario extremadamente alta; proveedores con lead times ajustados al mínimo; quejas recurrentes de casi nos quedamos sin stock.
**Typical_Causes:** Cultura de eficiencia extrema; presión financiera para liberar capital de trabajo; falta de experiencia en gestión de riesgos.
**Business_Impact:** Cualquier disrupción menor para la producción; costo de apagar y encender producción; pérdida de ventas por falta de inventario.
**Metrics_To_Check:** Días de inventario; rotación de inventario; frecuencia de quiebres de stock; horas de producción perdidas por falta de insumos.
**Diagnostic_Questions:** ¿Cuántos días de inventario de seguridad tienes para tu insumo más crítico? ¿Cuándo fue la última vez que tuviste un quiebre de stock?
**Recommended_Actions:** Calcular nivel óptimo de inventario de seguridad basado en variabilidad de demanda y lead time; identificar insumos críticos y mantener stock mínimo.
**Severity_Level:** High
**Related_Patterns:** BMP-026, BMP-029, BMP-100

### BMP-031
**Pattern_Name:** Supplier Captive Relationship
**Category:** Supplier Dependency
**Description:** La empresa está atada a un proveedor por contratos lock-in, inversiones compartidas o integración técnica que hace prohibitivo el cambio.
**Observable_Symptoms:** Imposibilidad de cambiar de proveedor aunque su calidad/precio empeore; sistemas propietarios que solo funcionan con ese proveedor.
**Early_Warning_Signals:** Contratos con cláusulas de exclusividad o penalidades por salida; inversiones específicas para la relación; dependencia técnica (formatos, APIs propietarios).
**Typical_Causes:** Contratos mal negociados en etapas tempranas; inversiones en activos específicos para la relación; integración técnica profunda.
**Business_Impact:** Proveedor puede degradar calidad o subir precios sin consecuencias; empresa pierde poder de negociación; imposibilidad de aprovechar mejores ofertas.
**Metrics_To_Check:** Costo de cambio de proveedor estimado; duración restante de contratos lock-in; % de insumos sujetos a exclusividad.
**Diagnostic_Questions:** ¿Cuánto te costaría cambiar de proveedor? ¿Tus contratos te permiten cambiar? ¿El proveedor sabe que estás atrapado?
**Recommended_Actions:** Negociar cláusulas de salida en próximas renovaciones; desarrollar capacidades técnicas internas para reducir dependencia; mantener opciones abiertas.
**Severity_Level:** High
**Related_Patterns:** BMP-026, BMP-040, BMP-041

### BMP-032
**Pattern_Name:** Supplier Bankruptcy Contagion Risk
**Category:** Supplier Dependency
**Description:** Proveedores clave tienen salud financiera frágil, poniendo en riesgo la continuidad del negocio si ellos quiebran.
**Observable_Symptoms:** Proveedores pidiendo adelantos de pago; disculpas recurrentes por retrasos; calidad inconsistente; rumores de problemas financieros.
**Early_Warning_Signals:** Proveedores con problemas de liquidez; concentración en proveedores pequeños sin respaldo; aumento de precios injustificado.
**Typical_Causes:** Dependencia de proveedores pequeños o financieramente débiles; falta de monitoreo de salud financiera de proveedores.
**Business_Impact:** Quiebra de proveedor puede paralizar la producción; costo y tiempo para calificar nuevos proveedores; posible efecto dominó.
**Metrics_To_Check:** Score de salud financiera de top-5 proveedores; % de proveedores con más de 60 días de atraso en sus propios pagos.
**Diagnostic_Questions:** ¿Conoces la salud financiera de tus proveedores clave? ¿Qué pasaría si tu principal proveedor quiebra? ¿Tienes alternativos ya calificados?
**Recommended_Actions:** Monitorear indicadores financieros básicos de proveedores críticos; mantener siempre un proveedor alternativo calificado; diversificar volumen.
**Severity_Level:** High
**Related_Patterns:** BMP-026, BMP-029, BMP-100
---

## Scalability

### BMP-033
**Pattern_Name:** Founder-as-Bottleneck
**Category:** Scalability
**Description:** El fundador es el cuello de botella central: todo pasa por él/ella, limitando severamente la capacidad de crecimiento.
**Observable_Symptoms:** Fundador trabajando 14+ horas diarias; decisiones de todo nivel escalan al fundador; equipo espera instrucciones para todo; vacaciones del fundador = operación en pausa.
**Early_Warning_Signals:** Fundador involucrado en decisiones operativas del día a día; equipo sin autonomía para decisiones menores; tareas se acumulan cuando el fundador está en reuniones.
**Typical_Causes:** Dificultad para delegar; perfeccionismo; falta de procesos documentados; miedo a perder control; equipo no capacitado para tomar decisiones.
**Business_Impact:** Techo de crecimiento = capacidad personal del fundador; riesgo de burnout; empresa no escalable ni vendible; rotación de talento por falta de autonomía.
**Metrics_To_Check:** % de decisiones que requieren aprobación del fundador; horas trabajadas por el fundador vs equipo; tiempo de respuesta del fundador a solicitudes.
**Diagnostic_Questions:** ¿Podrías tomarte 2 semanas de vacaciones sin que el negocio se resienta? ¿Cuántas decisiones toma tu equipo sin consultarte?
**Recommended_Actions:** Documentar procesos críticos; implementar reuniones de delegación semanales; establecer reglas claras de autonomía por monto y tipo de decisión; contratar COO.
**Severity_Level:** Critical
**Related_Patterns:** BMP-078, BMP-079, BMP-080

### BMP-034
**Pattern_Name:** Non-Scalable Service Model
**Category:** Scalability
**Description:** El modelo de negocio requiere presencia física o tiempo del equipo para cada unidad de valor entregada, limitando drásticamente la escala.
**Observable_Symptoms:** Cada nuevo cliente requiere más personas; ingresos crecen linealmente con headcount; no hay componentes digitales o automatizados.
**Early_Warning_Signals:** Ratio revenue/empleado estancado o decreciente; competidores digitalizando servicios similares; dificultad para encontrar personal calificado.
**Typical_Causes:** Modelo de servicios puros (consultoría, talleres, mantención presencial); falta de inversión en tecnología; producto no estandarizado.
**Business_Impact:** Crecimiento limitado por capacidad de contratación; márgenes decrecen con el tiempo; empresa no atractiva para inversores.
**Metrics_To_Check:** Revenue por empleado; margen neto por empleado; ratio ingresos digitales vs presenciales.
**Diagnostic_Questions:** ¿Cuánto crecerían tus ingresos si duplicaras tu equipo? ¿Hay partes de tu servicio que podrías automatizar o digitalizar?
**Recommended_Actions:** Identificar componentes del servicio que pueden estandarizarse o automatizarse; crear versión digital o remota del servicio; desarrollar modelo de capacitación a clientes (train-the-trainer) para escalar.
**Severity_Level:** High
**Related_Patterns:** BMP-003, BMP-010, BMP-036

### BMP-035
**Pattern_Name:** Low Marginal Scalability (Diseconomies of Scale)
**Category:** Scalability
**Description:** Al crecer, los costos marginales aumentan en lugar de disminuir, haciendo que la empresa sea menos rentable a mayor escala.
**Observable_Symptoms:** Márgenes que se comprimen al crecer; costos de operación que crecen más rápido que los ingresos; necesidad de más supervisión por cada nuevo empleado.
**Early_Warning_Signals:** Margen neto decreciente en períodos de crecimiento de ingresos; costos operativos creciendo como % de revenue; burocracia interna aumentando.
**Typical_Causes:** Modelo de negocio con alta componente de servicio personalizado; falta de inversión en sistemas y procesos; cultura que requiere supervisión constante.
**Business_Impact:** Crecimiento destruye valor en lugar de crearlo; empresa cada vez más difícil de gestionar; eventual techo de rentabilidad.
**Metrics_To_Check:** Margen neto histórico vs revenue; ratio gastos operativos / ingresos; costo de coordinación por empleado.
**Diagnostic_Questions:** ¿Tu empresa es más rentable ahora que cuando era la mitad del tamaño? ¿Cada nuevo empleado incrementa o reduce el margen?
**Recommended_Actions:** Invertir en sistemas y automatización antes de crecer; revisar estructura de costos fijos vs variables; simplificar operaciones antes de escalar.
**Severity_Level:** Critical
**Related_Patterns:** BMP-033, BMP-034, BMP-051

### BMP-036
**Pattern_Name:** Unbundling Opportunity
**Category:** Scalability
**Description:** La empresa ofrece sus servicios solo como paquete completo, cuando podría escalar desagregando componentes y ofreciéndolos como productos autónomos.
**Observable_Symptoms:** Clientes preguntando por solo una parte del servicio; cotizaciones personalizadas constantemente; producto percibido como caro porque incluye componentes no deseados.
**Early_Warning_Signals:** Competidores ofreciendo partes específicas del servicio más baratas; clientes que contratan y no usan partes del servicio; solicitudes de versión básica.
**Typical_Causes:** Estrategia de bundling histórica; falta de análisis de necesidades segmentadas; comodidad de ofrecer una sola opción.
**Business_Impact:** Pérdida de clientes que quieren solo una parte; percepción de precio alto; oportunidades de ingresos desagregados no explotadas.
**Metrics_To_Check:** % de clientes que usan todas las funcionalidades; NPS por componente; ingresos potenciales de unbundling estimados.
**Diagnostic_Questions:** ¿Qué partes de tu oferta podrían venderse por separado? ¿Hay clientes que se van porque no quieren pagar por lo que no usan?
**Recommended_Actions:** Identificar módulos independientes dentro de la oferta actual; crear paquete básico, estándar y premium; probar venta de componentes individuales.
**Severity_Level:** Medium
**Related_Patterns:** BMP-003, BMP-010, BMP-025

### BMP-037
**Pattern_Name:** Process-Dependent Scaling Limit
**Category:** Scalability
**Description:** La empresa opera con procesos altamente dependientes de personas clave (no documentados, no sistematizados), impidiendo escalar.
**Observable_Symptoms:** Cuando una persona se va, el proceso se rompe; solo Juan sabe hacer eso; onboarding lento porque no hay manuales.
**Early_Warning_Signals:** Ausencia de documentación de procesos; funciones críticas con una sola persona backup; tiempo de training de nuevos empleados excesivo.
**Typical_Causes:** Crecimiento acelerado sin inversión en procesos; cultura artesanal; subestimación de la importancia de sistemas.
**Business_Impact:** Riesgo alto de perder capacidades clave; incapacidad para crecer porque no se puede replicar el conocimiento; calidad inconsistente.
**Metrics_To_Check:** % de procesos documentados; bus factor (cuántas personas pueden irse antes de que el negocio pare); tiempo de onboarding.
**Diagnostic_Questions:** ¿Si una persona clave renuncia hoy, cuánto afecta al negocio? ¿Tienes documentados tus procesos críticos? ¿Cuánto tarda un nuevo empleado en ser productivo?
**Recommended_Actions:** Documentar procesos críticos (SOPs) en formato ejecutable; implementar sistema de gestión de conocimiento; asegurar que cada función crítica tenga al menos 2 personas capacitadas.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-080, BMP-081

### BMP-038
**Pattern_Name:** Technology-Underinvestment Ceiling
**Category:** Scalability
**Description:** La empresa no invierte en tecnología/automatización en la medida necesaria, manteniendo procesos manuales que limitan la escala.
**Observable_Symptoms:** Tareas manuales repetitivas que consumen horas del equipo; hojas de cálculo como sistema central; procesos que no se actualizan hace años.
**Early_Warning_Signals:** La tecnología actual es >5 años obsoleta; % de gasto en tecnología <2% de ingresos; equipo pidiendo herramientas modernas sin respuesta.
**Typical_Causes:** Falta de visión tecnológica del fundador; priorización de gastos operativos sobre inversión; miedo a implementar tecnología porque siempre funcionó así.
**Business_Impact:** Límite de escala por capacidad manual; costos operativos más altos que competidores tecnificados; desventaja competitiva creciente.
**Metrics_To_Check:** Gasto en tecnología como % de ingresos; % de procesos automatizados; horas hombre dedicadas a tareas automatizables.
**Diagnostic_Questions:** ¿Cuánto tiempo pierde tu equipo en tareas que una máquina podría hacer? ¿Tus competidores usan tecnología que tú no?
**Recommended_Actions:** Hacer auditoría de procesos automatizables; presupuestar al menos 3-5% de ingresos para tecnología; implementar ERP/CRM moderno como base.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-037, BMP-051

### BMP-039
**Pattern_Name:** Scaling-Without-Systems Trap
**Category:** Scalability
**Description:** La empresa crece en ingresos y personas pero no invierte en sistemas de gestión, control y coordinación, generando caos operativo.
**Observable_Symptoms:** Reuniones interminables de coordinación; errores operativos frecuentes; nadie sabe quién hace qué; información clave se pierde en cadenas de WhatsApp/email.
**Early_Warning_Signals:** Crecimiento de ingresos >20% sin inversión en sistemas; quejas de empleados sobre falta de claridad; retrabajo constante.
**Typical_Causes:** Fundador enfocado solo en ventas; cultura de moverse rápido sin contrapeso operativo; subestimación de la complejidad de coordinación.
**Business_Impact:** Caos operativo que frena el crecimiento; calidad del producto/servicio se degrada; rotación de empleados por frustración; errores costosos.
**Metrics_To_Check:** % de tiempo del equipo en reuniones de coordinación; frecuencia de errores operativos; eNPS.
**Diagnostic_Questions:** ¿Tu equipo sabe exactamente qué hacer cada día? ¿Cuánto tiempo se pierde buscando información? ¿Los errores operativos aumentaron en el último año?
**Recommended_Actions:** Implementar sistema de gestión (OKRs, reuniones estructuradas); adoptar herramientas de gestión de proyectos; establecer procesos de coordinación explícitos.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-037, BMP-038
---

## Differentiation

### BMP-040
**Pattern_Name:** Commodity Trap
**Category:** Differentiation
**Description:** El producto/servicio es percibido como indistinguible de los competidores, compitiendo exclusivamente por precio.
**Observable_Symptoms:** Clientes dicen es lo mismo que el de la competencia; guerras de precio constantes; margen comprimido; marca no es factor de decisión.
**Early_Warning_Signals:** Elasticidad precio de la demanda >2; clientes cambian de proveedor por diferencias mínimas de precio; % de decisiones basadas en precio >80%.
**Typical_Causes:** Producto sin características distintivas; falta de innovación; mercado maduro con estándares establecidos.
**Business_Impact:** Márgenes mínimos o negativos; nula lealtad de clientes; imposibilidad de invertir en mejora; empresa prescindible.
**Metrics_To_Check:** Diferencia de precio con competidores; elasticidad precio; margen neto vs industria; share of voice vs share of market.
**Diagnostic_Questions:** ¿Por qué un cliente te elegiría si fueras 10% más caro? ¿Qué perdería un cliente si dejaras de existir? ¿Puedes nombrar 3 razones no-precio por las que te compran?
**Recommended_Actions:** Identificar atributos de valor no-precio (servicio, garantía, conveniencia, estatus); reposicionar marca alrededor de diferenciación real; especializarse en un nicho.
**Severity_Level:** Critical
**Related_Patterns:** BMP-042, BMP-047, BMP-051

### BMP-041
**Pattern_Name:** Me-Too Product
**Category:** Differentiation
**Description:** La empresa lanzó un producto/servicio que es copia de lo que ya existe, sin ofrecer ventaja sustancial para el cliente.
**Observable_Symptoms:** Discurso de ventas lleno de somos como X pero...; comparaciones constantes con competidores; dificultad para cerrar ventas.
**Early_Warning_Signals:** Tiempo de ciclo de venta largo para ser commodity; tasa de conversión baja; clientes no perciben diferencia significativa.
**Typical_Causes:** Estrategia de fast follower sin ejecución excelente; falta de investigación de mercado; entrada a mercado saturado sin ventaja clara.
**Business_Impact:** Lucha constante por participación de mercado; márgenes bajos; alta tasa de fracaso; inversión desperdiciada.
**Metrics_To_Check:** Tasa de conversión vs industria; tiempo de ciclo de venta; cuota de mercado vs inversión.
**Diagnostic_Questions:** ¿Qué haces mejor que tus competidores? ¿Puedes probarlo? ¿Un cliente percibiría la diferencia en 30 segundos?
**Recommended_Actions:** Detener inversión en marketing hasta definir diferenciación clara; pivotear hacia un nicho desatendido; innovar en al menos un atributo significativo.
**Severity_Level:** High
**Related_Patterns:** BMP-040, BMP-042, BMP-047

### BMP-042
**Pattern_Name:** Hidden Differentiation
**Category:** Differentiation
**Description:** La empresa tiene ventajas competitivas reales pero no sabe comunicarlas ni capitalizarlas comercialmente.
**Observable_Symptoms:** Equipo de ventas no sabe qué decir; propuesta de valor genérica en el sitio web; clientes descubren ventajas después de comprar.
**Early_Warning_Signals:** Testimonios de clientes mencionan atributos que la empresa no promociona; equipo de ventas usa argumentos distintos entre sí; marketing no refleja fortalezas reales.
**Typical_Causes:** Falta de introspección estratégica; equipo técnico que asume que las ventajas son obvias; no se ha preguntado a los clientes por qué compran.
**Business_Impact:** Ventas por debajo del potencial; desventaja frente a competidores que comunican mejor; precio menor al que el mercado pagaría.
**Metrics_To_Check:** Propuesta de valor vs razones reales de compra; consistencia del discurso de ventas; % de clientes que mencionan diferenciación como razón de compra.
**Diagnostic_Questions:** ¿Por qué tus mejores clientes te compran a ti y no a la competencia? ¿Qué dicen de ti cuando te recomiendan? ¿Tu sitio web comunica lo único que ofreces?
**Recommended_Actions:** Entrevistar a top-10 clientes preguntando por qué compran; documentar las 3 ventajas competitivas reales; rediseñar propuesta de valor alrededor de esas ventajas.
**Severity_Level:** Medium
**Related_Patterns:** BMP-040, BMP-047, BMP-049

### BMP-043
**Pattern_Name:** Premium Positioning Without Premium Substance
**Category:** Differentiation
**Description:** La empresa se posiciona como premium (precios altos) pero no ofrece experiencia, calidad o servicio que justifique el precio.
**Observable_Symptoms:** Clientes que se quejan de caro; tasa de cierre baja para precio alto; reseñas negativas sobre relación precio/valor; devoluciones frecuentes.
**Early_Warning_Signals:** Precios >20% sobre el promedio del mercado sin diferenciación tangible; NPS bajo a pesar de margen alto; clientes premium potenciales no convierten.
**Typical_Causes:** Confundir precio alto con posicionamiento premium; falta de inversión en atributos que justifican el precio; producto no alineado con la promesa.
**Business_Impact:** Reputación de caro sin justificación; clientes premium buscan alternativas; atrapados en tierra de nadie (ni baratos, ni realmente premium).
**Metrics_To_Check:** Price premium vs competidores; NPS por segmento; tasa de conversión; tasa de devolución/quejas.
**Diagnostic_Questions:** ¿Qué recibe un cliente premium que no recibe uno estándar? ¿Tu calidad, servicio y experiencia justifican tu precio?
**Recommended_Actions:** Alinear la experiencia completa con el precio (garantía, servicio, packaging, atención); o bajar precios; o invertir en atributos para justificar el premium.
**Severity_Level:** High
**Related_Patterns:** BMP-040, BMP-042, BMP-051

### BMP-044
**Pattern_Name:** Feature Bloat
**Category:** Differentiation
**Description:** El producto acumula decenas de características que pocos clientes usan, complicando la propuesta de valor y aumentando costos.
**Observable_Symptoms:** Producto complejo de usar; onboarding largo; funcionalidades que nadie pide; equipo de desarrollo dedicado a mantener features legacy.
**Early_Warning_Signals:** <20% de las features generan >80% del uso; solicitudes de simplificación de clientes; tiempo de desarrollo para nuevas features aumentando.
**Typical_Causes:** Feature creep por escuchar a todos los clientes; falta de criterio para decir que no; competidores añadiendo funcionalidades.
**Business_Impact:** Costos de desarrollo y mantenimiento elevados; producto percibido como complicado; experiencia de usuario deficiente.
**Metrics_To_Check:** % de features usadas por cliente promedio; % de features con <5% adopción; costo de mantenimiento de features legacy.
**Diagnostic_Questions:** ¿Cuántas de tus funcionalidades realmente usan tus clientes? ¿Podrías eliminar el 30% de las features sin perder clientes?
**Recommended_Actions:** Realizar análisis de uso de features; establecer sunset policy para funcionalidades con baja adopción; simplificar producto alrededor del core value proposition.
**Severity_Level:** Medium
**Related_Patterns:** BMP-040, BMP-049, BMP-052

### BMP-045
**Pattern_Name:** Innovation Plateau
**Category:** Differentiation
**Description:** La empresa no ha lanzado ninguna innovación significativa en los últimos 2-3 años.
**Observable_Symptoms:** Misma oferta que hace 3 años; clientes preguntando qué hay de nuevo; competidores lanzando cosas que la empresa no tiene.
**Early_Warning_Signals:** % de ingresos de productos lanzados en los últimos 2 años <10%; presupuesto de I+D <2% de ingresos; ausencia de roadmap de innovación.
**Typical_Causes:** Conformismo del fundador; falta de inversión en I+D; cultura de si funciona no lo toques; equipo sin tiempo dedicado a innovación.
**Business_Impact:** Pérdida gradual de relevancia; competidores más innovadores ganan participación; eventual commoditización.
**Metrics_To_Check:** % de ingresos de nuevos productos; años desde el último lanzamiento significativo; gasto en I+D como % de ingresos.
**Diagnostic_Questions:** ¿Cuándo fue la última vez que lanzaste algo realmente nuevo? ¿Tus competidores están innovando más que tú?
**Recommended_Actions:** Crear fondo de innovación (5-10% de utilidades); implementar 20% time para experimentación; establecer proceso de innovación continua con métricas.
**Severity_Level:** High
**Related_Patterns:** BMP-040, BMP-041, BMP-060

### BMP-046
**Pattern_Name:** Expertise Undervaluation
**Category:** Differentiation
**Description:** La empresa tiene conocimiento técnico profundo o propiedad intelectual valiosa pero no la capitaliza como ventaja competitiva.
**Observable_Symptoms:** Expertos técnicos haciendo trabajo operativo; conocimiento valioso que no se cobra; competidores replicando know-how.
**Early_Warning_Signals:** Empresa cobra precios de commodity teniendo expertise único; know-how no está protegido (patentes, secretos); empleados clave se llevan conocimiento.
**Typical_Causes:** Fundador técnico que no valora su conocimiento; falta de cultura de propiedad intelectual; enfoque en ejecución sobre estrategia.
**Business_Impact:** Dejar dinero sobre la mesa; competidores se apropian del conocimiento; empresa no captura el valor de su diferenciación real.
**Metrics_To_Check:** Precio promedio vs benchmark de expertise comparable; % de ingresos de servicios de alto valor agregado; número de activos de PI registrados.
**Diagnostic_Questions:** ¿Qué sabe tu empresa que nadie más sabe? ¿Estás cobrando por ese conocimiento? ¿Tu PI está protegida?
**Recommended_Actions:** Identificar y documentar conocimiento diferenciador; patentar o proteger secretos industriales; crear línea de consultoría/asesoría basada en expertise.
**Severity_Level:** Medium
**Related_Patterns:** BMP-010, BMP-042, BMP-047

### BMP-047
**Pattern_Name:** Unclear Value Proposition
**Category:** Differentiation
**Description:** La empresa no tiene una propuesta de valor clara y concisa: no se entiende qué problema resuelve, para quién y por qué es mejor.
**Observable_Symptoms:** Discurso de elevator pitch confuso; sitio web genérico; visitantes no entienden qué hace la empresa en <5 segundos; equipo de ventas da explicaciones distintas.
**Early_Warning_Signals:** Tasa de conversión de sitio web baja; leads calificados no cierran; inversión en marketing sin retorno; clientes preguntan qué hacen exactamente.
**Typical_Causes:** Falta de proceso de definición estratégica; querer ser todo para todos; equipo que no ha hecho el ejercicio de sintetizar la propuesta de valor.
**Business_Impact:** Esfuerzo de marketing inefectivo; ventas toman más tiempo; precio no refleja valor; clientes no recomiendan porque no saben explicar qué hace la empresa.
**Metrics_To_Check:** Tiempo que toma explicar qué hace la empresa; tasa de conversión site-to-lead; consistencia del pitch entre miembros del equipo.
**Diagnostic_Questions:** ¿Puedes explicar qué hace tu empresa en 10 palabras? ¿Tus empleados dan la misma respuesta? ¿Un cliente potencial entiende tu valor en los primeros 5 segundos de tu sitio web?
**Recommended_Actions:** Realizar ejercicio de Value Proposition Canvas; definir propuesta de valor en una oración (<15 palabras); probar la propuesta con 10 personas ajenas al negocio.
**Severity_Level:** High
**Related_Patterns:** BMP-040, BMP-042, BMP-049
---

## Recurrence

### BMP-048
**Pattern_Name:** Pure Transactional Model
**Category:** Recurrence
**Description:** El modelo de ingresos es 100% transaccional (cada venta es independiente), sin elementos de recurrencia ni retención estructural.
**Observable_Symptoms:** Cada mes hay que volver a empezar en ventas; ingresos impredecibles; equipo comercial ansioso al final de cada mes.
**Early_Warning_Signals:** Ingresos del mes siguiente nunca están asegurados; esfuerzo de ventas constante e igual cada mes; clientes que no tienen razón para volver.
**Typical_Causes:** Producto/servicio de compra única; falta de modelo de suscripción; industry practice sin recurrencia.
**Business_Impact:** Pronóstico de ingresos difícil; CAC alto porque hay que reemplazar clientes; valor de la empresa bajo (múltiplos más bajos); estrés financiero recurrente.
**Metrics_To_Check:** % de ingresos recurrentes; ratio de repetición de compra; customer lifetime; ingresos de clientes existentes vs nuevos.
**Diagnostic_Questions:** ¿Tus clientes tienen una razón para comprarte todos los meses? ¿Podrías convertir una compra única en una suscripción?
**Recommended_Actions:** Convertir producto en servicio (suscripción); crear programa de membresía con beneficios recurrentes; implementar modelo de consumibles/recargas.
**Severity_Level:** High
**Related_Patterns:** BMP-003, BMP-025, BMP-034

### BMP-049
**Pattern_Name:** Subscription Model Without Engagement
**Category:** Recurrence
**Description:** Tienen ingresos recurrentes (suscripción), pero los clientes no usan activamente el servicio, generando riesgo de churn latente.
**Observable_Symptoms:** Altos registros pero baja activación; clientes que pagan pero no usan; churn que aparece sin razón aparente; NPS de usuarios inactivos es bajo.
**Early_Warning_Signals:** Ratio de activación (registro a primer uso) <40%; clientes que no logran en >30 días; correlación entre inactividad y churn futuro.
**Typical_Causes:** Onboarding deficiente; producto con valor no evidente; suscripción que se vende pero no se integra en la rutina del cliente.
**Business_Impact:** Churn alto a los 3-6 meses; ingresos recurrentes frágiles; esfuerzo constante en adquirir nuevos suscriptores.
**Metrics_To_Check:** Tasa de activación; días hasta el primer valor (time-to-value); % de suscriptores activos semanalmente; churn rate por cohorte.
**Diagnostic_Questions:** ¿Tus suscriptores realmente usan tu producto? ¿Cuándo fue la última vez que un cliente inactivo te dijo por qué no usa el servicio?
**Recommended_Actions:** Rediseñar onboarding para asegurar primer valor en <7 días; implementar campañas de re-engagement automatizadas; crear programa de customer success preventivo.
**Severity_Level:** High
**Related_Patterns:** BMP-022, BMP-036, BMP-048

### BMP-050
**Pattern_Name:** Lock-In Absence
**Category:** Recurrence
**Description:** No existen mecanismos de lock-in o switching costs para retener clientes, facilitando que se vayan a la competencia.
**Observable_Symptoms:** Clientes que se van sin previo aviso; facilidad con que los clientes prueban competidores; esfuerzo constante en retención.
**Early_Warning_Signals:** Bajo costo de cambio para el cliente; clientes que trabajan con múltiples proveedores simultáneamente; procesos de salida simples.
**Typical_Causes:** Producto/servicio estandarizado; falta de integración con sistemas del cliente; no hay datos históricos valiosos retenidos.
**Business_Impact:** Churn más alto; necesidad de invertir constantemente en adquisición; menor LTV; competidores pueden robar clientes fácilmente.
**Metrics_To_Check:** Costo de cambio estimado para el cliente; churn rate; % de clientes con múltiples proveedores; duración promedio de relación.
**Diagnostic_Questions:** ¿Qué tan fácil es para un cliente dejar tu servicio? ¿Qué perdería si se fuera? ¿Tus clientes usan también a la competencia?
**Recommended_Actions:** Crear switching costs no predatorios: datos históricos, configuraciones personalizadas, integraciones técnicas; implementar programa de fidelización.
**Severity_Level:** Medium
**Related_Patterns:** BMP-022, BMP-025, BMP-048

### BMP-051
**Pattern_Name:** Margin Erosion Due to Lack of Recurrence
**Category:** Recurrence
**Description:** La ausencia de ingresos recurrentes fuerza a la empresa a invertir constantemente en adquisición de clientes, erosionando márgenes.
**Observable_Symptoms:** CAC alto como % del LTV; equipo comercial grande para el tamaño de la empresa; gastos de marketing que consumen el margen.
**Early_Warning_Signals:** CAC/LTV ratio >30%; gastos de ventas creciendo más rápido que revenue; rentabilidad neta baja a pesar de márgenes brutos saludables.
**Typical_Causes:** Modelo transaccional que requiere reposición constante de clientes; falta de retención programática; inversión en adquisición sin optimización.
**Business_Impact:** Márgenes netos comprimidos; empresa no genera efectivo para invertir; crecimiento depende enteramente de inversión en marketing.
**Metrics_To_Check:** CAC; LTV; ratio LTV/CAC; % de ingresos destinado a adquisición; margen neto.
**Diagnostic_Questions:** ¿Cuánto gastas para adquirir un cliente y cuánto te deja en total? ¿Si dejaras de invertir en marketing, cuánto durarían tus ingresos?
**Recommended_Actions:** Implementar estrategias de retención para incrementar LTV; reducir CAC optimizando canales; aumentar ingresos de clientes existentes (upsell, cross-sell).
**Severity_Level:** High
**Related_Patterns:** BMP-022, BMP-023, BMP-048

### BMP-052
**Pattern_Name:** Recurrence Without Margin Expansion
**Category:** Recurrence
**Description:** La empresa tiene ingresos recurrentes, pero los costos de servir a esos clientes recurrentes no disminuyen con el tiempo.
**Observable_Symptoms:** Clientes de larga data tienen costos de servicio similares a los nuevos; no hay automatización en la entrega.
**Early_Warning_Signals:** Margen de clientes con >2 años similar al de clientes nuevos; costo de servicio como % del ingreso no mejora.
**Typical_Causes:** Producto/servicio que requiere intervención constante; falta de inversión en self-service y automatización.
**Business_Impact:** Márgenes no mejoran con el tiempo; beneficios de la recurrencia no se materializan.
**Metrics_To_Check:** Margen neto por antigüedad de cliente; costo de servicio como % del ingreso por cohorte; % de interacciones automatizadas vs manuales.
**Diagnostic_Questions:** ¿Tus clientes más antiguos son más rentables que los nuevos? ¿El costo de servir a un cliente disminuye con el tiempo?
**Recommended_Actions:** Invertir en automatización de entrega de servicio; implementar portales de autoservicio para clientes; diseñar producto para menos intervención humana.
**Severity_Level:** Medium
**Related_Patterns:** BMP-034, BMP-035, BMP-051

### BMP-053
**Pattern_Name:** Negative Churn Capability Missing
**Category:** Recurrence
**Description:** La empresa no tiene mecanismos para que los clientes existentes aumenten su gasto (expansion revenue), perdiendo el principal beneficio de la recurrencia.
**Observable_Symptoms:** Ingresos de clientes existentes planos mes a mes; sin upsell, cross-sell ni aumento de precio; el crecimiento depende solo de nuevos clientes.
**Early_Warning_Signals:** Revenue expansion rate <5% anual; LTV plano; equipo de ventas enfocado solo en nuevos clientes.
**Typical_Causes:** Modelo de precio fijo sin niveles; falta de productos complementarios; equipo sin incentivos para expansion revenue.
**Business_Impact:** Crecimiento más lento; LTV sub-óptimo; CAC no se diluye en una base creciente de ingresos.
**Metrics_To_Check:** Net Revenue Retention (NRR); Expansion Revenue como % de ingresos recurrentes; % de clientes que upsellan anualmente.
**Diagnostic_Questions:** ¿Tus clientes existentes gastan más contigo con el tiempo? ¿Tienes niveles de precio o productos adicionales para ofrecerles?
**Recommended_Actions:** Crear tiers de pricing con valor creciente; desarrollar productos/servicios complementarios; implementar programa de expansion revenue con métricas claras.
**Severity_Level:** Medium
**Related_Patterns:** BMP-025, BMP-048, BMP-049

### BMP-054
**Pattern_Name:** Recurring Revenue as Illusion
**Category:** Recurrence
**Description:** La empresa clasifica ingresos como recurrentes cuando en realidad son contratos de corto plazo con alta probabilidad de no renovación.
**Observable_Symptoms:** Ingresos recurrentes reportados son altos, pero la empresa sigue en estrés de caja; renovaciones no automáticas; cada renovación requiere negociación.
**Early_Warning_Signals:** Contratos de suscripción de <6 meses; renovación manual; tasa de renovación <70%.
**Typical_Causes:** Inflar métricas para reportes; contratos que no tienen auto-renovación; clientes que no están realmente comprometidos.
**Business_Impact:** Falsa sensación de seguridad; decisiones estratégicas basadas en datos incorrectos; sorpresa cuando los ingresos recurrentes desaparecen.
**Metrics_To_Check:** Tasa de renovación automática; % de ingresos con contratos >12 meses; duración promedio de compromiso; true recurring revenue.
**Diagnostic_Questions:** ¿Tus ingresos recurrentes se renuevan automáticamente? ¿Cuál es tu tasa real de renovación?
**Recommended_Actions:** Reclasificar ingresos recurrentes vs contratos renovables; migrar a contratos con auto-renovación y facturación automática; medir true recurring revenue.
**Severity_Level:** High
**Related_Patterns:** BMP-003, BMP-048, BMP-049
---

## Margins

### BMP-055
**Pattern_Name:** Low Gross Margin Trap
**Category:** Margins
**Description:** El margen bruto es estructuralmente bajo (<20-30%), dejando poco espacio para cubrir gastos operativos y generar utilidad.
**Observable_Symptoms:** Cada venta deja poco después de costo de producto; cualquier gasto operativo adicional elimina la utilidad; la empresa necesita volumen extremo.
**Early_Warning_Signals:** Margen bruto <30% sostenidamente; costo de ventas creciendo como % del ingreso; incapacidad para cubrir gastos operativos con margen bruto.
**Typical_Causes:** Materia prima cara; poder de negociación de proveedores; precio de venta comprimido por competencia; ineficiencia productiva.
**Business_Impact:** Cualquier aumento de costos o baja en ventas genera pérdidas; poca capacidad de inversión; empresa opera al filo.
**Metrics_To_Check:** Margen bruto; tendencia del margen bruto; breakdown de costo de ventas; margen bruto por línea de producto.
**Diagnostic_Questions:** ¿Cuánto te queda después de pagar el costo directo del producto? ¿Puedes aumentar precios sin perder clientes?
**Recommended_Actions:** Reducir costo de ventas (renegociar proveedores, mejorar eficiencia productiva); incrementar precio de venta (diferenciación, valor agregado); eliminar líneas de bajo margen bruto.
**Severity_Level:** Critical
**Related_Patterns:** BMP-008, BMP-024, BMP-040

### BMP-056
**Pattern_Name:** Fixed Cost Heavy Structure
**Category:** Margins
**Description:** Alta proporción de costos fijos en la estructura total, generando alto punto de equilibrio y riesgo en períodos de baja demanda.
**Observable_Symptoms:** Gastos mensuales rígidos; imposibilidad de reducir costos rápidamente cuando bajan las ventas; altas pérdidas en meses malos.
**Early_Warning_Signals:** Costos fijos >60% de los costos totales; punto de equilibrio alto (>70% de capacidad); costos variables son una fracción pequeña.
**Typical_Causes:** Alta inversión en infraestructura, maquinaria o instalaciones; nómina elevada y fija; compromisos de arriendo/leasing a largo plazo.
**Business_Impact:** Alta palanca operativa (bueno en boom, peligroso en crisis); dificultad para ajustarse a caídas de demanda; riesgo de quiebra si ingresos caen.
**Metrics_To_Check:** Ratio costos fijos / costos totales; punto de equilibrio; apalancamiento operativo (DOL).
**Diagnostic_Questions:** ¿Cuánto pueden caer tus ingresos antes de tener pérdidas? ¿Puedes reducir costos rápidamente si es necesario?
**Recommended_Actions:** Convertir costos fijos en variables donde sea posible (outsourcing, personal variable, alquileres flexibles); reducir punto de equilibrio; mantener reserva de efectivo.
**Severity_Level:** High
**Related_Patterns:** BMP-055, BMP-058, BMP-061

### BMP-057
**Pattern_Name:** Price Sensitivity Neglect
**Category:** Margins
**Description:** La empresa no ajusta precios periódicamente por inflación, mejora de producto o cambios de mercado, erosionando márgenes reales.
**Observable_Symptoms:** Precios que no se actualizan hace >12 meses; clientes contentos con precios (muy contentos); márgenes que se comprimen silenciosamente.
**Early_Warning_Signals:** Inflación acumulada >10% sin ajuste de precios; margen bruto disminuyendo sin cambio en mix de producto; competidores subiendo precios.
**Typical_Causes:** Miedo a perder clientes; falta de proceso de revisión de precios; dueño que no quiere molestar a los clientes; inercia.
**Business_Impact:** Erosión lenta pero constante de márgenes; empresa trabaja cada vez más por menos; eventualmente márgenes negativos.
**Metrics_To_Check:** Frecuencia de revisión de precios; diferencial entre inflación acumulada y ajuste de precios; margen bruto tendencia 3 años.
**Diagnostic_Questions:** ¿Cuándo fue la última vez que ajustaste tus precios? ¿Tus precios suben al mismo ritmo que tus costos?
**Recommended_Actions:** Establecer política de revisión de precios trimestral; implementar ajustes automáticos por inflación en contratos; probar aumentos con un segmento.
**Severity_Level:** High
**Related_Patterns:** BMP-006, BMP-055, BMP-061

### BMP-058
**Pattern_Name:** Negative Unit Economics
**Category:** Margins
**Description:** Cada venta unitaria (producto, servicio, cliente) es económicamente negativa o marginal después de asignar todos los costos.
**Observable_Symptoms:** Empresa ocupada pero sin dinero; vende mucho pero no ve ganancias; dueño confundido sobre a dónde se va el dinero.
**Early_Warning_Signals:** Margen de contribución por unidad negativo; margen neto negativo sostenido; costo de servir al cliente > ingresos del cliente.
**Typical_Causes:** Fijación de precios incorrecta; costos ocultos no considerados; modelo de subsidio cruzado no intencional.
**Business_Impact:** Cada venta incrementa las pérdidas; crecimiento empeora la situación; quiebra asegurada si no se corrige.
**Metrics_To_Check:** Margen de contribución unitario; margen neto por unidad de producto; CAC vs LTV; costo full-service por cliente.
**Diagnostic_Questions:** ¿Cada producto que vendes deja dinero después de todos los costos? ¿Sabes cuál es tu margen de contribución unitario?
**Recommended_Actions:** Calcular el costo total por unidad de producto/servicio (full costing); ajustar precios para asegurar margen positivo; eliminar productos con economía unitaria negativa.
**Severity_Level:** Critical
**Related_Patterns:** BMP-008, BMP-024, BMP-055

### BMP-059
**Pattern_Name:** Price-Value Misalignment
**Category:** Margins
**Description:** La empresa cobra muy por debajo del valor que realmente entrega, dejando dinero sobre la mesa.
**Observable_Symptoms:** Clientes sorprendidos por lo barato que es; alta retención a pesar de aumentos de precio; recomendaciones boca a boca fuertes.
**Early_Warning_Signals:** Márgenes saludables pero muy por debajo de competidores comparables; clientes dicen deberías cobrar más; precio parece bajo para el valor percibido.
**Typical_Causes:** Fundador con síndrome del impostor; fijación de precios por costos en lugar de valor; miedo a perder clientes.
**Business_Impact:** Dejar ganancias significativas sin capturar; empresa infravalora su oferta; capacidad de inversión limitada por ingresos sub-óptimos.
**Metrics_To_Check:** Price-to-value ratio estimado; margen vs competidores directos; % de clientes que aceptarían un aumento de precio.
**Diagnostic_Questions:** ¿Cuánto más estarían dispuestos a pagar tus clientes? ¿Tu precio refleja el valor que entregas o el costo en que incurres?
**Recommended_Actions:** Investigar percepción de valor del cliente (Van Westendorp, Gabor-Granger); implementar pricing basado en valor; probar aumento con segmento piloto.
**Severity_Level:** Medium
**Related_Patterns:** BMP-042, BMP-046, BMP-055

### BMP-060
**Pattern_Name:** Margin Leakage via Operational Waste
**Category:** Margins
**Description:** Ineficiencias operativas (retrabajo, desperdicio, baja productividad) erosionan silenciosamente los márgenes.
**Observable_Symptoms:** Horas extras recurrentes; quejas de calidad; retrabajo constante; procesos que parecen más largos de lo necesario; equipo trabajando apagando incendios.
**Early_Warning_Signals:** Costos operativos como % de revenue creciendo; alta tasa de defectos/devoluciones; productividad por empleado por debajo de benchmark.
**Typical_Causes:** Falta de procesos estandarizados; mala capacitación; equipos/tecnología obsoletos; cultura reactiva.
**Business_Impact:** Márgenes más bajos de lo posible; equipo ocupado sin ser productivo; calidad inconsistente; clientes insatisfechos.
**Metrics_To_Check:** Costo de calidad (prevención + evaluación + fallas); productividad por empleado; tasa de defectos.
**Diagnostic_Questions:** ¿Cuánto tiempo gasta tu equipo en arreglar lo que se hizo mal? ¿Cuánto producto se desperdicia o devuelve?
**Recommended_Actions:** Implementar sistema de mejora continua (Kaizen, Lean); medir y atacar las principales fuentes de desperdicio; invertir en capacitación y herramientas.
**Severity_Level:** Medium
**Related_Patterns:** BMP-035, BMP-056, BMP-061

### BMP-061
**Pattern_Name:** Cost Structure Not Benchmarkable
**Category:** Margins
**Description:** La empresa no conoce su estructura de costos en detalle ni la compara con benchmarks de la industria.
**Observable_Symptoms:** Dueño no sabe cuánto cuesta producir cada unidad; estados financieros genéricos; decisiones se toman a ojo; sorpresas de rentabilidad al cierre de mes.
**Early_Warning_Signals:** Falta de sistema de costeo; no hay desglose de costos por producto; margen se calcula solo al cierre contable; no se conoce el punto de equilibrio.
**Typical_Causes:** Baja sofisticación financiera; falta de herramientas de gestión (ERP, controlling); fundador enfocado en ventas no en costos.
**Business_Impact:** Decisiones sub-óptimas por falta de información; márgenes no gestionados activamente; rentabilidad por debajo del potencial.
**Metrics_To_Check:** Existencia de sistema de costeo; precisión del cálculo de márgenes; frecuencia de reporte de rentabilidad por línea.
**Diagnostic_Questions:** ¿Sabes exactamente cuánto cuesta producir cada uno de tus productos? ¿Tienes un sistema que te dé rentabilidad en tiempo real?
**Recommended_Actions:** Implementar sistema de costeo básico; desglosar costos fijos y variables por línea de producto; establecer reporte mensual de márgenes.
**Severity_Level:** High
**Related_Patterns:** BMP-055, BMP-058, BMP-060

### BMP-062
**Pattern_Name:** Margin Squeeze from Both Sides
**Category:** Margins
**Description:** La empresa enfrenta presión simultánea de proveedores (costos suben) y clientes (precios bajan), comprimiendo márgenes de ambos lados.
**Observable_Symptoms:** Negociaciones duras con proveedores y clientes simultáneamente; incapacidad para trasladar aumentos de costo; márgenes decreciendo tendencialmente.
**Early_Warning_Signals:** Proveedores aumentan precios por encima de inflación; clientes exigen descuentos sistemáticos; margen bruto disminuyendo 2-3% anual.
**Typical_Causes:** Bajo poder de negociación con ambos lados; producto commodity sin diferenciación; mercado con exceso de oferta y concentración de compradores.
**Business_Impact:** Márgenes comprimidos progresivamente a cero; eventual inviabilidad del negocio; ventana de cierre de 2-5 años.
**Metrics_To_Check:** Spread entre precio de venta y costo de insumos; margen neto tendencial; poder de negociación relativo.
**Diagnostic_Questions:** ¿Puedes subir precios a tus clientes cuando tus costos suben? ¿Estás ganando o perdiendo margen año a año?
**Recommended_Actions:** Diferenciar producto para reducir elasticidad precio; integrarse verticalmente en el eslabón más presionado; buscar nuevos mercados con mejor dinámica.
**Severity_Level:** Critical
**Related_Patterns:** BMP-026, BMP-027, BMP-040
---

## Vertical Integration

### BMP-063
**Pattern_Name:** Missing Backward Integration
**Category:** Vertical Integration
**Description:** La empresa depende de proveedores externos para insumos críticos que podría producir internamente con ventajas de costo, calidad o control.
**Observable_Symptoms:** Problemas recurrentes de calidad con proveedores; dependencia de insumos importados con lead times largos; costos que no se pueden reducir.
**Early_Warning_Signals:** Insumo crítico representa >40% del costo de ventas; hay capacidad de producción interna no utilizada; proveedores con calidad inconsistente.
**Typical_Causes:** Historial de externalización por falta de capital; enfoque en core business; no se ha evaluado el costo-beneficio de integración.
**Business_Impact:** Dependencia estratégica de terceros; calidad no controlada; márgenes comprimidos por margen del proveedor.
**Metrics_To_Check:** % del costo de ventas en insumos externalizados; comparación de costo interno vs externo; lead time de insumos críticos.
**Diagnostic_Questions:** ¿Hay insumos que podrías producir tú mismo más barato o mejor? ¿Qué % de tu costo total está en manos de proveedores?
**Recommended_Actions:** Evaluar económicamente la integración hacia atrás de los 3 insumos más críticos; comenzar con producción parcial para aprender.
**Severity_Level:** Medium
**Related_Patterns:** BMP-026, BMP-027, BMP-040

### BMP-064
**Pattern_Name:** Missing Forward Integration
**Category:** Vertical Integration
**Description:** La empresa depende de intermediarios/distribuidores para llegar al cliente final, perdiendo margen y control de la experiencia.
**Observable_Symptoms:** Márgenes bajos en relación al precio final al consumidor; marca no es conocida por el consumidor final; distribuidores tienen el control de la relación.
**Early_Warning_Signals:** El margen del canal es mayor que el margen del productor; distribuidores deciden precios finales; quejas de clientes finales no llegan.
**Typical_Causes:** Modelo tradicional de distribución; falta de capacidad de venta directa; miedo a conflictos con canales existentes.
**Business_Impact:** Margen capturado por intermediarios; desconexión del cliente final; poder de negociación del distribuidor crece.
**Metrics_To_Check:** Margen del canal vs margen del productor; % de ventas directas; NPS del cliente final; % del precio final que retiene la empresa.
**Diagnostic_Questions:** ¿Cuánto paga el consumidor final vs cuánto recibes tú? ¿Conoces a tus consumidores finales? ¿Podrías vender directamente?
**Recommended_Actions:** Desarrollar canal de venta directa (e-commerce, tienda propia); crear programa de D2C para productos seleccionados.
**Severity_Level:** Medium
**Related_Patterns:** BMP-028, BMP-029, BMP-040

### BMP-065
**Pattern_Name:** Over-Integration (Vertical Silo)
**Category:** Vertical Integration
**Description:** La empresa ha integrado verticalmente demasiados eslabones de la cadena, perdiendo foco y eficiencia.
**Observable_Symptoms:** La empresa hace de todo en lugar de especializarse; áreas internas que no son competitivas; gerentes sobrepasados.
**Early_Warning_Signals:** Departamentos internos con costos superiores a proveedores externos; inversiones en activos que no son core; falta de expertise en algunas áreas.
**Typical_Causes:** Mentalidad de control total; malas experiencias previas con proveedores; falta de análisis make vs buy riguroso.
**Business_Impact:** Costos más altos que competidores especializados; falta de foco estratégico; ineficiencias en áreas no-core.
**Metrics_To_Check:** Costo interno vs externalizado por función; ROI por área integrada; % de activos en áreas no-core.
**Diagnostic_Questions:** ¿Todas las áreas que integras son realmente competitivas? ¿Podrías externalizar alguna y mejorar calidad/costo?
**Recommended_Actions:** Realizar análisis make-vs-buy por cada función integrada; externalizar áreas no-core donde existan proveedores competitivos.
**Severity_Level:** Medium
**Related_Patterns:** BMP-015, BMP-017, BMP-029

### BMP-066
**Pattern_Name:** Strategic Alliance Underutilization
**Category:** Vertical Integration
**Description:** La empresa no utiliza alianzas estratégicas para suplir capacidades faltantes, intentando hacer todo internamente.
**Observable_Symptoms:** Empresa pequeña intentando tener todas las funciones; soledad estratégica; oportunidades que requieren capacidades complementarias se dejan pasar.
**Early_Warning_Signals:** Empresa con <20 empleados y todas las funciones internas (RRHH, marketing, legal, TI); sin socios comerciales estratégicos.
**Typical_Causes:** Mentalidad de hacerlo solo; desconfianza en partners; falta de habilidades de gestión de alianzas.
**Business_Impact:** Crecimiento más lento; falta de capacidades complementarias; inversiones en áreas que podrían ser partnerizadas.
**Metrics_To_Check:** % de ingresos generados vía alianzas; número de alianzas estratégicas activas; % de capacidades cubiertas por partners.
**Diagnostic_Questions:** ¿Qué capacidades no tienes que podrías conseguir mediante una alianza? ¿Hay empresas complementarias con las que podrías colaborar?
**Recommended_Actions:** Identificar 3 capacidades complementarias necesarias; buscar socios potenciales con esas capacidades; proponer alianzas win-win.
**Severity_Level:** Medium
**Related_Patterns:** BMP-015, BMP-029, BMP-063

### BMP-067
**Pattern_Name:** Captive Distribution Channel
**Category:** Distribution Channels
**Description:** La empresa depende de un solo canal de distribución controlado por un tercero, sin alternativa real para llegar al mercado.
**Observable_Symptoms:** Distribuidor marca las condiciones; amenazas implícitas de deslistado; empresa acepta márgenes decrecientes por no tener otra opción.
**Early_Warning_Signals:** Un canal concentra >60% de las ventas; el canal vende también productos de la competencia; cambios en política del canal afectan directamente.
**Typical_Causes:** Poder de mercado del canal; producto que requiere distribución especializada; falta de inversión en canales alternativos.
**Business_Impact:** Canal controla el acceso al mercado; comisiones pueden subir unilateralmente; riesgo de deslistado o reemplazo.
**Metrics_To_Check:** % de ventas por canal; margen por canal; % de ingresos en riesgo si el canal cambia condiciones.
**Diagnostic_Questions:** ¿Qué pasaría si tu distribuidor principal decidiera no trabajar más contigo? ¿Tienes alternativas? ¿El canal sabe que dependes de él?
**Recommended_Actions:** Desarrollar canal directo como alternativa; diversificar distribuidores; construir marca que el consumidor final demande (pull strategy).
**Severity_Level:** Critical
**Related_Patterns:** BMP-012, BMP-018, BMP-028

### BMP-068
**Pattern_Name:** Multi-Channel Conflict
**Category:** Distribution Channels
**Description:** La empresa vende a través de múltiples canales que compiten entre sí, generando conflictos de precios y canibalización.
**Observable_Symptoms:** Distribuidores quejosos porque la empresa vende directo más barato; clientes comparando precios entre canales; guerras de precio intra-marca.
**Early_Warning_Signals:** Diferencias de precio >10% entre canales; quejas formales de canales; clientes comprando en canal más barato y usando servicio de otro.
**Typical_Causes:** Estrategia multicanal sin reglas claras; precios no coordinados; comisiones diferentes que incentivan comportamientos.
**Business_Impact:** Erosión de márgenes; relaciones tensas con canales; marca devaluada; canales dejan de promover la marca.
**Metrics_To_Check:** Diferencia de precio entre canales; % de ventas en cada canal; nivel de conflicto reportado por canales.
**Diagnostic_Questions:** ¿Tus canales compiten entre sí o se complementan? ¿Tienes reglas claras de pricing por canal?
**Recommended_Actions:** Definir estrategia clara de canales; implementar pricing consistente; diferenciar productos por canal (SKUs exclusivos); establecer territorios exclusivos.
**Severity_Level:** High
**Related_Patterns:** BMP-029, BMP-030, BMP-018

### BMP-069
**Pattern_Name:** Channel Partner Dependency
**Category:** Distribution Channels
**Description:** Modelo de negocio basado en partners/revendedores que controlan la relación con el cliente final, dejando a la empresa sin visibilidad ni control.
**Observable_Symptoms:** La empresa no conoce a sus clientes finales; partners se resisten a compartir información; cualquier cambio en la relación con el partner afecta las ventas.
**Early_Warning_Signals:** Sin CRM de clientes finales; partners que no responden comunicaciones; partner que desarrolla capacidades para reemplazar a la empresa.
**Typical_Causes:** Modelo de canal puro; falta de inversión en marca directa; partners con mayor poder de mercado.
**Business_Impact:** Sin relación directa con el cliente final; partner puede cambiar de proveedor fácilmente; márgenes comprimidos.
**Metrics_To_Check:** % de clientes finales conocidos; % de ingresos sin control directo; NPS de clientes finales medido independientemente.
**Diagnostic_Questions:** ¿Conoces a los clientes que usan tu producto? ¿Podrías contactarlos directamente? ¿Tu partner podría reemplazarte?
**Recommended_Actions:** Exigir a partners compartir datos de clientes finales; crear programa de marketing directo al consumidor final; desarrollar marca que genere demanda pull.
**Severity_Level:** High
**Related_Patterns:** BMP-029, BMP-030, BMP-067

### BMP-070
**Pattern_Name:** Inefficient Direct Sales Force
**Category:** Distribution Channels
**Description:** La empresa mantiene una fuerza de ventas directa cuando productos/servicios podrían venderse más eficientemente por canales digitales o indirectos.
**Observable_Symptoms:** Equipo de ventas grande para el volumen; vendedores dedicados a transacciones pequeñas; costo de ventas desproporcionado.
**Early_Warning_Signals:** Costo de fuerza de ventas >15-20% de ingresos; ticket promedio bajo para venta consultiva; ciclo de venta corto pero con vendedor dedicado.
**Typical_Causes:** Modelo histórico de venta directa; falta de plataforma de e-commerce; resistencia del fundador a cambiar.
**Business_Impact:** Estructura de costos más alta que competidores digitales; inversión desproporcionada en ventas; márgenes más bajos.
**Metrics_To_Check:** Costo de fuerza de ventas como % de ingresos; ticket promedio por vendedor; comparación eficiencia canal directo vs digital.
**Diagnostic_Questions:** ¿Tus vendedores agregan valor en cada transacción o algunas podrían automatizarse? ¿Tus clientes quieren comprar online?
**Recommended_Actions:** Implementar e-commerce o canal de autoservicio; migrar transacciones pequeñas a canales digitales; transformar fuerza de ventas a roles de consultoría.
**Severity_Level:** Medium
**Related_Patterns:** BMP-018, BMP-029, BMP-067
---

## Competitive Advantages

### BMP-071
**Pattern_Name:** Cost Leadership Without Operational Excellence
**Category:** Competitive Advantages
**Description:** La empresa intenta ser líder en costos pero no tiene la eficiencia operativa, escala o tecnología para sostenerlo.
**Observable_Symptoms:** Precios más bajos que competidores pero márgenes muy ajustados; estrés operativo constante; calidad que se resiente.
**Early_Warning_Signals:** Márgenes inferiores al promedio de la industria siendo el de precio más bajo; quejas de calidad frecuentes.
**Typical_Causes:** Estrategia de bajo precio sin estructura de costos correspondiente; competidores con mayor escala o mejor tecnología.
**Business_Impact:** Márgenes insostenibles; calidad inferior que aleja clientes; posición atrapada.
**Metrics_To_Check:** Costo unitario vs competidor de menor costo; margen neto vs industria; brecha de productividad.
**Diagnostic_Questions:** ¿Tus costos son realmente más bajos que los de tus competidores? ¿O solo tus precios son más bajos?
**Recommended_Actions:** Abandonar estrategia de costo y buscar diferenciación; o invertir agresivamente en eficiencia operativa.
**Severity_Level:** Critical
**Related_Patterns:** BMP-040, BMP-055, BMP-073

### BMP-072
**Pattern_Name:** First-Mover Without Moat
**Category:** Competitive Advantages
**Description:** La empresa fue primera en el mercado pero no construyó barreras de entrada, permitiendo que competidores la alcancen.
**Observable_Symptoms:** Competidores copiando la oferta rápidamente; participación de mercado decreciente; ventaja de primero desvaneciéndose.
**Early_Warning_Signals:** Competidores lanzando productos similares en <12 meses; innovaciones replicadas rápidamente; % de mercado disminuyendo.
**Typical_Causes:** Falta de patentamiento; no se invirtió en marca; producto sin efectos de red.
**Business_Impact:** Pérdida de liderazgo de mercado; competidores capturan valor de la innovación.
**Metrics_To_Check:** Participación de mercado tendencial; velocidad de imitación; número de barreras de entrada construidas.
**Diagnostic_Questions:** ¿Qué le impide a un competidor copiar lo que haces? ¿Tu participación de mercado está creciendo o decreciendo?
**Recommended_Actions:** Construir agresivamente barreras de entrada (patentes, marca, efectos de red, datos); acelerar innovación.
**Severity_Level:** High
**Related_Patterns:** BMP-074, BMP-075, BMP-077

### BMP-073
**Pattern_Name:** Imitation Resilience
**Category:** Competitive Advantages
**Description:** La empresa tiene una ventaja competitiva difícil de imitar pero no la reconoce ni capitaliza.
**Observable_Symptoms:** Competidores intentan copiar pero no logran el mismo resultado; clientes notan diferencias que la empresa no promociona.
**Early_Warning_Signals:** Competidores entran al mercado pero no prosperan; la empresa gana contra ofertas más baratas.
**Typical_Causes:** Ventaja basada en cultura, procesos o conocimiento tácito difícil de articular.
**Business_Impact:** Oportunidad perdida de cobrar premium; empresa sub-valorada; ventaja erosionable si no se protege.
**Metrics_To_Check:** Tasa de éxito vs competidores que intentan imitar; margen vs competidores directos.
**Diagnostic_Questions:** ¿Qué haces bien que otros intentan copiar pero no logran? ¿Por qué tus clientes te eligen incluso cuando hay opciones más baratas?
**Recommended_Actions:** Identificar y documentar fuentes de ventaja difícil de imitar; comunicarlas en propuesta de valor; cobrar premium.
**Severity_Level:** Medium
**Related_Patterns:** BMP-042, BMP-046, BMP-047

### BMP-074
**Pattern_Name:** Network Effect Absence
**Category:** Competitive Advantages
**Description:** El producto podría beneficiarse de efectos de red pero la empresa no ha diseñado para activarlos.
**Observable_Symptoms:** Cada cliente obtiene valor solo de su uso individual; no hay interacción entre usuarios.
**Early_Warning_Signals:** Competidores con efectos de red ganando tracción; clientes pidiendo funcionalidades colaborativas.
**Typical_Causes:** Diseño de producto individual; falta de visión de plataforma.
**Business_Impact:** Crecimiento lineal en lugar de exponencial; vulnerabilidad ante competidores con efectos de red.
**Metrics_To_Check:** Coeficiente de viralidad; % de valor generado por interacciones entre usuarios.
**Diagnostic_Questions:** ¿Tu producto se vuelve más valioso cuantos más usuarios lo usan? ¿Tus usuarios interactúan entre sí?
**Recommended_Actions:** Identificar oportunidades de efectos de red; rediseñar producto para incluir componentes sociales o colaborativos.
**Severity_Level:** Medium
**Related_Patterns:** BMP-010, BMP-029, BMP-075

### BMP-075
**Pattern_Name:** Brand Equity Deficit
**Category:** Competitive Advantages
**Description:** La empresa no ha invertido en construir marca, operando como commodity a pesar de tener calidad superior.
**Observable_Symptoms:** Marca desconocida fuera del círculo inmediato; clientes no recomiendan activamente; decisión de compra basada solo en precio.
**Early_Warning_Signals:** Bajo recall de marca; poco tráfico directo a sitio web; clientes no saben el nombre de la empresa.
**Typical_Causes:** Fundador no valora el branding; presupuesto cero para marketing de marca.
**Business_Impact:** Competidores con marca capturan premium; menor lealtad; dificultad para lanzar nuevos productos.
**Metrics_To_Check:** Brand recall/awareness; tráfico directo vs pagado; price premium vs competidores sin marca.
**Diagnostic_Questions:** ¿Tus clientes recuerdan tu marca? ¿Cuánto más podrías cobrar si tu marca fuera más conocida?
**Recommended_Actions:** Invertir en construcción de marca (contenido, PR, redes sociales); crear programa de referidos.
**Severity_Level:** Medium
**Related_Patterns:** BMP-040, BMP-042, BMP-047

### BMP-076
**Pattern_Name:** Data Moat Opportunity
**Category:** Competitive Advantages
**Description:** La empresa genera datos valiosos pero no los aprovecha como ventaja competitiva ni fuente de ingresos.
**Observable_Symptoms:** Datos generados que no se analizan; información valiosa que no se usa; decisiones basadas en intuición.
**Early_Warning_Signals:** Datos no estructurados ni almacenados sistemáticamente; sin capacidad de analytics.
**Typical_Causes:** Falta de cultura data-driven; no hay herramientas de BI; subestimación del valor de los datos.
**Business_Impact:** Oportunidad perdida de diferenciación; decisiones sub-óptimas.
**Metrics_To_Check:** % de decisiones basadas en datos; madurez analítica; ingresos generados por datos.
**Diagnostic_Questions:** ¿Qué datos generas en tu operación diaria? ¿Los estás utilizando para mejorar tu producto?
**Recommended_Actions:** Implementar sistema de captura y almacenamiento de datos; invertir en BI y analytics.
**Severity_Level:** Medium
**Related_Patterns:** BMP-010, BMP-042, BMP-074

### BMP-077
**Pattern_Name:** Switching Cost Erosion
**Category:** Competitive Advantages
**Description:** Los switching costs se están erosionando por cambios tecnológicos o de mercado.
**Observable_Symptoms:** Clientes leales ahora evalúan alternativas; competidores ofreciendo migración fácil.
**Early_Warning_Signals:** Clientes antiguos preguntan por competidores; nuevos entrantes ofrecen importación de datos.
**Typical_Causes:** Estandarización tecnológica; APIs abiertas; regulación que obliga a portabilidad de datos.
**Business_Impact:** Aumento de churn; presión en precios; pérdida de la principal ventaja competitiva.
**Metrics_To_Check:** Tasa de churn de clientes antiguos; duración promedio de relación.
**Diagnostic_Questions:** ¿Tus clientes están más dispuestos a considerar alternativas? ¿Qué tan fácil es migrar a un competidor?
**Recommended_Actions:** Innovar en nuevos switching costs: mejor integración, datos retenidos, personalización profunda.
**Severity_Level:** High
**Related_Patterns:** BMP-050, BMP-072, BMP-075
---

## Entry Barriers

### BMP-078
**Pattern_Name:** Low Entry Barriers in Industry
**Category:** Entry Barriers
**Description:** La industria tiene barreras de entrada muy bajas, permitiendo que nuevos competidores entren constantemente y presionen márgenes.
**Observable_Symptoms:** Nuevos competidores aparecen cada mes; guerras de precio recurrentes; diferenciación difícil.
**Early_Warning_Signals:** Alta tasa de entrada de nuevos competidores; bajo CAPEX requerido; tecnología accesible para todos.
**Typical_Causes:** Industria atomizada; tecnología democratizada; pocos requisitos de capital.
**Business_Impact:** Márgenes estructuralmente bajos; necesidad constante de innovar; competencia por precio sostenida.
**Metrics_To_Check:** Tasa de entrada de nuevos competidores; margen neto promedio de la industria; inversión requerida para entrar.
**Diagnostic_Questions:** ¿Qué tan fácil es para alguien nuevo empezar a competirte? ¿Cuántos competidores nuevos aparecieron este año?
**Recommended_Actions:** Construir barreras de entrada activamente (marca, escala, patentes, relaciones, datos); especializarse en nicho con barreras naturales.
**Severity_Level:** High
**Related_Patterns:** BMP-040, BMP-074, BMP-077

### BMP-079
**Pattern_Name:** Capital Requirement Blindness
**Category:** Entry Barriers
**Description:** La empresa no reconoce que su principal barrera de entrada es el capital requerido, y no la refuerza ni aprovecha estratégicamente.
**Observable_Symptoms:** Empresa tiene ventaja de escala/capital pero compite como si fuera pequeña; no usa su poder financiero.
**Early_Warning_Signals:** Competidores pequeños ganando participación; empresa no invierte en activos que aumenten la barrera.
**Typical_Causes:** Mentalidad de PyME; no reconocer la ventaja de capital; falta de agresividad estratégica.
**Business_Impact:** Barrera de capital se erosiona; competidores acceden a financiamiento alternativo.
**Metrics_To_Check:** CAPEX como % de ingresos; inversión requerida para competir; % de competidores con respaldo financiero.
**Diagnostic_Questions:** ¿Cuánto capital necesita alguien para competirte? ¿Estás usando tu ventaja de capital para invertir en activos que otros no pueden?
**Recommended_Actions:** Invertir agresivamente en activos que eleven el listón de capital requerido; adquirir competidores pequeños.
**Severity_Level:** Medium
**Related_Patterns:** BMP-074, BMP-078, BMP-080

### BMP-080
**Pattern_Name:** Regulatory Barrier Vulnerability
**Category:** Entry Barriers
**Description:** La empresa opera donde las barreras regulatorias son la principal protección, pero cambios regulatorios podrían eliminarlas.
**Observable_Symptoms:** Cumplimiento regulatorio es el core de la propuesta de valor; lobby o relaciones gubernamentales son clave.
**Early_Warning_Signals:** Discusiones sobre desregulación en el sector; nuevos entrantes usando tecnología para sortear regulación.
**Typical_Causes:** Modelo construido alrededor de protección regulatoria; falta de ventajas más allá de la regulación.
**Business_Impact:** Si la regulación cambia, el negocio se vuelve commodity; riesgo existencial.
**Metrics_To_Check:** % de ventaja competitiva atribuible a regulación; indicadores de cambio regulatorio.
**Diagnostic_Questions:** ¿Qué pasaría si desregulan tu industria? ¿Tienes ventajas más allá de la regulación?
**Recommended_Actions:** Desarrollar ventajas no regulatorias (marca, eficiencia, tecnología); monitorear cambios regulatorios.
**Severity_Level:** High
**Related_Patterns:** BMP-075, BMP-078, BMP-082

### BMP-081
**Pattern_Name:** Intellectual Property Not Protected
**Category:** Entry Barriers
**Description:** La empresa tiene propiedad intelectual valiosa pero no la ha protegido formalmente.
**Observable_Symptoms:** Competidores copian productos/procesos abiertamente; secretos comerciales no documentados ni asegurados.
**Early_Warning_Signals:** Ex-empleados trabajando en competidores; productos de competidores sospechosamente similares; sin patentes ni acuerdos de confidencialidad.
**Typical_Causes:** Falta de conocimiento legal; cultura de compartir sin protección; costo percibido de patentamiento.
**Business_Impact:** Ventaja competitiva se erosiona; competidores se apropian de innovaciones sin costo.
**Metrics_To_Check:** Número de patentes/marcas registradas; % de know-how documentado y protegido.
**Diagnostic_Questions:** ¿Qué información, si la obtuviera un competidor, te haría daño? ¿Está legalmente protegida?
**Recommended_Actions:** Realizar auditoría de PI; patentar invenciones patentables; registrar marcas; implementar acuerdos de confidencialidad.
**Severity_Level:** High
**Related_Patterns:** BMP-046, BMP-073, BMP-077

### BMP-082
**Pattern_Name:** Economies of Scale Not Achieved
**Category:** Entry Barriers
**Description:** La empresa no ha alcanzado la escala necesaria para tener ventaja de costos sobre competidores más pequeños o nuevos entrantes.
**Observable_Symptoms:** Costos unitarios similares a competidores pequeños; no hay descuentos por volumen significativos.
**Early_Warning_Signals:** Costos unitarios no disminuyen con el volumen; competidores más grandes tienen ventaja de precio.
**Typical_Causes:** Producción en lotes pequeños; falta de estandarización; capacidad ociosa recurrente.
**Business_Impact:** Desventaja de costos vs competidores más grandes; márgenes más bajos; presión de precio.
**Metrics_To_Check:** Costo unitario vs volumen; curva de experiencia; diferencial de costo con competidor más grande.
**Diagnostic_Questions:** ¿Tus costos unitarios bajan cuando produces más? ¿Tienes ventaja de costo contra competidores más grandes?
**Recommended_Actions:** Consolidar producción para ganar escala; estandarizar componentes; buscar crecimiento en volumen.
**Severity_Level:** Medium
**Related_Patterns:** BMP-055, BMP-078, BMP-079

### BMP-083
**Pattern_Name:** Technology Moat Missing
**Category:** Entry Barriers
**Description:** La empresa no usa tecnología propietaria o difícil de replicar como barrera de entrada, a pesar de tener capacidad para desarrollarla.
**Observable_Symptoms:** Procesos manuales que podrían automatizarse; tecnología disponible para todos; sin diferenciación técnica.
**Early_Warning_Signals:** Competidores usando tecnología similar o mejor; baja inversión en I+D tecnológico.
**Typical_Causes:** Falta de visión tecnológica; inversión insuficiente en I+D; cultura de copy-paste.
**Business_Impact:** Facilidad de imitación; competencia basada en precio; obsolescencia tecnológica.
**Metrics_To_Check:** Gasto en I+D como % de ingresos; patentes tecnológicas; brecha tecnológica vs industria.
**Diagnostic_Questions:** ¿Tu tecnología te da ventaja sobre competidores? ¿Podrías desarrollar tecnología propietaria?
**Recommended_Actions:** Invertir en I+D para crear tecnología propietaria; patentar innovaciones técnicas; construir plataforma tecnológica difícil de replicar.
**Severity_Level:** Medium
**Related_Patterns:** BMP-038, BMP-072, BMP-081
---

## Founder Dependency

### BMP-084
**Pattern_Name:** Founder Single Point of Failure
**Category:** Founder Dependency
**Description:** El fundador concentra conocimiento crítico, relaciones clave y toma de decisiones, siendo un riesgo existencial para el negocio.
**Observable_Symptoms:** Fundador es el único que sabe ciertos procesos; clientes clave solo se relacionan con el fundador; si el fundador no está, no se deciden cosas importantes.
**Early_Warning_Signals:** Fundador trabajando 12+ horas diarias; sin sucesor identificado; relaciones comerciales atadas a la persona.
**Typical_Causes:** Fundador fundó la empresa desde cero y nunca delegó; ego; falta de confianza en el equipo.
**Business_Impact:** Empresa no vendible (due diligence mata el deal); riesgo de colapso si el fundador se enferma; estancamiento por cuello de botella.
**Metrics_To_Check:** % de ingresos que dependen de relaciones del fundador; bus factor; horas trabajadas por el fundador vs equipo.
**Diagnostic_Questions:** ¿Qué pasaría si el fundador no pudiera trabajar por 6 meses? ¿Cuántos clientes se irían? ¿Quién tomaría las decisiones?
**Recommended_Actions:** Documentar conocimiento crítico del fundador; transferir relaciones clave a otros miembros del equipo; nombrar COO o gerente general.
**Severity_Level:** Critical
**Related_Patterns:** BMP-033, BMP-080, BMP-086

### BMP-085
**Pattern_Name:** Founder-Led Sales Dependency
**Category:** Founder Dependency
**Description:** El fundador es el principal o único vendedor, limitando severamente la capacidad de crecimiento de ingresos.
**Observable_Symptoms:** Fundador cerrando todos los deals importantes; equipo comercial sin autonomía; pipeline controlado por el fundador.
**Early_Warning_Signals:** Fundador presente en todas las reuniones de ventas; equipo de ventas con baja productividad; clientes piden hablar solo con el fundador.
**Typical_Causes:** Fundador construyó relaciones desde el inicio; desconfianza en que otros puedan vender; personalidad carismática central.
**Business_Impact:** Techo de ingresos = capacidad del fundador; empresa no escalable; rotación de vendedores por falta de oportunidades.
**Metrics_To_Check:** % de ingresos cerrados por el fundador; productividad del equipo de ventas vs fundador; pipeline fuera del fundador.
**Diagnostic_Questions:** ¿Cuánto del revenue depende de que el fundador venda? ¿Podrías duplicar ventas sin que el fundador venda más?
**Recommended_Actions:** Construir proceso de ventas independiente del fundador; crear material de ventas y playbook; entrenar y empoderar al equipo de ventas.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-084, BMP-087

### BMP-086
**Pattern_Name:** Lack of Succession Plan
**Category:** Founder Dependency
**Description:** No existe un plan de sucesión para el fundador ni para roles clave de liderazgo.
**Observable_Symptoms:** Fundador no ha nombrado sucesor; roles clave sin backup; incertidumbre sobre el futuro de la empresa.
**Early_Warning_Signals:** Fundador mayor de 55 años sin plan de retiro; nadie en la organización preparado para liderar; empleados clave no saben qué pasaría si el fundador se va.
**Typical_Causes:** El fundador no quiere enfrentar su mortalidad; falta de candidatos internos; cultura de dependencia del fundador.
**Business_Impact:** Pérdida total de valor si el fundador se retira abruptamente; imposibilidad de vender la empresa; incertidumbre para empleados e inversores.
**Metrics_To_Check:** Edad del fundador; existencia de plan de sucesión documentado; % de roles críticos con sucesor identificado.
**Diagnostic_Questions:** ¿Quién lideraría la empresa si el fundador se retirara mañana? ¿Esa persona está preparada? ¿Hay un plan documentado?
**Recommended_Actions:** Desarrollar plan de sucesión con horizonte de 3-5 años; identificar y preparar candidatos internos; considerar opciones de gobierno corporativo.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-084, BMP-085

### BMP-087
**Pattern_Name:** Founder Ego as Strategic Blindness
**Category:** Founder Dependency
**Description:** El ego del fundador impide ver la realidad del mercado, escuchar feedback o pivotear cuando es necesario.
**Observable_Symptoms:** Fundador ignora datos que contradicen su visión; despido de empleados que dan malas noticias; repetición de estrategias fallidas.
**Early_Warning_Signals:** Alta rotación de gerentes; falta de diversidad de opiniones en el equipo; decisiones basadas en corazonadas vs datos.
**Typical_Causes:** Fundador con éxito pasado que cree tener la fórmula; personalidad narcisista; falta de contrapeso en el gobierno.
**Business_Impact:** Decisiones estratégicas erróneas; fuga de talento que podría haber corregido el rumbo; empresa persiste en dirección equivocada.
**Metrics_To_Check:** Rotación de gerentes/seniors; % de decisiones basadas en datos; diversidad de opiniones en reuniones clave.
**Diagnostic_Questions:** ¿El fundador acepta críticas constructivas? ¿Hay alguien en la empresa que pueda decirle que está equivocado? ¿Se consideran datos objetivos en las decisiones?
**Recommended_Actions:** Incorporar consejo asesor externo; implementar procesos de decisión basados en datos; fomentar cultura de feedback y diversidad de opiniones.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-084, BMP-096

### BMP-088
**Pattern_Name:** Founder Key Person Insurance Missing
**Category:** Founder Dependency
**Description:** La empresa no tiene seguro de vida o invalidez para el fundador, siendo económicamente devastadora su pérdida.
**Observable_Symptoms:** Fundador no tiene seguro de vida a nombre de la empresa; si el fundador fallece, la empresa no tendría recursos para continuar.
**Early_Warning_Signals:** Fundador sin seguro; póliza insuficiente vs valor del fundador para el negocio; dependencia financiera del fundador.
**Typical_Causes:** Desconocimiento; costo percibido alto; optimismo sobre la salud; falta de asesoría.
**Business_Impact:** Pérdida del fundador = quiebra o venta forzada; familias de socios sin protección; empleados sin trabajo.
**Metrics_To_Check:** Existencia y monto de seguro key person; valor económico del fundador para el negocio.
**Diagnostic_Questions:** ¿Tiene el fundador un seguro de vida que proteja a la empresa? ¿El monto cubre el costo de reemplazarlo y mantener la operación?
**Recommended_Actions:** Contratar seguro key person por al menos 5-10x el ingreso anual del fundador; revisar cobertura anualmente.
**Severity_Level:** High
**Related_Patterns:** BMP-084, BMP-086, BMP-089

### BMP-089
**Pattern_Name:** Founder Illiquidity Trap
**Category:** Founder Dependency
**Description:** El fundador tiene todo su patrimonio neto invertido en la empresa, sin diversificación personal ni liquidez.
**Observable_Symptoms:** Fundador no tiene ahorros separados del negocio; cualquier crisis de la empresa es también crisis personal del fundador; toma decisiones conservadoras por miedo a perderlo todo.
**Early_Warning_Signals:** Fundador no tiene inversiones fuera de la empresa; patrimonio personal = valor de la empresa; endeudamiento personal cruzado con la empresa.
**Typical_Causes:** Reinversión constante de utilidades; falta de planificación financiera personal; crecimiento que requiere todo el capital disponible.
**Business_Impact:** Decisiones sub-óptimas por aversión al riesgo; imposibilidad de retirarse; estrés financiero personal del fundador.
**Metrics_To_Check:** % del patrimonio del fundador en la empresa; deuda personal del fundador relacionada con la empresa; historial de dividendos.
**Diagnostic_Questions:** ¿Qué % de tu patrimonio personal está en la empresa? ¿Podrías sobrevivir financieramente si la empresa quebrara?
**Recommended_Actions:** Establecer política de dividendos regular; diversificar inversiones personales fuera del negocio; separar finanzas personales y empresariales.
**Severity_Level:** Medium
**Related_Patterns:** BMP-084, BMP-086, BMP-088
---

## Model Maturity

### BMP-090
**Pattern_Name:** Startup Stagnation (Pre-Seed / Seed Limbo)
**Category:** Model Maturity
**Description:** La empresa lleva años operando como startup sin lograr tracción significativa ni alcanzar product-market fit claro.
**Observable_Symptoms:** Ingresos bajos e irregulares; pivotes constantes sin mejora; equipo pequeño desde hace años; inversión externa no llega.
**Early_Warning_Signals:** Más de 3-5 años sin alcanzar  ARR; múltiples pivotes sin dirección; fundador desgastado.
**Typical_Causes:** Falta de validación de mercado; producto que no resuelve un problema real; founder sin experiencia en startups.
**Business_Impact:** Empresa en modo zombie; consumo de ahorros personales; eventual cierre por agotamiento.
**Metrics_To_Check:** ARR; meses de runway; tasa de crecimiento interanual; product-market fit score (encuesta).
**Diagnostic_Questions:** ¿Tus clientes te pagan? ¿Volverían a comprar? ¿Recomendarían tu producto? ¿Cuánto tiempo más puedes sostenerte?
**Recommended_Actions:** Validar product-market fit con encuesta (si >40% dice muy decepcionado sin tu producto, sigue; si no, pivota); reducir gastos a mínimo; considerar cerrar si no hay tracción.
**Severity_Level:** Critical
**Related_Patterns:** BMP-001, BMP-003, BMP-045

### BMP-091
**Pattern_Name:** Growth Without Profitability
**Category:** Model Maturity
**Description:** La empresa crece en ingresos pero nunca ha generado ganancias netas sostenidas.
**Observable_Symptoms:** Revenue creciendo 20-50% anual pero pérdidas recurrentes; rondas de inversión para tapar agujeros; quema de caja constante.
**Early_Warning_Signals:** Margen neto negativo por >3 años consecutivos; quema de caja acelerándose con el crecimiento; dependencia de financiamiento externo.
**Typical_Causes:** Modelo de negocio con economía unitaria no probada; priorización de crecimiento sobre rentabilidad; estructura de costos fijos alta.
**Business_Impact:** Si el financiamiento se corta, la empresa quiebra; fundador diluido; empresa difícil de vender.
**Metrics_To_Check:** Margen neto; EBITDA; burn rate; months of runway; unit economics (CAC, LTV, margen de contribución).
**Diagnostic_Questions:** ¿Tu negocio genera efectivo? ¿Cuántos meses de operación te quedan sin nueva inversión? ¿Cada cliente nuevo es rentable?
**Recommended_Actions:** Alcanzar rentabilidad antes de buscar crecimiento agresivo; mejorar unit economics; reducir burn rate; considerar crecimiento rentable vs growth-at-all-costs.
**Severity_Level:** Critical
**Related_Patterns:** BMP-008, BMP-055, BMP-058

### BMP-092
**Pattern_Name:** Mature Company, Startup Processes
**Category:** Model Maturity
**Description:** Empresa con años de operación pero que aún opera con procesos informales propios de una startup.
**Observable_Symptoms:** Falta de procesos formales; decisiones ad-hoc; roles no definidos; comunicación informal; crisis recurrentes.
**Early_Warning_Signals:** Empresa con >10 años y <10 empleados; fundador tomando decisiones operativas diarias; sin manuales ni procedimientos.
**Typical_Causes:** Cultura startup que no evolucionó; fundador que no quiere crecer; éxito temprano que no exigió profesionalización.
**Business_Impact:** Techo de crecimiento bajo; ineficiencias operativas; dependencia del fundador; empresa difícil de vender.
**Metrics_To_Check:** Edad de la empresa vs tamaño; existencia de organización formal; % de procesos documentados.
**Diagnostic_Questions:** ¿Tu empresa opera como cuando empezó? ¿Tienes roles, procesos y sistemas formales? ¿Podrías escalar sin colapsar?
**Recommended_Actions:** Profesionalizar gestión (roles, procesos, sistemas); implementar reuniones estructuradas y OKRs; considerar incorporar talento gerencial experimentado.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-037, BMP-039

### BMP-093
**Pattern_Name:** Scaling Company, Founder-Led Management
**Category:** Model Maturity
**Description:** La empresa está en fase de escalamiento pero el fundador aún gestiona como si fuera una startup pequeña.
**Observable_Symptoms:** Fundador microgestionando equipos grandes; falta de middle management; proceso de decisión lento; cuellos de botella del fundador.
**Early_Warning_Signals:** Empresa >30 empleados y fundador aún aprueba gastos menores; sin gerentes intermedios; rotación de empleados por falta de autonomía.
**Typical_Causes:** Fundador no se adaptó a su nuevo rol; falta de habilidades de gestión de equipos grandes; desconfianza en delegar.
**Business_Impact:** Estancamiento del crecimiento; fuga de talento; imposibilidad de escalar más allá de la capacidad del fundador.
**Metrics_To_Check:** Ratio de employees por manager; tiempo de toma de decisiones; rotación de empleados; engagement score.
**Diagnostic_Questions:** ¿El fundador aún aprueba gastos pequeños? ¿Hay gerentes capacitados entre el fundador y el equipo? ¿El equipo tiene autonomía?
**Recommended_Actions:** Contratar gerentes intermedios; transicionar al fundador a rol de CEO estratégico; implementar sistema de delegación con niveles de autoridad.
**Severity_Level:** High
**Related_Patterns:** BMP-033, BMP-084, BMP-092

### BMP-094
**Pattern_Name:** Product-Led Growth Without Sales Capability
**Category:** Model Maturity
**Description:** Empresa que creció orgánicamente vía producto pero no ha desarrollado capacidades de ventas para escalar a segmentos enterprise.
**Observable_Symptoms:** Crecimiento orgánico se estanca; no pueden cerrar cuentas grandes; equipo técnico sin skills de ventas.
**Early_Warning_Signals:** Crecimiento orgánico decreciente; intentos fallidos de contratar fuerza de ventas; cuentas enterprise rechazan por falta de soporte comercial.
**Typical_Causes:** Cultura product-first sin inversión en ventas; equipo técnico que desconfía de ventas; producto no adaptado a necesidades enterprise.
**Business_Impact:** Techo de crecimiento al agotar segmento bottom-up; imposibilidad de capturar cuentas de alto valor; vulnerabilidad ante competidores con sales motion.
**Metrics_To_Check:** % de ingresos de cuentas enterprise; crecimiento orgánico vs crecimiento por ventas; tasa de conversión enterprise.
**Diagnostic_Questions:** ¿Puedes vender a empresas grandes? ¿Tienes equipo de ventas enterprise? ¿Tu producto soporta necesidades de cuentas grandes?
**Recommended_Actions:** Construir capacidad de ventas enterprise; adaptar producto para requerimientos enterprise (seguridad, compliance, integraciones); contratar VP de Ventas con experiencia en el segmento.
**Severity_Level:** Medium
**Related_Patterns:** BMP-034, BMP-070, BMP-093

### BMP-095
**Pattern_Name:** International Expansion Readiness
**Category:** Model Maturity
**Description:** La empresa domina el mercado local pero no tiene capacidad para expandirse internacionalmente, limitando su crecimiento.
**Observable_Symptoms:** Mercado local saturado; ingresos estancados; sin presencia internacional; producto solo en idioma local.
**Early_Warning_Signals:** Participación de mercado local >30%; crecimiento local <5% anual; solicitudes de clientes internacionales no atendidas.
**Typical_Causes:** Falta de recursos para expansión; producto no adaptado a otros mercados; miedo a la complejidad internacional.
**Business_Impact:** Techo de crecimiento; vulnerabilidad ante competidores internacionales que entran al mercado local.
**Metrics_To_Check:** % de ingresos internacionales; TAM internacional vs local; preparación del producto para internacionalización.
**Diagnostic_Questions:** ¿Tu producto funciona en otros mercados? ¿Tienes capacidad para vender internacionalmente? ¿Competidores internacionales están entrando a tu mercado?
**Recommended_Actions:** Investigar mercados prioritarios (cercanía cultural, regulatoria); adaptar producto para internacionalización; probar con partners/distribuidores en mercado target.
**Severity_Level:** Medium
**Related_Patterns:** BMP-013, BMP-029, BMP-082

### BMP-096
**Pattern_Name:** Succession Crisis Imminent
**Category:** Model Maturity
**Description:** Empresa madura donde el fundador/socio fundador está próximo a retirarse sin un plan de sucesión o salida claro.
**Observable_Symptoms:** Fundador menciona retiro pero no hay plan; hijos/familia no interesados o no capacitados; posibles compradores no identificados.
**Early_Warning_Signals:** Fundador >60 años; ausencia de plan de sucesión documentado; hijos trabajando en otras industrias; empresa no preparada para due diligence.
**Typical_Causes:** Dificultad emocional para soltar; falta de candidatos internos; empresa no profesionalizada para ser vendible.
**Business_Impact:** Riesgo de venta forzada a bajo precio; conflicto familiar; cierre de la empresa; pérdida del legado y valor construido.
**Metrics_To_Check:** Edad del fundador; existencia de plan de sucesión; niveles de profesionalización; interés de compradores potenciales.
**Diagnostic_Questions:** ¿Quién tomará el negocio cuando el fundador se retire? ¿Hay un plan concreto con fechas? ¿La empresa está lista para ser vendida o transferida?
**Recommended_Actions:** Iniciar planificación de sucesión con 3-5 años de anticipación; profesionalizar gestión para hacer la empresa vendible; considerar opciones: venta, fusión, transición familiar, management buyout.
**Severity_Level:** Critical
**Related_Patterns:** BMP-084, BMP-086, BMP-092
