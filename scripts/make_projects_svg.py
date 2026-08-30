#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

def write_project_svg(name, title_text, hl, dim, t1, t2, filename, delay="0.2s"):
    body = f"""
    <style>
      .txt {{ fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .hl {{ fill: #22d3ee; font-weight: bold; font-size: 16px;}}
      .dim {{ fill: #8b949e; font-size: 13px;}}
      .fade-in {{ opacity: 0; animation: fadeIn 0.5s forwards; }}
      @keyframes fadeIn {{ to {{ opacity: 1; }} }}
      .card {{ fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045</tspan>:<tspan fill="#79c0ff">~/projects</tspan>$ cat {name}.md</text>

    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: {delay}">
      <rect class="card" width="380" height="90" />
      <text class="hl" x="20" y="30">{hl}</text>
      <text class="dim" x="20" y="55">{dim}</text>
      <text class="txt" x="20" y="75" font-size="12px">{t1}</text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text=title_text,
        body_content=body,
        width=420,
        height=200
    )
    
    out_path = os.path.join(os.path.dirname(__file__), "..", filename)
    with open(out_path, "w") as f:
        f.write(svg)
    print(f"wrote {out_path}")

def generate():
    write_project_svg(
        name="resync",
        title_text="~/projects/resync",
        hl="💳 Resync",
        dim="UPI Autopay Recovery Platform",
        t1="• Go / Kafka / Microservices",
        t2="",
        filename="project-resync.svg",
        delay="0.1s"
    )
    
    write_project_svg(
        name="continum",
        title_text="~/projects/continum",
        hl="🤖 Continum",
        dim="AI/ML Automation Platform",
        t1="• NLP Email Triage Engine",
        t2="",
        filename="project-continum.svg",
        delay="0.2s"
    )

    write_project_svg(
        name="crowd",
        title_text="~/projects/crowd",
        hl="👁️ Crowd Management",
        dim="Real-Time CV Pipeline (YOLO)",
        t1="• Processes 4 streams @ 24 FPS",
        t2="",
        filename="project-crowd.svg",
        delay="0.3s"
    )

if __name__ == "__main__":
    generate()
