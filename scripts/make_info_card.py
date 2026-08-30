#!/usr/bin/env python3
"""
Generate a neofetch-style info card SVG with infinite scrolling.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "info-mandar1045.svg")

def generate():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="450" viewBox="0 0 490 450" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="wbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
    <clipPath id="terminal-clip">
      <rect x="0" y="29" width="490" height="421" />
    </clipPath>
  </defs>
  <rect width="490" height="450" rx="12" fill="url(#wbg)"/>
  <rect x="0.5" y="0.5" width="489" height="449" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>
  <line x1="0" y1="28" x2="490" y2="28" stroke="#30363d"/>
  <circle cx="18" cy="14" r="4.5" fill="#ff5f56"/>
  <circle cx="33" cy="14" r="4.5" fill="#ffbd2e"/>
  <circle cx="48" cy="14" r="4.5" fill="#27c93f"/>
  <text x="245" y="18" fill="#7d8590" font-size="11.5" text-anchor="middle">mandar1045@github: ~$ cat info.txt</text>
  
  <style>
    .title { fill: #22d3ee; font-weight: bold; font-size: 16px; }
    .header { fill: #f2cc60; font-weight: bold; font-size: 14px; }
    .label { fill: #39d353; font-weight: bold; }
    .text { fill: #c9d1d9; font-size: 13px; }
    .dim { fill: #7d8590; font-size: 13px; }
  </style>

  <g clip-path="url(#terminal-clip)">
    <g>
      <animateTransform 
        attributeName="transform" 
        type="translate" 
        from="30 420" 
        to="30 -900" 
        dur="30s" 
        repeatCount="indefinite" />
      
      <!-- Identity -->
      <text y="0" class="title">Mandar Joshi</text>
      <text y="20" class="dim">------------------------------------------</text>
      <text y="45" class="text"><tspan class="label">Role   </tspan>   Software Engineer / Student</text>
      <text y="70" class="text"><tspan class="label">College</tspan>   VIT Vellore (IT)</text>
      <text y="95" class="text"><tspan class="label">Focus  </tspan>   Distributed Systems, Microservices, Open Source</text>
      <text y="120" class="text"><tspan class="label">Stack  </tspan>   Go, Python, TypeScript, Kafka, Kubernetes</text>

      <!-- Open Source -->
      <text y="160" class="dim">------------------------------------------</text>
      <text y="190" class="header">Open Source Contributions</text>
      
      <text y="215" class="text">  • <tspan class="label">Linux Foundation — FOSSology</tspan></text>
      <text y="235" class="text">    API Correctness, Import Reliability, Kubernetes</text>
      
      <text y="260" class="text">  • <tspan class="label">Supabase &amp; Cal.com</tspan></text>
      <text y="280" class="text">    Studio Reliability, CSV Import, Constraints</text>

      <text y="305" class="text">  • <tspan class="label">Kubernetes CNCF</tspan></text>
      <text y="325" class="text">    Active Contributor &amp; Community Member</text>

      <text y="350" class="text">  • <tspan class="label">PostHog</tspan></text>
      <text y="370" class="text">    Frontend Resilience, Stale Chunk Recovery</text>

      <!-- Projects -->
      <text y="410" class="dim">------------------------------------------</text>
      <text y="440" class="header">Featured Engineering Projects</text>
      
      <text y="465" class="text">  • <tspan class="label">Resync</tspan> (Live at resync.biz)</text>
      <text y="485" class="text">    UPI Autopay Recovery Platform (9 Microservices)</text>
      <text y="505" class="text">    Built with Go, Redpanda, Redis, gRPC, AWS Fargate</text>

      <text y="535" class="text">  • <tspan class="label">Continum</tspan> (Live at continum.online)</text>
      <text y="555" class="text">    AI-powered email automation and workflow platform</text>

      <text y="585" class="text">  • <tspan class="label">fossology-k8s-poc</tspan></text>
      <text y="605" class="text">    Kubernetes-native FOSSology deployment w/ Argo CD</text>

      <text y="635" class="text">  • <tspan class="label">Vaulta</tspan></text>
      <text y="655" class="text">    Desktop browser and wallet (React, Tauri, viem)</text>
      
      <text y="685" class="text">  • <tspan class="label">Crowd Management System</tspan></text>
      <text y="705" class="text">    Scalable analytics and density tracking system</text>

      <text y="735" class="text">  • <tspan class="label">ubice-poc</tspan> &amp; <tspan class="label">openclaw</tspan></text>
      <text y="755" class="text">    Binary intelligence workflows &amp; AI-first automation</text>

      <!-- Connect -->
      <text y="795" class="dim">------------------------------------------</text>
      <text y="825" class="header">Connect &amp; Links</text>
      <text y="850" class="text"><tspan class="label">GitHub   </tspan> github.com/mandar1045</text>
      <text y="875" class="text"><tspan class="label">Portfolio</tspan> mandarjoshi-portfolio.vercel.app</text>
      
      <!-- EOF / End blocks -->
      <g transform="translate(0, 920)">
        <rect x="0" y="0" width="14" height="14" fill="#000000" />
        <rect x="14" y="0" width="14" height="14" fill="#ff5555" />
        <rect x="28" y="0" width="14" height="14" fill="#50fa7b" />
        <rect x="42" y="0" width="14" height="14" fill="#f1fa8c" />
        <rect x="56" y="0" width="14" height="14" fill="#bd93f9" />
        <rect x="70" y="0" width="14" height="14" fill="#ff79c6" />
        <rect x="84" y="0" width="14" height="14" fill="#8be9fd" />
        <rect x="98" y="0" width="14" height="14" fill="#bbbbbb" />
      </g>
    </g>
  </g>
</svg>"""
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
