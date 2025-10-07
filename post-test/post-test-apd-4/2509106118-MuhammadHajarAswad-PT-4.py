nim = input("Masukkan NIM Anda :")


stamina = int(nim[-3:])
chakra = 0

while chakra < 200:
    chakra += 5
    stamina -= 3
    if stamina < 0:
        stamina = 0

print("chakra terkumpul = ", chakra)
print("stamina terkumpul =", stamina)
if chakra >= 200:
    print("berhasil")
else:
    print("gagal")


