### Sistem Manajemen Penyewaan Mobil
Program ini merupakan aplikasi berbasis Python yang dibuat untuk mengelola proses penyewaan mobil. Sistem berjalan di terminal (CLI) dan berfungsi membantu admin dalam mencatat data mobil, data pelanggan, serta mengatur transaksi sewa dan pengembalian kendaraan. Seluruh logika dijalankan secara prosedural dan data disimpan sementara di memori menggunakan struktur list dan dictionary.

### Deskripsi Umum
Sistem ini berperan sebagai simulasi sederhana dari bisnis rental mobil. Melalui menu interaktif, pengguna dapat menambahkan data mobil dan pelanggan, melakukan pencarian kendaraan berdasarkan berbagai kriteria, serta memproses transaksi penyewaan dan pengembalian. Program dirancang agar mudah dipahami dan menjadi dasar untuk pengembangan sistem yang lebih kompleks di masa depan, misalnya dengan penyimpanan data ke file atau database.

### Fitur dan Cara Kerja
Fitur pertama yang tersedia adalah Input Data Mobil, di mana admin dapat menambahkan informasi kendaraan seperti nomor kendaraan, merek, model, tahun, harga sewa per hari, serta status ketersediaan. Setiap data disimpan sebagai dictionary di dalam list bernama data_mobil. Dengan cara ini, semua mobil yang dimasukkan akan terdaftar dalam sistem selama program berjalan.

Selanjutnya terdapat fitur Hapus Data Mobil, yang memungkinkan admin menghapus kendaraan tertentu berdasarkan nomor kendaraannya. Program akan mencari data tersebut di dalam list dan menghapusnya apabila ditemukan. Jika tidak ada kecocokan, sistem menampilkan pesan bahwa mobil tidak ditemukan.

Fitur Input Data Pelanggan berfungsi untuk menyimpan data penyewa ke dalam list data_pelanggan. Data ini berisi ID pelanggan, nama, alamat, dan nomor HP. Sama seperti data mobil, seluruh informasi pelanggan akan tersimpan sementara selama sesi program berlangsung.
Untuk membantu pencarian, tersedia fungsi Cari Mobil yang dapat digunakan untuk menemukan kendaraan berdasarkan nomor kendaraan, merek, atau model. Pencarian dilakukan tanpa memperhatikan huruf besar atau kecil (case-insensitive), dan hasilnya akan menampilkan detail lengkap mobil yang ditemukan, termasuk status ketersediaan serta harga sewanya.

Fitur Transaksi Sewa menjadi bagian inti dari sistem ini. Admin dapat memproses penyewaan mobil dengan memasukkan nomor kendaraan, ID pelanggan, dan lama sewa dalam hitungan hari. Program kemudian memeriksa apakah mobil tersebut tersedia. Jika ya, sistem menghitung total biaya sewa berdasarkan harga harian dikalikan dengan lama sewa, lalu memperbarui status mobil menjadi “Tidak Tersedia”. Jika mobil sedang disewa oleh pelanggan lain, program akan menolak transaksi baru.

Sebagai pelengkap, fungsi Transaksi Pengembalian digunakan untuk memperbarui status mobil setelah pelanggan mengembalikannya. Admin hanya perlu memasukkan nomor kendaraan, dan sistem akan memeriksa statusnya. Jika mobil sebelumnya disewa, maka statusnya dikembalikan menjadi “Tersedia”. Jika ternyata mobil sudah tersedia, sistem memberi tahu bahwa tidak ada perubahan yang perlu dilakukan.

Seluruh fitur di atas diatur melalui menu utama yang ditampilkan oleh fungsi tampilkan_menu(). Menu ini berisi opsi interaktif yang dapat dipilih pengguna dengan mengetikkan angka sesuai fitur yang diinginkan. Program akan terus berjalan dalam loop hingga pengguna memilih opsi keluar. Dengan pendekatan ini, pengguna dapat berpindah antarfitur tanpa harus menjalankan ulang program setiap kali.

### Alur Logika Program
Ketika program dijalankan, fungsi tampilkan_menu() langsung aktif dan menampilkan daftar pilihan utama. Setiap kali pengguna memilih salah satu opsi, sistem memanggil fungsi yang sesuai — misalnya input_data_mobil() untuk menambahkan mobil baru, atau transaksi_sewa() untuk memproses penyewaan. Setelah fungsi selesai dijalankan, pengguna akan dikembalikan ke menu utama untuk melanjutkan proses lain. Program hanya akan berhenti jika pengguna memilih keluar.

Sederhananya, alur logika program dimulai dari tampilan menu, kemudian mengarah ke fungsi sesuai pilihan, dan berakhir kembali ke menu utama dalam satu siklus berulang. Pola ini memastikan bahwa sistem tetap aktif selama dibutuhkan dan interaksi berjalan dengan lancar.

### Catatan Tambahan
Data dalam sistem tidak tersimpan secara permanen. Setelah program ditutup, semua informasi mobil, pelanggan, dan transaksi akan hilang karena hanya tersimpan di memori sementara. Hal ini menjadikan program ini ideal sebagai prototipe awal atau latihan untuk konsep manajemen data.

Program ini dapat dikembangkan lebih lanjut dengan menambahkan penyimpanan file (seperti CSV atau JSON), koneksi ke database, sistem login untuk admin, serta pencatatan riwayat transaksi secara otomatis.

### Cara Menjalankan Program
Pastikan Python versi 3 sudah terpasang di perangkatmu. Simpan file program dengan nama rental_mobil.py, lalu jalankan melalui terminal atau command prompt dengan perintah:
python rental_mobil.py

### Diagram Sederhana Alur Program
[Mulai] -> [Tampilkan Menu] -> [Pilih Opsi] -> [Jalankan Fungsi Sesuai Pilihan] -> [Kembali ke Menu Utama] -> [Keluar] -> [Selesai]

### Kesimpulan
Sistem Manajemen Penyewaan Mobil ini merupakan contoh penerapan dasar logika pemrograman dalam pengelolaan data menggunakan Python. Meskipun sederhana, struktur kodenya dirancang modular dan mudah dikembangkan. Program ini dapat menjadi pijakan awal sebelum beralih ke sistem yang lebih kompleks dengan penyimpanan data permanen, autentikasi pengguna, serta antarmuka berbasis web atau GUI.
