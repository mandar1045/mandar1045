import typing

def render_terminal_svg(
    title_text: str,
    body_content: str,
    width: int = 860,
    height: int = 300,
    mac_buttons: bool = True
) -> str:
    """
    Renders a standard terminal window SVG with a title bar and a dark background.
    `body_content` should contain SVG elements (like <text>, <g>, etc.) to be placed inside the terminal.
    """
    buttons = ""
    if mac_buttons:
        buttons = """
  <circle cx="18" cy="14" r="4.5" fill="#ff5f56"/>
  <circle cx="33" cy="14" r="4.5" fill="#ffbd2e"/>
  <circle cx="48" cy="14" r="4.5" fill="#27c93f"/>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="wbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" rx="12" fill="url(#wbg)"/>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>
  <line x1="0" y1="28" x2="{width}" y2="28" stroke="#30363d"/>
{buttons}
  <text x="{width // 2}" y="18" fill="#7d8590" font-size="11.5" text-anchor="middle">{title_text}</text>
  
  <g fill="#c9d1d9" font-size="13" transform="translate(30, 60)">
    {body_content}
  </g>
</svg>"""
    return svg
