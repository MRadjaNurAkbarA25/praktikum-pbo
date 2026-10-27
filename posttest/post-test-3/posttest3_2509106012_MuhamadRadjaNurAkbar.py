# File utama: hanya berisi demo/pemanggilan. Semua kelas ada di folder models/
# Jalankan dari folder ini:  python posttest3_2509106012_MuhamadRadjaNurAkbar.py
# Baris bertanda "# PERUBAHAN" = berbeda dari posttest 2.

import os
from models import (                                # PERUBAHAN: kelas diimpor dari package models
    BarangInventaris, Karyawan, Staff, Manager, Magang, Ruangan, rupiah
)

os.system('cls || clear')


# PERUBAHAN (BARU) - duck typing: tidak peduli kelasnya, yang penting objek punya method info()
def tampilkan_info(objek):
    objek.info()


# objek barang inventaris
print('===== BARANG INVENTARIS =====')                # PERUBAHAN: typo '===' diperbaiki
b1 = BarangInventaris('BRG001', 'Laptop', 'Elektronik', 10)
b2 = BarangInventaris.dari_dict(
    {'kode': 'BRG002', 'nama': 'Meja', 'kategori': 'Furnitur', 'stok': 12}
)

print('Riwayat')
b1.tambah_stok(3)
b1.kurangi_stok(1)
b1.tampilkan_riwayat()

print()                                              # PERUBAHAN: print('\n') -> print()

print('Data awal')
b1.info()
b2.info()
BarangInventaris.tampilkan_total()

print()

print('Data setelah pengurangan dan penambahan stok')
b1.kurangi_stok(3)
b1.tambah_stok(2)
b1.info()
b2.info()

print()

print('Mengatur stok baru di setter')
b1.stok = 8
print('Stok baru laptop:', b1.stok)

print()

print('Validasi nilai negatif pada setter')           # PERUBAHAN: 'method private' -> 'setter'
try:
    b1.stok = -5
except ValueError as e:
    print('Ditolak:', e)

print('Validasi nilai pengurangan stok lebih banyak dari stok saat ini')
try:
    b1.kurangi_stok(12)
except ValueError as e:
    print('Ditolak:', e)

print('Validasi nilai menambah stok')
try:
    b1.tambah_stok(0)
except ValueError as e:
    print('Ditolak:', e)

# PERUBAHAN (BARU): dua validasi baru
print('Validasi menambah stok dengan bilangan desimal')
try:
    b1.tambah_stok(2.5)
except ValueError as e:
    print('Ditolak:', e)

print('Validasi kode barang yang sudah dipakai')
try:
    BarangInventaris('BRG001', 'Printer', 'Elektronik', 2)
except ValueError as e:
    print('Ditolak:', e)

print()

print('Validasi format kode barang')
print('Kode = BRG003 ->', BarangInventaris.validasi_kode('BRG003'))
print('Kode = BRG 003 ->', BarangInventaris.validasi_kode('BRG 003'))

# objek karyawan
print()

print('===== KARYAWAN =====')

# PERUBAHAN (BARU) - bukti abstraksi: abstract class tidak bisa diinstansiasi
print('Bukti abstract class tidak bisa diinstansiasi')
try:
    Karyawan('K000', 'Tes', 'Umum', 1000000)
except TypeError as e:
    print('Ditolak:', e)

print()

# PERUBAHAN: k1 dan k2 dulu objek Karyawan, sekarang Staff dan Manager
k1 = Staff('K001', 'Adi', 'Sekretaris', 6000000, 5)
k2 = Manager.dari_dict(
    {'nip': 'K002', 'nama': 'Lisa', 'divisi': 'Keuangan', 'gaji_pokok': 6000000, 'tunjangan_jabatan': 1000000}
)

print('Role Staff')
s1 = Staff('S001', 'Memet', 'IT', 5000000, 10)
s1.info()
print(f'Gaji : {rupiah(s1.hitung_gaji())}')             # PERUBAHAN: dibungkus rupiah()
print(f'Gaji pokok : {rupiah(s1.gaji_pokok)}')          # PERUBAHAN: dibungkus rupiah()
                                                       # PERUBAHAN: s1.info() kedua dihapus

print()

print('Role Manager')
m1 = Manager('M001', 'Rina', 'IT', 8000000, 1500000)
m1.info()
print(f'Gaji : {rupiah(m1.hitung_gaji())}')
print(f'Gaji pokok : {rupiah(m1.gaji_pokok)}')

m2 = Manager.dari_dict(
    {'nip': 'M002', 'nama': 'Lucy', 'divisi': 'Marketing', 'gaji_pokok': 5000000, 'tunjangan_jabatan': 50000}
)
m2.info()
print(f'Gaji : {rupiah(m2.hitung_gaji())}')

print()

