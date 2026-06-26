# Process_Patterns.md

**File:** Process_Patterns.md
**Description:** Patrones operativos y de procesos para PyMEs — diagnóstico de eficiencia, productividad, cuellos de botella, calidad, retrabajo, desperdicios, automatización, estandarización, capacidad instalada, planificación y mejora continua.
**Total Patterns:** 130 (PRC-001 a PRC-130)
**Categories:** 11
**Version:** 1.0

---

## Summary Table

| Category | Pattern IDs | Count | Description |
|---|---|---|---|
| Eficiencia | PRC-001 a PRC-011 | 11 | Uso ineficiente de recursos y tiempo |
| Productividad | PRC-012 a PRC-023 | 12 | Baja producción por unidad de recurso |
| Cuellos de botella | PRC-024 a PRC-035 | 12 | Etapas que limitan el flujo total |
| Calidad | PRC-036 a PRC-047 | 12 | Problemas de calidad y defectos |
| Retrabajo | PRC-048 a PRC-058 | 11 | Corrección de trabajo mal hecho |
| Desperdicios | PRC-059 a PRC-070 | 12 | Siete desperdicios + otros |
| Automatización | PRC-071 a PRC-081 | 11 | Falta o mala implementación de automatización |
| Estandarización | PRC-082 a PRC-092 | 11 | Procesos no estandarizados |
| Capacidad instalada | PRC-093 a PRC-104 | 12 | Capacidad mal dimensionada o utilizada |
| Planificación | PRC-105 a PRC-116 | 12 | Planificación deficiente de operaciones |
| Mejora continua | PRC-117 a PRC-130 | 14 | Ausencia de cultura de mejora |

---

# Patrones de Procesos

## Eficiencia

### PRC-001
**Pattern_Name:** Tiempo de Ciclo Excesivo
**Category:** Eficiencia
**Description:** El tiempo total que toma completar un proceso o entregar un producto/servicio es significativamente mayor al necesario, por demoras, esperas o pasos que no agregan valor.
**Observable_Symptoms:** Los pedidos tardan más de lo que el cliente espera; hay tiempos muertos entre etapas; los procesos tienen pasos que no agregan valor; el equipo está ocupado pero los resultados tardan; los plazos de entrega se alargan constantemente.
**Early_Warning_Signals:** Tiempo de ciclo > 2x el tiempo de valor agregado; lead time creciente; % de tiempo de valor agregado < 20%; cuellos de botella visibles; clientes se quejan de demoras.
**Typical_Causes:** Procesos con muchas transferencias; falta de paralelización; lotes grandes; esperas entre etapas; aprobaciones innecesarias; layout ineficiente.
**Business_Impact:** Clientes insatisfechos por demoras; menor capacidad efectiva; capital de trabajo inmovilizado; pérdida de ventas por lead time largo; competitividad reducida.
**Metrics_To_Check:** Tiempo de ciclo total; tiempo de valor agregado; % de tiempo de valor agregado; lead time por tipo de pedido; tendencia del tiempo de ciclo.
**Diagnostic_Questions:** ¿Cuánto tiempo toma completar el proceso? ¿Cuánto de ese tiempo agrega valor? ¿Dónde ocurren las mayores demoras? ¿Los pasos son necesarios? ¿El proceso está diseñado para velocidad?
**Recommended_Actions:** Mapear flujo de valor (VSM); identificar y eliminar pasos que no agregan valor; reducir transferencias; implementar trabajo en paralelo; reducir tamaño de lotes; optimizar layout.
**Severity_Level:** Critical
**Related_Patterns:** PRC-012, PRC-024, PRC-025, PRC-059, PRC-093, PRC-105

### PRC-002
**Pattern_Name:** Procesos con Múltiples Aprobaciones Innecesarias
**Category:** Eficiencia
**Description:** El proceso requiere aprobaciones de múltiples niveles para decisiones que podrían tomarse en el punto de acción, generando demoras y burocracia excesiva.
**Observable_Symptoms:** Cada decisión requiere firma de varios niveles; aprobaciones demoran más que la ejecución; el equipo espera autorizaciones para avanzar; procesos lentos por burocracia; niveles de aprobación excesivos.
**Early_Warning_Signals:** Número de aprobaciones por proceso > 3; tiempo de aprobación > 30% del tiempo total; % de aprobaciones que rechazan < 5% (son mero trámite); decisiones podrían tomarse en nivel inferior; cuellos de botella en aprobaciones.
**Typical_Causes:** Cultura de control excesivo; falta de confianza en el equipo; procesos heredados; miedo a errores; falta de delegación; organigrama jerárquico.
**Business_Impact:** Procesos lentos; equipo desmotivado por falta de autonomía; gerentes dedicados a aprobar en lugar de gestionar; costos administrativos altos; capacidad de respuesta baja.
**Metrics_To_Check:** Número de aprobaciones por proceso; tiempo de aprobación; % de aprobaciones que modifican la decisión; % de aprobaciones que son trámite; tiempo de respuesta al cliente.
**Diagnostic_Questions:** ¿Cuántas aprobaciones requiere cada proceso? ¿Son todas necesarias? ¿Qué % de aprobaciones rechazan o modifican? ¿Podrían delegarse? ¿La burocracia afecta la velocidad?
**Recommended_Actions:** Revisar y eliminar aprobaciones que no agregan valor; delegar autoridad al nivel de ejecución; establecer límites por monto/riesgo; implementar "excepción por defecto"; medir tiempo de aprobación.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-008, PRC-059, PRC-082, PRC-105

### PRC-003
**Pattern_Name:** Movimiento Innecesario de Personas, Materiales o Información
**Category:** Eficiencia
**Description:** Personas, materiales o información se mueven más de lo necesario debido a un layout deficiente, procesos mal diseñados o falta de integración, consumiendo tiempo sin agregar valor.
**Observable_Symptoms:** Personas caminan largas distancias para completar tareas; materiales se mueven de un lado a otro; información viaja por múltiples sistemas; el layout obliga a desplazamientos; el equipo pasa tiempo transportando no produciendo.
**Early_Warning_Signals:** Distancia recorrida por operario > 20% del tiempo; movimientos de materiales innecesarios; información ingresa múltiples veces en diferentes sistemas; layout no optimizado; diagrama de flujo muestra movimientos sin valor.
**Typical_Causes:** Layout no diseñado para flujo; procesos en silos físicos; sistemas no integrados; falta de análisis de movimientos; crecimiento orgánico sin planificación de espacio.
**Business_Impact:** Tiempo improductivo; fatiga del equipo; mayor riesgo de errores; procesos lentos; capacidad desperdiciada; costos operativos más altos.
**Metrics_To_Check:** Distancia recorrida por operario/día; % de tiempo en movimiento vs valor agregado; número de transferencias; tiempo de transporte; costo de movimientos.
**Diagnostic_Questions:** ¿Cuánto se mueven personas y materiales? ¿El layout está optimizado para el flujo? ¿La información viaja eficientemente? ¿Hay movimientos que podrían eliminarse? ¿El espacio físico está bien distribuido?
**Recommended_Actions:** Rediseñar layout basado en flujo de valor; acercar estaciones de trabajo relacionadas; integrar sistemas para eliminar movimientos de información; implementar 5S; medir movimientos y reducirlos.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-008, PRC-059, PRC-063, PRC-093

### PRC-004
**Pattern_Name:** Procesos con Pasos Redundantes
**Category:** Eficiencia
**Description:** El proceso contiene pasos que se repiten o duplican en diferentes etapas o departamentos, haciendo el mismo trabajo múltiples veces sin valor agregado.
**Observable_Symptoms:** La misma información se pide o ingresa varias veces; diferentes departamentos hacen la misma verificación; tareas duplicadas en distintos puntos del proceso; el equipo nota que "esto ya se hizo antes"; procesos redundantes.
**Early_Warning_Signals:** Número de veces que se ingresa misma información > 1; verificaciones duplicadas; tareas repetidas en diferentes departamentos; % de pasos redundantes > 10%; quejas del equipo sobre duplicación.
**Typical_Causes:** Procesos diseñados en silos; falta de visión de extremo a extremo; sistemas no integrados; desconfianza entre departamentos; procesos heredados sin revisión.
**Business_Impact:** Tiempo y recursos desperdiciados; procesos lentos; equipo frustrado; costos operativos más altos; mayor probabilidad de errores por reintroducción de datos.
**Metrics_To_Check:** Número de pasos redundantes; % de pasos que duplican trabajo; tiempo dedicado a tareas redundantes; costo de redundancia; satisfacción del equipo.
**Diagnostic_Questions:** ¿Hay pasos duplicados en el proceso? ¿La misma información se ingresa múltiples veces? ¿Hay verificaciones repetidas? ¿Los departamentos hacen lo mismo? ¿El proceso podría simplificarse?
**Recommended_Actions:** Mapear proceso de extremo a extremo; identificar y eliminar redundancias; integrar sistemas; establecer dueño de proceso con visión global; rediseñar eliminando pasos duplicados.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-003, PRC-008, PRC-059, PRC-082

### PRC-005
**Pattern_Name:** Tiempo de Setup o Cambio de Lote Excesivo
**Category:** Eficiencia
**Description:** El tiempo requerido para preparar una máquina, línea o equipo entre cambios de producto o lote es excesivo, reduciendo la capacidad productiva y obligando a producir en lotes grandes.
**Observable_Symptoms:** Cambios de producto toman mucho tiempo; se producen lotes grandes para evitar cambios; las máquinas están paradas durante cambios; el equipo "prepara" más que produce; los tiempos de setup no se miden ni mejoran.
**Early_Warning_Signals:** Tiempo de setup > 10% del tiempo total disponible; relación setup/tiempo de procesamiento alta; lotes mínimos grandes por tiempo de setup; sin medición de setup; sin iniciativa SMED.
**Typical_Causes:** Falta de metodología SMED; preparaciones internas (con máquina parada) no convertidas a externas; desorganización en herramientas y materiales; falta de estandarización; cultura de "siempre fue así".
**Business_Impact:** Capacidad perdida por setups largos; lotes grandes incrementan inventario; menor flexibilidad; lead times largos; respuesta lenta a cambios de demanda.
**Metrics_To_Check:** Tiempo de setup promedio; relación setup/tiempo de procesamiento; % de tiempo disponible perdido en setups; tendencia de mejora de setup; tamaño de lote mínimo.
**Diagnostic_Questions:** ¿Cuánto tiempo toma cambiar de producto? ¿Hay iniciativa SMED? ¿Los cambios están estandarizados? ¿Las herramientas están organizadas? ¿Se producen lotes grandes por el tiempo de setup?
**Recommended_Actions:** Implementar SMED (Single Minute Exchange of Die); convertir preparaciones internas en externas; estandarizar y organizar herramientas; medir y mejorar setup continuamente; reducir tamaño de lotes.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-012, PRC-024, PRC-059, PRC-093, PRC-106

### PRC-006
**Pattern_Name:** Baja Eficiencia General de Equipos (OEE)
**Category:** Eficiencia
**Description:** La eficiencia general de los equipos (OEE) está por debajo del 60%, indicando pérdidas significativas por disponibilidad, rendimiento y calidad que no se gestionan.
**Observable_Symptoms:** Máquinas paradas frecuentemente; velocidad de operación menor a la nominal; defectos y retrabajos; la producción real es muy inferior a la capacidad instalada; no se mide OEE.
**Early_Warning_Signals:** OEE < 60%; disponibilidad < 85%; rendimiento < 80%; calidad < 95%; tendencia de OEE decreciente; % de tiempo perdido no medido.
**Typical_Causes:** Falta de mantenimiento preventivo; paradas no programadas; micro-paradas; velocidad reducida por problemas de calidad; falta de estandarización; operadores no entrenados.
**Business_Impact:** Menor producción sin invertir en nueva capacidad; costos unitarios más altos; plazos de entrega más largos; necesidad de invertir en más equipos; competitividad reducida.
**Metrics_To_Check:** OEE; disponibilidad; rendimiento; calidad; tendencia de OEE; causas de pérdida de OEE.
**Diagnostic_Questions:** ¿Medimos OEE? ¿Cuál es el OEE actual? ¿Dónde están las mayores pérdidas (disponibilidad, rendimiento, calidad)? ¿Hay plan de mejora de OEE? ¿Los operadores conocen OEE?
**Recommended_Actions:** Implementar medición de OEE; atacar causas de pérdida por disponibilidad (TPM); mejorar rendimiento (reducir micro-paradas, estandarizar); mejorar calidad (control de procesos); establecer metas de OEE; capacitar operadores.
**Severity_Level:** Critical
**Related_Patterns:** PRC-012, PRC-024, PRC-036, PRC-059, PRC-093, PRC-125

### PRC-007
**Pattern_Name:** Procesos con Buffer Excesivos entre Etapas
**Category:** Eficiencia
**Description:** Existen inventarios o buffers excesivos entre etapas del proceso, ocultando problemas de flujo, aumentando el capital de trabajo y extendiendo los lead times.
**Observable_Symptoms:** Acumulación de trabajo en proceso (WIP) entre estaciones; inventario en proceso visible; producción se detiene por falta de espacio; WIP oculta problemas; tiempos de espera largos.
**Early_Warning_Signals:** WIP > 20% del valor de producción; días de inventario en proceso elevados; rotación de WIP baja; espacio ocupado por WIP; problemas ocultos por buffers.
**Typical_Causes:** Desbalance de capacidad entre etapas; lotes grandes; procesos no sincronizados; miedo a parar la producción; falta de flujo continuo.
**Business_Impact:** Capital de trabajo inmovilizado; lead times largos; problemas ocultos no se resuelven; espacio desperdiciado; mayor riesgo de obsolescencia o daños.
**Metrics_To_Check:** Nivel de WIP; rotación de WIP; días de inventario en proceso; % de espacio ocupado por WIP; tendencia de WIP.
**Diagnostic_Questions:** ¿Hay acumulación de WIP entre etapas? ¿Cuánto inventario en proceso hay? ¿El WIP oculta problemas? ¿Las etapas están balanceadas? ¿Podríamos implementar flujo continuo?
**Recommended_Actions:** Implementar producción pull; reducir tamaño de lotes; balancear capacidades; establecer sistema kanban; reducir WIP gradualmente para exponer problemas; implementar flujo de una pieza.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-024, PRC-025, PRC-059, PRC-093, PRC-105

### PRC-008
**Pattern_Name:** Procesos con Handoffs Excesivos
**Category:** Eficiencia
**Description:** El proceso requiere múltiples transferencias entre personas, departamentos o sistemas, cada una con riesgo de demora, error y pérdida de información.
**Observable_Symptoms:** Muchas personas tocan el mismo pedido; cada transferencia agrega demora; la información se pierde o distorsiona en cada handoff; errores por comunicación deficiente; el proceso tiene muchos "pases de mano".
**Early_Warning_Signals:** Número de handoffs por proceso > 5; % de errores en handoffs; tiempo acumulado en handoffs; información perdida o distorsionada; quejas sobre coordinación.
**Typical_Causes:** Procesos funcionales en silos; organigrama departamental estricto; falta de equipos multifuncionales; cultura de "eso no es mi trabajo"; sistemas no integrados.
**Business_Impact:** Procesos lentos; errores de comunicación; responsabilidad difusa; falta de accountability; clientes afectados por demoras; costos de coordinación altos.
**Metrics_To_Check:** Número de handoffs por proceso; tiempo en handoffs; % de errores por handoff; satisfacción del cliente interno; tiempo de ciclo por handoff.
**Diagnostic_Questions:** ¿Cuántos handoffs tiene el proceso? ¿Son necesarios todos? ¿Dónde ocurren más errores? ¿Podrían reducirse con equipos multifuncionales? ¿La información fluye correctamente?
**Recommended_Actions:** Reducir número de handoffs; crear equipos multifuncionales; implementar case management (una persona responsable); integrar sistemas; estandarizar transferencias.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-003, PRC-004, PRC-059, PRC-082

### PRC-009
**Pattern_Name:** Exceso de Reuniones Operativas
**Category:** Eficiencia
**Description:** El equipo dedica una proporción significativa del tiempo a reuniones que podrían resolverse con comunicación asíncrona o decisiones más rápidas, restando tiempo a la ejecución.
**Observable_Symptoms:** Múltiples reuniones diarias; el equipo pasa más tiempo en reuniones que trabajando; reuniones sin agenda ni objetivo claro; asistentes que no necesitan estar; reuniones que podrían ser un email.
**Early_Warning_Signals:** % de tiempo en reuniones > 25%; número de reuniones por semana > 10; reuniones sin agenda; duración promedio > 1 hora; reuniones recurrentes sin evaluación de necesidad.
**Typical_Causes:** Cultura de "reuniones = trabajo"; falta de confianza para decidir sin reunión; ausencia de normas de reuniones; gerencia no predica con el ejemplo; falta de herramientas de comunicación asíncrona.
**Business_Impact:** Tiempo de ejecución reducido; fatiga de reuniones; decisiones lentas; equipos interrumpidos constantemente; menor productividad.
**Metrics_To_Check:** % de tiempo en reuniones; número de reuniones por semana; horas-hombre en reuniones; % de reuniones con agenda y objetivo; satisfacción del equipo con reuniones.
**Diagnostic_Questions:** ¿Cuánto tiempo dedicamos a reuniones? ¿Son todas necesarias? ¿Tienen agenda y objetivo? ¿Quién realmente necesita asistir? ¿Podrían ser más cortas o asíncronas?
**Recommended_Actions:** Establecer políticas de reuniones (agenda, tiempo, asistentes); implementar "día sin reuniones"; evaluar recurrencia; usar herramientas asíncronas; cancelar reuniones sin agenda.
**Severity_Level:** Medium
**Related_Patterns:** PRC-008, PRC-059, PRC-105, PRC-117

### PRC-010
**Pattern_Name:** Procesos sin Dueño Claro
**Category:** Eficiencia
**Description:** Los procesos no tienen un dueño asignado responsable de su rendimiento, mejora y coordinación, resultando en procesos sin accountability y problemas crónicos no resueltos.
**Observable_Symptoms:** Nadie es responsable del proceso completo; cada quien hace su parte sin visión global; problemas cruzan departamentos sin resolver; el proceso no mejora; falta de accountability.
**Early_Warning_Signals:** % de procesos con dueño asignado < 30%; problemas que cruzan departamentos no se resuelven; procesos sin mejora; falta de métricas de proceso; nadie puede describir el proceso completo.
**Typical_Causes:** Organización funcional jerárquica; cultura de "eso no es mi problema"; falta de gestión por procesos; desconocimiento de la metodología; resistencia a la rendición de cuentas.
**Business_Impact:** Problemas no se resuelven; procesos no mejoran; clientes afectados por problemas entre áreas; responsabilidad difusa; costos de coordinación altos.
**Metrics_To_Check:** % de procesos con dueño; % de procesos con métricas; % de procesos con mejora documentada; tiempo de resolución de problemas cross-funcionales; satisfacción del cliente interno.
**Diagnostic_Questions:** ¿Cada proceso tiene un dueño claro? ¿Alguien es responsable del resultado completo? ¿Los problemas entre áreas tienen solución? ¿Los procesos mejoran con el tiempo? ¿Hay accountability?
**Recommended_Actions:** Asignar dueños de procesos; definir responsabilidades y autoridad; establecer métricas de proceso; implementar reuniones de revisión de procesos; crear cultura de gestión por procesos.
**Severity_Level:** High
**Related_Patterns:** PRC-001, PRC-004, PRC-008, PRC-082, PRC-117

### PRC-011
**Pattern_Name:** Procesos con Baja Estandarización
**Category:** Eficiencia
**Description:** Los procesos no están estandarizados, cada persona o turno ejecuta de manera diferente, generando variabilidad en resultados, calidad y tiempos.
**Observable_Symptoms:** Cada operario hace el trabajo a su manera; resultados inconsistentes entre turnos; el método cambia según quién ejecuta; no hay instrucciones de trabajo; la calidad varía.
**Early_Warning_Signals:** % de procesos estandarizados < 30%; sin instrucciones de trabajo escritas; variabilidad alta entre operadores; quejas de calidad inconsistentes; método no documentado.
**Typical_Causes:** Falta de disciplina de estandarización; cultura de "cada quien sabe su trabajo"; resistencia a la estandarización; falta de recursos para documentar; desconocimiento de la importancia.
**Business_Impact:** Resultados inconsistentes; calidad variable; dificultad para entrenar; problemas difíciles de replicar; imposibilidad de mejora continua sin estándar.
**Metrics_To_Check:** % de procesos estandarizados; variabilidad entre operadores; desviación de tiempo entre ejecuciones; % de operadores que siguen el estándar; índice de cumplimiento de estándar.
**Diagnostic_Questions:** ¿Los procesos están estandarizados? ¿Hay instrucciones de trabajo? ¿Todos hacen el trabajo igual? ¿La variabilidad es alta? ¿Tenemos un estándar documentado?
**Recommended_Actions:** Estandarizar procesos críticos; crear instrucciones de trabajo; capacitar en el estándar; verificar cumplimiento; mejorar el estándar continuamente (kaizen).
**Severity_Level:** Critical
**Related_Patterns:** PRC-036, PRC-048, PRC-059, PRC-082, PRC-117, PRC-125


## Productividad

### PRC-012
**Pattern_Name:** Productividad Laboral Baja y Sin Diagnóstico
**Category:** Productividad
**Description:** La productividad por empleado es baja en comparación con el benchmark del sector o con la capacidad instalada, y la empresa no investiga las causas para mejorarla.
**Observable_Symptoms:** La empresa produce menos por empleado que competidores; el equipo parece ocupado pero los resultados no acompañan; no hay métricas de productividad individual; las causas de baja productividad no se conocen; se contrata más personal en lugar de mejorar la productividad.
**Early_Warning_Signals:** Productividad por empleado < 70% del benchmark sectorial; tendencia de productividad plana o decreciente; % de tiempo productivo < 60%; sin métricas de productividad; % de capacidad utilizada baja.
**Typical_Causes:** Falta de medición de productividad; procesos ineficientes; equipo no capacitado; falta de incentivos; herramientas o equipos inadecuados; distracciones y reuniones excesivas.
**Business_Impact:** Costos laborales unitarios altos; necesidad de más personal para misma producción; márgenes reducidos; competitividad baja; escalabilidad limitada.
**Metrics_To_Check:** Productividad por empleado (unidades/hora, valor agregado/empleado); benchmark sectorial; % de tiempo productivo; tendencia de productividad; costo laboral unitario.
**Diagnostic_Questions:** ¿Medimos la productividad individual y global? ¿Cómo nos comparamos con el sector? ¿El equipo es productivo? ¿Sabemos qué afecta la productividad? ¿Hay planes de mejora?
**Recommended_Actions:** Implementar medición de productividad; identificar causas de baja productividad (estudio de tiempos, análisis de desperdicios); capacitar al equipo; mejorar procesos y herramientas; establecer metas de productividad; alinear incentivos.
**Severity_Level:** Critical
**Related_Patterns:** PRC-001, PRC-006, PRC-013, PRC-024, PRC-059, PRC-093

### PRC-013
**Pattern_Name:** Micro-Gestión que Reduce la Productividad
**Category:** Productividad
**Description:** La supervisión excesiva y el control detallado de cada tarea ralentizan la toma de decisiones, desmotivan al equipo y reducen la productividad en lugar de aumentarla.
**Observable_Symptoms:** Los supervisores revisan cada paso; el equipo espera autorización para todo; decisiones simples requieren aprobación; los empleados no toman iniciativa; hay desmotivación y rotación.
**Early_Warning_Signals:** Tiempo dedicado a supervisión > 30% del tiempo total; número de aprobaciones por tarea alto; equipo no toma decisiones autónomamente; rotación alta; clima laboral negativo.
**Typical_Causes:** Falta de confianza en el equipo; supervisores que no delegan; cultura de control; miedo a errores; falta de capacitación del equipo; liderazgo inmaduro.
**Business_Impact:** Procesos lentos; equipo desmotivado; baja productividad; rotación; falta de desarrollo del equipo; gerentes quemados.
**Metrics_To_Check:** Ratio supervisión/producción; % de decisiones autónomas; tiempo de respuesta a decisiones; rotación; clima laboral.
**Diagnostic_Questions:** ¿Hay microgestión? ¿El equipo tiene autonomía? ¿Los supervisores delegan? ¿Las decisiones toman más tiempo del necesario? ¿La confianza es baja?
**Recommended_Actions:** Delegar autoridad al nivel más bajo posible; definir límites de decisión autónoma; capacitar al equipo; reducir puntos de control; confiar y empoderar; medir resultados no actividades.
**Severity_Level:** High
**Related_Patterns:** PRC-002, PRC-008, PRC-012, PRC-059

### PRC-014
**Pattern_Name:** Productividad Variable entre Turnos
**Category:** Productividad
**Description:** Existe una diferencia significativa en productividad entre diferentes turnos (mañana, tarde, noche), indicando falta de estandarización, fatiga o problemas de gestión de turnos.
**Observable_Symptoms:** El turno de la mañana produce más que el de la tarde; el turno nocturno tiene más errores; los resultados varían sistemáticamente por turno; no hay estándares comunes; cada turno opera de manera diferente.
**Early_Warning_Signals:** Diferencia de productividad entre turnos > 15%; variabilidad de calidad por turno; quejas sobre turnos específicos; rotación mayor en ciertos turnos; falta de comunicación entre turnos.
**Typical_Causes:** Falta de estandarización entre turnos; supervisión diferente; fatiga en turnos nocturnos; falta de comunicación en el cambio de turno; equipos desbalanceados.
**Business_Impact:** Capacidad no aprovechada uniformemente; calidad inconsistente; problemas en turnos de baja productividad afectan a los siguientes; conflictos entre turnos.
**Metrics_To_Check:** Productividad por turno; calidad por turno; variabilidad; rotación por turno; cumplimiento de estándar por turno.
**Diagnostic_Questions:** ¿La productividad varía por turno? ¿Por qué? ¿Los estándares se aplican en todos los turnos? ¿La comunicación entre turnos es efectiva? ¿Los supervisores tienen el mismo enfoque?
**Recommended_Actions:** Estandarizar procesos en todos los turnos; alinear criterios de supervisión; mejorar comunicación en cambios de turno; rotar personal entre turnos; implementar reuniones de solape; medir y balancear.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-012, PRC-036, PRC-082

### PRC-015
**Pattern_Name:** Curva de Aprendizaje Prolongada
**Category:** Productividad
**Description:** Los nuevos empleados tardan demasiado en alcanzar la productividad esperada, indicando que el onboarding, la capacitación o la estandarización son deficientes.
**Observable_Symptoms:** Nuevos empleados tardan meses en ser productivos; la calidad inicial es baja; se necesita supervisión intensiva; el período de aprendizaje es mayor al esperado; rotación alta durante el período de prueba.
**Early_Warning_Signals:** Tiempo para alcanzar productividad estándar > 3 meses; % de nuevos empleados que alcanzan estándar en período esperado < 50%; errores de nuevos empleados altos; rotación en período de prueba > 30%; sin programa de onboarding estructurado.
**Typical_Causes:** Falta de proceso de onboarding; capacitación no estructurada; ausencia de instructores o mentores; procesos no estandarizados (difíciles de aprender); materiales de entrenamiento inexistentes.
**Business_Impact:** Baja productividad temporal; costos de capacitación altos; rotación por frustración; supervisores distraídos entrenando; calidad inconsistente.
**Metrics_To_Check:** Tiempo para alcanzar productividad estándar; % que alcanza estándar en tiempo esperado; tasa de errores de nuevos; rotación en período de prueba; satisfacción del nuevo empleado.
**Diagnostic_Questions:** ¿Cuánto tardan los nuevos en ser productivos? ¿Hay proceso de onboarding estructurado? ¿Hay instructores? ¿Los procesos están estandarizados para facilitar el aprendizaje? ¿Los materiales de entrenamiento existen?
**Recommended_Actions:** Crear programa de onboarding estructurado; asignar mentores o instructores; estandarizar procesos para facilitar aprendizaje; crear materiales de entrenamiento (instrucciones, videos); establecer hitos de productividad.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-012, PRC-082, PRC-117

