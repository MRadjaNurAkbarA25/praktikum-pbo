# models/riwayat_stok.py
# PERUBAHAN dari posttest 2: TIDAK ADA. Kelas dipindah apa adanya ke file sendiri.
# Peran: bagian "Komposisi" -> objek ini dibuat dan dimiliki oleh BarangInventaris.


class RiwayatStok:
    def __init__(self):
        self.__catatan = []                # ◄◄ private

    def catat(self, aksi, jumlah):
        self.__catatan.append(f'{aksi} {jumlah}')

    def tampilkan(self):
        for c in self.__catatan:
            print(' -', c)