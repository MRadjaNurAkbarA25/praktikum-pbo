Posttest 2 Pemrograman Berorientasi Ojek
Nama  : Muhamad Radja Nur Akbar
NIM   : 2509106012
Kelas : Informatika A'25

Posttest 2 : Penerapan UML dan Inheritance pada Tema Posttest Terakhir

A. Penerapan UML
  UML (Unified Modeling Language) adalah bahasa pemodelan standar visual yang digunakan untuk merancang, mendokumentasikan, dan memvisualisasikan sistem perangkat lunak berorientasi objek. UML class relationships adalah cara standar dalam UML Class Diagram untuk menggambarkan hubungan antar kelas menggunakan simbol dan garis tertentu. Dalam program ini diterapkan 3 jenis hubungan antar kelas, yakni:
  
1. Asosiasi, adalah hubungan yang paling longgar antar kelas. Objek A mengenal atau menggunakan objek B, tetapi keduanya tetap hidup secara independen.
   Asosiasi diterapkan pada kelas Ruangan, yang memiliki atribut private __penanggung_jawab. Nilai atribut ini diisi lewat setter penanggung_jawab, yang hanya menerima objek Karyawan (termasuk subclass-nya). Dengan begitu, Ruangan menyimpan referensi ke satu Karyawan sebagai penanggung jawab, tanpa membuat atau memiliki objek tersebut.

class Ruangan:
    def __init__(self, kode_ruangan, nama, lantai, penanggung_jawab):
        ...
        self.__penanggung_jawab = None
        self.penanggung_jawab = penanggung_jawab      # karyawan diterima dari luar

    @property
    def penanggung_jawab(self):
        return self.__penanggung_jawab

    @penanggung_jawab.setter
    def penanggung_jawab(self, nilai):
        if not isinstance(nilai, Karyawan):           # wajib objek Karyawan
            raise ValueError('Penanggung jawab harus objek Karyawan')
        self.__penanggung_jawab = nilai               # simpan referensinya

Objek Karyawan dibuat di luar kelas Ruangan, lalu dikirim lewat parameter. Satu objek Karyawan dapat menjadi penanggung jawab lebih dari satu Ruangan. Jika r1 dihapus, k1 tetap ada karena keberadaannya tidak bergantung pada ruangan.

k1 = Karyawan('K001', 'Adi', 'Sekretaris', 6000000)
...
r1 = Ruangan('R001', 'Ruang IT', 3, k1)

2. Agregasi, adalah hubungan kepemilikan yang lebih kuat dari asosiasi, namun siklus hidup objek bagian tetap mandiri. Hubungan ini "memiliki" antara keseluruhan (whole) dan bagian (part), di mana bagian tetap dapat hidup secara independen walaupun keseluruhannya dihapus.
   Agregasi diterapkan pada kelas Ruangan, yang memiliki atribut daftar_barang berupa list untuk menampung kumpulan objek BarangInventaris. Objek barang ditambahkan lewat method tambah_barang(), yang hanya menerima objek BarangInventaris dan menolak barang yang sudah ada di ruangan tersebut. Dengan begitu, Ruangan berperan sebagai wadah yang berisi barang-barang, tanpa membuat objek barangnya sendiri.

class Ruangan:
    def __init__(self, kode_ruangan, nama, lantai, penanggung_jawab):
        ...
        self.daftar_barang = []                       # wadah kumpulan barang

    def tambah_barang(self, barang):
        if not isinstance(barang, BarangInventaris):  # wajib objek BarangInventaris
            raise ValueError('Barang harus berupa objek BarangInventaris!')
        elif barang in self.daftar_barang:
            raise ValueError(f'{barang.nama} sudah ada di ruangan ini!')
        self.daftar_barang.append(barang)             # simpan referensinya

    def total_stok(self):
        return sum(barang.stok for barang in self.daftar_barang)

Objek BarangInventaris dibuat di luar kelas Ruangan, lalu dimasukkan lewat tambah_barang(). Satu objek barang dapat berada di lebih dari satu ruangan, dan jika ruangan dihapus, objek barang tetap ada.

b1 = BarangInventaris('BRG001', 'Laptop', 'Elektronik', 10)
...
r1.tambah_barang(b1)
r2.tambah_barang(b1)    # b1 yang sama berada di dua ruangan

3. Komposisi, adalah bentuk hubungan paling erat. Objek bagian tidak dapat berdiri sendiri tanpa objek induknya. Untuk menerapkan komposisi, dibuat kelas baru bernama RiwayatStok, kelas ini mencatat semua riwayat perubahan stok pada BarangInventaris, riwayat tersebut disimpan di sebuah list yang dibuat pada kelas RiwayatStok.
   Kelas ini memiliki dua method instance yaitu catat() untuk menambah catatan riwayat ke dalam list menggunakan .append() dan method tampilkan yang menggunakan perulangan for untuk menampilkan isi list catatan.
   Komposisi diterapkan pada kelas BarangInventaris yang memiliki objek RiwayatStok untuk mencatat setiap perubahan stok. Objek RiwayatStok dibuat langsung di dalam __init__ milik BarangInventaris, bukan diterima dari parameter, dan disimpan sebagai atribut private __riwayat. Perubahan stok melalui tambah_stok() dan kurangi_stok() dicatat otomatis oleh barang itu sendiri.

class RiwayatStok:
    def __init__(self):
        self.__catatan = []

    def catat(self, aksi, jumlah):
        self.__catatan.append(f'{aksi} {jumlah}')

    def tampilkan(self):
        for c in self.__catatan:
            print(' -', c)


