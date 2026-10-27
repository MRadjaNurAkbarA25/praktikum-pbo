Posttest 3 Pemrograman Berorientasi Objek
Nama    : Muhamad Radja Nur Akbar
NIM     : 2509106012
Kelas   : A1'25

Posttest 3: Polimorfisme, Abstraksi, dan SOLID

  Pada posttest ketiga ini, pilar polimorfisme dan abstraksi serta salah satu prinsip SOLID juga diterapkan pada program inventaris barang. Di posttest ini struktur program dimodularisasikan untuk mempermudah dalam membaca kode dan memahami alurnya. 

posttest/post-test-3/
├── posttest3_2509106012_MuhamadRadjaNurAkbar.py   ← main (program utama / demo)
├── README.md                                       ← laporan
├── images/
│   ├── class_diagram.png
│   └── output_*.png                                ← screenshot output
└── models/
    ├── __init__.py
    ├── utils.py               ← cek_bulat(), cek_teks(), rupiah()
    ├── riwayat_stok.py        ← RiwayatStok
    ├── barang_inventaris.py   ← BarangInventaris
    ├── karyawan.py            ← Karyawan (abstract, ABC)
    ├── staff.py               ← Staff
    ├── manager.py             ← Manager
    ├── magang.py              ← Magang
    └── ruangan.py             ← Ruangan

  Dalam laporan ini, saya akan menjelaskan setiap file, mulai dari yang baru hingga perubahan apa yang ada pada file sejak posttest kedua.

A. File __init__.py
  File ini tidak punya fungsi atau kelas. Tugasnya menjadikan folder models sebuah package Python dan mengumpulkan semua kelas, sehingga file utama cukup menulis from models import Staff, Ruangan, rupiah. Pada baris:

from .utils import rupiah

  Titik mengacu pada folder models itu sendiri. Hanya mengimpor rupiah karena fungsi lain pada .utils hanya dipakai di dalam kelas. Sementara itu, baris-baris seterusnya mengimpor kelas-kelas lain. Jika menggunakan asterisks (*) atau mengimpor semua yang ada di models, daftar nama di dalam __all__ akan terikut.

B. File utils.py
  File ini berisi fungsi pembantu, 2 diantara 3 fungsi merupakan fungsi validasi yang dipakai di setiap setter. Jadi tidak perlu menulis validasi yang sama terus-menerus. Fungsi cek_bulat() memastikan suatu nilai merupakan bilangan bulat dan tidak negatif. Digunakan untuk menjaga angka adalah bulat dalam operasi matematika dan lain-lain.

def cek_bulat(nilai, label):
    # bool adalah turunan int (True == 1), jadi ditolak secara eksplisit
    if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai < 0:
        raise ValueError(f'{label} harus bilangan bulat dan tidak boleh negatif!')
    return nilai

  Fungsi cek_teks() memastikan nilai bertipe string, atau jika kosong setelah strip() (spasi di awal dan akhir dibuang, sehingga '   ' ikut ditolak).

def cek_teks(nilai, label):
    if not isinstance(nilai, str) or nilai.strip() == '':
        raise ValueError(f'{label} tidak boleh kosong!')
    return nilai

  Fungsi rupiah() berfungsi untuk memodelkan format uang rupiah. Bagian f'{nilai:,}' memberi pemisah ribuan koma. Bagian .replace mengganti koma menjadi titik yang merupakan gaya pemisah di Indonesia.

def rupiah(nilai):
    return 'Rp' + f'{nilai:,}'.replace(',', '.')
