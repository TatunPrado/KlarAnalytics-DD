---
name: risk-scoring
description: >
  Sistema de scoring multidimensional. Asigna puntuación 0-100 por factor de riesgo
  (financiero, legal, tributario, AML, reputacional, operativo, compliance), genera
  matriz impacto/probabilidad, risk wheel y nivel de riesgo general.
---

# Risk Scoring System

Sistema integral de scoring, matriz de riesgos y visualización de criticidad.

## ESCALA DE RIESGO

| Nivel | Rango | Color | Descripción |
|-------|-------|-------|-------------|
| Bajo | 0–20 | #10B981 | Sin hallazgos relevantes |
| Bajo-Medio | 21–40 | #34D399 | Hallazgos menores, controlables |
| Medio | 41–60 | #F59E0B | Hallazgos que requieren monitoreo |
| Alto | 61–80 | #EF4444 | Hallazgos graves, requieren acción |
| Crítico | 81–100 | #7F1D1D | Hallazgos que impiden continuar |

## FACTORES DE RIESGO

### 1. Riesgo Financiero (RF)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Clasificación BCRA (1-6) | 30% | 6→80, 5→65, 4→50, 3→35, 2→20, 1→10 |
| Cheques rechazados | 20% | Frecuencia + monto |
| Relación deuda/patrimonio | 20% | >2→70, 1-2→50, <1→20 |
| Resultado del ejercicio | 15% | Pérdida→70, equilibrio→40, superávit→10 |
| Sanciones cambiarias | 15% | Sí→80, No→0 |

### 2. Riesgo Tributario (RT)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Estado ARCA (activo/inactivo) | 25% | Inactivo→100 |
| Deudas fiscales (públicas) | 25% | Existencia→60+ |
| Embargos fiscales | 25% | Sí→80 |
| Categoría (Monotributo vs RI) | 15% | No relevante en PJ |
| IIBB / Convenio Multilateral | 10% | Incumplimiento→70 |

### 3. Riesgo Legal (RL)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Causas judiciales activas | 35% | Cantidad + gravedad |
| Embargos / inhibiciones | 25% | Sí→70+ |
| Sumarios administrativos | 20% | Gravedad |
| Condenas previas | 20% | Sí→90 |

### 4. Riesgo AML (RA)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Coincidencia OFAC/ONU/UE | 40% | Directa→100 |
| Posible coincidencia fonética | 15% | 40 |
| PEP (Persona Políticamente Expuesta) | 20% | Sí→50 |
| Estructura societaria compleja | 15% | Sin justificación→60 |
| Jurisdicción no cooperante | 10% | Sí→50 |

### 5. Riesgo Reputacional (RR)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Noticias negativas graves | 35% | Cantidad + gravedad |
| Noticias negativas menores | 15% | Cantidad |
| Controversias públicas | 20% | Sí→60+ |
| Riesgos en redes sociales | 15% | Gravedad |
| Antigüedad positiva (+5 años sin incidentes) | 15% | -20 puntos |

### 6. Riesgo Operativo (RO)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| Dependencia de un solo cliente/proveedor | 30% | >50%→65 |
| Concentración geográfica | 20% | Una sola locación→40 |
| Antigüedad de la empresa | 20% | <1 año→60 |
| Cantidad de empleados | 15% | <5→40 |
| Cambios frecuentes de autoridades | 15% | >2 cambios/año→50 |

### 7. Riesgo Compliance / Integridad (RC)
| Indicador | Peso | Scoring |
|-----------|------|---------|
| PEP o vínculos con PEP | 30% | Sí→60+ |
| Contrataciones con el Estado sin control | 25% | Monto elevado→60 |
| Inhabilitaciones para contratar | 25% | Sí→80 |
| Causas de corrupción / soborno | 20% | Sí→90 |

## CÁLCULO DEL RIESGO GENERAL

```
RGeneral = (RF * 0.20) + (RT * 0.15) + (RL * 0.20) + (RA * 0.20) + (RR * 0.10) + (RO * 0.05) + (RC * 0.10)
```

## MATRIZ IMPACTO vs PROBABILIDAD

```
                IMPACTO
            Bajo  Medio  Alto  Crítico
          ┌─────┬──────┬──────┬────────┐
Prob Alto │Medio│ Alto │ Crít │ Crít   │
├─────┼──────┼──────┼────────┤
Prob Med  │Bajo │ Medio│ Alto │ Crít   │
├─────┼──────┼──────┼────────┤
Prob Bajo │Bajo │ Bajo │ Medio│ Alto   │
└─────┴──────┴──────┴────────┘
```

| Código | Rango | Color |
|--------|-------|-------|
| Bajo | 0–25 | #10B981 |
| Medio | 26–50 | #F59E0B |
| Alto | 51–75 | #EF4444 |
| Crítico | 76–100 | #7F1D1D |

## RISK WHEEL (7 dimensiones)

```
                Financiero
                    │
              ╱    ╱│╲    ╲
   Compliance ◀──  │  ──▶ Legal
              ╲    │╱    ╱
          ╲    ╲   │   ╱    ╱
   Operativo ◀──── ┼ ────▶ Tributario
           ╱    ╱  │  ╲    ╲
              ╱   │││   ╲
        Reputacional AML
```

Cada eje se puntúa 0-100. El área del polígono representa el riesgo global.
A mayor área, mayor riesgo.

## SALIDA

```json
{
  "riesgo_general": {
    "score": 0-100,
    "nivel": "bajo|medio|alto|critico",
    "color": "#hex"
  },
  "factores": {
    "financiero": {"score": 0-100, "nivel": "...", "peso": 0.20},
    "tributario": {"score": 0-100, "nivel": "...", "peso": 0.15},
    "legal": {"score": 0-100, "nivel": "...", "peso": 0.20},
    "aml": {"score": 0-100, "nivel": "...", "peso": 0.20},
    "reputacional": {"score": 0-100, "nivel": "...", "peso": 0.10},
    "operativo": {"score": 0-100, "nivel": "...", "peso": 0.05},
    "compliance": {"score": 0-100, "nivel": "...", "peso": 0.10}
  },
  "matriz_impacto_probabilidad": {
    "impacto": "bajo|medio|alto|critico",
    "probabilidad": "baja|media|alta",
    "resultado": "bajo|medio|alto|critico"
  },
  "risk_wheel": {
    "ejes": {
      "financiero": 0-100,
      "legal": 0-100,
      "tributario": 0-100,
      "aml": 0-100,
      "reputacional": 0-100,
      "operativo": 0-100,
      "compliance": 0-100
    }
  },
  "recomendacion": "aprobar|aprobar_con_mitigaciones|rechazar"
}
```

## REGLAS

- Todo score debe basarse en evidencia real.
- Si no hay datos para un factor, asignar score = 0 con observación "sin datos".
- No inflar scores sin justificación.
- La recomendación final se basa en el riesgo general:
  - 0–25: Aprobar
  - 26–50: Aprobar con mitigaciones
  - 51–75: Rechazar (requiere revisión de Compliance)
  - 76–100: Rechazar
