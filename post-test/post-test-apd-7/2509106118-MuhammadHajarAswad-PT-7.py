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
status_login = False


def tampilkan_film():
    global daftar_film
    i = 0
    for NamaFilm, TahunRilis in daftar_film.items():
         print(f"{i+1}. {NamaFilm} ({TahunRilis})")
         i +=1

def tambah_film(nama, tahun):
    global daftar_film
    daftar_film.update({nama: tahun})
    return f"Film {nama} dengan tahun rilis {tahun} berhasil ditambahkan"

def mengubah_film(nama_lama, nama_baru, tahun_baru):
    global daftar_film
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
        print(f"film {nama_lama} berhasil di hapus")
    except KeyError:
        print("Pilihan tidak valid")

    

def register():
    global data_login
    regis_username = input("Masukkan username  :")
    regis_password = input("Masukkan password  :")
    new_user = len(data_login) + 1
    data_login[new_user] = {"username": regis_username, "password": regis_password, "tipe": "user"}
    print("Anda berhasil register")

def logout():
    global status_login
    status_login = False
    print("Anda berhasil logout")

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
        register()
    
    elif menu_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LOGIN")
        input_username = input("Masukkan username  :")
        input_password = input("Masukkan password  :")
        login_berhasil = False
        for cek_login, value in data_login.items():
            if input_username == value["username"] and input_password == value["password"]:
                login_berhasil = True
                status_login = True
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
                            try:
                                print("TAMBAH FILM & TAHUN RILIS")
                                nama_film =  input("Masukkan nama film  :")
                                tahun_rilis = int(input("Masukkan tahun rilis  :"))
                                print(tambah_film(nama_film, tahun_rilis))
                            except ValueError:
                                print("Tahun rilis harus berupa angka")

                        elif menu_admin == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENAMPILKAN FILM & TAHUN RILIS")
                            tampilkan_film()

                        elif menu_admin == "3":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENGUBAH NAMA FILM / TAHUN RILIS")   
                            try:
                                i = 0
                                tampilkan_film()
                                film_ke_nomor = {} 
                                for NamaFilm, TahunRilis in daftar_film.items():
                                     film_ke_nomor[i] = NamaFilm
                                     i +=1
                                pilih_film = int(input(f"Pilih film yang ingin di ubah (1-{len(daftar_film)}): ")) - 1
                                nama_lama = film_ke_nomor[pilih_film]    
                                nama_baru = input("Masukkan nama film baru  :")
                                tahun_baru = int(input("Masukkan tahun rilis baru  :"))
                                print(mengubah_film(nama_lama, nama_baru, tahun_baru))
                            except KeyError:
                                print("Pilihan tidak valid")
                            except ValueError:
                                print("Tahun rilis harus berupa angka!")
                        
                        elif menu_admin == "4":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("HAPUS NAMA FILM DAN TAHUN RILIS")   
                            hapus_film()

                        elif menu_admin == "5":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            logout()
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
                            tampilkan_film() 

                                
                        elif menu_user == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            logout()
                            break
                        else:
                            print("Tidak valid pilihan hanya 1-2 !!!")
                            
                break
    elif menu_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Anda berhasil keluar dari program")
        exit()
    else:
        print("Tidak valid pilihan hanya 1-3 !!!")
        pass

    