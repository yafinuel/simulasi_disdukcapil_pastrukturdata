import json
import os
from datetime import datetime

# File untuk menyimpan data
DATA_FILE = "data_warga.json"

def load_data():
    """Memuat data dari file JSON jika ada"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except:
            return []
    return []

def save_data(data):
    """Menyimpan data ke file JSON"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def validate_date(date_str):
    """Validasi format tanggal DD-MM-YYYY"""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def input_data():
    """Fungsi untuk menginput data warga baru"""
    print("\n" + "="*100)
    print("FORMULIR PENDAFTARAN WARGA".center(100))
    print("="*100)
    
    data_warga = []
    
    # Memuat data yang sudah ada
    data_warga = load_data()
    
    while True:
        # Input nik dengan validasi
        while True:
            nik = input("nik (16 digit angka)\t: ").strip()
            
            # Validasi nik harus unik
            if nik in data_warga:
                print("\n❌ nik sudah terdaftar! Gunakan nik yang berbeda")
                continue
                
            # Validasi nik harus angka dan 16 digit
            if not nik.isdigit() or len(nik) != 16:
                print("\n❌ nik harus 16 digit angka!")
                continue
                
            break
        
        # Input data lainnya
        nama = input("Nama Lengkap \t: ").title()
        tempat_lahir = input("Tempat Lahir \t: ").title()
        
        # Validasi format tanggal
        while True:
            tanggal_lahir = input("Tanggal Lahir (DD-MM-YYYY) : ")
            if validate_date(tanggal_lahir):
                break
            print("❌ Format tanggal salah! Gunakan format DD-MM-YYYY")
        
        PEKERJAAN = input("Pekerjaan \t: ").title()
        ALAMAT = input("Alamat Domisili \t: ")
        agama = input ("Masukan Agama \t: ")
        
        # Validasi status perkawinan
        status_perkawinan = ""
        while status_perkawinan not in ['Lajang', 'Menikah', 'Cerai']:
            status_perkawinan = input("Status Perkawinan (Lajang/Menikah/Cerai) : ").title()
            if status_perkawinan not in ['Lajang', 'Menikah', 'Cerai']:
                print("❌ Pilihan tidak valid! Pilih dari: Lajang, Menikah, Cerai")
        
        # Validasi jenis kelamin
        jenis_kelamin = ""
        while jenis_kelamin not in ['L', 'P']:
            jenis_kelamin = input("Jenis Kelamin (L/P) \t: ").upper()
            if jenis_kelamin not in ['L', 'P']:
                print("❌ Pilihan tidak valid! Masukkan L atau P")

        # Menambahkan data baru
        data_ktp = {
            "NIK": nik,
            'NAMA': nama,
            'TEMPAT LAHIR': tempat_lahir,
            'TANGGAL LAHIR': tanggal_lahir,
            'PEKERJAAN': PEKERJAAN,
            'ALAMAT': ALAMAT,
            'AGAMA' : agama,
            'STATUS PERKAWINAN': status_perkawinan,
            'JENIS KELAMIN': jenis_kelamin
        }
        data_warga.append(data_ktp)       
        save_data(data_warga)
        print("\n✅ Data warga berhasil didaftarkan!")
        
        # Tanya apakah ingin input data lagi
        ulangi = input("\nInput data warga lagi? (y/t): ").lower()
        if ulangi != 'y':
            print("\nTerima kasih! Program pendaftaran selesai.")
            break

