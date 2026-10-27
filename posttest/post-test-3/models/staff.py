# models/staff.py
# Peran: subclass Karyawan. Meng-override hitung_gaji() dan info() (abstract method).
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

from .karyawan import Karyawan                      # PERUBAHAN: import dari file lain
from .utils import cek_bulat                        # PERUBAHAN


class Staff(Karyawan):
    TARIF_LEMBUR = 20000

    def __init__(self, nip, nama, divisi, gaji_pokok, jam_lembur):
        # PERUBAHAN: atribut unik divalidasi dulu supaya NIP tidak terdaftar
        # jika jam lembur salah (NIP baru dicatat di akhir Karyawan.__init__)
        self.jam_lembur = jam_lembur
        super().__init__(nip, nama, divisi, gaji_pokok)

    # PERUBAHAN (BARU): jam_lembur jadi private + property agar bisa divalidasi
    @property
    def jam_lembur(self):
        return self.__jam_lembur

    @jam_lembur.setter
    def jam_lembur(self, jam):
        self.__jam_lembur = cek_bulat(jam, 'Jam lembur')

    def hitung_gaji(self):
        return self._gaji_pokok + (self.__jam_lembur * Staff.TARIF_LEMBUR)

    def info(self):
        # PERUBAHAN: memakai _info_dasar() dari Karyawan, format output berubah
        print(f'{self._info_dasar()} - Staff, lembur {self.__jam_lembur} jam')

    @classmethod
    def dari_dict(cls, data):
        return cls(data['nip'], data['nama'], data['divisi'],
            data['gaji_pokok'], data['jam_lembur'])