"""HTML report generation with Prisma Consulting / Klar Analytics branding.
Generates a self-contained, professional HTML report inspired by the
DUE DILIGENCE project's Big Four style, without external dependencies.
"""

import re
from datetime import date

BLUE = "#2563eb"
DARK = "#0f172a"
GRAY = "#475569"
LIGHT_GRAY = "#94a3b8"
WHITE = "#ffffff"
BG = "#f8fafc"
BORDER = "#e2e8f0"
NAVY = "#0f172a"
GREEN = "#10b981"
AMBER = "#f59e0b"
RED = "#ef4444"
RED_DARK = "#7f1d1d"


def _risk_color(score):
    if score is None: return GRAY
    if score <= 20:   return GREEN
    if score <= 40:   return GREEN
    if score <= 60:   return AMBER
    if score <= 80:   return RED
    return RED_DARK


def _risk_label(score):
    if score is None: return "N/D"
    if score <= 20:   return "Bajo"
    if score <= 40:   return "Bajo-Medio"
    if score <= 60:   return "Medio"
    if score <= 80:   return "Alto"
    return "Critico"


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


def _md_to_html(text):
    """Convert basic markdown (bold, italic, lists, headings) to HTML."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"^### (.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.+)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^# (.+)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)
    lines = text.split("\n")
    in_list = False
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                result.append("<ul>")
                in_list = True
            result.append("<li>%s</li>" % stripped[2:])
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(line)
    if in_list:
        result.append("</ul>")
    text = "\n".join(result)
    text = re.sub(r"\n\n+", r"</p><p>", text)
    text = "<p>" + text + "</p>"
    return text


def _build_score_cards(scores):
    factor_order = [
        ("financiero",  "Financiero",       20),
        ("tributario",  "Tributario",       15),
        ("legal",       "Legal / Societario", 20),
        ("aml",         "AML / Sanciones",  20),
        ("reputacional","Reputacional",     10),
        ("operativo",   "Operativo",         5),
        ("compliance",  "Compliance",       10),
    ]
    cards = []
    for key, name, peso in factor_order:
        score = scores.get(key)
        color = _risk_color(score)
        label = _risk_label(score)
        display = str(score) if score is not None else "--"
        bar_pct = min(score, 100) if score is not None else 0
        cards.append("""
        <div class="score-card">
            <div class="sc-header">
                <span class="sc-name">%s</span>
                <span class="sc-weight">%d%%%%</span>
            </div>
            <div class="sc-body">
                <div class="sc-number" style="color:%s">%s</div>
                <div class="sc-bar-wrap">
                    <div class="sc-bar"><div class="sc-fill" style="width:%d%%%%;background:%s"></div></div>
                </div>
                <span class="sc-badge" style="background:%s">%s</span>
            </div>
        </div>""" % (name, peso, color, display, bar_pct, color, color, label))
    return "\n".join(cards)


def _build_styles():
    return f"""
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: {BG};
    color: {DARK};
    line-height: 1.6;
}}

