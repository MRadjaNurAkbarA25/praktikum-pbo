# models/manager.py
# Peran: subclass Karyawan. Meng-override hitung_gaji() dan info() (abstract method).
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

from .karyawan import Karyawan                      # PERUBAHAN: import dari file lain
from .utils import cek_bulat, rupiah                # PERUBAHAN


class Manager(Karyawan):
    def __init__(self, nip, nama, divisi, gaji_pokok, tunjangan_jabatan):
        # PERUBAHAN: atribut unik divalidasi dulu sebelum super().__init__()
        # (baris "self.__tunjangan_jabatan = 0" di versi lama tidak diperlukan lagi)
        self.tunjangan_jabatan = tunjangan_jabatan
        super().__init__(nip, nama, divisi, gaji_pokok)

    @property
    def tunjangan_jabatan(self):
        return self.__tunjangan_jabatan

    @tunjangan_jabatan.setter
    def tunjangan_jabatan(self, nilai):
        self.__tunjangan_jabatan = cek_bulat(nilai, 'Tunjangan')    # PERUBAHAN: pakai helper

    def hitung_gaji(self):
        return self._gaji_pokok + self.__tunjangan_jabatan          # PERUBAHAN: pakai _gaji_pokok (protected)

    def info(self):
        # PERUBAHAN: memakai _info_dasar() dan rupiah(), format output berubah
        print(f'{self._info_dasar()} - Manager, tunjangan {rupiah(self.__tunjangan_jabatan)}')

    @classmethod
    def dari_dict(cls, data):
        return cls(data['nip'], data['nama'], data['divisi'],
            data['gaji_pokok'], data['tunjangan_jabatan'])