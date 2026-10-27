# models/karyawan.py
# Peran: ABSTRACT BASE CLASS. Karyawan tidak bisa dibuat langsung; hanya
# subclass yang mengimplementasikan seluruh abstract method yang bisa dibuat.
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

from abc import ABC, abstractmethod                 # PERUBAHAN: import ABC
from .utils import cek_teks, cek_bulat, rupiah      # PERUBAHAN: import helper


class Karyawan(ABC):                                # PERUBAHAN: mewarisi ABC
    jumlah_karyawan = 0
    _nip_terpakai = set()                           # PERUBAHAN: menyimpan NIP yang sudah dipakai

    def __init__(self, nip, nama, divisi, gaji_pokok):

        if not Karyawan.validasi_nip(nip):
            raise ValueError('Format nip tidak valid!')
        if nip in Karyawan._nip_terpakai:                                   # PERUBAHAN
            raise ValueError(f'NIP {nip} sudah dipakai karyawan lain!')     # PERUBAHAN

        self.nip = nip
        self.nama = cek_teks(nama, 'Nama karyawan')         # PERUBAHAN: divalidasi
        self.__divisi = ''
        self.divisi = divisi
        self._gaji_pokok = 0                                # protected
        self.gaji_pokok = gaji_pokok

        Karyawan._nip_terpakai.add(nip)                     # PERUBAHAN
        Karyawan.jumlah_karyawan += 1

    @property
    def divisi(self):
        return self.__divisi

    @divisi.setter
    def divisi(self, divisi_baru):
        self.__divisi = cek_teks(divisi_baru, 'Divisi')     # PERUBAHAN: pakai helper

    @property
    def gaji_pokok(self):
        return self._gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, gaji_pokok_baru):
        self._gaji_pokok = cek_bulat(gaji_pokok_baru, 'Gaji pokok')   # PERUBAHAN: pakai helper

    # PERUBAHAN: sebelumnya method biasa. Sekarang ABSTRACT, wajib di-override subclass
    @abstractmethod
    def hitung_gaji(self):
        pass

    @abstractmethod
    def info(self):
        pass

    # PERUBAHAN (BARU) - method konkret yang dipakai bersama oleh semua subclass
    def cetak_slip_gaji(self):
        self.info()                                         # info() milik subclass masing-masing
        print(f'   Gaji pokok: {rupiah(self._gaji_pokok)} | Total gaji: {rupiah(self.hitung_gaji())}')

    # PERUBAHAN (BARU) - bagian info yang sama untuk semua subclass
    def _info_dasar(self):
        return f'{self.nip} {self.nama} - Divisi {self.__divisi}'

    # PERUBAHAN (BARU) - operator overloading: bandingkan karyawan lewat total gaji (dipakai sorted())
    def __lt__(self, lain):
        return self.hitung_gaji() < lain.hitung_gaji()

    @classmethod
    def tampilkan_total(cls):
        print(f'Total jumlah karyawan: {cls.jumlah_karyawan}')

    # PERUBAHAN: dari_dict() DIHAPUS dari sini (kelas abstrak tidak bisa dibuat);
    # tiap subclass punya dari_dict() sendiri.

    @staticmethod
    def validasi_nip(nip):
        return isinstance(nip, str) and nip.strip() != "" and " " not in nip