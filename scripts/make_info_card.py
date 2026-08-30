#!/usr/bin/env python3
"""
Generate a neofetch-style info card SVG.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")

def generate():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="387" viewBox="0 0 490 387" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="wbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="490" height="387" rx="12" fill="url(#wbg)"/>
  <rect x="0.5" y="0.5" width="489" height="386" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>
  <line x1="0" y1="28" x2="490" y2="28" stroke="#30363d"/>
  <circle cx="18" cy="14" r="4.5" fill="#ff5f56"/>
  <circle cx="33" cy="14" r="4.5" fill="#ffbd2e"/>
  <circle cx="48" cy="14" r="4.5" fill="#27c93f"/>
  <text x="245" y="18" fill="#7d8590" font-size="11.5" text-anchor="middle">mandar1045@github: ~$ neofetch</text>
  
  <g fill="#c9d1d9" font-size="13" transform="translate(30, 60)">
    <text y="0" font-weight="bold" fill="#22d3ee" font-size="16">Mandar Joshi</text>
    <text y="20" fill="#7d8590">---------------------</text>
    <text y="50"><tspan fill="#39d353" font-weight="bold">Role</tspan>       Software Engineer / Student</text>
    <text y="80"><tspan fill="#39d353" font-weight="bold">College</tspan>    VIT Vellore (IT)</text>
    <text y="110"><tspan fill="#39d353" font-weight="bold">Focus</tspan>      Distributed Systems, Microservices</text>
    <text y="140"><tspan fill="#39d353" font-weight="bold">Stack</tspan>      Go, Python, TypeScript</text>
    
    <text y="170" fill="#7d8590">---------------------</text>
    
    <text y="200"><tspan fill="#f2cc60" font-weight="bold">Open Source</tspan></text>
    <text y="220">  • Linux Foundation — FOSSology (8+ PRs)</text>
    <text y="240">  • Supabase &amp; Cal.com Contributor</text>
    <text y="260">  • Kubernetes CNCF Active Contributor</text>

    <text y="290"><tspan fill="#f2cc60" font-weight="bold">Projects</tspan></text>
    <text y="310">  • Resync: UPI Autopay Recovery Platform</text>
    <text y="330">  • Continum: AI/ML Automation Platform</text>
  </g>
</svg>"""
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
