# Sales Patterns — SME Knowledge Base

> Base de conocimiento para que agentes de IA detecten patrones comerciales relevantes en PyMEs: funnel de ventas, conversión, ticket promedio, productividad comercial, dependencia de vendedores, recurrencia, cross selling, upselling, cobertura comercial, gestión de oportunidades, forecast y ciclo de ventas.

---

## Categorías cubiertas

| # | Categoría | Patrones |
|---|-----------|----------|
| 1 | Funnel de Ventas | 8 |
| 2 | Conversión | 8 |
| 3 | Ticket Promedio | 7 |
| 4 | Productividad Comercial | 8 |
| 5 | Dependencia de Vendedores | 7 |
| 6 | Recurrencia | 8 |
| 7 | Cross Selling | 7 |
| 8 | Upselling | 7 |
| 9 | Cobertura Comercial | 7 |
| 10 | Gestión de Oportunidades | 8 |
| 11 | Forecast | 7 |
| 12 | Ciclo de Ventas | 7 |
| **Total** | | **89** |

---

## Funnel de Ventas

### SAL-001
**Pattern_Name:** Embudo Angosto en Etapa Temprana
**Category:** Funnel de Ventas
**Description:** El funnel de ventas tiene pocos leads u oportunidades en las etapas tempranas (prospección, contacto inicial), lo que limita la capacidad de generar clientes a mediano plazo independientemente de la eficiencia en etapas posteriores.
**Observable_Symptoms:** Bajo volumen de leads entrantes; el equipo comercial pasa más tiempo en administración que en prospección; pipeline de oportunidades con pocas opciones en etapas iniciales; alta conversión de lead a cliente pero pocos leads; sensación de que "faltan oportunidades".
**Early_Warning_Signals:** Lead generation < 3x la meta de clientes nuevos; ratio de oportunidades en etapa temprana vs etapa tardía < 1:1; cobertura de pipeline (oportunidades / meta) < 3x; número de actividades de prospección por vendedor en descenso.
**Typical_Causes:** Falta de inversión en generación de demanda; equipo comercial reactivo (espera leads); sin proceso de prospección estructurado; marketing digital insuficiente o inefectivo; dependencia de referidos sin cultivarlos.
**Business_Impact:** Crecimiento limitado por falta de leads; volatilidad en resultados comerciales; incapacidad de reemplazar clientes perdidos; presión excesiva sobre conversión para cumplir metas; estancamiento de ingresos.
**Metrics_To_Check:** Leads generados / mes; Costo de Adquisición de Lead; ratio leads a oportunidades; cobertura de pipeline (oportunidades / meta); actividad de prospección por vendedor / semana.
**Diagnostic_Questions:** ¿Cuántos leads nuevos entran al funnel cada semana? ¿La meta de leads nuevos está definida y se monitorea? ¿El equipo dedica tiempo suficiente a prospección? ¿Hay canales de generación de demanda funcionando? ¿Se mide el retorno de inversión en generación de leads?
**Recommended_Actions:** Implementar programa estructurado de prospección; invertir en canales de generación de demanda (inbound, outbound, referidos, redes); asignar tiempo específico a prospección (bloques en agenda); establecer meta de leads por vendedor; medir y optimizar canales de generación.
**Severity_Level:** High
**Related_Patterns:** SAL-002, SAL-009, SAL-017, SAL-025, SAL-056

### SAL-002
**Pattern_Name:** Embudo con Fugas en Etapa de Cierre
**Category:** Funnel de Ventas
**Description:** Una proporción significativa de oportunidades que llegan a etapa de cierre se pierden, indicando problemas en la propuesta de valor, la negociación o la calificación temprana.
**Observable_Symptoms:** Muchas oportunidades avanzan hasta cotización/negociación pero no se cierran; tasa de cierre baja (win rate < 20%); pérdidas en etapa final con justificaciones vagas del cliente; el equipo reporta "competencia agresiva" o "precio" como causa recurrente.
**Early_Warning_Signals:** Win rate en etapa de cierre < 30%; ratio de propuestas enviadas / clientes cerrados > 5:1; pérdidas repetidas contra el mismo competidor; cliente menciona precio/valor en etapas tardías (debió detectarse antes).
**Typical_Causes:** Mala calificación de oportunidades en etapas tempranas (se avanza lo que no califica); propuesta de valor no diferenciada; precio no alineado con valor percibido; objeciones no identificadas tempranamente; falta de habilidades de cierre.
**Business_Impact:** Desperdicio de recursos comerciales en oportunidades no calificadas; frustración del equipo de ventas; tiempo perdido que podría usarse en mejores oportunidades; ingresos por debajo del potencial; rotación de vendedores por baja efectividad.
**Metrics_To_Check:** Win rate por etapa; ratio propuestas / cierres; tiempo en etapa de cierre; causas de pérdida (top 3); win rate contra principal competidor.
**Diagnostic_Questions:** ¿Las oportunidades que llegan a cierre estaban bien calificadas desde el inicio? ¿La propuesta de valor aborda las necesidades específicas del cliente? ¿El precio se presenta después de validar el valor? ¿Se identifican objeciones tempranamente? ¿Hay un proceso de cierre definido?
**Recommended_Actions:** Mejorar calificación de oportunidades (BANT, MEDDIC, etc.) antes de avanzar; desarrollar propuestas de valor diferenciadas; entrenar en manejo de objeciones y cierre; implementar revisión de oportunidades antes de propuesta (deal review); analizar pérdidas sistemáticamente.
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-009, SAL-010, SAL-057, SAL-058, SAL-075

### SAL-003
**Pattern_Name:** Embudo con Estancamiento en Etapa Media
**Category:** Funnel de Ventas
**Description:** Las oportunidades se estancan en la etapa media del funnel (evaluación, demo, propuesta) sin avanzar ni retroceder, generando un pipeline inflado con oportunidades falsas.
**Observable_Symptoms:** Oportunidades que llevan meses en "evaluación" sin avance; pipeline con muchas oportunidades pero pocas que realmente se mueven; vendedores reportan clientes que "están por decidir" durante meses; opportunities sin próxima acción definida.
**Early_Warning_Signals:** % de oportunidades en etapa media > 50% del pipeline; oportunidades sin actividad > 30 días; edad promedio de oportunidades en etapa media > 90 días; ratio de avance (etapa media a tardía) < 20%.
**Typical_Causes:** Falta de proceso de avance de oportunidades (next steps no definidos); vendedores que no califican adecuadamente y mantienen oportunidades falsas para inflar pipeline; clientes sin urgencia real de compra; falta de seguimiento estructurado.
**Business_Impact:** Pipeline inflado que da falsa sensación de cumplimiento; mala asignación de recursos comerciales; forecast poco confiable; energía desperdiciada en oportunidades que no avanzan; imposibilidad de enfocarse en oportunidades reales.
**Metrics_To_Check:** % de oportunidades estancadas (sin actividad > 30 días); edad promedio de oportunidades por etapa; ratio de avance entre etapas; pipeline real vs pipeline nominal; tasa de movimiento semanal de oportunidades.
**Diagnostic_Questions:** ¿Las oportunidades tienen próxima acción y fecha definida? ¿Hay oportunidades con más de 60 días sin avance? ¿Los vendedores tienen incentivos para mantener oportunidades falsas? ¿Hay un proceso de revisión periódica del pipeline? ¿Se purgan oportunidades regularmente?
**Recommended_Actions:** Implementar regla de "próxima acción siempre definida"; revisar pipeline semanalmente purgando oportunidades estancadas; establecer antigüedad máxima por etapa; entrenar en calificación y avance de oportunidades; vincular forecast solo a oportunidades con avance real.
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-009, SAL-056, SAL-075, SAL-076

### SAL-004
**Pattern_Name:** Embudo Estacional con Picos y Valles
**Category:** Funnel de Ventas
**Description:** El volumen del funnel varía drásticamente según la temporada, generando picos de actividad comercial seguidos de valles donde no hay suficientes oportunidades.
**Observable_Symptoms:** Meses con pipeline lleno seguidos de meses con pipeline vacío; el equipo comercial trabaja intensamente en ciertos períodos y está ocioso en otros; dificultad para mantener resultados consistentes mes a mes; presión excesiva en temporada baja.
**Early_Warning_Signals:** Variación mensual de pipeline > 50%; meses con < 2x de cobertura de pipeline; picos de actividad seguidos de inactividad; el equipo comercial tiene capacidad ociosa en meses valle; resultados inconsistentes.
**Typical_Causes:** Estrategia de prospección sin planificación anual; campañas comerciales concentradas en pocos meses; falta de actividades de generación de demanda continua; estacionalidad natural del mercado no gestionada; ausencia de prospección outbound para nivelar.
**Business_Impact:** Resultados comerciales inconsistentes; capacidad comercial subutilizada parte del año; estrés en picos de actividad; imposibilidad de crecer sostenidamente; dificultad para retener talento comercial.
**Metrics_To_Check:** Variación mensual de pipeline; meses con cobertura < 2x; correlación entre actividad de prospección y pipeline; utilización de capacidad comercial por mes; ratio de ingresos por mes (máx / mín).
**Diagnostic_Questions:** ¿Hay actividades de prospección planificadas para todos los meses? ¿Se puede nivelar la generación de demanda a lo largo del año? ¿Hay capacidad comercial ociosa en algunos meses? ¿Se puede hacer prospección outbound en temporada baja? ¿Hay productos/servicios que se vendan en contra-ciclo?
**Recommended_Actions:** Planificar actividades de prospección 12 meses; implementar outbound en temporada baja para llenar pipeline; diversificar oferta para suavizar estacionalidad; establecer metas de pipeline por mes (no solo de ingresos); crear campañas de marketing continuas (no solo en picos).
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-009, SAL-017, SAL-054, SAL-055

### SAL-005
**Pattern_Name:** Velocidad de Embudo Lenta
**Category:** Funnel de Ventas
**Description:** Las oportunidades tardan demasiado en avanzar a través del funnel, desde el primer contacto hasta el cierre, alargando el ciclo de ventas más allá del promedio del sector.
**Observable_Symptoms:** Ciclo de ventas prolongado; oportunidades que se demoran en cada etapa; clientes que piden múltiples reuniones sin avanzar; seguimiento extenso antes de la decisión; sensación de que el proceso es más lento que la competencia.
**Early_Warning_Signals:** Velocidad de funnel (oportunidades/día) en descenso; tiempo promedio por etapa > 2x el benchmark; oportunidades con > 30 días en misma etapa; ratio de conversión bajo combinado con ciclo largo.
**Typical_Causes:** Proceso de ventas no definido ni optimizado; falta de urgencia en el cliente (no se califica necesidad temporal); múltiples stakeholders no identificados; propuesta de valor poco clara; seguimiento no estructurado.
**Business_Impact:** Menor productividad comercial; ingresos que tardan en materializarse; mayor costo de adquisición de clientes; menor capacidad de escalar; forecast incierto.
**Metrics_To_Check:** Velocidad de funnel (etapas/día); tiempo promedio en cada etapa; tiempo total ciclo de ventas; ratio de avance semanal; comparación con benchmark sectorial.
**Diagnostic_Questions:** ¿En qué etapa se pierde más tiempo? ¿El cliente tiene urgencia real de compra? ¿Se identifican todos los stakeholders desde el inicio? ¿Hay un proceso de ventas documentado? ¿El equipo tiene habilidades para avanzar oportunidades?
**Recommended_Actions:** Mapear y optimizar proceso de ventas; implementar criterios de avance por etapa; calificar urgencia como parte del proceso de calificación; entrenar en técnicas de avance de oportunidades; medir velocidad de funnel por vendedor.
**Severity_Level:** Medium
**Related_Patterns:** SAL-002, SAL-003, SAL-009, SAL-056, SAL-075, SAL-083

### SAL-006
**Pattern_Name:** Cobertura de Pipeline Insuficiente
**Category:** Funnel de Ventas
**Description:** El pipeline de oportunidades es insuficiente para cubrir la meta de ingresos, indicando que no hay suficientes oportunidades en desarrollo para alcanzar los objetivos comerciales.
**Observable_Symptoms:** El equipo lucha por encontrar oportunidades para cerrar; presión excesiva sobre pocas oportunidades para cumplir; metas que requieren milagros para alcanzarse; vendedores que dependen de una o dos oportunidades grandes; incertidumbre permanente sobre el cumplimiento.
**Early_Warning_Signals:** Cobertura de pipeline (pipeline / meta) < 3x; ratio de oportunidades por vendedor < 5; pipeline en etapa temprana < 50% del total; cantidad de oportunidades decreciente; pipeline no cubre meta a 90 días.
**Typical_Causes:** Baja actividad de prospección; generación de leads insuficiente; equipo comercial pequeño para la meta; metas no alineadas con capacidad de pipeline; falta de planificación de pipeline.
**Business_Impact:** Incumplimiento recurrente de metas; estrés y presión sobre el equipo; decisiones desesperadas (descuentos, clientes incorrectos); rotación de vendedores; ingresos por debajo del potencial.
**Metrics_To_Check:** Cobertura de pipeline a 30, 60, 90 días; pipeline / meta por vendedor; ratio de oportunidades por vendedor; pipeline en etapa tardía / meta del mes; tendencia de cobertura.
**Diagnostic_Questions:** ¿La cobertura de pipeline es suficiente para la meta (3x recomendado)? ¿Hay suficiente pipeline en etapas tardías para el próximo mes? ¿Cada vendedor tiene suficientes oportunidades? ¿La meta es realista dado el pipeline actual? ¿Hay un plan para generar más pipeline?
**Recommended_Actions:** Establecer meta de pipeline (no solo de ingresos); implementar revisión semanal de pipeline; aumentar actividad de prospección y generación de leads; asignar recursos a generación de demanda; ajustar metas a pipeline realista.
**Severity_Level:** Critical
**Related_Patterns:** SAL-001, SAL-003, SAL-004, SAL-009, SAL-025

### SAL-007
**Pattern_Name:** Pipeline Inflado por Oportunidades Falsas
**Category:** Funnel de Ventas
**Description:** El pipeline contiene muchas oportunidades que no son reales (poco calificadas, sin presupuesto, sin autoridad, sin necesidad), dando una falsa sensación de cobertura.
**Observable_Symptoms:** Pipeline grande pero los resultados no llegan; vendedores con pipelines "llenos" que no cierran; muchas oportunidades en etapas tempranas que nunca avanzan; diferencia significativa entre pipeline reportado y forecast; revisión de pipeline revela oportunidades débiles.
**Early_Warning_Signals:** Tasa de conversión de pipeline a cierre < 10%; % de oportunidades sin BANT/calificación > 40%; oportunidades con edad > 90 días sin avance; vendedores consistentemente sobre-optimistas en forecast; diferencia pipeline vs cierre > 80%.
**Typical_Causes:** Falta de criterios de calificación objetivos; vendedores que inflan pipeline para satisfacer a la gerencia; cultura de "todo es oportunidad"; presión excesiva por pipeline en revisiones; falta de verificación independiente del pipeline.
**Business_Impact:** Forecast siempre errado (optimista); decisiones basadas en pipeline falso; imposibilidad de planificar recursos; gerencia desinformada sobre la realidad comercial; confianza erosionada en el equipo comercial.
**Metrics_To_Check:** Tasa de conversión pipeline a cierre; % de oportunidades calificadas; ratio pipeline real vs nominal; precisión de forecast; % de pipeline perdido en cada etapa.
**Diagnostic_Questions:** ¿Las oportunidades pasan por un proceso de calificación objetivo? ¿Hay criterios claros de qué es una oportunidad? ¿Los vendedores son penalizados por oportunidades que no se concretan? ¿Hay verificación independiente del pipeline? ¿Se purga el pipeline regularmente?
**Recommended_Actions:** Implementar criterios objetivos de calificación (BANT, MEDDIC, etc.); revisar pipeline semanalmente con foco en calidad; purgar oportunidades no calificadas; vincular forecast solo a oportunidades cualificadas; entrenar en diferencia entre "prospecto" y "oportunidad".
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-003, SAL-009, SAL-056, SAL-075

### SAL-008
**Pattern_Name:** Dependencia de Lead Generation de Terceros
**Category:** Funnel de Ventas
**Description:** La empresa depende exclusivamente de generación de leads externa (agencias, plataformas, referidos) sin desarrollar canales propios, perdiendo control sobre su pipeline.
**Observable_Symptoms:** El pipeline depende de leads comprados o generados por terceros; si la fuente externa se corta, no hay leads; alto costo de adquisición de leads; poca visibilidad de cómo se generan los leads; calidad variable de leads externos.
**Early_Warning_Signals:** > 70% de leads provienen de una fuente externa; Costo de Adquisición de Lead > 30% del ticket promedio; tasa de conversión de leads externos < leads orgánicos; dependencia de un solo proveedor de leads; sin inversión en canales propios.
**Typical_Causes:** Falta de capacidad interna de generación de leads; cultura de "comprar leads" en lugar de generarlos; falta de inversión en marketing de contenidos; desconocimiento de canales orgánicos; urgencia por resultados rápidos.
**Business_Impact:** Dependencia peligrosa de terceros; costo de adquisición elevado; poca previsibilidad del pipeline; imposibilidad de escalar por costo; riesgo de que el proveedor cambie condiciones o desaparezca.
**Metrics_To_Check:** % de leads por fuente; diversificación de fuentes de leads; costo de lead por fuente; conversión por fuente; dependencia de top 3 fuentes.
**Diagnostic_Questions:** ¿Qué pasaría si la principal fuente de leads se corta? ¿Se está invirtiendo en canales propios de generación? ¿Hay diversificación de fuentes? ¿El costo de leads externos es sostenible? ¿Se puede generar leads internamente?
**Recommended_Actions:** Desarrollar canales propios de generación (contenido, SEO, redes, referidos); diversificar fuentes de leads (mínimo 5 canales); reducir gradualmente dependencia de terceros; invertir en marketing de contenidos y presencia digital; medir efectividad por fuente.
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-006, SAL-009, SAL-017, SAL-025


## Conversión

### SAL-009
**Pattern_Name:** Tasa de Conversión Global Baja
**Category:** Conversión
**Description:** La tasa de conversión de lead a cliente es baja en relación al promedio del sector, indicando problemas en el proceso comercial, la calificación de leads o la propuesta de valor.
**Observable_Symptoms:** Muchos leads entran pero pocos se convierten en clientes; el equipo comercial trabaja mucho pero cierra poco; embudo con base ancha y salida angosta; leads que desaparecen sin seguimiento; sensación de "molino que muele pero no produce".
**Early_Warning_Signals:** Tasa de conversión lead a cliente < 10% (o < 50% del benchmark sectorial); ratio de leads a reuniones < 30%; ratio reuniones a propuestas < 40%; ratio propuestas a cierres < 20%; tasa de conversión decreciente.
**Typical_Causes:** Mala calificación de leads (se persiguen leads no calificados); proceso de ventas no definido; propuesta de valor poco convincente; falta de seguimiento estructurado; equipo sin habilidades de conversión; precio no competitivo.
**Business_Impact:** Bajo retorno de inversión en generación de leads; equipo comercial desmotivado; costos de adquisición elevados; crecimiento limitado por baja eficiencia; necesidad de más leads para compensar baja conversión.
**Metrics_To_Check:** Tasa de conversión lead a oportunidad; oportunidad a propuesta; propuesta a cierre; tasa de conversión global; comparación con benchmark del sector.
**Diagnostic_Questions:** ¿En qué etapa del proceso se pierden más leads? ¿Los leads están bien calificados antes de pasar a ventas? ¿Hay un proceso de ventas definido y seguido? ¿El equipo tiene habilidades de conversión? ¿Hay seguimiento estructurado de leads?
**Recommended_Actions:** Definir y documentar proceso de ventas; implementar lead scoring para calificar leads; entrenar al equipo en técnicas de conversión; establecer SLA de seguimiento; analizar pérdidas por etapa y corregir.
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-002, SAL-010, SAL-017, SAL-025

