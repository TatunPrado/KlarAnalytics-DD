---
name: infographic-generator
description: >
  Generar infografías y gráficos profesionales para informes de Due Diligence.
  Produce gráficos de barras, líneas, distribución, evolución, comparativos y
  de riesgo en formato SVG inline apto para HTML.
---

# Infographic Generator

Generar gráficos e infografías en SVG inline para informes ejecutivos de Due Diligence.

## TIPOS DE GRÁFICO

### 1. Bar Chart (Gráfico de Barras)
```svg
<!-- Barras verticales u horizontales -->
<!-- Colores de brand.md -->
<!-- Labels, valores, tooltips -->
<!-- Ejes con formato -->
```

Aplicaciones:
- Comparación de scores por factor
- Evolución anual de ingresos
- Distribución de contrataciones por organismo
- Cantidad de hallazgos por categoría

### 2. Line Chart (Gráfico de Líneas)
```svg
<!-- Línea continua con puntos -->
<!-- Área sombreada bajo la línea -->
<!-- Grid sutil -->
<!-- Múltiples series comparativas -->
```

Aplicaciones:
- Evolución de score de riesgo en el tiempo
- Tendencia de indicadores financieros
- Historial de contrataciones
- Evolución de patrimonio neto

### 3. Distribution Chart (Gráfico de Distribución)
```svg
<!-- Donut / Pie chart con SVG -->
<!-- Segmentos con colores de brand.md -->
<!-- Porcentaje en cada segmento -->
<!-- Label con nombre + valor -->
```

Aplicaciones:
- Distribución del riesgo (peso de cada factor)
- Origen de hallazgos por fuente
- Tipos de contrataciones
- Distribución de empleados por área

### 4. Evolution Chart (Gráfico de Evolución)
Línea temporal con eventos clave:
```svg
<!-- Línea horizontal -->
<!-- Hitos con marcadores -->
<!-- Fechas en cada hito -->
<!-- Color coding por tipo de evento -->
```

Aplicaciones:
- Línea de tiempo de la empresa
- Eventos legales relevantes
- Cambios de autoridades
- Hitos de contrataciones

### 5. Comparative Chart (Gráfico Comparativo)
```svg
<!-- Barras agrupadas -->
<!-- Distintos colores por serie -->
<!-- Leyenda clara -->
<!-- Valores en barras -->
```

Aplicaciones:
- Comparativa scores vs benchmarks
- Período actual vs anterior
- Comparación con pares del sector

### 6. Risk Chart (Gráfico de Riesgos)
```svg
<!-- Risk wheel/radar (7 ejes) -->
<!-- Polígono coloreado según nivel -->
<!-- Ejes con labels -->
<!-- Grid radial -->
```

Aplicaciones:
- Risk wheel del sujeto
- Comparativa de perfiles de riesgo
- Benchmark vs industria

## ESPECIFICACIONES TÉCNICAS

```javascript
{
  "svg_config": {
    "width": 800,
    "height": 400,
    "padding": { "top": 40, "right": 30, "bottom": 50, "left": 60 },
    "colors": ["#0066CC", "#00A3A3", "#6C5CE7", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6"],
    "font_family": "'Inter', sans-serif",
    "font_size": {
      "title": 16,
      "axis_label": 12,
      "tick": 11,
      "value": 13,
      "legend": 11
    },
    "grid": true,
    "animation": true,
    "responsive": true
  }
}
```

## GENERACIÓN

Cada método genera SVG inline listo para incrustar en HTML:

```json
{
  "bar_chart": "<svg>...</svg>",
  "line_chart": "<svg>...</svg>",
  "distribution_chart": "<svg>...</svg>",
  "evolution_chart": "<svg>...</svg>",
  "comparative_chart": "<svg>...</svg>",
  "risk_chart": "<svg>...</svg>"
}
```

## REGLAS DE DISEÑO

- Todos los gráficos deben ser SVG inline (sin external dependencies)
- Colores según brand.md (paleta de 10 colores)
- Tipografía: sistema font stack de brand.md
- Animaciones CSS opcionales para transiciones
- Responsive: viewBox escalable
- Tooltips en hover para valores
- Leyenda clara en cada gráfico
- Ejes con formato intuitivo (miles, %, fechas)
- Grid sutil para facilitar lectura
- Sin efectos 3D, diseño plano moderno
- Enlace "Ver Fuente" en la parte inferior de cada gráfico

## REGLAS

- Los datos deben ser reales, no simulados.
- Si no hay datos suficientes: mostrar mensaje "Datos insuficientes para generar gráfico".
- Los gráficos deben ser autoexplicativos.
- Incluir título descriptivo en cada gráfico.
- Preparado para impresión (print-friendly).
