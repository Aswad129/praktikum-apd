import os
from crud import tampilkan_film, tambah_film, mengubah_film, hapus_film
from auth import logout
from termcolor import colored
from data import daftar_film


def admin_menu():
    while True:
        print(colored("""  
=========================================
| 1. TAMBAH FILM & TAHUN RILIS          |
| 2. LIHAT FILM & TAHUN RILIS           |  
| 3. MENGUBAH NAMA FILM / TAHUN RILIS   |
| 4. HAPUS FILM / TAHUN RILIS           |
| 5. LOGOUT                             |
=========================================   
""", "cyan"
        ))
        menu_admin = input(colored("Pilih menu 1-5  :", "green"))
        if menu_admin == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                print("TAMBAH FILM & TAHUN RILIS")
                nama_film =  input("Masukkan nama film  :").strip().title()
                tahun_rilis = input("Masukkan tahun rilis  :")
                print(tambah_film(nama_film, tahun_rilis))
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
        
        elif menu_admin == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("LIHAT FILM & TAHUN RILIS")
            tampilkan_film()
        
        elif menu_admin == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                i = 0
                tampilkan_film()
                film_ke_nomor = {} 
                for NamaFilm, TahunRilis in daftar_film.items():
                    film_ke_nomor[i] = NamaFilm
                    i +=1
                pilih_film = int(input(f"Pilih film yang ingin di ubah (1-{len(daftar_film)}): ")) - 1
                nama_lama = film_ke_nomor[pilih_film]    
                nama_baru = input("Masukkan nama film baru  :").strip().title()
                tahun_baru = int(input("Masukkan tahun rilis baru  :"))
                print(mengubah_film(nama_lama, nama_baru, tahun_baru))
            except KeyError:
                print("Pilihan tidak valid")
            except ValueError:
                print("Tahun rilis harus berupa angka!")
        
        elif menu_admin == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HAPUS FILM / TAHUN RILIS")
            hapus_film()
        
        elif menu_admin == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            logout()
            break
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pilihan tidak valid, silahkan coba lagi.")