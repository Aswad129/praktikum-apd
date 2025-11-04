# # # # angka = float ("10")

# # # # print(type(angka))  

# # # # angka = [1, 2, 3, 4, 5]

# # # # print(max(angka))
# # # # print(min(angka))
# # # # print(sum(angka))

# # # for i, v in enumerate(['a','b']):
# # #     print(i, v) # 0 a , 1 b
# # # panjang = len([10, 20, 30]) 
# # # print(panjang) # 3
# # # list(map(str, [1,2,3])) # ['1', '2', '3']
# # # pendek = sorted([3, 1, 2]) # [1, 2, 3]
# # # print(pendek)
# # # list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

# # # x = 42
# # # y = 'Halo Dunia'
# # # def fungsi():
# # #     x = 10
# # #     y = 20
# # #     z = 30
# # #     print(globals()['y']) # mendapatkan isi dari variabel x (global)
# # #     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
# # #     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# # # fungsi()

# # import math

# # print(math.sqrt(16)) 
# # print(math.factorial(5))

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apa coba"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang

# print(acak_kartu)

# from datetime import datetime
# print(datetime.now())

import inquirer
pertanyaan = [
inquirer.List(
'size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
]
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size'])