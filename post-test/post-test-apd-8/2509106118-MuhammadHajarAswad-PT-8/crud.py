from prettytable import PrettyTable
from data import daftar_film

def tampilkan_film():
    global daftar_film
    table = PrettyTable()
    table.field_names = ["No", "Nama Film", "Tahun Rilis"]
    for i, (NamaFilm, TahunRilis) in enumerate(daftar_film.items(), start=1):
        table.add_row([i, NamaFilm, TahunRilis])
    print(table)

def tambah_film(nama, tahun):
    global daftar_film
    daftar_film.update({nama: tahun})
    return f"Film {nama} dengan tahun rilis {tahun} berhasil ditambahkan"

def mengubah_film(nama_lama, nama_baru, tahun_baru):
    global daftar_film
    tampilkan_film
    del daftar_film[nama_lama]
    daftar_film.update({nama_baru: tahun_baru})
    return f"Film {nama_lama} berhasil di ubah menjadi {nama_baru} dengan tahun rilis {tahun_baru}"

def hapus_film():
    global daftar_film
    i = 0
    tampilkan_film()
    try:
        film_ke_nomor = {} 
        for NamaFilm, TahunRilis in daftar_film.items():
             film_ke_nomor[i] = NamaFilm
             i +=1
        pilih_film = int(input(f"Pilih film yang ingin dihapus (1-{len(daftar_film)}): ")) - 1
        nama_lama = film_ke_nomor[pilih_film]    
        del daftar_film[nama_lama]   
        print(f"film {nama_lama.title()} berhasil di hapus")
    except KeyError:
        print("Pilihan tidak valid")