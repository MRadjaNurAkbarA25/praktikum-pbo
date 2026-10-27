Posttest 3 Pemrograman Berorientasi Objek
Nama    : Muhamad Radja Nur Akbar
NIM     : 2509106012
Kelas   : A1'25

Posttest 3: Polimorfisme, Abstraksi, dan SOLID
    Pada posttest ketiga ini, pilar polimorfisme dan abstraksi diterapkan pada program inventaris barang. Selain itu, prinsip SOLID juga diterapkan. Di posttest ini juga program dimodularisasikan untuk mempermudah dalam membaca kode dan memahami alurnya.

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

    Dalam laporan ini, saya akan menjelaskan setiap file, mulai dari yang baru hingga perubahan apa yang terjadi pada file sejak posttest kedua.

A. File __init__.py
    File ini tidak punya fungsi atau kelas. Tugasnya menjadikan folder models sebuah package Python dan mengumpulkan semua kelas, sehingga file utama cukup menulis from models import Staff, Ruangan, rupiah.
    Pada baris:
    
    from .utils import rupiah

    Titik mengacu pada folder models itu sendiri. Hanya mengimpor rupiah karena fungsi lain pada .utils hanya dipakai di dalam kelas.

    
