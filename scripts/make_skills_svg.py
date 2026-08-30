#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "skills-mandar1045.svg")

def generate():
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 14px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .cat { fill: #22d3ee; font-weight: bold; font-size: 15px; }
      .cursor {
        fill: #c9d1d9;
        animation: blink 1s step-end infinite;
      }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.5s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
      .bar-bg { fill: #21262d; rx: 5px; }
      .bar-fg { rx: 5px; }
    </style>
    
    <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./skills.sh</text>
    
    <!-- Languages Column -->
    <g transform="translate(0, 40)" class="fade-in" style="animation-delay: 0.2s">
      <text class="cat" y="0">Languages</text>
      
      <text class="txt" y="35">Go</text>
      <rect class="bar-bg" x="110" y="24" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="24" width="0" height="12" fill="#00add8">
        <animate attributeName="width" from="0" to="225" dur="1s" fill="freeze" />
      </rect>
      
      <text class="txt" y="65">Python</text>
      <rect class="bar-bg" x="110" y="54" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="54" width="0" height="12" fill="#3776ab">
        <animate attributeName="width" from="0" to="210" dur="1s" fill="freeze" />
      </rect>

      <text class="txt" y="95">TypeScript</text>
      <rect class="bar-bg" x="110" y="84" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="84" width="0" height="12" fill="#3178c6">
        <animate attributeName="width" from="0" to="200" dur="1s" fill="freeze" />
      </rect>

      <text class="txt" y="125">Java / C</text>
      <rect class="bar-bg" x="110" y="114" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="114" width="0" height="12" fill="#ed8b00">
        <animate attributeName="width" from="0" to="175" dur="1s" fill="freeze" />
      </rect>
    </g>

    <!-- Backend Column -->
    <g transform="translate(420, 40)" class="fade-in" style="animation-delay: 0.4s">
      <text class="cat" y="0">Backend &amp; Microservices</text>
      
      <text class="txt" y="35">gRPC / PB</text>
      <rect class="bar-bg" x="120" y="24" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="24" width="0" height="12" fill="#244c5a">
        <animate attributeName="width" from="0" to="220" dur="1s" fill="freeze" />
      </rect>

      <text class="txt" y="65">FastAPI</text>
      <rect class="bar-bg" x="120" y="54" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="54" width="0" height="12" fill="#009688">
        <animate attributeName="width" from="0" to="210" dur="1s" fill="freeze" />
      </rect>
      
      <text class="txt" y="95">Node.js</text>
      <rect class="bar-bg" x="120" y="84" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="84" width="0" height="12" fill="#339933">
        <animate attributeName="width" from="0" to="200" dur="1s" fill="freeze" />
      </rect>
    </g>

    <!-- Streaming Column -->
    <g transform="translate(0, 200)" class="fade-in" style="animation-delay: 0.6s">
      <text class="cat" y="0">Streaming &amp; Databases</text>
      
      <text class="txt" y="35">Kafka / Redis</text>
      <rect class="bar-bg" x="110" y="24" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="24" width="0" height="12" fill="#dc382d">
        <animate attributeName="width" from="0" to="230" dur="1s" fill="freeze" />
      </rect>

      <text class="txt" y="65">PostgreSQL</text>
      <rect class="bar-bg" x="110" y="54" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="54" width="0" height="12" fill="#4169e1">
        <animate attributeName="width" from="0" to="215" dur="1s" fill="freeze" />
      </rect>
      
      <text class="txt" y="95">Supabase</text>
      <rect class="bar-bg" x="110" y="84" width="250" height="12"/>
      <rect class="bar-fg" x="110" y="84" width="0" height="12" fill="#3ecf8e">
        <animate attributeName="width" from="0" to="200" dur="1s" fill="freeze" />
      </rect>
    </g>

    <!-- Cloud Column -->
    <g transform="translate(420, 200)" class="fade-in" style="animation-delay: 0.8s">
      <text class="cat" y="0">Cloud Native &amp; DevOps</text>
      
      <text class="txt" y="35">Docker</text>
      <rect class="bar-bg" x="120" y="24" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="24" width="0" height="12" fill="#2496ed">
        <animate attributeName="width" from="0" to="225" dur="1s" fill="freeze" />
      </rect>

      <text class="txt" y="65">Kubernetes</text>
      <rect class="bar-bg" x="120" y="54" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="54" width="0" height="12" fill="#326ce5">
        <animate attributeName="width" from="0" to="200" dur="1s" fill="freeze" />
      </rect>
      
      <text class="txt" y="95">AWS / TF</text>
      <rect class="bar-bg" x="120" y="84" width="250" height="12"/>
      <rect class="bar-fg" x="120" y="84" width="0" height="12" fill="#f46800">
        <animate attributeName="width" from="0" to="190" dur="1s" fill="freeze" />
      </rect>
    </g>

    <g transform="translate(0, 340)" class="fade-in" style="animation-delay: 1.0s">
      <text class="txt" y="0"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/skills",
        body_content=body,
        width=860,
        height=450
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
