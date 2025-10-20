# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)
# 
# angka_ganjil = {1, 3, 5, 7, 9}
# # for angka in angka_ganjil:
#     print(angka)

# angka_ganjil.add(11)
# print(angka_ganjil)

# input_tambah = int(input("Masukkan angka yang ingin ditambahkan :"))
# angka_ganjil.add(input_tambah)
# print(angka_ganjil)

# print(angka_ganjil)

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
# "Instagram" : "daffahrhap"
# }
# }
# # print(f"nama saya adalah {Biodata["Nama"]}")
# # print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # print(f"nama saya adalah {Biodata.get("Nama")}")
# # print(Biodata.get("Nama"))
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key tersebut tidak ada"))

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah : {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# print(data)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# # cache = data.pop("Nama")
# # #Setelah dihapus
# # print(data)
# # print(cache)
# # data.clear()
# # print(data)
# print("Jumlah Data = ", len(data))

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
for song in j:
    print(song)
print("")
