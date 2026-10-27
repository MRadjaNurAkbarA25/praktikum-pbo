Posttest 3 Pemrograman Berorientasi Objek
Nama    : Muhamad Radja Nur Akbar
NIM     : 2509106012
Kelas   : A1'25

Posttest 3: Polimorfisme, Abstraksi, dan SOLID

  Pada posttest ketiga ini, pilar polimorfisme dan abstraksi serta salah satu prinsip SOLID juga diterapkan pada program inventaris barang. Di posttest ini struktur program dimodularisasikan untuk mempermudah dalam membaca kode dan memahami alurnya. 

posttest/post-test-3/
├── posttest3_2509106012_MuhamadRadjaNurAkbar.py   ← main (program utama / demo)
├── README.md                                       ← laporan
├── images/
│   ├── class_diagram.png
│   └── output_*.png                                ← screenshot output
└── models/
    ├── __init__.py
    ├── utils.py               ← cek_bulat(), cek_teks(), rupiah()
    ├── riwayat_stok.py        ← RiwayatStok
    ├── barang_inventaris.py   ← BarangInventaris
    ├── karyawan.py            ← Karyawan (abstract, ABC)
    ├── staff.py               ← Staff
    ├── manager.py             ← Manager
    ├── magang.py              ← Magang
    └── ruangan.py             ← Ruangan

  Dalam laporan ini, saya akan menjelaskan setiap file, mulai dari yang baru hingga perubahan apa yang ada pada file sejak posttest kedua.

A. File __init__.py
  File ini tidak punya fungsi atau kelas. Tugasnya menjadikan folder models sebuah package Python dan mengumpulkan semua kelas, sehingga file utama cukup menulis from models import Staff, Ruangan, rupiah. Pada baris:

from .utils import rupiah

  Titik mengacu pada folder models itu sendiri. Hanya mengimpor rupiah karena fungsi lain pada .utils hanya dipakai di dalam kelas. Sementara itu, baris-baris seterusnya mengimpor kelas-kelas lain. Jika menggunakan asterisks (*) atau mengimpor semua yang ada di models, daftar nama di dalam __all__ akan terikut.

B. File utils.py
  File ini berisi fungsi pembantu, 2 diantara 3 fungsi merupakan fungsi validasi yang dipakai di setiap setter. Jadi tidak perlu menulis validasi yang sama terus-menerus. Fungsi cek_bulat() memastikan suatu nilai merupakan bilangan bulat dan tidak negatif. Digunakan untuk menjaga angka adalah bulat dalam operasi matematika dan lain-lain.

def cek_bulat(nilai, label):
    # bool adalah turunan int (True == 1), jadi ditolak secara eksplisit
    if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai < 0:
        raise ValueError(f'{label} harus bilangan bulat dan tidak boleh negatif!')
    return nilai

  Fungsi cek_teks() memastikan nilai bertipe string, atau jika kosong setelah strip() (spasi di awal dan akhir dibuang, sehingga '   ' ikut ditolak).

def cek_teks(nilai, label):
    if not isinstance(nilai, str) or nilai.strip() == '':
        raise ValueError(f'{label} tidak boleh kosong!')
    return nilai

  Fungsi rupiah() berfungsi untuk memodelkan format uang rupiah. Bagian f'{nilai:,}' memberi pemisah ribuan koma. Bagian .replace mengganti koma menjadi titik yang merupakan gaya pemisah di Indonesia.

def rupiah(nilai):
    return 'Rp' + f'{nilai:,}'.replace(',', '.')

C. File riwayat_stok.py
  Kelas RiwayatStok menyimpan catatan perubahan stok. Isinya sama persis dengan posttest 2, hanya dipindah ke file sendiri. Kelas ini adalah bagian komposisi: objeknya dibuat dan dimiliki oleh BarangInventaris.

  Constructor __init__ ditambahkan tanpa parameter tambahan, karena riwayat selalu dimulai kosong. Pada baris berikutnya, atribut __catatan adalah atribut private berupa list kosong. Method catat() adalah method instance karena menggunakan .self, method ini menambah 1 catatan, dengan aksi berupa menambah atau mengurangi serta jumlah yang dioperasikan. Method tampilkan() menampilkan seluruh isi catatan dengan cara perulangan for, setiap baris diawali '-'.

