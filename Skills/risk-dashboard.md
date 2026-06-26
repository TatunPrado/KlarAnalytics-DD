---
name: risk-dashboard
description: >
  Generar un dashboard ejecutivo de riesgos multidimensional. Incluye riesgo
  general, financiero, legal, tributario, reputacional, compliance y operativo,
  expresados numérica, gráfica y visualmente con semáforos, barras y scoring.
---

# Risk Dashboard

Generar dashboard ejecutivo de riesgos con visualización multidimensional.

## PANELES DEL DASHBOARD

### Panel 1 — Riesgo General
- **Score general**: 0-100 (numérico + semáforo)
- **Nivel**: Bajo / Medio / Alto / Crítico
- **Tendencia**: ↑ estable ↓ (comparativa vs período anterior)
- **Risk Wheel**: gráfico radial de 7 ejes (SVG)
- **Barra de riesgo general**: visualización horizontal

### Panel 2 — Riesgo Financiero
- Score BCRA (0-100)
- Clasificación deudor (1-6)
- Cheques rechazados (cantidad + monto)
- Sanciones cambiarias
- Tendencia financiera

### Panel 3 — Riesgo Legal
- Causas activas (cantidad + gravedad)
- Embargos / inhibiciones
- Sumarios administrativos
- Condenas
- Tendencia legal

### Panel 4 — Riesgo Tributario
- Estado ARCA
- Deudas fiscales
- Embargos fiscales
- IIBB / Convenio Multilateral
- Tendencia tributaria

### Panel 5 — Riesgo Reputacional
- Noticias negativas (cantidad + gravedad)
- Controversias públicas
- Riesgo redes sociales
- Antigüedad positiva
- Tendencia reputacional

### Panel 6 — Riesgo AML
- Coincidencias OFAC/ONU/UE
- Posibles coincidencias
- PEP detection
- Jurisdicciones de riesgo
- Tendencia AML

### Panel 7 — Riesgo Compliance
- PEP / vínculos
- Contrataciones con el Estado
- Inhabilitaciones
- Causas de corrupción
- Tendencia compliance

### Panel 8 — Riesgo Operativo
- Concentración cliente/proveedor
- Concentración geográfica
- Antigüedad
- Empleados
- Cambios de autoridades
- Tendencia operativo

## VISUALIZACIONES POR PANEL

Cada panel de riesgo debe incluir:
1. **Score numérico** (0-100) con semáforo
2. **Barra de progreso** horizontal con el nivel coloreado
3. **Indicadores secundarios** (métricas específicas del factor)
4. **Enlace "Ver Fuente"** que apunta a fuentes.html#factor
5. **Tooltip** con desglose del score

## COMPORTAMIENTO

- Dashboard responsive: 4 columnas en desktop, 2 en tablet, 1 en mobile
- Los paneles se ordenan por criticidad (mayor riesgo primero)
- Colores según brand.md
- Los scores deben actualizarse si cambian los datos de entrada
- Cada panel expandible para ver detalle

## FORMATO DE SALIDA

```json
{
  "dashboard_html": "string (HTML completo del dashboard)",
  "paneles": {
    "general": {
      "score": 0-100,
      "nivel": "bajo|medio|alto|critico",
      "tendencia": "up|stable|down",
      "color": "#hex",
      "detalle_html": "string"
    },
    "financiero": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "legal": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "tributario": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "reputacional": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "aml": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "compliance": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... },
    "operativo": { "score": ..., "nivel": ..., "tendencia": ..., "color": ..., "detalle_html": ... }
  },
  "risk_wheel_svg": "string (SVG inline)",
  "ultima_actualizacion": "YYYY-MM-DD HH:mm"
}
```

## REGLAS

- Todos los datos deben basarse en hallazgos reales.
- Scores sin datos: mostrar "Sin datos" con semáforo gris.
- Dashboard generado como HTML completo para incrustar en due_diligence.html.
- Incluir CSS inline según brand.md.
- Cada panel debe ser una card independiente con sombra.
- El risk wheel debe generarse como SVG inline para escalabilidad.
