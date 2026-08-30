#!/usr/bin/env python3
import os
from svg_utils import render_terminal_svg

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "opensource-mandar1045.svg")

import requests
from collections import defaultdict

def fetch_orgs():
    token = os.environ.get('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    headers['User-Agent'] = 'profile-readme-bot/1.0'
    url = 'https://api.github.com/search/issues?q=is:pr+author:mandar1045+is:public&per_page=100'
    
    orgs = defaultdict(lambda: {'merged': 0, 'open': 0, 'closed': 0})
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        
        for item in data.get('items', []):
            repo_url = item.get('repository_url', '')
            if not repo_url: continue
            
            org = repo_url.split('/')[-2]
            if org.lower() in ('mandar1045', 'sahilmurhekar'):
                continue
                
            if item.get('pull_request', {}).get('merged_at'):
                orgs[org]['merged'] += 1
            elif item.get('state') == 'open':
                orgs[org]['open'] += 1
            else:
                orgs[org]['closed'] += 1
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [
            ("fossology", {"merged": 8, "open": 1, "closed": 14}),
            ("supabase", {"merged": 1, "open": 3, "closed": 4}),
            ("kubernetes", {"merged": 0, "open": 0, "closed": 2}),
            ("PostHog", {"merged": 0, "open": 0, "closed": 3})
        ]
        
    sorted_orgs = sorted(orgs.items(), key=lambda x: -(x[1]['merged'] + (x[1]['open'] * 0.5)))
    return sorted_orgs[:12] # Limit to top 12 orgs so it fits in terminal

import base64

def get_avatar_b64(org):
    try:
        url = f"https://github.com/{org}.png?size=40"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            b64 = base64.b64encode(resp.content).decode('utf-8')
            return f'<image href="data:image/png;base64,{b64}" x="20" y="15" width="24" height="24" style="border-radius: 4px;" />'
    except Exception as e:
        print(f"Failed to fetch avatar for {org}: {e}")
    # Fallback to the folder icon if fetch fails
    return f'<text class="hl" x="20" y="32">📁</text>'

def generate():
    org_data = fetch_orgs()
    
    body = """
    <style>
      .txt { fill: #c9d1d9; font-size: 13px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
      .hl { fill: #22d3ee; font-weight: bold; font-size: 14px;}
      .success { fill: #39d353; font-weight: bold; font-size: 12px;}
      .warn { fill: #f2cc60; font-weight: bold; font-size: 12px;}
      .dim { fill: #8b949e; font-size: 12px; }
      .cursor { fill: #c9d1d9; animation: blink 1s step-end infinite; }
      @keyframes blink { 50% { opacity: 0; } }
      .fade-in { opacity: 0; animation: fadeIn 0.5s forwards; }
      @keyframes fadeIn { to { opacity: 1; } }
      .card { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
    </style>
    
    <text class="txt" y="0" font-size="14px"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ ./opensource.sh</text>
"""
    
    # Generate cards for each org
    for i, (org, counts) in enumerate(org_data):
        col = i % 2
        row = i // 2
        
        x_pos = 0 if col == 0 else 420
        y_pos = 30 + row * 80
        delay = 0.2 + (i * 0.1)
        
        status_text = ""
        status_class = ""
        if counts['merged'] > 0:
            status_text = f"✓ {counts['merged']} Merged PRs"
            status_class = "success"
        elif counts['open'] > 0:
            status_text = f"⟳ {counts['open']} Open PRs"
            status_class = "warn"
        else:
            status_text = f"• {counts['closed']} Contributions"
            status_class = "dim"
            
        avatar_svg = get_avatar_b64(org)
            
        card = f"""
    <!-- Card {i} -->
    <g transform="translate({x_pos}, {y_pos})" class="fade-in" style="animation-delay: {delay}s">
      <rect class="card" width="380" height="70" />
      {avatar_svg}
      <text class="hl" x="52" y="32">{org}</text>
      <text class="{status_class}" x="20" y="52">{status_text}</text>
    </g>"""
        body += card

    total_rows = (len(org_data) + 1) // 2
    final_y = 30 + (total_rows * 80) + 10
    
    body += f"""
    <g transform="translate(0, {final_y})" class="fade-in" style="animation-delay: {0.2 + len(org_data) * 0.1}s">
      <text class="txt" y="0" font-size="14px"><tspan fill="#39d353">mandar1045@github</tspan>:<tspan fill="#79c0ff">~</tspan>$ <tspan class="cursor">█</tspan></text>
    </g>
    """
    
    svg = render_terminal_svg(
        title_text="mandar1045@github: ~/opensource",
        body_content=body,
        width=860,
        height=final_y + 40
    )
    
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    generate()
