# models/__init__.py
# 1. Keberadaan file ini menjadikan folder `models` sebuah package Python.
# 2. Semua kelas dikumpulkan di sini, jadi file utama cukup menulis:
#        from models import Staff, Ruangan, rupiah
#    tanpa perlu tahu kelas itu ada di file yang mana.

from .utils import rupiah
from .riwayat_stok import RiwayatStok
from .barang_inventaris import BarangInventaris
from .karyawan import Karyawan
from .staff import Staff
from .manager import Manager
from .magang import Magang
from .ruangan import Ruangan

# daftar nama yang ikut ter-import jika memakai: from models import *
__all__ = [
    'rupiah',
    'RiwayatStok',
    'BarangInventaris',
    'Karyawan',
    'Staff',
    'Manager',
    'Magang',
    'Ruangan',
]