### PRC-016
**Pattern_Name:** Personal Calificado Realizando Tareas de Bajo Valor
**Category:** Productividad
**Description:** Personal con alta calificación dedica tiempo significativo a tareas administrativas, operativas o de bajo valor que podrían realizar personas con menor costo o automatizarse.
**Observable_Symptoms:** Ingenieros haciendo planillas; profesionales en tareas administrativas; personal calificado en logística o limpieza; quejas de "no es mi trabajo"; talento desperdiciado.
**Early_Warning_Signals:** % de tiempo de personal calificado en tareas de bajo valor > 20%; quejas sobre tareas no acordes al rol; falta de personal de soporte; rotación por frustración; costo de oportunidad del talento.
**Typical_Causes:** Estructura organizacional plana sin soporte administrativo; cultura de "todos hacen de todo"; falta de delegación; procesos mal diseñados; presupuesto limitado para soporte.
**Business_Impact:** Talento desperdiciado; productividad del personal calificado baja; desmotivación; rotación; costo de oportunidad alto (podrían estar generando más valor).
**Metrics_To_Check:** % de tiempo en tareas de alto vs bajo valor por rol; costo de oportunidad; satisfacción del personal; rotación; productividad del talento clave.
**Diagnostic_Questions:** ¿El personal calificado dedica tiempo a tareas de bajo valor? ¿Podrían delegarse o automatizarse? ¿Hay soporte administrativo suficiente? ¿El talento está siendo bien utilizado? ¿Hay quejas sobre tareas no acordes al rol?
**Recommended_Actions:** Analizar uso del tiempo del personal calificado; delegar tareas de bajo valor a personal de soporte; automatizar tareas administrativas; rediseñar roles; liberar tiempo para tareas de alto valor.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-059, PRC-071, PRC-082

### PRC-017
**Pattern_Name:** Sin Métricas de Productividad Individual
**Category:** Productividad
**Description:** La empresa no mide la productividad a nivel individual o por equipo, por lo que no puede identificar quiénes rinden por debajo del estándar ni reconocer a los de alto rendimiento.
**Observable_Symptoms:** No hay métricas de productividad por persona; el rendimiento se evalúa subjetivamente; no se identifica quién rinde más o menos; no hay metas individuales; las evaluaciones de desempeño no tienen base objetiva.
**Early_Warning_Signals:** Sin métricas de productividad individual; evaluación de desempeño sin datos; % de colaboradores con metas cuantitativas < 30%; diferencias de productividad no identificadas; reconicimiento sin base.
**Typical_Causes:** Cultura de "medir es controlar"; falta de sistemas de registro; desconocimiento de cómo medir; resistencia a la medición; gerencia no exige métricas.
**Business_Impact:** Imposibilidad de gestionar productividad; brechas de rendimiento no abordadas; talento no reconocido; mediocre no identificado; productividad no mejora.
**Metrics_To_Check:** (Deberían medirse) unidades por hora, tareas completadas, tiempo por tarea, calidad, cumplimiento de metas; variabilidad entre colaboradores.
**Diagnostic_Questions:** ¿Medimos productividad individual? ¿Sabemos quién rinde más y menos? ¿Las evaluaciones son objetivas? ¿Hay metas individuales? ¿La productividad mejora con el tiempo?
**Recommended_Actions:** Implementar métricas de productividad por rol; establecer metas individuales; dar feedback basado en datos; reconocer alto rendimiento; abordar bajo rendimiento con planes de mejora.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-013, PRC-082, PRC-117

### PRC-018
**Pattern_Name:** Sobrecarga de Trabajo en Personal Clave
**Category:** Productividad
**Description:** Ciertas personas clave están sobrecargadas mientras otras tienen capacidad ociosa, generando cuellos de botella humanos, estrés y riesgo de rotación de talento crítico.
**Observable_Symptoms:** Personas clave trabajando horas extras constantemente; otros tienen tiempo disponible; el trabajo se acumula en ciertas personas; la empresa depende de individuos específicos; esas personas están agotadas.
**Early_Warning_Signals:** % de horas extras de personal clave > 20%; diferencia de carga entre personal clave y otros > 2x; rotación de personal clave; estrés reportado; tareas se acumulan en ciertas personas.
**Typical_Causes:** Falta de planificación de carga; procesos no estandarizados (dependen de conocimiento tácito); falta de capacitación cruzada; personal clave no delega; cultura de "héroe".
**Business_Impact:** Riesgo de rotación de talento clave; cuellos de botella humanos; estrés y burnout; calidad afectada; falta de resiliencia si esa persona falta.
**Metrics_To_Check:** Carga de trabajo por persona; horas extras; % de capacidad utilizada por persona; rotación de personal clave; satisfacción laboral.
**Diagnostic_Questions:** ¿Hay personas sobrecargadas mientras otras tienen capacidad? ¿Quiénes son los cuellos de botella humanos? ¿Hay plan de sucesión? ¿El trabajo está distribuido equitativamente? ¿Hay capacitación cruzada?
**Recommended_Actions:** Distribuir carga de trabajo equitativamente; capacitar a otros en tareas clave; estandarizar procesos para reducir dependencia de personas; planificar capacidad; implementar capacitación cruzada.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-013, PRC-024, PRC-059, PRC-082

### PRC-019
**Pattern_Name:** Baja Productividad por Interrupciones Constantes
**Category:** Productividad
**Description:** El equipo enfrenta interrupciones constantes (llamadas, correos, consultas, urgencias) que fragmentan el tiempo de trabajo y reducen drásticamente la productividad.
**Observable_Symptoms:** El equipo reporta no poder concentrarse; constantes interrupciones durante el día; tareas largas tardan más de lo necesario; se trabaja en múltiples cosas a la vez; al final del día no se completó lo planificado.
**Early_Warning_Signals:** Tiempo de trabajo ininterrumpido < 60 minutos; número de interrupciones por hora > 3; % de tiempo en foco < 40%; multitarea constante; tareas planificadas vs completadas < 50%.
**Typical_Causes:** Cultura de "puertas abiertas" sin límites; falta de bloques de tiempo dedicados; urgencias mal gestionadas; equipos sin normas de comunicación; falta de herramientas asíncronas.
**Business_Impact:** Productividad baja; errores por multitarea; estrés; calidad del trabajo afectada; jornadas largas por trabajo no completado.
**Metrics_To_Check:** Tiempo de trabajo ininterrumpido; número de interrupciones por hora; % de tiempo en foco; tareas completadas vs planificadas; satisfacción con concentración.
**Diagnostic_Questions:** ¿El equipo puede concentrarse? ¿Cuántas interrupciones tienen por hora? ¿Hay bloques de trabajo ininterrumpido? ¿Las urgencias se gestionan adecuadamente? ¿Hay normas de comunicación?
**Recommended_Actions:** Establecer bloques de trabajo ininterrumpido; crear normas de comunicación (emergencias vs consultas); implementar "no molestar"; usar herramientas asíncronas; reducir urgencias con mejor planificación.
**Severity_Level:** High
**Related_Patterns:** PRC-009, PRC-012, PRC-013, PRC-059

### PRC-020
**Pattern_Name:** Productividad sin Incentivos
**Category:** Productividad
**Description:** No existe un sistema de incentivos vinculado a la productividad, por lo que no hay motivación económica para que el equipo mejore su rendimiento.
**Observable_Symptoms:** Todos cobran igual independientemente de su productividad; no hay bonos por rendimiento; los más productivos ganan lo mismo que los menos; no hay reconocimiento económico; el equipo no tiene incentivos para mejorar.
**Early_Warning_Signals:** % de compensación variable vinculada a productividad = 0%; sin bonos por rendimiento; productividad plana; equipo no motivado a mejorar; quejas sobre "da lo mismo".
**Typical_Causes:** Cultura de salario fijo; desconocimiento de diseño de incentivos; resistencia a medir productividad; miedo a conflictos; sindicato o regulación.
**Business_Impact:** Falta de motivación para mejorar; productividad estancada; talento no retenido; los mejores se van; mediocridad generalizada.
**Metrics_To_Check:** % de compensación variable; correlación incentivos-productividad; productividad con vs sin incentivos; rotación de talento; encuesta de motivación.
**Diagnostic_Questions:** ¿Hay incentivos por productividad? ¿Los más productivos ganan más? ¿El equipo está motivado a mejorar? ¿La compensación refleja el rendimiento? ¿Hay reconocimiento económico?
**Recommended_Actions:** Diseñar sistema de incentivos basado en productividad (bonos por metas, ganancias compartidas); medir impacto; ajustar según resultados; complementar con reconocimiento no económico.
**Severity_Level:** Medium
**Related_Patterns:** PRC-012, PRC-013, PRC-017, PRC-117

### PRC-021
**Pattern_Name:** Productividad Afectada por Clima Laboral
**Category:** Productividad
**Description:** El clima laboral negativo (conflictos, desmotivación, falta de reconocimiento) afecta la productividad del equipo, pero la empresa no lo aborda ni mide su impacto.
**Observable_Symptoms:** Conflictos entre miembros del equipo; desmotivación general; alta rotación; ausentismo; quejas sobre el ambiente de trabajo; baja colaboración; el equipo hace el mínimo.
**Early_Warning_Signals:** Rotación > 20% anual; ausentismo > 5%; clima laboral negativo en encuestas; conflictos frecuentes; productividad en declive sin causa operativa; quejas a RRHH.
**Typical_Causes:** Liderazgo deficiente; falta de reconocimiento; conflictos no resueltos; condiciones laborales inadecuadas; falta de comunicación; inequidad.
**Business_Impact:** Productividad baja; rotación alta; costos de reemplazo; pérdida de talento; clima tóxico afecta toda la organización; calidad del trabajo baja.
**Metrics_To_Check:** Rotación; ausentismo; encuesta de clima; satisfacción laboral; productividad vs clima; quejas y conflictos.
**Diagnostic_Questions:** ¿El clima laboral es positivo? ¿Afecta la productividad? ¿Hay conflictos no resueltos? ¿El equipo está motivado? ¿Se mide el clima laboral?
**Recommended_Actions:** Medir clima laboral regularmente; abordar causas de insatisfacción; mejorar liderazgo y comunicación; reconocer logros; resolver conflictos; crear ambiente de trabajo positivo.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-013, PRC-020, PRC-117

### PRC-022
**Pattern_Name:** Productividad sin Herramientas Adecuadas
**Category:** Productividad
**Description:** El equipo no cuenta con las herramientas, equipos o software adecuados para realizar su trabajo eficientemente, teniendo que usar métodos manuales o workarounds que reducen la productividad.
**Observable_Symptoms:** Procesos manuales que podrían automatizarse; software lento o inadecuado; herramientas en mal estado; el equipo pide mejores herramientas sin ser escuchado; workarounds constantes.
**Early_Warning_Signals:** % de tareas que podrían automatizarse pero son manuales > 30%; edad promedio de equipos > 5 años; quejas sobre herramientas inadecuadas; tiempo perdido en workarounds; inversión en herramientas < 2% de ingresos.
**Typical_Causes:** Falta de inversión; desconocimiento de herramientas disponibles; cultura de "con lo que hay"; priorización de otras inversiones; falta de innovación tecnológica.
**Business_Impact:** Productividad baja; equipo frustrado; calidad afectada; costos operativos más altos; competitividad reducida; talento se va por falta de herramientas.
**Metrics_To_Check:** % de tareas manuales automatizables; inversión en herramientas; quejas del equipo; productividad comparada con competidores; tiempo perdido por herramientas inadecuadas.
**Diagnostic_Questions:** ¿El equipo tiene las herramientas adecuadas? ¿Hay workarounds constantes? ¿Se invierte en herramientas? ¿Los procesos manuales podrían automatizarse? ¿El equipo está frustrado por las herramientas?
**Recommended_Actions:** Realizar auditoría de herramientas y necesidades; invertir en herramientas que mejoren productividad; involucrar al equipo en selección; capacitar en uso; medir ROI de herramientas.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-016, PRC-059, PRC-071, PRC-082

### PRC-023
**Pattern_Name:** Baja Productividad por Falta de Capacitación
**Category:** Productividad
**Description:** El equipo no recibe capacitación adecuada para realizar sus tareas eficientemente, resultando en métodos subóptimos, errores y baja productividad.
**Observable_Symptoms:** El equipo aprende "sobre la marcha"; no hay programa de capacitación; errores recurrentes por falta de conocimiento; métodos ineficientes; el equipo pide capacitación sin ser escuchado.
**Early_Warning_Signals:** % de empleados capacitados en su rol < 40%; horas de capacitación por empleado < 8 al año; errores por falta de conocimiento; métodos de trabajo subóptimos; quejas sobre falta de capacitación.
**Typical_Causes:** Falta de presupuesto de capacitación; cultura de "aprender haciendo"; desconocimiento del ROI de capacitación; tiempo dedicado a producción no a aprendizaje; falta de plan de capacitación.
**Business_Impact:** Productividad baja; errores costosos; métodos ineficientes perpetuados; desmotivación; rotación; incapacidad de mejorar procesos.
**Metrics_To_Check:** Horas de capacitación por empleado; % de empleados capacitados; impacto de capacitación en productividad; tasa de errores antes/después; satisfacción con capacitación.
**Diagnostic_Questions:** ¿El equipo recibe capacitación adecuada? ¿Hay plan de capacitación? ¿Los errores son por falta de conocimiento? ¿La capacitación mejora la productividad? ¿Se invierte en desarrollo del equipo?
**Recommended_Actions:** Desarrollar plan de capacitación por rol; asignar presupuesto; medir impacto en productividad; capacitar en métodos estandarizados; evaluar efectividad.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-012, PRC-015, PRC-036, PRC-082


## Cuellos de botella

### PRC-024
**Pattern_Name:** Cuello de Botella en Etapa de Proceso Clave
**Category:** Cuellos de botella
**Description:** Una etapa específica del proceso tiene menos capacidad que las demás, limitando el flujo total de la operación y generando acumulación de trabajo antes de ella y capacidad ociosa después.
**Observable_Symptoms:** Acumulación de WIP antes de una etapa específica; equipos parados después de esa etapa; la etapa siempre está atrasada; se trabaja horas extras en esa etapa; todos los pedidos pasan por ella.
**Early_Warning_Signals:** WIP acumulado antes de la etapa; % de utilización de la etapa = 100% mientras otras < 80%; tiempo de espera antes de la etapa > 30% del lead time; producción total limitada por esa etapa; la etapa opera al máximo todo el tiempo.
**Typical_Causes:** Capacidad de la etapa menor al resto; equipo obsoleto o lento; falta de personal en esa etapa; método de trabajo ineficiente; cuello de botella no identificado ni gestionado.
**Business_Impact:** Producción total limitada; lead times largos; inventario en proceso antes del cuello; capacidad ociosa después; incumplimiento de plazos; estrés en la etapa cuello.
**Metrics_To_Check:** % de utilización por etapa; WIP antes y después de cada etapa; tiempo de espera por etapa; producción total; tendencia del cuello de botella.
**Diagnostic_Questions:** ¿Dónde se acumula WIP? ¿Qué etapa tiene mayor % de utilización? ¿Dónde esperan los pedidos? ¿Qué etapa limita la producción total? ¿El cuello de botella está identificado y gestionado?
**Recommended_Actions:** Identificar el cuello de botella (etapa con mayor % de utilización); protegerlo de interrupciones; aumentar capacidad en esa etapa (mejora de método, horas extras, inversión); reducir pérdidas en el cuello; balancear después de mejorar.
**Severity_Level:** Critical
**Related_Patterns:** PRC-001, PRC-006, PRC-025, PRC-093, PRC-106, PRC-125

### PRC-025
**Pattern_Name:** Cuello de Botella Flotante (No Identificado)
**Category:** Cuellos de botella
**Description:** El cuello de botella cambia de ubicación según el producto, la demanda o el turno, y la empresa no lo identifica ni gestiona, generando ineficiencia general.
**Observable_Symptoms:** Diferentes etapas son cuello según el día o producto; el equipo no sabe dónde está el cuello hoy; se invierte en aumentar capacidad y el cuello se mueve; la producción es impredecible.
**Early_Warning_Signals:** Cuello de botella no estable; % de utilización varía entre etapas por día; inversiones en capacidad no resuelven el problema; el cuello se mueve con el mix de productos; falta de medición de cuellos.
**Typical_Causes:** Mix de productos variable; procesos no estandarizados; demanda fluctuante; falta de flexibilidad de equipos; mala planificación.
**Business_Impact:** Producción impredecible; inversiones en capacidad mal dirigidas; lead time variable; imposibilidad de optimizar; estrés operativo.
**Metrics_To_Check:** % de utilización por etapa (tendencia diaria/semanal); variabilidad del cuello; producción total; lead time; efectividad de inversiones.
**Diagnostic_Questions:** ¿El cuello de botella cambia frecuentemente? ¿Sabemos dónde está hoy? ¿Las inversiones en capacidad resuelven el problema? ¿El mix de productos afecta? ¿Gestionamos proactivamente los cuellos?
**Recommended_Actions:** Monitorear % de utilización por etapa diariamente; identificar patrón de cuellos por producto; flexibilizar recursos (personal multifuncional); estandarizar procesos; nivelar producción (heijunka).
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-026, PRC-093, PRC-105, PRC-106

### PRC-026
**Pattern_Name:** Cuello de Botella en Procesos Administrativos
**Category:** Cuellos de botella
**Description:** El cuello de botella no está en la producción sino en procesos administrativos (aprobaciones, compras, facturación), limitando el flujo general del negocio.
**Observable_Symptoms:** Pedidos listos para producir pero esperando aprobación; producción parada por falta de insumos (compras lentas); facturación demorada afecta cobranza; procesos administrativos más lentos que producción; la operación espera por administración.
**Early_Warning_Signals:** Tiempo de proceso administrativo > 2x tiempo de producción; pedidos detenidos en aprobación; compras no llegan a tiempo; facturación > 5 días post-entrega; % de lead time administrativo > 30%.
**Typical_Causes:** Procesos administrativos no optimizados; falta de automatización; aprobaciones excesivas; personal administrativo insuficiente; procesos manuales.
**Business_Impact:** Producción detenida por falta de insumos; clientes esperan por facturación; lead time total más largo; capital de trabajo inmovilizado; eficiencia general baja.
**Metrics_To_Check:** Tiempo de proceso administrativo; % de lead time total administrativo; pedidos detenidos en administrativo; tiempo de aprobación; tiempo de compras; tiempo de facturación.
**Diagnostic_Questions:** ¿Los procesos administrativos son más lentos que la producción? ¿La operación espera por administración? ¿Hay aprobaciones lentas? ¿Las compras llegan a tiempo? ¿La facturación es rápida?
**Recommended_Actions:** Mapear procesos administrativos; identificar cuellos de botella; automatizar y simplificar; eliminar aprobaciones innecesarias; integrar sistemas; balancear capacidad administrativa.
**Severity_Level:** High
**Related_Patterns:** PRC-002, PRC-003, PRC-024, PRC-059, PRC-071, PRC-105

### PRC-027
**Pattern_Name:** Capacidad Ociosa Aguas Abajo del Cuello
**Category:** Cuellos de botella
**Description:** Las etapas posteriores al cuello de botella tienen capacidad ociosa porque el cuello no les provee suficiente trabajo, desperdiciando recursos y aumentando costos.
**Observable_Symptoms:** Personas o equipos esperando trabajo después del cuello; la etapa posterior al cuello está infrautilizada; se paga por capacidad que no se usa; frustración por no poder producir más.
**Early_Warning_Signals:** % de utilización post-cuello < 60%; diferencia de utilización entre pre y post cuello > 30%; personas paradas esperando; costos fijos diluidos por baja producción; quejas de "no tenemos trabajo".
**Typical_Causes:** Cuello de botella no gestionado; desbalance de capacidad; falta de flujo continuo; lotes grandes; planificación no protege el cuello.
**Business_Impact:** Costos fijos por capacidad no utilizada; rentabilidad menor; equipos ociosos; inversiones en capacidad desaprovechadas; desperdicio de recursos.
**Metrics_To_Check:** % de utilización por etapa; capacidad ociosa post-cuello; costo de capacidad no utilizada; producción vs capacidad; rentabilidad por hora.
**Diagnostic_Questions:** ¿Hay capacidad ociosa después del cuello? ¿Cuánto cuesta esa capacidad no utilizada? ¿Podríamos usar mejor esa capacidad? ¿El cuello está protegido? ¿Podríamos balancear mejor?
**Recommended_Actions:** Maximizar throughput del cuello (protegerlo, eliminar pérdidas); reevaluar capacidad post-cuello (redistribuir); rediseñar flujo; balancear líneas; usar capacidad ociosa para otros productos.
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-025, PRC-093, PRC-106, PRC-107

### PRC-028
**Pattern_Name:** Cuello de Botella por Falta de Personal Calificado
**Category:** Cuellos de botella
**Description:** El cuello de botella es una persona o rol específico con habilidades que no tienen otros, limitando la capacidad total y generando dependencia crítica.
**Observable_Symptoms:** Ciertas tareas solo las puede hacer una persona; si esa persona falta, la operación se detiene; esa persona está sobrecargada; no hay plan de sucesión; capacitación cruzada inexistente.
**Early_Warning_Signals:** % de tareas que puede hacer una sola persona > 30%; personas con skills únicos sin respaldo; operación se detiene si falta alguien; % de personal con capacitación cruzada < 20%; quejas de "solo él sabe".
**Typical_Causes:** Falta de capacitación cruzada; conocimiento tácito no documentado; procesos no estandarizados; rotación no planificada; crecimiento sin desarrollar talento.
**Business_Impact:** Vulnerabilidad operativa; cuello de botella humano no escalable; estrés en la persona clave; rotación de esa persona es crítica; producción limitada por disponibilidad de esa persona.
**Metrics_To_Check:** % de tareas con una sola persona capacitada; % de personal con capacitación cruzada; % de procesos documentados; tiempo para reemplazar persona clave; impacto de ausencia de persona clave.
**Diagnostic_Questions:** ¿Hay tareas que solo una persona puede hacer? ¿Si esa persona falta, la operación se detiene? ¿Hay capacitación cruzada? ¿Hay plan de sucesión? ¿El conocimiento está documentado?
**Recommended_Actions:** Capacitar a múltiples personas en tareas críticas; documentar conocimiento táctico; estandarizar procesos; crear plan de sucesión; reducir dependencia de individuos.
**Severity_Level:** Critical
**Related_Patterns:** PRC-018, PRC-024, PRC-082, PRC-093

### PRC-029
**Pattern_Name:** Cuello de Botella por Mantenimiento No Planificado
**Category:** Cuellos de botella
**Description:** Paradas no planificadas por mantenimiento crean cuellos de botella temporales que interrumpen el flujo y reducen la capacidad disponible.
**Observable_Symptoms:** Equipos que se detienen inesperadamente; reparaciones de emergencia; mantenimiento reactivo; la producción se detiene por fallas; no hay programa de mantenimiento preventivo.
**Early_Warning_Signals:** % de mantenimiento reactivo > 70%; tiempo de parada no planificada > 5% del tiempo disponible; averías frecuentes en equipos críticos; sin plan de mantenimiento preventivo; costos de manten correctivo altos.
**Typical_Causes:** Falta de programa TPM; cultura de "arreglar cuando se rompe"; presupuesto insuficiente para preventivo; falta de repuestos críticos; personal de mantenimiento insuficiente.
**Business_Impact:** Producción interrumpida; plazos incumplidos; costos de reparación altos; vida útil de equipos reducida; productividad baja.
**Metrics_To_Check:** % de mantenimiento reactivo vs preventivo; MTBF (tiempo medio entre fallas); MTTR (tiempo medio de reparación); disponibilidad de equipos; costo de mantenimiento.
**Diagnostic_Questions:** ¿El mantenimiento es reactivo o preventivo? ¿Cuánto tiempo se pierde por paradas no planificadas? ¿Hay programa TPM? ¿Los equipos críticos tienen plan de mantenimiento? ¿Los repuestos están disponibles?
**Recommended_Actions:** Implementar TPM (Total Productive Maintenance); establecer programa de mantenimiento preventivo; crear plan de repuestos críticos; capacitar operadores en mantenimiento autónomo; medir disponibilidad.
**Severity_Level:** Critical
**Related_Patterns:** PRC-006, PRC-024, PRC-036, PRC-093, PRC-125

### PRC-030
**Pattern_Name:** Cuello de Botella en la Planificación de Compras
**Category:** Cuellos de botella
**Description:** El proceso de compras es un cuello de botella: los insumos no llegan a tiempo, las órdenes de compra se demoran y la producción espera por materiales.
**Observable_Symptoms:** Producción parada por falta de materiales; compras no procesadas a tiempo; órdenes de compra urgentes constantemente; proveedores no evaluados; stockouts frecuentes.
**Early_Warning_Signals:** % de órdenes de compra urgentes > 30%; stockouts por falta de compra a tiempo; tiempo de procesamiento de OC > 3 días; producción detenida por materiales; quejas de "compras no funciona".
**Typical_Causes:** Proceso de compras manual y lento; falta de automatización; pocos proveedores; plazos de entrega de proveedores no gestionados; mala planificación de necesidades.
**Business_Impact:** Producción detenida; ventas perdidas por falta de producto; lead times largos; costos de compras urgentes; relaciones tensas con proveedores.
**Metrics_To_Check:** Tiempo de procesamiento de OC; % de OC urgentes; stockouts; días de inventario; cumplimiento de proveedores.
**Diagnostic_Questions:** ¿Las compras son un cuello de botella? ¿La producción espera por materiales? ¿El proceso de compras es eficiente? ¿Hay automatización? ¿Los proveedores cumplen plazos?
**Recommended_Actions:** Automatizar proceso de compras; establecer parámetros de reaprovisionamiento; evaluar y gestionar proveedores; crear stocks de seguridad para críticos; planificar necesidades con anticipación.
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-026, PRC-059, PRC-071, PRC-105

### PRC-031
**Pattern_Name:** Múltiples Cuellos de Botella por Falta de Enfoque
**Category:** Cuellos de botella
**Description:** La empresa identifica múltiples "cuellos de botella" e intenta mejorar todos a la vez, diluyendo recursos y sin lograr avances significativos en ninguno.
**Observable_Symptoms:** Se intenta mejorar muchas áreas simultáneamente; recursos dispersos; ninguna mejora se completa; el equipo está abrumado; los cuellos persisten.
**Early_Warning_Signals:** Número de iniciativas de mejora simultáneas > 5; % de iniciativas completadas < 30%; recursos de mejora diluidos; frustración del equipo; cuellos de botella sin resolver.
**Typical_Causes:** Falta de priorización basada en teoría de restricciones; cultura de "todo es prioridad"; falta de enfoque; equipos sin metodología; presión por mejorar todo.
**Business_Impact:** Recursos desperdiciados; ninguna mejora significativa; frustración; tiempo perdido; cuellos persisten; cultura de "mejora no funciona".
**Metrics_To_Check:** Número de iniciativas activas; % completadas; impacto en throughput; recursos dedicados por iniciativa; tiempo promedio de resolución de cuellos.
**Diagnostic_Questions:** ¿Estamos intentando mejorar demasiadas cosas a la vez? ¿Hay un cuello de botella claro? ¿Las mejoras se completan? ¿Los recursos están enfocados? ¿Hay una restricción clara?
**Recommended_Actions:** Aplicar teoría de restricciones (TOC): identificar la restricción, explotarla, subordinar, elevar, repetir; priorizar una restricción a la vez; enfocar recursos en la restricción actual; celebrar avances.
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-025, PRC-106, PRC-117, PRC-125

### PRC-032
**Pattern_Name:** Cuello de Botella en Sistema de Información
**Category:** Cuellos de botella
**Description:** El sistema de información (ERP, software de gestión) es un cuello de botella: lento, con poca capacidad, mal configurado o con procesos manuales que lo rodean.
**Observable_Symptoms:** El sistema es lento; la información tarda en procesarse; el equipo debe usar workarounds manuales; reportes tardan horas; el sistema se cae frecuentemente.
**Early_Warning_Signals:** Tiempo de respuesta del sistema > 5 segundos; caídas semanales; % de procesos manuales que rodean al sistema > 30%; quejas sobre lentitud; pedidos atrasados por sistema.
**Typical_Causes:** Sistema obsoleto; capacidad insuficiente; mala configuración; falta de mantenimiento; implementación incompleta; usuarios no capacitados.
**Business_Impact:** Operación lenta; errores por workarounds manuales; información desactualizada; decisiones retrasadas; productividad baja; costos de múltiples sistemas.
**Metrics_To_Check:** Tiempo de respuesta del sistema; disponibilidad del sistema; % de procesos automatizados vs manuales; tiempo de generación de reportes; quejas de usuarios.
**Diagnostic_Questions:** ¿El sistema de información es un cuello de botella? ¿Es rápido y confiable? ¿Los procesos son manuales por culpa del sistema? ¿La información está disponible cuando se necesita? ¿El sistema soporta la operación?
**Recommended_Actions:** Evaluar capacidad y rendimiento del sistema; optimizar consultas y procesos; actualizar hardware/software; capacitar usuarios; migrar a sistema más moderno si es necesario.
**Severity_Level:** High
**Related_Patterns:** PRC-022, PRC-024, PRC-026, PRC-059, PRC-071

