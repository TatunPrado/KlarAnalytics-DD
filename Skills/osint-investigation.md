---
name: osint-investigation
description: >
  Investigación OSINT de fuentes abiertas. Busca noticias, menciones en medios,
  litigios, antecedentes públicos, fraudes, corrupción, reputación, redes sociales
  y contenido público sobre personas físicas o jurídicas.
---

# OSINT Investigation

Investigar fuentes abiertas para detectar riesgos reputacionales, legales y de integridad.

## FUENTES

- Google News, Bing News
- Medios nacionales y provinciales
- Diarios oficiales (Boletín Oficial, boletines provinciales)
- Redes sociales (contenido público)
- LinkedIn, Twitter/X, Facebook (perfiles públicos)
- Instagram, TikTok (contenido público)
- Wikipedia
- YouTube (canales públicos)
- Foros públicos, blogs
- Registros públicos de causas judiciales
- CSJN (Corte Suprema), Poder Judicial de cada provincia

## TAREAS

1. Buscar noticias y menciones en medios sobre el sujeto
2. Buscar litigios, causas judiciales, procesamientos
3. Buscar fraudes, corrupción, delitos económicos
4. Buscar antecedentes reputacionales
5. Analizar redes sociales (contenido público)
6. Buscar participaciones en empresas, directorios
7. Identificar vínculos con PEP
8. Identificar riesgos de discriminación, discurso de odio

## SALIDA

```json
{
  "hallazgos": [
    {
      "tipo": "noticia_positiva|noticia_negativa|litigio|causa_judicial|mencion|pep|otro",
      "descripcion": "string",
      "fuente": "string",
      "url": "string",
      "fecha": "YYYY-MM-DD",
      "confianza": "alta|media|baja",
      "evidencia": "string"
    }
  ],
  "riesgos_potenciales": ["string"],
  "resumen": "string"
}
```

## REGLAS

- No inventar información.
- No inferir conductas sin evidencia.
- Citar URL exacta de cada hallazgo.
- No realizar perfiles ideológicos ni clasificaciones políticas.
- Limitarse a hechos públicos verificables.
- Diferenciar: hecho comprobado / indicio / riesgo potencial.
