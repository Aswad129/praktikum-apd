nim = input("Masukkan NIM Anda :")


stamina = int(nim[-3:])
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3
    if stamina < 0:
        stamina = 0


print("MISI MENYEMPURNAKAN RASENGAN NARUTO".center(50, "="))
print("chakra terkumpul  = ", chakra)
print("stamina terkumpul =", stamina)
if chakra >= 200:
    print("chakra berhasil di kumpulkan")
else:
    print("chakra tidak berhasil di kumpulkan karena kehabisan stamina")
print("END".center(50, "="))


tinggi_menara = int(nim[-2:])
jumlah_gulungan = 0


for i in range (3, tinggi_menara + 1, 3 ):
    jumlah_gulungan += 1

print("MISI INFILTRASI".center(50, "="))
print (f"Tinggi Menara  : {tinggi_menara}M")
print(f"Jumlah Gulungan informasi yang telah di Dapatkan : {jumlah_gulungan}")
print("END".center(50, "="))    




jumlah_koridor = int(nim[-2])
data_intelegen = 0
perangkap_peledak = 0

print("MISI PENYELIDIKAN".center(50, "="))
for i in range(1, jumlah_koridor + 1):
    for j in range(1,4):
        if j % 2 != 0:
            print(f" Ruangan {j}: Data intelejen di temukan")
            data_intelegen +=1
        else:
            print(f" Ruangan {j}: Perangkap peledak berhasil di jinakkan")
            perangkap_peledak +=1


print(f" Total data intelegen yang di temukan : {data_intelegen}")
print(f" Total perangkap peledak di jinakkan  : {perangkap_peledak}")
print("END".center(50, "="))