### SAL-010
**Pattern_Name:** Conversión Variable por Vendedor
**Category:** Conversión
**Description:** Existe una gran variabilidad en las tasas de conversión entre vendedores, indicando que el éxito depende más de habilidades individuales que del proceso.
**Observable_Symptoms:** Algunos vendedores cierran mucho mientras otros luchan; no hay estándar de conversión entre el equipo; los nuevos vendedores tardan mucho en alcanzar productividad; el mejor vendedor cierra 3x más que el promedio; no hay procesos replicables.
**Early_Warning_Signals:** Desviación estándar de conversión entre vendedores > 40% del promedio; ratio de conversión mejor vendedor / peor vendedor > 5x; nuevos vendedores con período de ramp-up > 6 meses; falta de correlación entre actividad y resultados.
**Typical_Causes:** Falta de proceso de ventas estandarizado; vendedores trabajan de forma aislada sin compartir mejores prácticas; entrenamiento insuficiente o inexistente; cultura de "cada vendedor tiene su método"; falta de herramientas de ventas comunes.
**Business_Impact:** Riesgo de concentración de ingresos en pocos vendedores; dificultad para escalar el equipo; nuevos vendedores tardan en ser productivos; rotación de vendedores de bajo rendimiento; resultados inconsistentes.
**Metrics_To_Check:** Tasa de conversión por vendedor; desviación estándar de conversión; ratio mejor/peor vendedor; tiempo de ramp-up de nuevos vendedores; correlación actividad vs conversión.
**Diagnostic_Questions:** ¿Hay un proceso de ventas documentado que todos siguen? ¿Los mejores vendedores comparten sus prácticas? ¿Hay entrenamiento regular? ¿Los nuevos vendedores reciben capacitación estructurada? ¿Se utiliza CRM para estandarizar procesos?
**Recommended_Actions:** Documentar y estandarizar proceso de ventas; implementar entrenamiento regular basado en mejores prácticas; establecer programa de onboarding estructurado; usar CRM para forzar proceso; realizar sesiones de peer learning entre vendedores.
**Severity_Level:** Medium
**Related_Patterns:** SAL-002, SAL-009, SAL-017, SAL-025, SAL-083

### SAL-011
**Pattern_Name:** Fuga de Leads por Falta de Seguimiento
**Category:** Conversión
**Description:** Una proporción significativa de leads se pierde porque no reciben seguimiento oportuno o consistente, ya sea porque se olvidan, se enfrían o se priorizan incorrectamente.
**Observable_Symptoms:** Leads que quedan sin contactar por días o semanas; leads que desaparecen sin explicación; clientes que mencionan que "nadie los contactó"; falta de sistema de recordatorios; vendedores abrumados por cantidad de leads y priorizan solo algunos.
**Early_Warning_Signals:** Tiempo de respuesta a lead > 24 horas; % de leads sin seguimiento > 20%; leads perdidos por falta de contacto (no por rechazo); volumen de leads > capacidad de seguimiento; sin sistema de asignación y seguimiento de leads.
**Typical_Causes:** Exceso de leads para la capacidad del equipo; falta de proceso de asignación de leads; sin SLA de seguimiento; CRM no utilizado o mal configurado; vendedores que priorizan leads grandes ignorando pequeños.
**Business_Impact:** Desperdicio de inversión en generación de leads; leads que se enfrían y son más difíciles de convertir; mala experiencia del cliente potencial; pérdida de ingresos potenciales; ineficiencia comercial.
**Metrics_To_Check:** Tiempo de respuesta a lead; % de leads con seguimiento en < 24h; % de leads perdidos por falta de seguimiento; ratio leads asignados / capacidad de vendedor; lead aging sin contacto.
**Diagnostic_Questions:** ¿Cuánto tiempo pasa entre que un lead entra y se contacta? ¿Hay leads que nunca se contactan? ¿El volumen de leads supera la capacidad del equipo? ¿Hay un sistema de alertas para leads sin seguimiento? ¿Se priorizan leads por tamaño o por probabilidad?
**Recommended_Actions:** Implementar SLA de seguimiento (< 1 hora para leads calientes, < 24 horas para todos); automatizar asignación de leads en CRM; configurar alertas de leads sin seguimiento; ajustar capacidad de generación a capacidad de seguimiento; implementar lead nurturing para leads que requieren más tiempo.
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-009, SAL-012, SAL-025, SAL-075

### SAL-012
**Pattern_Name:** Conversión Alta en Leads Fríos vs Calientes
**Category:** Conversión
**Description:** Los leads fríos o no calificados se convierten a tasas similares o superiores que los leads calientes, indicando que el sistema de lead scoring o calificación no funciona.
**Observable_Symptoms:** Leads que parecen fríos se convierten en clientes mientras leads calientes no; sorpresas sobre qué leads se convierten; el equipo no confía en el sistema de calificación; inversión en generación de leads calientes no se refleja en conversión; leads "random" cierran más que los segmentos objetivo.
**Early_Warning_Signals:** Tasa de conversión de leads fríos > leads calientes; correlación baja entre lead score y conversión; % de ingresos de leads no calificados > 30%; leads de canales no prioritarios con mejor conversión; equipo ignora el lead scoring.
**Typical_Causes:** Sistema de lead scoring mal diseñado (criterios incorrectos); datos de leads incorrectos o desactualizados; segmentación de mercado incorrecta; definición de "lead caliente" basada en supuestos no validados; falta de retroalimentación de ventas a marketing.
**Business_Impact:** Mala asignación de recursos de generación de leads; equipo comercial persiguiendo leads incorrectos; inversión en canales equivocados; pérdida de leads que realmente podrían convertirse; sistema de calificación que nadie usa.
**Metrics_To_Check:** Tasa de conversión por score/categoría de lead; correlación lead score vs conversión; % de ingresos por categoría de lead; efectividad de canales por conversión (no solo volumen).
**Diagnostic_Questions:** ¿El sistema de lead scoring está basado en datos reales de conversión? ¿Se revisa y actualiza periódicamente? ¿Hay retroalimentación de ventas a marketing sobre calidad de leads? ¿Los criterios de lead scoring reflejan al cliente ideal (ICP)? ¿Se ha validado la segmentación de mercado?
**Recommended_Actions:** Revisar y recalibrar lead scoring basado en datos históricos; implementar retroalimentación sistemática de ventas a marketing; validar ICP (cliente ideal) con datos de clientes reales; testear diferentes criterios de calificación; segmentar leads por comportamiento y datos firmográficos.
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-009, SAL-011, SAL-015, SAL-025

### SAL-013
**Pattern_Name:** Conversión que Cae al Aumentar Volumen
**Category:** Conversión
**Description:** La tasa de conversión disminuye cuando aumenta el volumen de leads, indicando que el equipo comercial no puede manejar picos de demanda y la calidad del proceso se resiente.
**Observable_Symptoms:** En meses con muchos leads, la conversión cae; el equipo se siente abrumado cuando hay alta demanda; leads se desperdician en períodos de alta actividad; calidad de seguimiento disminuye con el volumen; relación inversa entre leads entrantes y tasa de cierre.
**Early_Warning_Signals:** Correlación negativa entre volumen de leads y tasa de conversión; caída de conversión > 20% en meses de pico; tiempo de respuesta a lead aumenta con el volumen; leads sin seguimiento aparecen en meses de alta demanda; equipo comercial saturado.
**Typical_Causes:** Capacidad comercial fija vs demanda variable; falta de capacidad de escalamiento; proceso no diseñado para alto volumen; sin automatización de procesos de seguimiento; equipo que prioriza cantidad sobre calidad cuando hay presión.
**Business_Impact:** Desperdicio de inversión en generación de leads en picos; resultados inconsistentes; equipo quemado por sobrecarga; leads valiosos perdidos en momentos de alta demanda; imposibilidad de capitalizar picos de demanda.
**Metrics_To_Check:** Correlación volumen leads vs conversión; tasa de conversión por tramo de volumen; tiempo de respuesta vs volumen; leads sin seguimiento en picos; capacidad de seguimiento máxima del equipo.
**Diagnostic_Questions:** ¿Cuántos leads puede procesar el equipo sin perder calidad? ¿Hay capacidad de escalar en picos? ¿Se puede automatizar parte del proceso? ¿Hay un plan de contingencia para picos de demanda? ¿Se puede nivelar la generación de leads?
**Recommended_Actions:** Establecer capacidad máxima de leads por vendedor; automatizar lead nurturing para picos; implementar sistema de colas con priorización; considerar capacidad variable (freelance, temporal); nivelar campañas de generación para evitar picos.
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-009, SAL-011, SAL-017, SAL-025

### SAL-014
**Pattern_Name:** Conversión Reactiva vs Proactiva
**Category:** Conversión
**Description:** La empresa depende exclusivamente de conversión reactiva (el cliente busca) sin capacidad de conversión proactiva (outbound, venta consultiva), limitando el control sobre el pipeline.
**Observable_Symptoms:** Solo se vende a clientes que llegan por iniciativa propia; el equipo no prospecta activamente; cuando baja la demanda entrante, bajan las ventas; falta de capacidad de generar demanda; el equipo no sabe vender de forma consultiva.
**Early_Warning_Signals:** > 80% de ingresos de leads inbound; cero actividad de prospección outbound; caída de ventas cuando baja el marketing; equipo que no sabe hacer llamadas en frío; sin proceso de venta consultiva.
**Typical_Causes:** Cultura de "esperar a que el cliente venga"; falta de habilidades de venta proactiva; equipo acostumbrado a leads calientes; falta de herramientas y procesos outbound; percepción de que outbound no funciona (mala experiencia previa).
**Business_Impact:** Vulnerabilidad a cambios en demanda entrante; incapacidad de crecer activamente; equipo que no desarrolla habilidades completas; límite al crecimiento por capacidad de atracción; desventaja competitiva.
**Metrics_To_Check:** % de ingresos inbound vs outbound; actividad de prospección outbound por vendedor; tasa de conversión outbound; número de citas generadas por outbound; ROI de actividades outbound.
**Diagnostic_Questions:** ¿El equipo sabe prospectar activamente? ¿Hay un proceso de venta outbound definido? ¿Se han evaluado canales outbound? ¿Hay incentivos para la prospección activa? ¿Qué pasa si baja la demanda entrante?
**Recommended_Actions:** Desarrollar capacidad de venta outbound; entrenar en prospección y venta consultiva; implementar proceso de outbound estructurado; establecer metas de actividad outbound; crear incentivos para prospección activa; balancear inbound y outbound.
**Severity_Level:** Medium
**Related_Patterns:** SAL-001, SAL-004, SAL-008, SAL-009, SAL-017

### SAL-015
**Pattern_Name:** Leads Calificados que No Cierran
**Category:** Conversión
**Description:** Una proporción de leads que pasan todos los criterios de calificación (presupuesto, autoridad, necesidad, tiempo) no se convierten en clientes, indicando problemas en la propuesta de valor o en el proceso de cierre.
**Observable_Symptoms:** Leads BANT+ que se pierden en etapa de cierre; clientes que "deberían comprar" pero no lo hacen; pérdidas sin explicación clara después de avanzar hasta cotización; clientes que alaban el producto pero no compran; objeciones de último momento.
**Early_Warning_Signals:** Tasa de cierre de leads calificados < 40%; pérdidas en etapa de cierre sin causa identificada; clientes que desaparecen después de la propuesta; objeciones de precio en etapa tardía (debieron detectarse antes); competidor gana sin ser claramente superior.
**Typical_Causes:** Propuesta de valor no diferenciada realmente; precio no justificado frente a alternativas; falta de sentido de urgencia en el cliente; no se identificó al decisor real; objeciones no manejadas adecuadamente; competidor con mejor solución o relación.
**Business_Impact:** Desperdicio de recursos en oportunidad que debió cerrarse; frustración del equipo; forecast incorrecto; ingresos dejados sobre la mesa; necesidad de más leads para compensar.
**Metrics_To_Check:** Tasa de cierre de leads calificados; causas de pérdida (top 5); tiempo en etapa de cierre; comparación win/loss contra competidores; % de oportunidades perdidas en etapa final.
**Diagnostic_Questions:** ¿Por qué estos leads calificados no compran? ¿Hay un competidor específico que gana? ¿El precio es realmente el problema o es una excusa? ¿Se identificó al decisor correcto? ¿Se creó urgencia? ¿La propuesta de valor es realmente diferenciadora?
**Recommended_Actions:** Analizar pérdidas en detalle (revisión win/loss); fortalecer propuesta de valor y diferenciación; entrenar en manejo de objeciones y cierre; validar que se habla con el decisor correcto; crear urgencia en el proceso de venta; hacer seguimiento post-pérdida.
**Severity_Level:** High
**Related_Patterns:** SAL-002, SAL-009, SAL-010, SAL-057, SAL-083

### SAL-016
**Pattern_Name:** Conversión Estancada por Falta de Urgencia
**Category:** Conversión
**Description:** Los leads tienen necesidad y presupuesto pero no tienen urgencia de compra, por lo que las conversaciones se alargan indefinidamente sin concretarse.
**Observable_Symptoms:** Clientes que dicen "nos interesa pero no es el momento"; oportunidades que se posponen trimestre a trimestre; leads que vuelven a aparecer cíclicamente sin comprar; falta de "trigger events" en el proceso de venta; clientes que están en "evaluación permanente".
**Early_Warning_Signals:** Tiempo promedio en etapa de decisión > 60 días; % de oportunidades con "sin fecha estimada" > 30%; clientes que reaparecen cada 3-6 meses sin comprar; falta de eventos desencadenantes identificados; ratio de retorno de leads sin compra.
**Typical_Causes:** No se calificó la urgencia al inicio del proceso; falta de eventos de presión (cambios regulatorios, vencimientos, temporada); propuesta de valor no urgente; cliente no percibe costo de esperar; vendedor no crea urgencia.
**Business_Impact:** Ciclo de ventas prolongado; recursos invertidos en oportunidades que no cierran; pipeline inflado con oportunidades sin avance; forecast incierto; costo de adquisición elevado.
**Metrics_To_Check:** Tiempo promedio en etapa de decisión; % de oportunidades sin fecha de cierre; ratio de retorno de leads (vuelven pero no compran); edad promedio de oportunidades abiertas; tasa de cierre de oportunidades con urgencia vs sin urgencia.
**Diagnostic_Questions:** ¿Se califica la urgencia al inicio del proceso? ¿Hay trigger events identificados para el cliente? ¿El cliente percibe un costo de no comprar? ¿Se ha creado urgencia artificial (ofertas limitadas)? ¿Hay eventos externos que generen urgencia?
**Recommended_Actions:** Calificar urgencia como criterio de avance (no solo BANT); identificar y crear trigger events; ofertas con tiempo limitado o descuento por pronto cierre; educar al cliente sobre costo de esperar; establecer fechas de revisión de oportunidad con deadline.
**Severity_Level:** Medium
**Related_Patterns:** SAL-002, SAL-003, SAL-009, SAL-015, SAL-056


## Ticket Promedio

### SAL-017
**Pattern_Name:** Ticket Promedio en Caída
**Category:** Ticket Promedio
**Description:** El ticket promedio de venta muestra una tendencia decreciente, indicando que se vende más barato o a clientes más pequeños, comprimiendo el margen sin compensación en volumen.
**Observable_Symptoms:** Ingresos crecen menos que cantidad de transacciones; clientes nuevos compran menos que clientes antiguos; presión por reducir precios para cerrar ventas; mezcla de ventas hacia productos/servicios de menor valor; descuentos crecientes.
**Early_Warning_Signals:** Ticket promedio en descenso 3+ trimestres consecutivos; ratio ingresos / transacciones decreciente; % de ventas de productos/servicios de alto valor en caída; descuentos / ticket promedio en aumento; ticket promedio de clientes nuevos < ticket de clientes existentes.
**Typical_Causes:** Presión competitiva que fuerza reducción de precios; mezcla de ventas hacia productos de entrada; enfoque en volumen sobre valor; descuentos excesivos para cerrar; falta de upselling/cross-selling.
**Business_Impact:** Menor rentabilidad por transacción; necesidad de más volumen para mantener ingresos; mayor costo operativo por mayor cantidad de transacciones; deterioro del margen; esfuerzo comercial no compensado.
**Metrics_To_Check:** Ticket promedio mensual (tendencia); ticket promedio por segmento de cliente; ticket promedio cliente nuevo vs recurrente; % de ventas de alto valor; descuentos / ticket promedio.
**Diagnostic_Questions:** ¿El ticket cae por mezcla de productos o por descuentos? ¿Se está vendiendo a clientes más pequeños? ¿Hay presión competitiva por precio? ¿El equipo comercial tiene incentivos para vender valor o volumen? ¿Se hace upselling/cross-selling?
**Recommended_Actions:** Entrenar en venta por valor (no por precio); ajustar incentivos a ticket y margen (no solo volumen); implementar upselling y cross-selling en el proceso de venta; revisar política de descuentos; desarrollar productos/servicios de alto valor.
**Severity_Level:** High
**Related_Patterns:** SAL-018, SAL-019, SAL-027, SAL-035, SAL-048, SAL-049

### SAL-018
**Pattern_Name:** Ticket Promedio Bajo vs Competidores
**Category:** Ticket Promedio
**Description:** El ticket promedio de la empresa es significativamente menor que el de competidores directos, indicando que no está capturando el valor completo de su oferta.
**Observable_Symptoms:** Clientes mencionan que los precios son "bajos" vs competencia; la empresa vende más unidades pero gana menos que competidores; comparación de ingresos por cliente vs benchmark desfavorable; sensación de dejar dinero sobre la mesa.
**Early_Warning_Signals:** Ticket promedio < 70% del benchmark sectorial; % de descuento sobre precio de lista > 20%; clientes dispuestos a pagar más pero no se les pide; precio de venta por debajo del valor percibido por el cliente; comparación de ingresos por cliente desfavorable.
**Typical_Causes:** Falta de confianza para pedir precios más altos; propuesta de valor no comunicada adecuadamente; política de precios conservadora; venta basada en precio en lugar de valor; equipo comercial no entrenado en negociación.
**Business_Impact:** Menor rentabilidad y generación de caja; necesidad de más clientes para alcanzar metas; subvaloración de la oferta en el mercado; imposibilidad de invertir en mejora de producto/servicio; desventaja para escalar.
**Metrics_To_Check:** Ticket promedio vs benchmark; precio de venta vs precio de lista; % de descuento promedio; valor percibido por cliente (encuestas); ingresos por cliente vs competidores.
**Diagnostic_Questions:** ¿Cuál es el ticket promedio de los competidores? ¿Los clientes perciben que el precio es bajo? ¿Se comunica el valor antes del precio? ¿El equipo tiene habilidades de negociación? ¿Hay temor a perder ventas si se suben precios?
**Recommended_Actions:** Revisar estrategia de precios; entrenar en venta por valor y negociación; comunicar valor antes de presentar precio; segmentar clientes por disposición a pagar; hacer pruebas de aumento de precio en segmentos; mejorar propuesta de valor.
**Severity_Level:** High
**Related_Patterns:** SAL-017, SAL-019, SAL-035, SAL-048, SAL-049

### SAL-019
**Pattern_Name:** Ticket Concentrado en Producto de Bajo Valor
**Category:** Ticket Promedio
**Description:** La mayor parte de los ingresos proviene de productos o servicios de bajo ticket, mientras que las ofertas de alto valor tienen baja penetración.
**Observable_Symptoms:** El producto/servicio de entrada (bajo ticket) representa > 60% de ingresos; productos de alto valor tienen baja adopción; los clientes compran la opción más básica; el equipo no ofrece alternativas superiores; la empresa es percibida como "barata".
**Early_Warning_Signals:** % de ingresos de producto estrella (si es de bajo valor) > 60%; ratio de venta de producto básico vs premium > 5:1; % de clientes que compran producto de alto valor < 20%; ticket de cliente nuevo consistentemente en el rango más bajo.
**Typical_Causes:** Proceso de venta no incluye oferta de opciones superiores; equipo no capacitado para vender productos de alto valor; productos de alto valor mal diseñados o posicionados; incentivos basados en volumen (no en valor); clientes no conocen las opciones superiores.
**Business_Impact**: Bajo crecimiento de ingresos; rentabilidad sub-óptima; esfuerzo comercial no maximizado; clientes que podrían comprar más pero no se les ofrece; posición de mercado de bajo valor.
**Metrics_To_Check:** % de ingresos por línea de producto; penetración de productos de alto valor; ratio venta básica / premium; ticket promedio por vendedor; % de clientes que compran opción superior.
**Diagnostic_Questions:** ¿Los vendedores ofrecen opciones superiores en cada venta? ¿Hay un proceso de "next best offer"? ¿Los clientes conocen todas las opciones disponibles? ¿Los productos de alto valor tienen buena relación calidad-precio? ¿Los incentivos comerciales favorecen la venta de alto valor?
**Recommended_Actions:** Incorporar oferta de opciones superiores en el proceso de venta; entrenar en venta de valor agregado; ajustar incentivos para favorecer venta de alto valor; revisar posicionamiento de productos premium; diseñar programas de upgrade post-venta.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-018, SAL-035, SAL-048, SAL-049

