import os
from prompt_toolkit import prompt
from rich.console import Console
from display_panel import tampil_panel

datas = [
{
    "NIK" : 123456789,
    "NAMA" : "Yafi Nuqman Elianto",
    "TTL" : ['Bantul', '2000-01-01'],
    "ALAMAT" : ["Sedayu", "Bantul", "Yogyakarta"],
    "AGAMA" : "Islam",
    "STATUS PERKAWINAN" : "Belum Kawin",
    "PEKERJAAN" : "Pelajar/Mahasiswa",
    "KEWARGANEGARAAN" : "WNI",
    "BERLAKU HINGGA" : "Seumur hidup"
},{
    "NIK" : 234567891,
    "NAMA" : "Manusia 2",
    "TTL" : ['Sleman', '2000-01-02'],
    "ALAMAT" : ["Godean", "Sleman", "Yogyakarta"],
    "AGAMA" : "Islam",
    "STATUS PERKAWINAN" : "Belum Kawin",
    "PEKERJAAN" : "Pelajar/Mahasiswa",
    "KEWARGANEGARAAN" : "WNI",
    "BERLAKU HINGGA" : "Seumur hidup"
}]


def textPanel(dictionary):
    text = "\n"
    indent = max(len(key) for key in dictionary.keys())
    for key, value in dictionary.items():
        if len(key) < 4:
            key_format = key
        else: 
            key_format = key.title()

        if isinstance(value, list):
            value_format = ', '.join(map(str, value))
        else:
            value_format = str(value)
        spacing = " " * (indent - len(key_format) +1)
        text += f"{key_format}{spacing}: {value_format}\n"

    return text

console = Console()
page = "Edit data"


def updateData():
    running = True
    while running:
        os.system('cls')
        data = datas[1]
        console.print(tampil_panel(textPanel(data), page))
        option = input("Apa yang ingin Anda ubah? [ketik 'q' untuk keluar]\nKetik: ").upper()
        match option:
            case "NIK":
                print("Dilarang mengubah NIK")
                input("Enter untuk lanjutkan:")
            case "NAMA":
                data["NAMA"] = prompt("Nama: ", default=data["NAMA"])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "TTL" | "TEMPAT, TANGGAL LAHIR" | "TEMPAT/ TANGGAL LAHIR":
                data["TTL"][0] = prompt("Tempat kelahiran: ", default=data["TTL"][0])
                data["TTL"][1] = prompt("Tanggal kelahiran: ", default=data["TTL"][1])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "ALAMAT":
                data["ALAMAT"][0] = prompt("Kecamatan: ", default=data["ALAMAT"][0])
                data["ALAMAT"][1] = prompt("Kabupaten: ", default=data["ALAMAT"][1])
                data["ALAMAT"][2] = prompt("Provinsi: ", default=data["ALAMAT"][2])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "AGAMA":
                data["AGAMA"] = prompt("Agama: ", default=data["AGAMA"])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "STATUS PERKAWINAN":
                benar = True
                while benar:
                    print("1. Sudah Kawin\n2. Belum Kawin")
                    pilih = int(input("Status Perkawinan: "))
                    match pilih:
                        case 1:
                            data["STATUS PERKAWINAN"] = "Sudah Kawin"
                            input("Enter untuk lanjutkan:")
                            benar = False
                        case 2:
                            data["STATUS PERKAWINAN"] = "Belum Kawin"
                            input("Enter untuk lanjutkan:")
                            benar = False
                        case _:
                            print("Inputmu salah, pilih dengan benar!")
                            input("Enter untuk lanjutkan:")
            case "PEKERJAAN":
                data["PEKERJAAN"] = prompt("Pekerjaan: ", default=data["PEKERJAAN"])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "KEWARGANEGARAAN":
                data["KEWARGANEGARAAN"] = prompt("Kewarganegaraan: ", default=data["KEWARGANEGARAAN"])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case "BERLAKU HINGGA":
                data["BERLAKU HINGGA"] = prompt("Berlaku Hingga: ", default=data["BERLAKU HINGGA"])
                print("data berhasil diubah")
                input("Enter untuk lanjutkan:")
            case 'Q':
                running = False
            case _:
                input("Masukkan input dengan benar! [enter untuk lanjutkan]")