class RiwayatStok:
    def __init__(self):
        self.__catatan = []                # ◄◄ private

    def catat(self, aksi, jumlah):
        self.__catatan.append(f'{aksi} {jumlah}')

    def tampilkan(self):
        for c in self.__catatan:
            print(' -', c)

D. File barang_inventaris.py
  File ini berisi kelas BarangInventaris. Perubahan yang terjadi sejak posttest kedua adalah sebagai berikut.

  Mengimport fungsi dan method pada .utils.py dan riwayat_stok.py. Membuat atr kelas jumlah_barang dengan nilai awal 0 dan _kode_terpakai dengan nilai adalah set kosong.

  Kode barang harus unik Ditambahkan atribut kelas _kode_terpakai berupa set untuk menyimpan kode yang sudah dipakai. Jika kode yang sama dipakai lagi, program melempar ValueError. Kode baru didaftarkan di akhir constructor, supaya kode hanya tercatat jika semua validasi sudah lolos.

_kode_terpakai = set()

if kode in BarangInventaris._kode_terpakai:
    raise ValueError(f'Kode {kode} sudah dipakai barang lain!')

  Berikutnya mengisi atr instance, atr nama dan kategori divalidasi dengan cek_teks() supaya tidak kosong.

self.nama = cek_teks(nama, 'Nama barang')       
self.kategori = cek_teks(kategori, 'Kategori')

  Urutan __riwayat dan __stok ditukar Pada posttest kedua, urutannya __stok lalu __riwayat. Sekarang __riwayat dibuat lebih dulu. Alasannya, baris self.stok = stok di constructor tidak mengisi atribut secara langsung, tetapi menjalankan setter. Setter stok sekarang memanggil self.__riwayat.catat(), sehingga jika __riwayat belum ada akan terjadi AttributeError. Objek RiwayatStok dibuat di dalam constructor, bukan diterima dari parameter, sehingga relasi komposisi tetap terjaga.

self.__riwayat = RiwayatStok()
self.__stok = 0
self.stok = stok

  Property stok (getter dan setter) Atribut __stok bersifat private sehingga tidak bisa diakses dari luar. Getter dan setter dengan @property menjadi satu-satunya jalan untuk membaca dan mengubahnya, tetapi cara pemakaiannya tetap seperti atribut biasa (b1.stok dan b1.stok = 8). Getter mengembalikan __stok. Setter memvalidasi nilai dengan cek_bulat() lebih dulu, baru kemudian menyimpan dan mencatat 'atur' ke riwayat. Jika nilai salah, ValueError dilempar sebelum penyimpanan dan pencatatan, sehingga stok tidak berubah. Constructor juga memakai setter, jadi stok awal ikut divalidasi.

@property
def stok(self):
    return self.__stok

@stok.setter
def stok(self, stok_baru):
    self.__stok = cek_bulat(stok_baru, 'Stok')
    self.__riwayat.catat('atur', stok_baru)

  Validasi jumlah lewat _cek_jumlah() Method statis _cek_jumlah() dipakai oleh tambah_stok() dan kurangi_stok() untuk menolak nilai nol, negatif, desimal, dan True/False. Pada posttest kedua, nilai desimal seperti 2.5 masih lolos. Digunakan pada method tambah_stok() dan kurangi_stok(). 

@staticmethod
def _cek_jumlah(n):
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError('Jumlah harus bilangan bulat lebih dari nol!')

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

  Operator overloading __str__ Method str() ditambahkan untuk menentukan teks yang tampil ketika objek di-print. Method info() sekarang cukup print(self) yang otomatis memanggil str(), sehingga format teks barang hanya ditulis di satu tempat.

def info(self):
    print(self)

def __str__(self):
    return f'[{self.kode}] {self.nama} ({self.kategori}) - Stok: {self.__stok}'


