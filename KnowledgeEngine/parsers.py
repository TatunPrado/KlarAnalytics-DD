"""
Parsers for Prisma Consulting knowledge documents.

Each parser takes raw Markdown text and returns a structured dict
with metadata, sections, and typed content extracted from the file.
All parsers follow the same signature: parse(text: str, filepath: str) -> dict
"""

import os
import re
from typing import List, Dict, Optional


def _extract_yaml_frontmatter(text: str) -> Dict[str, str]:
    """Extract key-value pairs from YAML frontmatter (between --- markers)."""
    meta = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        lines = m.group(1).split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                i += 1
                continue
            if ':' in stripped:
                key, _, val = stripped.partition(':')
                key = key.strip().lower()
                val = val.strip()
                if val in ('>', '>-'):
                    # Folded block scalar: collect following indented lines
                    folded_lines = []
                    i += 1
                    while i < len(lines) and lines[i].startswith((' ', '\t')):
                        folded_lines.append(lines[i].strip())
                        i += 1
                    val = ' '.join(folded_lines)
                    meta[key] = val
                    continue  # i already advanced past collected lines
                elif val in ('|', '|-'):
                    # Literal block scalar: collect following indented lines
                    lit_lines = []
                    i += 1
                    while i < len(lines) and lines[i].startswith((' ', '\t')):
                        lit_lines.append(lines[i].strip())
                        i += 1
                    val = '\n'.join(lit_lines)
                    meta[key] = val
                    continue
                else:
                    val = val.strip('"\'')
                    meta[key] = val
            i += 1
    return meta


# ─── Shared utilities ───

def _extract_h1(text: str) -> Optional[str]:
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    return m.group(1).strip() if m else None


def _extract_h2_sections(text: str) -> Dict[str, str]:
    sections = {}
    pattern = r'^##\s+(.+?)$'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[heading] = body
    return sections


def _extract_h3_sections(text: str) -> Dict[str, str]:
    sections = {}
    pattern = r'^###\s+(.+?)$'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[heading] = body
    return sections


def _extract_bullets(text: str) -> List[str]:
    return [i.strip() for i in re.findall(r'^[*-]\s+(.+)$', text, re.MULTILINE)]


def _extract_ordered_items(text: str) -> List[str]:
    return [i.strip() for i in re.findall(r'^\d+[.)]\s+(.+)$', text, re.MULTILINE)]


def _extract_bold_key_values(text: str) -> Dict[str, str]:
    pairs = {}
    for m in re.finditer(r'\*\*(.+?)\*\*:\s*(.*)', text):
        pairs[m.group(1).strip()] = m.group(2).strip()
    return pairs


def _extract_tables(text: str) -> List[Dict]:
    table_pattern = r'^\|(.+)\|\n\|[-| ]+\|\n((?:\|.+\|\n?)*)'
    tables = []
    for m in re.finditer(table_pattern, text, re.MULTILINE):
        headers = [h.strip() for h in m.group(1).split('|') if h.strip()]
        rows = []
        for line in m.group(2).strip().split('\n'):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if cells:
                rows.append(cells)
        if headers:
            tables.append({'headers': headers, 'rows': rows})
    return tables


def _extract_blockquote_meta(text: str) -> Dict[str, str]:
    meta = {}
    for m in re.finditer(r'>\s+\*\*(.+?)\*\*:?\s*(.*)', text):
        meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def _extract_checklist(text: str) -> List[Dict]:
    items = []
    for m in re.finditer(r'^[-*]\s+\[([ xX])\]\s+(.+)$', text, re.MULTILINE):
        items.append({
            'checked': m.group(1).lower() == 'x',
            'text': m.group(2).strip()
        })
    return items


def _extract_tags(text: str) -> List[str]:
    tags = re.findall(r'#(\w+)', text)
    tags += re.findall(r'\[([^\]]+)\]', text)
    return list(set(tags))


def _count_tokens(text: str) -> int:
    return len(text) // 4


# ─── Parser: Agent ───