### SAL-020
**Pattern_Name:** Descuentos que Erosionan el Ticket
**Category:** Ticket Promedio
**Description:** La política de descuentos es agresiva y no controlada, erosionando el ticket promedio y el margen sin que se traduzca en mayor volumen de ventas.
**Observable_Symptoms:** Descuentos frecuentes y significativos; los clientes esperan descuento y negocian siempre; el margen neto es muy inferior al margen de lista; descuentos que no están justificados por volumen o relación; el equipo da descuento sin autorización.
**Early_Warning_Signals:** % de descuento promedio > 15%; descuentos / ventas en aumento; margen neto vs margen bruto con diferencia creciente; % de ventas con descuento > 60%; descuentos sin correlación con volumen o fidelidad.
**Typical_Causes:** Falta de política de descuentos formal; presión por cumplir metas lleva a concesiones; equipo comercial usa descuento como muleta para cerrar; clientes entrenados para pedir descuento; sin consecuencias por descontar en exceso.
**Business_Impact:** Erosión del margen y rentabilidad; ticket promedio artificialmente bajo; clientes que no valoran el producto a precio completo; dependencia de descuentos para vender; cultura de "regateo" en la fuerza de ventas.
**Metrics_To_Check:** % de descuento promedio; % de ventas con descuento; margen neto vs margen de lista; ticket con descuento vs sin descuento; descuento promedio por vendedor.
**Diagnostic_Questions:** ¿Hay una política de descuentos documentada? ¿Los descuentos requieren aprobación? ¿Se analiza el impacto de descuentos en margen? ¿Hay vendedores que descuentan más que otros? ¿Los descuentos generan realmente más volumen?
**Recommended_Actions:** Implementar política de descuentos con niveles de autorización; entrenar en negociación basada en valor (no en precio); medir y publicar descuento por vendedor; desincentivar descuentos no justificados; probar períodos sin descuentos y medir impacto.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-018, SAL-019, SAL-035, SAL-048

### SAL-021
**Pattern_Name:** Ticket Estancado sin Crecimiento
**Category:** Ticket Promedio
**Description:** El ticket promedio se mantiene plano sin crecimiento a pesar de la inflación y el aumento de costos, erosionando el margen real año tras año.
**Observable_Symptoms:** Ticket promedio no se actualiza con inflación; ingresos por cliente crecen por debajo de la inflación; el margen real se comprime; la empresa no traslada aumentos de costos a precios; clientes pagan lo mismo que hace años.
**Early_Warning_Signals:** Ticket promedio sin cambios en 12+ meses; diferencia entre inflación acumulada y crecimiento de ticket; margen bruto en caída libre por costos crecientes; precio de venta congelado mientras costos suben; falta de revisión periódica de precios.
**Typical_Causes:** Miedo a perder clientes por aumento de precios; falta de revisión periódica de precios; proceso de fijación de precios no vinculado a costos; cultura de "no aumentar precios"; competidores que no aumentan.
**Business_Impact:** Erosión silenciosa del margen; rentabilidad decreciente; necesidad de más volumen para compensar; eventual inviabilidad del negocio si costos siguen subiendo; pérdida de valor real.
**Metrics_To_Check:** Ticket promedio real vs inflación; margen bruto (tendencia); frecuencia de actualización de precios; diferencia entre aumento de costos y aumento de precios; elasticidad precio de la demanda.
**Diagnostic_Questions:** ¿Cuándo fue la última vez que se actualizaron los precios? ¿La inflación de costos se traslada a precios? ¿Hay miedo a perder clientes? ¿Se ha probado aumentar precios en algún segmento? ¿Los competidores han aumentado precios?
**Recommended_Actions:** Establecer revisión periódica de precios (trimestral); indexar precios a inflación o costos; segmentar clientes para pruebas de aumento; comunicar aumentos basados en valor agregado; monitorear elasticidad precio para ajustar.
**Severity_Level:** High
**Related_Patterns:** SAL-017, SAL-018, SAL-020, SAL-035, SAL-048

### SAL-022
**Pattern_Name:** Ticket de Primera Compra Bajo
**Category:** Ticket Promedio
**Description:** El ticket de primera compra es significativamente menor que el ticket de compras recurrentes, indicando que los nuevos clientes empiezan con productos/servicios de entrada y no se les incentiva a comprar más desde el inicio.
**Observable_Symptoms:** Clientes nuevos compran la opción más barata; el primer pedido es pequeño comparado con clientes recurrentes; falta de oferta de upgrade en primera compra; proceso de onboarding no incluye venta adicional; el equipo no invierte en clientes nuevos por su bajo ticket.
**Early_Warning_Signals:** Ticket primera compra / ticket recurrente < 0.5; % de clientes que empiezan con producto básico > 70%; sin oferta de upgrade en primera compra; caída del ticket promedio por incorporación de muchos clientes nuevos.
**Typical_Causes:** Proceso de venta orientado a cerrar rápido sin buscar ampliar; equipo comercial enfocado en cantidad de clientes no en valor inicial; falta de ofertas de entrada + upgrade; miedo a pedir más en primera venta; política de "primero que compre, después se vende más".
**Business_Impact:** Bajo retorno de inversión en adquisición de clientes; ciclo largo para recuperar CAC; clientes que se acostumbran al precio bajo; menor ingresos totales por cliente; esfuerzo comercial no optimizado.
**Metrics_To_Check:** Ticket primera compra vs recurrente; % de primera compra con producto básico; tiempo de primera compra a primera expansión; ratio LTV/CAC ajustado por ticket inicial.
**Diagnostic_Questions:** ¿Se ofrece una opción superior en la primera compra? ¿Hay un proceso de "land and expand"? ¿Los clientes conocen todas las opciones desde el inicio? ¿Hay un programa de onboarding con venta adicional? ¿Los incentivos favorecen ticket inicial o largo plazo?
**Recommended_Actions:** Incluir oferta de opciones superiores en primera venta; diseñar programa de "land and expand"; crear bundles de entrada con opción de upgrade; ajustar incentivos a valor inicial + potencial; mejorar proceso de onboarding con cross-selling temprano.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-019, SAL-023, SAL-035, SAL-048, SAL-049

### SAL-023
**Pattern_Name:** Ticket Promedio por Canal Muy Dispar
**Category:** Ticket Promedio
**Description:** Existe una gran diferencia en el ticket promedio entre canales de venta (online, presencial, distribuidores, fuerza de ventas), indicando que la estrategia de precios y valor no es consistente.
**Observable_Symptoms:** Mismo producto se vende a precios muy diferentes según canal; canales de bajo costo tienen tickets más altos (o viceversa); canibalización entre canales; clientes que compran en canal barato y se quejan de precios en otro; conflictos entre canales.
**Early_Warning_Signals:** Diferencia de ticket entre canales > 30%; canal de menor costo tiene menor ticket (o al revés sin explicación); % de ventas en canal de bajo ticket creciendo sobre canales de alto ticket; quejas de distribuidores por precios inconsistentes; conflictos entre canales.
**Typical_Causes**: Estrategia de precios no coordinada por canal; estructura de comisiones diferente por canal; canales con poder de fijar precios independientemente; falta de política de precio mínimo (MAP); canales nuevos que compiten con precio.
**Business_Impact:** Canibalización entre canales; erosión de margen global; conflictos de canal; imagen de precio inconsistente; clientes que eligen canal por precio en lugar de valor.
**Metrics_To_Check:** Ticket promedio por canal; margen por canal; % de ventas por canal; correlación entre crecimiento de canal y canibalización; cumplimiento de precio mínimo por canal.
**Diagnostic_Questions:** ¿Hay una estrategia de precios por canal definida? ¿Los precios son consistentes entre canales? ¿Hay política de precio mínimo? ¿Los canales canibalizan ventas entre sí? ¿El margen varía significativamente por canal?
**Recommended_Actions:** Definir estrategia de precios por canal con reglas claras; implementar política de precio mínimo (MAP); segmentar ofertas por canal para evitar canibalización; medir contribución neta por canal (considerando canibalización); alinear incentivos con estrategia de canal.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-018, SAL-020, SAL-035, SAL-048


## Productividad Comercial

### SAL-024
**Pattern_Name:** Baja Productividad por Vendedor
**Category:** Productividad Comercial
**Description:** Los vendedores generan ingresos por debajo del benchmark del sector o por debajo de su costo total, indicando que la fuerza de ventas no es rentable o eficiente.
**Observable_Symptoms:** Ingresos por vendedor estancados o decrecientes; vendedores que no cubren su costo (sueldo + gastos); equipo grande pero resultados no proporcionales; muchas actividades pero pocos cierres; comparación desfavorable con competidores o años anteriores.
**Early_Warning_Signals:** Ingresos por vendedor < 5x su costo total; tendencia decreciente en ingresos por vendedor; ratio de actividades a cierres bajo; % de vendedores que no alcanzan meta > 40%; productividad por vendedor por debajo de benchmark.
**Typical_Causes:** Vendedores dedican tiempo a tareas no comerciales; falta de herramientas de productividad; territorios mal asignados; procesos ineficientes; vendedores con habilidades inadecuadas; pocas oportunidades por falta de leads.
**Business_Impact:** Fuerza de ventas no rentable; necesidad de más vendedores para crecer o mantener; altos costos fijos en compensación; imposibilidad de escalar; rotación y desmotivación.
**Metrics_To_Check:** Ingresos por vendedor; ingresos / costo total del vendedor; ratio de actividades comerciales vs administrativas; % de tiempo en ventas; productividad por vendedor (tendencia).
**Diagnostic_Questions:** ¿Cuánto genera cada vendedor vs su costo? ¿En qué gastan el tiempo los vendedores? ¿Hay herramientas que automaticen tareas no comerciales? ¿Los territorios están bien asignados? ¿El proceso de ventas es eficiente?
**Recommended_Actions:** Liberar tiempo de vendedores de tareas no comerciales (automatización, soporte); implementar herramientas de productividad (CRM, automatización); revisar asignación de territorios; entrenar en habilidades de venta; establecer estándares de productividad mínimos.
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-009, SAL-010, SAL-025, SAL-026, SAL-083

### SAL-025
**Pattern_Name:** Vendedores Dedican Tiempo a Tareas No Comerciales
**Category:** Productividad Comercial
**Description:** Los vendedores invierten una porción significativa de su tiempo en tareas administrativas, de soporte u operativas, reduciendo el tiempo disponible para vender.
**Observable_Symptoms:** Vendedores que se quejan de "no tener tiempo para vender"; mucha actividad pero poca venta; vendedores haciendo tareas de soporte, facturación, logística; días ocupados sin resultados de venta; reuniones internas excesivas.
**Early_Warning_Signals:** % de tiempo en ventas < 40%; ratio de horas administrativas / horas de venta > 1:1; vendedores que gestionan soporte post-venta; número de reuniones internas / reuniones con clientes > 1:2; vendedores que generan informes manualmente.
**Typical_Causes:** Falta de áreas de soporte (administración, post-venta, customer service); cultura de "el vendedor hace todo"; procesos manuales que consumen tiempo; falta de herramientas de automatización; mala definición de roles.
**Business_Impact:** Baja productividad comercial; vendedores caros haciendo tareas baratas; menor capacidad de generar ingresos; frustración y rotación; necesidad de más vendedores para compensar.
**Metrics_To_Check:** % de tiempo en actividades de venta; ratio tiempo admin / tiempo venta; ingresos por hora de venta; % de tareas no comerciales realizadas por vendedores; horas de venta por semana.
**Diagnostic_Questions:** ¿En qué gastan el tiempo los vendedores? ¿Qué tareas no comerciales realizan? ¿Hay áreas de soporte que puedan asumir esas tareas? ¿Hay herramientas que automaticen procesos? ¿Están claramente definidos los roles?
**Recommended_Actions:** Transferir tareas no comerciales a áreas de soporte; automatizar procesos administrativos; definir claramente el rol del vendedor; implementar CRM que centralice información; medir y optimizar tiempo en ventas.
**Severity_Level:** High
**Related_Patterns:** SAL-024, SAL-026, SAL-027, SAL-083

### SAL-026
**Pattern_Name:** Productividad Variable por Territorio
**Category:** Productividad Comercial
**Description:** Existe una gran disparidad en la productividad entre diferentes territorios o zonas de venta, indicando mala asignación de recursos o diferencias de potencial no gestionadas.
**Observable_Symptoms:** Algunos territorios rinden muy por encima de otros; vendedores en zonas "difíciles" consistentemente rinden menos; el mejor territorio genera 3x más que el peor; rotación en territorios de bajo rendimiento; quejas sobre asignación desigual.
**Early_Warning_Signals:** Diferencia de ingresos entre mejor y peor territorio > 3x; producto por vendedor varía > 50% entre territorios; territorios con bajo potencial asignados a vendedores sin recursos; rotación alta en ciertos territorios; falta de análisis de potencial por zona.
**Typical_Causes:** Territorios mal diseñados (tamaño, potencial); asignación histórica no revisada; diferencias de mercado no consideradas; vendedores con habilidades no coinciden con territorio; falta de soporte diferenciado por zona.
**Business_Impact:** Recursos mal asignados; vendedores en territorios difíciles desmotivados; potencial de mercado no explotado; rotación en territorios de bajo rendimiento; resultados generales sub-óptimos.
**Metrics_To_Check:** Ingresos por territorio; productividad por vendedor por territorio; potencial de mercado vs capturado; diferencia entre mejor y peor territorio; rotación por territorio.
**Diagnostic_Questions:** ¿Los territorios están diseñados según potencial de mercado? ¿Se revisa periódicamente la asignación? ¿Hay diferencias de soporte entre territorios? ¿Los vendedores tienen habilidades acordes al territorio? ¿Hay territorios con potencial no explotado?
**Recommended_Actions:** Rediseñar territorios basado en potencial de mercado; ajustar metas y recursos por potencial de territorio; rotar vendedores para equilibrar; dar soporte diferenciado; revisar asignación periódicamente.
**Severity_Level:** Medium
**Related_Patterns:** SAL-024, SAL-027, SAL-028, SAL-054

### SAL-027
**Pattern_Name:** Alta Rotación de Vendedores
**Category:** Productividad Comercial
**Description:** La tasa de rotación de vendedores es alta, generando costos de reclutamiento y entrenamiento, pérdida de relaciones con clientes y períodos de baja productividad.
**Observable_Symptoms:** Vendedores que se van antes de 12 meses; reclutamiento constante; el equipo siempre tiene vacantes; clientes que mencionan "otra vez cambio de vendedor"; costos de onboarding recurrentes.
**Early_Warning_Signals:** Rotación anual de vendedores > 30%; tiempo promedio en el puesto < 18 meses; % de vendedores con menos de 1 año > 50%; costo de rotación / nómina > 10%; período de ramp-up > 6 meses.
**Typical_Causes:** Metas poco realistas; compensación no competitiva; falta de entrenamiento y soporte; mal liderazgo comercial; cultura de alta presión sin reconocimiento; selección inadecuada de vendedores.
**Business_Impact:** Costos recurrentes de reclutamiento y entrenamiento; pérdida de relaciones con clientes; equipos inexpertos que rinden por debajo del potencial; inestabilidad comercial; dificultad para escalar.
**Metrics_To_Check:** Tasa de rotación anual; tiempo promedio en el puesto; costo de rotación (reclutamiento + entrenamiento + pérdida de productividad); % de vendedores en ramp-up; satisfacción del equipo comercial.
**Diagnostic_Questions:** ¿Por qué se van los vendedores? ¿Hay entrevistas de salida? ¿La compensación es competitiva? ¿Hay oportunidades de desarrollo? ¿El liderazgo comercial es efectivo? ¿Se seleccionan adecuadamente los vendedores?
**Recommended_Actions:** Mejorar proceso de selección (assessment, referencias); establecer compensación competitiva con base + variable; implementar programa de onboarding y mentoría; desarrollar carrera comercial; mejorar liderazgo y cultura de equipo; realizar entrevistas de salida y actuar sobre resultados.
**Severity_Level:** High
**Related_Patterns:** SAL-010, SAL-024, SAL-025, SAL-028, SAL-083

### SAL-028
**Pattern_Name:** Curva de Aprendizaje Prolongada
**Category:** Productividad Comercial
**Description:** Los nuevos vendedores tardan demasiado en alcanzar la productividad esperada (ramp-up lento), generando un alto costo de incorporación y retraso en el retorno de inversión.
**Observable_Symptoms:** Nuevos vendedores que no venden en los primeros meses; período de capacitación extenso sin práctica real; vendedores que "aprenden" pero no cierran; rotación durante el período de prueba; gerencia impaciente con nuevos vendedores.
**Early_Warning_Signals:** Ramp-up > 6 meses para alcanzar productividad; nuevos vendedores con < 50% de la meta en primeros 6 meses; % de nuevos vendedores que no superan período de prueba > 30%; tiempo hasta primera venta > 60 días; costo de ramp-up > 20% del costo total del vendedor.
**Typical_Causes:** Falta de programa de onboarding estructurado; entrenamiento insuficiente o inefectivo; producto/servicio complejo sin material de apoyo; falta de acompañamiento en terreno; expectativas irreales.
**Business_Impact:** Alto costo de incorporación; retorno lento de inversión en nuevas contrataciones; rotación durante período de aprendizaje; equipos permanentemente con vendedores en ramp-up; capacidad comercial por debajo de la nominal.
**Metrics_To_Check:** Tiempo de ramp-up (días hasta productividad); % de meta alcanzado por mes (nuevos); tiempo hasta primera venta; % de nuevos que superan período de prueba; productividad promedio de vendedores con < 12 meses.
**Diagnostic_Questions:** ¿Hay un programa de onboarding estructurado? ¿Los nuevos vendedores tienen mentores? ¿Hay material de entrenamiento disponible? ¿Se hace acompañamiento en terreno? ¿Las expectativas son realistas para los primeros meses?
**Recommended_Actions:** Diseñar programa de onboarding de 30-60-90 días; asignar mentor a cada nuevo vendedor; crear material de entrenamiento (scripts, objeciones, demos); hacer acompañamiento en terreno las primeras semanas; establecer metas progresivas (no plenas desde el inicio).
**Severity_Level:** Medium
**Related_Patterns:** SAL-010, SAL-024, SAL-027, SAL-083