E.File karyawan.py
  File ini berisi kelas Karyawan yang sekarang menjadi abstract class. Perubahan yang terjadi sejak posttest kedua adalah sebagai berikut.

1. Mewarisi ABC Kelas Karyawan sekarang mewarisi ABC dari modul abc. Selama masih ada abstract method yang belum di-override, Python menolak pembuatan objeknya dengan TypeError.
2. Dua abstract method Method hitung_gaji() dan info() diberi dekorator @abstractmethod. Sebelumnya keduanya method biasa. Isinya hanya pass karena yang menghitung adalah subclass masing-masing, sehingga setiap   subclass wajib mengimplementasikannya.

class Karyawan(ABC):

    @abstractmethod
    def hitung_gaji(self):
        pass

    @abstractmethod
    def info(self):
        pass

3. Method konkret cetak_slip_gaji() Method ini ditulis sekali di Karyawan dan dipakai bersama oleh semua subclass. Di dalamnya, self.info() dan self.hitung_gaji() otomatis memakai versi milik subclass yang sedang dipakai. 

def cetak_slip_gaji(self):
    self.info()
    print(f'   Gaji pokok: {rupiah(self._gaji_pokok)} | Total gaji: {rupiah(self.hitung_gaji())}')

4. Method _info_dasar() Method ini mengembalikan teks nip, nama, dan divisi yang sama untuk semua subclass. Karena __divisi bersifat private, subclass tidak bisa mengaksesnya langsung, sehingga mereka memanggil _info_dasar().
5. Operator overloading __lt__ Method lt() membandingkan dua karyawan berdasarkan hasil hitung_gaji(). Dengan ini, sorted() bisa mengurutkan daftar karyawan tanpa parameter key, dan perbandingan seperti s1 < m1 bisa dipakai.

  def __lt__(self, lain):
    return self.hitung_gaji() < lain.hitung_gaji()

6. Perubahan lainnya NIP harus unik (atribut kelas _nip_terpakai, sama seperti kode pada BarangInventaris). Setter divisi dan gaji_pokok memakai cek_teks() dan cek_bulat(). Method dari_dict() dihapus dari kelas ini karena kelas abstrak tidak bisa dibuat langsung, dan setiap subclass memiliki dari_dict() sendiri.

F. File staff.py
  Kelas Staff adalah subclass dari Karyawan. Atribut uniknya jam_lembur sekarang bersifat private dengan property agar bisa divalidasi. Constructor memanggil super().init() untuk mengisi atribut milik Karyawan, sehingga Staff hanya mengurus atribut miliknya sendiri. Atribut jam_lembur diisi sebelum super().init(). Alasannya, NIP baru dicatat di akhir constructor Karyawan. Jika jam lembur salah dan baru dicek sesudahnya, NIP sudah terlanjur terdaftar padahal objeknya gagal dibuat. Method hitung_gaji() dan info() merupakan hasil override dari abstract method Karyawan. Gaji Staff dihitung dari gaji pokok ditambah jam_lembur dikali TARIF_LEMBUR.

class Staff(Karyawan):
    TARIF_LEMBUR = 20000

    def __init__(self, nip, nama, divisi, gaji_pokok, jam_lembur):
        self.jam_lembur = jam_lembur
        super().__init__(nip, nama, divisi, gaji_pokok)

    def hitung_gaji(self):
        return self._gaji_pokok + (self.__jam_lembur * Staff.TARIF_LEMBUR)

    def info(self):
        print(f'{self._info_dasar()} - Staff, lembur {self.__jam_lembur} jam')

G. File manager.py
  Kelas Manager adalah subclass kedua dari Karyawan. Polanya sama dengan Staff. Atribut uniknya tunjangan_jabatan diisi sebelum super().init() dan divalidasi di setter dengan cek_bulat(). Baris self.__tunjangan_jabatan = 0 dari versi lama tidak diperlukan lagi. Method hitung_gaji() menjumlahkan _gaji_pokok dengan tunjangan jabatan, sedangkan info() mencetak data dasar dan tunjangan dalam format rupiah.

