data_mobil = []
data_pelanggan = []

def input_data_mobil():
    print("\n=== Input Data Mobil ===")
    nomor_kendaraan = input("Nomor Kendaraan: ")
    merek = input("Merek: ")
    model = input("Model: ")
    tahun = input("Tahun: ")
    harga_sewa = float(input("Harga Sewa per Hari: "))
    status = input("Status (Tersedia/Tidak Tersedia): ")
    data_mobil.append({
        'nomor_kendaraan': nomor_kendaraan,
        'merek': merek,
        'model': model,
        'tahun': tahun,
        'harga_sewa': harga_sewa,
        'status': status
    })
    print("Data mobil berhasil ditambahkan.")

def hapus_data_mobil():
    print("\n=== Hapus Data Mobil ===")
    nomor_kendaraan = input("Masukkan Nomor Kendaraan yang akan dihapus: ")
    mobil_ditemukan = False
    for mobil in data_mobil:
        if mobil['nomor_kendaraan'] == nomor_kendaraan:
            mobil_ditemukan = True
            data_mobil.remove(mobil)
            print("Data mobil berhasil dihapus.")
            break
    if not mobil_ditemukan:
        print("Mobil tidak ditemukan.")

def input_data_pelanggan():
    print("\n=== Input Data Pelanggan ===")
    id_pelanggan = input("ID Pelanggan: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    no_hp = input("No. HP: ")
    data_pelanggan.append({
        'id_pelanggan': id_pelanggan,
        'nama': nama,
        'alamat': alamat,
        'no_hp': no_hp
    })
    print("Data pelanggan berhasil ditambahkan.")

def tampilkan_menu():
    while True:
        print("\n=== Sistem Manajemen Penyewaan Mobil ===")
        print("1. Input Data Mobil")
        print("2. Hapus Data Mobil")
        print("3. Input Data Pelanggan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            input_data_mobil()
        elif pilihan == "2":
            hapus_data_mobil()
        elif pilihan == "3":
            input_data_pelanggan()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

def cari_mobil():
    print("\n=== Cari Mobil ===")
    keyword = input("Masukkan Nomor Kendaraan, Merek, atau Model: ")
    mobil_ditemukan = False
    for mobil in data_mobil:
        if (keyword.lower() in mobil['nomor_kendaraan'].lower() or
                keyword.lower() in mobil['merek'].lower() or
                keyword.lower() in mobil['model'].lower()):
            mobil_ditemukan = True
            print("\nMobil Ditemukan:")
            print(f"Nomor Kendaraan: {mobil['nomor_kendaraan']}")
            print(f"Merek: {mobil['merek']}")
            print(f"Model: {mobil['model']}")
            print(f"Tahun: {mobil['tahun']}")
            print(f"Harga Sewa per Hari: {mobil['harga_sewa']}")
            print(f"Status: {mobil['status']}")
    if not mobil_ditemukan:
        print("Mobil tidak ditemukan.")

def transaksi_sewa():
    print("\n=== Transaksi Sewa ===")
    nomor_kendaraan = input("Masukkan Nomor Kendaraan yang ingin disewa: ")
    id_pelanggan = input("Masukkan ID Pelanggan: ")
    lama_sewa = int(input("Lama Sewa (dalam hari): "))
    mobil_ditemukan = False
    for mobil in data_mobil:
        if mobil['nomor_kendaraan'] == nomor_kendaraan:
            mobil_ditemukan = True
            if mobil['status'].lower() == "tersedia":
                total_biaya = mobil['harga_sewa'] * lama_sewa
                mobil['status'] = "Tidak Tersedia"
                print(f"Transaksi sewa berhasil. Total biaya sewa: Rp {total_biaya}")
                print("Transaksi sewa berhasil. Mobil status diperbarui menjadi 'Tidak Tersedia'.")
            else:
                print("Maaf, mobil tidak tersedia untuk disewa.")
            break
    if not mobil_ditemukan:
        print("Mobil tidak ditemukan.")

def transaksi_pengembalian():
    print("\n=== Transaksi Pengembalian ===")
    nomor_kendaraan = input("Masukkan Nomor Kendaraan yang dikembalikan: ")
    mobil_ditemukan = False
    for mobil in data_mobil:
        if mobil['nomor_kendaraan'] == nomor_kendaraan:
            mobil_ditemukan = True
            if mobil['status'].lower() == "tidak tersedia":
                mobil['status'] = "Tersedia"
                print("Pengembalian berhasil. Status mobil diperbarui menjadi 'Tersedia'.")
            else:
                print("Mobil sudah dalam status 'Tersedia'. Tidak ada perubahan status.")
            break
    if not mobil_ditemukan:
        print("Mobil tidak ditemukan.")

def tampilkan_menu():
    while True:
        print("\n=== Sistem Manajemen Penyewaan Mobil ===")
        print("1. Input Data Mobil")
        print("2. Hapus Data Mobil")
        print("3. Input Data Pelanggan")
        print("4. Cari Mobil")
        print("5. Transaksi Sewa")
        print("6. Transaksi Pengembalian")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == "1":
            input_data_mobil()
        elif pilihan == "2":
            hapus_data_mobil()
        elif pilihan == "3":
            input_data_pelanggan()
        elif pilihan == "4":
            cari_mobil()
        elif pilihan == "5":
            transaksi_sewa()
        elif pilihan == "6":
            transaksi_pengembalian()
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

tampilkan_menu()