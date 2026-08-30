#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "projects-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .hl { fill: #22d3ee; font-weight: bold; }
      .link { fill: #39d353; text-decoration: underline; }
      .dim { fill: #8b949e; }
      .cursor {
        fill: #c9d1d9;
        animation: blink 1s step-end infinite;
      }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.3s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~/projects</tspan>$ ls -la</text>
    
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.5s">
      <text class="txt dim" y="0">total 3</text>
    </g>

    <g transform="translate(0, 60)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt" y="0">drwxr-xr-x  mandar1045  <tspan class="hl">Resync</tspan>                 <tspan class="link">https://resync.biz</tspan></text>
      <text class="txt dim" y="20">  ↳ UPI Autopay Recovery Platform (Go, gRPC, Redpanda, Redis)</text>
      <text class="txt dim" y="40">  ↳ 9 Microservices | Smart Dunning Classifier | Distributed Locks</text>
    </g>

    <g transform="translate(0, 100)" class="fade-in" style="animation-delay: 1.5s">
      <text class="txt" y="0">drwxr-xr-x  mandar1045  <tspan class="hl">Continum</tspan>               <tspan class="link">https://continum.online</tspan></text>
      <text class="txt dim" y="20">  ↳ AI/ML Automation Platform</text>
      <text class="txt dim" y="40">  ↳ NLP Email Triage Engine | High Availability Microservices</text>
    </g>

    <g transform="translate(0, 160)" class="fade-in" style="animation-delay: 2.0s">
      <text class="txt" y="0">drwxr-xr-x  mandar1045  <tspan class="hl">Crowd-Management-System</tspan></text>
      <text class="txt dim" y="20">  ↳ Real-Time CV Pipeline (YOLO @ 24 FPS)</text>
      <text class="txt dim" y="40">  ↳ Stampede Risk Prediction with flow velocity &lt;1.5s alerts</text>
    </g>

    <g transform="translate(0, 240)" class="fade-in" style="animation-delay: 2.5s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/projects",
        body_content=body,
        width=860,
        height=360
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
