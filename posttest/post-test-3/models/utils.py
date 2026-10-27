# models/utils.py
# Fungsi bantu (helper) yang dipakai bersama oleh beberapa kelas.
# PERUBAHAN dari posttest 2: seluruh isi file ini BARU. Validasi yang dulu
# ditulis berulang di tiap setter (isinstance, < 0, strip) dikumpulkan di sini.


def cek_bulat(nilai, label):
    # bool adalah turunan int (True == 1), jadi ditolak secara eksplisit
    if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai < 0:
        raise ValueError(f'{label} harus bilangan bulat dan tidak boleh negatif!')
    return nilai


def cek_teks(nilai, label):
    if not isinstance(nilai, str) or nilai.strip() == '':
        raise ValueError(f'{label} tidak boleh kosong!')
    return nilai


def rupiah(nilai):
    return 'Rp' + f'{nilai:,}'.replace(',', '.')