### SAL-029
**Pattern_Name:** Vendedores No Alcanzan Metas Consistentemente
**Category:** Productividad Comercial
**Description:** Una proporción significativa de vendedores no alcanza sus metas de manera recurrente, indicando problemas en el establecimiento de metas, la capacidad del equipo o la ejecución.
**Observable_Symptoms:** % alto de vendedores por debajo de meta mes tras mes; el equipo justifica sistemáticamente el incumplimiento; metas que se revisan a la baja recurrentemente; algunos vendedores nunca han cumplido meta; la gerencia acepta el bajo desempeño como normal.
**Early_Warning_Signals:** % de vendedores que alcanzan meta < 60%; vendedores que no alcanzan meta por 3+ meses consecutivos; tendencia de cumplimiento de metas decreciente; metas revisadas a la baja en mitad del período; falta de consecuencias por no cumplir.
**Typical_Causes:** Metas mal diseñadas (irreales, inconsistentes); vendedores sin habilidades necesarias; falta de capacitación y soporte; herramientas inadecuadas; mala gestión del desempeño; ausencia de accountability.
**Business_Impact:** Incumplimiento de ingresos; equipo desmotivado; cultura de baja exigencia; rotación de mejores vendedores; inversión sin retorno en fuerza de ventas.
**Metrics_To_Check:** % de vendedores que alcanzan meta; meses consecutivos por debajo de meta; desviación promedio de meta; tendencia de cumplimiento; rotación entre vendedores que no cumplen.
**Diagnostic_Questions:** ¿Las metas son realistas y alcanzables? ¿Los vendedores tienen las habilidades y recursos necesarios? ¿Hay consecuencias por no cumplir? ¿Se ofrece entrenamiento y soporte? ¿Hay un proceso de gestión del desempeño?
**Recommended_Actions:** Revisar diseño de metas (realistas, consistentes); implementar plan de mejora para vendedores de bajo rendimiento; entrenar en habilidades detectadas como débiles; reforzar accountability con consecuencias claras; considerar rotación de vendedores que persistentemente no cumplen.
**Severity_Level:** High
**Related_Patterns:** SAL-010, SAL-024, SAL-027, SAL-028, SAL-083

### SAL-030
**Pattern_Name:** Productividad Comercial No Measurada
**Category:** Productividad Comercial
**Description:** La empresa no mete ni monitorea la productividad comercial de manera sistemática, operando sin datos sobre la eficiencia y efectividad de la fuerza de ventas.
**Observable_Symptoms:** Falta de KPIs comerciales; decisiones basadas en intuición; no se sabe cuánto genera cada vendedor; no hay métricas de actividad, conversión o eficiencia; resultados se conocen al cierre del mes (demasiado tarde).
**Early_Warning_Signals:** Sin CRM o CRM no utilizado; no hay reportes de pipeline; no se mide actividad por vendedor; sin metas individuales claras; resultados se conocen después del cierre del mes; gerencia no tiene visibilidad de la operación diaria.
**Typical_Causes:** Falta de cultura de datos; CRM no implementado o mal implementado; gerencia comercial no entrenada en gestión con métricas; equipo resistente a ser medido; falta de herramientas accesibles.
**Business_Impact:** Imposibilidad de identificar problemas a tiempo; decisiones basadas en corazonadas; mala asignación de recursos; imposibilidad de escalar; gerencia sin control de la operación.
**Metrics_To_Check:** Los que deberían medirse: actividades por vendedor, tasa de conversión, ticket promedio, pipeline, velocidad de funnel, ingresos por vendedor.
**Diagnostic_Questions:** ¿Se mide la actividad comercial diaria? ¿Hay un CRM implementado y usado? ¿Los vendedores tienen metas individuales claras? ¿La gerencia tiene visibilidad del pipeline? ¿Se toman decisiones basadas en datos?
**Recommended_Actions:** Implementar CRM y asegurar su adopción; definir KPIs comerciales (actividad, conversión, pipeline, ticket, ingresos); establecer dashboard comercial semanal; entrenar en gestión con métricas; crear cultura de datos y accountability.
**Severity_Level:** Critical
**Related_Patterns:** SAL-024, SAL-025, SAL-056, SAL-075, SAL-083

### SAL-031
**Pattern_Name:** Vendedores Canibalizan Canales de Bajo Costo
**Category:** Productividad Comercial
**Description:** La fuerza de ventas captura ventas que podrían cerrarse en canales de menor costo (web, autoservicio), canibalizando canales más eficientes y reduciendo la rentabilidad global.
**Observable_Symptoms:** Vendedores cierran ventas pequeñas que podrían hacerse online; clientes compran por canal caro cuando el barato está disponible; el equipo comercial procesa pedidos en lugar de vender; comisiones pagadas por ventas que no requieren intervención comercial; canales digitales infrautilizados.
**Early_Warning_Signals:** Vendedores cierran operaciones de bajo ticket que podrían ser autoservicio; % de ventas de canales digitales bajo; comisiones pagadas por ventas sin esfuerzo comercial; clientes redirigidos a vendedor para transacciones simples; falta de reglas de derivación entre canales.
**Typical_Causes:** Falta de reglas de derivación de canales; comisiones mal diseñadas (pagan por todo); vendedores que "protegen" comisiones; canales digitales pobres o no disponibles; clientes acostumbrados a tratar con vendedor.
**Business_Impact:** Costo de venta innecesariamente alto; canales de bajo costo subutilizados; rentabilidad menor por comisiones excesivas; fricción para clientes que preferirían autoservicio; ineficiencia comercial.
**Metrics_To_Check:** % de ventas por canal; costo de venta por canal; % de transacciones pequeñas manejadas por vendedores; cumplimiento de reglas de derivación; comisiones pagadas en ventas de autoservicio.
**Diagnostic_Questions:** ¿Hay reglas claras de qué ventas deben ir a cada canal? ¿Los vendedores reciben comisión por ventas que no requieren su intervención? ¿El canal digital es bueno y fácil de usar? ¿Los clientes conocen el canal de autoservicio? ¿Hay incentivos para derivar a canales de bajo costo?
**Recommended_Actions:** Definir reglas de derivación: qué ventas van a vendedor y cuáles a autoservicio; ajustar comisiones para no pagar por ventas que no requieren esfuerzo; mejorar canales digitales para que sean efectivos; entrenar clientes en uso de autoservicio; incentivar derivación a canales eficientes.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-023, SAL-024, SAL-035


## Dependencia de Vendedores

### SAL-032
**Pattern_Name:** Concentración de Ingresos en Pocos Vendedores
**Category:** Dependencia de Vendedores
**Description:** Un pequeño número de vendedores genera la mayor parte de los ingresos, creando una peligrosa dependencia de personas clave cuyo reemplazo sería muy costoso.
**Observable_Symptoms:** 1-2 vendedores generan > 50% de ingresos; si un vendedor clave se enferma o va de vacaciones, caen las ventas; el mejor vendedor tiene procesos y relaciones no documentadas; el resto del equipo rinde muy por debajo.
**Early_Warning_Signals:** Top 1 vendedor genera > 30% de ingresos; Top 3 vendedores generan > 70% de ingresos; diferencia entre mejor vendedor y promedio > 3x; vendedores clave sin procesos documentados; alta rotación en vendedores no clave.
**Typical_Causes:** Sistemas y procesos no estandarizados; vendedores estrella que no comparten conocimiento; selección inadecuada del resto del equipo; falta de entrenamiento y desarrollo; cultura de "héroes" en lugar de procesos.
**Business_Impact:** Riesgo severo si un vendedor clave se va; pérdida de clientes si el vendedor se lleva la relación; dificultad para escalar el equipo; diferencias salariales que generan tensión; inconsistencia en resultados.
**Metrics_To_Check:** % de ingresos del Top 1, Top 3, Top 5; concentración de ingresos (índice Herfindahl); ingresos del mejor / promedio; documentos de procesos por vendedor; % de clientes con relación exclusiva con vendedor.
**Diagnostic_Questions:** ¿Qué pasa si el mejor vendedor se va? ¿Sus procesos están documentados? ¿Comparte su conocimiento? ¿Los clientes tienen relación con la empresa o con el vendedor? ¿Hay un plan de sucesión para vendedores clave?
**Recommended_Actions:** Documentar procesos y relaciones de vendedores estrella; implementar CRM para centralizar relaciones con clientes; fomentar distribución de clientes entre varios vendedores; entrenar al equipo en mejores prácticas; crear programa de mentores; diversificar cartera de clientes entre vendedores.
**Severity_Level:** Critical
**Related_Patterns:** SAL-010, SAL-024, SAL-027, SAL-033, SAL-083

### SAL-033
**Pattern_Name:** Vendedores que No Documentan en CRM
**Category:** Dependencia de Vendedores
**Description:** Los vendedores no registran sus actividades, oportunidades y clientes en el CRM, haciendo que la información comercial dependa de la memoria individual y no de la empresa.
**Observable_Symptoms:** CRM vacío o desactualizado; vendedores que "tienen la info en la cabeza"; gerencia no puede ver el pipeline real; reportes manuales en Excel; clientes que nadie sabe quién los contactó; pérdida de información cuando un vendedor se va.
**Early_Warning_Signals:** % de actividades registradas en CRM < 50%; oportunidades en CRM desactualizadas (> 7 días sin actualización); vendedores que no usan CRM a pesar de tenerlo; reportes paralelos fuera del CRM; información perdida por rotación.
**Typical_Causes:** CRM mal implementado o difícil de usar; falta de consecuencias por no usarlo; vendedores ven el CRM como "trabajo extra" no como herramienta; liderazgo no exige su uso; cultura de "lo importante es vender, no registrar".
**Business_Impact:** Pérdida de información crítica cuando un vendedor se va; imposibilidad de hacer forecast confiable; gerencia sin visibilidad; decisiones basadas en información incompleta; dificultad para escalar.
**Metrics_To_Check:** % de uso de CRM (actividades registradas vs reales); % de oportunidades actualizadas en CRM; tiempo desde última actualización de pipeline; reportes generados desde CRM; pérdida de información por rotación.
**Diagnostic_Questions:** ¿El CRM es fácil de usar? ¿Los vendedores recibieron entrenamiento adecuado? ¿Hay consecuencias por no usarlo? ¿La gerencia revisa el CRM y exige su uso? ¿Los vendedores ven valor en el CRM?
**Recommended_Actions:** Mejorar usabilidad del CRM; entrenar en uso de CRM; establecer políticas de uso con consecuencias; gerencia debe liderar con el ejemplo (revisar CRM, dar feedback); mostrar valor del CRM a vendedores (reportes, alertas, eficiencia); integrar CRM con herramientas diarias.
**Severity_Level:** High
**Related_Patterns:** SAL-030, SAL-032, SAL-056, SAL-075, SAL-083

### SAL-034
**Pattern_Name:** Relación Cliente-Vendedor sin Vínculo Institucional
**Category:** Dependencia de Vendedores
**Description:** Los clientes tienen una relación exclusiva con su vendedor y no con la empresa, por lo que si el vendedor se va, existe alto riesgo de que el cliente también se vaya.
**Observable_Symptoms:** Clientes que solo quieren tratar con un vendedor específico; clientes que se van cuando su vendedor se fue; el vendedor maneja la relación sin intervención de la empresa; cliente no conoce a otros miembros del equipo; quejas de clientes cuando otro vendedor los contacta.
**Early_Warning_Signals:** % de clientes con relación exclusiva con un vendedor; clientes perdidos tras rotación de vendedores > 20%; cliente no tiene contacto con nadie más de la empresa; sin reuniones de account review sin el vendedor; cliente se niega a hablar con otro vendedor.
**Typical_Causes:** Falta de gestión de cuentas a nivel institucional; vendedores que fomentan la dependencia para asegurar su puesto; falta de touch points institucionales (servicio al cliente, account management, gerencia); cultura de "el cliente es del vendedor".
**Business_Impact:** Riesgo de pérdida de clientes ante rotación; dificultad para escalar la relación con el cliente; clientes que exigen al vendedor en todas las interacciones; pérdida de valor de la cartera de clientes; barrera para crecer.
**Metrics_To_Check:** % de clientes con relación exclusiva; clientes perdidos por rotación; número de contactos institucionales por cliente; % de clientes que han interactuado con > 1 persona de la empresa; satisfacción del cliente con la relación institucional.
**Diagnostic_Questions:** ¿Los clientes conocen a más personas de la empresa además de su vendedor? ¿Hay reuniones periódicas sin el vendedor? ¿Hay un proceso de account management institucional? ¿Los clientes se van cuando el vendedor se va? ¿La empresa es "dueña" de la relación?
**Recommended_Actions:** Implementar account management multicontacto; introducir ejecutivo de cuenta institucional; realizar reuniones periódicas sin el vendedor; involucrar a gerencia en relaciones clave; documentar toda interacción en CRM; crear programa de customer success.
**Severity_Level:** High
**Related_Patterns:** SAL-032, SAL-033, SAL-036, SAL-037, SAL-083

### SAL-035
**Pattern_Name:** Vendedores que Definen Precios sin Control
**Category:** Dependencia de Vendedores
**Description:** Los vendedores tienen autonomía para definir descuentos y precios sin controles, erosionando el margen y creando inconsistencia en la política comercial.
**Observable_Symptoms:** Vendedores que negocian precios sin supervisión; descuentos variables sin justificación; precios diferentes para clientes similares; margen inconsistentes por vendedor; clientes que comparan precios entre sí y reclaman.
**Early_Warning_Signals:** Desviación de precio de venta vs precio de lista > 20%; % de descuento promedio muy variable entre vendedores; falta de registro de autorización de descuentos; vendedores que "dan precio" sin aprobación; margen por vendedor con alta variabilidad.
**Typical_Causes:** Falta de política de precios y descuentos; confianza excesiva en criterio del vendedor; presión por metas que lleva a concesiones; sin sistema de autorización de descuentos; cultura de "el vendedor sabe".
**Business_Impact:** Erosión de margen; inconsistencia de precios que genera conflictos con clientes; clientes entrenados para negociar siempre; vendedores que regalan margen para cerrar fácil; menor rentabilidad general.
**Metrics_To_Check:** Descuento promedio por vendedor; desviación de precio de venta; margen por vendedor; % de descuentos sin autorización; correlación descuento vs cumplimiento de meta.
**Diagnostic_Questions:** ¿Hay una política de precios y descuentos documentada? ¿Los descuentos requieren aprobación? ¿Hay niveles de autorización por monto? ¿Se monitorean los descuentos por vendedor? ¿Hay consecuencias por desviarse de la política?
**Recommended_Actions:** Implementar política de precios y descuentos con niveles de autorización; establecer precio mínimo por producto/segmento; monitorear y publicar descuento por vendedor; vincular compensación a margen (no solo a ingresos); entrenar en negociación basada en valor.
**Severity_Level:** High
**Related_Patterns:** SAL-017, SAL-018, SAL-020, SAL-032, SAL-048

### SAL-036
**Pattern_Name:** Dependencia de Vendedores para Gestión de Clientes Existentes
**Category:** Dependencia de Vendedores
**Description:** Los mismos vendedores que captan clientes nuevos también gestionan la relación con clientes existentes, descuidando la prospección y la venta consultiva por dedicarse a la operación diaria.
**Observable_Symptoms:** Vendedores pasan más tiempo con clientes existentes que prospectando; clientes nuevos escasean; el equipo se queja de "no tener tiempo para prospectar"; el 80% del tiempo se va en clientes actuales; clientes nuevos solo crecen por referidos.
**Early_Warning_Signals:** % de tiempo en clientes existentes > 60%; ratio de nuevos clientes vs clientes existentes < 1:5; horas de prospección / horas de gestión < 0.3; crecimiento de ingresos de clientes existentes > 3x crecimiento de nuevos clientes; vendedores no prospectan.
**Typical_Causes:** Estructura comercial sin roles definidos (hunter vs farmer); vendedores prefieren trabajar con clientes conocidos (más fácil); falta de equipo de account management o customer success; comisiones pagan tanto por nuevos como por existentes; clientes existentes demandan atención.
**Business_Impact:** Estancamiento en captación de nuevos clientes; vulnerabilidad si se pierden clientes existentes; equipo comercial subutilizado en tareas de soporte; crecimiento limitado; dificultad para escalar.
**Metrics_To_Check:** % de tiempo en prospección vs gestión; ratio ingresos nuevos vs existentes; tasa de captación de nuevos clientes; número de nuevos clientes por vendedor por mes; crecimiento de cartera de clientes.
**Diagnostic_Questions:** ¿Están separados los roles de hunter y farmer? ¿Los vendedores tienen tiempo para prospectar? ¿Hay un equipo de account management? ¿Las comisiones incentivan la captación de nuevos clientes? ¿Los clientes existentes consumen demasiado tiempo comercial?
**Recommended_Actions:** Separar roles: hunters (captación) y farmers (gestión); crear equipo de customer success/account management; ajustar comisiones para incentivar captación; asignar tiempo específico a prospección (bloques protegidos); transferir clientes existentes a farmers después del onboarding.
**Severity_Level:** High
**Related_Patterns:** SAL-025, SAL-032, SAL-033, SAL-034, SAL-037

### SAL-037
**Pattern_Name:** Cartera de Clientes Concentrada en Vendedores Antiguos
**Category:** Dependencia de Vendedores
**Description:** Los vendedores más antiguos tienen carteras grandes de clientes existentes que gestionan, mientras que los nuevos vendedores no tienen cartera y solo prospectan, generando inequidad y desmotivación.
**Observable_Symptoms:** Vendedores antiguos viven de comisiones de clientes existentes sin prospectar; vendedores nuevos solo tienen clientes nuevos (difícil); diferencias salariales enormes entre vendedores antiguos y nuevos; vendedores nuevos se frustran y se van; falta de rotación de carteras.
**Early_Warning_Signals:** Diferencia de ingresos entre vendedor más antiguo y más nuevo > 5x; vendedores antiguos sin prospección; vendedores nuevos con cartera < 50% de la media; rotación alta en vendedores nuevos; sin rotación de carteras en > 2 años.
**Typical_Causes:** No se rotan carteras periódicamente; comisiones perpetuas sobre cartera; vendedores antiguos "protegen" su cartera; falta de política de redistribución; cultura de "el que tiene la cartera, tiene el ingreso".
**Business_Impact:** Inequidad que genera desmotivación; rotación de vendedores nuevos; vendedores antiguos cómodos sin prospectar; crecimiento estancado; estructura comercial no escalable.
**Metrics_To_Check:** Diferencia de ingresos entre vendedores antiguos y nuevos; % de cartera por antigüedad del vendedor; antigüedad promedio de cartera sin rotar; rotación de vendedores nuevos; % de vendedores que prospectan activamente.
**Diagnostic_Questions:** ¿Se rotan las carteras periódicamente? ¿Las comisiones sobre cartera existente son perpetuas o tienen plazo? ¿Hay oportunidad para vendedores nuevos de acceder a carteras? ¿Los vendedores antiguos prospectan? ¿Hay un tope de cartera por vendedor?
**Recommended_Actions:** Implementar rotación periódica de carteras; limitar comisiones sobre cartera existente en el tiempo; redistribuir carteras al incorporar nuevos vendedores; establecer tope de clientes por vendedor; crear programa de "graduación" de cartera.
**Severity_Level:** Medium
**Related_Patterns:** SAL-032, SAL-034, SAL-036, SAL-083


## Recurrencia

### SAL-038
**Pattern_Name:** Baja Tasa de Retención de Clientes
**Category:** Recurrencia
**Description:** La empresa pierde clientes a una tasa elevada (alto churn), lo que requiere un esfuerzo constante de captación solo para mantener el nivel de ingresos.
**Observable_Symptoms:** Clientes que se van después de la primera compra; tasa de cancelación alta en suscripciones/contratos; clientes que no repiten; el equipo comercial pasa más tiempo reemplazando clientes perdidos que captando nuevos; ingresos estancados a pesar de buena captación.
**Early_Warning_Signals:** Tasa de churn anual > 20% (o > benchmark sectorial); vida media del cliente < 12 meses; tasa de repetición de compra < 30%; ratio LTV/CAC < 3x; clientes que no renuevan contratos.
**Typical_Causes:** Mala experiencia del cliente post-venta; producto/servicio no cumple expectativas; falta de onboarding y soporte; precio no justificado post-compra; competidor ofrece mejor alternativa; sin programa de fidelización.
**Business_Impact:** Esfuerzo comercial enfocado en reemplazar clientes en lugar de crecer; alto CAC que no se recupera; ingresos estancados o decrecientes; inversión en captación desperdiciada; imposibilidad de escalar.
**Metrics_To_Check:** Tasa de churn mensual/anual; vida media del cliente; tasa de repetición de compra; ratio LTV/CAC; NPS o satisfacción del cliente; ingresos recurrentes vs nuevos.
**Diagnostic_Questions:** ¿Por qué se van los clientes? ¿Hay entrevistas de salida? ¿La experiencia post-venta es buena? ¿El producto cumple expectativas? ¿Hay un programa de fidelización? ¿El onboarding es efectivo?
**Recommended_Actions:** Implementar programa de customer success; mejorar onboarding de nuevos clientes; realizar entrevistas de salida y actuar; crear programa de fidelización y recompensas; monitorear NPS y satisfacción; mejorar producto basado en feedback.
**Severity_Level:** Critical
**Related_Patterns:** SAL-039, SAL-040, SAL-041, SAL-042, SAL-046, SAL-047

