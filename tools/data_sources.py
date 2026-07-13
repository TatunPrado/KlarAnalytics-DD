"""Real-time data sources for Due Diligence automation.

Currently supports:
- BCRA Central de Deudores API (cheques rechazados + deudas)
- ARCA/AFIP (datos fiscales via cuitcuil.com API)
"""

import json
import logging
import re
import socket
import urllib.request
import urllib.error

BCRA_CHEQUES_URL = "https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/ChequesRechazados/{cuit}"
BCRA_DEUDAS_URL = "https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/{cuit}"

CUITCUIL_API = "https://cuitcuil.com/api"

SITUACION_LABELS = {
    1: "Normal (1)",
    2: "Observaci\u00f3n (2)",
    3: "Problemas (3)",
    4: "Alto Riesgo (4)",
    5: "Irrecuperable (5)",
    6: "Irrecuperable por disposici\u00f3n t\u00e9cnica (6)",
}

_UA = "PrismaConsulting-KlarAnalytics/1.0"


def _fmt_cuit(raw):
    """Convierte CUIT a formato XX-XXXXXXXX-X (11 dígitos sin guiones)."""
    digits = re.sub(r"\D", "", raw)
    if len(digits) != 11:
        return raw
    return "%s-%s-%s" % (digits[:2], digits[2:10], digits[10:])

# ─────────────────────────────────────────────
#  BCRA — Central de Deudores
# ─────────────────────────────────────────────