### PRC-033
**Pattern_Name:** Cuello de Botella en Proceso de Toma de Decisiones
**Category:** Cuellos de botella
**Description:** Las decisiones operativas se centralizan en una persona o comité que no tiene capacidad para resolver rápido, retrasando toda la operación.
**Observable_Symptoms:** Todo se decide en una persona; esa persona es un cuello de botella; las decisiones se acumulan; la operación espera por decisiones simples; la persona clave está sobrecargada.
**Early_Warning_Signals:** Tiempo de decisión > 24h para decisiones operativas; % de decisiones que podría tomar otro nivel > 50%; acumulación de decisiones sin resolver; quejas de "todo depende de fulano"; rotación de la persona clave es crítica.
**Typical_Causes:** Cultura centralizada; falta de delegación; desconfianza; organigrama jerárquico; microgestión; personal clave no delega.
**Business_Impact:** Operación lenta; decisiones retrasadas; oportunidades perdidas; persona clave agotada; equipo desempoderado; falta de agilidad.
**Metrics_To_Check:** Tiempo de decisión; % de decisiones delegables; % de decisiones delegadas; satisfacción con velocidad de decisión; productividad de la persona clave.
**Diagnostic_Questions:** ¿Las decisiones operativas se centralizan? ¿Quién es el cuello de botella en decisiones? ¿Podrían delegarse más decisiones? ¿El equipo tiene autonomía? ¿La velocidad de decisión afecta la operación?
**Recommended_Actions:** Delegar decisiones al nivel más bajo posible; definir límites de autoridad; capacitar al equipo en toma de decisiones; confiar y empoderar; medir velocidad de decisión.
**Severity_Level:** High
**Related_Patterns:** PRC-002, PRC-013, PRC-018, PRC-024, PRC-028

### PRC-034
**Pattern_Name:** Cuello de Botella por Especificaciones del Cliente
**Category:** Cuellos de botella
**Description:** Los requisitos especiales o cambios constantes de especificaciones de ciertos clientes generan cuellos de botella, ya que requieren procesos especiales que ralentizan toda la operación.
**Observable_Symptoms:** Ciertos pedidos requieren procesos especiales que toman más tiempo; la operación se detiene para atender pedidos especiales; clientes con especificaciones complejas afectan a otros; el equipo se queja de "pedidos raros".
**Early_Warning_Signals:** % de pedidos con especificaciones especiales > 20%; tiempo de proceso de pedidos especiales > 2x; lead time de pedidos especiales afecta promedio general; conflictos entre pedidos estándar y especiales; pedidos especiales causan desvíos.
**Typical_Causes:** Falta de segmentación de procesos (estándar vs especial); clientes no educados; ventas acepta cualquier requerimiento; producción no preparada para variabilidad; falta de política de pedidos especiales.
**Business_Impact:** Lead time general alargado; eficiencia reducida; costos más altos; clientes estándar afectados; complejidad operativa; errores por falta de estandarización.
**Metrics_To_Check:** % de pedidos especiales; tiempo de proceso especial vs estándar; impacto en lead time general; margen de pedidos especiales vs estándar; satisfacción de clientes estándar.
**Diagnostic_Questions:** ¿Los pedidos especiales generan cuellos de botella? ¿Hay procesos diferenciados? ¿Los clientes están educados en estándares? ¿Ventas acepta cualquier especificación? ¿El margen justifica la complejidad?
**Recommended_Actions:** Segmentar pedidos en estándar y especiales; crear procesos diferenciados; educar a clientes en opciones estándar; cobrar premium por especiales; limitar % de pedidos especiales.
**Severity_Level:** Medium
**Related_Patterns:** PRC-024, PRC-034, PRC-082, PRC-105, PRC-106

### PRC-035
**Pattern_Name:** Cuello de Botella por Flujo de Información Lento
**Category:** Cuellos de botella
**Description:** La información (órdenes, especificaciones, aprobaciones, planos) viaja más lento que los materiales, generando cuellos de botella donde la producción espera por datos o instrucciones.
**Observable_Symptoms:** Producción detenida esperando información; "estamos esperando que nos digan"; aprobaciones tardan más que la producción; órdenes incompletas al llegar a piso; especificaciones que llegan cuando ya se empezó; información desactualizada.
**Early_Warning_Signals:** % de tiempo de producción esperando información > 10%; tiempo de aprobación > tiempo de producción; % de órdenes con información incompleta al inicio; frecuencia de "esperando datos"; lead time de información > lead time de materiales.
**Typical_Causes:** Procesos administrativos lentos; sistemas de información deficientes; comunicación manual entre áreas; aprobaciones secuenciales lentas; falta de integración ventas-producción; datos ingresados tarde.
**Business_Impact:** Producción detenida por espera de información; lead time más largo que el necesario; capacidad desperdiciada; urgencias de última hora; errores por información apresurada; clientes afectados.
**Metrics_To_Check:** % de tiempo de producción esperando información; tiempo de flujo de información vs materiales; % de órdenes con información completa al inicio; cuello de botella informativo; satisfacción del equipo con flujo de información.
**Diagnostic_Questions:** ¿La producción espera por información? ¿La información llega antes que los materiales? ¿Las aprobaciones son oportunas? ¿Hay integración entre áreas? ¿El flujo de información es más lento que el de materiales?
**Recommended_Actions:** Acelerar flujo de información (digitalizar, automatizar); integrar sistemas; sincronizar flujo de información con flujo de materiales; reducir aprobaciones innecesarias; establecer SLA de información.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-024, PRC-026, PRC-050, PRC-057, PRC-068, PRC-103


## Calidad

### PRC-036
**Pattern_Name:** Tasa de Defectos Alta y Sin Mejora
**Category:** Calidad
**Description:** El porcentaje de productos o servicios defectuosos es alto y no mejora con el tiempo, indicando problemas de proceso, materiales o capacitación que no se abordan.
**Observable_Symptoms:** Defectos recurrentes; clientes devuelven productos; retrabajo constante; el equipo acepta defectos como "normales"; la tasa de defectos no se reduce.
**Early_Warning_Signals:** Tasa de defectos > 5% (o > benchmark); tendencia de defectos plana; % de retrabajo sobre producción > 5%; quejas de clientes por calidad; costo de calidad > 10% de ventas.
**Typical_Causes:** Procesos no estandarizados; falta de control de calidad en proceso; materiales deficientes; equipo no capacitado; herramientas inadecuadas; cultura de "aceptar defectos".
**Business_Impact:** Clientes insatisfechos; retrabajo y desperdicio; costos de calidad altos; reputación dañada; pérdida de ventas; competitividad reducida.
**Metrics_To_Check:** Tasa de defectos; % de retrabajo; costo de calidad (prevención + evaluación + fallas); quejas de clientes; tendencia de defectos.
**Diagnostic_Questions:** ¿Cuál es la tasa de defectos? ¿Está mejorando? ¿Cuánto cuestan los defectos? ¿Hay control de calidad en proceso? ¿Las causas raíz se investigan y resuelven?
**Recommended_Actions:** Medir tasa de defectos sistemáticamente; implementar control de calidad en proceso (no solo al final); investigar causas raíz; estandarizar procesos; capacitar al equipo; implementar Poka-Yoke (a prueba de errores).
**Severity_Level:** Critical
**Related_Patterns:** PRC-011, PRC-037, PRC-048, PRC-059, PRC-082, PRC-125

### PRC-037
**Pattern_Name:** Control de Calidad Solo al Final del Proceso
**Category:** Calidad
**Description:** La inspección de calidad se realiza solo al final del proceso, detectando defectos tarde, cuando ya se agregó todo el valor y el retrabajo es más costoso.
**Observable_Symptoms:** Los defectos se detectan al final, después de todo el trabajo; retrabajo costoso; no hay controles intermedios; productos defectuosos avanzan por todo el proceso; desperdicio de materiales y tiempo.
**Early_Warning_Signals:** % de inspección al final > 80% del total de puntos de control; costo de retrabajo alto; defectos detectados en etapas tardías; tiempo entre defecto y detección largo; producto con defecto recorre todo el proceso.
**Typical_Causes:** Falta de calidad en proceso; cultura de "inspeccionar al final"; falta de Poka-Yoke; procesos sin controles intermedios; desconocimiento de calidad en la fuente.
**Business_Impact:** Costos de retrabajo altos; desperdicio de materiales y tiempo; lead times largos por retrabajo al final; inspección final cuellode botella; calidad no se construye en el proceso.
**Metrics_To_Check:** Puntos de control en proceso vs final; costo de retrabajo por etapa; tiempo entre defecto y detección; % de defectos detectados en cada etapa.
**Diagnostic_Questions:** ¿La inspección es solo al final o en proceso? ¿Los defectos se detectan temprano? ¿Hay controles en cada etapa? ¿Se construye calidad en el proceso? ¿El retrabajo es costoso?
**Recommended_Actions:** Implementar controles de calidad en procesos; calidad en la fuente (cada operario inspecciona); Poka-Yoke; detener proceso ante defecto (Andon); capacitar en auto-inspección.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-048, PRC-049, PRC-059, PRC-082

### PRC-038
**Pattern_Name:** Defectos por Falta de Especificaciones Claras
**Category:** Calidad
**Description:** Los defectos ocurren porque las especificaciones del producto/servicio no están claramente definidas, documentadas o comunicadas, dejando espacio para interpretación.
**Observable_Symptoms:** Cada operador interpreta la calidad de manera diferente; reclamos por "no es lo que pedí"; especificaciones verbales no documentadas; cambios de último minuto mal comunicados; disputas sobre lo que "debería ser".
**Early_Warning_Signals:** % de procesos con especificaciones documentadas < 40%; reclamos por "malinterpretación"; especificaciones verbales; cambios sin registro; variabilidad entre operadores por falta de estándar.
**Typical_Causes:** Falta de documentación; especificaciones no detalladas; comunicación informal; procesos artesanales no estandarizados; cultura de "se entiende".
**Business_Impact:** Defectos por interpretación; clientes insatisfechos; retrabajo; discusiones sobre especificaciones; calidad inconsistente; dificultad para escalar.
**Metrics_To_Check:** % de procesos con especificaciones documentadas; reclamos por especificaciones; variabilidad entre operadores; % de defectos por falta de especificación.
**Diagnostic_Questions:** ¿Las especificaciones están documentadas? ¿Son claras? ¿Todos las entienden igual? ¿Hay cambios sin registrar? ¿Los reclamos son por falta de claridad?
**Recommended_Actions:** Documentar especificaciones detalladas; usar estándares visuales (fotos, muestras); comunicar cambios formalmente; capacitar en especificaciones; verificar entendimiento.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-036, PRC-082, PRC-083

### PRC-039
**Pattern_Name:** Alta Variabilidad de Calidad entre Turnos u Operadores
**Category:** Calidad
**Description:** La calidad varía significativamente según quién o cuándo se realiza el trabajo, indicando falta de estandarización y procesos que dependen del individuo.
**Observable_Symptoms:** Calidad inconsistente; ciertos turnos producen más defectos; algunos operadores tienen mejor calidad que otros; el cliente nota diferencias; no hay estándar común.
**Early_Warning_Signals:** Desviación estándar de calidad entre operadores > 10%; diferencia de defectos entre turnos > 2x; reclamos de calidad asociados a turnos/personas; % de operadores fuera de especificación; capacitación inconsistente.
**Typical_Causes:** Falta de estandarización; capacitación desigual; criterios de calidad subjetivos; supervisión diferente entre turnos; métodos de trabajo no documentados.
**Business_Impact:** Clientes reciben calidad inconsistente; retrabajo variable; dificultad para identificar causas; imposibilidad de mejora sin estándar; reputación de calidad impredecible.
**Metrics_To_Check:** Variabilidad de calidad entre operadores/turnos; % de operadores dentro de especificación; tendencia de variabilidad; reclamos por inconsistencia.
**Diagnostic_Questions:** ¿La calidad varía por turno u operador? ¿Hay un estándar común? ¿La capacitación es consistente? ¿Los criterios de calidad están claros? ¿La variabilidad se mide?
**Recommended_Actions:** Estandarizar procesos y criterios; capacitar a todos en el mismo estándar; implementar instrucciones de trabajo visuales; auditar consistencia; medir y reducir variabilidad.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-014, PRC-036, PRC-082

### PRC-040
**Pattern_Name:** Costo de Calidad No Medido
**Category:** Calidad
**Description:** La empresa no calcula el costo de la calidad (prevención, evaluación, fallas internas y externas), por lo que no sabe cuánto le cuestan los defectos ni puede justificar inversiones en mejora.
**Observable_Symptoms:** No se sabe cuánto cuestan los defectos; se invierte poco en prevención; los costos ocultos de mala calidad no se conocen; las decisiones de calidad se toman sin datos económicos; el verdadero impacto de los defectos se ignora.
**Early_Warning_Signals:** Costo de calidad no calculado; % de ventas destinado a calidad desconocido; inversión en prevención < 1% de ventas; fallas externas (clientes) no cuantificadas; decisiones de calidad sin base económica.
**Typical_Causes:** Desconocimiento de la métrica; falta de sistema de costos; cultura de "calidad es responsabilidad de todos y de nadie"; falta de asignación de costos de calidad; contabilidad no separa costos de calidad.
**Business_Impact:** Subinversión en prevención; costos ocultos de mala calidad no controlados; imposibilidad de priorizar inversiones en calidad; calidad no mejora por falta de justificación económica.
**Metrics_To_Check:** (Deberían medirse) costo total de calidad como % de ventas; costo de prevención; costo de evaluación; costo de fallas internas; costo de fallas externas; tendencia.
**Diagnostic_Questions:** ¿Sabemos cuánto nos cuesta la mala calidad? ¿Calculamos el costo de calidad? ¿Invertimos en prevención? ¿Conocemos el costo de fallas externas (clientes insatisfechos, devoluciones)? ¿Justificamos inversiones en calidad con datos?
**Recommended_Actions:** Implementar cálculo de costo de calidad; separar costos de prevención, evaluación, fallas internas y externas; reportar trimestralmente; usar datos para justificar inversiones; establecer metas de reducción.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-048, PRC-049, PRC-059, PRC-117

### PRC-041
**Pattern_Name:** Proveedores con Calidad Inconsistente
**Category:** Calidad
**Description:** Los materiales o insumos de proveedores tienen calidad variable, generando defectos en la producción que la empresa termina asumiendo en lugar de exigir calidad al proveedor.
**Observable_Symptoms:** Defectos causados por materiales recibidos; inspección de recepción encuentra no conformidades; proveedores no evaluados; mismos defectos se repiten con mismos proveedores; no hay consecuencia para proveedores de baja calidad.
**Early_Warning_Signals:** % de lotes de proveedores rechazados > 5%; defectos atribuibles a materiales; sin evaluación de proveedores; proveedores no certificados; quejas a proveedores sin seguimiento.
**Typical_Causes:** Falta de evaluación de proveedores; compras por precio no por calidad; pocos proveedores; especificaciones no comunicadas; falta de consecuencias.
**Business_Impact:** Defectos en producción; retrabajo; clientes afectados; costos de calidad altos; relación tensa con proveedores; producción detenida por materiales defectuosos.
**Metrics_To_Check:** % de rechazo por proveedor; defectos atribuibles a materiales; scorecard de proveedores; certificaciones de proveedores; costo de defectos por proveedor.
**Diagnostic_Questions:** ¿La calidad de los proveedores es consistente? ¿Los defectos son por materiales? ¿Evaluamos proveedores? ¿Hay consecuencias por baja calidad? ¿Comunicamos especificaciones claras?
**Recommended_Actions:** Evaluar y clasificar proveedores por calidad; establecer especificaciones claras; implementar inspección de recepción; crear scorecard de proveedores; desarrollar proveedores o reemplazar los de baja calidad.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-038, PRC-042, PRC-059

### PRC-042
**Pattern_Name:** Cultura de "Calidad es del Departamento de Calidad"
**Category:** Calidad
**Description:** El equipo de producción y operaciones no se siente responsable de la calidad; creen que "calidad es cosa del departamento de calidad", generando una desconexión peligrosa.
**Observable_Symptoms:** Operadores producen sin preocuparse por calidad; "que lo revise calidad"; el departamento de calidad es visto como policía; los defectos se justifican; no hay calidad en la fuente.
**Early_Warning_Signals:** % de operadores que se consideran responsables de calidad < 30%; calidad vista como "departamento separado"; operadores no inspeccionan su trabajo; defectos encontrados solo por calidad; quejas de "para eso está calidad".
**Typical_Causes**: Estructura organizacional separada; cultura de inspección no de prevención; liderazgo no promueve calidad de todos; falta de capacitación; incentivos solo por cantidad.
**Business_Impact:** Calidad deficiente; costos de inspección altos; defectos no prevenidos; cultura de "ellos vs nosotros"; calidad no mejora; clientes afectados.
**Metrics_To_Check:** % de empleados que se consideran responsables de calidad; defectos encontrados por producción vs calidad; costo de calidad; clima de calidad; tendencia de defectos.
**Diagnostic_Questions:** ¿Todos se sienten responsables de la calidad? ¿O solo el departamento de calidad? ¿Los operadores inspeccionan su trabajo? ¿Hay cultura de calidad en la fuente? ¿La calidad es prioridad de todos?
**Recommended_Actions:** Capacitar a toda la organización en calidad como responsabilidad de todos; eliminar "policía de calidad"; implementar calidad en la fuente; medir y reconocer calidad; alinear incentivos con calidad.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-037, PRC-061, PRC-082, PRC-117

### PRC-043
**Pattern_Name:** Sin Sistema de Gestión de Calidad
**Category:** Calidad
**Description:** La empresa no tiene un sistema de gestión de calidad formal (ISO 9001 o similar) ni procesos documentados de control, aseguramiento y mejora de la calidad.
**Observable_Symptoms:** No hay procedimientos de calidad documentados; no hay registros de calidad; las acciones correctivas no se documentan; no hay auditorías de calidad; la calidad se gestiona informalmente.
**Early_Warning_Signals:** Sin certificación de calidad; sin procedimientos documentados; sin registros de calidad; sin acciones correctivas documentadas; sin auditorías internas; calidad depende de personas no de sistemas.
**Typical_Causes:** Desconocimiento de normas; costo de implementación; cultura de "es demasiado para nosotros"; falta de recursos; empresa pequeña que cree no necesitarlo.
**Business_Impact:** Calidad inconsistente; imposibilidad de certificarse; dificultad para vender a ciertos clientes; falta de mejora sistemática; conocimiento no institucionalizado; riesgo de problemas de calidad recurrentes.
**Metrics_To_Check:** Sistema de calidad implementado; % de procesos documentados; % de acciones correctivas registradas; frecuencia de auditorías; tendencia de calidad.
**Diagnostic_Questions:** ¿Tenemos un sistema de gestión de calidad? ¿Los procesos de calidad están documentados? ¿Hay registro de acciones correctivas? ¿Hay auditorías de calidad? ¿La calidad está institucionalizada?
**Recommended_Actions:** Implementar sistema de gestión de calidad gradual (ISO 9001 o similar); documentar procesos críticos; establecer registros de calidad; implementar acciones correctivas; realizar auditorías periódicas.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-040, PRC-082, PRC-117, PRC-125

### PRC-044
**Pattern_Name:** Calidad No es Criterio en Evaluación de Desempeño
**Category:** Calidad
**Description:** La calidad no es un factor en la evaluación de desempeño del equipo; solo se mide cantidad, incentivando producir rápido sin importar la calidad.
**Observable_Symptoms:** Bonos solo por cantidad; el equipo prioriza velocidad sobre calidad; no hay consecuencias por defectos; calidad no se menciona en evaluaciones; los más rápidos son reconocidos aunque tengan defectos.
**Early_Warning_Signals:** % de compensación variable vinculada a calidad = 0%; evaluación sin criterios de calidad; incentivos solo por volumen; correlación velocidad-defectos; equipo no prioriza calidad.
**Typical_Causes:** Cultura de "cantidad es lo que importa"; facilidad de medir cantidad sobre calidad; desconocimiento de cómo medir calidad en evaluación; presión por producir; falta de métricas de calidad individual.
**Business_Impact:** Producción rápida pero defectuosa; retrabajo; clientes insatisfechos; costos de calidad altos; cultura de cantidad sobre calidad; sostenibilidad comprometida.
**Metrics_To_Check:** % de evaluación basada en calidad; % de compensación variable por calidad; tendencia de calidad vs incentivos; correlación velocidad-calidad; quejas de clientes.
**Diagnostic_Questions:** ¿La calidad es parte de la evaluación de desempeño? ¿Los incentivos consideran calidad? ¿El equipo prioriza cantidad sobre calidad? ¿Hay consecuencias por defectos? ¿La calidad se reconoce?
**Recommended_Actions:** Incorporar calidad en evaluación de desempeño; vincular compensación a calidad; balancear métricas de cantidad y calidad; reconocer calidad; capacitar en calidad como prioridad.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-037, PRC-040, PRC-042, PRC-082

### PRC-045
**Pattern_Name:** Alta Tasa de Devoluciones de Clientes
**Category:** Calidad
**Description:** La tasa de devoluciones de productos por parte de clientes es alta, indicando problemas de calidad que afectan directamente la satisfacción y los ingresos.
**Observable_Symptoms:** Clientes devuelven productos frecuentemente; quejas por mala calidad; costos logísticos de devolución; productos devueltos que no pueden revenderse; la empresa normaliza devoluciones.
**Early_Warning_Signals:** Tasa de devoluciones > 5% de ventas; tendencia de devoluciones creciente; costos de devolución > 2% de ventas; % de productos devueltos no reutilizables; quejas recurrentes por calidad.
**Typical_Causes:** Defectos de fabricación; empaque inadecuado; producto no cumple expectativas; especificaciones no claras; control de calidad deficiente; logística de entrega dañina.
**Business_Impact:** Pérdida de ingresos por devoluciones; costos logísticos; insatisfacción del cliente; daño reputacional; cliente no recompra; LTV bajo.
**Metrics_To_Check:** Tasa de devoluciones; costo de devoluciones; % de devoluciones por causa; tendencia; satisfacción post-devolución.
**Diagnostic_Questions:** ¿Cuál es la tasa de devoluciones? ¿Está creciendo? ¿Cuáles son las causas principales? ¿Los defectos se corrigen? ¿Las devoluciones se analizan para mejora?
**Recommended_Actions:** Analizar causas de devoluciones; mejorar control de calidad; mejorar empaque; alinear expectativas del cliente; implementar análisis de causa raíz; reducir devoluciones sistemáticamente.
**Severity_Level:** Critical
**Related_Patterns:** PRC-036, PRC-048, PRC-049, PRC-054, PRC-059

### PRC-046
**Pattern_Name:** Quejas de Clientes por Calidad No Investigadas
**Category:** Calidad
**Description:** Las quejas de clientes por calidad se reciben pero no se investigan sistemáticamente para identificar causas raíz y prevenir recurrencia, por lo que los mismos problemas se repiten.
**Observable_Symptoms:** Mismas quejas recurrentes; no hay investigación de causas; se resuelve el caso individual pero no el problema de fondo; clientes se quejan de lo mismo que otros; el equipo sabe qué quejas van a llegar.
**Early_Warning_Signals:** % de quejas con investigación de causa raíz < 30%; quejas recurrentes mismo tipo > 40%; tiempo sin solución definitiva de quejas recurrentes; % de quejas que se repiten; equipo puede predecir quejas.
**Typical_Causes:** Falta de proceso de investigación; cultura de "apagar incendios"; recursos limitados; falta de metodología (5 porqués, Ishikawa); no se asigna responsabilidad.
**Business_Impact:** Mismos defectos se repiten; clientes insatisfechos recurrentemente; costos de retrabajo y devoluciones; reputación dañada; churn por calidad.
**Metrics_To_Check:** % de quejas con investigación de causa raíz; % de quejas recurrentes; tiempo de resolución definitiva; tendencia de quejas por tipo; satisfacción post-resolución.
**Diagnostic_Questions:** ¿Investigamos las quejas de calidad? ¿Identificamos causas raíz? ¿Las mismas quejas se repiten? ¿Resolvemos definitivamente? ¿Hay mejora en los tipos de queja?
**Recommended_Actions:** Implementar proceso de investigación de quejas (5 porqués, Ishikawa); registrar causas raíz; implementar acciones correctivas; verificar efectividad; medir recurrencia.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-045, PRC-048, PRC-049, PRC-117

### PRC-047
**Pattern_Name:** Sin Métricas de Calidad en Tiempo Real
**Category:** Calidad
**Description:** Las métricas de calidad se reportan con retraso (días o semanas después), imposibilitando la detección y corrección temprana de desviaciones en el proceso.
**Observable_Symptoms:** Los datos de calidad llegan cuando ya se produjeron muchos defectos; no hay monitoreo en tiempo real; la corrección es tardía; se descubre el problema cuando ya es grande; el proceso sigue produciendo defectos mientras se esperan los datos.
**Early_Warning_Signals:** Frecuencia de reporte de calidad > 1 día; % de defectos detectados en tiempo real < 20%; tiempo entre defecto y detección > 1 hora; lotes completos defectuosos antes de detectar; reacción tardía.
**Typical_Causes:** Inspección al final del proceso; datos ingresados manualmente; falta de sensores o sistemas de monitoreo; cultura de "reportar después"; sistemas no integrados.
**Business_Impact:** Defectos se producen en lotes completos antes de detectar; costo de retrabajo alto; desperdicio de materiales; cliente recibe productos defectuosos; capacidad desperdiciada.
**Metrics_To_Check:** Frecuencia de reporte de calidad; tiempo entre defecto y detección; % de defectos detectados en tiempo real; lotes defectuosos completos; costo de detección tardía.
**Diagnostic_Questions:** ¿Los datos de calidad están disponibles en tiempo real? ¿Detectamos defectos inmediatamente? ¿Cuánto tiempo pasa entre el defecto y la detección? ¿Producimos lotes defectuosos antes de enterarnos? ¿Hay monitoreo en línea?
**Recommended_Actions:** Implementar monitoreo de calidad en tiempo real; sensores y sistemas automáticos; control estadístico de procesos (SPC) en línea; alarmas de desviación; inspección en proceso.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-037, PRC-071, PRC-082, PRC-125


## Retrabajo

### PRC-048
**Pattern_Name:** Retrabajo Crónico y Aceptado como Normal
**Category:** Retrabajo
**Description:** El retrabajo (rehacer trabajo mal hecho) es una práctica habitual y aceptada como "parte del negocio", sin que se implementen acciones para eliminarlo en la fuente.
**Observable_Symptoms:** Se retrabaja constantemente; el equipo considera el retrabajo normal; no se investigan causas; se presupuesta retrabajo; el retrabajo no se mide como pérdida.
**Early_Warning_Signals:** % de retrabajo sobre producción total > 10%; retrabajo no medido como costo; equipo acepta retrabajo como normal; no hay acciones para eliminar causas; % de capacidad dedicada a retrabajo > 15%.
**Typical_Causes:** Defectos no investigados; procesos no estandarizados; especificaciones poco claras; materiales deficientes; falta de calidad en la fuente; cultura de "arreglarlo después".
**Business_Impact:** Capacidad desperdiciada en retrabajo; costos dobles (producir + rehacer); lead times más largos; clientes afectados por demoras; moral del equipo baja.
**Metrics_To_Check:** % de retrabajo sobre producción; costo de retrabajo; capacidad dedicada a retrabajo; tendencia de retrabajo; causas principales de retrabajo.
**Diagnostic_Questions:** ¿El retrabajo se considera normal? ¿Se mide el costo del retrabajo? ¿Se investigan las causas? ¿Se implementan acciones para eliminarlo? ¿Cuánta capacidad se pierde en retrabajo?
**Recommended_Actions:** Medir retrabajo sistemáticamente; calcular costo; investigar causas raíz; implementar calidad en la fuente; estandarizar procesos; establecer meta de cero retrabajo; capacitar al equipo.
**Severity_Level:** Critical
**Related_Patterns:** PRC-011, PRC-036, PRC-049, PRC-050, PRC-058, PRC-082

### PRC-049
**Pattern_Name:** Retrabajo por Falta de Instrucciones de Trabajo Claras
**Category:** Retrabajo
**Description:** El retrabajo ocurre porque las instrucciones de trabajo no son claras, están desactualizadas o no existen, llevando a que cada operador interprete cómo hacer el trabajo.
**Observable_Symptoms:** Cada quien hace el trabajo a su manera; errores por malentendidos; instrucciones verbales; procedimientos obsoletos; nuevos empleados aprenden "por ósmosis"; retrabajo por "no sabía que era así".
**Early_Warning_Signals:** % de procesos con instrucciones de trabajo documentadas < 50%; variabilidad entre operadores alta; errores de principiantes mayores que expertos; instrucciones no actualizadas; retrabajo por "interpretación".
**Typical_Causes:** Falta de documentación de procesos; procedimientos no actualizados; cultura de "se hace así nomás"; rotación de personal sin transferencia de conocimiento; ausencia de estandarización.
**Business_Impact:** Retrabajo constante; calidad inconsistente; dificultad para entrenar nuevos empleados; dependencia de operadores clave; imposibilidad de escalar; productividad reducida.
**Metrics_To_Check:** % de procesos con instrucciones documentadas; % de instrucciones actualizadas; variabilidad entre operadores; retrabajo por falta de instrucciones; tiempo de entrenamiento de nuevos.
**Diagnostic_Questions:** ¿Hay instrucciones de trabajo claras? ¿Están actualizadas? ¿Todos siguen las mismas instrucciones? ¿Los errores son por falta de claridad? ¿Cuánto cuesta no tener instrucciones?
**Recommended_Actions:** Documentar instrucciones de trabajo para procesos críticos; mantenerlas actualizadas; usar formato visual (fotos, diagramas); capacitar en el estándar; verificar cumplimiento.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-038, PRC-048, PRC-058, PRC-082, PRC-089