### SAL-039
**Pattern_Name:** Primera Compra sin Segunda Compra
**Category:** Recurrencia
**Description:** Un alto porcentaje de clientes realiza una sola compra y nunca vuelve a comprar, indicando problemas en la propuesta de valor, la experiencia del cliente o el seguimiento post-venta.
**Observable_Symptoms:** Base de clientes crece pero ingresos no; muchos clientes inactivos; lista de clientes llena de "one-timers"; el equipo celebra nuevas cuentas pero los ingresos no reflejan el esfuerzo; campañas de re-compra sin respuesta.
**Early_Warning_Signals:** % de clientes con una sola compra > 60%; ratio de compras recurrentes / compras totales < 30%; tiempo promedio entre compras > 12 meses; tasa de activación (segunda compra) < 20%; clientes inactivos > 50% de la base.
**Typical_Causes:** Producto/servicio de una sola vez sin oferta de continuación; falta de seguimiento post-venta; experiencia del cliente no memorable; sin programa de re-compra; cliente no percibe valor suficiente para repetir.
**Business_Impact:** Alto costo de adquisición nunca recuperado; crecimiento ilusorio (nuevos clientes que no aportan valor recurrente); base de clientes grande pero poco activa; ingresos impredecibles; necesidad constante de nuevos clientes.
**Metrics_To_Check:** % de clientes con compra única; tasa de segunda compra; ingresos de clientes recurrentes vs nuevos; tiempo entre primera y segunda compra; % de clientes activos (compraron en últimos 12 meses).
**Diagnostic_Questions:** ¿El producto/servicio está diseñado para compra recurrente? ¿Hay ofertas de post-venta? ¿Se hace seguimiento después de la primera compra? ¿La experiencia del cliente es buena? ¿Hay un programa de re-compra?
**Recommended_Actions:** Diseñar oferta de post-venta o recurrencia (suscripción, recambio, consumibles); implementar programa de seguimiento post-venta automatizado; crear campañas de re-compra segmentadas; mejorar experiencia del cliente; fidelizar con contenido y valor post-venta.
**Severity_Level:** High
**Related_Patterns:** SAL-022, SAL-038, SAL-040, SAL-041, SAL-042

### SAL-040
**Pattern_Name:** Ingresos Recurrentes Insuficientes
**Category:** Recurrencia
**Description:** Los ingresos recurrentes (suscripciones, contratos, mantenimiento) representan un porcentaje muy bajo del total, lo que hace que los ingresos sean impredecibles y dependientes de nueva venta constante.
**Observable_Symptoms:** Cada mes hay que "empezar de cero" para generar ingresos; mucha volatilidad en resultados mensuales; el equipo vive bajo presión constante por cerrar; los ingresosdel próximo mes son inciertos; falta de base de ingresos predecibles.
**Early_Warning_Signals:** Ingresos recurrentes / ingresos totales < 30%; ingresos de nuevos clientes > ingresos de clientes existentes; varianza mensual de ingresos > 30%; % de clientes en modelo recurrente < 20%; sin contratos de largo plazo.
**Typical_Causes:** Modelo de negocio transaccional sin componente recurrente; falta de oferta de suscripción o mantenimiento; clientes no ven valor en compromiso a largo plazo; cultura de venta única; producto no diseñado para recurrencia.
**Business_Impact:** Ingresos impredecibles; planificación financiera difícil; presión permanente por captar nuevos clientes; menor valoración de la empresa (múltiplos más bajos); imposibilidad de invertir con confianza.
**Metrics_To_Check:** % de ingresos recurrentes; MRR/ARR (Monthly/Annual Recurring Revenue); tasa de renovación; vida media del cliente; predictibilidad de ingresos.
**Diagnostic_Questions:** ¿Hay oferta de suscripción o contrato recurrente? ¿Los clientes estarían dispuestos a comprometerse a largo plazo? ¿El modelo de negocio permite recurrencia? ¿Hay ingresos predecibles mes a mes? ¿Se ha evaluado crear componentes recurrentes?
**Recommended_Actions:** Desarrollar oferta de suscripción, mantenimiento o contrato anual; convertir clientes transaccionales a modelo recurrente; crear programas de fidelización con beneficios por permanencia; ofrecer descuentos por compromiso a largo plazo; medir y publicar MRR.
**Severity_Level:** High
**Related_Patterns:** SAL-038, SAL-039, SAL-041, SAL-042, SAL-046

### SAL-041
**Pattern_Name:** Churn de Clientes Recurrentes
**Category:** Recurrencia
**Description:** Clientes que históricamente eran recurrentes están cancelando o dejando de comprar, indicando deterioro en la propuesta de valor o en la relación.
**Observable_Symptoms:** Clientes de largo plazo que cancelan; aumento en cancelaciones de suscripciones; clientes antiguos que reducen su compra; patrones de compra que se espacian; clientes que se quejan más antes de irse.
**Early_Warning_Signals:** Tasa de churn de clientes con > 12 meses de antigüedad en aumento; ingresos de clientes existentes decrecientes; % de clientes que reducen su gasto > 10% anual; NPS de clientes antiguos en caída; aumento en cancelaciones vs años anteriores.
**Typical_Causes:** Competidor ofrece mejor alternativa; deterioro de calidad del producto/servicio; falta de innovación y mejora; mal servicio al cliente; precio no actualizado que el cliente cuestiona; cliente cambió sus necesidades.
**Business_Impact:** Pérdida de la base más valiosa de ingresos; necesidad de captar más clientes para compensar; deterioro de la marca; señal de problemas estructurales; costo de recuperar clientes perdidos mayor que retenerlos.
**Metrics_To_Check:** Tasa de churn por antigüedad de cliente; ingresos de clientes existentes (tendencia); NPS por segmento; % de clientes que reducen gasto; tasa de cancelación de renovaciones.
**Diagnostic_Questions:** ¿Por qué se están yendo los clientes antiguos? ¿Hay señales previas a la cancelación? ¿Hay un programa de retención de clientes? ¿El producto ha evolucionado con las necesidades? ¿La competencia ofrece algo mejor?
**Recommended_Actions:** Implementar programa de retención con alertas tempranas; realizar entrevistas con clientes en riesgo; mejorar producto basado en feedback de clientes antiguos; fortalecer relación con clientes clave; crear programa de fidelización con beneficios crecientes; monitorear señales de churn.
**Severity_Level:** Critical
**Related_Patterns:** SAL-038, SAL-039, SAL-040, SAL-042, SAL-046, SAL-047

### SAL-042
**Pattern_Name:** Ingresos Dependientes de Clientes Nuevos
**Category:** Recurrencia
**Description:** La empresa depende casi exclusivamente de nuevos clientes para generar ingresos, sin una base sólida de ingresos recurrentes, lo que hace que cada mes sea una "carrera contrarreloj".
**Observable_Symptoms:** El equipo siempre está enfocado en nuevos clientes; no hay ingresos "seguros" de un mes a otro; la cartera de clientes existentes no genera ingresos significativos; el equipo no dedica tiempo a clientes actuales; cada mes comienza sin base de ingresos.
**Early_Warning_Signals:** Nuevos clientes representan > 70% de ingresos del mes; ingresos de clientes existentes < 30% del total; tasa de renovación < 50%; cartera de clientes existentes con baja actividad de compra; esfuerzo comercial 80% en nuevos, 20% en existentes.
**Typical_Causes:** Modelo de negocio transaccional; falta de upselling/cross-selling a clientes existentes; equipo comercial enfocado solo en captación; clientes existentes abandonados post-venta; falta de equipo de account management.
**Business_Impact:** Alta presión por captar constantemente; ingresos volátiles; clientes existentes sub-explotados; CAC no recuperado si el cliente no repite; imposibilidad de escalar; fatiga del equipo comercial.
**Metrics_To_Check:** % de ingresos de clientes nuevos vs existentes; ingresos por cliente existente (tendencia); tasa de venta adicional a existentes; % de clientes existentes que compran en el período.
**Diagnostic_Questions:** ¿Se factura a clientes existentes regularmente o solo a nuevos? ¿Hay un equipo dedicado a clientes existentes? ¿Se hace upselling/cross-selling? ¿Los clientes existentes tienen una oferta de valor continua? ¿Se mide el ingreso por cliente existente?
**Recommended_Actions:** Desarrollar ingresos recurrentes (suscripciones, contratos); implementar programa de upselling/cross-selling a clientes existentes; crear equipo de account management; establecer metas de ingresos de clientes existentes; mejorar oferta de valor post-venta.
**Severity_Level:** High
**Related_Patterns:** SAL-038, SAL-039, SAL-040, SAL-041, SAL-046, SAL-047

### SAL-043
**Pattern_Name:** Clientes Inactivos Sin Estrategia de Reactivación
**Category:** Recurrencia
**Description:** La empresa tiene una base significativa de clientes inactivos (que no compran hace tiempo) y no tiene una estrategia sistemática para reactivarlos.
**Observable_Symptoms:** Lista de clientes grande pero pocos activos; clientes que no compran hace meses o años; sin campañas de reactivación; el equipo ignora a clientes inactivos; se prioriza siempre captar nuevos sobre reactivar existentes.
**Early_Warning_Signals:** % de clientes inactivos > 40% de la base; tiempo promedio desde última compra > 12 meses; sin campañas de reactivación en el último año; clientes inactivos no contactados; % de reactivación desconocido.
**Typical_Causes:** Falta de estrategia de reactivación; equipo enfocado solo en nuevos; CRM no segmenta por actividad; cultura de "cliente que no compra, está muerto"; desconocimiento del valor potencial de reactivación.
**Business_Impact:** Base de clientes subutilizada; inversión en captación desperdiciada cuando clientes se vuelven inactivos; oportunidad de ingresos perdida; CAC de reactivación menor que CAC de nuevo cliente; deterioro de la base de clientes.
**Metrics_To_Check:** % de clientes activos vs inactivos; tasa de reactivación; ingresos de clientes reactivados; costo de reactivación vs CAC; % de clientes inactivos contactados en el período.
**Diagnostic_Questions:** ¿Cuántos clientes inactivos hay? ¿Se sabe por qué dejaron de comprar? ¿Hay campañas de reactivación? ¿El costo de reactivar es menor que captar nuevos? ¿Hay un proceso de segmentación por actividad?
**Recommended_Actions:** Segmentar clientes por antigüedad de última compra; diseñar campañas de reactivación por segmento; ofrecer incentivos de retorno (descuento, contenido, consultoría); contactar clientes inactivos periódicamente; medir tasa de reactivación como KPI.
**Severity_Level:** Medium
**Related_Patterns:** SAL-038, SAL-039, SAL-041, SAL-044, SAL-046

### SAL-044
**Pattern_Name:** Ventas Recurrentes sin Contrato Formal
**Category:** Recurrencia
**Description:** La empresa tiene clientes que compran recurrentemente pero sin contrato formal, lo que genera incertidumbre sobre la continuidad y dificulta la planificación.
**Observable_Symptoms:** Clientes recurrentes pero sin compromiso formal; compras que se dan por "costumbre" no por contrato; el cliente puede irse en cualquier momento sin previo aviso; dificultad para proyectar ingresos recurrentes; falta de palancas contractuales para retener.
**Early_Warning_Signals:** % de ingresos recurrentes sin contrato > 50%; clientes recurrentes sin plazo mínimo; tasa de pérdida de clientes sin contrato > clientes con contrato; sin renovación automática; facturación sin orden de compra ni contrato.
**Typical_Causes:** Cultura de relación informal con clientes; falta de estándar de contratación; cliente se resiste a firmar contrato; equipo comercial no exige contratos; proceso de venta no incluye contratos.
**Business_Impact:** Incertidumbre sobre ingresos futuros; riesgo de perder clientes sin previo aviso; imposibilidad de planificar inversiones; menor valoración de la empresa; vulnerabilidad comercial.
**Metrics_To_Check:** % de ingresos recurrentes con contrato; % de clientes recurrentes sin contrato; tasa de retención con contrato vs sin contrato; plazo promedio de contratos; % de renovación automática.
**Diagnostic_Questions:** ¿Los clientes recurrentes tienen contrato? ¿Hay plazo mínimo? ¿Hay renovación automática? ¿El cliente puede irse sin penalización? ¿Se ha intentado formalizar la relación contractual?
**Recommended_Actions:** Implementar contratos formales para relaciones recurrentes; ofrecer beneficios por compromiso contractual; establecer renovación automática con período de notice; migrar gradualmente clientes informales a contrato; incluir contratos en el proceso de venta estándar.
**Severity_Level:** Medium
**Related_Patterns:** SAL-038, SAL-040, SAL-041, SAL-042, SAL-046

### SAL-045
**Pattern_Name:** Recurrencia sin Programa de Fidelización
**Category:** Recurrencia
**Description:** La empresa tiene clientes recurrentes o potencial de recurrencia pero no cuenta con un programa de fidelización estructurado que incentive la repetición de compra.
**Observable_Symptoms:** Clientes repiten sin incentivos formales; no hay programa de puntos, beneficios o descuentos por fidelidad; no se reconoce a clientes frecuentes; los clientes no tienen razón para preferir la empresa sobre la competencia; falta de diferenciación en la experiencia del cliente recurrente.
**Early_Warning_Signals:** Sin programa de fidelización implementado; % de clientes recurrentes sin incentivos adicionales; tasa de churn sin programa > con programa; clientes frecuentes no identificados ni segmentados; sin beneficios exclusivos para recurrentes.
**Typical_Causes:** Falta de inversión en fidelización; desconocimiento del valor del cliente recurrente; cultura de captación sobre retención; recursos limitados para programas de fidelidad; ausencia de sistema CRM para gestionar fidelización.
**Business_Impact:** Clientes recurrentes no maximizados; vulnerabilidad a ofertas de competidores; menor LTV del cliente; oportunidad perdida de ingresos adicionales; clientes fieles no reconocidos que pueden sentirse infravalorados.
**Metrics_To_Check:** LTV de clientes en programa de fidelización vs fuera; % de clientes en programa; tasa de retención con programa; ingresos incrementales por programa; ROI del programa de fidelización.
**Diagnostic_Questions:** ¿Hay un programa de fidelización? ¿Los clientes recurrentes reciben beneficios especiales? ¿Se reconoce al cliente frecuente? ¿Hay incentivos para que el cliente prefiera la empresa? ¿Se ha evaluado el ROI de un programa de fidelización?
**Recommended_Actions:** Diseñar e implementar programa de fidelización (puntos, niveles, beneficios); segmentar clientes por valor y frecuencia; crear beneficios escalonados por antigüedad; implementar CRM para gestionar fidelización; medir impacto en retención y LTV.
**Severity_Level:** Medium
**Related_Patterns:** SAL-038, SAL-039, SAL-041, SAL-043, SAL-046


## Cross Selling

### SAL-046
**Pattern_Name:** Cross Selling Bajo o Inexistente
**Category:** Cross Selling
**Description:** El porcentaje de clientes que compran más de un producto/servicio es muy bajo, indicando que no se está aprovechando la base de clientes para vender productos complementarios.
**Observable_Symptoms:** La mayoría de los clientes compra un solo producto; no se ofrecen productos complementarios en la venta; clientes que no saben que la empresa tiene otros productos; el equipo no sugiere productos adicionales; falta de bundles o paquetes.
**Early_Warning_Signals:** % de clientes con > 1 producto < 20%; ratio de productos por cliente < 1.5; sin oferta de cross selling en el proceso de venta; equipo no capacitado en cross selling; ingresos de cross selling < 10% del total.
**Typical_Causes:** Falta de identificación de productos complementarios; proceso de venta no incluye cross selling; equipo no entrenado en sugerir productos adicionales; comisiones no incentivan cross selling; desconocimiento de la oferta completa por parte de vendedores.
**Business_Impact:** Clientes sub-explotados; menor LTV; oportunidad de ingresos perdida; mayor vulnerabilidad a pérdida de clientes (si solo tienen un producto, es más fácil que se vayan); inversión en captación no maximizada.
**Metrics_To_Check:** % de clientes con > 1 producto; productos por cliente; ingresos de cross selling / total; tasa de adopción de cross selling por vendedor; % de ventas con cross selling.
**Diagnostic_Questions:** ¿Los clientes conocen todos los productos de la empresa? ¿El proceso de venta incluye sugerir productos complementarios? ¿Hay comisiones por cross selling? ¿Los vendedores conocen la oferta completa? ¿Hay productos complementarios identificados?
**Recommended_Actions:** Identificar productos complementarios y crear bundles; incorporar cross selling en el proceso de venta estándar; entrenar al equipo en la oferta completa; ajustar comisiones para incentivar cross selling; crear campañas de cross selling a clientes existentes; medir y monitorear productos por cliente.
**Severity_Level:** Medium
**Related_Patterns:** SAL-022, SAL-038, SAL-047, SAL-048, SAL-049

### SAL-047
**Pattern_Name:** Productos Complementarios No Identificados
**Category:** Cross Selling
**Description:** La empresa tiene productos que son naturalmente complementarios pero no los ha identificado formalmente ni ha creado ofertas combinadas, perdiendo oportunidades de venta cruzada.
**Observable_Symptoms:** Productos que podrían venderse juntos pero se venden por separado; clientes que compran productos complementarios por separado (sin bundle); falta de ofertas combinadas; el equipo no sabe qué productos combinar; análisis de datos revela patrones de compra conjunta no explotados.
**Early_Warning_Signals:** Patrones de compra conjunta en datos de ventas no explotados; % de ventas conjuntas < potencial estimado; cliente promedio compra menos productos que el potencial; sin bundles ni paquetes; sin análisis de afinidad de productos.
**Typical_Causes:** Falta de análisis de datos de ventas; silos entre líneas de producto; equipo comercial no capacitado en oferta completa; falta de estrategia de producto; cultura de vender producto estrella ignorando el resto.
**Business_Impact:** Oportunidad de cross selling perdida; menor ticket promedio; clientes que no conocen la oferta completa; ventaja competitiva no aprovechada; ingresos por debajo del potencial.
**Metrics_To_Check:** % de clientes que compran productos complementarios; correlación de compra entre productos; % de ventas combinadas; ingresos adicionales potenciales por cross selling; tasa de adopción de bundles.
**Diagnostic_Questions:** ¿Se han analizado los patrones de compra conjunta? ¿Hay productos que se compran juntos naturalmente? ¿Se han creado bundles? ¿Los vendedores ofrecen combos? ¿Hay datos que indiquen oportunidades de cross selling?
**Recommended_Actions:** Analizar datos de ventas para identificar patrones de compra conjunta; crear bundles y paquetes de productos complementarios; entrenar al equipo en oferta de combos; promocionar ofertas combinadas; medir tasa de adopción de bundles.
**Severity_Level:** Medium
**Related_Patterns:** SAL-046, SAL-048, SAL-049, SAL-050

