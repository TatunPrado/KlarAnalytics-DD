---
name: bcra-playwright-scraper
description: >
  Función Playwright para scrapear datos financieros del BCRA. Consulta
  Cheques Rechazados y Central de Deudores usando el CUIT del sujeto.
  Devuelve JSON estructurado con hallazgos financieros.
---

# BCRA Playwright Scraper

Herramienta de scraping automatizado con Playwright para obtener situación financiera real del BCRA.

## PROPÓSITO

Ejecutar una consulta automatizada a las bases de datos públicas del BCRA usando el CUIT del sujeto investigado, para obtener:

- Cheques rechazados (cantidad, montos, motivos, reincidencia)
- Central de Deudores (deuda consolidada, clasificación crediticia)
- Sanciones cambiarias

## UBICACIÓN

`tools/bcra_scraper.py`

## REQUISITOS

```bash
pip install playwright
playwright install chromium
```

## MODO DE USO

```bash
# Consulta básica (headless)
python tools/bcra_scraper.py 30-12345678-9

# Guardar resultado en archivo
python tools/bcra_scraper.py 30-12345678-9 --output resultado.json

# Modo visible (para debugging)
python tools/bcra_scraper.py 30-12345678-9 --visible
```

## PARÁMETROS

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `cuit` | string (req) | CUIT con o sin formato |
| `--output` / `-o` | string | Ruta archivo JSON de salida |
| `--visible` | flag | Modo ventana visible (default: headless) |

## SALIDA (JSON)

```json
{
  "cuit": "30123456789",
  "fecha": "2026-06-21",
  "cheques_rechazados": {
    "fuente": "BCRA Cheques Rechazados",
    "url": "https://www.bcra.gob.ar/BCRAyVos/Cheques_rechazados.asp",
    "cuit_consultado": "30123456789",
    "cheques": [
      {"fecha": "2026-01-15", "motivo": "FALTA DE FONDOS", "monto": "$ 150.000", "estado": "RECHAZADO"}
    ],
    "cantidad_total": 1,
    "monto_total": 150000.0,
    "hay_rechazos": true,
    "error": null,
    "fecha_consulta": "2026-06-21"
  },
  "central_deudores": {
    "fuente": "BCRA Central de Deudores",
    "url": "https://www.bcra.gob.ar/BCRAyVos/Deudores.asp",
    "cuit_consultado": "30123456789",
    "requiere_autenticacion": true,
    "datos": null,
    "error": "REQUIERE_CLAVE_FISCAL: ...",
    "fecha_consulta": "2026-06-21"
  }
}
```

## INTERPRETACIÓN

### Cheques Rechazados
- Sin rechazos (`hay_rechazos: false`): situación financiera normal.
- Con rechazos: evaluar cantidad, montos, reincidencia y antigüedad.
- Rechazos reiterados o montos altos → riesgo financiero alto.

### Central de Deudores
- Generalmente requiere Clave Fiscal del sujeto (autenticación AFIP).
- Si hay datos: clasificación 1-2 es normal, 3-4 es alerta, 5-6 es crítico.

## ERRORES COMUNES

| Error | Significado |
|-------|-------------|
| `REQUIERE_CLAVE_FISCAL` | El sitio pide autenticación. No se pudo acceder. |
| `Timeout` | El sitio no respondió. Reintentar más tarde. |
| `Playwright no instalado` | Falta instalar dependencias. |

## REGLAS

- Solo consultar CUITs válidos (11 dígitos).
- No almacenar datos sensibles sin autorización.
- Indicar siempre la fuente de cada hallazgo.
- Si el sitio cambia su estructura, actualizar los selectores.
