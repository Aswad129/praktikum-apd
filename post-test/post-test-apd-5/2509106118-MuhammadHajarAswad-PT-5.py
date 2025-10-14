import os
data_login = [
    [1,"admin", "adminfilm22"],
    [2,"user", "user123"]
    ]

nama_film = []
tahun_rilis = []

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
        regis_tipe = 2 

        data_login.append([regis_tipe, regis_username, regis_password])
        print("Anda berhasil register")
    
    elif menu_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LOGIN")
        input_username = input("masukkan username  :")
        input_password = input("Masukkan password  :")

        for cek_login in range(len(data_login)):
            tipe_pengguna, username, password = data_login[cek_login]
            if input_username == username and input_password == password:
                print("Anda berhasil login")
                if tipe_pengguna == 1:
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
                            nama_film.append(film_baru)
                            tahun_rilis.append(input_tahun_rilis)
                            print(f"Film {nama_film} tahun rilis {tahun_rilis} berhasil ditambahkan")

                        elif menu_admin == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENAMPILKAN FILM & TAHUN RILIS")
                            for i in range(len(nama_film)):
                                 print(f"{i+1}. {nama_film[i]} ({tahun_rilis[i]})")

                        elif menu_admin == "3":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("MENGUBAH NAMA FILM / TAHUN RILIS")
                            for i in range(len(nama_film)):
                                print("{}. {} ({})".format(i+1, nama_film[i], tahun_rilis[i]))
                            pilih_film = int(input("Pilih film yang ingin diubah (1-{}): ".format(len(nama_film)))) - 1
                            update_film = input("Masukkan nama film baru: ")
                            update_tahun = input("Masukkan tahun rilis baru: ")
                            nama_film[pilih_film] = update_film
                            tahun_rilis[pilih_film] = update_tahun
                            print(f"Film {nama_film[pilih_film]} tahun rilis {tahun_rilis[pilih_film]} berhasil diubah menjadi {update_film} tahun rilis {update_tahun}")
                        
                        elif menu_admin == "4":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for i in range(len(nama_film)):
                                print("HAPUS FILM / TAHUN RILIS")
                                print(f"{i+1}. {nama_film[i]} ({tahun_rilis[i]})")
                            hapus_film = int(input(f"Pilih nomor film yang ingin di hapus : ")) - 1
                            print(f"Film {nama_film[hapus_film]} tahun rilis {tahun_rilis[hapus_film]} berhasil dihapus")
                            del nama_film[hapus_film]
                            del tahun_rilis[hapus_film]
                        
                        elif menu_admin == "5":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Anda berhasil logout")
                            break
                        
                        else:
                            print("Tidak valid pilihan hanya 1-5 !!!")
                            pass

                elif tipe_pengguna == 2:
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
                            for i in range(len(nama_film)):
                             print(f"{i+1}. {nama_film[i]} ({tahun_rilis[i]})")

                                
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

    