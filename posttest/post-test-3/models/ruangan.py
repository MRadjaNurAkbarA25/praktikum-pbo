# models/ruangan.py
# Peran: kelas "pengelola" yang memegang relasi
#   - Asosiasi : penanggung_jawab -> Karyawan
#   - Agregasi : daftar_barang    -> BarangInventaris
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

from .karyawan import Karyawan                      # PERUBAHAN: import dari file lain
from .barang_inventaris import BarangInventaris     # PERUBAHAN
from .utils import cek_teks, cek_bulat              # PERUBAHAN


class Ruangan:
    # atr class
    jumlah_ruangan = 0
    _kode_terpakai = set()                          # PERUBAHAN: menyimpan kode ruangan yang sudah dipakai

    def __init__(self, kode_ruangan, nama, lantai, penanggung_jawab):

        if not Ruangan.validasi_kode(kode_ruangan):
            raise ValueError('Format kode tidak valid!')
        if kode_ruangan in Ruangan._kode_terpakai:                                  # PERUBAHAN
            raise ValueError(f'Kode {kode_ruangan} sudah dipakai ruangan lain!')    # PERUBAHAN

        self.kode = kode_ruangan
        self.nama = cek_teks(nama, 'Nama ruangan')      # PERUBAHAN: divalidasi
        self.lantai = cek_bulat(lantai, 'Lantai')       # PERUBAHAN: divalidasi
        self.__penanggung_jawab = None
        self.penanggung_jawab = penanggung_jawab        # asosiasi

        self.daftar_barang = []                         # agregasi

        Ruangan._kode_terpakai.add(kode_ruangan)        # PERUBAHAN
        Ruangan.jumlah_ruangan += 1

    @property
    def penanggung_jawab(self):
        return self.__penanggung_jawab

    @penanggung_jawab.setter
    def penanggung_jawab(self, nilai):
        # PERUBAHAN (hanya komentar): bergantung pada abstraksi Karyawan (DIP),
        # jadi Staff, Manager, maupun Magang semuanya diterima
        if not isinstance(nilai, Karyawan):
            raise ValueError('Penanggung jawab harus objek Karyawan')
        self.__penanggung_jawab = nilai

    def tambah_barang(self, barang):
        if not isinstance(barang, BarangInventaris):
            raise ValueError('Barang harus berupa objek BarangInventaris!')
        elif barang in self.daftar_barang:
            raise ValueError(f'{barang.nama} sudah ada di ruangan ini!')
        self.daftar_barang.append(barang)

    def total_stok(self):
        return sum(barang.stok for barang in self.daftar_barang)

    def info(self):
        nama_barang = ", ".join(barang.nama for barang in self.daftar_barang) or "-"
        print(
            f"{self.kode} {self.nama} (lantai {self.lantai}) - "
            f"Penanggung jawab: {self.penanggung_jawab.nama} - "
            f"Barang ({len(self)}): {nama_barang}"       # PERUBAHAN: menampilkan jumlah lewat len(self)
        )

    # PERUBAHAN (BARU) - operator overloading: len(ruangan) = jumlah jenis barang di dalamnya
    def __len__(self):
        return len(self.daftar_barang)

    @classmethod
    def tampilkan_total(cls):
        print(f'Total ruangan: {cls.jumlah_ruangan}')

    @staticmethod
    def validasi_kode(kode):
        return isinstance(kode, str) and kode.strip() != "" and " " not in kode