[README.md](https://github.com/user-attachments/files/23933201/README.md)
# Permainan Kelereng Sederhana (Python)

Proyek ini berisi implementasi permainan kelereng sederhana secara modular menggunakan Python. Game dimainkan oleh dua pemain secara bergantian: satu pemain mempertaruhkan sejumlah kelereng, dan pemain lawan menebak apakah jumlah tersebut ganjil (G) atau genap (J). Tebakan benar memindahkan kelereng dari penaruh ke penebak.

## Struktur Berkas
- `main.py`  
  Program utama yang menjalankan alur permainan, membaca input pemain, dan mengatur giliran/ronde.
- `player.py`  
  Modul definisi kelas `Player` yang menangani atribut pemain (nama dan jumlah kelereng) serta metode untuk meminta taruhan dan tebakan melalui input pengguna.
- `kelereng.py`  
  Modul logika permainan yang berisi fungsi untuk menjalankan satu ronde (`mainkan_ronde`), memeriksa kondisi akhir permainan (`akhir_permainan`), dan menampilkan status pemain (`status_pemain`).

## Persyaratan
- Python 3.6+ (direkomendasikan Python 3.8 atau lebih baru)
- Tidak ada dependensi eksternal

## Cara Menjalankan
1. Pastikan ketiga berkas (`main.py`, `player.py`, `kelereng.py`) berada dalam direktori yang sama.
2. Jalankan program:
   ```
   python main.py
   ```
3. Ikuti instruksi pada layar:
   - Masukkan nama untuk Pemain 1 dan Pemain 2.
   - Masukkan jumlah ronde maksimal (0 untuk tak terbatas).
   - Pada tiap giliran, pemain yang bertaruh akan diminta memasukkan berapa kelereng yang dipertaruhkan.
   - Pemain penebak akan diminta menebak 'G' untuk ganjil atau 'J' untuk genap.

Permainan berakhir jika salah satu pemain kehabisan kelereng atau jika jumlah ronde mencapai batas maksimal (jika ditentukan). Jika ronde maksimal tercapai, pemenang ditentukan dari jumlah kelereng terbanyak; jika sama, hasil seri.

## Contoh Alur Singkat
- Pemain A dan Pemain B masing-masing mulai dengan 10 kelereng.
- Ronde 1: A mempertaruhkan 3 → B menebak "G" → jika benar B mendapatkan 3 kelereng dari A.
- Ronde 2: (berganti giliran) B mempertaruhkan, A menebak, dan seterusnya.

## Penjelasan Fungsi/Kelas Utama
- Player (player.py)
  - __init__(nama, jumlah_kelereng): inisialisasi pemain
  - taruhan(): meminta input jumlah taruhan yang valid antara 1 dan jumlah kelereng saat ini
  - tebakan(): meminta input tebakan 'G' atau 'J'
  - __str__(): representasi teks pemain dan jumlah kelereng

- cek_ganjil_genap(jumlah) (kelereng.py)
  - Mengembalikan "G" jika jumlah ganjil, "J" jika genap.

- mainkan_ronde(pemain1, pemain2) (kelereng.py)
  - Menjalankan satu ronde: pemain1 bertaruh, pemain2 menebak, dan kelereng dipindahkan jika tebakan benar.

- akhir_permainan(p1, p2, max_ronde=None, ronde_ke=None) (kelereng.py)
  - Mengecek apakah salah satu pemain habis kelereng atau ronde maksimal tercapai; mencetak hasil dan mengembalikan True jika permainan harus diakhiri.

## Rekomendasi Perbaikan / Ekstensi
- Validasi input lebih kuat (mis. menolak angka negatif atau string non-digit lebih informatif).
- Mode pemain vs komputer: tambahkan AI sederhana untuk taruhan dan tebakan.
- Antarmuka grafis (mis. tkinter) atau web sederhana untuk pengalaman interaktif.
- Unit tests untuk fungsi logika (cek_ganjil_genap, akhir_permainan) dan perilaku Player menggunakan mocking input.
- Menambahkan fitur logging atau kemampuan menyimpan skor.

## Lisensi
Gunakan sesuka hati — Anda bebas menyalin dan memodifikasi kode ini untuk keperluan belajar dan eksperimen.
