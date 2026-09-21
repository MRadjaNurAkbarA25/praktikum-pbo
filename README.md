Posttest 1 Pemrograman Berorientasi Objek
Nama  : Muhamad Radja Nur Akbar
NIM   : 2509106012
Kelas : Informatika A1'25

Tema PBO: Sistem Manajamen Inventaris Barang Kantor
Tema program ini berisi pengelolaan dan manajemen inventaris barang kantor. Selain barang, program ini juga memiliki sistem manajamen karyawan kantor dan ruangan.
Daftar Class:
1. Barang Inventaris - BarangInventaris:
    Atribut:
       - jumlah_barang ---> Atribut Class
       - kode      ---|
       - nama      ---|----> Instance Public
       - kategori  ---|
       - stok      ---> Instance Private
    Khusus stok diinisialisasikan nilai awal adalah nol.
2. Karyawan - Karyawan:
    Atribut:
       - jumlah_karyawan ---> Atribut Class
       - nip    ---|--> Instance Public
       - nama   ---|--> ----~~----
       - divisi ---> Instance Private
3. Ruangan - Ruangan:
     Atribut:
       - jumlah_ruangan ---> Atribut Class
       - kode_ruangan  ---|
       - nama          ---|---> Instance Public
       - lantai        ---|
       - daftar_barang ---|
       - penanggung_jawab ---> Instance Private

Ketiga class memiliki atribut class yang serupa yaitu jumlah objek ketika dibuat. Ketiga atribut class tersebut diiniisialisasikan dengan nilai awal nol dan terus bertambah seiring dengan menambahnya objek. 

Penjelasan Program:
A. Class BarangInventaris
    Class ini memiliki 4 atribut instance dengan atribut 'stok' sebagai atribut private, stok yang dimaksud disini adalah jumlah untuk satu jenis barang, nilai awal atribut ini adalah nol. Dekorator @property memungkinkan kita untuk mengubah sebuah method (fungsi dalam class) agar bisa diakses seperti atribut biasa, dalam hal ini tidak perlu lagi menggunakan tanda kurung seperti penggunaan fungsi pada umumnya.
    Kemudian ada getter berfungsi untuk membaca dan mengembalikan nilai private serta setter untuk mengubah dan memberi validasi pada nilai tersebut. Dalam class ini stok adalah atribut private, maka buat sebuah getter. Lalu buat setter dengan nama yang sama dengan setter-nya yang berfungsi memperbarui nilai lama. Validasi pada getter ini yaitu tipe data harus integer dan nilai tidak boleh kurang dari nol. Jika memenuhi maka perbarui nilai stok.
    Berpindah ke method pada class ini, ada 3 method instance yaitu tambah_stok dan kurangi_stok yang berfokus ke jumlah stok dengan validasi di antaranya tidak boleh kurang dari sama dengan nol dan tidak melebihi jumlah stok di kurangi_stok, serta method info yang berfungsi menampilkan data objek. Lalu ada method class yang menampilkan total barang menggunakan cls, yaitu parameter pertama dan merujuk ke class itu sendiri, bisa juga dipanggil dengan nama class tersebut. Method class juga bisa digunakan sebagai alternatif pembuatan objek tanpa menggunakan constructor __init__ biasa, pada program ini menggunakan format dictionary. Terakhir ada method static, jenis method yang biasa dipakai untuk fungsi bantu tanpa perlu data dari objek maupun class-nya. Contohnya untuk mengecek validasi nilai. Dalam program ini, ketiga class memiliki static method yang sama yaitu untuk memvalidasi format atribut id yaitu kode, nip, dan kode_ruangan. Penggunaanya berada di awal def __init__ setiap class untuk memastikan format kode tepat ketika dipanggil.

B. Class Karyawan
    Class ini memiliki 3 atribut instance dengan atribut 'divisi' sebagai atribut private. Layaknya pada class sebelumnya, divisi memiliki nilai awal kosong dan ditetapkan pada pembuatan objek nantinya. Class ini juga menggunakan enkapsulasi @property, getter dan setter. Getter dan setter berperan untuk memperbarui divisi dengan syarat harus bertipe string dan tidak kosong.
    Terdapat juga method instance info untuk menampilkan data. Method class dan method static yang sama persis seperti pada class BarangInventaris.

C. Class Ruangan
    Class ini memiliki 5 atribut dengan penanggung_jawab sebagai atribut private. Atribut ini juga disetel dengan nilai awal None dan nilai atribut ini harus berasal dari objek class Karyawan. Atribut daftar_barang masuk sebagai atribut namun tidak masuk ke dalam kosntruktor karena nilainya berupa list yang akan berisi barang-barang dari BarangInventaris. 
    Class ini juga menggunakan getter dan setter untuk menetapkan nilai penanggung_jawab. Method unik di class ini yaitu tambah_barang, method ini memiliki validasi yaitu barang harus berupa objek dari class BarangInventaris dan tidak bisa menambah barang yang sudah ada pada list. Lalu method total_stok untuk menghitung jumlah barang pada list. Terakhir ada method info dan method class serta method static yang konsepnya sama dengan method class dan method static pada kedua class sebelumnya. 

D. Pengujian Program
    Pada pengujian program bagian class BarangInventaris, pembuatan objek menggunakan teknik biasa dan memanggil method dictionary. Lalu menampilkan info setiap objek dan total barang. Selanjutnya memanggil method tambah dan kurangi. Lalu memanggil setter di b1.stok dan cukup memperbarui nilai layaknya memperbarui atribut biasa. Kemudian menguji setiap validasi value error pada setter dan method instance biasa. Terakhir menguji method static dengan memasukkan nilai eror yang akan ditangkap raise, yaitu menambah karakter spasi pada atribut kode.
    Pengujian pada class Karyawan juga kurang lebih sama, memanggil setiap method dan menguji nilainya. Khusus untuk class Ruangan, dapat dilihat method tambah_barang menggunakan objek dari class BarangInventaris (b1 dan b2) untuk ditambah ke dalam list. Pada baris "total stok" adalah jumlah stok pada setiap ruangan. Nilai penanggung_jawab juga berupa dan harus objek dari class Karyawan (k1 dan k2). Method-method yang tersisa dipanggil dan diuji validasi nilainya.

   