### PRC-050
**Pattern_Name:** Retrabajo por Cambios de Último Minuto
**Category:** Retrabajo
**Description:** Los cambios de último minuto en especificaciones, diseño o requerimientos generan retrabajo porque el trabajo ya estaba avanzado o completado cuando llega el cambio.
**Observable_Symptoms:** Cambios frecuentes después de empezar; "esto cambió" a mitad del proceso; retrabajo por nuevas especificaciones; equipo frustrado por cambios de último momento; aprobaciones tardías.
**Early_Warning_Signals:** % de órdenes con cambios después de inicio > 20%; frecuencia de cambios de último minuto; tiempo perdido por cambios; % de capacidad absorbida por cambios; equipo quejándose de "cambian todo el tiempo".
**Typical_Causes:** Falta de congelamiento de especificaciones; aprobaciones tardías; clientes que cambian de opinión; planificación insuficiente; comunicación deficiente entre áreas.
**Business_Impact:** Retrabajo y desperdicio; lead times más largos; productividad reducida; equipo desmotivado; costos adicionales; calidad afectada por apuro.
**Metrics_To_Check:** % de cambios después de inicio; tiempo perdido por cambios; frecuencia de cambios; capacidad consumida por retrabajo de cambios; satisfacción del equipo.
**Diagnostic_Questions:** ¿Los cambios son frecuentes después de empezar? ¿Hay congelamiento de especificaciones? ¿Las aprobaciones son oportunas? ¿Cuánto cuestan los cambios de último minuto? ¿Se gestionan los cambios formalmente?
**Recommended_Actions:** Establecer punto de congelamiento de especificaciones; gestionar cambios formalmente (solicitud, aprobación, impacto); mejorar planificación previa; involucrar a aprobadores temprano; medir costo de cambios.
**Severity_Level:** High
**Related_Patterns:** PRC-005, PRC-048, PRC-051, PRC-058, PRC-106

### PRC-051
**Pattern_Name:** Retrabajo por Falta de Coordinación entre Áreas
**Category:** Retrabajo
**Description:** La falta de coordinación entre departamentos (ventas, producción, calidad, logística) genera retrabajo porque cada área trabaja con información parcial o desactualizada.
**Observable_Symptoms:** Información contradictoria entre áreas; ventas promete lo que producción no puede; producción hace cambios sin avisar a logística; retrabajo por descoordinación; reuniones de "alineación" constantes.
**Early_Warning_Signals:** Frecuencia de reuniones de coordinación > 3 por semana; % de errores por descoordinación; información desactualizada compartida; áreas con objetivos contrapuestos; retrabajo que involucra múltiples áreas.
**Typical_Causes:** Silos organizacionales; falta de sistema compartido; comunicación informal; objetivos no alineados; procesos no integrados; falta de reuniones de sincronización.
**Business_Impact:** Retrabajo por información incorrecta; demoras por descoordinación; conflictos entre áreas; clientes afectados; eficiencia general reducida.
**Metrics_To_Check:** % de retrabajo por descoordinación; frecuencia de errores entre áreas; tiempo de coordinación; satisfacción de colaboración inter-áreas; cumplimiento de acuerdos de servicio.
**Diagnostic_Questions:** ¿La información entre áreas es consistente? ¿Hay retrabajo por descoordinación? ¿Los objetivos están alineados? ¿La comunicación es efectiva? ¿Hay un sistema compartido de información?
**Recommended_Actions:** Implementar reuniones de sincronización breves diarias; alinear objetivos inter-áreas; establecer acuerdos de nivel de servicio (SLA) entre áreas; implementar sistema compartido de información.
**Severity_Level:** High
**Related_Patterns:** PRC-006, PRC-048, PRC-050, PRC-058, PRC-084

### PRC-052
**Pattern_Name:** Retrabajo por Materia Prima Deficiente No Detectada a Tiempo
**Category:** Retrabajo
**Description:** La materia prima defectuosa pasa desapercibida hasta etapas avanzadas del proceso, generando retrabajo que podría haberse evitado con inspección de recepción efectiva.
**Observable_Symptoms:** Defectos que se originan en materia prima; materiales pasan a producción sin inspección; el defecto se descubre después de varias etapas; retrabajo por "lote malo desde el inicio"; proveedor no asume responsabilidad.
**Early_Warning_Signals:** % de materia prima sin inspección de recepción > 30%; defectos atribuibles a materiales descubiertos tarde; % de lotes de proveedores con problemas; costo de retrabajo por materiales; quejas a proveedores no resueltas.
**Typical_Causes:** Falta de inspección de recepción; presión por iniciar producción rápido; especificaciones de compra no claras; proveedores no evaluados; materiales críticos no identificados.
**Business_Impact:** Retrabajo costoso en etapas avanzadas; desperdicio de materiales y tiempo; producción detenida; clientes afectados; relación tensa con proveedores.
**Metrics_To_Check:** % de inspección de recepción; defectos por materiales descubiertos en cada etapa; costo de retrabajo por materiales; scorecard de proveedores.
**Diagnostic_Questions:** ¿Se inspecciona la materia prima al recibirla? ¿Los defectos de materiales se detectan temprano? ¿Los proveedores son evaluados? ¿Hay especificaciones claras de compra? ¿Cuánto cuesta el retrabajo por materiales?
**Recommended_Actions:** Implementar inspección de recepción para materiales críticos; establecer especificaciones claras de compra; evaluar proveedores; mover inspección hacia el proveedor (certificación de proveedores).
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-041, PRC-048, PRC-060, PRC-062

### PRC-053
**Pattern_Name:** Retrabajo por Herramientas o Equipos Inadecuados
**Category:** Retrabajo
**Description:** Las herramientas, equipos o maquinaria no son los adecuados para el trabajo, generando errores y retrabajo que se atribuye al operador pero que en realidad es por falta de medios adecuados.
**Observable_Symptoms:** Operadores se quejan de herramientas; errores por "la máquina no sirve"; herramientas improvisadas; mantenimiento deficiente; equipos obsoletos que no cumplen especificaciones; retrabajo atribuido a "error humano" pero causado por herramienta.
**Early_Warning_Signals:** % de quejas de operadores sobre herramientas/equipos; frecuencia de averías; % de retrabajo atribuible a equipos; herramientas no calibradas; equipos fuera de especificaciones; inversión en herramientas < 1% de costos operativos.
**Typical_Causes:** Falta de inversión en herramientas; mantenimiento deficiente; herramientas no calibradas; equipos obsoletos; cultura de "con lo que hay se hace"; no se escuchan quejas de operadores.
**Business_Impact:** Retrabajo por herramientas inadecuadas; productividad reducida; calidad inconsistente; operadores frustrados; lesiones por herramientas inapropiadas; costos de retrabajo.
**Metrics_To_Check:** % de retrabajo por herramientas/equipos; quejas de operadores; frecuencia de calibración; antigüedad de equipos; inversión en herramientas; disponibilidad de equipos.
**Diagnostic_Questions:** ¿Las herramientas son las adecuadas? ¿Los equipos están calibrados? ¿Los operadores reportan problemas de herramientas? ¿El retrabajo es por equipos? ¿Se invierte en herramientas adecuadas?
**Recommended_Actions:** Evaluar adecuación de herramientas y equipos; implementar mantenimiento preventivo; calibrar herramientas periódicamente; invertir en herramientas adecuadas; escuchar quejas de operadores.
**Severity_Level:** High
**Related_Patterns:** PRC-013, PRC-048, PRC-060, PRC-071, PRC-095

### PRC-054
**Pattern_Name:** Retrabajo por Error Humano sin Barreras de Protección
**Category:** Retrabajo
**Description:** Los errores humanos son frecuentes y no se implementan mecanismos a prueba de errores (Poka-Yoke) para prevenirlos, dependiendo exclusivamente de la atención y cuidado del operador.
**Observable_Symptoms:** Errores humanos repetitivos; "fue error de María"; se depende de la concentración del operador; no hay dispositivos que impidan el error; se culpa a la persona no al proceso.
**Early_Warning_Signals:** % de defectos atribuidos a "error humano" > 40%; mismos errores se repiten; no hay Poka-Yoke implementados; entrenamiento no reduce errores; se culpa a personas sistemáticamente.
**Typical_Causes:** Falta de Poka-Yoke; procesos que dependen exclusivamente de la atención humana; cultura de culpar a la persona; no se analiza el proceso como causa; falta de ingeniería de prevención de errores.
**Business_Impact:** Retrabajo por errores evitables; calidad inconsistente; moral baja por cultura de culpa; productividad reducida; clientes afectados; costo de retrabajo alto.
**Metrics_To_Check:** % de defectos por "error humano"; frecuencia de errores repetitivos; % de procesos con Poka-Yoke; tendencia de errores a pesar de entrenamiento; costo de errores.
**Diagnostic_Questions:** ¿Los errores humanos se repiten? ¿Hay Poka-Yoke? ¿Se culpa a la persona o se analiza el proceso? ¿El entrenamiento reduce errores? ¿Se implementan barreras para prevenir errores?
**Recommended_Actions:** Implementar Poka-Yoke (dispositivos a prueba de errores); rediseñar procesos para hacerlos más robustos; no culpar a personas sino mejorar procesos; analizar causas de error humano; automatizar puntos críticos.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-036, PRC-048, PRC-058, PRC-082

### PRC-055
**Pattern_Name:** Retrabajo no se Mide ni Reporta
**Category:** Retrabajo
**Description:** El retrabajo no se mide, reporta ni cuantifica como costo, por lo que la empresa no sabe cuánto está perdiendo ni puede priorizar acciones para reducirlo.
**Observable_Symptoms:** No hay registro de retrabajo; no se sabe cuánto tiempo se pierde; el retrabajo se oculta para no parecer ineficiente; no hay responsable de medirlo; el retrabajo es invisible en los reportes.
**Early_Warning_Signals:** Sin métrica de retrabajo; % de retrabajo desconocido; reportes no incluyen retrabajo; equipo oculta retrabajo; no hay responsable; no se habla del costo del retrabajo.
**Typical_Causes:** Falta de sistema de medición; cultura de ocultar errores; no se considera importante; medición difícil; no hay consecuencia por no medir.
**Business_Impact:** Pérdida invisible por retrabajo; imposibilidad de mejorar; recursos desperdiciados sin saberlo; decisiones sin datos; retrabajo crónico no abordado.
**Metrics_To_Check:** (Deberían medirse) % de retrabajo; costo de retrabajo; capacidad dedicada a retrabajo; tendencia; causas principales.
**Diagnostic_Questions:** ¿Se mide el retrabajo? ¿Se reporta? ¿Se conoce el costo? ¿Hay responsable de reducirlo? ¿El retrabajo es visible en los reportes?
**Recommended_Actions:** Implementar medición de retrabajo (tiempo, materiales, costo); reportar semanalmente; asignar responsable de reducción; establecer metas; hacer visible el costo del retrabajo.
**Severity_Level:** High
**Related_Patterns:** PRC-029, PRC-040, PRC-048, PRC-058, PRC-117

### PRC-056
**Pattern_Name:** Retrabajo por Procesos No Definidos o Ambiguos
**Category:** Retrabajo
**Description:** Los procesos no están definidos o son ambiguos, por lo que cada vez que se ejecutan se hace de manera diferente, generando errores y retrabajo por falta de un método estándar.
**Observable_Symptoms:** Cada ejecución del proceso es diferente; no hay un "cómo hacerlo" definido; los resultados varían; hay discusiones sobre la mejor manera; retrabajo por no seguir un método consistente.
**Early_Warning_Signals:** % de procesos definidos < 40%; variabilidad de resultados alta; tiempo de ejecución variable; falta de documentos de proceso; % de retrabajo por "no sabíamos cómo hacerlo".
**Typical_Causes:** Procesos artesanales no documentados; crecimiento sin estandarizar; cultura de "cada maestrito con su librito"; falta de metodología; procesos heredados no revisados.
**Business_Impact:** Retrabajo constante; calidad inconsistente; dificultad para entrenar; dependencia de personas; imposibilidad de escalar; productividad impredecible.
**Metrics_To_Check:** % de procesos definidos; % de procesos documentados; variabilidad de resultados; retrabajo por procesos no definidos; tiempo de entrenamiento.
**Diagnostic_Questions:** ¿Los procesos están definidos? ¿Documentados? ¿Todos ejecutan igual? ¿El retrabajo es por falta de definición? ¿Cuántos procesos críticos no están definidos?
**Recommended_Actions:** Definir y documentar procesos críticos; estandarizar método de trabajo; capacitar en el estándar; verificar cumplimiento; revisar y mejorar periódicamente.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-048, PRC-049, PRC-058, PRC-082, PRC-089

### PRC-057
**Pattern_Name:** Retrabajo por Aprobaciones Lentas o Tardías
**Category:** Retrabajo
**Description:** Las aprobaciones (de clientes, supervisores, áreas técnicas) llegan tarde, cuando el trabajo ya avanzó, generando retrabajo para ajustar lo ya hecho a los requisitos aprobados.
**Observable_Symptoms:** Se empieza a trabajar antes de la aprobación; la aprobación llega cuando ya se avanzó; cambios por aprobación tardía; presión por "empezar aunque no esté aprobado"; retrabajo por ajustes post-aprobación.
**Early_Warning_Signals:** % de trabajos iniciados sin aprobación; tiempo de aprobación > 20% del lead time; frecuencia de cambios post-aprobación; % de retrabajo por aprobaciones tardías; cola de aprobaciones pendientes.
**Typical_Causes:** Aprobadores sobrecargados; proceso de aprobación burocrático; falta de autoridad delegada; aprobaciones secuenciales lentas; no se priorizan las aprobaciones.
**Business_Impact:** Retrabajo por empezar sin aprobación; lead times más largos; equipo trabaja con incertidumbre; aprobaciones son cuello de botella; calidad afectada por apuro.
**Metrics_To_Check:** Tiempo de aprobación; % de trabajos iniciados sin aprobación; % de retrabajo por aprobaciones; cola de aprobaciones; tendencia.
**Diagnostic_Questions:** ¿Las aprobaciones son oportunas? ¿Se empieza a trabajar sin aprobación? ¿El retrabajo es por aprobaciones tardías? ¿Hay cuello de botella en aprobaciones? ¿Se puede delegar autoridad?
**Recommended_Actions:** Acelerar proceso de aprobación; delegar autoridad; aprobar en paralelo cuando sea posible; establecer SLA de aprobación; no empezar sin aprobación.
**Severity_Level:** High
**Related_Patterns:** PRC-005, PRC-026, PRC-048, PRC-050, PRC-108

### PRC-058
**Pattern_Name:** Retrabajo Encubierto (No Reportado)
**Category:** Retrabajo
**Description:** El retrabajo existe pero no se reporta formalmente porque el equipo lo oculta o lo absorbe en su tiempo regular, haciendo que la pérdida sea invisible para la gestión.
**Observable_Symptoms:** El equipo se queda hasta tarde o llega temprano para "arreglar cosas"; las horas extras son frecuentes pero no se justifican; los reportes muestran producción perfecta pero hay quejas; se oculta el retrabajo por miedo a represalias; el retrabajo "se resuelve en el camino".
**Early_Warning_Signals:** Horas extras no justificadas; producción reportada perfecta pero quejas de clientes; equipo trabaja fuera de horario; diferencia entre producción reportada y real; % de retrabajo reportado vs estimado real.
**Typical_Causes:** Cultura de culpa; miedo a represalias por reportar errores; medición punitiva; no hay espacio para la mejora; liderazgo no tolera errores.
**Business_Impact:** Pérdida invisible; imposibilidad de mejorar; equipo sobrecargado; moral baja; rotación de personal; desperdicio no identificado.
**Metrics_To_Check:** Horas extras vs retrabajo; diferencias entre producción y reportes; % de retrabajo estimado vs reportado; clima laboral; rotación.
**Diagnostic_Questions:** ¿Se oculta el retrabajo? ¿Hay miedo a reportar errores? ¿Las horas extras son por retrabajo encubierto? ¿Los reportes reflejan la realidad? ¿Hay cultura de transparencia con errores?
**Recommended_Actions:** Crear cultura de transparencia donde reportar errores no tenga consecuencias negativas; medir retrabajo de manera anónima; separar medición de mejora de evaluación de desempeño; celebrar identificación de problemas.
**Severity_Level:** Critical
**Related_Patterns:** PRC-048, PRC-055, PRC-059, PRC-117, PRC-125

### PRC-059
**Pattern_Name:** Retrabajo por Devoluciones de Clientes
**Category:** Retrabajo
**Description:** Los productos devueltos por clientes requieren retrabajo para ser revendidos, reparados o desechados, consumiendo capacidad que podría usarse para producción nueva.
**Observable_Symptoms:** Productos devueltos se acumulan; equipo dedicado a reparar devoluciones; el retrabajo de devoluciones compite con producción nueva; devoluciones no se analizan para prevenir; clientes se quejan del mismo problema.
**Early_Warning_Signals:** % de capacidad dedicada a retrabajo de devoluciones > 10%; volumen de devoluciones creciente; tiempo de reparación de devoluciones; % de productos devueltos que se reparan vs se desechan; quejas recurrentes.
**Typical_Causes:** Defectos de calidad; producto no cumple expectativas; empaque inadecuado; logística de entrega dañina; especificaciones no claras.
**Business_Impact:** Capacidad desperdiciada en retrabajo; costos de reparación; pérdida de ingresos por devoluciones; insatisfacción del cliente; LTV reducido; reputación dañada.
**Metrics_To_Check:** % de capacidad en retrabajo de devoluciones; costo de retrabajo de devoluciones; % de productos reparables vs pérdida total; tendencia de devoluciones; causas de devolución.
**Diagnostic_Questions:** ¿Cuánto tiempo se dedica a retrabajar devoluciones? ¿Las devoluciones se analizan? ¿Se implementan acciones para reducirlas? ¿El retrabajo de devoluciones afecta la producción nueva? ¿Cuál es el costo total?
**Recommended_Actions:** Analizar causas raíz de devoluciones; mejorar calidad; mejorar empaque; alinear expectativas; implementar acciones correctivas; medir y reducir costo de retrabajo de devoluciones.
**Severity_Level:** Critical
**Related_Patterns:** PRC-036, PRC-045, PRC-046, PRC-048, PRC-058


## Desperdicios

### PRC-060
**Pattern_Name:** Desperdicio de Materiales No Medido
**Category:** Desperdicios
**Description:** La empresa no mide el desperdicio de materiales (sobrantes, mermas, recortes, productos defectuosos), por lo que no sabe cuánto material se pierde ni puede tomar acciones para reducirlo.
**Observable_Symptoms:** Sobrantes de material que se tiran; mermas no registradas; no se sabe cuánto material se desperdicia por lote; el desperdicio se considera "normal"; no hay control de rendimiento de materiales.
**Early_Warning_Signals:** Desperdicio de materiales no medido; % de rendimiento de materiales desconocido; sobrantes sin control; mermas > 10% del material sin registrar; costo de desperdicio no calculado.
**Typical_Causes:** Falta de sistema de medición; cultura de "es normal perder"; materiales de bajo costo aparente; no se valora el desperdicio; falta de cultura de reducción.
**Business_Impact:** Pérdida económica invisible por desperdicio; materiales desperdiciados; mayor costo de producción; impacto ambiental; competitividad reducida; recursos escasos mal utilizados.
**Metrics_To_Check:** (Deberían medirse) % de rendimiento de materiales; costo de desperdicio; % de merma; tendencia; desperdicio por producto.
**Diagnostic_Questions:** ¿Se mide el desperdicio de materiales? ¿Se conoce el rendimiento por lote? ¿Los sobrantes se controlan? ¿Cuánto material se pierde? ¿Hay metas de reducción de desperdicio?
**Recommended_Actions:** Implementar medición de desperdicio de materiales por lote; calcular rendimiento; establecer metas de reducción; capacitar en reducción de desperdicio; implementar control de mermas.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-036, PRC-048, PRC-061, PRC-065, PRC-082

### PRC-061
**Pattern_Name:** Desperdicio de Tiempo por Esperas y Filas
**Category:** Desperdicios
**Description:** El tiempo de los operadores y equipos se desperdicia en esperas (de materiales, información, instrucciones, aprobaciones) y en filas (cola de trabajo en proceso).
**Observable_Symptoms:** Operadores esperando material; trabajo en proceso acumulado; máquinas detenidas esperando; personas ociosas porque "no hay trabajo"; aprobaciones demoran el flujo.
**Early_Warning_Signals:** % de tiempo de operadores en espera > 15%; WIP acumulado > 3 días de producción; máquinas detenidas por espera > 10% del tiempo; colas entre procesos; % de lead time que es espera > 50%.
**Typical_Causes:** Flujo desbalanceado; lotes grandes que generan colas; falta de sincronización; procesos con capacidad desigual; planificación deficiente; falta de monitoreo de flujo.
**Business_Impact:** Productividad reducida; lead times largos; capital de trabajo inmovilizado en WIP; capacidad desperdiciada; entregas tardías; costos operativos más altos.
**Metrics_To_Check:** % de tiempo en espera; nivel de WIP; ratio de lead time / tiempo de valor agregado; máquinas detenidas por espera; tendencia.
**Diagnostic_Questions:** ¿Los operadores pasan tiempo esperando? ¿Hay WIP acumulado? ¿Las máquinas se detienen por falta de material? ¿Cuánto del lead time es espera? ¿Hay colas entre procesos?
**Recommended_Actions:** Balancear líneas; reducir tamaño de lotes; implementar flujo continuo; sincronizar procesos; mejorar planificación; monitorear y reducir WIP; implementar sistema pull.
**Severity_Level:** Critical
**Related_Patterns:** PRC-009, PRC-024, PRC-026, PRC-029, PRC-031, PRC-060, PRC-075

### PRC-062
**Pattern_Name:** Desperdicio de Material por Sobreproducción
**Category:** Desperdicios
**Description:** Se produce más de lo necesario (sobreproducción), generando desperdicio de materiales que podrían haberse usado para otros pedidos o que se vuelven obsoletos.
**Observable_Symptoms:** Productos terminados en stock que nadie pidió; inventario de productos que se vuelven obsoletos; materiales usados para producir "por si acaso"; sobreproducción para "mantener máquinas ocupadas"; lotes grandes "para aprovechar".
**Early_Warning_Signals:** % de producción sobre pedido < 60%; inventario de productos terminados creciente; obsolescencia de inventario; % de productos producidos y no vendidos > 20%; costo de mantener inventario.
**Typical_Causes:** Producción contra pronóstico no contra pedido; miedo a quedarse sin stock; lotes económicos que no consideran demanda real; cultura de "mantener máquinas ocupadas"; planificación deficiente.
**Business_Impact:** Material desperdiciado en productos no vendidos; capital de trabajo inmovilizado; espacio ocupado por inventario; obsolescencia; costos de almacenamiento; descuentos por liquidar.
**Metrics_To_Check:** % de producción sobre pedido; inventario de productos terminados en días; obsolescencia; % de sobreproducción; costo de inventario.
**Diagnostic_Questions:** ¿Se produce contra pedido o contra pronóstico? ¿Hay sobreproducción? ¿El inventario de productos terminados crece? ¿Hay productos obsoletos? ¿Se produce "por si acaso"?
**Recommended_Actions:** Producir contra pedido (make-to-order); reducir tamaño de lotes; implementar sistema pull; alinear producción con demanda real; eliminar producción "para mantener ocupado".
**Severity_Level:** Critical
**Related_Patterns:** PRC-007, PRC-029, PRC-060, PRC-063, PRC-070, PRC-075

### PRC-063
**Pattern_Name:** Desperdicio de Material por Cambios de Formato o Set-Up
**Category:** Desperdicios
**Description:** Durante los cambios de formato, set-up o limpieza entre lotes, se desperdicia material (productos de arranque, purgas, ajustes) que no se recupera ni se mide.
**Observable_Symptoms:** Productos fuera de especificación al arrancar; material de purga no se recupera; ajustes generan desperdicio; el set-up genera una cantidad de material no conforme; no se optimiza el cambio.
**Early_Warning_Signals:** % de material desperdiciado en set-ups > 3% de producción; tiempo de set-up largo; material de arranque no conforme no recuperado; frecuencia de cambios alta; % de scrap en cambios.
**Typical_Causes:** Set-ups largos no optimizados (SMED); falta de procedimiento de cambio; materiales de arranque no estandarizados; equipos con ajustes complejos; no se mide desperdicio por cambio.
**Business_Impact:** Material desperdiciado en cambios; tiempo de set-up improductivo; menor capacidad efectiva; costo de producción más alto; competitividad reducida.
**Metrics_To_Check:** % de desperdicio en set-ups; tiempo de set-up; % de scrap en cambios; frecuencia de cambios; costo de desperdicio por cambio.
**Diagnostic_Questions:** ¿Se desperdicia material en cambios de formato? ¿El set-up genera desperdicio? ¿Se ha optimizado el cambio? ¿Se recupera material de purga? ¿Se mide el desperdicio por cambio?
**Recommended_Actions:** Implementar SMED (cambio rápido); Estandarizar procedimientos de cambio; recuperar material de purga cuando sea posible; optimizar ajustes; medir y reducir desperdicio en cambios.
**Severity_Level:** High
**Related_Patterns:** PRC-009, PRC-024, PRC-032, PRC-060, PRC-082

### PRC-064
**Pattern_Name:** Desperdicio de Espacio por Mala Distribución (Layout)
**Category:** Desperdicios
**Description:** La distribución de la planta o espacio de trabajo es ineficiente, generando desperdicio de movimiento, transporte y espacio que no agrega valor.
**Observable_Symptoms:** Distancias largas entre procesos; pasillos obstruidos; materiales transportados grandes distancias; operadores caminan mucho; áreas desordenadas; espacio mal aprovechado.
**Early_Warning_Signals:** Distancia recorrida por producto > 100 metros (o estándar); % de espacio utilizado productivamente < 60%; tiempo de transporte > 10% del lead time; operadores caminan > 2 km/día; áreas congestionadas.
**Typical_Causes:** Layout no planificado; crecimiento orgánico sin rediseño; procesos agregados donde se pudo; falta de estudio de flujo; instalaciones heredadas no optimizadas.
**Business_Impact:** Desperdicio de tiempo en transporte; productividad reducida; fatiga del operador; mayor lead time; espacio subutilizado; dificultad de flujo.
**Metrics_To_Check:** Distancia recorrida por producto; % de espacio utilizado; tiempo de transporte; distancia caminada por operador; eficiencia de layout.
**Diagnostic_Questions:** ¿La distribución es eficiente? ¿Los operadores caminan mucho? ¿Hay distancias largas entre procesos? ¿El espacio está bien aprovechado? ¿El flujo de materiales es directo?
**Recommended_Actions:** Analizar layout actual; rediseñar distribución por flujo de proceso; acercar procesos consecutivos; implementar celdas de manufactura; optimizar uso de espacio; 5S.
**Severity_Level:** Medium
**Related_Patterns:** PRC-009, PRC-028, PRC-061, PRC-065, PRC-069, PRC-095

