#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "projects-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .hl { fill: #22d3ee; font-weight: bold; font-size: 16px;}
      .dim { fill: #8b949e; font-size: 13px;}
      .cursor { fill: #c9d1d9; animation: blink 1s step-end infinite; }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.5s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
      .card { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~/projects</tspan>$ ls -la</text>

    <!-- Resync Card -->
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.2s">
      <rect class="card" width="380" height="110" />
      <text class="hl" x="20" y="30">💳 Resync</text>
      <text class="dim" x="20" y="55">UPI Autopay Recovery Platform</text>
      <text class="txt" x="20" y="75" font-size="12px">• Go / gRPC Microservices</text>
      <text class="txt" x="20" y="95" font-size="12px">• Distributed Locks &amp; Kafka</text>
    </g>

    <!-- Continum Card -->
    <g transform="translate(420, 30)" class="fade-in" style="animation-delay: 0.4s">
      <rect class="card" width="380" height="110" />
      <text class="hl" x="20" y="30">🤖 Continum</text>
      <text class="dim" x="20" y="55">AI/ML Automation Platform</text>
      <text class="txt" x="20" y="75" font-size="12px">• NLP Email Triage Engine</text>
      <text class="txt" x="20" y="95" font-size="12px">• High Availability Microservices</text>
    </g>

    <!-- Crowd Management Card -->
    <g transform="translate(0, 160)" class="fade-in" style="animation-delay: 0.6s">
      <rect class="card" width="380" height="110" />
      <text class="hl" x="20" y="30">👁️ Crowd Management</text>
      <text class="dim" x="20" y="55">Real-Time CV Pipeline (YOLO)</text>
      <text class="txt" x="20" y="75" font-size="12px">• Processes 4 streams @ 24 FPS</text>
      <text class="txt" x="20" y="95" font-size="12px">• Stampede Risk Prediction &lt;1.5s</text>
    </g>

    <g transform="translate(0, 320)" class="fade-in" style="animation-delay: 0.8s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/projects",
        body_content=body,
        width=860,
        height=420
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
