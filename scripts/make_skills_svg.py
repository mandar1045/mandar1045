#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "skills-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .cat { fill: #22d3ee; font-weight: bold; }
      .bar-bg { fill: #30363d; rx: 4px; }
      .bar-fg-go { fill: #00add8; rx: 4px; }
      .bar-fg-py { fill: #3776ab; rx: 4px; }
      .bar-fg-ts { fill: #3178c6; rx: 4px; }
      
      .cursor {
        fill: #c9d1d9;
        animation: blink 1s step-end infinite;
      }
      @keyframes blink { 50% { opacity: 0; } }
      
      .fade-in {
        opacity: 0;
        animation: fadeIn 0.3s forwards;
      }
      @keyframes fadeIn { to { opacity: 1; } }
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./skills.sh</text>
    
    <g transform="translate(0, 30)" class="fade-in" style="animation-delay: 0.5s">
      <text class="txt cat" y="0">Languages</text>
      <text class="txt" y="25" x="20">Go         [||||||||||||||||||] 90%</text>
      <text class="txt" y="45" x="20">Python     [||||||||||||||||| ] 85%</text>
      <text class="txt" y="65" x="20">TypeScript [||||||||||||||||  ] 80%</text>
      <text class="txt" y="85" x="20">Java/C     [||||||||||||||    ] 70%</text>
    </g>

    <g transform="translate(350, 30)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt cat" y="0">Backend &amp; Microservices</text>
      <text class="txt" y="25" x="20">• gRPC / Protobuf</text>
      <text class="txt" y="45" x="20">• FastAPI / Node.js</text>
      <text class="txt" y="65" x="20">• Redis / Distributed Locks</text>
    </g>

    <g transform="translate(0, 150)" class="fade-in" style="animation-delay: 1.5s">
      <text class="txt cat" y="0">Streaming &amp; Databases</text>
      <text class="txt" y="25" x="20">• Apache Kafka (Redpanda)</text>
      <text class="txt" y="45" x="20">• PostgreSQL / MongoDB</text>
      <text class="txt" y="65" x="20">• Supabase</text>
    </g>

    <g transform="translate(350, 150)" class="fade-in" style="animation-delay: 2.0s">
      <text class="txt cat" y="0">Cloud Native &amp; DevOps</text>
      <text class="txt" y="25" x="20">• Docker / Kubernetes</text>
      <text class="txt" y="45" x="20">• Terraform / AWS</text>
      <text class="txt" y="65" x="20">• Prometheus / Grafana</text>
    </g>

    <g transform="translate(0, 250)" class="fade-in" style="animation-delay: 2.5s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/skills",
        body_content=body,
        width=860,
        height=380
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
