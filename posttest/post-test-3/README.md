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
