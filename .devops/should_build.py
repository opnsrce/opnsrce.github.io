#!/usr/bin/env python3
"""
Prints 'true' if any content's effective publish time (publishDate or date)
is <= now (UTC). Otherwise prints 'false'.
"""
import json, re, sys
from pathlib import Path
from datetime import datetime, timezone

# Read Hugo timezone; default to UTC (your config uses UTC).
try:
    cfg = json.loads(Path("hugo.json").read_text(encoding="utf-8"))
    tzname = cfg.get("timeZone", "UTC")
except Exception:
    tzname = "UTC"

site_tz = timezone.utc  # only UTC supported here
now = datetime.now(timezone.utc)

fm_delim = re.compile(r'^(\-\-\-|\+\+\+)\s*$')  # YAML or TOML fences

# This regex is used in `effective_publish_dt()` to extract the publish date
# from the first front-matter block of each content file.
# It ensures we only match valid ISO date or datetime formats, optionally
# quoted, and only when the key is exactly `date` or `publishDate`.
#
# Matches front matter lines starting with either `date:` or `publishDate:`,
# followed by optional spaces, an optional single or double quote, then a date
# in one of these formats:
#
#   YYYY-MM-DD
#   YYYY-MM-DDThh:mm
#   YYYY-MM-DDThh:mm:ss
#   YYYY-MM-DDThh:mmZ
#   YYYY-MM-DDThh:mm:ssZ
#   YYYY-MM-DDThh:mm+HH:MM
#   YYYY-MM-DDThh:mm:ss+HH:MM
#
# Notes:
# - `^(date|publishDate):`    → must start with exactly `date:` or `publishDate:`
# - `\s*["']?`                → allow spaces and an optional opening quote
# - `[0-9]{4}-[0-9]{2}-[0-9]{2}` → the YYYY-MM-DD part
# - `(?:T...)?`               → optional time component:
#       - `[Tt][0-9]{2}:[0-9]{2}` → hour:minute (case-insensitive `T`)
#       - `(?::[0-9]{2})?`        → optional :seconds
#       - `(?:Z|[+\-][0-9]{2}:[0-9]{2})?` → optional UTC `Z` or offset ±HH:MM
# - `)?`                       → entire time part optional (so date-only is fine)
# - `\s*["']?$`                → optional closing quote and optional trailing spaces
kv_line = re.compile(
    r'^(date|publishDate):\s*["\']?('
    r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    r'(?:[Tt][0-9]{2}:[0-9]{2}(?::[0-9]{2})?'
    r'(?:Z|[+\-][0-9]{2}:[0-9]{2})?)?'
    r')\s*["\']?\s*$'
)

def parse_when(s: str):
    s = s.strip()
    if 'T' not in s and 't' not in s:
        dt = datetime.fromisoformat(s + "T00:00:00").replace(tzinfo=site_tz)
        return dt.astimezone(timezone.utc)
    if s.endswith('Z'):
        s = s[:-1] + '+00:00'
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=site_tz)
    return dt.astimezone(timezone.utc)

def effective_publish_dt(path: Path):
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            first = f.readline()
            if not fm_delim.match(first):
                return None
            publish = date = None
            for line in f:
                if fm_delim.match(line):
                    break
                m = kv_line.match(line)
                if not m:
                    continue
                key, val = m.group(1), m.group(2)
                if key == 'publishDate':
                    publish = val
                elif key == 'date':
                    date = val
            use = publish or date
            return parse_when(use) if use else None
    except Exception:
        return None

content = Path("content")
if content.exists():
    for p in content.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in (".md", ".markdown", ".mdx", ".mmark"):
            continue
        dt = effective_publish_dt(p)
        if dt and dt <= now:
            print("true")
            sys.exit(0)

print("false")