### SAL-048
**Pattern_Name:** Sin Oferta de Productos/Servicios Adicionales
**Category:** Cross Selling
**Description:** La empresa no ha desarrollado productos o servicios adicionales para vender a su base de clientes existentes, perdiendo la oportunidad de expandir el negocio con menor esfuerzo de captación.
**Observable_Symptoms:** La empresa solo tiene un producto o línea; clientes existentes no tienen opciones de comprar más; falta de innovación en la oferta; el crecimiento depende exclusivamente de nuevos clientes; el equipo no tiene nada más que ofrecer a clientes actuales.
**Early_Warning_Signals:** Sin nuevos productos lanzados en > 2 años; % de ingresos de productos complementarios = 0; clientes existentes sin oferta de expansión; crecimiento solo por nuevos clientes; sin road map de productos.
**Typical_Causes:** Falta de inversión en desarrollo de producto; cultura de producto único; equipo enfocado solo en captación; clientes existentes no priorizados; falta de innovación.
**Business_Impact:** Crecimiento limitado a captación de nuevos clientes; clientes existentes infravalorados; vulnerabilidad competitiva; oportunidad de expansión perdida; LTV bajo.
**Metrics_To_Check:** Número de productos/servicios; % de clientes que compran múltiples productos; ingresos de productos complementarios; inversión en desarrollo de producto; lanzamientos por año.
**Diagnostic_Questions:** ¿Hay productos complementarios que se podrían desarrollar? ¿Los clientes existentes demandan otros productos? ¿Se ha evaluado expandir la oferta? ¿Hay recursos para desarrollar nuevos productos? ¿La competencia ofrece productos complementarios?
**Recommended_Actions:** Desarrollar productos/servicios complementarios para base existente; investigar necesidades de clientes actuales; crear road map de productos; invertir en innovación; lanzar productos dirigidos a base instalada.
**Severity_Level:** Medium
**Related_Patterns:** SAL-046, SAL-047, SAL-049, SAL-050

### SAL-049
**Pattern_Name:** Cross Selling Solo en Primera Venta
**Category:** Cross Selling
**Description:** El cross selling solo se intenta en la primera venta (bundles iniciales) pero no hay un proceso continuo de cross selling a lo largo del ciclo de vida del cliente.
**Observable_Symptoms:** Bundles ofrecidos solo al inicio; clientes que nunca reciben ofertas de productos adicionales después de la compra; falta de campañas de cross selling post-venta; el equipo no contacta a clientes existentes para ofrecer nuevos productos; sin automatización de cross selling.
**Early_Warning_Signals:** Cross selling en primera venta > 80% del total de cross selling; sin campañas de cross selling a clientes existentes; % de cross selling post-venta < 20%; clientes antiguos con mismo número de productos que al inicio; sin triggers de cross selling en ciclo de vida.
**Typical_Causes:** Proceso de venta solo considera cross selling inicial; falta de estrategia de cross selling continuo; sin automatización de marketing; equipo no responsable de clientes existentes; CRM no configurado para cross selling post-venta.
**Business_Impact:** Oportunidades de cross selling perdidas a lo largo del ciclo de vida; clientes existentes sub-explotados; menor LTV; inversión en captación no maximizada; ingresos por debajo del potencial de la base instalada.
**Metrics_To_Check:** % de cross selling en primera venta vs post-venta; campañas de cross selling a existentes por año; % de clientes existentes que reciben ofertas; ingresos de cross selling post-venta; tasa de conversión de campañas de cross selling.
**Diagnostic_Questions:** ¿Se ofrecen productos adicionales después de la primera venta? ¿Hay campañas periódicas de cross selling? ¿El CRM tiene triggers de cross selling? ¿El equipo contacta a clientes existentes con nuevas ofertas? ¿Hay un proceso de cross selling en el ciclo de vida?
**Recommended_Actions:** Implementar campañas automatizadas de cross selling post-venta; configurar triggers en CRM (cumpleaños, aniversario, uso de producto); asignar responsabilidad de cross selling a account managers; crear calendario de ofertas a clientes existentes; medir cross selling post-venta como KPI.
**Severity_Level:** Medium
**Related_Patterns:** SAL-046, SAL-047, SAL-048, SAL-050, SAL-051

### SAL-050
**Pattern_Name:** Cross Selling Sin Segmentación
**Category:** Cross Selling
**Description:** Las ofertas de cross selling se hacen de manera masiva sin segmentar por perfil de cliente, necesidad o comportamiento, resultando en baja efectividad y molestia para los clientes.
**Observable_Symptoms:** Todos los clientes reciben las mismas ofertas; clientes reciben ofertas irrelevantes; baja tasa de conversión de cross selling; clientes que se quejan de comunicaciones irrelevantes; falta de personalización.
**Early_Warning_Signals:** Tasa de conversión de cross selling < 5%;% de ofertas rechazadas o ignoradas > 80%; clientes que se dan de baja de comunicaciones; sin segmentación en campañas de cross selling; ofertas no basadas en datos de cliente.
**Typical_Causes:** Falta de análisis de datos de clientes; CRM sin capacidades de segmentación; campañas masivas en lugar de segmentadas; desconocimiento del perfil de cada cliente; falta de personalización en la comunicación.
**Business_Impact:** Bajo retorno de inversión en cross selling; clientes molestos por ofertas irrelevantes; deterioro de la relación; recursos desperdiciados en campañas inefectivas; pérdida de oportunidades de cross selling real.
**Metrics_To_Check:** Tasa de conversión de cross selling por segmento; tasa de opt-out por campaña; % de ofertas relevantes; ingresos de cross selling segmentado vs masivo; satisfacción del cliente con ofertas.
**Diagnostic_Questions:** ¿Las ofertas de cross selling se basan en datos del cliente? ¿Hay segmentación por perfil, comportamiento o necesidad? ¿La tasa de conversión varía por segmento? ¿Los clientes reciben ofertas relevantes? ¿Hay personalización?
**Recommended_Actions:** Segmentar clientes por perfil, comportamiento de compra y necesidades; crear ofertas específicas por segmento; usar datos de CRM para personalizar comunicaciones; hacer pruebas A/B de ofertas; medir conversión por segmento y optimizar.
**Severity_Level:** Medium
**Related_Patterns:** SAL-046, SAL-047, SAL-049, SAL-051

### SAL-051
**Pattern_Name:** Cross Selling Sin Capacitación del Equipo
**Category:** Cross Selling
**Description:** El equipo comercial no está capacitado para hacer cross selling, no conoce los productos complementarios ni sabe cómo ofrecerlos.
**Observable_Symptoms:** Vendedores que solo venden el producto principal; equipo que no menciona otros productos; vendedores que no saben las características de otros productos; falta de argumentos de venta para cross selling; clientes que preguntan por otros productos y el vendedor no sabe responder.
**Early_Warning_Signals:** % de vendedores que hacen cross selling < 30%; pruebas de conocimiento de producto revelan desconocimiento de oferta completa; sin material de cross selling disponible; vendedores no incluyen cross selling en su proceso; comisiones no incentivan cross selling.
**Typical_Causes:** Entrenamiento enfocado solo en producto principal; falta de material de apoyo sobre otros productos; comisiones no incentivan cross selling; proceso de venta no incluye cross selling; cultura de "vender lo que se conoce".
**Business_Impact:** Cross selling bajo o nulo; clientes que no conocen la oferta completa; esfuerzo comercial sub-optimizado; ingresos por debajo del potencial; equipo con capacidades incompletas.
**Metrics_To_Check:** % de vendedores que hacen cross selling; % de ventas con cross selling por vendedor; conocimiento de producto del equipo; ingresos de cross selling por vendedor; capacitación en cross selling.
**Diagnostic_Questions:** ¿Los vendedores conocen todos los productos? ¿Hay entrenamiento en cross selling? ¿Hay material de apoyo (scripts, argumentos)? ¿Las comisiones incentivan cross selling? ¿El proceso de venta incluye cross selling?
**Recommended_Actions:** Capacitar al equipo en oferta completa de productos; crear scripts y argumentos de cross selling; ajustar comisiones para incentivar cross selling; incorporar cross selling en el proceso de ventas estándar; hacer role play de cross selling en entrenamientos.
**Severity_Level:** Medium
**Related_Patterns:** SAL-046, SAL-047, SAL-049, SAL-050


## Upselling

### SAL-052
**Pattern_Name:** Upselling Bajo o Inexistente
**Category:** Upselling
**Description:** El porcentaje de clientes que migran a planes/productos superiores es muy bajo, indicando que no se está aprovechando el potencial de crecimiento en clientes existentes.
**Observable_Symptoms:** Clientes que多年 con el mismo plan básico; falta de ofertas de upgrade; el equipo no ofrece versiones superiores; baja tasa de migración a planes premium; clientes que no saben que existen opciones superiores.
**Early_Warning_Signals:** % de clientes que upgradearon en el último año < 10%; % de clientes en plan básico > 70%; sin oferta de upgrade en el ciclo de vida; equipo no capacitado en upselling; ingresos de upselling < 5% del total.
**Typical_Causes:** Falta de productos/servicios escalonados (no hay versiones superiores); proceso de venta no incluye upselling; equipo no capacitado en ofrecer upgrades; comisiones no incentivan upselling; clientes no conocen opciones superiores.
**Business_Impact:** Clientes existentes sub-explotados; menor LTV; clientes en plan básico vulnerables a competencia; oportunidad de ingresos perdida; crecimiento por debajo del potencial.
**Metrics_To_Check:** % de clientes que upgradearon en el período; % de clientes por plan; ingresos de upselling / total; tasa de conversión de ofertas de upgrade; tiempo promedio hasta upgrade.
**Diagnostic_Questions:** ¿Hay versiones superiores de productos? ¿Los clientes conocen las opciones de upgrade? ¿El proceso de venta incluye upselling? ¿Hay incentivos para upselling? ¿Se hacen ofertas de upgrade periódicas?
**Recommended_Actions:** Desarrollar versiones escalonadas de productos (básico, premium, enterprise); incorporar upselling en proceso de venta estándar; crear campañas periódicas de upgrade; entrenar en upselling; ajustar comisiones; medir tasa de upgrade como KPI.
**Severity_Level:** Medium
**Related_Patterns:** SAL-017, SAL-019, SAL-022, SAL-046, SAL-047, SAL-053

### SAL-053
**Pattern_Name:** Upselling Sin Segmentación por Potencial
**Category:** Upselling
**Description:** Las ofertas de upselling se hacen sin considerar el potencial de cada cliente (tamaño, uso, necesidad), resultando en baja efectividad y molestia.
**Observable_Symptoms:** Ofrecen upgrade a clientes que no lo necesitan; clientes pequeños reciben ofertas premium; bajas tasas de conversión; clientes se quejan de ofertas irrelevantes; falta de criterios para identificar candidatos a upgrade.
**Early_Warning_Signals:** Tasa de conversión de upselling < 10%; % de ofertas de upgrade rechazadas > 80%; sin criterios de segmentación para upselling; clientes que reciben ofertas que no corresponden a su perfil; ofertas masivas no segmentadas.
**Typical_Causes:** Falta de análisis de datos de clientes; ausencia de modelo de propensity to upgrade; campañas masivas; desconocimiento del perfil de cliente; CRM sin capacidades de segmentación.
**Business_Impact:** Bajo retorno en upselling; clientes molestos por ofertas irrelevantes; recursos desperdiciados; oportunidades reales de upgrade no identificadas; ingresos por debajo del potencial.
**Metrics_To_Check:** Tasa de conversión de upselling por segmento; % de clientes con potencial de upgrade identificado; ingresos de upselling segmentado vs masivo; satisfacción con ofertas de upgrade.
**Diagnostic_Questions:** ¿Se segmentan los clientes por potencial de upgrade? ¿Hay criterios claros para identificar candidatos? ¿Las ofertas se personalizan? ¿La tasa de conversión varía por segmento? ¿Los datos del cliente se usan para segmentar?
**Recommended_Actions:** Segmentar clientes por tamaño, uso, antigüedad y potencial; implementar modelo de propensity to upgrade; personalizar ofertas por segmento; usar datos de CRM para identificar candidatos; hacer pruebas A/B de ofertas.
**Severity_Level:** Medium
**Related_Patterns:** SAL-048, SAL-050, SAL-052

### SAL-054
**Pattern_Name:** Upselling en Clientes No Preparados
**Category:** Upselling
**Description:** Se ofrece upgrade a clientes que no están preparados (no usan el producto actual completamente, no han visto valor suficiente), generando rechazo o upgrade prematuro que luego se cancela.
**Observable_Symptoms:** Clientes que upgraden pero vuelven al plan anterior; upgrades que no se usan; tasa de downgrade post-upgrade alta; clientes que upgraden por presión y se arrepienten; quejas post-upgrade por precio sin valor.
**Early_Warning_Signals:** % de downgrade post-upgrade > 20%; tasa de uso del producto post-upgrade < 30%; NPS de clientes que upgradearon baja; clientes que upgraden y no renuevan; tiempo entre upgrade y downgrade < 3 meses.
**Typical_Causes:** Upselling sin validar que el cliente está listo (uso del producto actual, necesidades); presión por cumplir metas de upselling; falta de customer health score; equipo no califica adecuadamente; clientes que upgraden por promociones no por valor.
**Business_Impact:** Ingresos temporales que se revierten; clientes insatisfechos por mala experiencia; recursos desperdiciados en upselling inefectivo; churn post-upgrade; desconfianza del cliente.
**Metrics_To_Check:** Tasa de downgrade post-upgrade; uso del producto post-upgrade; satisfacción de clientes que upgradearon; retención de upgrades vs no upgrades; tiempo hasta downgrade.
**Diagnostic_Questions:** ¿Los clientes usan el producto actual antes de upgrade? ¿Hay criterios de readiness para upgrade? ¿Los upgrades se basan en valor o en promociones? ¿Hay seguimiento post-upgrade? ¿Los clientes upgraden porque lo necesitan o por presión comercial?
**Recommended_Actions:** Establecer criterios de readiness para upgrade (uso, satisfacción, necesidades); implementar customer health score como condición para upselling; hacer upselling consultivo basado en valor; dar período de prueba de upgrade; monitorear satisfacción post-upgrade.
**Severity_Level:** Medium
**Related_Patterns:** SAL-048, SAL-052, SAL-053

### SAL-055
**Pattern_Name:** Sin Ofertas de Upgrade en el Ciclo de Vida
**Category:** Upselling
**Description:** La empresa no tiene ofertas de upgrade planificadas en las diferentes etapas del ciclo de vida del cliente (onboarding, madurez, renovación), perdiendo momentos clave para upsell.
**Observable_Symptoms:** Los clientes nunca reciben ofertas de upgrade; después de la compra inicial, no hay comunicación de upsell; falta de triggers de upgrade basados en comportamiento; renovaciones sin oferta de mejora; clientes que alcanzan hitos sin ser contactados.
**Early_Warning_Signals:** Sin campañas de upgrade en el ciclo de vida; sin triggers de upgrade en CRM; % de clientes contactados para upgrade en el año < 30%; renovaciones sin oferta de upgrade; onboarding sin mención de opciones superiores.
**Typical_Causes:** Falta de estrategia de upselling en ciclo de vida; CRM no configurado con triggers; equipo no responsable de upselling post-venta; falta de automatización de marketing; cultura de "vender y olvidar".
**Business_Impact:** Oportunidades de upgrade perdidas en momentos clave; clientes que podrían upgradear no reciben oferta; LTV por debajo del potencial; ingresos recurrentes no maximizados.
**Metrics_To_Check:** % de clientes contactados para upgrade por etapa; campañas de upgrade en ciclo de vida; triggers de upgrade configurados; tasa de conversión por etapa; ingresos de upgrade por etapa.
**Diagnostic_Questions:** ¿Hay ofertas de upgrade en onboarding? ¿En madurez? ¿En renovación? ¿El CRM tiene triggers de upgrade basados en comportamiento? ¿El equipo contacta a clientes en hitos? ¿Hay campañas automatizadas de upgrade?
**Recommended_Actions:** Mapear ciclo de vida del cliente con puntos de upgrade; configurar triggers en CRM (uso, antigüedad, renovación); crear campañas automatizadas de upgrade por etapa; asignar responsabilidad de upselling en post-venta; medir conversión por etapa.
**Severity_Level:** Medium
**Related_Patterns:** SAL-038, SAL-046, SAL-049, SAL-052


## Cobertura Comercial

### SAL-056
**Pattern_Name:** Cobertura Geográfica Insuficiente
**Category:** Cobertura Comercial
**Description:** La fuerza de ventas no cubre adecuadamente el territorio geográfico de mercado, dejando zonas sin atención o con atención sub-óptima.
**Observable_Symptoms:** Zonas del país/ciudad sin visita de vendedores; clientes en ciertas áreas que se quejan de falta de atención; vendedores concentrados en zona céntrica; potencial de mercado en zonas no cubiertas; ventas concentradas geográficamente.
**Early_Warning_Signals:** % de territorio cubierto < 50% del mercado potencial; diferencia de penetración entre mejor zona y peor > 5x; clientes en zonas no cubiertas sin contacto; vendedores concentrados en pocas zonas; potencial de mercado en zonas sin cobertura.
**Typical_Causes:** Crecimiento histórico no planificado; falta de análisis de potencial por zona; vendedores asignados por comodidad no por mercado; recursos limitados mal distribuidos; falta de estrategia de cobertura geográfica.
**Business_Impact:** Mercado potencial no explotado; clientes insatisfechos en zonas sin cobertura; competidores capturan zonas desatendidas; crecimiento limitado por alcance; desbalance en carga de trabajo de vendedores.
**Metrics_To_Check:** % de territorio cubierto; penetración por zona geográfica; potencial vs capturado por zona; número de vendedores por zona; satisfacción de clientes por zona.
**Diagnostic_Questions:** ¿Qué zonas del mercado no están cubiertas? ¿Hay potencial de mercado en zonas sin cobertura? ¿La distribución de vendedores refleja el potencial de mercado? ¿Los competidores están en zonas que la empresa no cubre? ¿Hay clientes potenciales en zonas no atendidas?
**Recommended_Actions:** Mapear potencial de mercado por zona geográfica; redistribuir vendedores según potencial y cobertura; establecer rutas de visita regulares; considerar canales alternativos en zonas de bajo potencial; medir penetración por zona.
**Severity_Level:** Medium
**Related_Patterns:** SAL-024, SAL-026, SAL-057, SAL-058

### SAL-057
**Pattern_Name:** Cobertura de Segmentos de Cliente Incompleta
**Category:** Cobertura Comercial
**Description:** La empresa solo atiende ciertos segmentos de clientes (pequeños, grandes, un sector) dejando segmentos enteros sin cubrir o mal atendidos.
**Observable_Symptoms:** Base de clientes concentrada en un segmento; clientes de otros segmentos no son contactados; la oferta no está adaptada a otros segmentos; el equipo comercial solo sabe vender a cierto perfil; oportunidades en otros segmentos no explotadas.
**Early_Warning_Signals:** % de ingresos de un solo segmento > 70%; penetración baja en segmentos con potencial; sin oferta adaptada a otros segmentos; vendedores no capacitados para otros segmentos; % de clientes por segmento desbalanceado.
**Typical_Causes:** Estrategia histórica enfocada en un segmento; falta de análisis de segmentos; equipo especializado en un perfil; oferta diseñada para un segmento; falta de recursos para expandir a otros segmentos.
**Business_Impact:** Dependencia excesiva de un segmento; vulnerabilidad a cambios en ese segmento; oportunidad de crecimiento en otros segmentos perdida; competidores capturan otros segmentos; límite al crecimiento.
**Metrics_To_Check:** % de ingresos por segmento; penetración en cada segmento; potencial vs capturado por segmento; satisfacción por segmento; % de clientes por segmento.
**Diagnostic_Questions:** ¿Qué segmentos de clientes no se están atendiendo? ¿Hay potencial en esos segmentos? ¿La oferta actual sirve para otros segmentos? ¿El equipo sabe vender a otros perfiles? ¿Los competidores están en segmentos que la empresa no cubre?
**Recommended_Actions:** Identificar segmentos de alto potencial no cubiertos; adaptar oferta y propuesta de valor por segmento; capacitar al equipo en venta a nuevos segmentos; asignar recursos específicos a nuevos segmentos; desarrollar materiales y canales por segmento.
**Severity_Level:** Medium
**Related_Patterns:** SAL-026, SAL-054, SAL-056, SAL-058

