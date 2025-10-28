# def perkenalan():
#     print("Halo, aku Nabil")
# perkenalan()

# def salam():
#     print ("Halo, Ridho")
# def kali():
#     x = 5*5
#     print(x)
# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

# #Pembuatan Fungsi Dengan Parameter
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas persegi panjang adalah" , luas)

# #Pemanggilan Fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 5)


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# # pemanggilan fungsi luas persegi
# print ("Luas persegi :", luas_persegi(8)) 

# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # membuat variabel lokal
# def info():
#     Nama = "Informatika"
#     Mata_Kuliah = "Logika Informatika"

# # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# # memanggil fungsi info
# info()

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# film = []

# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks+1, "|", film[indeks])

# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")
# insert_data()

# def edit_data():
    
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")
# edit_data()
# show_data()

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
    else:
        print("sesuai")
except ValueError as e:
    print(e)