class Manager(Karyawan):
    def __init__(self, nip, nama, divisi, gaji_pokok, tunjangan_jabatan):
        self.tunjangan_jabatan = tunjangan_jabatan
        super().__init__(nip, nama, divisi, gaji_pokok)

    def hitung_gaji(self):
        return self._gaji_pokok + self.__tunjangan_jabatan

    def info(self):
        print(f'{self._info_dasar()} - Manager, tunjangan {rupiah(self.__tunjangan_jabatan)}')

H. File magang.py
  File ini seluruhnya baru. Kelas Magang adalah subclass ketiga dari Karyawan dengan atribut unik durasi_bulan yang bersifat private dan minimal 1 bulan. Anak magang hanya menerima gaji pokok, sehingga hitung_gaji() langsung mengembalikan _gaji_pokok. Kelas ini ditambahkan tanpa mengubah Karyawan, Ruangan, maupun loop penggajian di file utama, dan semuanya tetap berjalan. Hal ini merupakan penerapan prinsip Open/Closed pada SOLID.

class Magang(Karyawan):
    def __init__(self, nip, nama, divisi, gaji_pokok, durasi_bulan):
        self.durasi_bulan = durasi_bulan
        super().__init__(nip, nama, divisi, gaji_pokok)

    @durasi_bulan.setter
    def durasi_bulan(self, bulan):
        if cek_bulat(bulan, 'Durasi magang') == 0:
            raise ValueError('Durasi magang minimal 1 bulan!')
        self.__durasi_bulan = bulan

    def hitung_gaji(self):
        return self._gaji_pokok

    def info(self):
        print(f'{self._info_dasar()} - Magang {self.__durasi_bulan} bulan')

I. File ruangan.py
  Kelas Ruangan memegang dua relasi, yaitu asosiasi ke Karyawan lewat penanggung_jawab dan agregasi ke BarangInventaris lewat daftar_barang. Kedua relasi itu tidak berubah sejak posttest kedua. Perubahan yang terjadi adalah sebagai berikut.
1. Kode ruangan harus unik (_kode_terpakai), nama divalidasi dengan cek_teks(), dan lantai divalidasi dengan cek_bulat().
2. Setter penanggung_jawab memeriksa isinya dengan isinstance(nilai, Karyawan), yaitu kelas abstrak, bukan Staff atau Manager. Dengan begitu semua subclass diterima, termasuk Magang yang ditambahkan belakangan.
3. Operator overloading len() ditambahkan sehingga len(ruangan) mengembalikan jumlah jenis barang di dalam ruangan. Method info() memakainya untuk menampilkan jumlah barang.

@penanggung_jawab.setter
def penanggung_jawab(self, nilai):
    if not isinstance(nilai, Karyawan):
        raise ValueError('Penanggung jawab harus objek Karyawan')
    self.__penanggung_jawab = nilai

def __len__(self):
    return len(self.daftar_barang)

J. File utama
  File utama tidak mendefinisikan kelas. Isinya hanya mengimpor kelas dari package models, membuat objek, dan memanggil method untuk mendemonstrasikan semua konsep. Bagian baru dibanding posttest kedua adalah:

  - fungsi tampilkan_info() untuk duck typing,
  - pembuktian bahwa abstract class Karyawan tidak bisa diinstansiasi,
  - objek k1 dan k2 yang sekarang berupa Staff dan Manager karena Karyawan tidak bisa dibuat langsung,
  - pembuatan objek Magang,
  - loop slip gaji untuk polimorfisme dan pengurutan dengan sorted() untuk operator overloading,
  - validasi baru (stok desimal, kode barang ganda, jam lembur negatif, NIP ganda),
  - pemanggilan len() pada ruangan,
  - bagian duck typing,
  - kode penerapa SOLID OCP dan DIP di akhir program.

from models import (
    BarangInventaris, Karyawan, Staff, Manager, Magang, Ruangan, rupiah
)

  Program dijalankan dari dalam folder post-test-3 dengan perintah python posttest3_2509106012_MuhamadRadjaNurAkbar.py.

