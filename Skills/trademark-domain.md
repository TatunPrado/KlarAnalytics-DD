---
name: trademark-domain
description: >
  Investigar marcas registradas ante el INPI y dominios de internet (NIC.ar, WHOIS).
  Identifica titularidad, solicitudes, registros vigentes, vencimientos y
  relaciones entre marcas, dominios y el sujeto investigado.
---

# Trademark & Domain Investigation

Investigar propiedad intelectual (marcas INPI) y registros de dominios de internet.

## FUENTES

| Fuente | URL | Tipo |
|--------|-----|------|
| INPI Marcas | https://portaltramites.inpi.gob.ar/ | Marcas Argentina |
| INPI Patentes | https://portaltramites.inpi.gob.ar/ | Patentes Argentina |
| INPI Modelos de Utilidad | https://portaltramites.inpi.gob.ar/ | Modelos utilidad |
| NIC.ar | https://nic.ar/ | Dominios .ar |
| WHOIS Internacional | https://www.whois.com/ | Dominios globales |
| DomainTools | https://domaintools.com/ | Historial dominios |
| WIPO | https://www.wipo.int/ | Marcas internacionales |
| EUIPO | https://euipo.europa.eu/ | Marcas UE |
| USPTO | https://www.uspto.gov/ | Marcas EE.UU. |
| LATIPAT | https://latipat.es/ | Patentes Latinoamérica |

## VERIFICACIONES

### Marcas (INPI)
- Marcas registradas a nombre del sujeto
- Solicitudes en trámite
- Clases INPI (Niza) registradas
- Fecha de registro y vencimiento
- Titular actual
- Cesiones o licencias registradas
- Oposiciones presentadas contra terceros
- Oposiciones de terceros contra el sujeto
- Marcas caducas o abandonadas

### Patentes
- Patentes registradas
- Solicitudes en trámite
- Titulares e inventores
- Estado: concedida, en examen, abandonada

### Dominios de Internet
- Dominios .ar registrados (NIC.ar)
- Dominios .com, .net, .org, etc. (WHOIS)
- Titular del dominio (registrant)
- Fecha de registro y vencimiento
- Servidores DNS
- Historial de titularidad (cambios de propietario)
- Dominios vinculados a la misma persona/empresa

## SALIDA

```json
{
  "marcas": [
    {
      "marca": "string",
      "clase_inpi": "string",
      "titular": "string",
      "fecha_registro": "YYYY-MM-DD",
      "vencimiento": "YYYY-MM-DD",
      "estado": "registrada|en_tramite|caduca|oposicion",
      "url_consulta": "string"
    }
  ],
  "patentes": [...],
  "dominios": [
    {
      "dominio": "string",
      "tld": ".ar|.com|...",
      "titular": "string",
      "fecha_registro": "YYYY-MM-DD",
      "vencimiento": "YYYY-MM-DD",
      "dns": ["string"],
      "url_consulta": "string"
    }
  ],
  "vinculos_detectados": ["string"],
  "riesgo_pi": "bajo|medio|alto|critico",
  "observaciones": "string"
}
```

## REGLAS

- Verificar tanto a nombre del sujeto como de vinculadas.
- No inferir falsificación sin evidencia.
- Documentar URL exacta de cada consulta.
- Para NIC.ar: usar búsqueda pública disponible.
- No acceder a información privada de titulares sin autorización.
