import os
data_login = {
    1: {"username": "admin", 
        "password": "adminfilm22", 
        "tipe": "admin"},
    2: {"username": "user", 
        "password": "user123", 
        "tipe": "user"}
}

daftar_film = {}

while True:
    print(
""""
=========================
| 1. REGISTER           |
| 2. LOGIN              |
| 3. OUT                |
=========================
"""
    )

    menu_utama = input("Pilih menu 1-3  :")
    if menu_utama == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SILAHKAN REGISTER")
        regis_username = input("Masukkan username  :")
        regis_password = input("Masukkan password  :")
        new_user = len(data_login) + 1


        data_login[new_user] = {"username": regis_username, "password": regis_password, "tipe": "user"}
        print("Anda berhasil register")
    
    elif menu_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LOGIN")
        input_username = input("masukkan username  :")
        input_password = input("Masukkan password  :")

        for cek_login, value in data_login.items():
            if value["username"] == input_username and value["password"] == input_password:
                print("Anda berhasil login")
                if value["tipe"] == "admin":
                    print("login sebagai admin")
                    while True:
                        print("""
=========================================
| 1. TAMBAH FILM & TAHUN RILIS          |
| 2. LIHAT FILM & TAHUN RILIS           |
| 3. MENGUBAH NAMA FILM / TAHUN RILIS   |
| 4. HAPUS FILM / TAHUN RILIS           |
| 5. LOGOUT                             |
=========================================
"""
                        )
                        menu_admin = input("Pilih menu 1-5  :")
                        if menu_admin == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("TAMBAH FILM & TAHUN RILIS")
                            film_baru = input("Masukkan nama film  :")
                            input_tahun_rilis = input("Masukkan tahun rilis  :")
                            daftar_film.update({film_baru: input_tahun_rilis})
                            print(f"Film {film_baru} tahun rilis {input_tahun_rilis} berhasil ditambahkan")

                        elif menu_admin == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENAMPILKAN FILM & TAHUN RILIS")
                            i = 0
                            for NamaFilm, TahunRilis in daftar_film.items():
                                 print(f"{i+1}. {NamaFilm} ({TahunRilis})")
                                 i +=1

                        elif menu_admin == "3":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENGUBAH NAMA FILM / TAHUN RILIS")   
                            i = 0
                            film_ke_nomor = {} 
                            for NamaFilm, TahunRilis in daftar_film.items():
                                 print(f"{i+1}. {NamaFilm} ({TahunRilis})")
                                 film_ke_nomor[i] = NamaFilm
                                 i +=1
                            pilih_film = int(input(f"Pilih film yang ingin diubah (1-{len(daftar_film)}): ")) - 1
                            nama_lama = film_ke_nomor[pilih_film]
                            tahun_lama = daftar_film[nama_lama]

                            update_film = input("Masukkan nama film baru: ")
                            update_tahun = input("Masukkan tahun rilis baru: ")
                            del daftar_film[nama_lama]
                            daftar_film.update({update_film: update_tahun})
                            print(f"Film {nama_lama} ({tahun_lama}) berhasil di ubah menjadi {update_film} ({update_tahun})")

                        
                        elif menu_admin == "4":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("HAPUS NAMA FILM DAN TAHUN RILIS")   
                            i = 0
                            film_ke_nomor = {} 
                            for NamaFilm, TahunRilis in daftar_film.items():
                                 print(f"{i+1}. {NamaFilm} ({TahunRilis})")
                                 film_ke_nomor[i] = NamaFilm
                                 i +=1
                            pilih_film = int(input(f"Pilih film yang ingin diubah (1-{len(daftar_film)}): ")) - 1
                            nama_lama = film_ke_nomor[pilih_film]    
                            del daftar_film[nama_lama]   
                            print(f"film {nama_lama} berhasil di hapus")


                        elif menu_admin == "5":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Anda berhasil logout")
                            break
                        
                        else:
                            print("Tidak valid pilihan hanya 1-5 !!!")
                            pass

                elif value["tipe"] == "user":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("login sebagai user")
                    while True:
                        print("""
=========================================
| 1. LIHAT FILM & TAHUN RILIS           |
| 2. LOGOUT                             |
=========================================
"""
                        )
                        menu_user = input("Pilih menu 1-2  :")
                        if menu_user == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("LIHAT FILM & TAHUN RILIS")
                            i = 0
                            for NamaFilm, TahunRilis in daftar_film.items():
                                 print(f"{i+1}. {NamaFilm} ({TahunRilis})")
                                 i +=1

                                
                        elif menu_user == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Anda berhasil logout")
                            break
                        else:
                            print("Tidak valid pilihan hanya 1-2 !!!")
                            
                break
    elif menu_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Anda berhasil keluar dari program")
        break
    else:
        print("Tidak valid pilihan hanya 1-3 !!!")
        pass

    