### PRC-065
**Pattern_Name:** Desperdicio de Movimiento en el Puesto de Trabajo
**Category:** Desperdicios
**Description:** Los operadores realizan movimientos innecesarios (buscar herramientas, agacharse, estirarse, caminar) que no agregan valor y reducen la productividad.
**Observable_Symptoms:** Operadores buscando herramientas; movimientos repetitivos no ergonómicos; estaciones desordenadas; herramientas lejos del punto de uso; operadores caminan a buscar materiales frecuentemente.
**Early_Warning_Signals:** % de tiempo en movimientos que no agregan valor > 20%; distancia caminada > estándar; herramientas no en punto de uso; desorden en estación; movimientos repetitivos no ergonómicos.
**Typical_Causes:** Puesto de trabajo mal diseñado; herramientas sin ubicación fija; falta de 5S; materiales no cerca del punto de uso; falta de estudio de movimientos.
**Business_Impact:** Productividad reducida; fatiga del operador; riesgo de lesiones; tiempo perdido; calidad afectada por movimientos apurados; moral baja.
**Metrics_To_Check:** % de tiempo en movimientos sin valor agregado; distancia caminada por turno; ergonomía del puesto; productividad por operador; incidentes de lesiones.
**Diagnostic_Questions:** ¿Los operadores se mueven innecesariamente? ¿Las herramientas están en el punto de uso? ¿El puesto está ordenado? ¿Se han estudiado los movimientos? ¿Hay fatiga por movimiento?
**Recommended_Actions:** Implementar 5S; rediseñar puestos de trabajo (ergonomía); acercar herramientas y materiales al punto de uso; estandarizar ubicaciones; estudiar movimientos y eliminar innecesarios.
**Severity_Level:** Medium
**Related_Patterns:** PRC-013, PRC-014, PRC-060, PRC-064, PRC-095, PRC-125

### PRC-066
**Pattern_Name:** Desperdicio de Talento y Conocimiento
**Category:** Desperdicios
**Description:** El talento, conocimiento y capacidad de resolución de problemas del equipo no se utiliza, desperdiciando ideas de mejora, sugerencias y experiencia que podrían beneficiar a la organización.
**Observable_Symptoms:** Los operadores tienen ideas pero no son escuchados; las sugerencias no se implementan; el equipo sabe cómo mejorar pero no se les pide; la experiencia de años no se captura; rotación de personal pierde conocimiento.
**Early_Warning_Signals:** % de sugerencias implementadas < 10%; equipo pasivo en mejoras; conocimiento no documentado; rotación de personal pierde know-how; no hay buzón de sugerencias o similar; equipo desmotivado.
**Typical_Causes:** Cultura jerárquica donde solo los jefes piensan; falta de canales de sugerencia; no se valora la experiencia operativa; gerencia no escucha al equipo; incentivos no incluyen mejora.
**Business_Impact:** Oportunidades de mejora perdidas; equipo desmotivado; rotación de personal; conocimiento perdido; innovación limitada; problemas no resueltos que el equipo sabría cómo solucionar.
**Metrics_To_Check:** % de sugerencias implementadas; número de sugerencias por empleado; % de conocimiento documentado; rotación de personal; clima laboral.
**Diagnostic_Questions:** ¿Se escuchan las ideas del equipo? ¿Hay canales de sugerencia? ¿Las sugerencias se implementan? ¿El conocimiento se documenta? ¿El equipo participa en la mejora?
**Recommended_Actions:** Crear canales de sugerencias; implementar ideas del equipo; reconocer contribuciones; documentar conocimiento crítico; capacitar al equipo en mejora continua; involucrar a todos en solución de problemas.
**Severity_Level:** High
**Related_Patterns:** PRC-042, PRC-058, PRC-082, PRC-117, PRC-119, PRC-125

### PRC-067
**Pattern_Name:** Desperdicio de Energía e Insumos
**Category:** Desperdicios
**Description:** La empresa desperdicia energía eléctrica, agua, gas u otros insumos sin medirlo ni controlarlo, asumiendo que es un costo fijo inevitable en lugar de una oportunidad de mejora.
**Observable_Symptoms:** Luces encendidas sin necesidad; equipos funcionando sin producir; compresores con fugas; aire comprimido perdido; agua corriendo sin uso; no hay medición por área o equipo; facturas de energía altas sin análisis.
**Early_Warning_Signals:** Costo energético como % de ventas > benchmark (ej. > 3% manufactura); no hay medidores por área; equipos encendidos sin producción; fugas de aire/agua no reparadas; consumo específico (por unidad) no calculado.
**Typical_Causes:** Desconocimiento del consumo; falta de medidores; cultura de "no es significativo"; equipos ineficientes; falta de mantenimiento; no hay responsable de eficiencia energética.
**Business_Impact:** Costos operativos más altos de lo necesario; margen reducido; impacto ambiental mayor; competitividad reducida; recursos escasos desperdiciados.
**Metrics_To_Check:** Costo energético como % de ventas; consumo específico (por unidad producida); % de fugas; tendencia; comparación con benchmark.
**Diagnostic_Questions:** ¿Se mide el consumo energético? ¿Hay medidores por área? ¿Los equipos se apagan cuando no producen? ¿Hay fugas? ¿El consumo específico se conoce?
**Recommended_Actions:** Medir consumo energético por área/equipo; implementar programa de eficiencia energética; apagar equipos cuando no producen; reparar fugas; cambiar a equipos eficientes; crear responsable de energía.
**Severity_Level:** Medium
**Related_Patterns:** PRC-013, PRC-060, PRC-068, PRC-082, PRC-117

### PRC-068
**Pattern_Name:** Desperdicio en Procesos Administrativos (Muda Administrativa)
**Category:** Desperdicios
**Description:** Los procesos administrativos (facturación, compras, reporting) contienen desperdicios como aprobaciones innecesarias, datos duplicados, retrabajo administrativo y esperas que no agregan valor.
**Observable_Symptoms:** Aprobaciones múltiples para lo mismo; datos ingresados varias veces en diferentes sistemas; reportes que nadie usa; procesos administrativos largos; papeleo excesivo; "esto siempre se hizo así".
**Early_Warning_Signals:** Tiempo de proceso administrativo > 3 días (según tipo); % de reportes no utilizados > 30%; duplicación de datos; número de aprobaciones > necesario; quejas del equipo por burocracia.
**Typical_Causes:** Procesos diseñados sin pensar en eficiencia; sistemas no integrados; controles excesivos por desconfianza; cultura de "siempre se hizo así"; falta de revisión de procesos administrativos.
**Business_Impact:** Tiempo perdido en actividades sin valor; lentitud en respuesta; equipo administrativo sobredimensionado; costos administrativos altos; demoras en decisiones; insatisfacción de clientes internos.
**Metrics_To_Check:** Tiempo de proceso administrativo; % de actividades sin valor agregado; % de reportes útiles; productividad administrativa; quejas internas.
**Diagnostic_Questions:** ¿Los procesos administrativos son eficientes? ¿Hay aprobaciones innecesarias? ¿Los datos se ingresan una sola vez? ¿Los reportes se usan? ¿Se han revisado los procesos administrativos?
**Recommended_Actions:** Mapear procesos administrativos; identificar y eliminar desperdicios; automatizar tareas repetitivas; eliminar aprobaciones innecesarias; integrar sistemas; reducir papeleo.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-048, PRC-060, PRC-072, PRC-082, PRC-084

### PRC-069
**Pattern_Name:** Desperdicio de Transporte de Materiales
**Category:** Desperdicios
**Description:** Los materiales se transportan múltiples veces, grandes distancias o con medios ineficientes, generando desperdicio de tiempo, recursos y riesgo de daños.
**Observable_Symptoms:** Materiales que van y vienen; transportes repetitivos; montacargas circulando vacío; distancias largas entre almacenes y producción; manipulación excesiva de materiales; daños por transporte.
**Early_Warning_Signals:** Distancia total recorrida por material > 500 metros (benchmark); % de tiempo de transporte en lead time > 15%; daños por manipulación; número de movimientos por producto; vehículos circulando vacíos > 30% del tiempo.
**Typical_Causes:** Layout ineficiente; almacenes lejos de producción; falta de planificación de rutas; múltiples manipulaciones; medios de transporte inadecuados; procesos no adyacentes.
**Business_Impact:** Tiempo perdido en transporte; riesgo de daños; productividad reducida; costo de transporte; lead time más largo; fatiga de operadores.
**Metrics_To_Check:** Distancia recorrida por material; tiempo de transporte; daños por manipulación; % de viajes vacíos; costo de transporte interno.
**Diagnostic_Questions:** ¿Los materiales se transportan distancias largas? ¿Hay movimientos repetitivos? ¿Los transportes van vacíos? ¿Hay daños por manipulación? ¿Se puede reducir el transporte?
**Recommended_Actions:** Rediseñar layout para minimizar distancias; planificar rutas de transporte; consolidar movimientos; usar medios de transporte eficientes; ubicar almacenes cerca de uso; reducir manipulaciones.
**Severity_Level:** Medium
**Related_Patterns:** PRC-028, PRC-060, PRC-064, PRC-065, PRC-095

### PRC-070
**Pattern_Name:** Desperdicio de Inventario (Materia Prima, WIP, Producto Terminado)
**Category:** Desperdicios
**Description:** La empresa mantiene inventarios excesivos en materias primas, trabajo en proceso o productos terminados, inmovilizando capital y generando costos de almacenamiento, obsolescencia y riesgo.
**Observable_Symptoms:** Almacén lleno de materiales que no se usan; WIP acumulado entre procesos; productos terminados que no se venden; inventario "por si acaso"; materiales obsoletos ocupando espacio; faltantes de ciertos ítems y exceso de otros.
**Early_Warning_Signals:** Rotación de inventario < 6 veces/año (manufactura) o < benchmark; % de inventario obsoleto > 10%; días de inventario > 60 días; costo de almacenamiento > 5% del valor del inventario; faltantes frecuentes a pesar de alto inventario.
**Typical_Causes:** Pronósticos inexactos; lotes grandes; producción contra pronóstico; compras no alineadas con producción; falta de sistema pull; miedo a desabastecimiento; múltiples SKUs sin segmentación ABC.
**Business_Impact:** Capital de trabajo inmovilizado; costo de almacenamiento; obsolescencia; riesgo de pérdida; efectivo disponible reducido; rentabilidad afectada.
**Metrics_To_Check:** Rotación de inventario; días de inventario; % de inventario obsoleto; costo de almacenamiento; nivel de servicio (fill rate); tendencia.
**Diagnostic_Questions:** ¿Los inventarios son excesivos? ¿Hay materiales obsoletos? ¿La rotación es baja? ¿Hay faltantes a pesar de alto inventario? ¿Se usa clasificación ABC? ¿Hay sistema pull?
**Recommended_Actions:** Implementar clasificación ABC de inventarios; reducir lotes; implementar sistema pull (Kanban); mejorar pronósticos; eliminar inventario obsoleto; establecer políticas de inventario por categoría.
**Severity_Level:** Critical
**Related_Patterns:** PRC-007, PRC-015, PRC-029, PRC-060, PRC-062, PRC-096

### PRC-071
**Pattern_Name:** Desperdicio de Capacidad por Mantenimiento Deficiente
**Category:** Desperdicios
**Description:** Las máquinas y equipos tienen baja disponibilidad por mantenimiento deficiente (reactivo, no preventivo), desperdiciando capacidad de producción que podría aprovecharse.
**Observable_Symptoms:** Máquinas que se detienen por averías; mantenimiento solo cuando se rompe; paradas no programadas frecuentes; equipos trabajando por debajo de su capacidad; el área de mantenimiento siempre "apagando incendios".
**Early_Warning_Signals:** Disponibilidad de equipos < 80%; MTBF (tiempo medio entre fallas) decreciente; % de mantenimiento reactivo > 60%; paradas no programadas > 5% del tiempo; horas de mantenimiento correctivo > preventivo.
**Typical_Causes:** Falta de mantenimiento preventivo; cultura de "arreglar cuando se rompe"; falta de plan de mantenimiento; repuestos críticos no disponibles; operadores no capacitados en mantenimiento básico.
**Business_Impact:** Capacidad perdida por averías; producción no cumplida; costos de mantenimiento reactivo altos; vida útil de equipos reducida; imprevisibilidad de producción; entregas tardías.
**Metrics_To_Check:** Disponibilidad de equipos; MTBF; % de mantenimiento reactivo vs preventivo; OEE (Overall Equipment Effectiveness); costos de mantenimiento.
**Diagnostic_Questions:** ¿Las máquinas tienen paradas no programadas frecuentes? ¿Hay mantenimiento preventivo? ¿El mantenimiento es reactivo? ¿Se mide la disponibilidad? ¿Hay plan de mantenimiento?
**Recommended_Actions:** Implementar mantenimiento preventivo; crear plan de mantenimiento; capacitar operadores en mantenimiento autónomo; asegurar repuestos críticos; medir disponibilidad; implementar TPM.
**Severity_Level:** Critical
**Related_Patterns:** PRC-013, PRC-024, PRC-025, PRC-029, PRC-060, PRC-095, PRC-096


## Automatización

### PRC-072
**Pattern_Name:** Procesos Manuales y Repetitivos sin Automatizar
**Category:** Automatización
**Description:** Tareas manuales, repetitivas y de alto volumen se realizan sin apoyo de herramientas tecnológicas o automatización, desperdiciando tiempo y recursos que podrían dedicarse a actividades de mayor valor.
**Observable_Symptoms:** Tareas manuales que consumen horas; datos ingresados a mano; cálculos manuales; reportes hechos uno por uno; procesos que claramente podrían automatizarse; el equipo pasa tiempo en tareas tediosas.
**Early_Warning_Signals:** % de tareas repetitivas manuales > 30%; tiempo dedicado a tareas administrativas manuales; errores por ingreso manual de datos; volumen de transacciones manuales; horas hombre en tareas automatizables.
**Typical_Causes:** Desconocimiento de herramientas; inversión inicial percibida como alta; cultura de "siempre se hizo así"; falta de habilidades técnicas; resistencia al cambio.
**Business_Impact:** Productividad baja; errores por trabajo manual; equipo desmotivado por tareas repetitivas; costos operativos altos; escalabilidad limitada; incapaz de manejar crecimiento.
**Metrics_To_Check:** % de procesos automatizados; tiempo en tareas manuales; errores por trabajo manual; productividad por empleado; tendencia.
**Diagnostic_Questions:** ¿Hay tareas manuales repetitivas que podrían automatizarse? ¿Qué procesos consumen más tiempo manual? ¿Se han evaluado herramientas de automatización? ¿El equipo está sobrecargado con tareas administrativas? ¿Hay resistencia a la automatización?
**Recommended_Actions:** Identificar procesos candidatos a automatización (alto volumen, repetitivos, manuales); evaluar herramientas (RPA, software, Excel avanzado); calcular ROI; implementar gradualmente; capacitar al equipo.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-068, PRC-073, PRC-082, PRC-125

### PRC-073
**Pattern_Name:** Automatización Parcial que Genera Cuellos de Botella
**Category:** Automatización
**Description:** Se automatizaron partes del proceso pero no el flujo completo, creando cuellos de botella donde lo automatizado entrega más rápido de lo que lo manual puede procesar, o viceversa.
**Observable_Symptoms:** Pasos automatizados rápidos, pasos manuales lentos; acumulación entre proceso automatizado y manual; el proceso más rápido espera al más lento; automatización no rinde todo su potencial; inversión en automatización no se justifica.
**Early_Warning_Signals:** Diferencia de velocidad entre paso automatizado y manual > 3x; WIP acumulado entre proceso automatizado y manual; % de capacidad ociosa del proceso automatizado > 30%; tiempo de ciclo del cuello de botella manual; inversión no genera mejora esperada.
**Typical_Causes:** Automatización de pasos aislados sin visión del flujo completo; falta de análisis de capacidad antes de automatizar; no se automatizaron los cuellos de botella; inversión mal priorizada.
**Business_Impact:** Inversión en automatización no rinde; cuello de botella persiste; productividad limitada; flujo desbalanceado; retorno de inversión bajo; frustración por no ver mejoras.
**Metrics_To_Check:** Diferencia de capacidad entre pasos automatizados y manuales; % de utilización de equipos automatizados; cuello de botella del proceso; ROI de automatización.
**Diagnostic_Questions:** ¿La automatización rinde todo su potencial? ¿Hay cuellos de botella entre procesos automatizados y manuales? ¿Se automatizaron los cuellos de botella? ¿El flujo completo está balanceado? ¿El ROI de automatización es el esperado?
**Recommended_Actions:** Analizar el flujo completo antes de automatizar; priorizar automatización de cuellos de botella; balancear capacidad automatizada y manual; considerar automatización del proceso completo; medir impacto.
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-025, PRC-072, PRC-074, PRC-082, PRC-096

### PRC-074
**Pattern_Name:** Herramientas Tecnológicas Subutilizadas
**Category:** Automatización
**Description:** La empresa ha invertido en herramientas tecnológicas (software, ERP, CRM) pero las utiliza solo parcialmente, aprovechando una fracción de su capacidad y dejando funciones valiosas sin usar.
**Observable_Symptoms:** Se usa 20% de las funciones del software; el ERP solo se usa para facturación; el CRM no se usa para seguimiento; hojas de Excel paralelas al sistema; el equipo prefiere sus métodos antiguos; funcionalidades compradas no implementadas.
**Early_Warning_Signals:** % de funcionalidades del sistema utilizadas < 40%; módulos comprados no implementados; datos en Excel fuera del sistema; % de usuarios activos de la herramienta; quejas del equipo sobre "el sistema no sirve" cuando no lo conocen.
**Typical_Causes:** Falta de capacitación en la herramienta; implementación incompleta; resistencia al cambio; selección de herramienta inadecuada; falta de liderazgo en adopción; personal no sabe todas las capacidades.
**Business_Impact:** Inversión desperdiciada; productividad no mejora; procesos siguen siendo manuales aunque hay herramientas; costos de licencia sin retorno; equipo frustrado con sistemas que "no sirven".
**Metrics_To_Check:** % de funcionalidades utilizadas; % de usuarios activos; módulos implementados vs comprados; datos fuera del sistema; ROI de la herramienta.
**Diagnostic_Questions:** ¿Se aprovechan las herramientas tecnológicas? ¿El equipo conoce todas las funcionalidades? ¿Hay datos fuera del sistema? ¿La inversión ha dado retorno? ¿Hay resistencia a usar el sistema?
**Recommended_Actions:** Capacitar al equipo en la herramienta; implementar módulos no utilizados; revisar si la herramienta es adecuada; estandarizar uso; eliminar sistemas paralelos; medir adopción.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-068, PRC-072, PRC-082, PRC-084, PRC-125

### PRC-075
**Pattern_Name:** Falta de Automatización en Control de Inventarios
**Category:** Automatización
**Description:** El control de inventarios se realiza manualmente (hojas de cálculo, conteo físico, tarjetas), sin un sistema automatizado que dé visibilidad en tiempo real de stocks, movimientos y alertas.
**Observable_Symptoms:** Inventarios en Excel desactualizados; conteos físicos frecuentes; diferencias entre sistema y real; faltantes o excesos no detectados a tiempo; no se sabe cuánto hay en tiempo real; órdenes de compra basadas en estimaciones.
**Early_Warning_Signals:** % de precisión de inventario < 90%; frecuencia de conteo cíclico; diferencias inventario físico vs sistema > 5%; rupturas de stock por falta de visibilidad; obsolescencia no detectada.
**Typical_Causes:** Falta de inversión en sistema de gestión; cultura de "Excel es suficiente"; crecimiento que superó el método manual; múltiples ubicaciones sin sistema; falta de integración compras-almacén-ventas.
**Business_Impact:** Desabastecimientos o excesos; capital de trabajo inmovilizado; falta de confianza en datos; decisiones basadas en información incorrecta; ventas perdidas por falta de stock; costos de almacenamiento excesivos.
**Metrics_To_Check:** Precisión de inventario (%); frecuencia de rupturas de stock; nivel de inventario; diferencias físico vs sistema; costo de inventario; rotación.
**Diagnostic_Questions:** ¿El inventario se controla manualmente? ¿Hay diferencias entre el sistema y la realidad? ¿Se sabe cuánto hay en tiempo real? ¿Hay rupturas de stock? ¿Hay obsolescencia?
**Recommended_Actions:** Implementar sistema de gestión de inventarios (WMS o módulo ERP); automatizar movimientos y conteo cíclico; establecer alertas de stock mínimo; integrar compras-almacén-ventas; capacitar al equipo.
**Severity_Level:** Critical
**Related_Patterns:** PRC-007, PRC-015, PRC-029, PRC-070, PRC-072, PRC-100

### PRC-076
**Pattern_Name:** Automatización sin Capacitación del Equipo
**Category:** Automatización
**Description:** Se invierte en automatización pero no se capacita adecuadamente al equipo en su uso, por lo que la herramienta no se adopta o se usa incorrectamente, desperdiciando la inversión.
**Observable_Symptoms:** El equipo no sabe usar la nueva herramienta; resistencia a la automatización por desconocimiento; errores por mal uso; la herramienta se abandona; se sigue usando el método anterior; quejas de "el sistema no sirve".
**Early_Warning_Signals:** % de capacitación completada sobre planificada < 60%; % de usuarios activos de la herramienta; errores post-implementación; tiempo hasta adopción completa > 6 meses; % de funcionalidades usadas correctamente.
**Typical_Causes:** Presupuesto insuficiente para capacitación; subestimación de la curva de aprendizaje; enfoque solo en tecnología no en personas; falta de plan de cambio; capacitación genérica no específica.
**Business_Impact:** Inversión en automatización desperdiciada; productividad no mejora inicialmente (empeora); equipo frustrado; resistencia a futuras automatizaciones; ROI negativo.
**Metrics_To_Check:** % de capacitación completada; % de adopción; errores post-implementación; productividad pre y post; tiempo de curva de aprendizaje.
**Diagnostic_Questions:** ¿Se capacitó al equipo en la automatización? ¿La capacitación fue adecuada? ¿El equipo adoptó la herramienta? ¿Hay resistencia? ¿La inversión está dando resultados?
**Recommended_Actions:** Invertir en capacitación (20-30% del presupuesto de automatización); capacitar antes de implementar; dar soporte continuo; identificar superusuarios; medir adopción y satisfacción.
**Severity_Level:** High
**Related_Patterns:** PRC-072, PRC-073, PRC-074, PRC-082, PRC-125

### PRC-077
**Pattern_Name:** Automatización de Procesos Erróneos (Digitalizar el Caos)
**Category:** Automatización
**Description:** Se automatizan procesos que son ineficientes o defectuosos, "digitalizando el caos" y haciendo que los problemas se ejecuten más rápido pero sigan siendo problemas.
**Observable_Symptoms:** Se automatizó un proceso que tenía problemas; los mismos errores ahora son más rápidos; automatización no mejoró los resultados; se aceleró un proceso ineficiente; la automatización "no sirvió para nada".
**Early_Warning_Signals:** Problemas del proceso no se resolvieron con automatización; % de mejora esperada no alcanzada; mismo número de errores pero más rápidos; procesos ineficientes antes de automatizar; indicadores clave no mejoraron.
**Typical_Causes:** Automatizar sin optimizar primero; enfoque en velocidad no en eficacia; no se analizó el proceso antes de automatizar; cultura de "primero automatizar, luego mejorar"; falta de análisis de valor.
**Business_Impact:** Automatización de procesos ineficientes; inversión desperdiciada; problemas más rápidos; no se resuelven causas raíz; equipo escéptico con automatización; mejora marginal o negativa.
**Metrics_To_Check:** Indicadores clave pre y post automatización; % de mejora en eficiencia y eficacia; errores pre y post; satisfacción del equipo; ROI real vs esperado.
**Diagnostic_Questions:** ¿Se optimizó el proceso antes de automatizar? ¿Los problemas del proceso se resolvieron? ¿La automatización mejoró los indicadores? ¿Se analizó el proceso previamente? ¿Se automatizaron procesos ineficientes?
**Recommended_Actions:** Optimizar procesos antes de automatizar (Lean antes de automatizar); analizar proceso actual; eliminar desperdicios primero; luego automatizar lo optimizado; verificar mejora post-automatización.
**Severity_Level:** High
**Related_Patterns:** PRC-048, PRC-060, PRC-068, PRC-072, PRC-082, PRC-125

### PRC-078
**Pattern_Name:** Falta de Integración entre Sistemas (Islas de Automatización)
**Category:** Automatización
**Description:** Los sistemas automatizados no están integrados entre sí (ERP, CRM, contabilidad, producción), generando duplicación de datos, retrabajo y falta de visibilidad del proceso completo.
**Observable_Symptoms:** Datos ingresados en múltiples sistemas; información inconsistente entre sistemas; reportes que no coinciden; interfaces manuales entre sistemas; falta de trazabilidad del proceso completo; reclamos de "el sistema no habla con el otro".
**Early_Warning_Signals:** Número de interfaces manuales > 3; % de datos ingresados más de una vez > 30%; diferencia de datos entre sistemas; tiempo dedicado a conciliar sistemas; % de procesos con integración automática < 40%.
**Typical_Causes:** Sistemas comprados en diferentes momentos sin plan de integración; falta de arquitectura de sistemas; departamentos que eligen sistemas sin coordinación; crecimiento no planificado; falta de inversión en integración.
**Business_Impact:** Retrabajo administrativo; datos inconsistentes; decisiones basadas en información parcial; falta de visibilidad del proceso completo; costos operativos más altos; ineficiencia general.
**Metrics_To_Check:** % de sistemas integrados; % de datos ingresados una vez; tiempo de conciliación; exactitud de datos entre sistemas; costo de interfaces manuales.
**Diagnostic_Questions:** ¿Los sistemas están integrados? ¿Se ingresan datos múltiples veces? ¿Los reportes son consistentes entre sistemas? ¿Hay interfaces manuales? ¿Hay visibilidad del proceso completo?
**Recommended_Actions:** Planificar integración de sistemas (ERP central, APIs); eliminar interfaces manuales; establecer fuente única de verdad para datos maestros; automatizar transferencias de datos; priorizar integración crítica.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-068, PRC-072, PRC-074, PRC-082, PRC-084

### PRC-079
**Pattern_Name:** Automatización de Bajo ROI por Mala Selección
**Category:** Automatización
**Description:** Se invierte en automatización en áreas equivocadas (bajo volumen, bajo impacto, baja frecuencia), obteniendo retorno bajo mientras áreas de alto potencial siguen manuales.
**Observable_Symptoms:** Automatización costosa para procesos de bajo volumen; procesos críticos siguen manuales; el ROI de automatización no se calculó antes de invertir; la automatización no liberó tiempo significativo; áreas de alto impacto no priorizadas.
**Early_Warning_Signals:** ROI de automatización < 20% anual; % de capacidad liberada por automatización < 10%; automatización de procesos con baja frecuencia o volumen; no hubo análisis de priorización; costo de automatización > beneficio anual.
**Typical_Causes:** Falta de análisis de priorización; automatizar lo "fácil" no lo de alto impacto; decisión basada en disponibilidad de presupuesto no en necesidad; no se calculó ROI antes de invertir; sesgo por "tecnología nueva".
**Business_Impact:** Inversiones con bajo retorno; recursos financieros mal asignados; áreas críticas siguen ineficientes; justificación difícil para futuras inversiones; frustración por falta de resultados.
**Metrics_To_Check:** ROI por proyecto de automatización; % de capacidad liberada; costo vs beneficio; priorización de proyectos; satisfacción con resultados.
**Diagnostic_Questions:** ¿Se calculó el ROI antes de automatizar? ¿Se priorizaron los procesos de alto impacto? ¿La automatización liberó tiempo significativo? ¿Hay áreas críticas sin automatizar? ¿El retorno justifica la inversión?
**Recommended_Actions:** Establecer criterios de priorización (volumen, frecuencia, impacto, facilidad); calcular ROI antes de invertir; priorizar procesos de alto impacto; medir resultados post-implementación; revisar portafolio de automatización.
**Severity_Level:** Medium
**Related_Patterns:** PRC-024, PRC-072, PRC-073, PRC-074, PRC-082, PRC-117

### PRC-080
**Pattern_Name:** Automatización sin Redundancia ni Plan de Contingencia
**Category:** Automatización
**Description:** Los procesos automatizados no tienen respaldo manual ni plan de contingencia en caso de falla del sistema, por lo que cualquier problema tecnológico detiene completamente la operación.
**Observable_Symptoms:** Cuando el sistema cae, la operación se detiene; no hay procedimiento manual de respaldo; el equipo no sabe cómo operar sin el sistema; dependencia total de la tecnología; caídas del sistema causan parálisis.
**Early_Warning_Signals:** % de procesos automatizados sin procedimiento manual de respaldo > 50%; tiempo de recuperación ante falla (RTO) > 4 horas; frecuencia de caídas; % de tiempo que el sistema no está disponible; el equipo no conoce proceso manual.
**Typical_Causes:** Falta de plan de contingencia; asumir que el sistema nunca falla; no documentar procesos manuales alternativos; no capacitar en procedimiento de contingencia; sistemas sin redundancia.
**Business_Impact:** Parálisis operativa ante fallas; pérdida de producción; clientes no atendidos; ingresos perdidos; datos no registrados; caos operativo.
**Metrics_To_Check:** % de procesos con plan de contingencia; tiempo de recuperación (RTO); disponibilidad del sistema; % de caídas con impacto operativo; % del equipo capacitado en contingencia.
**Diagnostic_Questions:** ¿Hay plan de contingencia si la automatización falla? ¿El equipo sabe operar sin el sistema? ¿Cuánto tiempo se recupera de una falla? ¿Hay redundancia? ¿La operación se detiene si el sistema cae?
**Recommended_Actions:** Desarrollar planes de contingencia; documentar procedimientos manuales alternativos; capacitar al equipo en contingencia; implementar redundancia en sistemas críticos; probar planes periódicamente.
**Severity_Level:** High
**Related_Patterns:** PRC-025, PRC-053, PRC-071, PRC-072, PRC-082, PRC-106

