# models/magang.py
# Peran: subclass Karyawan ke-3. Seluruh isi file ini BARU (tidak ada di posttest 2).
# SOLID - OCP (Open/Closed): kelas ini ditambahkan tanpa mengubah Karyawan,
# Ruangan, maupun loop penggajian di file utama.

from .karyawan import Karyawan
from .utils import cek_bulat


class Magang(Karyawan):
    def __init__(self, nip, nama, divisi, gaji_pokok, durasi_bulan):
        self.durasi_bulan = durasi_bulan
        super().__init__(nip, nama, divisi, gaji_pokok)

    @property
    def durasi_bulan(self):
        return self.__durasi_bulan

    @durasi_bulan.setter
    def durasi_bulan(self, bulan):
        if cek_bulat(bulan, 'Durasi magang') == 0:
            raise ValueError('Durasi magang minimal 1 bulan!')
        self.__durasi_bulan = bulan

    def hitung_gaji(self):
        # anak magang hanya menerima gaji pokok (uang saku)
        return self._gaji_pokok

    def info(self):
        print(f'{self._info_dasar()} - Magang {self.__durasi_bulan} bulan')