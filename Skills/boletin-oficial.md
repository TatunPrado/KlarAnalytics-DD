---
name: boletin-oficial
description: >
  Buscar publicaciones en el Boletín Oficial de la República Argentina y boletines
  provinciales. Localiza constituciones, reformas, autoridades, convocatorias,
  fusiones, disoluciones, sanciones y contrataciones.
---

# Boletín Oficial

Buscar y analizar publicaciones en boletines oficiales nacionales y provinciales.

## FUENTES

| Boletín | URL | Cobertura |
|---------|-----|-----------|
| Boletín Oficial República Argentina | https://www.boletinoficial.gob.ar/ | Nacional |
| Boletín Oficial CABA | https://boletinoficial.buenosaires.gob.ar/ | CABA |
| Boletín Oficial Córdoba | https://boletinoficial.cba.gov.ar/ | Córdoba |
| Boletín Oficial Santa Fe | https://www.santafe.gov.ar/boletinoficial/ | Santa Fe |
| Boletín Oficial Buenos Aires | https://www.boletinoficial.gba.gob.ar/ | Pcia. Bs. As. |
| Otros provinciales | Según corresponda | Varía |

## TIPOS DE PUBLICACIONES

### Personas Jurídicas
- Contrato social / estatuto
- Reformas de estatuto
- Cambios de autoridades (Consejo, Comisión Directiva)
- Cambio de sede social
- Fusión, escisión, transformación
- Disolución y liquidación
- Convocatorias a asambleas
- Balances y memorias (cuando se publican)
- Aumentos de capital
- Designación de síndicos
- Intervenciones judiciales

### Personas Físicas
- Edictos sucesorios
- Convocatorias judiciales
- Declaraciones de quiebra
- Inhabilitaciones

### Contrataciones y Licitaciones
- Llamados a licitación pública/privada
- Adjudicaciones
- Contratos y concesiones
- Resoluciones de adjudicación
- Impugnaciones

### Sanciones
- Sanciones administrativas
- Inhabilitaciones para contratar
- Sumarios administrativos
- Multas

## SALIDA

```json
{
  "publicaciones": [
    {
      "tipo": "constitucion|reforma|autoridad|convocatoria|fucion|disolucion|sancion|licitacion|otro",
      "boletin": "Nacional|Córdoba|...",
      "fecha_publicacion": "YYYY-MM-DD",
      "titulo": "string",
      "detalle": "string",
      "url": "string",
      "confianza": "alta|media|baja",
      "relevancia": "critica|alta|media|baja"
    }
  ],
  "cantidad_total": 0,
  "tiene_antecedentes_relevantes": true|false,
  "resumen": "string"
}
```

## REGLAS

- Siempre priorizar boletines oficiales originales.
- Proporcionar URL exacta de cada publicación.
- Indicar fecha exacta de publicación y fecha de consulta.
- No inferir consecuencias jurídicas sin asesoramiento legal.
- Diferenciar entre publicaciones obligatorias (edictos) y voluntarias.
