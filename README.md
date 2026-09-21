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
    Kemudian ada getter berfungsi untuk membaca dan mengembalikan nilai private serta setter untuk mengubah dan memberi validasi pada nilai tersebut. Dalam class ini stok adalah atribut private, maka buat sebuah getter. Lalu buat setter dengan nama yang sama dengan setter-nya yang berfungsi memperbarui nilai lama. 


   
