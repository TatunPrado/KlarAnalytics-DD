"""PDF report generation with Prisma Consulting branding - professional layout."""

import io
import re
from datetime import date

from fpdf import FPDF

NAVY = (15, 27, 45)
NAVY_LIGHT = (26, 45, 74)
BLUE = (37, 99, 235)
BLUE_LIGHT = (219, 234, 254)
DARK = (15, 23, 42)
GRAY = (71, 85, 105)
LIGHT_GRAY = (148, 163, 184)
WHITE = (255, 255, 255)
MUTED_BG = (248, 250, 252)
GREEN = (16, 185, 129)
GREEN_BG = (236, 253, 245)
AMBER = (245, 158, 11)
AMBER_BG = (255, 251, 235)
RED = (239, 68, 68)
RED_BG = (254, 242, 242)
RED_DARK = (127, 29, 29)
RED_DARK_BG = (254, 226, 226)
BORDER = (226, 232, 240)

DISCLAIMER = (
    "Este informe ha sido generado por inteligencia artificial de Prisma Consulting "
    "a traves de Klar Analytics. El analisis se basa en las respuestas brindadas "
    "por el cliente y en datos obtenidos de fuentes publicas oficiales (BCRA, ARCA/AFIP). "
    "Este documento no constituye un analisis profundo ni una auditoria profesional, "
    "sino un diagnostico preliminar orientado a simplificar la toma de decisiones. "
    "Se recomienda verificar los hallazgos con un profesional calificado."
)

_REPLACEMENTS = {
    "\u2014": "-", "\u2013": "-",
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2022": "-", "\u2026": "...", "\u00a0": " ",
}

LM = 15
CW = 180  # 210 - 15*2

def _sanitize(text):
    for orig, repl in _REPLACEMENTS.items():
        text = text.replace(orig, repl)
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    return text

def _mc(pdf, w, h, text, align="L"):
    pdf.set_x(LM)
    pdf.multi_cell(w, h, text, align=align)

def _risk_color(score):
    if score <= 20:   return GREEN, GREEN_BG
    if score <= 40:   return GREEN, GREEN_BG
    if score <= 60:   return AMBER, AMBER_BG
    if score <= 80:   return RED, RED_BG
    return RED_DARK, RED_DARK_BG

def _risk_label(score):
    if score <= 20:   return "Bajo"
    if score <= 40:   return "Bajo-Medio"
    if score <= 60:   return "Medio"
    if score <= 80:   return "Alto"
    return "Critico"

def _risk_badge_color(score):
    if score <= 20:   return GREEN, GREEN_BG
    if score <= 40:   return GREEN, GREEN_BG
    if score <= 60:   return AMBER, AMBER_BG
    if score <= 80:   return RED, RED_BG
    return RED_DARK, RED_DARK_BG

def _draw_risk_bar(pdf, y, score, w=140, h=8):
    pdf.set_fill_color(226, 232, 240)
    pdf.rect(LM, y, w, h, "F")
    fill_color, _ = _risk_color(score)
    pdf.set_fill_color(*fill_color)
    fill_w = max(w * score / 100, 4)
    pdf.rect(LM, y, fill_w, h, "F")

def _parse_scores(text):
    scores = {}
    m = re.search(r"===SCORES===\s*(.*?)\s*===END SCORES===", text, re.DOTALL)
    if not m:
        return scores
    for line in m.group(1).split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip().lower()
            val = val.strip()
            if key == "recomendacion":
                scores["recomendacion"] = val
            else:
                try:
                    scores[key] = int(re.sub(r"[^0-9]", "", val))
                except ValueError:
                    pass
    return scores

def _strip_scores_section(text):
    return re.sub(r"\n===SCORES===\s*.*?\s*===END SCORES===", "", text, flags=re.DOTALL)


class ReportPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*LIGHT_GRAY)
        self.cell(0, 4, "Prisma Consulting | Klar Analytics", align="R")
        self.ln(2)
        self.set_draw_color(*LIGHT_GRAY)
        self.line(LM, self.get_y(), 210 - LM, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-20)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*LIGHT_GRAY)
        self.cell(0, 10, "Pagina %d/{nb}" % self.page_no(), align="C")


