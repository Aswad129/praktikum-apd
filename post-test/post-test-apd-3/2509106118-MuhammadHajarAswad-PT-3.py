print("Input Data Perhitungan Gaji Karyawan PT.BOM".center(60, "="))

nama_karyawan = str(input("Masukkan nama karyawan :"))
jabatan_karyawan = str(input("Masukkan jabatan karyawan :"))
hari_kerja = int(input("Masukkan hari kerja anda :"))
jam_kerja = int(input("Masukkan jam kerja anda :"))
jumlah_lembur = int(input("Masukkan jumlah lembur anda :"))

harga_petasan_perPCS = 5000

if jabatan_karyawan == "peracik":
    if hari_kerja >= 24 and jam_kerja >= 8 and jumlah_lembur >= 4:
        bayaran_perjam = 25000
        per_perlemburan = 15000
    
    elif hari_kerja >= 18 and jam_kerja >= 6 and jumlah_lembur >= 2:
        bayaran_perjam = 20000
        per_perlemburan = 10000

    else :
        bayaran_perjam = 15000
        per_perlemburan = 10000


elif jabatan_karyawan == "pengantar petasan":
    if hari_kerja >= 20 and jam_kerja >= 7 and jumlah_lembur >= 7:
        bayaran_perjam = 25000
        per_perlemburan = 20000
    
    elif hari_kerja >= 16 and jam_kerja >= 5 and jumlah_lembur >= 4:
        bayaran_perjam = 20000
        per_perlemburan = 15000

    else :
        bayaran_perjam = 15000
        per_perlemburan = 12000

else:
    print("Jabatan tidak ada")
    exit()


total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (jumlah_lembur * per_perlemburan)


print("=" * 50)
print("        Penghitung Gaji Karyawan PT. BOM        ")
print("=" * 50)

print("Nama Karyawan           : ", nama_karyawan)
print(f"Harga Petasan per pcs   : Rp {harga_petasan_perPCS:,.0f}")
print("Hari Kerja              : ", hari_kerja, "hari")
print("Jam Kerja               : ", jam_kerja, "jam")
print("Jumlah Lembur           : ", jumlah_lembur)
print("-" * 50)
print(f"Bayaran per jam         : Rp {bayaran_perjam:,.0f}")
print(f"Bayaran per lemburan    : Rp {per_perlemburan:,.0f}")
print("-" * 50)
print(f"Total gaji anda  : Rp {total_gaji:,.0f}")
print("-" * 50)
