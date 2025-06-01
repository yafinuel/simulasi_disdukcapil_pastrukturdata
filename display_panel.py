from rich.panel import Panel

def tampil_panel(text, page):
    panel = Panel(
        text,
        title=page,
        subtitle="Simulasi Disdukcapil",
        border_style="blue",
        width=200
    )
    return panel
