---
name: bcra-analysis
description: >
  Analizar situación financiera ante el BCRA. Verifica Central de Deudores,
  cheques rechazados, clasificación crediticia, deuda consolidada y situación
  cambiaria de personas físicas o jurídicas.
---

# BCRA Analysis

Analizar situación financiera y crediticia ante el Banco Central de la República Argentina.

## FUENTES

| Fuente | URL | Tipo |
|--------|-----|------|
| BCRA Central de Deudores | https://www.bcra.gob.ar/BCRAyVos/Deudores.asp | Deuda consolidada |
| BCRA Cheques Rechazados | https://www.bcra.gob.ar/BCRAyVos/Cheques_rechazados.asp | Historial cheques |
| BCRA SIRAD | https://www.bcra.gob.ar/BCRAyVos/SIRAD.asp | Situación crediticia |
| BCRA Sanciones Cambiarias | https://www.bcra.gob.ar/ | Sanciones |
| BCRA Estadísticas | https://www.bcra.gob.ar/PublicacionesEstadisticas/ | Datos macro |

## VERIFICACIONES

### Central de Deudores
- Deuda total consolidada
- Clasificación del deudor (1 a 6)
- Entidades financieras informantes
- Situación: normal, con problemas, irregular
- Historial de los últimos 24 meses

### Cheques Rechazados
- Cantidad de cheques rechazados
- Motivos: falta de fondos, defectos formales, cuenta cerrada
- Montos involucrados
- Período analizado
- Reincidencia

### Situación Crediticia
- Límites de crédito
- Utilización
- Scoring crediticio (cuando disponible)
- Productos financieros contratados

### Sanciones Cambiarias
- Multas por infracciones cambiarias
- Legajo de sanciones
- Fecha de sanción

## SALIDA

```json
{
  "central_deudores": {
    "deuda_total": "ARS X",
    "clasificacion": "1|2|3|4|5|6",
    "situacion": "normal|con_problemas|irregular",
    "entidades": ["string"],
    "fecha_consulta": "YYYY-MM-DD",
    "observaciones": "string"
  },
  "cheques_rechazados": {
    "cantidad": 0,
    "motivos": ["string"],
    "monto_total": "ARS X",
    "reincidencia": true|false,
    "fecha_consulta": "YYYY-MM-DD"
  },
  "sanciones_cambiarias": {
    "tiene_sanciones": true|false,
    "detalle": "string",
    "monto": "ARS X",
    "fecha": "YYYY-MM-DD"
  },
  "riesgo_financiero": "bajo|medio|alto|critico",
  "score_financiero": 0-100
}
```

## ESCALA DE RIESGO FINANCIERO

| Situación BCRA | Nivel | Score |
|---------------|-------|-------|
| Todo normal, sin deuda, sin cheques rechazados | Bajo | 0-25 |
| Deuda normal, clasificación 1-2, pocos cheques | Bajo-Medio | 26-40 |
| Clasificación 3, cheques reiterados, deuda moderada | Medio | 41-55 |
| Clasificación 4-5, cheques frecuentes, deuda alta | Alto | 56-75 |
| Clasificación 6, cheques condenados, sanciones | Crítico | 76-100 |

## REGLAS

- Si no hay acceso a datos: "NO SE PUDO VERIFICAR".
- La consulta a Central de Deudores requiere Clave Fiscal del sujeto.
- Indicar siempre: fuente, fecha, URL consultada.
- No acceder a información protegida sin autorización.