### PRC-081
**Pattern_Name:** Falta de Automatización en Reportes y Dashboard
**Category:** Automatización
**Description:** Los reportes gerenciales y dashboards se preparan manualmente (Excel, copiar-pegar de sistemas) consumiendo horas del equipo, cuando podrían automatizarse para entregar información en tiempo real.
**Observable_Symptoms:** Reportes hechos a mano cada semana/mes; horas dedicadas a preparar reportes; la información llega tarde para tomar decisiones; datos copiados manualmente entre sistemas; reportes que ya están disponibles en el sistema pero se re-hacen en Excel.
**Early_Warning_Signals:** Horas/semana dedicadas a reportes manuales > 8; % de reportes automatizados < 30%; reportes disponibles con retraso > 2 días; % de datos copiados manualmente; satisfacción con calidad y oportunidad de reportes.
**Typical_Causes:** Desconocimiento de herramientas de BI; falta de integración de sistemas; cultura de "siempre se hizo así en Excel"; gerencia no exige reportes automatizados; falta de habilidades técnicas.
**Business_Impact:** Horas de trabajo desperdiciadas; decisiones basadas en información desactualizada; errores en reportes manuales; capacidad analítica limitada; falta de visibilidad en tiempo real.
**Metrics_To_Check:** % de reportes automatizados; horas dedicadas a reportes manuales; oportunidad de reportes; errores en reportes; satisfacción de la gerencia.
**Diagnostic_Questions:** ¿Los reportes se preparan manualmente? ¿Cuántas horas se dedican a reportes? ¿La información está disponible en tiempo real? ¿Hay errores en reportes manuales? ¿Se han evaluado herramientas de BI?
**Recommended_Actions:** Implementar herramientas de BI (Power BI, Tableau o gratuitas); automatizar reportes recurrentes; crear dashboards en tiempo real; capacitar al equipo en herramientas; eliminar reportes manuales.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-068, PRC-072, PRC-074, PRC-082, PRC-125

### PRC-082
**Pattern_Name:** Cultura Organizacional que Resiste la Automatización
**Category:** Automatización
**Description:** Existe resistencia cultural a la automatización, ya sea por miedo a perder el empleo, por comodidad con métodos actuales o por falta de confianza en la tecnología, bloqueando iniciativas de mejora.
**Observable_Symptoms:** El equipo se opone a nuevas herramientas; frases como "esto siempre funcionó así"; miedo a que la automatización reemplace personas; métodos manuales persisten incluso con herramientas disponibles; sabotaje pasivo de iniciativas.
**Early_Warning_Signals:** % de adopción de herramientas < 30% después de 6 meses; resistencia abierta a nuevas tecnologías; % del equipo que apoya la automatización < 50%; rotación en proyectos de automatización; proyectos de automatización abandonados.
**Typical_Causes:** Cultura organizacional conservadora; falta de comunicación sobre beneficios; miedo al cambio; experiencias previas negativas; liderazgo que no promueve el cambio; falta de incentivos para adoptar tecnología.
**Business_Impact:** Proyectos de automatización fallan; inversiones desperdiciadas; empresa pierde competitividad; equipo con habilidades obsoletas; eficiencia no mejora; brecha tecnológica creciente.
**Metrics_To_Check:** % de adopción de herramientas; satisfacción con tecnología; % de procesos manuales vs automatizados; rotación en áreas afectadas; éxito de proyectos de automatización.
**Diagnostic_Questions:** ¿Hay resistencia a la automatización? ¿El equipo apoya las iniciativas tecnológicas? ¿Las nuevas herramientas se adoptan? ¿Hay miedo al cambio? ¿La cultura organizacional es favorable a la innovación?
**Recommended_Actions:** Comunicar beneficios de automatización (no reemplaza, potencia); involucrar al equipo en selección e implementación; celebrar éxitos tempranos; capacitar y mostrar resultados; liderazgo debe predicar con el ejemplo.
**Severity_Level:** Critical
**Related_Patterns:** PRC-042, PRC-066, PRC-072, PRC-074, PRC-076, PRC-125


## Estandarización

### PRC-083
**Pattern_Name:** Procesos No Estandarizados (Cada Quien Hace a su Manera)
**Category:** Estandarización
**Description:** Los procesos no tienen un método estándar definido; cada operador ejecuta el trabajo de manera diferente, generando variabilidad en resultados, calidad y productividad.
**Observable_Symptoms:** Cada quien hace el trabajo diferente; no hay un "mejor método"; la calidad y velocidad varían por persona; hay discusiones sobre cómo se debe hacer; nuevos empleados aprenden "mirando" sin un método definido.
**Early_Warning_Signals:** % de procesos estandarizados < 30%; variabilidad de resultados entre operadores > 20%; tiempo de ciclo variable; método no documentado; operadores con diferencias significativas de productividad.
**Typical_Causes:** Crecimiento orgánico sin estandarizar; cultura artesanal; falta de disciplina; supervisión no exige estándar; no se ha definido el mejor método.
**Business_Impact:** Calidad inconsistente; productividad variable; dificultad para entrenar; dependencia de operadores clave; imposibilidad de escalar; problemas recurrentes no resueltos.
**Metrics_To_Check:** % de procesos estandarizados; variabilidad de resultados entre operadores; % de procesos documentados; cumplimiento del estándar; tendencia.
**Diagnostic_Questions:** ¿Los procesos están estandarizados? ¿Todos hacen el trabajo igual? ¿Hay un método documentado? ¿Se cumple el estándar? ¿La variabilidad entre operadores es alta?
**Recommended_Actions:** Definir el mejor método para cada proceso (involucrando a operadores); documentar instrucciones de trabajo; capacitar en el estándar; verificar cumplimiento; revisar y mejorar el estándar periódicamente.
**Severity_Level:** Critical
**Related_Patterns:** PRC-011, PRC-014, PRC-039, PRC-049, PRC-084, PRC-089, PRC-125

### PRC-084
**Pattern_Name:** Estandarización Solo en Papel (No se Cumple)
**Category:** Estandarización
**Description:** Los procesos están documentados y estandarizados en papel, pero en la práctica no se sigue el estándar; cada quien sigue haciendo lo que quiere, ignorando la documentación.
**Observable_Symptoms:** Procedimientos documentados pero no seguidos; el equipo no consulta los documentos; los procedimientos están desactualizados; se hace diferente a lo documentado; auditorías encuentran no conformidades recurrentes.
**Early_Warning_Signals:** % de cumplimiento del estándar < 60%; % de procedimientos desactualizados > 40%; frecuencias de no conformidades en auditorías; equipo no conoce el estándar documentado; % de operadores que siguen el estándar.
**Typical_Causes:** Estandarización impuesta sin participación del equipo; procedimientos no actualizados; falta de verificación de cumplimiento; supervisión no exige el estándar; estándar no práctico o difícil de seguir.
**Business_Impact:** Estandarización inútil; calidad inconsistente; problemas recurrentes; auditorías fallidas; certificaciones en riesgo; desperdicio de recursos en documentación que no se usa.
**Metrics_To_Check:** % de cumplimiento del estándar; % de procedimientos actualizados; resultados de auditorías; % del equipo que conoce el estándar; satisfacción con el estándar.
**Diagnostic_Questions:** ¿El estándar documentado se cumple? ¿El equipo conoce el estándar? ¿Está actualizado? ¿Es práctico? ¿La supervisión exige cumplimiento?
**Recommended_Actions:** Involucrar al equipo en creación/revisión del estándar; hacer el estándar práctico y visual; verificar cumplimiento regularmente; actualizar periódicamente; dar ejemplo desde la supervisión; reconocer cumplimiento.
**Severity_Level:** High
**Related_Patterns:** PRC-038, PRC-049, PRC-083, PRC-085, PRC-089, PRC-117

### PRC-085
**Pattern_Name:** Estandarización que Inhibe la Mejora Continua
**Category:** Estandarización
**Description:** El estándar se aplica de manera rígida y no se revisa ni mejora, convirtiéndose en una camisa de fuerza que impide la mejora continua y la adaptación a cambios.
**Observable_Symptoms:** El estándar no se revisa nunca; las mejoras no se incorporan al estándar; el equipo no propone cambios porque "el estándar dice así"; el estándar se vuelve obsoleto; procedimientos que nadie sigue porque están desactualizados.
**Early_Warning_Signals:** Tiempo desde última revisión del estándar > 12 meses; % de estándares sin revisión; % de sugerencias de mejora no incorporadas; % de equipo que considera el estándar una traba; estándar no refleja la práctica actual.
**Typical_Causes:** Cultura de "estándar es sagrado"; falta de proceso de revisión; burocracia excesiva para cambiar el estándar; miedo a perder control; falta de involucramiento del equipo en mejora.
**Business_Impact:** Estándar obsoleto; mejoras no se implementan; equipo desmotivado; adaptación lenta a cambios; competitividad reducida; procesos no mejoran.
**Metrics_To_Check:** Frecuencia de revisión de estándares; % de estándares actualizados; % de sugerencias implementadas en el estándar; % del equipo que participa en mejora del estándar.
**Diagnostic_Questions:** ¿El estándar se revisa periódicamente? ¿Las mejoras se incorporan al estándar? ¿El equipo puede proponer cambios? ¿El estándar es una herramienta de mejora o una traba? ¿Está actualizado?
**Recommended_Actions:** Establecer revisión periódica del estándar; crear mecanismo para proponer cambios; capacitar en que el estándar es la base para mejorar, no un fin; celebrar mejoras al estándar; involucrar al equipo.
**Severity_Level:** High
**Related_Patterns:** PRC-083, PRC-084, PRC-089, PRC-117, PRC-125, PRC-126

### PRC-086
**Pattern_Name:** Falta de Estandarización en Compras
**Category:** Estandarización
**Description:** Las compras se realizan sin un proceso estandarizado (sin especificaciones claras, sin evaluación de proveedores, sin órdenes de compra), generando variabilidad en calidad, precio y condiciones.
**Observable_Symptoms:** Compras sin orden de compra; especificaciones verbales; precios diferentes por el mismo producto; proveedores no evaluados; compras de emergencia frecuentes; cada quien compra donde quiere.
**Early_Warning_Signals:** % de compras con orden de compra < 50%; % de productos con especificaciones documentadas < 40%; variabilidad de precios > 10%; % de compras de emergencia > 20%; número de proveedores por producto excesivo.
**Typical_Causes:** Falta de proceso de compras estandarizado; cultura de "comprar rápido"; descentralización de compras; falta de especificaciones; no hay catálogo de proveedores aprobados.
**Business_Impact:** Calidad variable; precios no óptimos; falta de control de gastos; compras de emergencia más costosas; riesgo de proveedores no confiables; sobreprecio.
**Metrics_To_Check:** % de compras con orden de compra; % de especificaciones documentadas; variabilidad de precios; % de compras de emergencia; ahorro por estandarización.
**Diagnostic_Questions:** ¿Las compras siguen un proceso estandarizado? ¿Hay especificaciones claras? ¿Los proveedores están evaluados? ¿Hay compras de emergencia frecuentes? ¿Los precios son consistentes?
**Recommended_Actions:** Estandarizar proceso de compras (solicitud→aprobación→orden); documentar especificaciones; crear catálogo de proveedores aprobados; centralizar compras; reducir compras de emergencia.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-007, PRC-041, PRC-083, PRC-087, PRC-100

### PRC-087
**Pattern_Name:** Falta de Estandarización en Atención al Cliente
**Category:** Estandarización
**Description:** La atención al cliente no sigue un proceso estandarizado; cada asesor responde de manera diferente, generando experiencia inconsistente para el cliente y dificultad para medir calidad de servicio.
**Observable_Symptoms:** Clientes reciben respuestas diferentes al mismo problema; algunos asesores son excelentes, otros malos; no hay guión ni protocolo; la calidad depende de quién atiende; quejas por inconsistencia en atención.
**Early_Warning_Signals:** % de interacciones que siguen protocolo < 40%; variabilidad en satisfacción por asesor > 20 puntos; % de clientes que reportan inconsistencia; cumplimiento de protocolo; NPS variable por asesor.
**Typical_Causes:** Falta de protocolo de atención; capacitación inconsistente; cada asesor desarrolla su propio estilo; supervisión no monitorea consistencia; cultura de "cada quien como quiera".
**Business_Impact:** Experiencia inconsistente del cliente; clientes insatisfechos; dificultad para escalar; NPS variable; problemas recurrentes no resueltos; imagen de marca inconsistente.
**Metrics_To_Check:** % de cumplimiento de protocolo; NPS por asesor; variabilidad de satisfacción; % de llamadas/interacciones monitoreadas; tiempo de atención.
**Diagnostic_Questions:** ¿La atención al cliente está estandarizada? ¿Hay protocolo? ¿Todos atienden igual? ¿La satisfacción varía por asesor? ¿Se monitorea la calidad de atención?
**Recommended_Actions:** Desarrollar protocolo de atención al cliente (saludo, manejo de objeciones, cierre); capacitar en el protocolo; monitorear cumplimiento; medir satisfacción por asesor; reconocer buena atención.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-039, PRC-045, PRC-083, PRC-088, PRC-089

### PRC-088
**Pattern_Name:** Estandarización en Silos (Cada Área Estandariza sin Coordinación)
**Category:** Estandarización
**Description:** Cada departamento estandariza sus procesos de manera independiente, sin coordinación con las otras áreas, generando interfaces inconsistentes y problemas en los puntos de contacto entre áreas.
**Observable_Symptoms:** Documentos que cada área llena diferente; formatos incompatibles entre áreas; información que se pierde en la transición; "ese formato no me sirve"; cada área tiene su propia nomenclatura; falta de estándar común.
**Early_Warning_Signals:** Número de formatos diferentes para la misma información; % de interfaces entre áreas sin estandarizar; errores en transferencias entre áreas; % de datos que se re-ingresan; quejas por "formatos que no sirven".
**Typical_Causes:** Departamentos autónomos sin coordinación; falta de visión de proceso transversal; cada área define sus estándares sin consultar; sistemas no integrados; cultura de silos.
**Business_Impact:** Problemas en interfaces; retrabajo por formatos incompatibles; información perdida; clientes internos insatisfechos; eficiencia general reducida; procesos transversales deficientes.
**Metrics_To_Check:** % de procesos transversales estandarizados; % de formatos comunes; errores en interfaces; tiempo de transferencia entre áreas; satisfacción con procesos compartidos.
**Diagnostic_Questions:** ¿Hay estándares comunes entre áreas? ¿Los formatos son compatibles? ¿La información fluye sin problemas? ¿Cada área tiene sus propios estándares sin coordinación? ¿Los procesos transversales son eficientes?
**Recommended_Actions:** Establecer estándares transversales que crucen áreas; crear equipos multifuncionales para definir procesos compartidos; unificar formatos y nomenclaturas; integrar sistemas; revisar interfaces.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-051, PRC-068, PRC-078, PRC-083, PRC-084

### PRC-089
**Pattern_Name:** Mejores Prácticas No Compartidas No Estandarizadas
**Category:** Estandarización
**Description:** Existen operadores o áreas que tienen un desempeño superior (mejores prácticas), pero ese conocimiento no se captura, estandariza ni comparte con el resto de la organización.
**Observable_Symptoms:** Algunos operadores siempre rinden mejor; ciertos turnos tienen mejor productividad; el "secreto" del mejor desempeño no se conoce; los nuevos aprenden por ensayo y error; el conocimiento del mejor operador se pierde si se va.
**Early_Warning_Signals:** Diferencia de productividad entre mejor y peor operador > 30%; % de mejores prácticas documentadas < 20%; no hay proceso para compartir conocimiento; rotación de mejores operadores pierde know-how; % de operadores en nivel superior de desempeño.
**Typical_Causes:** Falta de proceso de captura de conocimiento; cultura de "cada quien sabe lo suyo"; no se mide desempeño individual; supervisión no identifica mejores prácticas; falta de incentivos para compartir.
**Business_Impact:** Conocimiento no aprovechado; desempeño promedio no mejora; dependencia de personas clave; rotación pérdida de know-how; dificultad para entrenar nuevos; productividad general baja.
**Metrics_To_Check:** Diferencia de productividad entre operadores; % de mejores prácticas documentadas; % de operadores que aplican mejores prácticas; retención de conocimiento; curva de aprendizaje de nuevos.
**Diagnostic_Questions:** ¿Hay operadores que rinden mejor? ¿Se sabe por qué? ¿Ese conocimiento se comparte? ¿Está documentado? ¿Se capacita a otros en las mejores prácticas?
**Recommended_Actions:** Identificar mejores prácticas (operadores de alto desempeño); documentar el método; estandarizar como nuevo estándar; capacitar a todos; reconocer a los que comparten conocimiento.
**Severity_Level:** Medium
**Related_Patterns:** PRC-039, PRC-066, PRC-083, PRC-084, PRC-117, PRC-119, PRC-125

### PRC-090
**Pattern_Name:** Falta de Estandarización en Procesos de Calidad
**Category:** Estandarización
**Description:** Los procesos de control de calidad no están estandarizados (dónde, cuándo, cómo inspeccionar; qué tolerancias aplicar; cómo registrar), generando calidad inconsistente y datos no comparables.
**Observable_Symptoms:** Puntos de inspección varían según operador; tolerancias no definidas o no conocidas; muestreo no estandarizado; registros de calidad incompletos; criterios de aprobación/rechazo subjetivos; inspección inconsistente.
**Early_Warning_Signals:** % de procesos de calidad estandarizados < 50%; % de puntos de inspección definidos; % de registros de calidad completos; criterios de aceptación documentados; variabilidad en resultados de inspección entre inspectores.
**Typical_Causes:** Falta de procedimientos de inspección; inspectores no capacitados en el mismo estándar; tolerancias no documentadas; criterios subjetivos; muestreo no definido estadísticamente.
**Business_Impact:** Calidad inconsistente; datos de calidad no confiables; decisiones basadas en información incorrecta; defectos pasan o productos buenos se rechazan; costos de calidad más altos.
**Metrics_To_Check:** % de procesos de calidad estandarizados; variabilidad entre inspectores; % de registros completos; exactitud de inspección; confiabilidad de datos de calidad.
**Diagnostic_Questions:** ¿Los procesos de calidad están estandarizados? ¿Los criterios de aceptación son claros? ¿Los inspectores aplican los mismos criterios? ¿Los registros de calidad son consistentes? ¿Los datos de calidad son confiables?
**Recommended_Actions:** Estandarizar procesos de calidad (qué, cómo, cuándo, quién inspecciona); definir tolerancias y criterios; capacitar inspectores; estandarizar registros; auditar consistencia.
**Severity_Level:** High
**Related_Patterns:** PRC-036, PRC-037, PRC-038, PRC-039, PRC-083, PRC-084

### PRC-091
**Pattern_Name:** Estandarización de Procesos Críticos No Priorizada
**Category:** Estandarización
**Description:** La empresa intenta estandarizar todos los procesos al mismo tiempo, sin priorizar los críticos, dispersando esfuerzos y logrando poco avance real en los procesos que más impacto tienen.
**Observable_Symptoms:** Proyecto de estandarización avanza lento en todos lados; procesos críticos y no críticos reciben la misma atención; no hay criterio de priorización; el equipo está abrumado; procesos clave siguen sin estandarizar.
**Early_Warning_Signals:** % de procesos críticos estandarizados < 30% mientras se trabaja en todos; tiempo desde inicio sin avance significativo; % de procesos de alto impacto estandarizados; equipo desbordado; quejas de "estandarizan todo menos lo importante".
**Typical_Causes:** Falta de priorización por impacto; querer hacer todo al mismo tiempo; presión por estandarizar "todos los procesos"; falta de criterio ABC; proyecto sin foco.
**Business_Impact:** Esfuerzo disperso; resultados lentos; procesos críticos siguen sin estandarizar; equipo desmotivado; inversión de tiempo sin retorno visible; frustración.
**Metrics_To_Check:** % de procesos críticos estandarizados; % de procesos totales estandarizados; tiempo de avance; % de impacto logrado; satisfacción del equipo.
**Diagnostic_Questions:** ¿Se priorizan los procesos críticos? ¿O se intenta estandarizar todo a la vez? ¿Hay criterio de priorización? ¿Los procesos de alto impacto están estandarizados? ¿El equipo está disperso?
**Recommended_Actions:** Clasificar procesos por criticidad (impacto en cliente, costo, calidad); priorizar procesos críticos; estandarizar por etapas; comunicar avances; celebrar logros en procesos clave.
**Severity_Level:** High
**Related_Patterns:** PRC-024, PRC-083, PRC-084, PRC-117, PRC-125, PRC-126

### PRC-092
**Pattern_Name:** Estandarización que Ignora la Voz del Operador
**Category:** Estandarización
**Description:** El estándar es definido solo por supervisores/gerencia sin consultar a los operadores que ejecutan el trabajo, resultando en un estándar poco práctico que no se adopta.
**Observable_Symptoms:** El estándar fue impuesto desde arriba; los operadores dicen "los que hacen el trabajo somos nosotros"; el estándar no refleja la realidad del día a día; procedimientos que entorpecen el trabajo; el equipo ignora el estándar.
**Early_Warning_Signals:** % de operadores que participaron en definir el estándar < 20%; % de cumplimiento del estándar; % de operadores que considera el estándar práctico; quejas sobre el estándar; % de estándar que refleja la práctica real.
**Typical_Causes:** Enfoque jerárquico; subestimación del conocimiento operativo; rapidez en imponer vs construir; cultura de "los jefes saben"; falta de metodología participativa.
**Business_Impact:** Estándar no práctico; baja adopción; resistencia al estándar; mejora no lograda; recursos desperdiciados en crear estándar que no se usa; relación tensa entre supervisión y operadores.
**Metrics_To_Check:** % de participación de operadores en creación; % de cumplimiento; % de operadores que considera el estándar práctico; % de sugerencias incorporadas; clima laboral.
**Diagnostic_Questions:** ¿Los operadores participaron en crear el estándar? ¿Consideran el estándar práctico? ¿Se adoptó el estándar? ¿Refleja la realidad del trabajo? ¿Hay resistencia?
**Recommended_Actions:** Involucrar a operadores en diseño del estándar; preguntar su opinión sobre mejor método; validar el estándar con ellos; ajustar según feedback; reconocer su contribución.
**Severity_Level:** High
**Related_Patterns:** PRC-042, PRC-066, PRC-083, PRC-084, PRC-089, PRC-117, PRC-125


## Capacidad Instalada

### PRC-093
**Pattern_Name:** Capacidad Instalada Real Desconocida
**Category:** Capacidad Instalada
**Description:** La empresa no conoce su capacidad real de producción, ni la utiliza como referencia para planificar, aceptar pedidos o identificar limitaciones.
**Observable_Symptoms:** Se aceptan pedidos sin saber si se pueden cumplir; no se sabe cuánto se puede producir; se trabaja "al máximo" sin saber cuál es el máximo; hay promesas incumplidas a clientes; capacidad se confunde con disponibilidad teórica.
**Early_Warning_Signals:** Capacidad real no calculada; % de utilización de capacidad desconocido; aceptación de pedidos sin verificar capacidad; entregas tardías frecuentes; % de capacidad teórica vs real > 30% de diferencia.
**Typical_Causes:** Falta de medición de capacidad; confundir capacidad teórica con real; no considerar pérdidas (mantenimiento, set-up, calidad); planificación sin datos de capacidad; crecimiento no planificado.
**Business_Impact:** Pedidos aceptados que no se pueden cumplir; entregas tardías; clientes insatisfechos; sobrecarga del equipo; cuellos de botella no identificados; estrés organizacional.
**Metrics_To_Check:** Capacidad real (unidades/turno); % de utilización; % de eficiencia (real vs teórica); OEE; % de pedidos entregados a tiempo.
**Diagnostic_Questions:** ¿Se conoce la capacidad real de producción? ¿Se utiliza para planificar? ¿Se aceptan pedidos sin verificar capacidad? ¿Hay sobreventa? ¿La capacidad teórica es realista?
**Recommended_Actions:** Calcular capacidad real de cada proceso (unidades/turno considerando pérdidas); medir utilización y eficiencia; usar capacidad real para planificar; establecer límites de aceptación de pedidos.
**Severity_Level:** Critical
**Related_Patterns:** PRC-024, PRC-029, PRC-030, PRC-071, PRC-094, PRC-096, PRC-108

### PRC-094
**Pattern_Name:** Capacidad Subutilizada (Ociosidad)
**Category:** Capacidad Instalada
**Description:** La capacidad instalada está significativamente subutilizada, con equipos y personas ociosas gran parte del tiempo, generando costos fijos distribuidos en menos producción.
**Observable_Symptoms:** Máquinas detenidas largos períodos; operadores sin trabajo; turnos parciales; capacidad > demanda consistentemente; costos fijos altos por unidad; se paga capacidad que no se usa.
**Early_Warning_Signals:** % de utilización de capacidad < 60%; % de tiempo ocioso de equipos > 30%; costo fijo unitario alto; % de capacidad instalada vs demanda; horas extras vs capacidad ociosa (paradoja).
**Typical_Causes:** Demanda insuficiente; sobreinversión en capacidad; falta de flexibilidad para ajustar capacidad a demanda; equipos sobredimensionados; falta de planificación de capacidad; mix de productos no rentable.
**Business_Impact:** Costos fijos altos por unidad; rentabilidad baja; retorno de inversión bajo en activos; riesgo financiero; competitividad reducida; desperdicio de recursos.
**Metrics_To_Check:** % de utilización de capacidad; costo fijo por unidad; capacidad vs demanda; horas de operación vs horas disponibles; OEE (disponibilidad).
**Diagnostic_Questions:** ¿La capacidad está subutilizada? ¿Hay equipos y personas ociosas? ¿Los costos fijos unitarios son altos? ¿La demanda justifica la capacidad? ¿Se puede ajustar capacidad a demanda?
**Recommended_Actions:** Alinear capacidad con demanda; considerar reducción de turnos o jornadas; vender capacidad excedente; diversificar productos; no invertir en más capacidad sin análisis; flexible capacity (horarios, subcontratación).
**Severity_Level:** High
**Related_Patterns:** PRC-013, PRC-016, PRC-024, PRC-029, PRC-061, PRC-071, PRC-093

### PRC-095
**Pattern_Name:** Capacidad Limitada por Cuello de Botella No Gestionado
**Category:** Capacidad Instalada
**Description:** La capacidad total del sistema está limitada por un cuello de botella que no se gestiona activamente, restringiendo la producción de toda la planta y generando subutilización en otros procesos.
**Observable_Symptoms:** Un proceso siempre está retrasado; los demás procesos tienen que esperar; WIP se acumula antes del cuello de botella; después del cuello de botella hay capacidad ociosa; toda la línea depende de un proceso.
**Early_Warning_Signals:** % de utilización de cuello de botella > 95%; WIP acumulado antes del cuello de botella; capacidad ociosa después; lead time controlado por cuello de botella; % de tiempo que el cuello de botella determina la producción total.
**Typical_Causes:** Cuello de botella no identificado; no se protege la capacidad del cuello de botella; no se optimiza el cuello de botella; se deja que el cuello de botella espere por materiales o mantenimiento; falta de teoría de restricciones.
**Business_Impact:** Producción total limitada por un proceso; capacidad desbalanceada; lead times largos; eficiencia general baja; entregas tardías; estrés en el cuello de botella y sus operadores.
**Metrics_To_Check:** % de utilización del cuello de botella; producción total del sistema; WIP antes del cuello de botella; tiempo de espera en cuello de botella; throughput del sistema.
**Diagnostic_Questions:** ¿Cuál es el cuello de botella? ¿Se gestiona activamente? ¿Se protege su capacidad? ¿Se optimiza? ¿La producción total depende de ese proceso?
**Recommended_Actions:** Identificar el cuello de botella; proteger su capacidad (no dejar que espere); optimizar el cuello de botella; subordinar el resto al cuello de botella; elevar la capacidad del cuello de botella (inversión).
**Severity_Level:** Critical
**Related_Patterns:** PRC-024, PRC-025, PRC-026, PRC-029, PRC-030, PRC-032, PRC-093, PRC-096

