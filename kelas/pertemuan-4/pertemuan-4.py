# ulangi = 10
# for i in range (1,10,4):
#     print(f'Perulangan ke {i}')

# for i in range(1, 5):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 7):# Mengontrol kolom dalam tabel perkalian
#        print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi 

# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)

# for index, nilai in enumerate(simpan):
#     print(simpan[index])

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")