### SAL-058
**Pattern_Name:** Sobrecarga de Clientes por Vendedor
**Category:** Cobertura Comercial
**Description:** Los vendedores tienen demasiados clientes asignados, lo que impide dar atención de calidad, hacer seguimiento adecuado y prospectar nuevos clientes.
**Observable_Symptoms:** Vendedores que no dan abasto con clientes existentes; clientes que se quejan de falta de atención; vendedores pasan el día "apagando incendios"; no hay tiempo para prospectar; seguimiento de clientes espaciado.
**Early_Warning_Signals:** Clientes por vendedor > benchmark sectorial; % de clientes contactados en el mes < 50%; tiempo entre visitas a cliente > 90 días; vendedores que trabajan horas extras regularmente; rotación por agotamiento.
**Typical_Causes:** Crecimiento de cartera sin aumentar equipo; mala distribución de clientes; falta de segmentación (todos los clientes reciben mismo nivel de atención); vendedores que no quieren ceder clientes; estructura comercial insuficiente.
**Business_Impact:** Atención al cliente deficiente; clientes descuidados que se van; vendedores quemados; prospección abandonada; ingresos por cliente por debajo del potencial.
**Metrics_To_Check:** Clientes por vendedor; % de clientes contactados en el período; tiempo entre visitas; horas de trabajo semanales; rotación del equipo.
**Diagnostic_Questions:** ¿Cuántos clientes tiene cada vendedor? ¿Cuál es el benchmark del sector? ¿Los clientes reciben atención adecuada? ¿Hay tiempo para prospectar? ¿Los vendedores están sobrecargados?
**Recommended_Actions:** Redistribuir clientes entre vendedores; segmentar clientes por valor y ajustar frecuencia de contacto; contratar más vendedores si es necesario; implementar canales de bajo costo para clientes pequeños; establecer tope de clientes por vendedor.
**Severity_Level:** High
**Related_Patterns:** SAL-024, SAL-025, SAL-026, SAL-036, SAL-056

### SAL-059
**Pattern_Name:** Canales de Venta No Diversificados
**Category:** Cobertura Comercial
**Description:** La empresa depende de un solo canal de venta (presencial, telefónico, web), limitando su capacidad de llegar a diferentes segmentos de clientes.
**Observable_Symptoms:** Un solo canal genera > 80% de ingresos; clientes piden otros canales no disponibles; falta de presencia digital; canal único vulnerable a cambios; equipo resistente a nuevos canales.
**Early_Warning_Signals:** % de ingresos de canal principal > 80%; sin canal online; sin canal telefónico dedicado; clientes demandan otros canales; canal principal muestra saturación o declive.
**Typical_Causes:** Inversión histórica en un solo canal; falta de capacidad para desarrollar nuevos canales; resistencia al cambio; desconocimiento de otros canales; falta de recursos.
**Business_Impact:** Vulnerabilidad si el canal principal falla o cambia; segmentos de clientes no alcanzables por el canal actual; límite al crecimiento; desventaja competitiva; dependencia peligrosa.
**Metrics_To_Check:** % de ingresos por canal; diversificación de canales; penetración en segmentos por canal; satisfacción del cliente con canales disponibles; crecimiento de canales alternativos.
**Diagnostic_Questions:** ¿Qué pasa si el canal principal falla? ¿Hay clientes que no se pueden alcanzar con el canal actual? ¿Qué canales usa la competencia? ¿Hay demanda de otros canales? ¿Se ha evaluado el ROI de nuevos canales?
**Recommended_Actions:** Desarrollar canales alternativos (online, telefónico, distribuidores, alianzas); invertir en presencia digital; probar nuevos canales con pilotos; capacitar al equipo en nuevos canales; medir y optimizar mix de canales.
**Severity_Level:** High
**Related_Patterns:** SAL-008, SAL-023, SAL-054, SAL-056

### SAL-060
**Pattern_Name:** Canales con Conflicto y Canibalización
**Category:** Cobertura Comercial
**Description:** Los canales de venta compiten entre sí por los mismos clientes, generando conflictos internos, canibalización y erosión de márgenes.
**Observable_Symptoms:** Mismo cliente contactado por múltiples canales; vendedores internos compiten con distribuidores; clientes confundidos por diferentes precios o condiciones; canales que se quejan de otros canales; descuentos para captar clientes de otros canales.
**Early_Warning_Signals:** Mismo cliente en pipeline de múltiples canales; quejas de canales sobre competencia interna; % de clientes que compran en más de un canal; diferencias de precio entre canales; canales que ofrecen descuentos para quitar clientes a otros canales.
**Typical_Causes:** Estrategia multicanal sin reglas claras; falta de definición de territorios o segmentos por canal; comisiones que incentivan robo de clientes; sin sistema de derivación entre canales; crecimiento desordenado de canales.
**Business_Impact:** Conflictos internos; clientes confundidos; descuentos innecesarios; ineficiencia en fuerza de ventas; erosión de margen; relaciones tensas con distribuidores.
**Metrics_To_Check:** % de clientes en múltiples canales; quejas de canales; diferencia de precio entre canales; costo de adquisición por canal ajustado por canibalización; contribución neta por canal.
**Diagnostic_Questions:** ¿Hay reglas claras de asignación de clientes por canal? ¿Los canales tienen territorios o segmentos definidos? ¿Hay conflictos entre canales? ¿Los incentivos están alineados o generan competencia? ¿Hay un sistema de derivación?
**Recommended_Actions:** Definir reglas claras de asignación (territorios, segmentos, productos) por canal; implementar sistema de derivación; ajustar comisiones para evitar conflictos; medir contribución neta por canal (considerando canibalización); alinear incentivos entre canales.
**Severity_Level:** Medium
**Related_Patterns:** SAL-023, SAL-031, SAL-054, SAL-059


## Gestión de Oportunidades

### SAL-061
**Pattern_Name:** Oportunidades Sin Próxima Acción Definida
**Category:** Gestión de Oportunidades
**Description:** Las oportunidades en el pipeline no tienen una próxima acción concreta ni fecha definida, lo que impide que avancen y genera estancamiento.
**Observable_Symptoms:** Oportunidades con notas vagas ("pendiente de decisión", "el cliente está evaluando"); pipeline lleno pero poco movimiento; vendedores que no saben qué hacer con cada oportunidad; revisión de pipeline revela falta de acciones concretas; oportunidades que no se mueven por semanas.
**Early_Warning_Signals:** % de oportunidades sin próxima acción > 40%; oportunidades sin fecha de próximo contacto; % de oportunidades estancadas > 30%; edad promedio de oportunidades sin acción; falta de seguimiento entre revisiones.
**Typical_Causes:** Falta de proceso de gestión de oportunidades; vendedores no capacitados en avanzar oportunidades; CRM no exige próxima acción; cultura de "esperar a que el cliente decida"; falta de disciplina en revisiones de pipeline.
**Business_Impact:** Pipeline inflado con oportunidades inmóviles; forecast poco confiable; tiempo perdido en oportunidades que no avanzan; menor velocidad de funnel; resultados por debajo del potencial.
**Metrics_To_Check:** % de oportunidades con próxima acción definida; edad promedio sin acción; % de pipeline que avanza semanalmente; velocidad de funnel.
**Diagnostic_Questions:** ¿Cada oportunidad tiene una próxima acción y fecha definida? ¿El CRM exige este campo? ¿En la revisión de pipeline se valida la próxima acción? ¿Los vendedores saben cómo avanzar oportunidades? ¿Hay oportunidades sin actividad por semanas?
**Recommended_Actions:** Establecer regla: toda oportunidad debe tener próxima acción + fecha; configurar CRM para exigir estos campos; revisar pipeline semanalmente validando avances; entrenar en técnicas de avance de oportunidades; purgar oportunidades sin avance.
**Severity_Level:** High
**Related_Patterns:** SAL-003, SAL-005, SAL-007, SAL-056, SAL-075

### SAL-062
**Pattern_Name:** Oportunidades Sin Calificación Formal
**Category:** Gestión de Oportunidades
**Description:** Las oportunidades no pasan por un proceso de calificación formal (BANT, MEDDIC, etc.), por lo que se persiguen oportunidades que nunca debieron entrar al pipeline.
**Observable_Symptoms:** Muchas oportunidades que nunca se concretan; pipeline lleno de "ruido"; vendedores persiguiendo leads sin presupuesto o sin autoridad; el equipo se queja de "malos leads"; oportunidades que llegan a cierre y se descubre que no había presupuesto.
**Early_Warning_Signals:** % de oportunidades sin calificación > 50%; ratio de conversión de pipeline bajo; oportunidades perdidas que nunca debieron estar en pipeline; presupuesto como causa de pérdida en etapa tardía; falta de criterios de calificación.
**Typical_Causes:** Falta de proceso de calificación formal; equipo no capacitado en calificar; presión por llenar pipeline lleva a incluir cualquier cosa; vendedores optimistas que no califican objetivamente; falta de criterios de salida.
**Business_Impact:** Desperdicio de recursos en falsas oportunidades; pipeline inflado; forecast inexacto; frustración del equipo; resultados por debajo del potencial.
**Metrics_To_Check:** % de oportunidades calificadas formalmente; ratio de conversión pipeline; % de pipeline perdido en etapa temprana (debió calificarse antes); precisión de forecast.
**Diagnostic_Questions:** ¿Hay un proceso de calificación formal (BANT, MEDDIC, etc.)? ¿Toda oportunidad pasa por calificación antes de entrar al pipeline? ¿Los vendedores están capacitados en calificación? ¿Hay criterios de salida claros? ¿Se revisa la calificación en las revisiones de pipeline?
**Recommended_Actions:** Implementar proceso de calificación formal (BANT, MEDDIC o similar); exigir calificación antes de crear oportunidad en CRM; entrenar al equipo en calificación; revisar calificación en pipeline reviews; establecer criterios de salida para oportunidades no calificadas.
**Severity_Level:** High
**Related_Patterns:** SAL-002, SAL-003, SAL-007, SAL-015, SAL-056, SAL-075

### SAL-063
**Pattern_Name:** Oportunidades con Edad Avanzada sin Decisión
**Category:** Gestión de Oportunidades
**Description:** Oportunidades que llevan mucho tiempo en el pipeline sin avanzar ni cerrarse, indicando que el cliente no tiene urgencia, no está calificado o el vendedor no gestiona adecuadamente.
**Observable_Symptoms:** Oportunidades con más de 6 meses en pipeline; clientes que "están por decidir" desde hace meses; oportunidades que nunca se cierran ni se pierden; pipeline con "viejas" oportunidades que nadie purga; optimismo recurrente sobre mismas oportunidades.
**Early_Warning_Signals:** % de oportunidades con edad > 90 días; edad promedio del pipeline; oportunidades con > 6 meses sin cierre ni pérdida; % de pipeline perdido por "no decisión"; vendedores que mantienen oportunidades viejas "por si acaso".
**Typical_Causes:** Falta de purga periódica de pipeline; vendedores que no quieren perder oportunidades (optimismo); clientes sin urgencia real; calificación inadecuada inicial; falta de política de antigüedad máxima.
**Business_Impact:** Pipeline inflado que da falsa cobertura; forecast poco confiable; recursos invertidos en oportunidades que no avanzan; distorsión de métricas de pipeline; decisiones basadas en datos incorrectos.
**Metrics_To_Check:** % de oportunidades por rango de edad; edad promedio del pipeline; tasa de purga mensual; % de pipeline cerrado/pedido por mes; antigüedad de oportunidades activas.
**Diagnostic_Questions:** ¿Hay oportunidades con más de 6 meses en pipeline? ¿Por qué no se han cerrado o perdido? ¿Hay una política de antigüedad máxima? ¿Se purga el pipeline regularmente? ¿Los vendedores mantienen oportunidades falsas por optimismo?
**Recommended_Actions:** Establecer política de antigüedad máxima (ej. 90 días sin avance = purgar); purgar pipeline trimestralmente; revisar antigüedad en cada pipeline review; entrenar en manejo de objeciones de tiempo; implementar regla de "fecha de caducidad".
**Severity_Level:** Medium
**Related_Patterns:** SAL-003, SAL-005, SAL-007, SAL-016, SAL-061, SAL-075

### SAL-064
**Pattern_Name:** Pérdida de Oportunidades por Falta de Seguimiento
**Category:** Gestión de Oportunidades
**Description:** Oportunidades se pierden porque el vendedor no hace el seguimiento adecuado en el momento correcto, dejando que el cliente se enfríe o la competencia gane.
**Observable_Symptoms:** Clientes que mencionan "nadie me llamó"; oportunidades que desaparecen sin explicación; vendedores que no cumplen con seguimientos prometidos; pérdidas por "falta de contacto" o "el cliente se enfrió"; CRM con tareas de seguimiento vencidas.
**Early_Warning_Signals:** % de tareas de seguimiento vencidas > 30%; % de oportunidades perdidas por "falta de seguimiento"; tiempo de respuesta a consultas de clientes; % de oportunidades sin actividad > 7 días; clientes que contactan porque no los llamaron.
**Typical_Causes:** Falta de disciplina de seguimiento; vendedores abrumados por cantidad de oportunidades; CRM no configurado con alertas; cultura de "esperar a que el cliente llame"; falta de proceso de seguimiento estructurado.
**Business_Impact:** Ingresos perdidos por falta de acción; imagen de poca seriedad; clientes que se van a la competencia; desperdicio de esfuerzo de captación de oportunidades; mala reputación.
**Metrics_To_Check:** % de tareas de seguimiento completadas a tiempo; % de oportunidades perdidas por seguimiento; tiempo promedio de respuesta a cliente; % de oportunidades con actividad reciente; cumplimiento de SLA de seguimiento.
**Diagnostic_Questions:** ¿Hay un proceso de seguimiento definido? ¿Los vendedores cumplen con los seguimientos? ¿El CRM alerta sobre seguimientos vencidos? ¿Se miden las pérdidas por falta de seguimiento? ¿Hay consecuencias por no hacer seguimiento?
**Recommended_Actions:** Definir SLA de seguimiento post-contacto; configurar alertas automáticas en CRM; establecer proceso de seguimiento estructurado (días 1, 3, 7, 15, 30); monitorear cumplimiento de seguimiento; vincular seguimiento a compensación.
**Severity_Level:** High
**Related_Patterns:** SAL-003, SAL-005, SAL-011, SAL-016, SAL-061, SAL-075

### SAL-065
**Pattern_Name:** Oportunidades Gestionadas sin Metodología
**Category:** Gestión de Oportunidades
**Description:** Las oportunidades se gestionan sin una metodología de ventas definida, cada vendedor usa su propio enfoque, resultando en procesos inconsistentes y resultados impredecibles.
**Observable_Symptoms:** Cada vendedor tiene su propio método; no hay fases de venta definidas; falta de criterios de avance entre etapas; procesos de venta no documentados; dificultad para identificar en qué etapa está una oportunidad.
**Early_Warning_Signals:** Sin metodología de ventas implementada; % de oportunidades en etapa "personalizada" (no estándar); vendedores que no pueden explicar su proceso; falta de etapas de venta definidas; resultados inconsistentes entre vendedores.
**Typical_Causes:** Falta de inversión en metodología de ventas; cultura de "cada vendedor sabe"; liderazgo sin formación en metodologías; resistencia al cambio; desconocimiento de metodologías existentes (SPIN, Challenger, MEDDIC, etc.).
**Business_Impact:** Procesos no replicables; dificultad para escalar; resultados inconsistentes; baja previsibilidad; rotación afecta más porque no hay proceso estándar.
**Metrics_To_Check:** % de oportunidades gestionadas con metodología; % de vendedores que siguen la metodología; consistencia de pipeline entre vendedores; previsibilidad de forecast; resultados antes y después de implementar metodología.
**Diagnostic_Questions:** ¿Hay una metodología de ventas implementada? ¿Todos los vendedores la siguen? ¿Hay fases de venta definidas? ¿Se revisa el avance según la metodología? ¿Los resultados son consistentes?
**Recommended_Actions:** Implementar metodología de ventas (MEDDIC, SPIN, Challenger, Sandler); entrenar a todo el equipo; configurar CRM según fases de la metodología; hacer role play y acompañamiento; medir adopción y resultados.
**Severity_Level:** Medium
**Related_Patterns:** SAL-010, SAL-024, SAL-030, SAL-065, SAL-075

### SAL-066
**Pattern_Name:** Sin Proceso de Deal Review
**Category:** Gestión de Oportunidades
**Description:** No existe un proceso formal de revisión de oportunidades (deal review) donde se analicen las probabilidades de cierre y se definan acciones para avanzar oportunidades clave.
**Observable_Symptoms:** No hay reuniones periódicas de revisión de pipeline; gerencia no conoce el estado de oportunidades clave; oportunidades importantes sin visibilidad; falta de apoyo gerencial en oportunidades complejas; decisiones sobre oportunidades basadas en intuición.
**Early_Warning_Signals:** Sin deal reviews semanales/quincenales; % de oportunidades sin revisión gerencial; forecast basado solo en opinión del vendedor; falta de apoyo en oportunidades complejas; decisiones comerciales sin análisis estructurado.
**Typical_Causes:** Falta de disciplina de revisión; gerencia no involucrada en pipeline; cultura de "cada vendedor gestiona sus oportunidades"; falta de agenda; desconocimiento del valor del deal review.
**Business_Impact**: Oportunidades clave sin atención adecuada; pronósticos poco confiables; falta de apoyo en momentos críticos; decisiones basadas en información incompleta; desempeño sub-óptimo.
**Metrics_To_Check:** % de pipeline revisado semanalmente; frecuencia de deal reviews; % de oportunidades con apoyo gerencial; precisión de forecast por oportunidad; tasa de rescate de oportunidades en riesgo.
**Diagnostic_Questions:** ¿Hay reuniones de revisión de pipeline regulares? ¿Se revisan las oportunidades clave? ¿La gerencia participa en oportunidades complejas? ¿Hay un formato de deal review? ¿Se toman acciones concretas de las revisiones?
**Recommended_Actions:** Implementar deal reviews semanales; establecer formato de revisión (situación, probabilidad, próxima acción, apoyo necesario); involucrar a gerencia en oportunidades clave; documentar acuerdos y seguimiento; medir impacto de deal reviews en resultados.
**Severity_Level:** Medium
**Related_Patterns:** SAL-003, SAL-007, SAL-056, SAL-061, SAL-075


## Forecast

### SAL-067
**Pattern_Name:** Forecast Consistentemente Optimista
**Category:** Forecast
**Description:** El forecast de ventas es sistemáticamente superior a los resultados reales, indicando que las proyecciones no son realistas y que la gerencia toma decisiones basadas en información inflada.
**Observable_Symptoms:** Mes tras mes, el forecast no se cumple; la gerencia celebra un buen forecast pero los resultados no llegan; los vendedores reportan números optimistas que no se concretan; diferencia recurrente entre forecast y real; pérdida de credibilidad del forecast.
**Early_Warning_Signals:** Precisión de forecast (real / forecast) < 70% en múltiples períodos; sesgo optimista consistente (forecast siempre > real); desviación promedio > 20% en los últimos 6 meses; forecast no se ajusta con la realidad; gerencia ignora el forecast.
**Typical_Causes:** Falta de criterios objetivos para forecast; vendedores reportan pipeline como forecast; presión gerencial por mostrar números altos; cultura de optimismo; forecast basado en esperanza no en datos; falta de consecuencias por forecast inexacto.
**Business_Impact:** Decisiones basadas en información incorrecta; mala asignación de recursos; incumplimiento de metas; pérdida de credibilidad del área comercial; planificación financiera errada.
**Metrics_To_Check:** Precisión de forecast (real / forecast); desviación promedio; sesgo (forecast - real); % de meses con forecast > real; precisión por vendedor.
**Diagnostic_Questions:** ¿El forecast se basa en datos objetivos o en opiniones? ¿Hay criterios claros para incluir una oportunidad en forecast? ¿La gerencia presiona por forecast altos? ¿Hay consecuencias por forecast inexacto? ¿Se ajusta el forecast durante el mes?
**Recommended_Actions:** Establecer criterios objetivos de forecast (etapa en pipeline, próxima acción, fecha probable); separar pipeline de forecast; implementar metodología de forecast con pesos por etapa; revisar forecast semanalmente; vincular precisión de forecast a evaluación del equipo.
**Severity_Level:** Critical
**Related_Patterns:** SAL-003, SAL-006, SAL-007, SAL-056, SAL-068, SAL-075