### PRC-096
**Pattern_Name:** Expansión de Capacidad sin Análisis de Demanda
**Category:** Capacidad Instalada
**Description:** La empresa invierte en aumentar capacidad (máquinas, personal, espacio) sin un análisis riguroso de demanda actual y futura, arriesgando sobreinversión y capacidad ociosa.
**Observable_Symptoms:** Se compra maquinaria que luego no se usa a plena capacidad; se contrata personal que luego no hay trabajo suficiente; inversiones en capacidad que no mejoran el throughput; expansión sin estudio de mercado; decisiones basadas en optimismo.
**Early_Warning_Signals:** % de capacidad nueva utilizada < 60% después de 6 meses; inversión en capacidad > 2x el crecimiento de demanda; % de capacidad ociosa nueva; ROI de expansión < esperado; decisiones sin análisis de demanda.
**Typical_Causes:** Decisiones de inversión sin datos; optimismo gerencial; "comprar antes de que suban los precios"; presión por crecimiento; falta de planificación estratégica; vendedores de equipos persuasivos.
**Business_Impact:** Capital inmovilizado en activos subutilizados; costos fijos altos; rentabilidad baja; riesgo financiero; capacidad de pago afectada; retorno de inversión deficiente.
**Metrics_To_Check:** % de utilización de nueva capacidad; ROI de inversión en capacidad; % de crecimiento de demanda vs capacidad; costo fijo unitario post-expansión; flujo de caja.
**Diagnostic_Questions:** ¿La expansión de capacidad se basó en datos de demanda? ¿Se utiliza la nueva capacidad? ¿El ROI es el esperado? ¿Hay sobrecapacidad? ¿Se analizaron alternativas antes de invertir?
**Recommended_Actions:** Realizar análisis de demanda antes de expandir; considerar alternativas (turnos extras, subcontratar, mejorar eficiencia) antes de invertir; calcular ROI con escenarios; planificar expansión gradual.
**Severity_Level:** Critical
**Related_Patterns:** PRC-016, PRC-029, PRC-071, PRC-093, PRC-094, PRC-108, PRC-110

### PRC-097
**Pattern_Name:** Capacidad de Almacenamiento Insuficiente
**Category:** Capacidad Instalada
**Description:** La capacidad de almacenamiento (materia prima, WIP, producto terminado) es insuficiente, generando desorden, pérdidas, riesgos de seguridad y dificultad para gestionar inventarios.
**Observable_Symptoms:** Pasillos obstruidos; materiales apilados en cualquier lugar; productos terminados sin espacio; almacén desbordado; dificultad para encontrar materiales; condiciones inadecuadas de almacenamiento.
**Early_Warning_Signals:** % de capacidad de almacenamiento utilizada > 90% constantemente; pasillos obstruidos; % de materiales en ubicaciones no designadas; % de merma por almacenamiento deficiente; quejas de operadores por falta de espacio.
**Typical_Causes:** Crecimiento sin expandir almacén; inventarios excesivos; mala distribución del almacén; falta de estanterías adecuadas; layout ineficiente; no se usa almacenamiento vertical.
**Business_Impact:** Desorden; pérdida de materiales; dificultad para encontrar ítems; condiciones inseguras; lead times de picking largos; inventario no controlado; riesgo de accidentes.
**Metrics_To_Check:** % de capacidad de almacén utilizada; % de materiales en ubicación designada; tiempo de picking; % de merma por almacenamiento; nivel de desorden.
**Diagnostic_Questions:** ¿Hay suficiente capacidad de almacenamiento? ¿Está organizada? ¿Hay materiales fuera de lugar? ¿Hay dificultad para encontrar materiales? ¿Hay condiciones inseguras por falta de espacio?
**Recommended_Actions:** Optimizar layout del almacén (vertical, estanterías); reducir inventarios (Lean); clasificar ABC para ubicación; considerar expansión de almacén si es necesario; implementar 5S.
**Severity_Level:** High
**Related_Patterns:** PRC-007, PRC-015, PRC-028, PRC-064, PRC-070, PRC-086, PRC-095

### PRC-098
**Pattern_Name:** Capacidad de Personal No Dimensionada
**Category:** Capacidad Instalada
**Description:** La cantidad de personal no está dimensionada según la carga de trabajo, generando sobrecarga en unos períodos y ociosidad en otros, sin flexibilidad para ajustar.
**Observable_Symptoms:** Picos de trabajo con horas extras; en otros momentos personal ocioso; rotación alta por sobrecarga; quejas de "no damos abasto" seguido de "no hay trabajo"; contrataciones reactivas.
**Early_Warning_Signals:** % de horas extras sobre horas regulares > 10%; % de personal ocioso en períodos valle > 20%; rotación de personal > 20% anual; % de variabilidad de carga de trabajo; tiempo de contratación > demanda de personal.
**Typical_Causes:** Plantilla fija para demanda variable; falta de flexibilidad laboral; mala planificación de personal; no se usa personal temporal/part-time; cultura de "siempre contratar".
**Business_Impact:** Costos de horas extras; rotación alta; clima laboral negativo; capacidad no ajustada a demanda; costos fijos de personal altos; productividad variable.
**Metrics_To_Check:** % de horas extras; % de utilización de personal; rotación; costo de personal como % de ventas; flexibilidad de plantilla.
**Diagnostic_Questions:** ¿El personal está dimensionado según la carga? ¿Hay horas extras frecuentes? ¿En otros momentos hay ociosidad? ¿Hay flexibilidad para ajustar? ¿La rotación es alta?
**Recommended_Actions:** Dimensionar plantilla según carga promedio con flexibilidad (personal temporal, horas extras planificadas, turnos); implementar planning de personal; polifuncionalidad; ajustar capacidad de personal a demanda.
**Severity_Level:** High
**Related_Patterns:** PRC-012, PRC-013, PRC-016, PRC-094, PRC-099, PRC-108, PRC-119

### PRC-099
**Pattern_Name:** Falta de Polifuncionalidad del Personal
**Category:** Capacidad Instalada
**Description:** El personal solo sabe hacer una tarea o manejar un equipo, sin capacidad de rotar a otras funciones, generando rigidez y vulnerabilidad ante ausencias o cambios de demanda.
**Observable_Symptoms:** Si un operador falta, su proceso se detiene; no hay quién cubra otras posiciones; personas asignadas siempre al mismo puesto; curva de aprendizaje lenta; temor a rotación.
**Early_Warning_Signals:** % de personal polifuncional < 20%; número de operadores por proceso (bajo = riesgo); % de procesos sin respaldo; tiempo para cubrir ausencias; % de paradas por falta de operador.
**Typical_Causes:** Entrenamiento limitado a una tarea; cultura de "cada quien su puesto"; falta de programa de polifuncionalidad; rotación de personal impide invertir en entrenamiento; supervisión prefiere "no mover".
**Business_Impact:** Paradas por ausencias; inflexibilidad para ajustar capacidad; cuellos de botella por falta de personal calificado; vulnerabilidad ante rotación; capacidad subutilizada por rigidez.
**Metrics_To_Check:** % de personal polifuncional; % de procesos con respaldo; % de paradas por falta de operador; tiempo de adaptación a cambios de puesto; satisfacción del personal.
**Diagnostic_Questions:** ¿El personal puede hacer múltiples tareas? ¿Hay respaldo para cada puesto? ¿Qué pasa si un operador falta? ¿Hay programa de polifuncionalidad? ¿El equipo está capacitado en múltiples funciones?
**Recommended_Actions:** Implementar programa de polifuncionalidad (rotación planificada); capacitar en múltiples habilidades; crear matriz de habilidades; incentivar aprendizaje; asegurar respaldo para cada puesto crítico.
**Severity_Level:** High
**Related_Patterns:** PRC-013, PRC-014, PRC-039, PRC-089, PRC-094, PRC-098, PRC-119

### PRC-100
**Pattern_Name:** Capacidad de Proveedores No Evaluada
**Category:** Capacidad Instalada
**Description:** La empresa depende de proveedores cuya capacidad de producción se desconoce, arriesgando desabastecimientos cuando la demanda aumenta o el proveedor tiene problemas.
**Observable_Symptoms:** Proveedores que no cumplen plazos en momentos de alta demanda; calidad variable en picos de producción; rotura de stock por problemas del proveedor; no se conocen las limitaciones del proveedor; el proveedor no alerta sobre problemas de capacidad.
**Early_Warning_Signals:** % de pedidos a proveedores entregados a tiempo < 85%; % de roturas de stock por falla del proveedor; % de capacidad del proveedor utilizada; tiempo de lead time del proveedor variable; sin evaluación de capacidad de proveedores.
**Typical_Causes:** Falta de evaluación de proveedores; compras sin análisis de capacidad del proveedor; relación transaccional no colaborativa; no hay planes de contingencia; proveedor único sin respaldo.
**Business_Impact:** Desabastecimientos; producción detenida; clientes no atendidos; ventas perdidas; costos de compras de emergencia; relación tensa con proveedores.
**Metrics_To_Check:** % de entregas a tiempo de proveedores; % de roturas por proveedor; % de capacidad del proveedor evaluada; días de inventario de seguridad; % de proveedores con plan de contingencia.
**Diagnostic_Questions:** ¿Se conoce la capacidad de los proveedores? ¿Cumplen en momentos de alta demanda? ¿Hay planes de contingencia si fallan? ¿Hay proveedores de respaldo? ¿Se evalúa la capacidad de proveedores?
**Recommended_Actions:** Evaluar capacidad de proveedores críticos; desarrollar plan de contingencia; tener múltiples fuentes; establecer alertas tempranas con proveedores; colaborar para mejorar su capacidad.
**Severity_Level:** High
**Related_Patterns:** PRC-007, PRC-029, PRC-041, PRC-070, PRC-086, PRC-108

### PRC-101
**Pattern_Name:** Capacidad de Tecnología de la Información Insuficiente
**Category:** Capacidad Instalada
**Description:** La capacidad de TI (servidores, sistemas, ancho de banda, licencias) es insuficiente para la operación, generando lentitud, caídas del sistema y limitaciones al crecimiento.
**Observable_Symptoms:** Sistemas lentos; caídas frecuentes; el sistema no soporta el volumen de transacciones; usuarios esperando respuesta del sistema; procesos detenidos por TI; el sistema "se cuelga" en horas pico.
**Early_Warning_Signals:** % de disponibilidad de sistemas < 95%; % de utilización de recursos de TI > 80%; tiempo de respuesta del sistema > 3 segundos; frecuencia de caídas; % de procesos afectados por capacidad de TI.
**Typical_Causes:** Subinversión en TI; crecimiento de negocio sin escalar TI; falta de planificación de capacidad de TI; equipos obsoletos; software no escalable; ancho de banda insuficiente.
**Business_Impact:** Operación detenida por caídas; productividad reducida; usuarios frustrados; clientes afectados (página web lenta); ventas perdidas por sistema no disponible; riesgo de pérdida de datos.
**Metrics_To_Check:** Disponibilidad de sistemas; tiempo de respuesta; % de utilización de recursos; % de capacidad de TI vs demanda; número de incidentes por capacidad.
**Diagnostic_Questions:** ¿La capacidad de TI es suficiente? ¿Los sistemas son lentos o se caen? ¿El crecimiento del negocio ha superado la capacidad de TI? ¿Hay plan de escalabilidad? ¿Se invierte lo necesario en TI?
**Recommended_Actions:** Evaluar capacidad actual de TI; planificar escalabilidad; invertir en infraestructura adecuada; monitorear capacidad; implementar cloud para flexibilidad; plan de contingencia TI.
**Severity_Level:** Critical
**Related_Patterns:** PRC-072, PRC-074, PRC-078, PRC-080, PRC-081, PRC-093, PRC-110

### PRC-102
**Pattern_Name:** Estacionalidad que Sobrexige la Capacidad
**Category:** Capacidad Instalada
**Description:** La demanda estacional (temporadas altas) supera la capacidad instalada, generando sobrecarga, horas extras, calidad reducida y entregas tardías, mientras que en temporada baja la capacidad está ociosa.
**Observable_Symptoms:** Picos de producción con estrés; en temporada alta no se da abasto; en temporada baja hay ociosidad; calidad baja en temporada alta; entregas tardías en picos; rotación aumenta después de temporada.
**Early_Warning_Signals:** % de capacidad utilizada en pico > 110%; % de entregas tardías en temporada alta > 20%; % de horas extras en temporada > 15%; % de capacidad ociosa en valle < 50%; % de rotación post-temporada; % de defectos en pico vs valle.
**Typical_Causes:** Capacidad dimensionada para demanda promedio; falta de flexibilidad; no se planifica la temporada; no se usa personal temporal; inventario no se acumula previamente; cultura de "aguantar".
**Business_Impact:** Sobrecostos en temporada alta; calidad reducida; clientes insatisfechos; rotación post-temporada; estrés del equipo; capacidad ociosa en valle; rentabilidad afectada.
**Metrics_To_Check:** Capacidad utilizada en pico vs valle; % de entregas tardías por temporada; % de horas extras; % de defectos por temporada; % de rotación post-temporada.
**Diagnostic_Questions:** ¿Hay estacionalidad marcada? ¿La capacidad se ajusta? ¿Se produce para inventario antes de temporada? ¿Se usa personal temporal? ¿Hay planificación de temporada alta?
**Recommended_Actions:** Planificar temporada alta con anticipación; acumular inventario pre-temporada; usar personal temporal; subcontratar picos; planificar mantenimiento en temporada baja; nivelar producción.
**Severity_Level:** Critical
**Related_Patterns:** PRC-016, PRC-094, PRC-096, PRC-098, PRC-108, PRC-110, PRC-113


## Planificación

### PRC-103
**Pattern_Name:** Planificación de Producción Inexistente o Reactiva
**Category:** Planificación
**Description:** No existe una planificación formal de producción; se produce según van llegando los pedidos, sin orden ni priorización, generando cambios constantes, urgencias y baja eficiencia.
**Observable_Symptoms:** Se produce "lo que llega primero"; cambios de prioridad constantes; urgencias diarias; el equipo no sabe qué viene después; materiales no preparados; máquinas set-up innecesarios por cambios.
**Early_Warning_Signals:** % de producción planificada vs real < 50%; frecuencia de cambios de prioridad > 2/día; % de órdenes urgentes > 30%; horas extras por "apagar incendios"; % de cumplimiento del programa de producción.
**Typical_Causes:** Falta de proceso de planificación; cultura reactiva; ventas sin coordinar con producción; dueño toma decisiones del día a día; falta de horizonte de planificación.
**Business_Impact:** Ineficiencia operativa; cambios constantes; set-ups innecesarios; entregas tardías; estrés del equipo; capacidad desperdiciada; costos operativos altos.
**Metrics_To_Check:** % de cumplimiento del plan de producción; frecuencia de cambios de prioridad; % de órdenes urgentes; productividad; entregas a tiempo.
**Diagnostic_Questions:** ¿Hay planificación de producción? ¿Se cumple el plan? ¿Hay cambios constantes de prioridad? ¿Se produce reactivamente? ¿Hay urgencias todos los días?
**Recommended_Actions:** Implementar planificación semanal de producción; establecer horizonte de planificación; coordinar ventas-producción; proteger el plan de cambios innecesarios; medir cumplimiento.
**Severity_Level:** Critical
**Related_Patterns:** PRC-005, PRC-024, PRC-026, PRC-029, PRC-050, PRC-104, PRC-108, PRC-113

### PRC-104
**Pattern_Name:** Planificación sin Capacidad Real como Restricción
**Category:** Planificación
**Description:** La planificación ignora la capacidad real de producción, programando más de lo que se puede producir y generando retrasos, sobrecarga e incumplimiento de promesas.
**Observable_Symptoms:** El plan de producción es imposible de cumplir; se programa más de lo que se puede hacer; el equipo empieza el día ya "atrasado"; al final del día/semana el plan no se cumple; reprogramación constante.
**Early_Warning_Signals:** % de cumplimiento del plan < 70%; brecha entre capacidad real y planificada > 20%; días de atraso acumulado creciente; % de órdenes reprogramadas; productividad vs plan.
**Typical_Causes:** Planificación optimista; ventas promete sin consultar capacidad; falta de datos de capacidad real; presión por aceptar todos los pedidos; cultura de "planificar contra la pared".
**Business_Impact:** Plan imposible de cumplir; equipo desmotivado por metas inalcanzables; entregas tardías; clientes insatisfechos; reprogramación constante; caos operativo.
**Metrics_To_Check:** % de cumplimiento del plan; brecha capacidad vs plan; atraso acumulado; % de órdenes tardías; satisfacción del equipo con el plan.
**Diagnostic_Questions:** ¿El plan de producción es realista? ¿Considera la capacidad real? ¿Se cumple el plan? ¿El equipo lo considera alcanzable? ¿Se reprograma constantemente?
**Recommended_Actions:** Planificar contra capacidad real, no teórica; establecer reglas claras de aceptación de pedidos; crear planes factibles; medir cumplimiento; ajustar promesas de ventas a capacidad real.
**Severity_Level:** Critical
**Related_Patterns:** PRC-005, PRC-024, PRC-029, PRC-093, PRC-103, PRC-106, PRC-108

### PRC-105
**Pattern_Name:** Planificación Sin Visibilidad de Materiales (MRP)
**Category:** Planificación
**Description:** La planificación no considera disponibilidad de materiales; se programa producción sin verificar si los materiales están disponibles, generando paradas por falta de insumos.
**Observable_Symptoms:** Se programa producción y luego falta material; paradas por "no hay insumo"; compras de emergencia; producción detenida esperando materiales; materiales comprados que no se usan.
**Early_Warning_Signals:** % de órdenes con material disponible al inicio > 80% (objetivo 100%); % de paradas por falta de material; % de compras de emergencia; frecuencia de "no hay material"; horas perdidas por falta de insumos.
**Typical_Causes:** Planificación sin integración con compras/inventarios; falta de MRP (Material Requirements Planning); datos de inventario no confiables; compras no planificadas; lead times de materiales no considerados.
**Business_Impact:** Producción detenida por falta de materiales; horas improductivas; entregas tardías; compras de emergencia más costosas; programación ineficiente; capacidad desperdiciada.
**Metrics_to_Check:** % de disponibilidad de material al inicio de orden; % de paradas por falta de material; % de compras de emergencia; cumplimiento de plan de producción.
**Diagnostic_Questions:** ¿La planificación considera disponibilidad de materiales? ¿Se verifica stock antes de programar? ¿Hay paradas por falta de material? ¿Se usan compras de emergencia? ¿Hay integración planificación-compras?
**Recommended_Actions:** Integrar planificación con inventarios y compras; implementar MRP básico; verificar disponibilidad de materiales antes de programar; planificar compras según plan de producción; mantener datos de inventario confiables.
**Severity_Level:** Critical
**Related_Patterns:** PRC-007, PRC-015, PRC-029, PRC-070, PRC-075, PRC-100, PRC-103, PRC-108

### PRC-106
**Pattern_Name:** Planificación a Corto Plazo sin Visión de Mediano/Largo
**Category:** Planificación
**Description:** La planificación es exclusivamente de corto plazo (día a día, semana), sin un plan de mediano/largo plazo que permita anticipar necesidades de capacidad, materiales y personal.
**Observable_Symptoms:** Se planifica solo el día o la semana; no hay plan mensual/trimestral; las necesidades de materiales se descubren muy tarde; no se anticipa capacidad; decisiones reactivas; falta de previsión.
**Early_Warning_Signals:** % de planificación con horizonte > 1 mes < 20%; frecuencia de roturas de stock por falta de previsión; % de decisiones reactivas vs planificadas; % de capacidad no anticipada; % de compras sin planificación.
**Typical_Causes:** Cultura de corto plazo; falta de sistema de planificación; demanda impredecible (o percibida como tal); falta de proceso de S&OP (Sales & Operations Planning); gerencia ocupada en el día a día.
**Business_Impact:** Falta de previsión; roturas de stock; capacidad insuficiente en picos; decisiones apresuradas; costos más altos por falta de anticipación; crecimiento no planificado; estrés organizacional.
**Metrics_To_Check:** Horizonte de planificación; % de decisiones anticipadas; % de roturas de stock; % de capacidad planificada vs real; cumplimiento de plan a mediano plazo.
**Diagnostic_Questions:** ¿Hay planificación a mediano/largo plazo? ¿Se anticipan necesidades? ¿Se planifican materiales, capacidad y personal con anticipación? ¿Hay proceso S&OP? ¿Se opera reactivamente?
**Recommended_Actions:** Implementar planificación a mediano plazo (mensual/trimestral); proceso S&OP; rolling forecast; integrar planificación comercial con operaciones; anticipar necesidades críticas.
**Severity_Level:** High
**Related_Patterns:** PRC-005, PRC-029, PRC-093, PRC-096, PRC-103, PRC-107, PRC-108, PRC-112

### PRC-107
**Pattern_Name:** Planificación sin Seguimiento ni Control (Ejecución No Monitoreada)
**Category:** Planificación
**Description:** Existe un plan pero no se hace seguimiento de su ejecución; no se sabe si se está cumpliendo hasta que es demasiado tarde, imposibilitando la corrección temprana de desviaciones.
**Observable_Symptoms:** El plan existe pero nadie lo monitorea; desviaciones no detectadas a tiempo; recién al final se sabe si se cumplió; no hay reunión de seguimiento; no hay métricas de cumplimiento; "plan es solo un papel".
**Early_Warning_Signals:** Frecuencia de seguimiento del plan > 1 semana; % de desviaciones detectadas tarde; no hay reunión de producción diaria; % de cumplimiento desconocido durante la ejecución; % de acciones correctivas tardías.
**Typical_Causes:** Falta de disciplina de seguimiento; reuniones de seguimiento no establecidas; falta de indicadores visibles; cultura de "planificar y olvidar"; supervisión no monitorea.
**Business_Impact:** Desviaciones no corregidas a tiempo; plan no se cumple; entregas tardías; capacidad desperdiciada; falta de accountability; resultados impredecibles.
**Metrics_To_Check:** Frecuencia de seguimiento; % de desviaciones detectadas temprano; % de cumplimiento; % de acciones correctivas implementadas a tiempo; visibilidad del plan.
**Diagnostic_Questions:** ¿Se hace seguimiento del plan? ¿Hay reuniones de producción regulares? ¿Se detectan desviaciones temprano? ¿Se toman acciones correctivas? ¿El plan es monitoreado visiblemente?
**Recommended_Actions:** Establecer reunión de producción diaria de 15 min; crear tablero visual de seguimiento; definir indicadores clave; monitorear cumplimiento en tiempo real; tomar acciones correctivas inmediatas.
**Severity_Level:** High
**Related_Patterns:** PRC-029, PRC-103, PRC-104, PRC-108, PRC-117, PRC-121, PRC-123

### PRC-108
**Pattern_Name:** Planificación que No Considera la Variabilidad de la Demanda
**Category:** Planificación
**Description:** La planificación asume demanda constante o usa promedios, ignorando la variabilidad real, generando faltantes en picos y excesos en valles.
**Observable_Symptoms:** Promedios que no reflejan la realidad; períodos con sobreproducción y otros con falta; roturas de stock seguidas de excesos; % de error de pronóstico alto; planificación basada en "mes pasado".
**Early_Warning_Signals:** % de error de pronóstico > 20%; % de roturas de stock; % de sobreproducción; % de plan cumplido; desviación estándar de demanda vs plan; % de ajustes por variabilidad.
**Typical_Causes:** Pronósticos simples sin método estadístico; no se considera estacionalidad; demanda percibida como impredecible; falta de datos históricos; planificación rígida.
**Business_Impact:** Faltantes o excesos; clientes insatisfechos por falta de producto; inventario excesivo; costos de ajuste; capacidad no alineada; rentabilidad afectada.
**Metrics_To_Check:** % de error de pronóstico; % de roturas de stock; % de sobreproducción; % de cumplimiento de plan; variabilidad de demanda vs plan.
**Diagnostic_Questions:** ¿La planificación considera la variabilidad de demanda? ¿Hay estacionalidad? ¿El pronóstico es preciso? ¿Hay faltantes o excesos? ¿Se ajusta el plan a la demanda real?
**Recommended_Actions:** Mejorar pronósticos (métodos estadísticos, considerar estacionalidad); planificar con rangos (optimista-pesimista); tener flexibilidad para ajustar; monitorear error de pronóstico; usar inventarios de seguridad.
**Severity_Level:** High
**Related_Patterns:** PRC-016, PRC-070, PRC-094, PRC-098, PRC-102, PRC-103, PRC-107, PRC-113

### PRC-109
**Pattern_Name:** Planificación de Mantenimiento Inexistente
**Category:** Planificación
**Description:** No existe planificación de mantenimiento preventivo; el mantenimiento es exclusivamente reactivo (se repara cuando se rompe), generando paradas no programadas y pérdida de capacidad.
**Observable_Symptoms:** Máquinas se reparan solo cuando se rompen; paradas no programadas frecuentes; mantenimiento siempre "apagando incendios"; no hay calendario de mantenimiento; repuestos no planificados.
**Early_Warning_Signals:** % de mantenimiento reactivo vs preventivo > 70%; % de paradas no programadas; % de mantenimiento planificado < 30%; MTBF decreciente; % de repuestos críticos sin stock.
**Typical_Causes:** Cultura de "arreglar cuando se rompe"; falta de plan de mantenimiento; falta de sistema de gestión de mantenimiento; recursos limitados; no se valora el mantenimiento preventivo.
**Business_Impact:** Paradas no programadas; capacidad perdida; costos de reparación más altos; vida útil de equipos reducida; producción impredecible; entregas tardías.
**Metrics_To_Check:** % de mantenimiento preventivo; % de paradas no programadas; MTBF; disponibilidad de equipos; costo de mantenimiento.
**Diagnostic_Questions:** ¿Hay mantenimiento preventivo planificado? ¿O solo reactivo? ¿Hay paradas no programadas frecuentes? ¿Hay plan de mantenimiento? ¿Se programa el mantenimiento?
**Recommended_Actions:** Crear plan de mantenimiento preventivo; programar mantenimiento en períodos de baja demanda; implementar sistema de gestión de mantenimiento; capacitar en TPM; planificar repuestos críticos.
**Severity_Level:** Critical
**Related_Patterns:** PRC-013, PRC-025, PRC-029, PRC-053, PRC-071, PRC-093, PRC-103, PRC-110

### PRC-110
**Pattern_Name:** Planificación Financiera de la Operación Insuficiente
**Category:** Planificación
**Description:** No se planifica financieramente la operación (presupuesto de producción, costo proyectado, inversiones), por lo que no se anticipan necesidades de capital ni se controlan costos.
**Observable_Symptoms:** No hay presupuesto de producción; los costos se conocen después de producir; no se anticipan necesidades de capital de trabajo; las inversiones se deciden sin plan financiero; la operación no tiene metas financieras claras.
**Early_Warning_Signals:** Presupuesto de producción no existe; % de desviación de costos reales vs plan > 15%; % de inversiones con plan financiero < 40%; % de capital de trabajo no anticipado; rentabilidad desconocida por producto.
**Typical_Causes:** Falta de integración finanzas-operaciones; cultura de "producir primero, costos después"; falta de sistema de costos; gerencia operativa no orientada a finanzas; tamaño pequeño donde "no se necesita".
**Business_Impact:** Falta de control de costos; sorpresas financieras; inversiones sin análisis; rentabilidad desconocida; capital de trabajo insuficiente; decisiones operativas sin visión financiera.
**Metrics_To_Check:** % de desviación de costos reales vs plan; % de inversiones con plan financiero; rentabilidad por producto; % de capital de trabajo planificado; cumplimiento de presupuesto.
**Diagnostic_Questions:** ¿Hay presupuesto de producción? ¿Se planifican los costos? ¿Se anticipan necesidades de capital de trabajo? ¿Las inversiones tienen plan financiero? ¿Se controlan los costos operativos?
**Recommended_Actions:** Integrar planificación operativa con financiera; elaborar presupuesto de producción; proyectar costos y necesidades de capital; hacer seguimiento presupuestario; capacitar a operaciones en finanzas.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-029, PRC-096, PRC-103, PRC-107, PRC-112, PRC-117

