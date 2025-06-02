from register import load_data
from sorting import urutanDataNama

def tampilkan_ktp():
    print("\n--- Cetak KTP ---")
    data = load_data()
    if not data:
        print("Belum ada data.")
        return

    for item in data:
        print("+" + "=" * 60 + "+")
        print("|{:^60}|".format("PROVINSI DAERAH ISTIMEWA YOGYAKARTA"))
        print("|{:^60}|".format("KABUPATEN/KOTA {}".format(item['ALAMAT'].upper())))
        print("+" + "-" * 60 + "+")
        print("| NIK               : {:<38} |".format(item['NIK']))
        print("| Nama              : {:<38} |".format(item['NAMA'].upper()))
        print("| Tempat/Tgl Lahir  : {:<38} |".format(f"{item['TEMPAT LAHIR'].upper()}, {item['TANGGAL LAHIR']}"))
        print("| Alamat            : {:<38} |".format(item['ALAMAT'].upper()))
        print("| Pekerjaan         : {:<38} |".format(item['PEKERJAAN'].upper()))
        print("| Agama             : {:<38} |".format(item['AGAMA'].upper()))
        print("| Status Perkawinan : {:<38} |".format(item['STATUS PERKAWINAN'].upper()))
        print("| Jenis Kelamin     : {:<38} |".format(item['JENIS KELAMIN'].upper()))
        print("+" + "=" * 60 + "+\n")
    
    sorting = input("mau sorting via NIK? [ketik Y]").upper()
    if sorting == "Y":
        urutanDataNama()