K. Penerapan Abstraksi
  - Abstract class: Karyawan (di karyawan.py), memakai ABC.
  - Abstract method: hitung_gaji() dan info(), keduanya diberi @abstractmethod.
  - Subclass yang mengimplementasikan seluruh abstract method: Staff, Manager, dan Magang.
  - Method konkret: cetak_slip_gaji(), dipakai bersama oleh semua subclass.
  - Konsep inheritance dari posttest sebelumnya tetap dipakai: super().init(...) di setiap subclass, atribut unik tiap subclass (jam_lembur, tunjangan_jabatan, durasi_bulan), atribut protected _gaji_pokok, serta atribut private seperti __divisi, __jam_lembur, dan __tunjangan_jabatan.

  Bukti abstract class tidak bisa diinstansiasi ada di file utama:

try:
    Karyawan('K000', 'Tes', 'Umum', 1000000)
except TypeError as e:
    print('Ditolak:', e)

L. Penerapan Polimorfisme
  1. Polimorfisme via pewarisan Method hitung_gaji() dan info() di-override oleh Staff, Manager, dan Magang dengan perilaku berbeda. Ketiganya dipanggil lewat satu loop pada objek yang bercampur di dalam satu list.

daftar_karyawan = [k1, k2, s1, m1, m2, g1]
for karyawan in daftar_karyawan:
    karyawan.cetak_slip_gaji()

  Output polimorfisme

  2. Duck typing Kelas BarangInventaris, Ruangan, dan Manager tidak berhubungan lewat pewarisan, tetapi sama-sama memiliki method info(). Ketiganya dipanggil lewat satu fungsi yang sama, tampilkan_info(), yang tidak mengecek tipe objek.

def tampilkan_info(objek):
    objek.info()

for objek in [b2, r2, m1]:
    tampilkan_info(objek)

Output duck typing

3. Operator overloading
  - str() di BarangInventaris, untuk menentukan teks hasil print(objek).
  - lt() di Karyawan, untuk membandingkan karyawan berdasarkan gaji, dipakai oleh sorted() dan s1 < m1.
  - len() di Ruangan, untuk mengetahui jumlah jenis barang lewat len(ruangan).

Output operator overloading

4. Larangan anti-pattern Tidak ada rantai if/elif yang mengecek type() atau string jenis untuk membedakan perilaku objek. Setiap objek menentukan perilakunya sendiri lewat method. Fungsi isinstance hanya dipakai di Ruangan untuk memvalidasi tipe input, bukan untuk membedakan perilaku.

M. Penerapan Solid
1. Open/Closed Principle (OCP), adalah Kelas harus terbuka untuk ditambah (open for extension), tetapi tertutup untuk diubah(closed for modification). Artinya, fitur baru ditambahkan dengan membuat kelas baru,
bukan dengan membongkar kode lama yang sudah berjalan dan sudah diuji. Kelas Magang ditambahkan sebagai subclass baru tanpa mengubah kode Karyawan, Ruangan, maupun loop penggajian di file utama. Karena semua kode lama bergantung pada method hitung_gaji() dan info(), objek Magang langsung bisa dipakai di loop slip gaji dan sebagai penanggung jawab ruangan.
2. Dependency Inversion Principle (DIP), yaitu Kelas tingkat tinggi tidak boleh bergantung langsung pada kelas tingkat rendah. Keduanya harus bergantung pada abstraksi. Kelas Ruangan bergantung pada abstraksi Karyawan, bukan pada kelas konkret Staff atau Manager. Penanggung jawab diberikan dari luar lewat constructor (dependency injection), sehingga Ruangan bisa menerima jenis karyawan apa pun tanpa diubah.

N. Relasi UML
<img width="912" height="684" alt="DiagramRelasi drawio" src="https://github.com/user-attachments/assets/23197565-f175-4fbb-8803-bb5a52dcf83d" />

Diagram memperlihatkan tiga relasi yang wajib beserta pewarisan. Ketiga relasi benar-benar ada di kode program.

