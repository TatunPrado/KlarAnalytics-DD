---
name: procurement-analysis
description: >
  Analizar contrataciones con el Estado. Busca en COMPR.AR, sistemas provinciales
  y registros de proveedores del Estado para identificar contratos, montos,
  organismos contratantes y posibles riesgos de integridad.
---

# Procurement Analysis

Analizar contrataciones públicas, licitaciones y adjudicaciones del sujeto con el Estado.

## FUENTES

| Fuente | URL | Cobertura |
|--------|-----|-----------|
| COMPR.AR | https://comprar.gob.ar/ | Nacional |
| Buenos Aires Compras | https://www.bacompras.gba.gob.ar/ | Pcia. Bs. As. |
| Córdoba Compras | https://comprascordoba.gob.ar/ | Córdoba |
| Santa Fe Compras | https://compras.santafe.gov.ar/ | Santa Fe |
| CABA Compras | https://www.buenosairescompras.gob.ar/ | CABA |
| ONC (Oficina Nacional de Contrataciones) | https://www.argentina.gob.ar/onc | Nacional |
| SINTyS | https://www.sintys.gob.ar/ | Empleo público |
| Inhabilitados Nación | https://www.argentina.gob.ar/onc/inhabilitados | Proveedores |
| SIGEN | https://www.sigen.gob.ar/ | Control interno |

## VERIFICACIONES

### Contratos Vigentes
- Organismo contratante
- Objeto del contrato
- Monto adjudicado
- Fecha de inicio y fin
- Modalidad (licitación pública, privada, contratación directa, etc.)
- Estado (vigente, finalizado, rescindido)

### Historial de Contrataciones
- Total contratado por año
- Organismos recurrentes
- Tipos de contratación
- Montos máximos y mínimos

### Inhabilitaciones
- Registro de proveedores inhabilitados
- Causas de inhabilitación
- Período de inhabilitación
- Organismo que sancionó

### Indicadores de Riesgo
- Contrataciones directas sin licitación
- Montos inusualmente altos
- Contratos con organismos vinculados a PEP
- Cambios frecuentes de objeto contractual
- Rescisiones anticipadas
- Sobreturnos o urgencias declaradas

## SALIDA

```json
{
  "contratos_vigentes": [
    {
      "organismo": "string",
      "objeto": "string",
      "monto": "ARS X",
      "fecha_inicio": "YYYY-MM-DD",
      "fecha_fin": "YYYY-MM-DD",
      "modalidad": "licitacion_publica|privada|directa|otro",
      "estado": "vigente|finalizado|rescindido"
    }
  ],
  "historial_anual": {"2023": 0, "2024": 0, "2025": 0},
  "esta_inhabilitado": true|false,
  "detalle_inhabilitacion": "string",
  "indicadores_riesgo": ["string"],
  "riesgo_contrataciones": "bajo|medio|alto|critico",
  "score_contrataciones": 0-100,
  "total_contratado_historico": "ARS X",
  "fuentes": ["string"]
}
```

## INDICADORES DE ALERTA

- Contrataciones directas sin concurrencia
- Montos cercanos a topes permitidos
- Contrataciones en zonas grises regulatorias
- Vínculos entre funcionarios contratantes y el proveedor
- Cambios societarios posteriores a la adjudicación
- Subcontrataciones a vinculadas
- Facturación al Estado > 50% de ingresos totales

## REGLAS

- No acceder a información protegida.
- Verificar también registros de inhabilitados.
- Documentar URL exacta de cada consulta.
- No inferir corrupción sin evidencia.
- Identificar patrones sospechosos como riesgos, no como hechos.