### SAL-068
**Pattern_Name:** Forecast Sin Pesos por Etapa
**Category:** Forecast
**Description:** El forecast se calcula sumando el valor de todas las oportunidades sin aplicar probabilidades por etapa, sobrestimando drásticamente los ingresos esperados.
**Observable_Symptoms:** Forecast = suma de pipeline (sin ponderar); pipeline de etapas tempranas cuenta igual que etapas tardías; forecast irrealmente alto vs capacidad histórica; gerencia sorprendida cuando no se cumple; falta de metodología de forecast ponderado.
**Early_Warning_Signals:** Forecast sin ponderar > 3x forecast ponderado; % de pipeline en etapa temprana > 50% del forecast; correlación baja entre forecast y real; forecast ponderado nunca se usa; metodología de forecast no definida.
**Typical_Causes:** Desconocimiento de metodología de forecast ponderado; falta de definición de pesos por etapa; cultura de "todo suma"; gerencia prefiere ver números grandes; falta de herramientas para forecast ponderado.
**Business_Impact:** Forecast consistentemente errado; decisiones basadas en números irreales; imposibilidad de planificar; incumplimiento de metas; pérdida de credibilidad.
**Metrics_To_Check:** Diferencia entre forecast ponderado y no ponderado; precisión de forecast ponderado vs no ponderado; % de pipeline por etapa en forecast; factores de ponderación asignados.
**Diagnostic_Questions:** ¿El forecast pondera las oportunidades por etapa? ¿Hay factores de ponderación definidos y actualizados? ¿La gerencia usa forecast ponderado o sin ponderar? ¿La precisión mejora con ponderación? ¿Hay herramientas que calculen forecast ponderado?
**Recommended_Actions:** Implementar forecast ponderado por etapa con factores basados en datos históricos; configurar CRM para forecast ponderado; entrenar al equipo en metodología de forecast; reportar forecast ponderado como principal; revisar factores de ponderación periódicamente.
**Severity_Level:** High
**Related_Patterns:** SAL-006, SAL-007, SAL-056, SAL-067, SAL-075

### SAL-069
**Pattern_Name:** Forecast Basado Solo en Opinión del Vendedor
**Category:** Forecast
**Description:** El forecast se basa exclusivamente en la opinión subjetiva del vendedor sobre si va a cerrar o no, sin criterios objetivos que respalden la estimación.
**Observable_Symptoms:** Forecast = "lo que el vendedor cree"; cada vendedor tiene su propio criterio; no hay forma de validar el forecast; vendedores optimistas siempre reportan alto; vendedores pesimistas siempre reportan bajo; gerencia no confía en el forecast pero lo usa igual.
**Early_Warning_Signals:** Sin criterios objetivos de forecast; forecast basado en "feeling"; desviación alta entre forecast y real; vendedores no pueden explicar por qué creen que van a cerrar; falta de correlación entre forecast del vendedor y resultado.
**Typical_Causes:** Falta de metodología de forecast; gerencia no exige criterios; cultura de "el vendedor conoce al cliente"; falta de herramientas; vendedores no entrenados en forecast.
**Business_Impact:** Forecast poco confiable; imposibilidad de planificar; resultados sorpresa; decisiones incorrectas; desconfianza en el proceso comercial.
**Metrics_To_Check:** Precisión de forecast por vendedor; correlación forecast subjetivo vs real; % de forecast con criterios objetivos; desviación estándar de precisión entre vendedores.
**Diagnostic_Questions:** ¿El forecast se basa en datos objetivos o en lo que el vendedor "cree"? ¿Hay criterios definidos para incluir en forecast? ¿Los vendedores pueden explicar por qué creen que cerrarán? ¿La precisión varía mucho entre vendedores? ¿Hay entrenamiento en forecast?
**Recommended_Actions:** Establecer criterios objetivos para incluir oportunidad en forecast; implementar forecast con pesos por etapa y verificación de criterios; entrenar al equipo en forecast basado en datos; reconciliar forecast con pipeline; revisar forecast con datos objetivos.
**Severity_Level:** High
**Related_Patterns:** SAL-007, SAL-056, SAL-067, SAL-068, SAL-075

### SAL-070
**Pattern_Name:** Sin Forecast de Mediano Plazo
**Category:** Forecast
**Description:** La empresa solo hace forecast a corto plazo (este mes, próximo mes) sin proyecciones a 3-6 meses, lo que impide la planificación estratégica y la detección temprana de problemas.
**Observable_Symptoms:** Solo se proyecta el mes en curso; no hay visibilidad de los próximos trimestres; las decisiones se toman con visión de muy corto plazo; sorpresas cuando bajan los ingresos; imposibilidad de planificar inversiones.
**Early_Warning_Signals:** Forecast limitado a 30 días; sin pipeline proyectado a 90 días; sin rolling forecast; planificación comercial sin base de mediano plazo; decisiones reactivas por falta de visibilidad.
**Typical_Causes:** Falta de disciplina de planificación; equipo enfocado solo en el corto plazo; falta de herramientas; cultura de "vivir el día a día"; gerencia no exige forecast de mediano plazo.
**Business_Impact:** Imposibilidad de planificar; reacciones tardías a cambios; inversiones sin base sólida; incertidumbre permanente; dificultad para gestionar recursos.
**Metrics_To_Check:** Forecast a 30, 60, 90 días; % de pipeline en etapa temprana para próximos meses; rolling forecast; precisión de forecast a 90 días; visibilidad de pipeline a mediano plazo.
**Diagnostic_Questions:** ¿Hay forecast a 90 días? ¿Se proyecta el pipeline futuro? ¿Se planifica con base en forecast de mediano plazo? ¿Hay sorpresas recurrentes por falta de visibilidad? ¿Se puede predecir ingresos a 3 meses?
**Recommended_Actions:** Implementar rolling forecast a 90 días; proyectar pipeline futuro basado en actividades de prospección; revisar forecast de mediano plazo mensualmente; planificar recursos basados en forecast; incorporar forecast en reuniones de dirección.
**Severity_Level:** High
**Related_Patterns:** SAL-001, SAL-004, SAL-006, SAL-056, SAL-067

### SAL-071
**Pattern_Name:** Forecast No Ajustado Durante el Período
**Category:** Forecast
**Description:** El forecast se hace una vez al mes y no se actualiza durante el período, por lo que la gerencia opera con información desactualizada y no puede reaccionar a cambios.
**Observable_Symptoms:** Forecast congelado al inicio del mes; no se actualiza con avances o pérdidas; sorpresas a mitad de mes; decisiones basadas en forecast de hace semanas; falta de visibilidad de la evolución del período.
**Early_Warning_Signals:** Forecast actualizado solo una vez al mes; desviación entre forecast inicial y real > 30%; sin revisión de forecast durante el mes; decisiones tomadas con información de semanas; falta de alertas tempranas de desviación.
**Typical_Causes:** Falta de disciplina de actualización; CRM no actualizado; cultura de "forecast es al inicio"; gerencia no exige actualizaciones; herramientas no soportan actualizaciones en tiempo real.
**Business_Impact:** Decisiones basadas en información desactualizada; incapacidad de reaccionar a cambios; imposibilidad de ajustar planes; incumplimiento de metas por falta de corrección a tiempo; planificación deficiente.
**Metrics_To_Check:** Frecuencia de actualización de forecast; desviación entre forecast inicial y real; % de meses con forecast ajustado; precisión de forecast actualizado vs inicial.
**Diagnostic_Questions:** ¿Se actualiza el forecast durante el mes? ¿Con qué frecuencia? ¿La gerencia revisa el forecast actualizado? ¿Hay alertas de cambios en forecast? ¿El CRM permite actualización en tiempo real?
**Recommended_Actions:** Establecer actualización semanal de forecast; configurar CRM para actualización en tiempo real; revisar forecast semanalmente en reunión comercial; implementar alertas de cambios significativos; ajustar planes basados en forecast actualizado.
**Severity_Level:** Medium
**Related_Patterns:** SAL-056, SAL-067, SAL-068, SAL-070

### SAL-072
**Pattern_Name:** Forecast y Presupuesto sin Reconciliación
**Category:** Forecast
**Description:** El forecast comercial no se reconcilia con el presupuesto financiero, generando planes de negocio inconsistentes donde el área comercial proyecta algo diferente a lo que finanzas presupuesta.
**Observable_Symptoms:** Forecast comercial y presupuesto financiero no coinciden; finanzas planifica con un número, ventas con otro; discusiones entre áreas sobre "el número correcto"; falta de un número único de planificación; decisiones basadas en cifras inconsistentes.
**Early_Warning_Signals:** Diferencia entre forecast y presupuesto > 10%; forecast y presupuesto elaborados por separado; sin proceso de reconciliación; áreas con metas inconsistentes; planificación basada en múltiples números.
**Typical_Causes:** Falta de integración entre comercial y finanzas; silos organizacionales; forecast y presupuesto con metodologías diferentes; ausencia de proceso de reconciliación; culturas departamentales separadas.
**Business_Impact:** Planificación inconsistente; asignación de recursos inadecuada; conflictos entre áreas; decisiones basadas en información contradictoria; imposibilidad de tener un plan unificado.
**Metrics_To_Check:** Diferencia forecast vs presupuesto; % de meses con forecast y presupuesto reconciliados; número de reuniones de reconciliación; alineación de metas entre áreas.
**Diagnostic_Questions:** ¿El forecast y el presupuesto se reconcilian? ¿Hay un número único de planificación? ¿Comercial y finanzas trabajan con la misma cifra? ¿Hay reuniones de alineación? ¿Los planes de negocio son consistentes?
**Recommended_Actions:** Establecer proceso mensual de reconciliación forecast-presupuesto; alinear metodologías de proyección; crear un número único de planificación; realizar reuniones conjuntas comercial-finanzas; integrar sistemas de forecast y presupuesto.
**Severity_Level:** High
**Related_Patterns:** SAL-067, SAL-068, SAL-070


## Ciclo de Ventas

### SAL-073
**Pattern_Name:** Ciclo de Ventas Prolongado
**Category:** Ciclo de Ventas
**Description:** El ciclo de ventas (desde primer contacto hasta cierre) es significativamente más largo que el promedio del sector, aumentando el costo de adquisición y reduciendo la velocidad de ingresos.
**Observable_Symptoms:** Clientes que tardan meses en decidir; múltiples reuniones sin avance; ciclo de ventas que excede el benchmark; el equipo reporta "clientes que nunca deciden"; alta inversión de tiempo por cliente.
**Early_Warning_Signals:** Ciclo de ventas > 2x el benchmark sectorial; tiempo promedio por etapa en aumento; duración del ciclo creciente trimestre a trimestre; % de ciclo en etapa de evaluación > 50%; ratio tiempo invertido / ticket bajo.
**Typical_Causes:** Proceso de ventas sin urgencia; clientes no calificados en urgencia; múltiples stakeholders no identificados; propuesta de valor poco clara; falta de sentido de urgencia creado por el vendedor; producto de alta complejidad sin soporte de venta.
**Business_Impact:** Mayor costo de adquisición; menor velocidad de ingresos; equipo menos productivo (cierra menos clientes en mismo tiempo); pipeline requiere más oportunidades para mismo resultado; forecast incierto.
**Metrics_To_Check:** Duración promedio del ciclo de ventas; ciclo por segmento de cliente; ciclo por vendedor; comparación con benchmark; tendencia del ciclo.
**Diagnostic_Questions:** ¿En qué etapa se pierde más tiempo? ¿Los clientes tienen urgencia real? ¿Se identifican todos los stakeholders? ¿El proceso de ventas está optimizado? ¿El equipo tiene habilidades para acelerar el ciclo?
**Recommended_Actions:** Mapear y optimizar proceso de ventas; calificar urgencia desde el inicio; identificar stakeholders tempranamente; crear urgencia (ofertas limitadas, trigger events); entrenar en técnicas de aceleración de ciclo; implementar herramientas de venta que agilicen el proceso.
**Severity_Level:** High
**Related_Patterns:** SAL-002, SAL-003, SAL-005, SAL-009, SAL-016, SAL-075

### SAL-074
**Pattern_Name:** Ciclo de Ventas Variable por Segmento
**Category:** Ciclo de Ventas
**Description:** El ciclo de ventas varía drásticamente entre diferentes segmentos de clientes o productos, y la empresa no gestiona estas diferencias, aplicando el mismo proceso a todos.
**Observable_Symptoms:** Algunos segmentos cierran rápido, otros tardan mucho; productos simples tienen el mismo proceso que complejos; clientes pequeños reciben mismo tratamiento que grandes; falta de segmentación del proceso de ventas; el equipo trata a todos los clientes igual.
**Early_Warning_Signals:** Diferencia de ciclo entre segmentos > 2x; proceso de ventas único para todos los segmentos; falta de rutas de venta diferenciadas; % de ciclo prolongado en segmentos que deberían ser rápidos; ineficiencia en segmentos simples.
**Typical_Causes:** Proceso de ventas único para todos; falta de segmentación de clientes; equipo no adapta enfoque; cultura de "tratar a todos por igual"; desconocimiento de diferencias de ciclo por segmento.
**Business_Impact:** Ineficiencia en segmentos de ciclo corto (se les dedica más tiempo del necesario); segmentos de ciclo largo no reciben atención adecuada; recursos mal asignados; oportunidades perdidas por proceso inadecuado.
**Metrics_To_Check:** Ciclo por segmento de cliente; ciclo por producto; diferencia de ciclo entre segmentos; % de proceso adaptado al segmento; eficiencia por segmento.
**Diagnostic_Questions:** ¿El ciclo varía significativamente por segmento? ¿El proceso de ventas se adapta al segmento? ¿Los vendedores ajustan su enfoque según el cliente? ¿Hay rutas de venta diferenciadas? ¿Los recursos se asignan según complejidad del ciclo?
**Recommended_Actions:** Segmentar clientes y definir rutas de venta diferenciadas por segmento; crear procesos de venta específicos (express, estándar, enterprise); entrenar al equipo en adaptación al segmento; asignar recursos según complejidad; medir ciclo por segmento y optimizar.
**Severity_Level:** Medium
**Related_Patterns:** SAL-005, SAL-009, SAL-017, SAL-023, SAL-073, SAL-075

### SAL-075
**Pattern_Name:** Ciclo de Ventas No Medido
**Category:** Ciclo de Ventas
**Description:** La empresa no mide la duración del ciclo de ventas, por lo que no tiene visibilidad de su eficiencia ni puede identificar oportunidades de mejora.
**Observable_Symptoms:** No se sabe cuánto tarda una venta promedio; falta de métricas de ciclo; decisiones sin datos de duración; imposibilidad de identificar cuellos de botella; sin benchmark de ciclo.
**Early_Warning_Signals:** Sin métrica de ciclo de ventas; CRM no registra fechas de etapas; sin reportes de duración por etapa; vendedores no miden su ciclo; falta de análisis de eficiencia del proceso.
**Typical_Causes:** Falta de cultura de métricas; CRM no configurado para medir ciclo; gerencia no exige la métrica; desconocimiento de su importancia; equipo no capacitado en tracking de ciclo.
**Business_Impact:** Imposibilidad de mejorar lo que no se mide; cuellos de botella no identificados; ineficiencias no corregidas; forecast impreciso; incapacidad de planificar recursos.
**Metrics_To_Check:** Las que deberían medirse: duración total del ciclo; duración por etapa; duración por vendedor; duración por segmento; comparación con benchmark.
**Diagnostic_Questions:** ¿Se mide el ciclo de ventas? ¿El CRM registra fechas de entrada y salida de etapas? ¿Hay reportes de duración? ¿Se analizan los cuellos de botella? ¿Los vendedores conocen su ciclo promedio?
**Recommended_Actions:** Configurar CRM para medir ciclo de ventas (fechas de etapa); implementar reportes de duración por etapa, vendedor y segmento; revisar ciclo en reuniones comerciales; establecer benchmark y metas de ciclo; analizar y optimizar etapas que más tardan.
**Severity_Level:** Medium
**Related_Patterns:** SAL-003, SAL-005, SAL-030, SAL-056, SAL-073

### SAL-076
**Pattern_Name:** Ciclo con Etapas Sin Criterios de Avance
**Category:** Ciclo de Ventas
**Description:** Las etapas del ciclo de ventas no tienen criterios claros de avance, por lo que las oportunidades pasan de etapa sin estar realmente listas o se saltan etapas.
**Observable_Symptoms:** Oportunidades que "saltan" etapas; clientes que llegan a cierre sin haber visto demo o propuesta; procesos de venta inconsistentes; falta de definición de qué significa cada etapa; vendedores tienen su propia interpretación de las etapas.
**Early_Warning_Signals:** % de oportunidades que no siguen el proceso secuencial; vendedores definen etapas subjetivamente; falta de criterios de entrada/salida por etapa; confusión sobre qué significa cada etapa; procesos bypassados.
**Typical_Causes:** Etapas de venta mal definidas; falta de criterios de avance; vendedores que no siguen el proceso; presión por acelerar lleva a saltar etapas; cultura de "hacer lo que funciona".
**Business_Impact:** Oportunidades mal calificadas avanzan sin mérito; pipeline poco confiable; forecast inexacto; proceso de ventas no replicable; resultados inconsistentes.
**Metrics_To_Check:** % de oportunidades que siguen el proceso secuencial; % de oportunidades que saltan etapas; consistencia de pipeline entre vendedores; precisión de forecast por etapa.
**Diagnostic_Questions:** ¿Las etapas de venta tienen criterios de entrada y salida definidos? ¿Todas las oportunidades siguen el proceso secuencial? ¿Los vendedores interpretan las etapas de la misma manera? ¿Hay consecuencias por saltar etapas? ¿Los criterios de avance están documentados?
**Recommended_Actions:** Definir criterios de entrada y salida para cada etapa; documentar y comunicar a todo el equipo; configurar CRM para evitar saltos de etapa; entrenar en el significado de cada etapa; revisar cumplimiento de proceso en pipeline reviews.
**Severity_Level:** Medium
**Related_Patterns:** SAL-002, SAL-003, SAL-007, SAL-056, SAL-062, SAL-075

### SAL-077
**Pattern_Name:** Ciclo de Ventas sin Seguimiento Post-Venta
**Category:** Ciclo de Ventas
**Description:** El ciclo de ventas termina en el cierre sin considerar el seguimiento post-venta, perdiendo oportunidades de recurrencia, referidos y fidelización.
**Observable_Symptoms:** Después del cierre, no hay contacto hasta la próxima venta; clientes que compran y no reciben seguimiento; falta de proceso de handoff a post-venta; el vendedor desaparece después de cobrar; cliente no sabe a quién contactar después de la compra.
**Early_Warning_Signals:** Sin proceso de handoff a post-venta; tiempo sin contacto post-cierre > 30 días; clientes que reportan "abandono" post-compra; % de clientes con seguimiento post-venta < 50%; NPS post-compra bajo.
**Typical_Causes:** Ciclo de ventas definido solo hasta el cierre; falta de integración ventas-postventa; vendedores no involucrados en transición; cultura de "cerrar y seguir"; falta de proceso de onboarding.
**Business_Impact:** Clientes insatisfechos post-compra; baja retención; pérdida de oportunidades de upselling/cross-selling; referidos no solicitados; LTV por debajo del potencial.
**Metrics_To_Check:** % de clientes con handoff formal post-venta; tiempo hasta primer contacto post-venta; satisfacción post-compra; tasa de referidos; % de clientes que completan onboarding.
**Diagnostic_Questions:** ¿Hay un proceso de handoff de ventas a post-venta? ¿El cliente recibe seguimiento después de comprar? ¿Hay un proceso de onboarding? ¿Se solicita el referido después de la compra? ¿El vendedor hace seguimiento post-cierre?
**Recommended_Actions:** Definir proceso de handoff ventas-postventa; implementar programa de onboarding para nuevos clientes; establecer contacto post-venta a los 7, 30, 90 días; solicitar referidos en el momento de mayor satisfacción; medir satisfacción post-compra.
**Severity_Level:** Medium
**Related_Patterns:** SAL-036, SAL-038, SAL-039, SAL-042, SAL-046, SAL-077