def _fetch_json(url, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": _UA,
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
        detail = body[:300] if body.strip() else e.reason
        logging.warning("BCRA API HTTP %d for %s: %s", e.code, url, detail)
        return {"ok": False, "error": "HTTP %d - %s" % (e.code, detail)}
    except urllib.error.URLError as e:
        reason = str(e.reason)
        logging.warning("BCRA API URL error for %s: %s", url, reason)
        return {"ok": False, "error": "Error de red: %s" % reason}
    except socket.timeout:
        logging.warning("BCRA API timeout for %s", url)
        return {"ok": False, "error": "Tiempo de espera agotado (BCRA no responde)"}
    except Exception as e:
        logging.warning("BCRA API error for %s: %s", url, e)
        return {"ok": False, "error": str(e)}


def consultar_bcra_cheques(cuit):
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
    if not data.get("ok"):
        return "- BCRA Cheques Rechazados: %s" % data.get("error", "No disponible")
    lines = []
    lines.append("- BCRA Cheques Rechazados: Encontrados para %s (CUIT: %s)" % (
        data.get("denominacion", "N/D"), data.get("identificacion", "N/D")))
    causales = data.get("causales", [])
    if not causales:
        lines.append("  - Sin cheques rechazados registrados.")
        return "\n".join(lines)
    total_cheques = 0
    total_monto = 0.0
    impaga_count = 0
    for causal in causales:
        for ent in causal.get("entidades", []):
            for det in ent.get("detalle", []):
                total_cheques += 1
                monto = det.get("monto", 0) or 0
                total_monto += monto
                if det.get("estadoMulta") == "IMPAGA":
                    impaga_count += 1
    lines.append("  - Total de cheques rechazados: %d" % total_cheques)
    lines.append("  - Monto total rechazado: $%s" % "{:,.2f}".format(total_monto))
    lines.append("  - Cheques impagos (IMPAGA): %d" % impaga_count)
    for causal in causales:
        causal_name = causal.get("causal", "Sin especificar")
        for ent in causal.get("entidades", []):
            entidad_name = str(ent.get("entidad", "N/D"))
            for det in ent.get("detalle", []):
                monto = det.get("monto", 0) or 0
                estado = det.get("estadoMulta") or "Pagado"
                lines.append("  - Cheque #%s | $%s | Rechazo: %s | Estado: %s | Entidad: %s" % (
                    det.get("nroCheque"), "{:,.2f}".format(monto),
                    det.get("fechaRechazo"), estado, entidad_name))
    return "\n".join(lines)


def formatear_deudas(data):
    if not data.get("ok"):
        return "- BCRA Central de Deudores: %s" % data.get("error", "No disponible")
    lines = []
    lines.append("- BCRA Central de Deudores: Encontrados para %s (CUIT: %s)" % (
        data.get("denominacion", "N/D"), data.get("identificacion", "N/D")))
    periodos = data.get("periodos", [])
    if not periodos:
        lines.append("  - Sin deudas registradas en el sistema financiero.")
        return "\n".join(lines)
    for periodo in periodos:
        fec = periodo.get("periodo", "N/D")
        entidades = periodo.get("entidades", [])
        if not entidades:
            continue
        lines.append("  - Per\u00edodo %s: %d entidad(es) reportan" % (fec, len(entidades)))
        for ent in entidades:
            sit = ent.get("situacion", 0)
            monto = ent.get("monto", 0) or 0
            dias = ent.get("diasAtrasoPago", 0) or 0
            refin = "SI" if ent.get("refinanciaciones") else "NO"
            reccat = "SI" if ent.get("recategorizacionOblig") else "NO"
            lines.append("    - %s: Sit. %s | $%s | D\u00edas atraso: %d | Refin.: %s | Recat.: %s" % (
                ent.get("entidad", "N/D"), SITUACION_LABELS.get(sit, str(sit)),
                "{:,.2f}".format(monto), dias, refin, reccat))
            if ent.get("situacionJuridica"):
                lines.append("      \u26a0\ufe0f Situaci\u00f3n jur\u00eddica reportada")
            if ent.get("irrecDisposicionTecnica"):
                lines.append("      \u26a0\ufe0f Irrecuperable por disposici\u00f3n t\u00e9cnica")
    return "\n".join(lines)


# ─────────────────────────────────────────────
#  ARCA / AFIP — Datos fiscales via cuitcuil.com
# ─────────────────────────────────────────────

def consultar_fiscal(cuit):
    """Consulta datos fiscales de una CUIT via cuitcuil.com/api.

    La API de cuitcuil.com consulta el padrón de ARCA/AFIP en vivo.
    """
    import requests
    clean = re.sub(r"\D", "", cuit)
    if len(clean) != 11:
        return {"ok": False, "error": "CUIT inv\u00e1lido: debe tener 11 d\u00edgitos"}
    try:
        r = requests.get(
            "%s/persona/%s" % (CUITCUIL_API, clean),
            headers={"User-Agent": _UA, "Accept": "application/json"},
            timeout=15,
        )
        if r.status_code == 404:
            return {"ok": False, "error": "CUIT no encontrada en el padr\u00f3n ARCA/AFIP"}
        r.raise_for_status()
        data = r.json()
        domicilio = data.get("domicilioFiscal", {})
        result = {
            "ok": True,
            "nombre": data.get("razonSocial", ""),
            "cuit": _fmt_cuit(data.get("cuit", clean)),
            "tipo_persona": data.get("tipoPersona", ""),
            "estado": data.get("estadoClave", ""),
            "condicion_iva": data.get("condicionIVA", ""),
            "es_empleador": data.get("esEmpleador", False),
            "direccion": domicilio.get("direccion", ""),
            "localidad": domicilio.get("localidad", ""),
            "provincia": domicilio.get("provincia", ""),
            "codigo_postal": domicilio.get("codigoPostal", ""),
            "mes_cierre": data.get("mesCierre", ""),
            "actividades": [
                {"codigo": a.get("id"), "descripcion": a.get("descripcion"), "periodo": a.get("periodo")}
                for a in data.get("actividades", [])
            ],
            "impuestos": [
                {"descripcion": i.get("descripcion"), "estado": i.get("estado")}
                for i in data.get("impuestos", [])
            ],
        }
        # Detectar condición de IVA desde impuestos si no vino directo
        if not result["condicion_iva"]:
            iva_inscripto = any("IVA" in i["descripcion"] and i["estado"] == "ACTIVO" for i in result["impuestos"] if "descripcion" in i)
            result["condicion_iva"] = "IVA Inscripto" if iva_inscripto else "No disponible"
        return result
    except requests.exceptions.Timeout:
        return {"ok": False, "error": "Tiempo de espera agotado al consultar ARCA"}
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el servicio de ARCA (cuitcuil.com)"}
    except Exception as e:
        logging.warning("ARCA fiscal API error: %s", e)
        return {"ok": False, "error": str(e)}


def formatear_fiscal(data):
    if not data.get("ok"):
        return "- ARCA/AFIP: %s" % data.get("error", "No disponible")
    lines = []
    lines.append("- ARCA/AFIP: Datos fiscales encontrados (v\u00eda cuitcuil.com)")
    lines.append("  - Raz\u00f3n Social: %s" % data.get("nombre", "N/D"))
    lines.append("  - CUIT: %s" % data.get("cuit", "N/D"))
    lines.append("  - Tipo: %s" % data.get("tipo_persona", "N/D"))
    lines.append("  - Estado: %s" % data.get("estado", "N/D"))
    lines.append("  - Condici\u00f3n IVA: %s" % data.get("condicion_iva", "N/D"))
    if data.get("direccion"):
        lines.append("  - Domicilio: %s" % data["direccion"])
    if data.get("localidad"):
        lines.append("  - Localidad: %s" % data["localidad"])
    if data.get("provincia"):
        lines.append("  - Provincia: %s" % data["provincia"])
    lines.append("  - Empleador: %s" % ("S\u00ed" if data.get("es_empleador") else "No"))
    actividades = data.get("actividades", [])
    if actividades:
        lines.append("  - Actividades registradas:")
        for a in actividades[:5]:
            lines.append("    - %s: %s" % (a.get("codigo", ""), a.get("descripcion", "")))
    return "\n".join(lines)


# ─────────────────────────────────────────────
#  Todo en uno
# ─────────────────────────────────────────────

def consultar_todo(cuit):
    """Consulta todas las fuentes disponibles y devuelve texto formateado."""
    cheques = consultar_bcra_cheques(cuit)
    deudas = consultar_bcra_deudas(cuit)
    fiscal = consultar_fiscal(cuit)

    parts = [
        "=== DATOS OBTENIDOS DE FUENTES OFICIALES ===",
        "",
        "[ARCA/AFIP - Datos Fiscales]",
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


# Backward-compatible alias
consultar_cuit_online = consultar_fiscal
