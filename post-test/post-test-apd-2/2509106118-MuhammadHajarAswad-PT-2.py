
print("INPUT PEMBELIAN".center(60, "="))

pelanggan = str(input("Masukkan nama pelanggan: "))
jumlah_BatuBata = int(input("Masukkan jumlah batu bata: "))
jumlah_semen = int(input("Masukkan jumlah semen: "))
harga_perBatuBata = 100
harga_perSemen = 100000

total_harga = (jumlah_BatuBata * harga_perBatuBata) + (jumlah_semen * harga_perSemen)

if jumlah_BatuBata == 500 and jumlah_semen == 5:
    diskon = 0.15
    keterangan = "Paket Hemat"
elif jumlah_BatuBata == 2000 and jumlah_semen == 16:
    diskon = 0.30
    keterangan = "Paket Ultra Mantap"
else:   
    diskon = 0
    keterangan = "Tidak mendapatkan diskon"

    
harga_setelah_diskon = total_harga * (diskon)
harga_seluruh = total_harga - harga_setelah_diskon

print("ESTIMASI BIAYA BAHAN BANGUNAN".center(60, "="))
print("-" * 60)
print("Nama Pelanggan    : ", pelanggan)
print("Jumlah Batu Bata  : ", jumlah_BatuBata)        
print("Jumlah Semen      : ", jumlah_semen)
print("-" * 60)
print(f"Total Harga                     : Rp {total_harga:,}")
print(f"Diskon yang didapat             : {keterangan}, {diskon * 100:.0f}%")
print(f"Potongan setelah diskon         : Rp {harga_setelah_diskon:,.0f}")
print("-" * 60)
print(f"Total biaya yang di bayarkan    : Rp {harga_seluruh:,.0f}")
print("-" * 60)