/* ============ SIDEBAR ============ */
.sidebar {{
    position: fixed; top: 0; left: 0; bottom: 0; width: 220px;
    background: {DARK}; color: #fff; z-index: 100;
    display: flex; flex-direction: column; padding: 28px 0;
    overflow-y: auto;
}}
.sidebar-brand {{
    padding: 0 20px 20px; border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 12px;
}}
.sidebar-brand h3 {{ font-size: 0.7rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: {BLUE}; }}
.sidebar-brand p {{ font-size: 0.6rem; color: rgba(255,255,255,0.4); margin-top: 4px; }}
.sidebar a {{
    display: block; padding: 10px 20px; font-size: 0.78rem; color: rgba(255,255,255,0.6);
    text-decoration: none; transition: all 0.2s; border-left: 3px solid transparent;
}}
.sidebar a:hover {{ color: #fff; background: rgba(255,255,255,0.05); }}
.sidebar a.active {{ color: #fff; background: rgba(37,99,235,0.15); border-left-color: {BLUE}; }}

/* ============ COVER ============ */
.cover {{
    position: relative; min-height: 100vh;
    background: linear-gradient(135deg, {DARK} 0%, #0a0f1a 50%, {DARK} 100%);
    display: flex; align-items: center; justify-content: center;
    text-align: center; padding: 60px 40px 60px 260px; overflow: hidden;
}}
.cover::before {{
    content: ''; position: absolute; top: -30%; right: -20%;
    width: 70%; height: 120%;
    background: radial-gradient(ellipse, rgba(37,99,235,0.08) 0%, transparent 70%);
}}
.cover::after {{
    content: ''; position: absolute; bottom: -20%; left: -10%;
    width: 50%; height: 80%;
    background: radial-gradient(ellipse, rgba(16,185,129,0.05) 0%, transparent 70%);
}}
.cover-content {{ position: relative; z-index: 1; max-width: 750px; }}
.cover-badge {{
    display: inline-block; padding: 8px 28px;
    border: 1px solid rgba(255,255,255,0.15); border-radius: 100px;
    color: rgba(255,255,255,0.7); font-size: 0.7rem; font-weight: 600;
    letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 32px;
    background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);
}}
.cover h1 {{
    font-size: 0.85rem; font-weight: 400; color: {BLUE};
    letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px;
}}
.cover h2 {{
    font-size: 3rem; font-weight: 800; color: #fff;
    margin-bottom: 8px; letter-spacing: -0.03em; line-height: 1.15;
}}
.cover .cover-subtitle {{ font-size: 1.2rem; color: rgba(255,255,255,0.5); margin-bottom: 40px; font-weight: 300; }}
.cover-meta {{
    display: flex; flex-wrap: wrap; gap: 12px; justify-content: center;
}}
.cover-meta p {{
    background: rgba(255,255,255,0.06); padding: 10px 22px; border-radius: 8px;
    color: rgba(255,255,255,0.7); font-size: 0.8rem;
    border: 1px solid rgba(255,255,255,0.06);
}}
.cover-meta strong {{ color: #fff; }}
.cover-line {{
    width: 60px; height: 3px; background: {BLUE}; margin: 20px auto 24px; border-radius: 2px;
}}

/* ============ MAIN ============ */
.main-wrap {{ margin-left: 220px; }}
.main-content {{ max-width: 860px; margin: 0 auto; padding: 48px 40px; }}

/* ============ GENERAL SCORE ============ */
.hero-score {{
    border-radius: 16px; padding: 36px 40px; margin-bottom: 40px;
    color: #fff; display: flex; align-items: center; justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}}
.hero-left {{ display: flex; align-items: center; gap: 24px; }}
.hero-number {{ font-size: 3.5rem; font-weight: 800; line-height: 1; letter-spacing: -0.03em; }}
.hero-label {{ font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; opacity: 0.85; }}
.hero-verdict {{
    font-size: 1.1rem; font-weight: 700; letter-spacing: 0.02em;
    text-align: right; line-height: 1.4;
}}
.hero-verdict small {{ display: block; font-size: 0.65rem; font-weight: 400; opacity: 0.6; margin-top: 4px; }}

/* ============ SECTIONS ============ */
section {{ margin-bottom: 48px; }}
.section-title {{
    font-size: 1.3rem; font-weight: 700; color: {DARK};
    margin-bottom: 20px; padding-bottom: 10px;
    border-bottom: 2px solid {BLUE}; letter-spacing: -0.02em;
}}

/* ============ SCORE CARDS GRID ============ */
.score-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
.score-card {{
    background: #fff; border-radius: 12px; padding: 16px 20px;
    border: 1px solid {BORDER}; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; flex-direction: column; gap: 10px;
}}
.sc-header {{ display: flex; justify-content: space-between; align-items: center; }}
.sc-name {{ font-size: 0.75rem; font-weight: 700; color: {DARK}; text-transform: uppercase; letter-spacing: 0.03em; }}
.sc-weight {{ font-size: 0.6rem; color: {LIGHT_GRAY}; }}
.sc-body {{ display: flex; align-items: center; gap: 12px; }}
.sc-number {{ font-size: 1.5rem; font-weight: 800; min-width: 40px; text-align: right; line-height: 1; }}
.sc-bar-wrap {{ flex: 1; }}
.sc-bar {{ height: 6px; background: {BORDER}; border-radius: 3px; overflow: hidden; }}
.sc-fill {{ height: 100%; border-radius: 3px; transition: width 0.6s ease; }}
.sc-badge {{
    display: inline-block; padding: 3px 12px; border-radius: 100px;
    font-size: 0.6rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.04em; color: #fff; flex-shrink: 0; min-width: 55px; text-align: center;
}}

/* ============ BODY CONTENT ============ */
.body-content {{
    background: #fff; border-radius: 12px; padding: 36px;
    border: 1px solid {BORDER}; box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    line-height: 1.8; font-size: 0.9rem;
}}
.body-content h2 {{
    font-size: 1.2rem; font-weight: 700; color: {DARK};
    margin-top: 28px; margin-bottom: 10px;
}}
.body-content h3 {{
    font-size: 1rem; font-weight: 600; color: {DARK};
    margin-top: 20px; margin-bottom: 8px;
}}
.body-content p {{ margin-bottom: 12px; color: {GRAY}; }}
.body-content ul {{ margin: 8px 0 16px 24px; }}
.body-content li {{ margin-bottom: 4px; color: {GRAY}; }}
.body-content strong {{ color: {DARK}; }}
.body-content em {{ color: {GRAY}; }}

/* ============ DISCLAIMER ============ */
.disclaimer {{
    background: #fff; border-radius: 12px; padding: 28px 32px;
    border: 1px solid {BORDER}; margin-top: 40px;
    font-size: 0.78rem; color: {LIGHT_GRAY}; text-align: center; line-height: 1.7;
}}
.disclaimer strong {{ color: {DARK}; }}

/* ============ FOOTER ============ */
.footer {{
    text-align: center; padding: 24px; font-size: 0.7rem; color: {LIGHT_GRAY};
    border-top: 1px solid {BORDER}; margin-top: 32px;
}}

/* ============ PRINT ============ */
@media print {{
    body {{ background: #fff !important; font-size: 11pt; color: #000 !important; }}
    .sidebar {{ display: none !important; }}
    .main-wrap {{ margin-left: 0 !important; }}
    .cover {{ min-height: 60vh !important; padding: 40px !important; background: {DARK} !important; break-after: page; }}
    .cover::before, .cover::after {{ display: none !important; }}
    .score-card {{ break-inside: avoid; }}
    .hero-score {{ break-inside: avoid; }}
    @page {{ margin: 1.5cm; }}
}}

/* ============ RESPONSIVE ============ */
@media (max-width: 768px) {{
    .sidebar {{ display: none; }}
    .main-wrap {{ margin-left: 0; }}
    .cover {{ padding: 40px 20px; }}
    .cover h2 {{ font-size: 2rem; }}
    .main-content {{ padding: 24px 16px; }}
    .score-grid {{ grid-template-columns: 1fr; }}
    .hero-score {{ flex-direction: column; gap: 16px; text-align: center; padding: 24px; }}
    .hero-left {{ flex-direction: column; gap: 8px; }}
    .hero-verdict {{ text-align: center; }}
}}
"""


def _build_sidebar():
    return f"""
<div class="sidebar">
    <div class="sidebar-brand">
        <h3>Prisma Consulting</h3>
        <p>Klar Analytics</p>
    </div>
    <a href="#cover" class="active" onclick="document.getElementById('cover').scrollIntoView({{behavior:'smooth'}});return false">Portada</a>
    <a href="#scores" onclick="document.getElementById('scores').scrollIntoView({{behavior:'smooth'}});return false">Evaluacion de Riesgos</a>
    <a href="#detail" onclick="document.getElementById('detail').scrollIntoView({{behavior:'smooth'}});return false">Informe Detallado</a>
    <a href="#disclaimer" onclick="document.getElementById('disclaimer').scrollIntoView({{behavior:'smooth'}});return false">Descargo</a>
</div>
"""


def _build_cover(company, cuit, today):
    return f"""
<div class="cover" id="cover">
    <div class="cover-content">
        <div class="cover-badge">Confidencial &bull; Due Diligence</div>
        <h1>Prisma Consulting</h1>
        <h2>Informe de Due Diligence</h2>
        <div class="cover-line"></div>
        <div class="cover-subtitle">{company}</div>
        <div class="cover-meta">
            <p><strong>CUIT:</strong> {cuit}</p>
            <p><strong>Fecha:</strong> {today}</p>
            <p><strong>Clasificacion:</strong> USO CONFIDENCIAL</p>
        </div>
    </div>
</div>
"""


def _build_hero_score(general, rec):
    gcolor = _risk_color(general)
    glabel = _risk_label(general)
    return f"""
<div class="hero-score" style="background:{gcolor}">
    <div class="hero-left">
        <div class="hero-number">{general}</div>
        <div class="hero-label">RIESGO GLOBAL<br>{glabel.upper()}</div>
    </div>
    <div class="hero-verdict">
        {rec.upper() if rec else "SIN RECOMENDACION"}
        <small>Recomendacion</small>
    </div>
</div>
"""


def generate_dd_html(company, cuit, dd_text):
    scores = _parse_scores(dd_text)
    body = _strip_scores_section(dd_text)
    body_html = _md_to_html(body)

    today = date.today().strftime("%d/%m/%Y")
    general = scores.get("general")
    rec = scores.get("recomendacion", "")

    hero_html = _build_hero_score(general, rec) if general is not None else ""
    score_cards_html = _build_score_cards(scores)
    sidebar_html = _build_sidebar()
    cover_html = _build_cover(company, cuit, today)
    styles = _build_styles()

    no_scores_msg = ""
    if not scores:
        no_scores_msg = '<p style="text-align:center;color:{LIGHT_GRAY};padding:24px">No hay datos de scoring disponibles.</p>'

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Informe de Due Diligence - {company}</title>
<style>
{styles}
</style>
</head>
<body>

{sidebar_html}

{cover_html}

<div class="main-wrap">
<div class="main-content">

{hero_html}

<section id="scores">
    <h2 class="section-title">Evaluacion de Riesgos</h2>
    {no_scores_msg if not scores else ""}
    <div class="score-grid">
        {score_cards_html}
    </div>
</section>

<section id="detail">
    <h2 class="section-title">Informe Detallado</h2>
    <div class="body-content">
        {body_html}
    </div>
</section>

<div class="disclaimer" id="disclaimer">
    <strong>Descargo de responsabilidad</strong><br><br>
    Este informe ha sido generado por inteligencia artificial de <strong>Prisma Consulting</strong>
    a traves de <strong>Klar Analytics</strong>. El analisis se basa en las respuestas brindadas
    por el cliente y en datos obtenidos de fuentes publicas oficiales (BCRA, ARCA/AFIP via cuitcuil.com).
    Este documento no constituye un analisis profundo ni una auditoria profesional,
    sino un diagnostico preliminar orientado a simplificar la toma de decisiones.
    Se recomienda verificar los hallazgos con un profesional calificado.
</div>

<div class="footer">
    Prisma Consulting | Klar Analytics &mdash; Diagnostico con IA para PYMES<br>
    {today} &nbsp;|&nbsp; Pagina 1 de 1
</div>

</div>
</div>

<script>
(function() {{
    var links = document.querySelectorAll('.sidebar a');
    var sections = ['cover','scores','detail','disclaimer'];
    window.addEventListener('scroll', function() {{
        var scrollY = window.scrollY + 120;
        var current = 'cover';
        for (var i = 0; i < sections.length; i++) {{
            var el = document.getElementById(sections[i]);
            if (el && el.offsetTop <= scrollY) {{
                current = sections[i];
            }}
        }}
        for (var j = 0; j < links.length; j++) {{
            links[j].classList.remove('active');
            if (links[j].getAttribute('href') === '#' + current) {{
                links[j].classList.add('active');
            }}
        }}
    }});
}})();
</script>

</body>
</html>"""
