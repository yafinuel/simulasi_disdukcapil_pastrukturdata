from rich.console import Console
from display_panel import tampil_panel

console = Console()

text = """
1. Pendaftaran KTP
2. Lihat KTP terdaftar
3. Tutup
"""
page = "Menu utama"

running = True
while running:
    console.print(tampil_panel(text, page))
    menu = int(console.input("Pilih: "))
    if menu == 1:
        pass
    elif menu == 2:
        pass
    elif menu == 3:
        break