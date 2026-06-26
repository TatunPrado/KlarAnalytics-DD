"""Real-time data sources for Due Diligence automation.

Currently supports:
- BCRA Central de Deudores API (cheques rechazados + deudas)
- CUIT Online (datos fiscales: raz\u00f3n social, domicilio, condici\u00f3n IVA, etc.)
"""

import json
import logging
import re
import urllib.request
import urllib.error

BCRA_CHEQUES_URL = "https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/ChequesRechazados/{cuit}"
BCRA_DEUDAS_URL = "https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/{cuit}"

SITUACION_LABELS = {
    1: "Normal (1)",
    2: "Observaci\u00f3n (2)",
    3: "Problemas (3)",
    4: "Alto Riesgo (4)",
    5: "Irrecuperable (5)",
    6: "Irrecuperable por disposici\u00f3n t\u00e9cnica (6)",
}


def _fetch_json(url, timeout=15):
    req = urllib.request.Request(url, headers={
        "User-Agent": "PrismaConsulting-KlarAnalytics/1.0",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"ok": True, **json.loads(r.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 404:
            try:
                return {"ok": False, "not_found": True, **json.loads(body)}
            except json.JSONDecodeError:
                pass
        logging.warning("BCRA API HTTP %d for %s: %s", e.code, url, body[:200])
        return {"ok": False, "error": "HTTP %d" % e.code}
    except Exception as e:
        logging.warning("BCRA API error for %s: %s", url, e)
        return {"ok": False, "error": str(e)}


def consultar_bcra_cheques(cuit):
    """Consulta cheques rechazados de una CUIT en la API del BCRA."""
    url = BCRA_CHEQUES_URL.format(cuit=cuit)
    data = _fetch_json(url)
    if not data.get("ok") and data.get("not_found"):
        return {"ok": True, "identificacion": cuit, "denominacion": "Sin datos", "causales": []}
    if not data.get("ok"):
        return {"ok": False, "error": data.get("error", "No se pudo consultar la API del BCRA")}
    results = data.get("results")
    if not results:
        return {"ok": True, "identificacion": cuit, "denominacion": "Sin datos", "causales": []}
    return {"ok": True, **results}


def consultar_bcra_deudas(cuit):
    """Consulta deudas (central de deudores) de una CUIT en la API del BCRA."""
    url = BCRA_DEUDAS_URL.format(cuit=cuit)
    data = _fetch_json(url)
    if not data.get("ok") and data.get("not_found"):
        return {"ok": True, "identificacion": cuit, "denominacion": "Sin datos", "periodos": []}
    if not data.get("ok"):
        return {"ok": False, "error": data.get("error", "No se pudo consultar la API del BCRA")}
    results = data.get("results")
    if not results:
        return {"ok": True, "identificacion": cuit, "denominacion": "Sin datos", "periodos": []}
    return {"ok": True, **results}


def formatear_cheques(data):
    """Formatea los datos de cheques rechazados para incluirlos en un prompt."""
    if not data.get("ok"):
        return f"- BCRA Cheques Rechazados: {data.get('error', 'No disponible')}"
    
    lines = []
    lines.append(f"- BCRA Cheques Rechazados: Encontrados para {data.get('denominacion', 'N/D')} (CUIT: {data.get('identificacion', 'N/D')})")
    
    causales = data.get("causales", [])
    if not causales:
        lines.append("  - Sin cheques rechazados registrados.")
        return "\n".join(lines)
    
    total_cheques = 0
    total_monto = 0.0
    impaga_count = 0
    
    for causal in causales:
        causal_name = causal.get("causal", "Sin especificar")
        entidades = causal.get("entidades", [])
        
        for ent in entidades:
            entidad_name = str(ent.get("entidad", "N/D"))
            detalles = ent.get("detalle", [])
            
            for det in detalles:
                total_cheques += 1
                monto = det.get("monto", 0) or 0
                total_monto += monto
                if det.get("estadoMulta") == "IMPAGA":
                    impaga_count += 1
    
    lines.append(f"  - Total de cheques rechazados: {total_cheques}")
    lines.append(f"  - Monto total rechazado: ${total_monto:,.2f}")
    lines.append(f"  - Cheques impagos (IMPAGA): {impaga_count}")
    
    for causal in causales:
        causal_name = causal.get("causal", "Sin especificar")
        entidades = causal.get("entidades", [])
        if not entidades:
            continue
        
        for ent in entidades:
            entidad_name = str(ent.get("entidad", "N/D"))
            for det in ent.get("detalle", []):
                monto = det.get("monto", 0) or 0
                estado = det.get("estadoMulta") or "Pagado"
                lines.append(
                    f"  - Cheque #{det.get('nroCheque')} | "
                    f"${monto:,.2f} | "
                    f"Rechazo: {det.get('fechaRechazo')} | "
                    f"Estado: {estado} | "
                    f"Entidad: {entidad_name}"
                )
    
    return "\n".join(lines)


def formatear_deudas(data):
    """Formatea los datos de deudas para incluirlos en un prompt."""
    if not data.get("ok"):
        return f"- BCRA Central de Deudores: {data.get('error', 'No disponible')}"
    
    lines = []
    lines.append(f"- BCRA Central de Deudores: Encontrados para {data.get('denominacion', 'N/D')} (CUIT: {data.get('identificacion', 'N/D')})")
    
    periodos = data.get("periodos", [])
    if not periodos:
        lines.append("  - Sin deudas registradas en el sistema financiero.")
        return "\n".join(lines)
    
    for periodo in periodos:
        fec = periodo.get("periodo", "N/D")
        entidades = periodo.get("entidades", [])
        if not entidades:
            continue
        
        lines.append(f"  - Per\u00edodo {fec}: {len(entidades)} entidad(es) reportan")
        for ent in entidades:
            sit = ent.get("situacion", 0)
            monto = ent.get("monto", 0) or 0
            dias = ent.get("diasAtrasoPago", 0) or 0
            refin = "SI" if ent.get("refinanciaciones") else "NO"
            reccat = "SI" if ent.get("recategorizacionOblig") else "NO"
            
            lines.append(
                f"    - {ent.get('entidad', 'N/D')}: "
                f"Sit. {SITUACION_LABELS.get(sit, str(sit))} | "
                f"${monto:,.2f} | "
                f"D\u00edas atraso: {dias} | "
                f"Refin.: {refin} | "
                f"Recat.: {reccat}"
            )
            
            if ent.get("situacionJuridica"):
                lines.append(f"      \u26a0\ufe0f Situaci\u00f3n jur\u00eddica reportada")
            if ent.get("irrecDisposicionTecnica"):
                lines.append(f"      \u26a0\ufe0f Irrecuperable por disposici\u00f3n t\u00e9cnica")
    
    return "\n".join(lines)


def consultar_cuit_online(cuit):
    """Consulta datos fiscales de una CUIT en CUIT Online (cuitonline.com)."""
    try:
        import cuitonline
        results = cuitonline.search(cuit)
        if not results:
            return {"ok": False, "error": "No se encontr\u00f3 la CUIT en CUIT Online"}
        p = results[0]
        return {
            "ok": True,
            "nombre": p.nombre,
            "cuit": p.cuit,
            "tipo_persona": p.tipo_persona,
            "direccion": p.direccion,
            "provincia": p.provincia,
            "localidad": p.localidad,
            "nacionalidad": p.nacionalidad,
            "monotributo": p.monotributo,
            "empleador": p.empleador,
        }
    except ImportError:
        return {"ok": False, "error": "cuitonline no est\u00e1 instalado"}
    except Exception as e:
        logging.warning("CUIT Online error: %s", e)
        return {"ok": False, "error": str(e)}


def formatear_fiscal(data):
    """Formatea los datos fiscales de CUIT Online."""
    if not data.get("ok"):
        return "- CUIT Online: %s" % data.get("error", "No disponible")

    lines = []
    lines.append("- CUIT Online: Datos fiscales encontrados")
    lines.append("  - Raz\u00f3n Social: %s" % data.get("nombre", "N/D"))
    lines.append("  - CUIT Formateado: %s" % data.get("cuit", "N/D"))
    lines.append("  - Tipo: %s" % data.get("tipo_persona", "N/D"))

    if data.get("direccion"):
        lines.append("  - Domicilio: %s" % data["direccion"])
    if data.get("localidad"):
        lines.append("  - Localidad: %s" % data["localidad"])
    if data.get("provincia"):
        lines.append("  - Provincia: %s" % data["provincia"])

    lines.append("  - Monotributo: %s" % (data.get("monotributo") or "No"))
    lines.append("  - Empleador: %s" % ("S\u00ed" if data.get("empleador") else "No"))

    return "\n".join(lines)


def consultar_todo(cuit):
    """Consulta todas las fuentes disponibles para una CUIT y devuelve texto formateado."""
    cheques = consultar_bcra_cheques(cuit)
    deudas = consultar_bcra_deudas(cuit)
    fiscal = consultar_cuit_online(cuit)

    parts = [
        "=== DATOS OBTENIDOS DE FUENTES OFICIALES ===",
        "",
        "[ARCA/AFIP - Datos Fiscales (v\u00eda CUIT Online)]",
        formatear_fiscal(fiscal),
        "",
        "[BCRA - Cheques Rechazados]",
        formatear_cheques(cheques),
        "",
        "[BCRA - Central de Deudores]",
        formatear_deudas(deudas),
        "",
        "=== FIN DE DATOS OFICIALES ===",
    ]
    return "\n".join(parts)
