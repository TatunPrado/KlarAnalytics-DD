---
name: executive-visualization
description: >
  Generar visualizaciones ejecutivas profesionales: KPI Cards, Score Cards,
  semáforos, heatmaps, timelines, dashboards y resúmenes visuales. Diseño
  corporativo premium para informes de Due Diligence.
---

# Executive Visualization System

Generar componentes visuales profesionales para informes ejecutivos de Due Diligence.

## COMPONENTES

### 1. KPI Cards
```html
<div class="kpi-card">
  <div class="kpi-icon" style="background: {color}15;">
    <svg>...</svg>
  </div>
  <div class="kpi-content">
    <span class="kpi-value">{valor}</span>
    <span class="kpi-label">{label}</span>
    <span class="kpi-trend {trend_class}">{trend_text}</span>
  </div>
</div>
```

Características:
- Icono circular con color de fondo semitransparente
- Valor principal grande (2rem, bold)
- Label en uppercase con tracking
- Indicador de tendencia (↑ estable ↓) con color
- Sombra sutil, hover elevación

### 2. Executive Score Cards
```html
<div class="score-card {risk_level}">
  <div class="score-value">{score}/100</div>
  <div class="score-level">{nivel}</div>
  <div class="score-bar">
    <div class="score-bar-fill" style="width: {score}%; background: {color};"></div>
  </div>
  <div class="score-label">{factor}</div>
</div>
```

Estilos:
- Bajo: borde verde + badge verde
- Medio: borde amarillo + badge amarillo
- Alto: borde rojo + badge rojo
- Crítico: borde rojo oscuro + badge rojo oscuro

### 3. Risk Semaphores
```html
<div class="semaphore {level}">
  <span class="semaphore-dot" style="background: {color};"></span>
  <span class="semaphore-label">{level}</span>
  <span class="semaphore-score">({score}/100)</span>
</div>
```

### 4. Heatmap Grid
Matriz de 7x5 donde cada celda representa un factor vs indicador:
- Celda verde = bajo riesgo
- Celda amarilla = medio
- Celda roja = alto
- Celda rojo oscuro = crítico

### 5. Timeline
```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-marker" style="border-color: {color};"></div>
    <div class="timeline-date">{fecha}</div>
    <div class="timeline-content">{evento}</div>
    <a class="source-link" href="{url}" target="_blank">Ver Fuente</a>
  </div>
  ...
</div>
```

### 6. Risk Matrix (Impact vs Probability)
```html
<div class="risk-matrix">
  <div class="matrix-row">
    <div class="matrix-cell critical">Crítico</div>
    ...
  </div>
  ...
  <div class="matrix-coords">
    <span>Probabilidad ↓</span>
    <span>Impacto →</span>
  </div>
</div>
```

### 7. Executive Dashboard
Layout de 3 columnas:
- Col 1: Risk Wheel (SVG) + Score General
- Col 2: 7 Score Cards (2-rows + 1)
- Col 3: Risk Matrix + Heatmap

### 8. Comparative Indicators
```html
<div class="comparison-group">
  <div class="comparison-item">
    <span class="comparison-label">Factor</span>
    <div class="comparison-bar">
      <div class="comp-bar-fill" style="width: {score}%; background: {color};">
        <span>{score}</span>
      </div>
    </div>
  </div>
  ...
</div>
```

## SALIDA

La skill debe generar HTML con los componentes listos para incrustar en el reporte:

```json
{
  "kpi_cards": ["<html>..."],
  "score_cards": ["<html>..."],
  "semaphores": {"financiero": "...", ...},
  "heatmap": "<html>...",
  "timeline": "<html>...",
  "risk_matrix": "<html>...",
  "dashboard": "<html>...",
  "comparative_indicators": "<html>..."
}
```

## REGLAS DE DISEÑO

- Aplicar brand.md: colores, tipografías, espaciado
- Todos los componentes deben tener enlace "Ver Fuente"
- Diseño responsive (flex/grid)
- Preparado para impresión (media queries)
- Sin dependencias externas (todo inline CSS)
- Arquitectura de componentes anidables
- Los KPI deben representar datos reales, no decoración
