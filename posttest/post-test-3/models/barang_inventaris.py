# models/barang_inventaris.py
# Peran: bagian "Komposisi" (memiliki RiwayatStok) dan sisi "bagian" pada
# "Agregasi" (dimasukkan ke daftar_barang milik Ruangan).
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

from .utils import cek_teks, cek_bulat          # PERUBAHAN: import helper
from .riwayat_stok import RiwayatStok           # PERUBAHAN: kelas sudah di file lain


class BarangInventaris:
    # atr class
    jumlah_barang = 0
    _kode_terpakai = set()                      # PERUBAHAN: menyimpan kode yang sudah dipakai

    def __init__(self, kode, nama, kategori, stok):

        # validasi format kode sebagai identitas unik
        if not BarangInventaris.validasi_kode(kode):
            raise ValueError('Format kode tidak valid!')
        if kode in BarangInventaris._kode_terpakai:                         # PERUBAHAN
            raise ValueError(f'Kode {kode} sudah dipakai barang lain!')     # PERUBAHAN

        # instance public
        self.kode = kode
        self.nama = cek_teks(nama, 'Nama barang')           # PERUBAHAN: divalidasi
        self.kategori = cek_teks(kategori, 'Kategori')      # PERUBAHAN: divalidasi

        # private (komposisi: riwayat dibuat & dimiliki oleh barang)
        # PERUBAHAN: __riwayat dibuat SEBELUM stok, karena setter stok kini mencatat riwayat
        self.__riwayat = RiwayatStok()
        self.__stok = 0
        self.stok = stok

        BarangInventaris._kode_terpakai.add(kode)           # PERUBAHAN
        BarangInventaris.jumlah_barang += 1

    # getter
    @property
    def stok(self):
        return self.__stok

    # setter
    @stok.setter
    def stok(self, stok_baru):
        self.__stok = cek_bulat(stok_baru, 'Stok')          # PERUBAHAN: pakai helper
        self.__riwayat.catat('atur', stok_baru)             # PERUBAHAN: setter ikut dicatat

    # method instance
    def tambah_stok(self, n):
        BarangInventaris._cek_jumlah(n)                     # PERUBAHAN: validasi lewat helper
        self.__stok += n
        self.__riwayat.catat('tambah', n)

    def kurangi_stok(self, n):
        BarangInventaris._cek_jumlah(n)                     # PERUBAHAN
        if n > self.__stok:
            raise ValueError(f'Stok {self.nama} tidak cukup!')
        self.__stok -= n
        self.__riwayat.catat('kurang', n)

    def tampilkan_riwayat(self):
        print(f'Riwayat stok {self.nama}:')
        self.__riwayat.tampilkan()

    def info(self):
        print(self)                                         # PERUBAHAN: memakai __str__

    # PERUBAHAN (BARU) - operator overloading: dipanggil oleh print() / str()
    def __str__(self):
        return f'[{self.kode}] {self.nama} ({self.kategori}) - Stok: {self.__stok}'

    @classmethod
    def tampilkan_total(cls):
        print(f'Total jenis barang: {cls.jumlah_barang}')

    @classmethod
    def dari_dict(cls, data):
        return cls(data["kode"], data["nama"], data["kategori"], data["stok"])

    @staticmethod
    def validasi_kode(kode):
        return isinstance(kode, str) and kode.strip() != "" and " " not in kode

    # PERUBAHAN (BARU): menolak nol, negatif, desimal, dan True/False
    @staticmethod
    def _cek_jumlah(n):
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError('Jumlah harus bilangan bulat lebih dari nol!')