"""PDF report generation with Prisma Consulting branding."""

import io
import re
from datetime import date

from fpdf import FPDF

BLUE = (37, 99, 235)
DARK = (15, 23, 42)
GRAY = (71, 85, 105)
LIGHT_GRAY = (148, 163, 184)
WHITE = (255, 255, 255)
MUTED_BG = (248, 250, 252)

DISCLAIMER = (
    "Este informe ha sido generado por inteligencia artificial de Prisma Consulting "
    "a traves de Klar Analytics. El analisis se basa en las respuestas brindadas "
    "por el cliente y en datos obtenidos de fuentes publicas oficiales (BCRA, ARCA/AFIP). "
    "Este documento no constituye un analisis profundo ni una auditoria profesional, "
    "sino un diagnostico preliminar orientado a simplificar la toma de decisiones. "
    "Se recomienda verificar los hallazgos con un profesional calificado."
)


class ReportPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*LIGHT_GRAY)
        self.cell(0, 4, "Prisma Consulting | Klar Analytics", align="R")
        self.ln(2)
        self.set_draw_color(*LIGHT_GRAY)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-20)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*LIGHT_GRAY)
        self.cell(0, 10, "Pagina %d/{nb}" % self.page_no(), align="C")


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


def _write_disclaimer(pdf):
    pdf.ln(8)
    pdf.set_draw_color(37, 99, 235)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 4, "Descargo de responsabilidad")
    pdf.ln(1)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(0, 4, DISCLAIMER)


CW = 190  # effective content width (210 - 10*2 margins)

_REPLACEMENTS = {
    "\u2014": "-",   # em dash
    "\u2013": "-",   # en dash
    "\u2018": "'",   # left single quote
    "\u2019": "'",   # right single quote
    "\u201c": '"',   # left double quote
    "\u201d": '"',   # right double quote
    "\u2022": "-",   # bullet
    "\u2026": "...", # ellipsis
    "\u00a0": " ",   # non-breaking space
}

def _sanitize(text):
    """Replace non-Latin-1 characters with ASCII equivalents."""
    for orig, repl in _REPLACEMENTS.items():
        text = text.replace(orig, repl)
    # Encode to latin-1, replacing any remaining non-latin-1 chars
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    return text

def _mc(pdf, w, h, text):
    """multi_cell wrapper that resets x to left margin first."""
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(w, h, text)

def _write_content(pdf, title, content_text):
    for el_type, text in _parse_markdown_text(content_text):
        if el_type == "empty":
            pdf.ln(3)
        elif el_type == "h1":
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 7, text)
            pdf.ln(2)
        elif el_type == "h2":
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(*BLUE)
            _mc(pdf, CW, 6, text)
            pdf.ln(1)
        elif el_type == "h3":
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 5, text)
        elif el_type == "bullet":
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(*GRAY)
            _mc(pdf, CW, 4, "  - " + text)
        elif el_type == "table":
            pdf.set_font("Courier", "", 7)
            pdf.set_text_color(*DARK)
            cells = [c.strip() for c in text.split("|")]
            line = "  ".join(cells)
            _mc(pdf, CW, 3.5, line)
        elif el_type == "bold":
            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(*DARK)
            _mc(pdf, CW, 4, text)
        else:
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(*GRAY)
            _mc(pdf, CW, 4.5, text)


def generate_pdf(company, cuit, title_text, content, include_disclaimer=True):
    """Generate a branded PDF report. Returns bytes."""
    company = _sanitize(company)
    cuit = _sanitize(cuit)
    content = _sanitize(content)
    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # --- Cover / Header area ---
    w = pdf.w

    # Blue accent bar at top
    pdf.set_fill_color(*BLUE)
    pdf.rect(0, 0, w, 8, "F")

    # Logo area - use simple ASCII since core fonts don't support unicode
    pdf.ln(14)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(*BLUE)
    pdf.cell(0, 10, "PRISMA CONSULTING", align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 6, "Klar Analytics - Diagnostico con IA para PYMES", align="C")
    pdf.ln(10)

    # Separator
    pdf.set_draw_color(*BLUE)
    pdf.set_line_width(0.3)
    y = pdf.get_y()
    pdf.line(50, y, 160, y)
    pdf.ln(8)

    # Report title
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 8, title_text, align="C")
    pdf.ln(4)

    # Company / meta info box
    pdf.set_fill_color(*MUTED_BG)
    pdf.set_x(30)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*DARK)
    today_str = date.today().strftime('%d/%m/%Y')
    meta = "Empresa: %s  |  CUIT: %s  |  Fecha: %s" % (company, cuit, today_str)
    w_meta = pdf.get_string_width(meta) + 20
    pdf.cell(w_meta, 8, meta, border=0, fill=True, align="C")
    pdf.ln(12)

    # --- Content ---
    _write_content(pdf, title_text, content)

    # --- Disclaimer ---
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