### PRC-111
**Pattern_Name:** Planificación de Proyectos sin Metodología
**Category:** Planificación
**Description:** Los proyectos (lanzamientos, mejoras, expansiones) se planifican sin metodología formal (carta Gantt, hitos, recursos, riesgos), generando retrasos, sobrecostos y baja tasa de éxito.
**Observable_Symptoms:** Proyectos sin fecha clara de fin; no hay asignación de responsables; se avanza a "como se pueda"; los proyectos se retrasan; no se sabe si se está a tiempo; el alcance cambia sin control.
**Early_Warning_Signals:** % de proyectos completados a tiempo < 40%; % de proyectos dentro de presupuesto; % de proyectos con planificación formal < 30%; % de proyectos con cambios de alcance sin control; % de proyectos abandonados.
**Typical_Causes:** Falta de metodología de gestión de proyectos; cultura de "empezar sin plan"; optimismo en tiempos; falta de asignación de recursos; proyectos sin dueño claro.
**Business_Impact:** Proyectos no se completan; recursos desperdiciados; beneficios no realizados; frustración del equipo; falta de credibilidad; costos mayores.
**Metrics_To_Check:** % de proyectos a tiempo; % dentro de presupuesto; % con planificación formal; % completados; satisfacción con proyectos.
**Diagnostic_Questions:** ¿Los proyectos se planifican formalmente? ¿Hay carta Gantt? ¿Hay responsables claros? ¿Se hace seguimiento? ¿Los proyectos se completan a tiempo?
**Recommended_Actions:** Implementar metodología de gestión de proyectos (PMBOK básico, ágil); definir alcance, tiempo, recursos, riesgos; asignar responsables; hacer seguimiento semanal; celebrar hitos.
**Severity_Level:** High
**Related_Patterns:** PRC-006, PRC-050, PRC-106, PRC-107, PRC-112, PRC-117, PRC-121, PRC-126


## Mejora Continua

### PRC-112
**Pattern_Name:** Cultura de "Siempre lo Hicimos Así" (Resistencia al Cambio)
**Category:** Mejora Continua
**Description:** Existe una fuerte resistencia al cambio y apego a métodos tradicionales, con frases como "siempre lo hicimos así", que bloquea cualquier iniciativa de mejora y mantiene prácticas obsoletas.
**Observable_Symptoms:** Frase "siempre lo hicimos así" es común; resistencia a nuevas ideas; cambios propuestos son rechazados sin análisis; el equipo se siente cómodo con lo conocido; mejoras no se implementan; cultura estática.
**Early_Warning_Signals:** % de empleados abiertos al cambio < 30%; % de sugerencias de mejora < 1/empleado/año; % de cambios implementados sobre propuestos < 20%; antigüedad promedio de procesos sin cambio; resistencia visible a nuevas ideas.
**Typical_Causes:** Cultura organizacional conservadora; liderazgo que no promueve cambio; miedo a lo desconocido; comodidad con rutinas; experiencias pasadas negativas con cambios; falta de incentivos para innovar.
**Business_Impact:** Estancamiento; competitividad reducida; no se adoptan mejores prácticas; procesos obsoletos; talento joven frustrado; empresa pierde relevancia; incapacidad de adaptarse al mercado.
**Metrics_To_Check:** % de sugerencias de mejora; % de cambios implementados; % de apertura al cambio (encuesta); antigüedad de procesos; rotación de talento joven.
**Diagnostic_Questions:** ¿La frase "siempre lo hicimos así" es común? ¿Hay resistencia al cambio? ¿Se proponen mejoras? ¿Se implementan? ¿La organización es estática o dinámica?
**Recommended_Actions:** Liderazgo debe promover cambio; celebrar experimentación y aprendizaje; capacitar en mejora continua; empezar con cambios pequeños y visibles; reconocer a quienes proponen mejoras; comunicar beneficios del cambio.
**Severity_Level:** Critical
**Related_Patterns:** PRC-066, PRC-082, PRC-085, PRC-117, PRC-119, PRC-125, PRC-128

### PRC-113
**Pattern_Name:** Mejora Continua sin Metodología (Intuitiva y No Sistemática)
**Category:** Mejora Continua
**Description:** Se hacen "mejoras" pero de manera intuitiva, sin metodología estructurada (PDCA, DMAIC, Kaizen), por lo que las mejoras no son sostenibles ni replicables.
**Observable_Symptoms:** Mejoras basadas en corazonadas; no hay método estructurado; las mejoras no se documentan; los resultados no se miden; se vuelve a la forma anterior después de un tiempo; no hay ciclo de mejora.
**Early_Warning_Signals:** % de mejoras con método estructurado (PDCA/DMAIC) < 20%; % de mejoras documentadas; % de mejoras sostenidas después de 3 meses; % de equipo capacitado en metodología de mejora; % de mejoras con resultados medidos.
**Typical_Causes:** Desconocimiento de metodologías de mejora; cultura de "hacer nomás" sin estructura; falta de capacitación; impaciencia por resultados rápidos; liderazgo no exige método.
**Business_Impact:** Mejoras no sostenibles; resultados no medibles; frustración por "mejoramos y luego volvemos"; esfuerzo desperdiciado; no se construye capacidad de mejora; problemas crónicos no resueltos.
**Metrics_To_Check:** % de mejoras con método; % de mejoras sostenidas; % de mejoras con resultado medido; % de equipo capacitado en mejora; tendencia de indicadores.
**Diagnostic_Questions:** ¿Las mejoras siguen una metodología? ¿Se documentan? ¿Se miden resultados? ¿Son sostenibles? ¿El equipo conoce PDCA o similar?
**Recommended_Actions:** Capacitar en metodología PDCA (Plan-Do-Check-Act); implementar ciclo de mejora estructurado; documentar mejoras; medir antes y después; verificar sostenibilidad; estandarizar mejoras exitosas.
**Severity_Level:** High
**Related_Patterns:** PRC-046, PRC-066, PRC-082, PRC-107, PRC-112, PRC-117, PRC-121, PRC-125

### PRC-114
**Pattern_Name:** Mejora Continua Sin Participación del Equipo
**Category:** Mejora Continua
**Description:** La mejora continua es vista como responsabilidad exclusiva de la gerencia o un departamento, sin involucrar al equipo operativo que mejor conoce los problemas y soluciones.
**Observable_Symptoms:** Solo la gerencia propone mejoras; los operadores tienen ideas pero no se les pide; sugerencias no son bienvenidas; el equipo operativo no participa en soluciones; mejora es "de arriba hacia abajo".
**Early_Warning_Signals:** % de sugerencias de mejora de operadores < 10% del total; % de equipo que ha propuesto al menos una mejora en el último año < 20%; % de mejoras implementadas que vinieron de operadores; % de participación en eventos de mejora.
**Typical_Causes:** Cultura jerárquica; subestimación del conocimiento operativo; falta de canales de sugerencia; gerencia cree que "ellos piensan, los otros ejecutan"; falta de incentivos para participar.
**Business_Impact:** Oportunidades de mejora perdidas; equipo desmotivado; conocimiento operativo desperdiciado; mejoras no consideran la realidad del día a día; baja adopción de cambios.
**Metrics_To_Check:** % de sugerencias de operadores; % de participación en mejora; % de mejoras implementadas desde operadores; % de equipo capacitado en mejora; clima de participación.
**Diagnostic_Questions:** ¿El equipo participa en la mejora continua? ¿Hay canales de sugerencia? ¿Las ideas operativas se implementan? ¿Se valora el conocimiento del equipo? ¿Hay incentivos para participar?
**Recommended_Actions:** Crear canales de sugerencia (buzón, reuniones Kaizen); involucrar a operadores en análisis de problemas; implementar sus ideas; reconocer contribuciones; capacitar a todos en mejora continua.
**Severity_Level:** High
**Related_Patterns:** PRC-042, PRC-058, PRC-066, PRC-092, PRC-112, PRC-117, PRC-119, PRC-125

### PRC-115
**Pattern_Name:** Mejora Continua Focalizada Solo en Producción (No en Administración)
**Category:** Mejora Continua
**Description:** Las iniciativas de mejora se concentran exclusivamente en el área de producción/operaciones, ignorando los procesos administrativos, de soporte y gerenciales que también tienen desperdicios.
**Observable_Symptoms:** Producción mejora pero administración sigue con procesos ineficientes; cuellos de botella administrativos afectan a producción; procesos de soporte (compras, RRHH, finanzas) no se mejoran; las mejoras solo son en el piso de producción.
**Early_Warning_Signals:** % de proyectos de mejora en áreas administrativas < 15%; % de procesos administrativos mapeados; tiempo de procesos administrativos no mejora; % de desperdicio administrativo estimado; quejas de producción sobre procesos administrativos lentos.
**Typical_Causes:** Enfoque tradicional de mejora en manufactura; desconocimiento de Lean aplicado a administración; resistencia de áreas administrativas a ser evaluadas; falta de métricas administrativas; cultura de "nosotros no producimos".
**Business_Impact:** Procesos administrativos ineficientes; demoras en soporte a producción; costos administrativos altos; capacidad de respuesta lenta; mejora general limitada; cuellos de botella administrativos.
**Metrics_To_Check:** % de proyectos de mejora en administración; % de procesos administrativos mejorados; tiempo de procesos clave administrativos; satisfacción de clientes internos; costo administrativo como % de ventas.
**Diagnostic_Questions:** ¿La mejora continua solo se aplica en producción? ¿Los procesos administrativos se mejoran? ¿Hay cuellos de botella administrativos? ¿Se ha aplicado Lean en administración? ¿Hay métricas administrativas?
**Recommended_Actions:** Extender mejora continua a áreas administrativas; mapear procesos administrativos; identificar desperdicios (esperas, retrabajo, excesos); aplicar Lean Office; medir y mejorar procesos de soporte.
**Severity_Level:** High
**Related_Patterns:** PRC-004, PRC-048, PRC-060, PRC-068, PRC-082, PRC-117, PRC-125

### PRC-116
**Pattern_Name:** Mejora Continua Sin Estandarización Previa
**Category:** Mejora Continua
**Description:** Se intenta mejorar procesos que no están estandarizados, por lo que no hay una base estable desde la cual mejorar, y las "mejoras" no son sostenibles porque el proceso varía constantemente.
**Observable_Symptoms:** Procesos no estandarizados que se intentan mejorar; mejoras que no se mantienen; no hay "antes" estable para medir mejora; el proceso cambia todo el tiempo; no se sabe cuál es la línea base.
**Early_Warning_Signals:** % de procesos estandarizados antes de mejorar < 30%; % de mejoras que no se sostienen > 50%; % de procesos con línea base medida; % de variabilidad del proceso antes de mejora; % de mejora que es atribuible a estandarización vs mejora.
**Typical_Causes:** Desconocimiento del principio: "no se puede mejorar lo que no está estandarizado"; impaciencia por mejorar; cultura de "mejorar sobre la marcha"; falta de comprensión de variabilidad.
**Business_Impact:** Mejoras no sostenibles; resultados no medibles; frustración; retorno bajo de iniciativas de mejora; no se construye sobre bases sólidas; el proceso nunca se estabiliza.
**Metrics_To_Check:** % de procesos estandarizados antes de mejora; % de mejoras sostenidas; % de procesos con línea base; variabilidad del proceso; % de mejora atribuible.
**Diagnostic_Questions:** ¿Los procesos están estandarizados antes de mejorar? ¿Hay línea base? ¿Las mejoras se sostienen? ¿Se reduce variabilidad primero? ¿Hay un estándar estable?
**Recommended_Actions:** Estandarizar primero, luego mejorar; establecer línea base; reducir variabilidad antes de mejorar; asegurar que el estándar se cumple; luego implementar mejoras sobre base estable.
**Severity_Level:** High
**Related_Patterns:** PRC-011, PRC-014, PRC-039, PRC-083, PRC-084, PRC-085, PRC-113, PRC-125

### PRC-117
**Pattern_Name:** Indicadores de Mejora No Establecidos o No Visibles
**Category:** Mejora Continua
**Description:** No hay indicadores claros para medir la mejora continua; no se sabe si se está mejorando o empeorando; las decisiones se toman sin datos y el progreso no es visible.
**Observable_Symptoms:** No hay tablero de indicadores; no se sabe la tendencia de los procesos; mejoras no se miden; decisiones basadas en opiniones no en datos; no hay metas claras; no se visualiza el progreso.
**Early_Warning_Signals:** % de procesos con indicadores definidos < 30%; frecuencia de revisión de indicadores < mensual; % de decisiones basadas en datos; % de equipo que conoce los indicadores; % de metas definidas.
**Typical_Causes:** Falta de cultura de medición; sistemas de información insuficientes; no se definieron KPIs; gerencia no exige datos; miedo a medir y encontrar problemas; falta de tableros visuales.
**Business_Impact:** Incertidumbre sobre el progreso; decisiones sin datos; imposibilidad de saber si las mejoras funcionan; falta de enfoque; equipo no alineado; mejora sin dirección.
**Metrics_To_Check:** % de procesos con indicadores; % de indicadores visibles; % de decisiones basadas en datos; % de metas cumplidas; frecuencia de revisión de indicadores.
**Diagnostic_Questions:** ¿Hay indicadores para medir mejora? ¿Son visibles? ¿Se revisan periódicamente? ¿Las decisiones se basan en datos? ¿El equipo conoce los indicadores?
**Recommended_Actions:** Definir indicadores clave para cada proceso (KPIs); crear tablero visual (físico o digital); revisar periódicamente; establecer metas; tomar decisiones basadas en datos; celebrar avances.
**Severity_Level:** Critical
**Related_Patterns:** PRC-004, PRC-029, PRC-040, PRC-047, PRC-081, PRC-107, PRC-113, PRC-121, PRC-125

### PRC-118
**Pattern_Name:** Mejora Continua sin Reconocimiento ni Incentivos
**Category:** Mejora Continua
**Description:** No hay reconocimiento ni incentivos para quienes proponen o implementan mejoras, por lo que el equipo no se siente motivado a participar activamente en la mejora continua.
**Observable_Symptoms:** Nadie propone mejoras; las ideas no son reconocidas; no hay incentivos para mejorar; el equipo no ve beneficio en participar; solo unos pocos (o nadie) contribuyen con ideas; iniciativas de mejora mueren por falta de participación.
**Early_Warning_Signals:** % de equipo que ha propuesto mejoras en el último año < 10%; % de ideas reconocidas formalmente; % de incentivos vinculados a mejora; % de participación en eventos de mejora; % de mejora en indicadores vs incentivos.
**Typical_Causes:** Cultura de no reconocer; falta de programa de incentivos; gerencia da por sentado que mejorar es parte del trabajo; no hay presupuesto para reconocimiento; se reconoce solo a gerencia no a operadores.
**Business_Impact:** Baja participación en mejora; ideas valiosas no se generan; cultura de "para qué voy a proponer"; mejora continua no se arraiga; potencial de mejora desaprovechado; equipo desmotivado.
**Metrics_To_Check:** % de participación en mejora; número de sugerencias por empleado; % de sugerencias implementadas; % de reconocimiento otorgado; satisfacción con reconocimiento.
**Diagnostic_Questions:** ¿Se reconoce a quienes proponen mejoras? ¿Hay incentivos? ¿El equipo participa activamente? ¿Hay cultura de reconocimiento? ¿Se celebra la mejora?
**Recommended_Actions:** Establecer programa de reconocimiento (público, premios simbólicos, bonos por ideas implementadas); celebrar logros de mejora; vincular evaluación de desempeño a participación en mejora; agradecer públicamente.
**Severity_Level:** High
**Related_Patterns:** PRC-044, PRC-066, PRC-092, PRC-112, PRC-114, PRC-117, PRC-119, PRC-125

### PRC-119
**Pattern_Name:** Mejora Continua Sin Capacitación del Equipo
**Category:** Mejora Continua
**Description:** Se espera que el equipo participe en mejora continua pero no se le capacita en metodologías, herramientas (5 porqués, Ishikawa, PDCA, 5S) ni se le da tiempo para hacerlo.
**Observable_Symptoms:** El equipo no sabe cómo mejorar; las herramientas de mejora no se conocen; no hay tiempo asignado para mejora; se espera mejora "además del trabajo normal"; metodologías como 5S, PDCA no se usan.
**Early_Warning_Signals:** % de equipo capacitado en mejora continua < 20%; % de equipo que conoce herramientas (PDCA, 5 porqués, 5S); % de tiempo asignado a mejora < 2%; % de uso de herramientas de mejora; % de proyectos de mejora que usan metodología.
**Typical_Causes:** Falta de inversión en capacitación; cultura de "mejorar mientras se trabaja"; no se valora la capacitación en métodos; se asume que "todos saben mejorar"; falta de presupuesto de capacitación.
**Business_Impact:** Mejora sin método; herramientas no utilizadas; potencial de mejora limitado; equipo frustrado por no saber cómo hacerlo; resultados subóptimos; dependencia de consultores externos.
**Metrics_To_Check:** % de equipo capacitado; % de uso de herramientas; % de tiempo dedicado a mejora; % de proyectos con metodología; % de mejora en indicadores.
**Diagnostic_Questions:** ¿El equipo está capacitado en mejora continua? ¿Conoce herramientas como PDCA, 5 porqués? ¿Hay tiempo asignado para mejorar? ¿Se usan metodologías? ¿Hay inversión en capacitación?
**Recommended_Actions:** Capacitar a todo el equipo en mejora continua (PDCA, 5 porqués, 5S, Ishikawa); asignar tiempo semanal para mejora; crear proyectos de mejora con mentoría; invertir en desarrollo de habilidades.
**Severity_Level:** High
**Related_Patterns:** PRC-066, PRC-076, PRC-082, PRC-089, PRC-113, PRC-114, PRC-117, PRC-125

### PRC-120
**Pattern_Name:** Benchmarking Externo No Realizado
**Category:** Mejora Continua
**Description:** La empresa no compara sus procesos y métricas con referentes externos (benchmarking), por lo que no sabe si su desempeño es bueno, malo o regular en relación al mercado.
**Observable_Symptoms:** No se sabe cómo están otros; las métricas no se comparan externamente; se cree que se está bien sin evidencia; metas internas sin referencia externa; sorpresas cuando se descubre que otros son mejores.
**Early_Warning_Signals:** % de métricas comparadas externamente < 20%; % de indicadores con benchmark conocido; % de meta basada en benchmark; % de creencia vs realidad de desempeño; % de brecha de desempeño desconocida.
**Typical_Causes:** Falta de acceso a datos de benchmark; cultura de mirarse a sí mismo; temor a encontrar que se está mal; desconocimiento de fuentes de benchmark; no se considera importante.
**Business_Impact:** Percepción irreal del desempeño; metas no desafiantes; falta de urgencia por mejorar; competitividad no evaluada; oportunidades de mejora no identificadas; ventaja competitiva desconocida.
**Metrics_To_Check:** % de métricas con benchmark; % de brecha de desempeño conocida; % de metas basadas en benchmark; posición competitiva; % de mejoras basadas en benchmark.
**Diagnostic_Questions:** ¿Se comparan los procesos con referentes externos? ¿Se conoce el desempeño de la competencia? ¿Las metas consideran benchmark? ¿Hay brechas de desempeño conocidas? ¿Se usa benchmark para priorizar mejoras?
**Recommended_Actions:** Identificar fuentes de benchmark (asociaciones, publicaciones, redes); comparar indicadores clave con referentes; establecer metas basadas en benchmark; identificar brechas; priorizar mejoras para cerrar brechas.
**Severity_Level:** Medium
**Related_Patterns:** PRC-029, PRC-036, PRC-066, PRC-093, PRC-112, PRC-117, PRC-121, PRC-125

### PRC-121
**Pattern_Name:** Ciclo de Mejora No Completado (No Hay Check ni Act)
**Category:** Mejora Continua
**Description:** Se implementan mejoras pero no se verifica si funcionaron ni se estandarizan, por lo que el ciclo PDCA no se completa y las mejoras no son sostenibles.
**Observable_Symptoms:** Mejoras implementadas que no se evalúan; no se mide si la mejora funcionó; las mejoras se abandonan después de un tiempo; los mismos problemas vuelven; no se estandarizan las mejoras exitosas.
**Early_Warning_Signals:** % de mejoras con verificación de resultados < 30%; % de mejoras estandarizadas; % de mejoras sostenidas > 6 meses; % de problemas que recurren; % de ciclos PDCA completos.
**Typical_Causes:** Impaciencia por pasar a la siguiente mejora; falta de disciplina de seguimiento; no se asigna tiempo para verificar; cultura de "implementar y seguir"; falta de método.
**Business_Impact:** Mejoras no sostenibles; mismos problemas recurrentes; esfuerzo desperdiciado; frustración; no se construye conocimiento; mejora continua no se consolida.
**Metrics_To_Check:** % de mejoras verificadas; % de mejoras estandarizadas; % de sostenibilidad de mejoras; % de recurrencia de problemas; % de ciclos PDCA completos.
**Diagnostic_Questions:** ¿Se verifica si las mejoras funcionaron? ¿Se estandarizan las mejoras exitosas? ¿Los problemas vuelven? ¿Se completa el ciclo PDCA? ¿Las mejoras son sostenibles?
**Recommended_Actions:** Completar el ciclo PDCA: verificar resultados (Check), estandarizar si funcionó (Act); medir antes y después; documentar lecciones; asegurar sostenibilidad; celebrar éxito y pasar a siguiente mejora.
**Severity_Level:** High
**Related_Patterns:** PRC-046, PRC-085, PRC-107, PRC-113, PRC-116, PRC-117, PRC-125, PRC-128

### PRC-122
**Pattern_Name:** Mejora Continua como Iniciativa Temporal (No como Cultura)
**Category:** Mejora Continua
**Description:** La mejora continua se trata como un proyecto o iniciativa temporal (ej. "programa de mejora de 3 meses"), no como una cultura permanente, por lo que los resultados no se mantienen.
**Observable_Symptoms:** Iniciativas de mejora que empiezan y terminan; después de unos meses se vuelve a la rutina; "programa de mejora" lanzado con bombo y luego abandonado; el equipo ve la mejora como "otra iniciativa del mes"; cínicos que dicen "esto también pasará".
**Early_Warning_Signals:** % de iniciativas de mejora continuas después de 12 meses < 30%; % de equipo que ve mejora como cultura; % de tiempo dedicado a mejora de forma permanente; % de mejora en indicadores que se mantiene; rotación de prioridades de mejora.
**Typical_Causes:** Liderazgo sin compromiso a largo plazo; enfoque en resultados rápidos; falta de integración en la operación diaria; mejora vista como adicional no como forma de trabajar; falta de sistema de mejora continua.
**Business_Impact:** Resultados no sostenibles; escepticismo del equipo; energía desperdiciada en lanzamientos que no duran; cultura no cambia; mejoras abandonadas; empresa no desarrolla capacidad de mejora.
**Metrics_To_Check:** % de iniciativas continuas > 12 meses; % de mejora sostenida; % de equipo comprometido con mejora; % de tiempo dedicado a mejora; % de indicadores que siguen mejorando.
**Diagnostic_Questions:** ¿La mejora continua es una iniciativa temporal o una cultura? ¿Se mantiene en el tiempo? ¿El equipo cree en ella? ¿Está integrada en el día a día? ¿Hay compromiso a largo plazo?
**Recommended_Actions:** Incorporar mejora continua en la operación diaria (no como proyecto separado); hacerla parte de las reuniones regulares; asignar tiempo permanente; liderazgo debe mostrar compromiso sostenido; celebrar avances a largo plazo.
**Severity_Level:** Critical
**Related_Patterns:** PRC-082, PRC-085, PRC-112, PRC-113, PRC-114, PRC-117, PRC-121, PRC-125, PRC-128

### PRC-123
**Pattern_Name:** Kaizen sin Eventos o Talleres Estructurados
**Category:** Mejora Continua
**Description:** No se realizan eventos Kaizen o talleres de mejora estructurados (semanas Kaizen, eventos de mejora rápida), perdiendo la oportunidad de lograr avances significativos en corto tiempo.
**Observable_Symptoms:** Mejora solo incremental y lenta; no hay eventos intensivos de mejora; los cambios grandes no se abordan; falta de enfoque en problemas específicos; mejora solo en el día a día sin "aceleradores".
**Early_Warning_Signals:** Frecuencia de eventos Kaizen < 2/año; % de mejora lograda en eventos vs día a día; % de equipo participando en eventos Kaizen; % de problemas abordados en eventos; % de resultados significativos de eventos.
**Typical_Causes:** Desconocimiento de metodología Kaizen; falta de facilitadores; cultura de mejora lenta continua sin picos; recursos limitados; falta de compromiso para dedicar tiempo a eventos.
**Business_Impact:** Mejora solo incremental; cambios significativos tardan mucho; problemas grandes no se abordan con enfoque; equipo no experimenta mejoras rápidas; potencial de mejora no explotado.
**Metrics_To_Check:** Frecuencia de eventos Kaizen; % de mejora por evento; % de equipo participante; % de implementación de acciones de eventos; ROI de eventos Kaizen.
**Diagnostic_Questions:** ¿Se realizan eventos Kaizen? ¿Hay talleres de mejora estructurados? ¿Se logran avances significativos en corto tiempo? ¿El equipo participa en eventos? ¿Hay facilitadores capacitados?
**Recommended_Actions:** Implementar eventos Kaizen periódicos (semanas de mejora); capacitar facilitadores; seleccionar problemas críticos; dedicar equipo completo durante evento; implementar rápidamente; celebrar resultados.
**Severity_Level:** Medium
**Related_Patterns:** PRC-066, PRC-107, PRC-113, PRC-114, PRC-117, PRC-119, PRC-121, PRC-125, PRC-128

### PRC-124
**Pattern_Name:** Lecciones Aprendidas No Capturadas ni Compartidas
**Category:** Mejora Continua
**Description:** Las lecciones aprendidas de proyectos, problemas o mejoras no se documentan ni comparten, por lo que el conocimiento se pierde y los mismos errores se repiten en diferentes áreas o momentos.
**Observable_Symptoms:** Mismos errores se repiten en diferentes proyectos; el conocimiento se pierde cuando alguien se va; no hay base de conocimiento; lecciones no se documentan; cada área comete los mismos errores que otras ya cometieron.
**Early_Warning_Signals:** % de proyectos con lecciones aprendidas documentadas < 20%; % de errores recurrentes; % de conocimiento documentado; % de lecciones compartidas; tiempo entre repetición del mismo error.
**Typical_Causes:** Falta de proceso de documentación; cultura de "seguir adelante sin mirar atrás"; no se dedica tiempo a capturar lecciones; no hay sistema de gestión del conocimiento; urgencia del día a día no deja espacio.
**Business_Impact:** Errores repetidos; conocimiento perdido; curva de aprendizaje no se acelera; dependencia de personas; rotación pérdida de know-how; mejora lenta.
**Metrics_To_Check:** % de proyectos con lecciones documentadas; % de errores recurrentes; % de conocimiento documentado; % de lecciones aplicadas; satisfacción con gestión del conocimiento.
**Diagnostic_Questions:** ¿Se documentan las lecciones aprendidas? ¿Se comparten? ¿Los mismos errores se repiten? ¿El conocimiento se pierde con la rotación? ¿Hay sistema de gestión del conocimiento?
**Recommended_Actions:** Documentar lecciones aprendidas al final de proyectos/problemas; crear repositorio accesible; compartir en reuniones; revisar lecciones al iniciar proyectos similares; celebrar aprendizaje.
**Severity_Level:** Medium
**Related_Patterns:** PRC-046, PRC-058, PRC-066, PRC-089, PRC-112, PRC-113, PRC-117, PRC-121, PRC-125

### PRC-125
**Pattern_Name:** Cultura de "Culpar" en Lugar de "Mejorar"
**Category:** Mejora Continua
**Description:** La cultura organizacional tiende a culpar a las personas cuando algo sale mal, en lugar de analizar el proceso y buscar la mejora, inhibiendo la identificación abierta de problemas y el aprendizaje.
**Observable_Symptoms:** Cuando hay un error, se busca al culpable; el equipo oculta errores por miedo a represalias; los problemas se esconden; no se habla abiertamente de fallas; se repiten los mismos errores porque no se analizan; el "qué pasó" se convierte en "quién fue".
**Early_Warning_Signals:** % de incidentes donde se busca culpable vs causa raíz; % de errores ocultos; % de equipo que reportaría un error abiertamente; % de problemas que se repiten; clima de confianza vs miedo.
**Typical_Causes:** Liderazgo que culpa; cultura punitiva; falta de comprensión de que la mayoría de errores son del proceso; influencia cultural (miedo al error); sistema de evaluación que castiga errores.
**Business_Impact:** Errores ocultos; problemas no se resuelven; mismos errores repetidos; equipo con miedo; aprendizaje organizacional nulo; mejora continua imposible; moral baja.
**Metrics_To_Check:** % de errores reportados abiertamente; % de incidentes con análisis de causa raíz; % de problemas recurrentes; clima laboral (confianza); % de equipo que reportaría un error.
**Diagnostic_Questions:** ¿Se busca al culpable o la causa? ¿Los errores se ocultan? ¿Hay miedo a reportar problemas? ¿Los mismos errores se repiten? ¿La cultura es punitiva o de aprendizaje?
**Recommended_Actions:** Transitar de cultura de culpa a cultura de aprendizaje; analizar procesos no personas cuando hay errores; liderazgo debe modelar la transparencia; celebrar reporte de problemas; implementar "no blame" para errores no intencionales.
**Severity_Level:** Critical
**Related_Patterns:** PRC-042, PRC-054, PRC-058, PRC-066, PRC-082, PRC-112, PRC-113, PRC-114, PRC-117, PRC-122, PRC-126