def _cover_page(pdf, company, cuit, title_text, scores):
    w = 210

    # Dark navy block
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, w, 95, "F")

    # Accent line
    pdf.set_fill_color(*BLUE)
    pdf.rect(0, 95, w, 3, "F")

    pdf.ln(25)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*BLUE_LIGHT)
    pdf.cell(0, 5, "PRISMA CONSULTING", align="C")
    pdf.ln(7)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*LIGHT_GRAY)
    pdf.cell(0, 4, "Klar Analytics - Diagnostico con IA para PYMES", align="C")
    pdf.ln(20)

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*WHITE)
    _mc(pdf, CW, 9, title_text, "C")
    pdf.ln(6)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(148, 163, 184)
    pdf.cell(0, 6, company, align="C")
    pdf.ln(20)

    # Meta info
    today_str = date.today().strftime('%d/%m/%Y')
    meta_lines = [
        ("CUIT", cuit),
        ("Fecha", today_str),
        ("Clasificacion", "USO CONFIDENCIAL"),
    ]
    pdf.set_font("Helvetica", "", 8)
    for label, val in meta_lines:
        pdf.set_text_color(*LIGHT_GRAY)
        pdf.cell(0, 5, "%s: %s" % (label, val), align="C")
        pdf.ln(4.5)

    # Overall score card
    general = scores.get("general")
    if general is not None:
        pdf.ln(12)
        color, bg = _risk_color(general)
        label = _risk_label(general)
        # Score circle placeholder
        pdf.set_fill_color(*color)
        pdf.rect(80, pdf.get_y(), 50, 30, "F")
        pdf.set_text_color(*WHITE)
        pdf.set_font("Helvetica", "B", 18)
        y = pdf.get_y()
        pdf.set_xy(80, y + 3)
        pdf.cell(50, 10, str(general), align="C")
        pdf.set_xy(80, y + 15)
        pdf.set_font("Helvetica", "B", 7)
        pdf.cell(50, 5, "RIESGO " + label.upper(), align="C")


def _score_card(pdf, factor_name, score, y_start, w=CW):
    label = _risk_label(score) if score is not None else "N/D"
    color, _ = _risk_color(score) if score is not None else (GRAY, MUTED_BG)
    display_score = str(score) if score is not None else "--"
    h = 24

    # Card background
    pdf.set_fill_color(*WHITE)
    pdf.set_draw_color(*BORDER)
    pdf.rect(LM, y_start, w, h, "DF")

    # Left accent bar
    pdf.set_fill_color(*color)
    pdf.rect(LM, y_start, 3, h, "F")

    # Score number
    pdf.set_text_color(*color)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_xy(LM + 10, y_start + 3)
    pdf.cell(16, 7, display_score)

    # Label
    pdf.set_text_color(*DARK)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_xy(LM + 10, y_start + 12)
    pdf.cell(w - 55, 4, factor_name.upper())

    # Risk bar
    if score is not None:
        bar_x = LM + 10
        bar_y = y_start + 18
        bar_w = w - 55
        pdf.set_fill_color(226, 232, 240)
        pdf.rect(bar_x, bar_y, bar_w, 3, "F")
        pdf.set_fill_color(*color)
        fill_w = max(bar_w * score / 100, 3)
        pdf.rect(bar_x, bar_y, fill_w, 3, "F")

    # Badge
    badge_w = pdf.get_string_width(label) + 8
    if badge_w < 20:
        badge_w = 20
    pdf.set_fill_color(*color)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Helvetica", "B", 6)
    badge_x = LM + w - badge_w - 8
    pdf.set_xy(badge_x, y_start + 5)
    pdf.cell(badge_w, 6, label, fill=True, align="C")


def _parse_markdown_text(text):
    lines = text.split("\n")
    parsed = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            parsed.append(("empty", ""))
        elif stripped.startswith("### "):
            parsed.append(("h3", stripped[4:]))
        elif stripped.startswith("## "):
            parsed.append(("h2", stripped[3:]))
        elif stripped.startswith("# "):
            parsed.append(("h1", stripped[2:]))
        elif stripped.startswith("- ") or stripped.startswith("* "):
            parsed.append(("bullet", stripped[2:]))
        elif stripped.startswith("|"):
            parsed.append(("table", stripped.strip("|").strip()))
        elif stripped.startswith("**") and stripped.endswith("**"):
            parsed.append(("bold", stripped.strip("*")))
        else:
            parsed.append(("text", stripped))
    return parsed


