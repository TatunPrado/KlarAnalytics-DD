"""
Playwright-based scraper for BCRA financial data.

Usage:
    python bcra_scraper.py <CUIT> [--output <file.json>] [--headless]

Queries:
  - Cheques Rechazados: https://www.bcra.gob.ar/BCRAyVos/Cheques_rechazados.asp
  - Central de Deudores: https://www.bcra.gob.ar/BCRAyVos/Deudores.asp

Requires Playwright installed:
    pip install playwright
    playwright install chromium
"""

import argparse, json, sys, os, re, datetime
from typing import Dict, Optional

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
except ImportError:
    print(json.dumps({"error": "Playwright no instalado. Ejecut\u00e1: pip install playwright && playwright install chromium"}, ensure_ascii=False))
    sys.exit(1)


BCRA_DEUDORES_URL = "https://www.bcra.gob.ar/BCRAyVos/Deudores.asp"
BCRA_CHEQUES_URL  = "https://www.bcra.gob.ar/BCRAyVos/Cheques_rechazados.asp"
TIMEOUT = 15000


def _wait_and_fill(page, selector: str, value: str):
    page.wait_for_selector(selector, timeout=TIMEOUT)
    page.fill(selector, value)


def _extract_table(page) -> list:
    rows = []
    tables = page.query_selector_all("table")
    for table in tables:
        for tr in table.query_selector_all("tr"):
            cells = [td.inner_text().strip() for td in tr.query_selector_all("td, th")]
            if cells:
                rows.append(cells)
    return rows


def scrape_cheques_rechazados(cuit: str, headless: bool = True) -> Dict:
    result = {
        "fuente": "BCRA Cheques Rechazados",
        "url": BCRA_CHEQUES_URL,
        "cuit_consultado": cuit,
        "cheques": [],
        "cantidad_total": 0,
        "monto_total": None,
        "hay_rechazos": False,
        "error": None,
        "fecha_consulta": datetime.date.today().isoformat(),
    }
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            page.goto(BCRA_CHEQUES_URL, wait_until="networkidle", timeout=TIMEOUT * 2)

            form = page.query_selector("form")
            if form:
                _wait_and_fill(page, "input[name='cuit'], input[type='text']", cuit)
                page.click("input[type='submit'], button[type='submit'], button:has-text('Consultar')")
                page.wait_for_timeout(3000)
            else:
                _wait_and_fill(page, "input[type='text'], input[name='cuit']", cuit)
                page.keyboard.press("Enter")
                page.wait_for_timeout(3000)

            rows = _extract_table(page)
            if rows:
                cheques = []
                for r in rows[1:]:
                    cheques.append({
                        "fecha": r[0] if len(r) > 0 else "",
                        "motivo": r[1] if len(r) > 1 else "",
                        "monto": r[2] if len(r) > 2 else "",
                        "estado": r[3] if len(r) > 3 else "",
                    })
                result["cheques"] = cheques
                result["cantidad_total"] = len(cheques)
                result["hay_rechazos"] = len(cheques) > 0
                if cheques:
                    montos = []
                    for c in cheques:
                        try:
                            montos.append(float(c["monto"].replace(".", "").replace(",", ".").replace("$", "").strip()))
                        except ValueError:
                            pass
                    if montos:
                        result["monto_total"] = sum(montos)

            browser.close()
    except Exception as e:
        result["error"] = str(e)

    return result


def scrape_central_deudores(cuit: str, headless: bool = True) -> Dict:
    result = {
        "fuente": "BCRA Central de Deudores",
        "url": BCRA_DEUDORES_URL,
        "cuit_consultado": cuit,
        "requiere_autenticacion": True,
        "datos": None,
        "error": None,
        "fecha_consulta": datetime.date.today().isoformat(),
    }
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            page.goto(BCRA_DEUDORES_URL, wait_until="networkidle", timeout=TIMEOUT * 2)

            page_content = page.content().lower()
            if "clave" in page_content and ("fiscal" in page_content or "afip" in page_content):
                result["error"] = "REQUIERE_CLAVE_FISCAL: La consulta a Central de Deudores requiere autenticaci\u00f3n con Clave Fiscal del titular."
                browser.close()
                return result

            form = page.query_selector("form")
            if form:
                _wait_and_fill(page, "input[type='text'], input[name='cuit']", cuit)
                page.click("input[type='submit'], button[type='submit']")
                page.wait_for_timeout(3000)
                rows = _extract_table(page)
                if rows:
                    result["datos"] = rows
                    result["requiere_autenticacion"] = False

            browser.close()
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="BCRA Financial Data Scraper (Playwright)")
    parser.add_argument("cuit", help="CUIT a consultar (formato: 20-12345678-9 o 30123456789)")
    parser.add_argument("--output", "-o", help="Archivo JSON de salida")
    parser.add_argument("--headless", action="store_true", default=True, help="Modo headless (sin ventana)")
    parser.add_argument("--visible", action="store_false", dest="headless", help="Modo visible (con ventana)")
    args = parser.parse_args()

    cuit_clean = re.sub(r"\D", "", args.cuit)
    if len(cuit_clean) not in (11,):
        print(json.dumps({"error": f"CUIT inv\u00e1lido: {args.cuit}. Debe tener 11 d\u00edgitos."}, ensure_ascii=False))
        sys.exit(1)

    result = {
        "cuit": cuit_clean,
        "fecha": datetime.date.today().isoformat(),
        "cheques_rechazados": scrape_cheques_rechazados(cuit_clean, headless=args.headless),
        "central_deudores": scrape_central_deudores(cuit_clean, headless=args.headless),
    }

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Resultado guardado en: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
