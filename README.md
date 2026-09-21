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
   


   
