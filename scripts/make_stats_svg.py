#!/usr/bin/env python3
import os
import json
import requests
from svg_utils import render_terminal_svg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "stats-mandar1045.svg")

USER = "mandar1045"
HIDDEN_LANGS = {"HTML"}
PINNED_LANG = "Elixir"  # always shown, even if outside the top languages
FALLBACK_LANGS = [("TypeScript", 52), ("Python", 21), ("Java", 8), ("Elixir", 5), ("Other", 14)]

def fetch_languages(top_n=3):
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}
    headers["User-Agent"] = "profile-readme-bot/1.0"

    # Sum language bytes across own (non-fork) repos
    totals = {}
    try:
        resp = requests.get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner", headers=headers, timeout=10)
        resp.raise_for_status()
        for repo in resp.json():
            if repo.get("fork"):
                continue
            r = requests.get(repo["languages_url"], headers=headers, timeout=10)
            r.raise_for_status()
            for lang, size in r.json().items():
                if lang not in HIDDEN_LANGS:
                    totals[lang] = totals.get(lang, 0) + size
    except Exception as e:
        print(f"Error fetching languages: {e}")
        return FALLBACK_LANGS
    if not totals:
        return FALLBACK_LANGS

    total = sum(totals.values())
    shown = sorted(totals, key=totals.get, reverse=True)[:top_n]
    if PINNED_LANG in totals and PINNED_LANG not in shown:
        shown.append(PINNED_LANG)
    rows = [(lang, round(100 * totals[lang] / total)) for lang in shown]
    other = 100 - sum(pct for _, pct in rows)
    if other > 0:
        rows.append(("Other", other))
    return rows

def generate():
    total_contribs = 0
    current_streak = 0
    longest_streak = 0
    best_day = 0
    
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, "r") as f:
                data = json.load(f)
                total_contribs = data.get("total_contributions", 0)
                current_streak = data.get("current_streak", {}).get("length", 0)
                longest_streak = data.get("longest_streak", {}).get("length", 0)
                best_day = data.get("best_day", {}).get("count", 0)
        except Exception as e:
            print(f"Error reading {DATA_PATH}: {e}")

    lang_lines = ""
    for i, (lang, pct) in enumerate(fetch_languages()):
        filled = max(1, int(pct / 10 + 0.5))
        bar = "█" * filled + "░" * (10 - filled)
        cls = "txt pin" if lang == PINNED_LANG else "txt"
        lang_lines += f'\n      <text class="{cls}" y="{25 * (i + 1)}" xml:space="preserve">  • {lang:<11} [{bar}] {pct}%</text>'

    body = f"""
    <style>
      .txt {{ fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .hl {{ fill: #22d3ee; font-weight: bold; }}
      .val {{ fill: #39d353; font-weight: bold; }}
      .pin {{ fill: #d2a8ff; font-weight: bold; }}
      .cursor {{
        fill: #c9d1d9;
        animation: blink 1s step-end infinite;
      }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
      .fade-in {{ opacity: 0; animation: fadeIn 0.3s forwards; }}
      @keyframes fadeIn {{ to {{ opacity: 1; }} }}
      
      .type-line {{
        overflow: hidden;
        white-space: nowrap;
        animation: typing 0.5s steps(40, end) forwards;
        width: 0;
      }}
      @keyframes typing {{ from {{ width: 0 }} to {{ width: 100% }} }}
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./stats.sh</text>
    
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.5s">
      <text class="txt" y="0">Analyzing local contribution metrics...</text>
    </g>

    <g transform="translate(0, 70)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt hl" y="0">🏆  Contribution Stats (Last Year)</text>
      <text class="txt" y="25" xml:space="preserve">  • Total Contributions : <tspan class="val">{total_contribs}</tspan></text>
      <text class="txt" y="50" xml:space="preserve">  • Current Streak      : <tspan class="val">{current_streak} days</tspan></text>
      <text class="txt" y="75" xml:space="preserve">  • Longest Streak      : <tspan class="val">{longest_streak} days</tspan></text>
      <text class="txt" y="100" xml:space="preserve">  • Most in a day       : <tspan class="val">{best_day}</tspan></text>
    </g>

    <g transform="translate(430, 70)" class="fade-in" style="animation-delay: 1.5s">
      <text class="txt hl" y="0">🔥  Top Languages</text>{lang_lines}
    </g>

    <g transform="translate(0, 220)" class="fade-in" style="animation-delay: 2.0s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/stats",
        body_content=body,
        width=860,
        height=330
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