# PERUBAHAN (BARU): subclass ke-3
print('Role Magang')
g1 = Magang('G001', 'Budi', 'IT', 2000000, 3)
g1.info()
print(f'Gaji : {rupiah(g1.hitung_gaji())}')

print()

# PERUBAHAN (BARU) - polimorfisme via pewarisan: satu loop, objek dari subclass berbeda
print('Polimorfisme: slip gaji semua karyawan lewat satu loop')
daftar_karyawan = [k1, k2, s1, m1, m2, g1]
for karyawan in daftar_karyawan:
    karyawan.cetak_slip_gaji()

print()

# PERUBAHAN (BARU) - operator overloading __lt__
print('Operator overloading __lt__: urutan karyawan dari gaji terkecil')
for karyawan in sorted(daftar_karyawan):
    print(f' - {karyawan.nama}: {rupiah(karyawan.hitung_gaji())}')
print('Gaji Memet < gaji Rina ->', s1 < m1)

print()

print('Data awal')
k1.info()
k2.info()
Karyawan.tampilkan_total()

print()

print('Mengubah divisi')
k1.divisi = 'IT'
print(f'Divisi baru {k1.nama}: {k1.divisi}')

print()

print('Mengosongkan divisi')
try:
    k1.divisi = '   '
except ValueError as e:
    print('Ditolak:', e)                                # PERUBAHAN: 'Ditolak' -> 'Ditolak:'

# PERUBAHAN (BARU): dua validasi baru
print('Validasi jam lembur negatif')
try:
    Staff('S002', 'Joko', 'IT', 5000000, -100)
except ValueError as e:
    print('Ditolak:', e)

print('Validasi NIP yang sudah dipakai')
try:
    Manager('M001', 'Dewi', 'HRD', 7000000, 1000000)
except ValueError as e:
    print('Ditolak:', e)

print()

print('Mencoba validasi format NIP karyawan')
print('NIP = K003 -->', Karyawan.validasi_nip("K003"))   # True
print('NIP = 123 -->', Karyawan.validasi_nip(123))

# objek ruangan
print()

print('===== RUANGAN =====')
r1 = Ruangan('R001', 'Ruang IT', 3, k1)
r2 = Ruangan('R002', 'Ruang Keuangan', 1, k2)

print('Data awal')
r1.info()
r2.info()
Ruangan.tampilkan_total()

print()

print('Menambah barang ke ruangan')
r1.tambah_barang(b1)
r2.tambah_barang(b2)
r2.tambah_barang(b1)
r1.info()
r2.info()
print('Total stok', r1.nama, ':', r1.total_stok())
print('Total stok', r2.nama, ':', r2.total_stok())
print(f'Jumlah jenis barang di {r2.nama} (len): {len(r2)}')    # PERUBAHAN (BARU): memakai __len__

print()

# PERUBAHAN: penanggung jawab diganti ke g1 (Magang), bukan k2
print('Mengganti penanggung jawab (Magang juga diterima karena turunan Karyawan)')
r1.penanggung_jawab = g1
print(f'Penanggung jawab baru {r1.nama}: {r1.penanggung_jawab.nama}')

print('Validasi penanggung jawab bukan objek Karyawan')
try:
    r1.penanggung_jawab = 'Budi'
except ValueError as e:
    print('Ditolak:', e)

print('Validasi barang bukan objek BarangInventaris')
try:
    r1.tambah_barang('Kursi')
except ValueError as e:
    print('Ditolak:', e)

print('Validasi barang yang sudah ada di ruangan')
try:
    r1.tambah_barang(b1)
except ValueError as e:
    print('Ditolak:', e)

print('Validasi membuat ruangan dengan penanggung jawab teks')
try:
    Ruangan('R003', 'Ruang Uji', 1, 'Budi')
except ValueError as e:
    print('Ditolak:', e)

print()

print('Validasi format kode ruangan')
print('Kode = R003 ->', Ruangan.validasi_kode('R003'))
print('Kode = R 003 ->', Ruangan.validasi_kode('R 003'))

print()

# PERUBAHAN (BARU) - duck typing: satu fungsi untuk kelas yang tidak berhubungan lewat pewarisan
print('===== DUCK TYPING =====')
print('Satu fungsi tampilkan_info() untuk objek dari kelas yang tidak berhubungan')
for objek in [b2, r2, m1]:
    tampilkan_info(objek)
    
print()

# PERUBAHAN (BARU) - bukti penerapan SOLID
print('===== SOLID =====')
print('OCP: Magang ditambahkan tanpa mengubah Karyawan, Ruangan, dan loop gaji')
total = sum(k.hitung_gaji() for k in daftar_karyawan)
print(f'Total gaji semua karyawan (termasuk Magang): {rupiah(total)}')
print(f'DIP: penanggung jawab {r1.nama} adalah {r1.penanggung_jawab.nama}, diterima lewat abstraksi Karyawan')