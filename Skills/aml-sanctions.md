---
name: aml-sanctions
description: >
  Verificación de listas restrictivas internacionales y nacionales. Chequea personas
  físicas, jurídicas, directores, accionistas y beneficiarios finales contra listas
  OFAC, ONU, UE, UK OFSI, UIF Argentina y PEP.
---

# AML Sanctions

Verificar listas restrictivas nacionales e internacionales para cumplimiento AML/CFT.

## FUENTES OFICIALES

| Lista | URL | Tipo |
|-------|-----|------|
| OFAC SDN List | https://sanctionssearch.ofac.treas.gov/ | Sanciones EE.UU. |
| OFAC CAPTA List | https://www.treasury.gov/ofac | Sanciones Cuba |
| OFAC Non-SDN | https://www.treasury.gov/ofac | Sanciones varias |
| OFAC SSI List | https://www.treasury.gov/ofac | Sectorial sanciones |
| ONU Lista Consolidada | https://www.un.org/securitycouncil/es/content/un-sc-consolidated-list | Sanciones ONU |
| UE Lista Consolidada | https://webgate.ec.europa.eu/fsd/fsf/public/files/ | Sanciones UE |
| UK OFSI | https://www.gov.uk/government/publications/the-uk-sanctions-list | Sanciones UK |
| UIF Argentina | https://www.argentina.gob.ar/uif | Prevención LA/FT |
| BCRA Sanciones | https://www.bcra.gob.ar/ | Sanciones financieras |
| FATF / GAFI | https://www.fatf-gafi.org/ | Listas jurisdiccionales |
| World Bank Listing | https://www.worldbank.org/debarr | Sanciones Banco Mundial |

## COBERTURA

Verificar:
- Persona investigada (nombre, alias, CUIT)
- Directores y miembros del consejo
- Accionistas principales (>5%)
- Beneficiarios finales
- Apoderados y representantes legales
- Personas políticamente expuestas (PEP)
- Familiares y asociados cercanos de PEP (cuando información sea pública)
- Jurisdicciones de riesgo (FATF "grey list" / "black list")

## SALIDA

```json
{
  "coincidencias": [
    {
      "lista": "OFAC|ONU|UE|UK|UIF|BCRA|OTRO",
      "nombre_buscado": "string",
      "coincidencia": "directa|parcial|alias|fonetica",
      "nivel_confianza": "alta|media|baja",
      "detalle": "string",
      "url_consulta": "string",
      "fecha": "YYYY-MM-DD"
    }
  ],
  "posibles_coincidencias": [...],
  "sin_coincidencias": ["OFAC", "ONU", "UE", ...],
  "riesgo_aml": "bajo|medio|alto|critico",
  "score_aml": 0-100,
  "observaciones": "string"
}
```

## ESCALA DE RIESGO AML

| Coincidencias | Nivel | Acción |
|--------------|-------|--------|
| Sin coincidencias | Bajo | Continuar |
| Posible fonética parcial | Bajo | Verificar documentación |
| Coincidencia parcial nombre | Medio | Solicitar información adicional |
| Coincidencia alta (nombre + país) | Alto | Escalar a Compliance |
| Coincidencia directa (nombre + ID) | Crítico | Rechazar / Congelar |

## REGLAS

- No falsear resultados.
- Diferenciar: coincidencia directa, parcial, fonética.
- Si no hay acceso a la lista: "NO SE PUDO VERIFICAR".
- Documentar URL exacta de cada consulta.
- Verificar también en listas PEP y listas de inhabilitados para contratar.