1. Asosiasi: dari Ruangan ke Karyawan Ruangan menyimpan referensi satu Karyawan sebagai penanggung jawab lewat atribut private __penanggung_jawab yang diisi setter. Objek Karyawan dibuat di luar Ruangan dan hanya dikenal, tidak dimiliki, sehingga hubungannya paling longgar.
2. Agregasi: dari Ruangan ke BarangInventaris Ruangan menampung banyak BarangInventaris di list daftar_barang lewat method tambah_barang(). Dipilih agregasi karena barang dibuat di luar Ruangan, bisa berada di lebih dari satu ruangan (pada program, Laptop b1 masuk ke r1 dan r2), dan tetap ada walaupun ruangannya dihapus.
3. Komposisi: dari BarangInventaris ke RiwayatStok BarangInventaris membuat sendiri objek RiwayatStok di dalam constructor dan menyimpannya di atribut private __riwayat. Dipilih komposisi karena riwayat hanya ada untuk satu barang, tidak diterima dari luar, tidak bisa dibagikan ke barang lain, dan tidak berguna tanpa barangnya.

Perbedaan agregasi dan komposisi terletak pada siapa yang membuat objek bagian dan apakah bagian itu bisa hidup sendiri. Pada agregasi, bagian dibuat di luar dan tetap hidup mandiri. Pada komposisi, bagian dibuat oleh induknya dan tidak berdiri sendiri.

4. Pewarisan: dari Staff, Manager, dan Magang ke Karyawan Ketiga subclass mewarisi kelas abstrak Karyawan dan meng-override hitung_gaji() dan info().

O. Screenshot Output Program
1. Getter, Method tambah_stok(), kurangi_stok(), dan info() di barang_inventaris
<img width="418" height="405" alt="getter- -jumlah-stok-barang-inventaris" src="https://github.com/user-attachments/assets/dc1b7445-713b-45f8-a659-c763ee51864c" />
2. Validasi Nilai barang_inventaris
<img width="592" height="331" alt="validasi-nilai-brang-inventaris" src="https://github.com/user-attachments/assets/3428ff42-e267-4cee-b979-abafb38a1d27" />
3. Bukti abstract class tidak bisa diinstansiasi
<img width="1090" height="77" alt="bukti-abstraksi" src="https://github.com/user-attachments/assets/6aa2b2bb-5185-4c55-9232-c648d150e0df" />
4. Pewarisan Class Karyawan
<img width="547" height="345" alt="inheritance-karyawan" src="https://github.com/user-attachments/assets/e25ee90e-7a23-4cb1-bc10-8853d718a5c7" />
5. Polimorfisme pada Karyawan
<img width="572" height="305" alt="polimorfisme-karyawan" src="https://github.com/user-attachments/assets/83d54c2f-1613-4854-8055-d7b4d14f077f" />
6. Operator Overriding __lt__
<img width="596" height="191" alt="overriding" src="https://github.com/user-attachments/assets/0914a0f0-edfe-47dd-8307-eed3a1d36764" />
7. Getter dan Validasi Nilai di Karyawan
<img width="598" height="405" alt="getter-dan-validasi-karyawan" src="https://github.com/user-attachments/assets/2a2706ce-fd28-4eed-a9ed-02ccda0a3a5f" />
8. Getter dan Method di Ruangan
<img width="756" height="285" alt="getter-dan-method-ruangan" src="https://github.com/user-attachments/assets/7f901ea2-b953-43c7-aabd-ba8a3cf4c16d" />
9. Validasi Nilai di Ruangan
<img width="670" height="322" alt="validasi-nilai-ruangan" src="https://github.com/user-attachments/assets/5956f4bd-d956-4a80-80bd-d74800d55195" />
10. Duck Typing
<img width="758" height="117" alt="duck-typing" src="https://github.com/user-attachments/assets/232a8271-6d6f-40fb-ae3f-163ed4c3e074" />
11. SOLID OCP dan DIP
<img width="720" height="88" alt="output-prinsip-solid" src="https://github.com/user-attachments/assets/9858c9aa-9467-4923-934f-45ba4957a314" />

