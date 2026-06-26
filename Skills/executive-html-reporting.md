---
name: executive-html-reporting
description: >
  Coordinar la generación completa del informe ejecutivo HTML. Orquesta todas las
  skills de investigación, scoring, visualización y generación de reportes para
  producir los 3 entregables finales con diseño corporativo premium.
---

# Executive HTML Reporting

Skill orquestadora que coordina todo el pipeline de generación de informes ejecutivos.

## PIPELINE DE GENERACIÓN

```
FASE 1 ─► Investigación (skills de investigación)
                │
                ▼
FASE 2 ─► Análisis y Scoring (risk-scoring)
                │
                ▼
FASE 3 ─► Visualización (executive-visualization, risk-dashboard, infographic-generator)
                │
                ▼
FASE 4 ─► Generación de Informes (html-report-builder)
                │
                ▼
FASE 5 ─► Post-procesamiento (branding, referencias cruzadas, verificación)
                │
                ▼
           📁 due_diligence.html
           📁 anexos.html
           📁 fuentes.html
```

## FASES DETALLADAS

### Fase 1 — Investigación (paralela máxima)
Ejecutar concurrentemente:
- `osint_investigation` → datos reputacionales, noticias, litigios
- `aml_sanctions` → listas restrictivas OFAC, ONU, UE, UK, UIF
- `bcra_analysis` → BCRA, Central de Deudores
- `boletin_oficial` → publicaciones en boletines
- `procurement_analysis` → contrataciones con el Estado
- `trademark_domain` → marcas INPI + dominios

**Validación**: Cada skill debe devolver su resultado con fuente, URL, fecha y confianza.

### Fase 2 — Análisis y Scoring
- `risk_scoring` consumir los hallazgos de Fase 1
- Calcular scores para cada factor (0-100)
- Generar matriz impacto vs probabilidad
- Generar risk wheel (7 ejes)
- Asignar nivel general (Bajo/Medio/Alto/Crítico)
- Determinar recomendación

### Fase 3 — Visualización
- `executive_visualization` → KPI cards, score cards, semáforos, heatmap, timeline
- `risk_dashboard` → dashboard completo con paneles
- `infographic_generator` → gráficos SVG (barras, líneas, donut, radar)

### Fase 4 — Generación de Informes HTML
- `html_report_builder` con todos los datos anteriores
- Construir due_diligence.html
- Construir anexos.html (evidencia ampliada)
- Construir fuentes.html (tabla auditable)

### Fase 5 — Post-procesamiento
- Aplicar brand.md completo
- Insertar referencias cruzadas entre informes
- Verificar que cada KPI, score y conclusión tenga su enlace "Ver Fuente"
- Validar que no haya datos sin fuente
- Optimizar HTML (minificar CSS, comprimir SVG)
- Verificar impresión (print media query)

## VALIDACIONES DE CALIDAD

### Checklist de calidad
- [ ] Todos los hallazgos tienen fuente + URL + fecha + confianza
- [ ] Los scores están calculados con datos reales
- [ ] Cada KPI tiene enlace "Ver Fuente"
- [ ] La matriz impacto/probabilidad está poblada
- [ ] El risk wheel tiene los 7 ejes
- [ ] Las fuentes en fuentes.html están completas
- [ ] brand.md está aplicado correctamente
- [ ] El HTML es responsive
- [ ] El HTML es print-friendly
- [ ] No hay marcadores de posición ni datos falsos
- [ ] La navegación funciona correctamente
- [ ] Los enlaces entre archivos son válidos

## CONFIGURACIÓN DEL INFORME

```json
{
  "config": {
    "idioma": "es",
    "moneda": "ARS",
    "numeros_locale": "es-AR",
    "zona_horaria": "America/Argentina/Buenos_Aires"
  },
  "sujeto": {
    "tipo": "fisica|juridica",
    "nombre": "string",
    "cuit": "string",
    "domicilio": "string",
    "provincia": "string"
  },
  "cliente": {
    "nombre": "string",
    "area": "string"
  },
  "fecha_informe": "YYYY-MM-DD HH:mm"
}
```

## REGLAS DE CALIDAD

1. **Veracidad**: Todos los datos deben ser reales y verificables.
2. **Completitud**: No dejar secciones vacías. Si no hay datos: "Sin información disponible".
3. **Trazabilidad**: Cada afirmación debe poder seguirse hasta su fuente.
4. **Consistencia visual**: Todos los elementos deben seguir brand.md.
5. **Profesionalismo**: El resultado debe tener apariencia de consultora Big Four / auditoría.
6. **Auditabilidad**: El informe debe poder ser auditado por un tercero.
7. **No IA**: El informe no debe parecer generado por IA, sino por un equipo profesional.

## FORMATO DE SALIDA

```
📁 due-diligence-[sujeto]/
  ├── due_diligence.html      → Informe completo (portada + 15 secciones)
  ├── anexos.html             → Evidencia ampliada por hallazgo
  └── fuentes.html            → Tabla completa de fuentes auditables
```

Los 3 archivos deben estar interconectados mediante enlaces HTML.
