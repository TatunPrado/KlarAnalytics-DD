# Knowledge_Consolidation

> **Procedimiento Operativo Estándar (SOP)** — Sistema de Aprendizaje Organizacional y Consolidación de Conocimiento
> Versión: 1.0 | Última actualización: 2026-06-15

---

## Tabla de Contenidos

1. [Propósito y Arquitectura](#1-propósito-y-arquitectura)
2. [Estructura del Conocimiento](#2-estructura-del-conocimiento)
3. [Ciclo de Consolidación](#3-ciclo-de-consolidación)
4. [Etapa 1: Cosecha de Diagnósticos](#4-etapa-1-cosecha-de-diagnósticos)
5. [Etapa 2: Detección de Patrones](#5-etapa-2-detección-de-patrones)
6. [Etapa 3: Validación y Falsos Positivos](#6-etapa-3-validación-y-falsos-positivos)
7. [Etapa 4: Deduplicación](#7-etapa-4-deduplicación)
8. [Etapa 5: Enriquecimiento de Patrones Existentes](#8-etapa-5-enriquecimiento-de-patrones-existentes)
9. [Etapa 6: Generación de Nuevos Patrones](#9-etapa-6-generación-de-nuevos-patrones)
10. [Etapa 7: Actualización de Knowledge/Learned](#10-etapa-7-actualización-de-knowledgelearned)
11. [Etapa 8: Propuesta a Knowledge/Core](#11-etapa-8-propuesta-a-knowledgecore)
12. [Control de Calidad y Versionado](#12-control-de-calidad-y-versionado)
13. [Gobierno del Conocimiento](#13-gobierno-del-conocimiento)
14. [Métricas del Sistema](#14-métricas-del-sistema)

---

## 1. Propósito y Arquitectura

### 1.1 Objetivo General
Establecer un ciclo continuo de aprendizaje organizacional que permita al sistema multi-agente mejorar progresivamente su precisión, exhaustividad y relevancia a partir de la experiencia acumulada en diagnósticos reales de PyMEs.

### 1.2 Principios del Sistema

| Principio | Descripción |
|---|---|
| **Aprender de cada caso** | Ningún diagnóstico se archiva sin extraer su lección |
| **Separación Learned / Core** | El conocimiento experimental (Learned) se promueve a conocimiento validado (Core) solo tras aprobación |
| **Trazabilidad total** | Cada fragmento de conocimiento nuevo se traza a su diagnóstico de origen |
| **Calidad sobre cantidad** | Un patrón bien validado vale más que cien patrones sospechosos |
| **Mejora continua** | El sistema se evalúa a sí mismo con métricas de precisión y cobertura |
| **Sin duplicados** | Todo patrón nuevo se verifica contra el corpus existente antes de incorporarse |

### 1.3 Arquitectura del Conocimiento

```
                     ┌─────────────────────────────────────┐
                     │        Knowledge / Core              │
                     │  (Patrones validados y canónicos)    │
                     │  10 bases: BM, Fin, CF, Sales, Mkt, │
                     │  Cust, Proc, Risk, Org, Strat        │
                     └──────────────────┬──────────────────┘
                                        │
                     Promoción vía      │
                     aprobación         │
                                        │
                     ┌──────────────────▼──────────────────┐
                     │        Knowledge / Learned            │
                     │  (Patrones experimentales, en         │
                     │   observación, candidatos a Core)     │
                     └──────────────────┬──────────────────┘
                                        │
                     Alimentación vía   │
                     consolidación      │
                                        │
                     ┌──────────────────▼──────────────────┐
                     │     Diagnósticos Completados          │
                     │  (Hallazgos, causas raíz,             │
                     │   iniciativas, resultados)            │
                     └─────────────────────────────────────┘
```

### 1.4 Actores del Sistema

| Actor | Rol |
|---|---|
| **Knowledge_Consolidator** | Agente encargado de ejecutar el ciclo de consolidación (puede ser un rol del Master_Diagnosis_Orchestrator o un agente dedicado) |
| **Knowledge_Reviewer** | Agente o humano que revisa y aprueba propuestas de promoción a Core |
| **Domain_Validator** | Agente especializado por dominio que valida patrones contra su base de conocimiento (p.ej. Financial_Analyst revisa patrones financieros) |
| **Sistema de Métricas** | Subsistema que registra accuracy, cobertura, falsos positivos, frescura del conocimiento |

---

## 2. Estructura del Conocimiento

### 2.1 Taxonomía de Patrones

Cada patrón en el sistema pertenece a una de estas categorías:

| Categoría | Prefijo ID | Base de Conocimiento | Ejemplo |
|---|---|---|---|
| Modelo de Negocio | `P-BM` | Business_Model_Patterns | "PyMEs familiares con más de 20 años tienden a tener modelos de negocio basados en relaciones de confianza" |
| Financiero | `P-FI` | Financial_Patterns | "Empresas con CCC > 90 días tienen 70% de probabilidad de problemas de liquidez a 12 meses" |
| Cash Flow | `P-CF` | CashFlow_Patterns | "Estacionalidad positiva en Q4 es común en retail PyME; negativa en Q1 indica necesidad de financiamiento puente" |
| Ventas | `P-SA` | Sales_Patterns | "PyMEs con propiedad del fundador en ventas directas estancan crecimiento al llegar a 10 empleados" |
| Marketing | `P-MK` | Marketing_Patterns | "El canal orgánico (boca a boca) representa >60% de adquisición en PyMEs de servicios profesionales" |
| Clientes | `P-CU` | Customer_Patterns | "La concentración de ingresos en 1 cliente >40% es un predictor de vulnerabilidad en PyMEs de manufactura" |
| Procesos | `P-PR` | Process_Patterns | "PyMEs sin procesos documentados al alcanzar 15 empleados experimentan caídas de calidad del 20-30%" |
| Riesgos | `P-RI` | Risk_Patterns | "El riesgo de rotación de personal clave es 3x mayor en PyMEs sin plan de sucesión" |
| Organización | `P-OR` | Organization_Patterns | "PyMEs con estructura plana (>15 empleados) presentan cuellos de botella en la toma de decisiones" |
| Estrategia | `P-ST` | Strategy_Patterns | "Estrategias de diferenciación en PyMEs de commoditie tienen tasa de fracaso >80% sin un nicho claro" |

### 2.2 Esquema de un Patrón

```json
{
  "id": "P-FI-0042-v3.1",
  "titulo": "CCC > 90 días como predictor de crisis de liquidez a 12 meses",
  "categoria": "financiero",
  "tipo": "predictivo",
  "descripcion": "En PyMEs con ciclo de conversión de efectivo superior a 90 días, la probabilidad de experimentar una crisis de liquidez (incumplimiento de pagos a 30 días) en los siguientes 12 meses es del 70%, basado en una muestra de 45 diagnósticos.",
  "confianza": 0.85,
  "soporte_muestral": 45,
  "precision_estimada": 0.82,
  "tasa_falsos_positivos": 0.12,
  "ultima_actualizacion": "2026-06-01",
  "origen": {
    "tipo": "consolidacion",
    "diagnostico_id": "D-2026-042",
    "hallazgo_id": "H-FI-012-v1.2",
    "fecha_primer_observacion": "2025-11-15"
  },
  "condiciones_aplicacion": {
    "industrias": ["manufactura", "comercio", "distribucion"],
    "tamano_empresa": ["pequena", "mediana"],
    "antiguedad_minima_anios": 2
  },
  "metricas_historial": [
    {"fecha": "2026-01-01", "aciertos": 12, "fallos": 3, "precisión": 0.80},
    {"fecha": "2026-04-01", "aciertos": 18, "fallos": 4, "precisión": 0.82},
    {"fecha": "2026-06-01", "aciertos": 22, "fallos": 5, "precisión": 0.82}
  ],
  "referencias_cruzadas": ["P-FI-0010", "P-CF-0003"],
  "estado": "activo",
  "nivel_validacion": "core"
}
```

### 2.3 Atributos del Patrón

| Atributo | Descripción | Valores |
|---|---|---|
| `id` | Identificador único con versión | `P-{CAT}-{NNNN}-v{X.Y}` |
| `tipo` | Naturaleza del patrón | `predictivo`, `descriptivo`, `prescriptivo`, `correlacional` |
| `confianza` | Nivel de confianza del equipo en el patrón (0-1) | 0.0 - 1.0 |
| `soporte_muestral` | Número de diagnósticos que respaldan el patrón | Entero |
| `precision_estimada` | Tasa de aciertos del patrón en predicciones (0-1) | 0.0 - 1.0 |
| `tasa_falsos_positivos` | Proporción de falsas alarmas (0-1) | 0.0 - 1.0 |
| `nivel_validacion` | Estado en el ciclo de vida | `candidato`, `learned`, `core`, `deprecated` |
| `estado` | Estado operativo | `activo`, `en_revision`, `suspendido`, `archivado` |

---

## 3. Ciclo de Consolidación

### 3.1 Diagrama de Flujo General

```
[Diagnóstico Completado]
         │
         ▼
┌─────────────────────────────┐
│ E1: COSECHA                 │  ← Seleccionar diagnósticos para revisión
│   • Evaluar elegibilidad    │
│   • Indexar hallazgos       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ E2: DETECCIÓN DE PATRONES   │  ← Buscar recurrencias en hallazgos
│   • Análisis de frecuencia  │
│   • Correlaciones           │
│   • Identificar candidatos  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ E3: VALIDACIÓN              │  ← Evaluar candidatos
│   • Detectar falsos +       │
│   • Evaluar significancia   │
│   • Calcular confianza      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ E4: DEDUPLICACIÓN           │  ← Evitar duplicados
│   • Buscar en Core+Learned  │
│   • Fusionar si aplica      │
└─────────────┬───────────────┘
              │
        ┌─────┴─────┐
        │           │
   ¿Existe?    ¿Es nuevo?
        │           │
        ▼           ▼
┌───────────┐ ┌─────────────────┐
│ E5:       │ │ E6:             │
│ ENRIQUECER│ │ GENERAR NUEVO   │
│ patrón    │ │ patrón          │
│ existente │ │                 │
└─────┬─────┘ └────────┬────────┘
      │                │
      └───────┬────────┘
              ▼
┌─────────────────────────────┐
│ E7: ACTUALIZAR              │  ← Escribir en Knowledge/Learned
│   Knowledge/Learned         │
│   • Persistir patrón        │
│   • Indexar                 │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ E8: PROPONER A CORE         │  ← Promover si cumple criterios
│   • Evaluar madurez         │
│   • Enviar a revisión       │
│   • Aprobar/rechazar        │
└─────────────────────────────┘
```

### 3.2 Frecuencia de Ejecución

| Modalidad | Disparador | Descripción |
|---|---|---|
| **Continua** | Cada diagnóstico completado | Cosecha inmediata, detección ligera de patrones obvios |
| **Batch semanal** | Cada 7 días | Consolidación completa de todos los diagnósticos de la semana |
| **Batch mensual** | Cada 30 días | Revisión de falsos positivos, re-cálculo de métricas, promociones a Core |
| **Revisión trimestral** | Cada 90 días | Poda de patrones obsoletos, auditoría de calidad del corpus |

### 3.3 Disparadores del Ciclo

| Evento | Acción |
|---|---|
| Diagnóstico completado con severidad crítica | Cosecha inmediata (prioridad alta) |
| Mismo hallazgo detectado en 3+ diagnósticos | Disparar detección de patrón automática |
| Ratio de falsos positivos supera umbral (≥ 20%) | Disparar revisión de patrón |
| Nuevo cliente de industria no cubierta | Disparar búsqueda de lagunas de cobertura |
| Patrón en Learned con 10+ casos de soporte | Disparar evaluación para promoción a Core |

---

## 4. Etapa 1: Cosecha de Diagnósticos

### 4.1 Objetivo
Seleccionar diagnósticos finalizados que sean aptos para extracción de conocimiento, filtrando aquellos con calidad insuficiente o datos anómalos.

### 4.2 Responsable
**Knowledge_Consolidator**

### 4.3 Inputs

| Input | Formato | Fuente |
|---|---|---|
| Diagnóstico completo | `executive_report.md` + `consolidated_findings.json` | Sistema de diagnósticos |
| Resultados de iniciativas implementadas | `initiative_results.json` | Sistema de seguimiento (si existe) |
| Feedback del cliente post-diagnóstico | `client_feedback.json` | Encuesta de satisfacción |

### 4.4 Criterios de Elegibilidad

Un diagnóstico es apto para cosecha si cumple **todos** estos criterios:

- [ ] El diagnóstico se completó (E13 generado)
- [ ] `consolidated_findings.json` contiene al menos 5 hallazgos
- [ ] `root_cause_analysis.json` contiene al menos 2 causas raíz
- [ ] El cliente no reportó insatisfacción severa con el proceso
- [ ] Los datos financieros no fueron marcados como "no fiables" por el Financial_Analyst

### 4.5 Proceso de Cosecha

```
1. Obtener lista de diagnósticos completados desde última cosecha
2. Para cada diagnóstico, aplicar criterios de elegibilidad
3. Si pasa: marcar como "cosechado", extraer metadatos
4. Si no pasa: marcar como "no apto", registrar razón
5. Indexar hallazgos por categoría para facilitar matching
```

### 4.6 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `harvested_diagnostics.json` | JSON | Lista de IDs de diagnósticos aptos para minería |
| `findings_index_by_category.json` | JSON | Hallazgos indexados por categoría (BM, FI, OP, OR, RI) |
| `rejected_diagnostics_log.json` | JSON | Diagnósticos rechazados con motivo |
| `harvest_report.md` | Markdown | Resumen de la cosecha |

### 4.7 Reglas de Decisión

| Condición | Acción |
|---|---|
| Diagnóstico con < 5 hallazgos | Rechazar, insuficiente riqueza |
| Datos financieros marcados "no fiables" | Aceptar solo para patrones no financieros |
| Cliente insatisfecho | Rechazar, posible sesgo en la información |
| Diagnóstico de modo "Fast Track" | Aceptar pero marcar como "cobertura parcial" |
| Diagnóstico con industria nueva | Aceptar con prioridad alta (amplía cobertura) |

---

## 5. Etapa 2: Detección de Patrones

### 5.1 Objetivo
Identificar recurrencias, correlaciones y regularidades en los hallazgos cosechados que puedan constituir patrones transferibles a futuros diagnósticos.

### 5.2 Responsable
**Knowledge_Consolidator**

### 5.3 Métodos de Detección

#### 5.3.1 Detección por Frecuencia
```
Para cada categoría de hallazgo:
  1. Agrupar hallazgos por descripción normalizada (stemming + stopwords)
  2. Contar ocurrencias de cada grupo
  3. Si ocurrencias ≥ umbral_frecuencia → candidato a patrón

Umbral de activación:
  - Patrones generales: ≥ 5 ocurrencias
  - Patrones por industria: ≥ 3 ocurrencias
  - Patrones por tamaño de empresa: ≥ 3 ocurrencias
```

#### 5.3.2 Detección por Correlación
```
Para cada par de hallazgos (Hx, Hy):
  1. Calcular coeficiente de correlación (Cramér's V para categóricas)
  2. Si V > 0.6 y p < 0.05 → correlación significativa
  3. Evaluar si la correlación tiene sentido causal
  4. Si sí → candidato a patrón correlacional
```

#### 5.3.3 Detección por Secuencia Temporal
```
Para diagnósticos con seguimiento post-iniciativa:
  1. Identificar secuencias: (hallazgo → iniciativa → resultado)
  2. Si misma secuencia aparece ≥ 3 veces con éxito → patrón prescriptivo
  3. Si misma secuencia aparece ≥ 2 veces con fracaso → contra-patrón
```

#### 5.3.4 Detección por Desviación de Benchmark
```
Para cada hallazgo que compare contra la base de conocimiento:
  1. Si el hallazgo contradice un patrón existente en Core
  2. Y aparece ≥ 3 veces → posible excepción o evolución del patrón
  3. Registrar como "candidato a revisión de patrón existente"
```

### 5.4 Algoritmo de Priorización de Candidatos

```python
score_candidato = (
    0.30 * frecuencia_relativa +
    0.25 * significancia_estadistica +
    0.20 * impacto_promedio +
    0.15 * novedad (inverso de cobertura en Core) +
    0.10 * diversidad_muestral (industrias distintas)
)
```

Los candidatos con `score > 0.7` se procesan inmediatamente.
Los candidatos con `score 0.4-0.7` se acumulan para el batch semanal.
Los candidatos con `score < 0.4` se descartan o se siguen monitoreando.

### 5.5 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `pattern_candidates.json` | JSON | Lista de candidatos con score, frecuencia, diagnóstico origen |
| `correlation_matrix.json` | JSON | Matriz de correlaciones entre hallazgos |
| `temporal_sequences.json` | JSON | Secuencias hallazgo → iniciativa → resultado |
| `benchmark_deviations.json` | JSON | Desviaciones respecto a patrones existentes |

### 5.6 Reglas de Decisión

| Condición | Acción |
|---|---|
| Frecuencia ≥ 5 en misma categoría | Promover a candidato automático |
| Correlación Hallazgo A ↔ Hallazgo B (V > 0.7) | Crear patrón de co-ocurrencia |
| Secuencia hallazgo→iniciativa→éxito repetida 3+ | Crear patrón prescriptivo |
| Patrón existente contradicho 3+ veces | Iniciar revisión del patrón existente |
| Score < 0.4 | Archivar como "observación", no generar candidato |
| Misma industria, mismo hallazgo en 3+ casos | Patrón industria-específico |

---

## 6. Etapa 3: Validación y Falsos Positivos

### 6.1 Objetivo
Evaluar la validez estadística y sustantiva de cada candidato a patrón, descartando falsos positivos (correlaciones espurias, sesgos muestrales, ruido).

### 6.2 Responsable
**Knowledge_Consolidator** (con apoyo de **Domain_Validator** para validación sustantiva)

### 6.3 Proceso de Validación

```
Para cada candidato:

1. VALIDACIÓN ESTADÍSTICA
   a. Calcular significancia (p-value, chi-cuadrado, o prueba exacta de Fisher)
   b. Calcular intervalo de confianza (95%)
   c. Si n < 5 → marcar como "evidencia insuficiente"
   d. Si p > 0.10 → descartar como falso positivo
   
2. VALIDACIÓN SUSTANTIVA (Domain_Validator)
   a. ¿El patrón tiene sentido causal?
   b. ¿Hay una explicación lógica?
   c. ¿Contradice conocimiento establecido?
   d. Evaluar: soportar, rechazar, o marcar "requiere investigación"
   
3. CÁLCULO DE CONFIANZA PRELIMINAR
   confianza = 
     0.50 * (1 - p_value) +
     0.30 * (soporte_muestral / soporte_ideal) +
     0.20 * validacion_sustantiva (0/0.5/1.0)
   
4. CLASIFICACIÓN FINAL
   confianza ≥ 0.80 → Validado, pasar a E4
   confianza 0.50-0.79 → Validez condicional, pasar a Learned
   confianza < 0.50 → Rechazado, registrar como falso positivo
```

### 6.4 Detección de Falsos Positivos

#### 6.4.1 Causas Comunes de Falsos Positivos

| Causa | Descripción | Cómo Detectarlo |
|---|---|---|
| **Sesgo de selección** | La muestra no es representativa | Comparar distribución de la muestra vs población objetivo |
| **Correlación espuria** | Dos variables correlacionadas por causalidad externa | Validar con Domain_Validator |
| **Ruido muestral** | Muestra demasiado pequeña para ser significativa | n < 5 sin importar correlación |
| **Sobreajuste** | Patrón demasiado específico a un caso | Probar si se cumple en otros diagnósticos |
| **Sesgo de confirmación** | El agente busca evidencia que confirme su hipótesis | Revisión cruzada por Domain_Validator distinto |

#### 6.4.2 Test de Robustez

Para cada candidato con confianza ≥ 0.70, ejecutar:

```
1. Jackknife: Recalcular patrón omitiendo cada diagnóstico uno por uno
   - Si el patrón desaparece al omitir 1 diagnóstico → inestable → bajar confianza
   
2. Sub-muestreo: Calcular patrón en subconjuntos aleatorios (80% muestra)
   - Si la varianza entre subconjuntos es alta → patrón frágil → bajar confianza
```

### 6.5 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `validated_patterns.json` | JSON | Patrones validados con confianza, p-value, decisión |
| `false_positives_log.json` | JSON | Registro de candidatos rechazados con causa |
| `validation_rationale.md` | Markdown | Justificación detallada por patrón validado/rechazado |

### 6.6 Reglas de Decisión

| Condición | Acción |
|---|---|
| p > 0.10 | Descartar como falso positivo |
| n < 5 + confianza < 0.50 | Descartar, evidencia insuficiente |
| n < 5 + confianza ≥ 0.80 | Pasar a Learned, marcar como "débil, monitorear" |
| Domain_Validator rechaza | Descartar aunque estadística sea significativa |
| Test Jackknife inestable | Reducir confianza en 0.15 |
| Falso positivo recurrente (misma causa) | Crear regla para filtrar automáticamente en E2 |

---

## 7. Etapa 4: Deduplicación

### 7.1 Objetivo
Evitar que patrones duplicados o solapados ingresen al sistema, garantizando un corpus limpio y no redundante.

### 7.2 Responsable
**Knowledge_Consolidator**

### 7.3 Método de Deduplicación

```
Para cada patrón candidato validado (P_candidato):

1. BUSCAR EN KNOWLEDGE/CORE
   a. Calcular similitud textual (TF-IDF + cosine similarity) con todos
      los patrones activos en Core (misma categoría)
   b. Si similitud ≥ 0.85 → DUPLICADO EXACTO
   c. Si similitud 0.60-0.84 → SOLAPADO / VARIANTE

2. BUSCAR EN KNOWLEDGE/LEARNED
   a. Mismo proceso que en Core
   b. Si existe en Learned → fusionar soporte muestral

3. CLASIFICAR RESULTADO
   - DUPLICADO EXACTO → No crear nuevo; incrementar soporte del existente
   - SOLAPADO → Evaluar si es variante o si merece fusión/separación
   - NUEVO → Continuar a E6
```

### 7.4 Matriz de Decisión de Duplicados

| Similitud | En Core | En Learned | Acción |
|---|---|---|---|
| ≥ 0.85 | Sí | — | Incrementar soporte del patrón Core + recalcular confianza |
| ≥ 0.85 | No | Sí | Incrementar soporte del patrón Learned |
| 0.60-0.84 | Sí | — | Evaluar si es variante (crear como sub-patrón) o fusión |
| 0.60-0.84 | No | Sí | Fusionar soporte, enriquecer descripción |
| < 0.60 | — | — | Patrón nuevo, continuar a E6 |

### 7.5 Reglas de Fusión

Cuando dos patrones se fusionan:

```
Nuevo soporte = soporte_A + soporte_B - solapamiento
Nueva confianza = (confianza_A * soporte_A + confianza_B * soporte_B) / nuevo_soporte
Nueva descripción = fusión de ambas descripciones (más completa)
Orígenes = concatenar listas de diagnóstico_id
ID = mantener el más antiguo, marcar el otro como "fusionado_en: ID_principal"
```

### 7.6 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `deduplication_results.json` | JSON | Resultado por candidato (nuevo, duplicado, fusionado, solapado) |
| `merged_patterns_log.json` | JSON | Registro de fusiones realizadas |
| `dedup_summary.md` | Markdown | Resumen del proceso de deduplicación |

### 7.7 Reglas de Decisión

| Condición | Acción |
|---|---|
| Similitud ≥ 0.85 | No crear, incrementar soporte del existente |
| Solapado con patrón Core que tiene confianza < 0.60 | Reemplazar por el nuevo si confianza nueva > existente |
| Solapado parcial (0.60-0.70) y misma industria | Crear como variante industrial |
| 5+ variantes del mismo patrón base | Consolidar en un patrón general + tabla de variantes |

---

## 8. Etapa 5: Enriquecimiento de Patrones Existentes

### 8.1 Objetivo
Mejorar la calidad, precisión y cobertura de patrones existentes en Knowledge/Learned y Knowledge/Core usando nueva evidencia de diagnósticos recientes.

### 8.2 Responsable
**Knowledge_Consolidator** + **Domain_Validator**

### 8.3 Tipos de Enriquecimiento

| Tipo | Descripción | Cuándo Aplicar |
|---|---|---|
| **Soporte muestral** | Incrementar n del patrón | Nuevo caso confirma el patrón |
| **Precisión** | Recalcular tasa de aciertos | Nuevo caso con resultado conocido |
| **Cobertura industrial** | Añadir industria al rango de aplicación | Patrón se cumple en industria distinta |
| **Condiciones** | Refinar condiciones de aplicación | Se descubre límite o excepción |
| **Contra-ejemplo** | Documentar excepción conocida | Se identifica caso donde no aplica |
| **Correlación** | Añadir referencia a otro patrón | Se descubre relación con otro patrón |

### 8.4 Proceso de Enriquecimiento

```
Para cada patrón existente que coincide con un hallazgo nuevo:

1. ACTUALIZAR MÉTRICAS
   a. Nuevo soporte_muestral = anterior + 1
   b. Si hay resultado conocido, recalcular precisión
   c. Recalcular tasa de falsos positivos
   
2. VERIFICAR CONDICIONES
   a. ¿El nuevo caso cumple las condiciones de aplicación?
   b. Si no, evaluar si las condiciones deben ampliarse
   
3. VERIFICAR INDUSTRIA
   a. ¿La industria del nuevo caso ya está cubierta?
   b. Si no, añadir industria al patrón
   
4. ACTUALIZAR metrica_historial
   a. Añadir nuevo entry con fecha y resultado
   
5. SI procede: ACTUALIZAR descripción
   a. Mejorar redacción si nueva evidencia aporta matices
   b. Añadir contra-ejemplo si aplica
```

### 8.5 Versionado del Enriquecimiento

Cada enriquecimiento incrementa el versionado del patrón:

| Cambio | Versión | Ejemplo |
|---|---|---|
| Solo soporte muestral | Patch (X.Y → X.Y+1) | v2.1 → v2.2 |
| Nueva industria o condición | Minor (X.Y → X+1.0) | v2.2 → v3.0 |
| Cambio de descripción o confianza | Minor (X.Y → X+1.0) | v3.0 → v4.0 |
| Cambio de nivel validación (Learned→Core) | Major (X.Y → X+1.0) + cambio de nivel | v4.0 learned → v5.0 core |

### 8.6 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `enriched_patterns.json` | JSON | Patrones actualizados con nuevas métricas |
| `enrichment_log.json` | JSON | Registro detallado de cambios por patrón |
| `coverage_expansion_report.md` | Markdown | Reporte de expansión de cobertura por industria |

### 8.7 Reglas de Decisión

| Condición | Acción |
|---|---|
| Nuevo caso confirma patrón existente | Incrementar soporte, recalcular confianza |
| Nuevo caso contradice patrón | Documentar contra-ejemplo, reducir confianza en 0.05 |
| Patrón se cumple en nueva industria | Añadir industria, incrementar minor version |
| 3+ contra-ejemplos del mismo tipo | Iniciar revisión completa del patrón |
| Confianza cae por debajo de 0.50 | Mover a estado "en_revision" |

---

## 9. Etapa 6: Generación de Nuevos Patrones

### 9.1 Objetivo
Crear nuevos patrones formales a partir de candidatos validados, no duplicados, con la estructura y metadatos completos.

### 9.2 Responsable
**Knowledge_Consolidator**

### 9.3 Proceso de Generación

```
1. RECIBIR candidato validado y no duplicado (de E3 + E4)

2. ASIGNAR ID único:
   P-{CATEGORIA}-{CONTADOR_GLOBAL_PAD A 4 DÍGITOS}-v1.0

3. COMPLETAR ESQUEMA DEL PATRÓN:
   a. Titulo: generado automáticamente del hallazgo recurrente
   b. Descripción: redactada por Knowledge_Consolidator
   c. Tipo: clasificar según naturaleza
   d. Categoria: heredada del hallazgo original
   e. Confianza: heredada de E3
   f. Soporte_muestral: n de ocurrencias
   g. Precisión_estimada: si hay datos de seguimiento
   h. Tasa_falsos_positivos: 1 - precisión (o 0 si no hay datos)
   i. Condiciones_aplicación: inferidas de los casos de origen

4. REGISTRAR ORIGEN:
   a. diagnostico_id de cada caso donde se observó
   b. hallazgo_id específico
   c. Fecha del primer caso

5. CLASIFICAR NIVEL:
   - Si confianza ≥ 0.80 y n ≥ 10 → "core" (pasa directamente a revisión)
   - Si confianza ≥ 0.50 y n ≥ 3 → "learned"
   - Si confianza ≥ 0.50 y n < 3 → "candidato" (monitorear)
```

### 9.4 Clasificación Automática de Tipo de Patrón

| Tipo | Criterio | Ejemplo |
|---|---|---|
| **predictivo** | El hallazgo precede a un resultado | "PyMEs con X presentan Y en 12 meses" |
| **descriptivo** | Describe una característica recurrente | "El 70% de PyMEs familiares no tiene plan de sucesión" |
| **prescriptivo** | Recomienda una acción con resultado conocido | "Implementar Z reduce Y en un 30%" |
| **correlacional** | Dos hallazgos aparecen juntos frecuentemente | "X y Y co-ocurren en el 80% de los casos" |

### 9.5 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `new_patterns.json` | JSON | Nuevos patrones generados con esquema completo |
| `new_patterns_summary.md` | Markdown | Resumen de nuevos patrones por categoría |

### 9.6 Reglas de Decisión

| Condición | Acción |
|---|---|
| Candidato validado con n ≥ 10 y confianza ≥ 0.80 | Generar patrón y proponer directamente a Core |
| Candidato validado con n ≥ 3 | Generar patrón en Learned |
| Candidato con n < 3 | Generar como "candidato", monitorear próximos diagnósticos |
| Patrón predictivo sin dato temporal | Marcar como "descriptivo" hasta tener seguimiento |
| Patrón con condiciones de aplicación muy específicas | Validar si es generalizable o es ruido |

---

## 10. Etapa 7: Actualización de Knowledge/Learned

### 10.1 Objetivo
Persistir los patrones nuevos y enriquecidos en Knowledge/Learned, manteniendo el índice actualizado y garantizando la integridad del repositorio de conocimiento experimental.

### 10.2 Responsable
**Knowledge_Consolidator**

### 10.3 Estructura de Knowledge/Learned

```
Knowledge/
  Learned/
    patterns/
      business_model/
        P-BM-0001-v1.0.json
        P-BM-0002-v2.1.json
        ...
      financial/
        P-FI-0001-v1.0.json
        ...
      cashflow/
      sales/
      marketing/
      customer/
      process/
      risk/
      organization/
      strategy/
    indexes/
      by_industry.json
      by_company_size.json
      by_pattern_type.json
      cross_references.json
    logs/
      change_log.jsonl
      promotion_log.json
    metrics/
      learned_metrics.json
```

### 10.4 Proceso de Actualización

```
1. PRE-VALIDACIÓN DE ESCRITURA
   a. Verificar que el patrón tenga esquema completo
   b. Verificar que el ID no exista ya en Learned
   c. Verificar que el patrón no esté duplicado en Core

2. ESCRITURA
   a. Escribir archivo JSON del patrón en la subcarpeta correspondiente
   b. Actualizar índices (by_industry, by_size, by_type)
   c. Registrar en change_log.jsonl (timestamp, acción, patrón_id, versión)
   
3. POST-VALIDACIÓN
   a. Leer el archivo escrito y verificar integridad
   b. Verificar que los índices incluyen el nuevo patrón
   
4. NOTIFICACIÓN
   a. Si es patrón nuevo: notificar a los agentes de diagnóstico
   b. Si es enriquecimiento: notificar solo si cambia la confianza > 0.10
```

### 10.5 Outputs

| Output | Formato | Descripción |
|---|---|---|
| Patrones actualizados en filesystem | JSON | Archivos de patrón persistidos |
| `change_log.jsonl` | JSONL | Log de cambios (append-only) |
| `indexes_updated.json` | JSON | Confirmación de índices actualizados |

### 10.6 Reglas de Decisión

| Condición | Acción |
|---|---|
| Patrón con esquema incompleto | Rechazar escritura, devolver a E6 |
| ID duplicado en Learned | Rechazar, iniciar deduplicación forzada |
| Error de escritura | Reintentar 2 veces, si persiste escalar a operador humano |
| Cambio de confianza > 0.15 en enriquecimiento | Notificar a agentes de diagnóstico |
| Más de 100 patrones en Learned sin revisión trimestral | Disparar revisión de promociones |

---

## 11. Etapa 8: Propuesta a Knowledge/Core

### 11.1 Objetivo
Evaluar patrones de Knowledge/Learned para su promoción a Knowledge/Core, el repositorio canónico y validado del sistema.

### 11.2 Responsable
**Knowledge_Reviewer** (rol con capacidad de aprobación)

### 11.3 Criterios de Promoción a Core

Para que un patrón en Learned sea candidato a Core, debe cumplir **todos** estos criterios:

- [ ] **Madurez temporal**: Mínimo 60 días desde su creación en Learned
- [ ] **Soporte muestral mínimo**: n ≥ 10 diagnósticos
- [ ] **Confianza mínima**: ≥ 0.80
- [ ] **Tasa de falsos positivos**: ≤ 15%
- [ ] **Diversidad muestral**: Proviene de al menos 3 industrias distintas (o justificar aplicabilidad)
- [ ] **Validación sustantiva**: Aprobado por Domain_Validator del área correspondiente
- [ ] **Sin contradicciones**: No contradice ningún patrón activo en Core (o se propone la actualización del existente)
- [ ] **Documentación completa**: Descripción, condiciones, orígenes, métricas historiales

### 11.4 Proceso de Revisión y Aprobación

```
INICIO: Patrón candidato a Core
   │
   ▼
1. REVISIÓN AUTOMÁTICA (Knowledge_Consolidator)
   ├── Verificar criterios de promoción
   ├── Generar reporte de evaluación
   └── Si no cumple: devolver a Learned con recomendaciones
   │
2. REVISIÓN POR DOMAIN_VALIDATOR
   ├── Evaluar validez sustantiva
   ├── Evaluar impacto en diagnósticos existentes
   └── Votar: APROBAR / RECHAZAR / SOLICITAR MÁS DATOS
   │
3. REVISIÓN POR KNOWLEDGE_REVIEWER
   ├── Revisar evaluación y voto del Domain_Validator
   ├── Evaluar consistencia global con Core
   ├── Verificar que no haya conflictos con otros patrones Core
   └── Decisión final: APROBAR / RECHAZAR / DEVOLVER
   │
4. EJECUCIÓN (si aprobado)
   ├── Copiar patrón de Learned/ a Core/
   ├── Actualizar nivel_validacion → "core"
   ├── Registrar en change_log y promotion_log
   ├── Notificar a todos los agentes
   └── Eliminar de Learned (o marcar como "promovido")
   │
   ▼
FIN: Patrón promovido a Core
```

### 11.5 Flujo de Votación

| Voto Domain_Validator | Veto Knowledge_Reviewer | Resultado |
|---|---|---|
| Aprobar | Aprobar | **Promovido a Core** |
| Aprobar | Rechazar (con motivo) | Devuelto a Learned + retroalimentación |
| Rechazar (con motivo) | — | Devuelto a Learned + plan de mejora |
| Solicitar más datos | — | Pasa a estado "en_observación" en Learned |

### 11.6 Outputs

| Output | Formato | Descripción |
|---|---|---|
| `core_promotion_candidates.json` | JSON | Lista de candidatos evaluados para promoción |
| `promotion_approval_record.json` | JSON | Registro de aprobaciones con votos y justificación |
| `core_update_notification.json` | JSON | Notificación a agentes sobre cambios en Core |
| `learned_deprecation_log.json` | JSON | Patrones retirados de Learned tras promoción |

### 11.7 Reglas de Decisión

| Condición | Acción |
|---|---|
| Patrón cumple todos los criterios | Iniciar proceso de revisión |
| Domain_Validator rechaza | Devolver a Learned, no puede apelarse sin nueva evidencia |
| Knowledge_Reviewer rechaza | Devolver con retroalimentación escrita |
| Patrón promovido a Core | Notificar a todos los agentes, actualizar índices globales |
| Patrón en Learned sin actividad 6 meses | Evaluar archivado (pasar a "deprecated") |
| Confianza en Core cae < 0.70 post-promoción | Mover a "en_revision", posible degradación a Learned |

---

## 12. Control de Calidad y Versionado

### 12.1 Dimensiones de Calidad del Conocimiento

| Dimensión | Métrica | Estándar | Frecuencia |
|---|---|---|---|
| **Precisión** | Tasa de aciertos en predicciones | ≥ 80% | Mensual |
| **Cobertura** | % de hallazgos explicables por patrones Core | ≥ 70% | Trimestral |
| **Frescura** | Edad media de patrones Core | ≤ 18 meses | Trimestral |
| **Consistencia** | % de patrones sin contradicciones internas | ≥ 95% | Trimestral |
| **No redundancia** | % de patrones únicos (sin duplicados) | 100% | Continuo |
| **Utilidad** | % de patrones usados en ≥ 1 diagnóstico/mes | ≥ 60% | Mensual |

### 12.2 Versionado del Conocimiento

#### 12.2.1 Versionado de Patrones Individuales

Formato: `P-{CAT}-{NNNN}-v{MAJOR}.{MINOR}`

| Incremento | Cuándo | Ejemplo |
|---|---|---|
| **MAJOR** | Cambio de nivel (Learned ↔ Core), cambio de descripción sustancial, cambio de tipo | v2.3 → v3.0 |
| **MINOR** | Enriquecimiento, nuevo soporte, ajuste de confianza, nuevas condiciones | v2.3 → v2.4 |

#### 12.2.2 Versionado del Corpus Completo

Cada vez que se ejecuta una consolidación batch, se genera una versión del corpus:

```
Knowledge_Corpus-v{YYYY}.{MM}.{DD}-{NRO_CONSOLIDACION_MENSUAL}
Ejemplo: Knowledge_Corpus-v2026.06.15-02
```

#### 12.2.3 Changelog Centralizado

```
Formato: JSONL (una línea por evento)

{"timestamp": "2026-06-15T10:30:00Z", "accion": "creacion", "id": "P-FI-0042-v1.0", "nivel": "learned", "diagnostico_origen": "D-2026-042", "usuario": "Knowledge_Consolidator"}
{"timestamp": "2026-06-15T10:35:00Z", "accion": "enriquecimiento", "id": "P-FI-0042-v1.1", "cambios": ["soporte_muestral: 4→5", "confianza: 0.82→0.83"], "usuario": "Knowledge_Consolidator"}
{"timestamp": "2026-07-01T09:00:00Z", "accion": "promocion", "id": "P-FI-0042-v2.0", "nivel_origen": "learned", "nivel_destino": "core", "aprobado_por": "Knowledge_Reviewer"}
```

### 12.3 Podado y Archivado

Cada ciclo trimestral se ejecuta:

```
1. Identificar patrones candidatos a archivado:
   - Sin uso en últimos 6 meses (no referenciados en diagnósticos)
   - Confianza < 0.50 sostenida
   - Reemplazados por patrón más preciso
   
2. Para cada candidato:
   - Mover a Knowledge/Archived/{año}/
   - Cambiar estado → "archivado"
   - Registrar razón de archivado
   
3. Notificar a agentes sobre patrones archivados que pudieran estar en uso
```

### 12.4 Outputs de Calidad

| Output | Formato | Frecuencia | Descripción |
|---|---|---|---|
| `quality_report_weekly.md` | Markdown | Semanal | Métricas de calidad del conocimiento |
| `quality_report_monthly.md` | Markdown | Mensual | Reporte detallado con tendencias |
| `corpus_version_snapshot.json` | JSON | Por consolidación | Estado completo del corpus en un punto |
| `archived_patterns_log.json` | JSON | Trimestral | Patrones archivados con razón |

---

## 13. Gobierno del Conocimiento

### 13.1 Roles y Responsabilidades

| Rol | Nombre en el Sistema | Responsabilidades |
|---|---|---|
| **Knowledge_Consolidator** | Agente automático (Master_Diagnosis_Orchestrator) | Ejecutar ciclo E1-E7, mantener índices, generar reportes |
| **Domain_Validator** | Agente especializado (Business_Model_Analyst, Financial_Analyst, etc.) | Validar sustantivamente patrones de su dominio |
| **Knowledge_Reviewer** | Humano o agente senior | Aprobar/rechazar promociones a Core, decidir archivados |
| **Knowledge_Architect** | Humano | Diseñar evolución del sistema, resolver conflictos de esquema |

### 13.2 Políticas de Operación

| Política | Descripción |
|---|---|
| **Inmediata** | Patrones con confianza ≥ 0.90 y n ≥ 20 pueden saltarse el período de espera en Learned |
| **Derecho a réplica** | Un patrón rechazado puede volver a proponerse tras 3 nuevos casos de soporte |
| **Transparencia** | Todos los cambios son registrados y trazables al agente que los ejecutó |
| **Reversibilidad** | Toda promoción a Core es reversible si nueva evidencia la contradice |
| **Congelamiento** | En caso de error crítico, el corpus puede congelarse (modo read-only) mientras se investiga |
| **Cuarentena** | Patrones sospechosos se mueven a "cuarentena" sin eliminar, para investigación |

### 13.3 Conflictos y Resolución

| Tipo de Conflicto | Resolución |
|---|---|
| Patrón nuevo contradice patrón Core | No promover hasta que Knowledge_Reviewer decida cuál prevalece |
| Domain_Validator y Knowledge_Consolidator discrepan | Knowledge_Reviewer decide, documenta razón |
| Dos patrones Core se contradicen | Priorizar el de mayor soporte muestral; marcar el otro como "en_revision" |
| Agente de diagnóstico ignora patrón Core | Investigar por qué; puede ser falso positivo o necesidad de recalibración |

---

## 14. Métricas del Sistema

### 14.1 Dashboard de Conocimiento

El sistema mantiene un dashboard actualizado con:

```json
{
  "fecha_medicion": "2026-06-15",
  "corpus_version": "2026.06.15-02",
  "metrics": {
    "core": {
      "total_patterns": 245,
      "by_category": {
        "business_model": 32,
        "financial": 41,
        "cashflow": 18,
        "sales": 28,
        "marketing": 22,
        "customer": 35,
        "process": 24,
        "risk": 19,
        "organization": 16,
        "strategy": 10
      },
      "avg_confidence": 0.87,
      "avg_precision": 0.84,
      "avg_false_positive_rate": 0.09,
      "coverage": 0.73,
      "avg_age_days": 210
    },
    "learned": {
      "total_patterns": 89,
      "avg_confidence": 0.71,
      "avg_support": 5.2,
      "pending_review": 12
    },
    "activity": {
      "diagnostics_harvested_this_month": 18,
      "new_patterns_this_month": 7,
      "enrichments_this_month": 23,
      "promotions_this_month": 3,
      "false_positives_this_month": 2
    },
    "trends": {
      "precision_trend_last_6_months": [0.81, 0.82, 0.83, 0.83, 0.84, 0.84],
      "coverage_trend_last_6_months": [0.65, 0.67, 0.68, 0.70, 0.72, 0.73],
      "new_pattern_rate_per_month": 8.5
    }
  }
}
```

### 14.2 Alertas del Sistema de Conocimiento

| Alerta | Disparador | Acción |
|---|---|---|
| **Cobertura baja** | Cobertura < 60% | Disparar búsqueda proactiva de patrones en áreas descubiertas |
| **Precisión en declive** | Precisión baja 2+ meses consecutivos | Revisar calidad de patrones, posible deterioro |
| **Falsos positivos altos** | Tasa FP > 20% mensual | Revisar proceso de validación (E3) |
| **Estancamiento** | 0 patrones nuevos en 30 días | Revisar cosecha, posible falta de diagnósticos diversos |
| **Deuda técnica** | > 50 patrones en Learned sin revisar | Forzar revisión trimestral anticipada |

### 14.3 Ciclo de Mejora del Propio Sistema

El sistema de consolidación se evalúa a sí mismo cada 6 meses:

```
1. Evaluar si el ciclo de consolidación está generando valor:
   - ¿Ha mejorado la precisión de los diagnósticos?
   - ¿Se han reducido los falsos positivos?
   - ¿Los agentes usan los patrones generados?
   
2. Identificar cuellos de botella en el proceso:
   - ¿Dónde se acumulan los retrasos?
   - ¿Hay etapas que podrían automatizarse más?
   
3. Proponer mejoras al playbook:
   - Ajustar umbrales
   - Nuevos métodos de detección
   - Nuevas fuentes de datos
```

---

*Fin del documento — Knowledge_Consolidation.md v1.0*
