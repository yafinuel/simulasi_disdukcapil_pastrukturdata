from rich.console import Console
from display_panel import tampil_panel
from update import updateData
from register import input_data
from showdata import tampilkan_ktp

console = Console()

text = """
1. Pendaftaran KTP
2. Lihat KTP terdaftar
3. Update Data
4. Keluar
"""
page = "Menu utama"
3
running = True
while running:
    console.print(tampil_panel(text, page))
    menu = int(console.input("Pilih: "))
    if menu == 1:
        input_data()
    elif menu == 2:
        tampilkan_ktp()
    elif menu == 3:
        updateData()
    elif menu == 4:
        break