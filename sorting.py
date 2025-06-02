import json
from register import load_data

def urutanDataNama():
    """
    Load data warga dari data_warga.json, urutkan berdasarkan field 'NAMA',
    lalu cetak hasilnya secara terstruktur.
    """

    # 1. Muat data dari file JSON
    semua_data = load_data()  # Mengembalikan list (ideal) atau dict (alternatif).
    
    # 2. Jika load_data() mengembalikan dict (keyed by nik), konversi ke list.
    if isinstance(semua_data, dict):
        listPenduduk = []
        for nik_key, info in semua_data.items():
            if isinstance(info, dict):
                entri = info.copy()
                entri['NIK'] = nik_key
                listPenduduk.append(entri)
        # Jika dict kosong, listPenduduk akan tetap kosong.
    elif isinstance(semua_data, list):
        # Diasumsikan sudah list of dict sesuai cara register.py menyimpan.
        listPenduduk = semua_data[:]
    else:
        print("Format data di 'data_warga.json' tidak dikenali. Harus berupa list atau dict.")
        return

    if not listPenduduk:
        print("Tidak ada data penduduk dalam berkas 'data_warga.json'.")
        return

    # 3. Lakukan Insertion Sort berdasarkan field 'NAMA' (case-insensitive).
    for i in range(1, len(listPenduduk)):
        key_item = listPenduduk[i]
        nama_key = key_item.get('NIK', '')
        j = i - 1
        while j >= 0 and nama_key.lower() < listPenduduk[j].get('NIK', '').lower():
            j -= 1
        listPenduduk.insert(j + 1, listPenduduk.pop(i))

    # 4. Cetak hasil sorting secara terstruktur
    print("\n=== Data Penduduk (Urut berdasarkan NIK) ===\n")
    for idx, penduduk in enumerate(listPenduduk, start=1):
        nik_val               = penduduk.get('NIK', '-')
        nama_val              = penduduk.get('NAMA', '-')
        tempat_lahir_val      = penduduk.get('TEMPAT LAHIR', '-')
        tanggal_lahir_val     = penduduk.get('TANGGAL LAHIR', '-')
        pekerjaan_val         = penduduk.get('PEKERJAAN', '-')
        alamat_val            = penduduk.get('ALAMAT', '-')
        agama_val             = penduduk.get('AGAMA', '-')
        status_perkawinan_val = penduduk.get('STATUS PERKAWINAN', '-')
        jenis_kelamin_val     = penduduk.get('JENIS KELAMIN', '-')

        # Jika suatu field berupa list, gabungkan ke string
        if isinstance(tempat_lahir_val, list):
            tempat_lahir_val = ", ".join(tempat_lahir_val)
        if isinstance(tanggal_lahir_val, list):
            tanggal_lahir_val = ", ".join(tanggal_lahir_val)
        if isinstance(alamat_val, list):
            alamat_val = ", ".join(alamat_val)

        print(f"{idx}. NIK                : {nik_val}")
        print(f"   Nama              : {nama_val}")
        print(f"   Tempat Lahir      : {tempat_lahir_val}")
        print(f"   Tanggal Lahir     : {tanggal_lahir_val}")
        print(f"   Alamat            : {alamat_val}")
        print(f"   Agama             : {agama_val}")
        print(f"   Status Perkawinan : {status_perkawinan_val}")
        print(f"   Pekerjaan         : {pekerjaan_val}")
        print(f"   Jenis Kelamin     : {jenis_kelamin_val}\n")


