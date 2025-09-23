a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


a /= b
print (a)

nilai = 75

if nilai >= 70 :
    print("nilai kamu besar")
    if nilai == 75:
            print("nilai 75")
    else: print("tidak luls")
else :
            print("anda tidak lulus")

        # input nilai
umur = int(input("Masukkan umur Anda: "))
        # misalnya, umur = 16
        # Percabangan
if umur < 13:
            kategori = "Anak-anak"
elif umur < 18:
            kategori = "Remaja"
elif umur < 60:
            kategori = "Dewasa"
else:
            kategori = "Lansia"
        # Menampilkan umur dan kategori
print("Umur:", umur, "Kategori:", kategori)

tinggi_badan = 145
status = "di izinkan naik wahana" if tinggi_badan >= 145 else "tidak di izinkan"
print (status)


harga = 100000

if harga >= 100000:
        print("diskon 20%")
elif harga > 50000:
        print("diskon 10%")
else:
        print("tidak diskon")