#!/usr/bin/env python3
import os
import json
from svg_utils import render_terminal_svg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "stats-mandar1045.svg")

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

    body = f"""
    <style>
      .txt {{ fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .hl {{ fill: #22d3ee; font-weight: bold; }}
      .val {{ fill: #39d353; font-weight: bold; }}
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
      <text class="txt" y="25">  • Total Contributions : <tspan class="val">{total_contribs}</tspan></text>
      <text class="txt" y="50">  • Current Streak      : <tspan class="val">{current_streak} days</tspan></text>
      <text class="txt" y="75">  • Longest Streak      : <tspan class="val">{longest_streak} days</tspan></text>
      <text class="txt" y="100">  • Most in a day       : <tspan class="val">{best_day}</tspan></text>
    </g>

    <g transform="translate(430, 70)" class="fade-in" style="animation-delay: 1.5s">
      <text class="txt hl" y="0">🔥  Top Languages (Estimated)</text>
      <text class="txt" y="25">  • Go          [████████  ] 45%</text>
      <text class="txt" y="50">  • Python      [██████    ] 30%</text>
      <text class="txt" y="75">  • TypeScript  [████      ] 20%</text>
      <text class="txt" y="100">  • Other       [█         ] 5%</text>
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
