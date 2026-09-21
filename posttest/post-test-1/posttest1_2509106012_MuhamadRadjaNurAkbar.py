import os

os.system('cls || clear')

class BarangInventaris:
    # atr class
    jumlah_barang = 0
    
    def __init__(self, kode, nama, kategori, stok):
        
        # validasi format kode sebagai identitas unik 
        if not BarangInventaris.validasi_kode(kode):
            raise ValueError ('Format kode tidak valid!')
        
        # instance public
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        
        # private
        self.__stok = 0
        self.stok = stok
        
        BarangInventaris.jumlah_barang += 1
    
    # getter
    @property
    def stok(self):
        return self.__stok
    
    # setter
    @stok.setter
    def stok(self, stok_baru):
        if not isinstance(stok_baru, int) or stok_baru < 0:
            raise ValueError("Stok harus bilangan bulat!")
        self.__stok = stok_baru

    # method instance
    def tambah_stok(self, n):
        if n <= 0:
            raise ValueError('Nilai harus lebih dari nol!')
        else:
            self.__stok += n

    def kurangi_stok(self, n):
        if n <= 0:
            raise ValueError("Nilai harus lebih dari nol!")
        if n > self.__stok:
            raise ValueError(f'Stok {self.nama} tidak cukup!')
        else:
            self.__stok -= n
    
    def info(self):
        print(f'[{self.kode}] {self.nama} {self.kategori} - Stok : {self.__stok}')
    
    @classmethod
    def tampilkan_total(cls):
        print(f'Total jenis barang: {cls.jumlah_barang}')
        
    @classmethod
    def dari_dict(cls, data):
        return cls(data["kode"], data["nama"], data["kategori"], data["stok"])
    
    @staticmethod
    def validasi_kode(kode):
        return isinstance(kode, str) and kode.strip() != "" and " " not in kode


class Karyawan:
    jumlah_karyawan = 0
    
    def __init__(self, nip, nama, divisi):
        
        if not Karyawan.validasi_nip(nip):
            raise ValueError ('Format nip tidak valid!')
        
        self.nip = nip
        self.nama = nama
        self.__divisi = ''
        self.divisi = divisi
    
        Karyawan.jumlah_karyawan += 1
    
    @property
    def divisi(self):
        return self.__divisi
    
    @divisi.setter
    def divisi(self, divisi_baru):
        if not isinstance(divisi_baru, str) or divisi_baru.strip() == "":
            raise ValueError('Divisi tidak boleh kosong!')
        self.__divisi = divisi_baru
    
    def info(self):
        print(f'{self.nip} {self.nama} - Divisi {self.__divisi}')
    
    @classmethod
    def tampilkan_total(cls):
        print(f'Total jumlah karyawan: {cls.jumlah_karyawan}')
    
    @classmethod
    def dari_dict(cls, data):
        return cls(data['nip'], data['nama'], data['divisi'])
    
    @staticmethod
    def validasi_nip(nip):
        return isinstance(nip, str) and nip.strip() != "" and " " not in nip
        
class Ruangan:
    # atr class
    jumlah_ruangan = 0
    
    def __init__(self, kode_ruangan, nama, lantai, penanggung_jawab):
        
        if not Ruangan.validasi_kode(kode_ruangan):
            raise ValueError ('Format kode tidak valid!')
                
        self.kode = kode_ruangan
        self.nama = nama
        self.lantai = lantai
        self.__penanggung_jawab = None
        self.penanggung_jawab = penanggung_jawab
        
        self.daftar_barang = []
        
        Ruangan.jumlah_ruangan += 1
        
    @property
    def penanggung_jawab(self):
        return self.__penanggung_jawab
    
    @penanggung_jawab.setter
    def penanggung_jawab(self, nilai):
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
            f"Barang: {nama_barang}"
        )    
    @classmethod
    def tampilkan_total(cls):
        print(f'Total ruangan: {cls.jumlah_ruangan}')
        
    @staticmethod
    def validasi_kode(kode):
        return isinstance(kode, str) and kode.strip() != "" and " " not in kode


# objek barang inventaris
print('===== BARANG INVENTARIS ===')
b1 = BarangInventaris('BRG001', 'Laptop', 'Elektronik', 10)
b2 = BarangInventaris.dari_dict(
    {'kode': 'BRG002', 'nama': 'Meja', 'kategori': 'Furnitur', 'stok': 12}
)

print('Data awal')
b1.info()
b2.info()
BarangInventaris.tampilkan_total()

print('\n')

print('Data setelah pengurangan dan penambahan stok')
b1.kurangi_stok(3)
b1.tambah_stok(2)
b1.info()
b2.info()

print('\n')

print('Mengatur stok baru di setter')
b1.stok = 8
print('Stok baru laptop: ', b1.stok)

print('\n')

print('Validasi nilai negatif pada method private')
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

print('\n')

print('Validasi format kode barang')
print('Kode = BRG003 ->', BarangInventaris.validasi_kode('BRG003'))
print('Kode = BRG 003 ->', BarangInventaris.validasi_kode('BRG 003'))

# objek karyawan
print('\n')

print('===== KARYAWAN =====')
k1 = Karyawan('K001', 'Adi', 'Sekretaris')
k2 = Karyawan.dari_dict(
    {'nip': 'K002', 'nama': 'Lisa', 'divisi': 'Keuangan'}
)

print('Data awal')
k1.info()
k2.info()
Karyawan.tampilkan_total()

print('\n')

print('Mengubah divisi')
k1.divisi = 'IT'
print(f'Divisi baru {k1.nama}: {k1.divisi}')

print('\n')

print('Mengosongkan divisi')
try:
    k1.divisi = '   '
except ValueError as e:
    print('Ditolak', e)

print('\n')

print('Mencoba validasi format NIP karyawan')
print('NIP = K003 -->', Karyawan.validasi_nip("K003"))   # True
print('NIP = 123 -->', Karyawan.validasi_nip(123))

# objek ruangan
print('\n')

print('===== RUANGAN =====')
r1 = Ruangan('R001', 'Ruang IT', 3, k1)
r2 = Ruangan('R002', 'Ruang Keuangan', 1, k2)

print('Data awal')
r1.info()
r2.info()
Ruangan.tampilkan_total()

print('\n')

print('Menambah barang ke ruangan')
r1.tambah_barang(b1)
r2.tambah_barang(b2)
r2.tambah_barang(b1)
r1.info()
r2.info()
print('Total stok', r1.nama, ':', r1.total_stok())
print('Total stok', r2.nama, ':', r2.total_stok())

print('\n')

print('Mengganti penanggung jawab')
r1.penanggung_jawab = k2
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
    
print('\n')

print('Validasi format kode ruangan')
print('Kode = R003 ->', Ruangan.validasi_kode('R003'))
print('Kode = R 003 ->', Ruangan.validasi_kode('R 003'))