def _write_body(pdf, content):
    for el_type, text in _parse_markdown_text(content):
        if el_type == "empty":
            pdf.ln(3)
        elif el_type == "h1":
            pdf.ln(4)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 7, text)
            pdf.ln(2)
        elif el_type == "h2":
            pdf.ln(3)
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(*BLUE)
            _mc(pdf, CW, 6, text)
            pdf.ln(1)
        elif el_type == "h3":
            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 5, text)
        elif el_type == "bullet":
            pdf.set_font("Helvetica", "", 8.5)
            pdf.set_text_color(*GRAY)
            _mc(pdf, CW, 4, "  - " + text)
        elif el_type == "table":
            pdf.set_font("Courier", "", 7)
            pdf.set_text_color(*DARK)
            cells = [c.strip() for c in text.split("|")]
            _mc(pdf, CW, 3.5, "  ".join(cells))
        elif el_type == "bold":
            pdf.set_font("Helvetica", "B", 8.5)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 4, text)
        else:
            pdf.set_font("Helvetica", "", 8.5)
            pdf.set_text_color(*GRAY)
            _mc(pdf, CW, 4.5, text)


def _write_disclaimer(pdf):
    pdf.ln(8)
    pdf.set_draw_color(*BLUE)
    pdf.set_line_width(0.5)
    pdf.line(LM, pdf.get_y(), 210 - LM, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*DARK)
    _mc(pdf, CW, 4, "Descargo de responsabilidad")
    pdf.ln(1)
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(*GRAY)
    _mc(pdf, CW, 3.5, DISCLAIMER)


def generate_pdf(company, cuit, title_text, content, include_disclaimer=True):
    company = _sanitize(company)
    cuit = _sanitize(cuit)
    content = _sanitize(content)

    scores = _parse_scores(content)
    body = _strip_scores_section(content)

    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    _cover_page(pdf, company, cuit, title_text, scores)

    # New page for body
    pdf.add_page()

    # Score summary cards (if we have parsed scores)
    factor_order = [
        ("financiero", "Financiero"),
        ("tributario", "Tributario"),
        ("legal", "Legal"),
        ("aml", "AML / Sanciones"),
        ("reputacional", "Reputacional"),
        ("operativo", "Operativo"),
        ("compliance", "Compliance"),
    ]
    factors_with_scores = [(key, name) for key, name in factor_order if key in scores]
    if factors_with_scores:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*DARK)
        _mc(pdf, CW, 6, "RESUMEN DE RIESGOS")
        pdf.ln(3)

        for key, name in factors_with_scores:
            score = scores.get(key)
            y = pdf.get_y()
            _score_card(pdf, name, score, y)
            pdf.set_y(y + 27)

        pdf.ln(3)

        # General score line
        general = scores.get("general")
        rec = scores.get("recomendacion", "")
        if general is not None:
            color, _ = _risk_color(general)
            label = _risk_label(general)
            pdf.set_fill_color(*color)
            y = pdf.get_y()
            pdf.rect(LM, y, CW, 12, "F")
            pdf.set_text_color(*WHITE)
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_xy(LM + 8, y + 1)
            pdf.cell(50, 5, "Score General: %d" % general)
            pdf.set_xy(LM + 8, y + 6)
            pdf.set_font("Helvetica", "B", 7)
            pdf.cell(50, 4, label.upper())
            if rec:
                pdf.set_xy(LM + 70, y + 2)
                pdf.set_font("Helvetica", "B", 8)
                pdf.cell(CW - 78, 8, rec.upper(), align="R")
            pdf.set_y(y + 16)
            pdf.ln(4)

        pdf.set_draw_color(*BORDER)
        pdf.line(LM, pdf.get_y(), 210 - LM, pdf.get_y())
        pdf.ln(4)

    # Body content
    _write_body(pdf, body)

    if include_disclaimer:
        _write_disclaimer(pdf)

    return bytes(pdf.output())


def make_dd_pdf(company, cuit, dd_text):
    return generate_pdf(
        company, cuit,
        "Informe de Due Diligence Automatico",
        dd_text,
    )


def make_diagnosis_pdf(company, cuit, diagnosis_text):
    return generate_pdf(
        company, cuit,
        "Diagnostico Empresarial",
        diagnosis_text,
    )


def make_complete_pdf(company, cuit, dd_text, diagnosis_text):
    combined = ""
    if dd_text:
        combined += "## 1. INFORME DE DUE DILIGENCE\n\n" + dd_text + "\n\n"
    if diagnosis_text:
        combined += "## 2. DIAGNOSTICO EMPRESARIAL\n\n" + diagnosis_text
    return generate_pdf(
        company, cuit,
        "Informe Completo: Due Diligence + Diagnostico",
        combined,
    )