def parse_agent(text: str, filepath: str) -> Dict:
    h1 = _extract_h1(text)
    description = ""
    if h1:
        # Capture everything between the h1 line and the first h2 as description
        h1_pattern = r'^#\s+.+$'
        h1_match = re.search(h1_pattern, text, re.MULTILINE)
        h2_match = re.search(r'^##\s+', text, re.MULTILINE)
        if h1_match:
            start = h1_match.end()
            end = h2_match.start() if h2_match else len(text)
            description = text[start:end].strip()

    result = {
        "type": "agent",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": h1 or os.path.basename(filepath),
        "description": description,
        "sections": {},
        "frameworks": [],
        "skills": [],
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        section_data = {
            "body": body,
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
        }

        if "framework" in heading.lower():
            fw_from_bullets = _extract_bullets(body)
            fw_from_regex = [f"Framework_{m}" for m in re.findall(r'Framework_(\w+)', body)]
            # Normalize: strip "Framework_" prefix from all, use canonical dash-case
            all_fw = set()
            for fw in fw_from_bullets + fw_from_regex:
                clean = fw.replace("Framework_", "").replace("_", "-").replace(" ", "-").lower()
                all_fw.add(clean)
            existing_fw = set(result.get("frameworks", []))
            result["frameworks"] = sorted(existing_fw | all_fw)

        if "skill" in heading.lower():
            sk_from_bullets = _extract_bullets(body)
            sk_from_regex = re.findall(r'(\w+_Assessment)', body)
            all_sk = set()
            for sk in sk_from_bullets + sk_from_regex:
                clean = sk.replace("_", "-").replace(" ", "-").replace("assessment", "Assessment")
                clean = clean.lower()
                all_sk.add(clean)
            existing_sk = set(result.get("skills", []))
            result["skills"] = sorted(existing_sk | all_sk)

        if heading.lower() in ("rol", "objetivo", "responsabilidades"):
            section_data["key_values"] = _extract_bold_key_values(body)

        result["sections"][heading] = section_data

    return result


# ─── Parser: Skill ───

def parse_skill(text: str, filepath: str) -> Dict:
    yaml_meta = _extract_yaml_frontmatter(text)
    result = {
        "type": "skill",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or yaml_meta.get("name", "") or os.path.basename(filepath),
        "description": yaml_meta.get("description", ""),
        "sections": {},
        "framework_refs": re.findall(r'Framework_(\w+)', text),
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        section_data = {
            "body": body,
            "ordered_items": _extract_ordered_items(body),
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
        }
        result["sections"][heading] = section_data

    return result


# ─── Parser: Knowledge Framework ───

def parse_framework(text: str, filepath: str) -> Dict:
    result = {
        "type": "framework",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "sections": {},
        "subsections": {},
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        section_data = {
            "body": body,
            "bullets": _extract_bullets(body),
            "tables": _extract_tables(body),
            "h3_sections": h3_sections,
        }
        result["sections"][heading] = section_data
        result["subsections"].update({f"{heading} > {k}": v for k, v in h3_sections.items()})

    return result


# ─── Parser: CORE Pattern ───

def parse_pattern(text: str, filepath: str) -> Dict:
    result = {
        "type": "pattern",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "categories": {},
        "patterns": [],
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for category, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        patterns_in_category = []

        for pattern_id, pattern_body in h3_sections.items():
            key_values = _extract_bold_key_values(pattern_body)
            pattern_entry = {
                "pattern_id": pattern_id,
                "category": category,
                "fields": key_values,
                "raw": pattern_body,
            }
            patterns_in_category.append(pattern_entry)

        result["categories"][category] = {
            "body": body,
            "pattern_count": len(patterns_in_category),
            "patterns": patterns_in_category,
        }
        result["patterns"].extend(patterns_in_category)

    return result


# ─── Parser: Playbook ───

def parse_playbook(text: str, filepath: str) -> Dict:
    result = {
        "type": "playbook",
        "filepath": filepath,
        "filename": os.path.splitext(os.path.basename(filepath))[0],
        "title": _extract_h1(text) or os.path.basename(filepath),
        "metadata": _extract_blockquote_meta(text),
        "sections": {},
        "tables": _extract_tables(text),
        "checklists": _extract_checklist(text),
        "tags": _extract_tags(text),
        "tokens": _count_tokens(text),
    }

    sections = _extract_h2_sections(text)

    for heading, body in sections.items():
        h3_sections = _extract_h3_sections(body)
        section_data = {
            "body": body,
            "h3_sections": h3_sections,
            "bullets": _extract_bullets(body),
            "ordered_items": _extract_ordered_items(body),
            "tables": _extract_tables(body),
            "checklists": _extract_checklist(body),
        }
        result["sections"][heading] = section_data

    return result


# ─── Parser: Operations Process ───

def parse_process(text: str, filepath: str) -> Dict:
    return parse_playbook(text, filepath)


# ─── Parser registry ───

def detect_type(filepath: str) -> str:
    path = filepath.replace("\\", "/")
    if "/Agents/" in path:
        return "agent"
    if "/Skills/" in path:
        return "skill"
    if "/Knowledge/" in path:
        if "_Patterns." in path or "/CORE/" in path:
            return "pattern"
        if "Framework_" in path:
            return "framework"
        return "knowledge"
    if "/Playbooks/" in path:
        return "playbook"
    if "/Operations/" in path:
        return "process"
    return "unknown"


PARSER_REGISTRY = {
    "agent": parse_agent,
    "skill": parse_skill,
    "framework": parse_framework,
    "pattern": parse_pattern,
    "playbook": parse_playbook,
    "process": parse_process,
}


def parse_file(text: str, filepath: str) -> Dict:
    doc_type = detect_type(filepath)
    parser = PARSER_REGISTRY.get(doc_type)
    if parser:
        result = parser(text, filepath)
        result["doc_type"] = doc_type
        return result
    return {
        "type": "unknown",
        "filepath": filepath,
        "title": _extract_h1(text) or os.path.basename(filepath),
        "body": text[:200],
        "tokens": _count_tokens(text),
    }
