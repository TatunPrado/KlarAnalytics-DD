---
name: html-report-builder
description: >
  Motor de generación de informes HTML profesionales. Construye due_diligence.html,
  anexos.html y fuentes.html aplicando brand.md, integrando componentes de
  visualización ejecutiva, gráficos infográficos y dashboards de riesgo.
---

# HTML Report Builder

Motor que construye los 3 informes HTML finales a partir de los hallazgos, scores y componentes visuales.

## ARQUITECTURA

```
Hallazgos (JSON)
     │
     ▼
risk-scoring ──► scores.json
     │
     ▼
executive-visualization ──► componentes HTML
     │
     ▼
risk-dashboard ──► dashboard HTML
     │
     ▼
infographic-generator ──► gráficos SVG
     │
     ▼
html-report-builder ──► due_diligence.html
                    ├── anexos.html
                    └── fuentes.html
```

## ARCHIVOS GENERADOS

### due_diligence.html — Informe Completo

Estructura del documento:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="classification" content="CONFIDENCIAL">
  <title>Due Diligence - [Sujeto]</title>
  <style>
    /* brand.md CSS completo inline */
    /* styles.css inline compilado */
  </style>
</head>
<body>
  <!-- COVER PAGE -->
  <section id="cover">
    <div class="cover-overlay"></div>
    <div class="cover-content">
      <div class="cover-badge">CONFIDENCIAL</div>
      <h1 class="cover-title">Informe de Due Diligence</h1>
      <h2 class="cover-subtitle">[Nombre del Sujeto]</h2>
      <div class="cover-meta">
        <p><strong>CUIT:</strong> [cuit]</p>
        <p><strong>Fecha:</strong> [fecha]</p>
        <p><strong>Preparado para:</strong> [cliente]</p>
        <p><strong>Clasificación:</strong> USO CONFIDENCIAL</p>
      </div>
    </div>
  </section>

  <!-- TABLE OF CONTENTS -->
  <nav id="toc" class="side-nav">
    <!-- Generado automáticamente -->
  </nav>

  <!-- EXECUTIVE SUMMARY -->
  <section id="resumen-ejecutivo">
    <!-- KPI Cards + score general + recomendación -->
  </section>

  <!-- DASHBOARD -->
  <section id="dashboard">
    <!-- Risk Wheel + Score Cards + Risk Matrix -->
  </section>

  <!-- FINDINGS by category -->
  <section id="hallazgos-criticos">
    <!-- Tabla de hallazgos críticos priorizados -->
  </section>

  <section id="hallazgos-relevantes">
    <!-- Hallazgos por categoría con enlaces a fuentes -->
  </section>

  <!-- RISK MATRIX -->
  <section id="matriz-riesgos">
    <!-- Impacto vs Probabilidad + Risk Wheel -->
  </section>

  <!-- TIMELINE -->
  <section id="linea-tiempo">
    <!-- Timeline de eventos -->
  </section>

  <!-- EVALUATIONS -->
  <section id="evaluacion-financiera">...</section>
  <section id="evaluacion-tributaria">...</section>
  <section id="evaluacion-reputacional">...</section>
  <section id="evaluacion-legal">...</section>
  <section id="evaluacion-aml">...</section>

  <!-- CONCLUSIONS -->
  <section id="conclusiones">
    <!-- Conclusiones basadas en evidencia -->
  </section>

  <!-- RECOMMENDATIONS -->
  <section id="recomendaciones">
    <!-- Aprobar / Aprobar con mitigaciones / Rechazar -->
    <!-- Medidas de mitigación -->
  </section>

  <!-- FOOTER -->
  <footer>
    <p>© [año] Due Diligence Office — CONFIDENCIAL</p>
    <p>Este informe es confidencial y para uso exclusivo del destinatario.</p>
  </footer>

  <script>
    // Interacciones: navigation, tooltips, expand/collapse
  </script>
</body>
</html>
```

### anexos.html — Evidencia Ampliada

```html
<section class="evidencia">
  <h2>Hallazgo: [título]</h2>
  <div class="evidencia-meta">
    <span class="badge {risk}">{nivel}</span>
    <span>Fuente: {fuente}</span>
    <span>Fecha: {fecha}</span>
    <a href="{url}" target="_blank">Ver Original</a>
  </div>
  <div class="evidencia-contenido">
    <p>{descripción ampliada}</p>
    <!-- Capturas, tablas, citas textuales -->
  </div>
  <div class="evidencia-contexto">
    <h4>Contexto adicional</h4>
    <p>{contexto}</p>
  </div>
  <div class="evidencia-referencias">
    <h4>Referencias cruzadas</h4>
    <ul>
      <li><a href="fuentes.html#ref-{id}">Ver en fuentes</a></li>
    </ul>
  </div>
</section>
```

### fuentes.html — Fuentes Auditables

```html
<table class="data-table">
  <thead>
    <tr>
      <th>#</th>
      <th>Fuente</th>
      <th>URL</th>
      <th>Fecha Consulta</th>
      <th>Descripción</th>
      <th>Confiabilidad</th>
      <th>Observaciones</th>
    </tr>
  </thead>
  <tbody>
    <tr id="ref-1">
      <td>1</td>
      <td>OFAC SDN List</td>
      <td><a href="...">...</a></td>
      <td>2026-06-12</td>
      <td>Consulta de sanciones</td>
      <td><span class="badge badge-high">ALTA</span></td>
      <td>Sin coincidencias</td>
    </tr>
    ...
  </tbody>
</table>
```

## INTEGRACIÓN CON brand.md

El builder debe:
1. Cargar brand.md y extraer: colores, tipografías, espaciados, componentes
2. Aplicar los tokens CSS como variables raíz
3. Usar los estilos de componente definidos (cards, badges, tables, etc.)
4. Respetar el sistema de layout (grid, columnas)
5. Aplicar las reglas de impresión

## CONFIGURACIÓN

```json
{
  "sujeto": {
    "nombre": "string",
    "tipo": "fisica|juridica",
    "cuit": "string",
    "fecha_informe": "YYYY-MM-DD",
    "cliente": "string"
  },
  "scores": { ... },
  "hallazgos": [ ... ],
  "dashboard": { ... },
  "graficos": { ... },
  "fuentes": [ ... ],
  "recomendacion": "string",
  "mitigaciones": ["string"]
}
```

## REGLAS

- El HTML debe ser autónomo (todo inline, sin dependencias externas).
- Responsive: adaptable a desktop, tablet y móvil.
- Print-friendly: @media print optimizado.
- Navegación sticky con scroll spy.
- Todos los datos deben tener enlace a fuentes.html.
- El diseño debe seguir estrictamente brand.md.
- El informe no puede contener marcadores de posición ni datos falsos.
- Cada sección debe tener un ID para navegación directa.