class BarangInventaris:
    def __init__(self, kode, nama, kategori, stok):
        ...
        self.__riwayat = RiwayatStok()                # dibuat di dalam, bukan dari parameter

    def tambah_stok(self, n):
        ...
        self.__stok += n
        self.__riwayat.catat('tambah', n)

    def kurangi_stok(self, n):
        ...
        self.__stok -= n
        self.__riwayat.catat('kurang', n)

    def tampilkan_riwayat(self):
        print(f'Riwayat stok {self.nama}:')
        self.__riwayat.tampilkan()

Objek RiwayatStok tidak dapat diakses dari luar karena bersifat private dan tidak disediakan getter yang mengembalikan objeknya. Akibatnya, riwayat hanya dimiliki oleh satu barang dan tidak dapat dibagikan ke barang lain. Riwayat hanya dapat dilihat lewat method tampilkan_riwayat(). Berbeda dengan agregasi, objek bagian pada komposisi dibuat oleh objek induknya sendiri dan tidak dapat digunakan oleh objek lain.

B. Penerapan Inheritance
  Inheritance merupakan mekanisme di mana sebuah kelas baru (subclass) mewarisi atribut dan method dari kelas yang sudah ada (superclass). Subclass tidak perlu menulis ulang apa yang sudah dimiliki superclass, dan hanya menambahkan atau mengubah hal yang membedakannya. 
  Untuk memudahkan penerapan Inheritance, pada kelas Karyawan ditambah atribut baru yaitu _gaji_pokok bersifat atribut protected, diisi melalui setter gaji_pokok. Kemudian method baru hitung_gaji() yang mengembalikan nilai gaji_pokok.

class Karyawan:
    jumlah_karyawan = 0
    
    def __init__(self, nip, nama, divisi, gaji_pokok):
        
        ...
        self.gaji_pokok = gaji_pokok

    ...
    @property
    def gaji_pokok(self):
        return self._gaji_pokok
    
    @gaji_pokok.setter
    def gaji_pokok(self, gaji_pokok_baru):
        if not isinstance(gaji_pokok_baru, int) or gaji_pokok_baru < 0:
            raise ValueError("Gaji harus bilangan bulat!")
        self._gaji_pokok = gaji_pokok_baru
    
    def hitung_gaji(self):
        return self._gaji_pokok

Sekarang beralih ke subclass atau child class dari Karyawan. Terdapat dua subclass dari Karyawan yaitu Staff dan Manager.

1. Subclass Staff
  Subclass Staff memiliki semua atribut yang dimiliki parent-nya dengan tambahan atribut unik yaitu jam_lembur. Atribut ini dan atribut kelas TARIF_LEMBUR akan digunakan untuk menghitung gaji_pokok Staff. Konstruktor milik superclass (Karyawan) dipanggil menggunakan super() sehingga subclass hanya perlu mengisi atribut miliknya yakni jam_lembur.
  Subclass Staff juga memiliki 3 method yang didefinisikan ulang dengan nama dan parameter yang sama seperti pada superclass-nya, method ini disebut method overriding. Meski begitu, logika dan perilakunya berbeda. Pada Staff, method hitung_gaji() untuk menghitung gaji memiliki operasi gaji_pokok + (jam_lembur x TARIF_LEMBUR), membedakannya dari superclass dan subclass lain. Sementara method info() dan dari_dict() kurang lebih sama, perbedaan berada di penambahan atribut khusus subclass Staff.

class Staff(Karyawan):
    TARIF_LEMBUR = 20000
    
    def __init__(self, nip, nama, divisi, gaji_pokok, jam_lembur):
        super().__init__(nip, nama, divisi, gaji_pokok)
        self.jam_lembur = jam_lembur
    
    def hitung_gaji(self):
        return self._gaji_pokok + (self.jam_lembur * Staff.TARIF_LEMBUR)

    def info(self):
        print(f'{self.nip} {self.nama} - Divisi {self.divisi} - Jam lembur {self.jam_lembur} jam')
   
    @classmethod
    def dari_dict(cls, data):               
        return cls(data['nip'], data['nama'], data['divisi'],
            data['gaji_pokok'], data['jam_lembur'])

2. Subclass Manager
  Subclass Manager juga merupakan subclass dari Karyawan. Menggunakan super() untuk memanggil konstruktor miliki superclass-nya, subclass ini memiliki atribut unik yaitu tunjangan_jabatan, atribut ini dibuat sebagai atribut protected yang diisi melalui setter tunjangan_jabatan. Untuk method overriding hitung_gaji(), gaji_pokok ditambah dengan tunjangan_jabatan sementara method overriding lain (info() dan dari_dict()) cukup menambah atribut tunjangan_gaji pada isinya.

class Manager(Karyawan):
    def __init__(self, nip, nama, divisi, gaji_pokok, tunjangan_jabatan):
        super().__init__(nip, nama, divisi, gaji_pokok)
        self.__tunjangan_jabatan = 0
        self.tunjangan_jabatan = tunjangan_jabatan
    
    @property
    def tunjangan_jabatan(self):
        return self.__tunjangan_jabatan
        
    @tunjangan_jabatan.setter
    def tunjangan_jabatan(self, nilai):
        if not isinstance(nilai, int) or nilai < 0:
            raise ValueError('Tunjangan harus bilangan bulat!')
        self.__tunjangan_jabatan = nilai
    
    def hitung_gaji(self):
        return self.gaji_pokok + self.__tunjangan_jabatan
        
    def info(self):
        print(f'{self.nip} {self.nama} - Divisi {self.divisi} - Tunjangan jabatan: Rp.{self.__tunjangan_jabatan}')
        
    @classmethod
    def dari_dict(cls, data):
        return cls(data['nip'], data['nama'], data['divisi'],
            data['gaji_pokok'], data['tunjangan_jabatan'])
