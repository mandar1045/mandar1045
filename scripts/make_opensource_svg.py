#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "opensource-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 13px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .hl { fill: #22d3ee; font-weight: bold; font-size: 15px;}
      .success { fill: #39d353; font-weight: bold; font-size: 13px;}
      .warn { fill: #f2cc60; font-weight: bold; font-size: 13px;}
      .dim { fill: #8b949e; font-size: 12px; }
      .cursor { fill: #c9d1d9; animation: blink 1s step-end infinite; }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.5s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
      .card { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
    </style>
    
    <text class="txt" y="0" font-size="14px"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./opensource.sh</text>

    <!-- FOSSology Card -->
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.2s">
      <rect class="card" width="380" height="90" />
      <text class="hl" x="20" y="30">🐧 Linux Foundation — FOSSology</text>
      <text class="success" x="20" y="55">✓ 8 Merged PRs</text>
      <text class="dim" x="20" y="75">Core scanning pipelines &amp; API reliability</text>
    </g>

    <!-- Supabase Card -->
    <g transform="translate(420, 30)" class="fade-in" style="animation-delay: 0.4s">
      <rect class="card" width="380" height="90" />
      <text class="hl" x="20" y="30">⚡ Supabase &amp; Cal.com</text>
      <text class="success" x="20" y="55">✓ Merged PRs</text>
      <text class="dim" x="20" y="75">Studio logic, scheduling availability logic</text>
    </g>

    <!-- Kubernetes Card -->
    <g transform="translate(0, 140)" class="fade-in" style="animation-delay: 0.6s">
      <rect class="card" width="380" height="90" />
      <text class="hl" x="20" y="30">⚙️ CNCF — Kubernetes</text>
      <text class="warn" x="20" y="55">⟳ Active Contributor</text>
      <text class="dim" x="20" y="75">Upstream PRs &amp; container orchestration core</text>
    </g>

    <!-- PostHog Card -->
    <g transform="translate(420, 140)" class="fade-in" style="animation-delay: 0.8s">
      <rect class="card" width="380" height="90" />
      <text class="hl" x="20" y="30">📊 PostHog</text>
      <text class="success" x="20" y="55">✓ Merged &amp; Active PRs</text>
      <text class="dim" x="20" y="75">Analytics pipeline resilience, error handling</text>
    </g>

    <g transform="translate(0, 270)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt" y="0" font-size="14px"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/opensource",
        body_content=body,
        width=860,
        height=370
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
