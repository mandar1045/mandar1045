#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "opensource-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .hl { fill: #22d3ee; font-weight: bold; }
      .success { fill: #39d353; font-weight: bold; }
      .warn { fill: #f2cc60; font-weight: bold; }
      .cursor {
        fill: #c9d1d9;
        animation: blink 1s step-end infinite;
      }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.3s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
      
      .type-line {
        overflow: hidden;
        white-space: nowrap;
        animation: typing 0.5s steps(40, end) forwards;
        width: 0;
      }
      @keyframes typing { from { width: 0 } to { width: 100% } }
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./opensource.sh</text>
    
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.5s">
      <text class="txt hl" y="0">[*] Fetching Open Source Contributions...</text>
    </g>

    <g transform="translate(0, 60)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt" y="0">╭── <tspan class="hl">Linux Foundation — FOSSology</tspan></text>
      <text class="txt" y="20">│   <tspan class="success">✓ 8 Merged PRs</tspan></text>
      <text class="txt" y="40">│   <tspan fill="#8b949e">Core scanning pipelines, API correctness, import reliability</tspan></text>
      <text class="txt" y="60">╰─────────────────────────────────────────────────────────────</text>
    </g>

    <g transform="translate(0, 140)" class="fade-in" style="animation-delay: 1.5s">
      <text class="txt" y="0">╭── <tspan class="hl">CNCF — Kubernetes</tspan></text>
      <text class="txt" y="20">│   <tspan class="warn">⟳ Active Contributor</tspan></text>
      <text class="txt" y="40">│   <tspan fill="#8b949e">Upstream PRs &amp; improvements to container orchestration core</tspan></text>
      <text class="txt" y="60">╰─────────────────────────────────────────────────────────────</text>
    </g>

    <g transform="translate(430, 60)" class="fade-in" style="animation-delay: 2.0s">
      <text class="txt" y="0">╭── <tspan class="hl">Supabase &amp; Cal.com</tspan></text>
      <text class="txt" y="20">│   <tspan class="success">✓ Merged PRs</tspan></text>
      <text class="txt" y="40">│   <tspan fill="#8b949e">Supabase Studio logic, Cal.com scheduling availability</tspan></text>
      <text class="txt" y="60">╰─────────────────────────────────────────────────────────────</text>
    </g>

    <g transform="translate(430, 140)" class="fade-in" style="animation-delay: 2.5s">
      <text class="txt" y="0">╭── <tspan class="hl">PostHog</tspan></text>
      <text class="txt" y="20">│   <tspan class="success">✓ Merged &amp; Active PRs</tspan></text>
      <text class="txt" y="40">│   <tspan fill="#8b949e">Analytics pipeline resilience, frontend error handling</tspan></text>
      <text class="txt" y="60">╰─────────────────────────────────────────────────────────────</text>
    </g>

    <g transform="translate(0, 240)" class="fade-in" style="animation-delay: 3.0s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/opensource",
        body_content=body,
        width=860,
        height=360
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
