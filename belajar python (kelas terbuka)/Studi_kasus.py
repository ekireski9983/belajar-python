# studi kasus 1
print("====== studi kasus 1 =====")
print(" hitunglah gaji karyawan berikut!!!")
nama_karyawan = input(" nama karyawan : ")
posisi = input(" posisi pekerjaan : ")
gaji_pokok = int(input(" gaji pokok : "))
gaji_harian = int(input(" gaji harian : "))
gaji_tahunan = int(input(" gaji tahunan : "))
gaji_lebaran = int(input(" tunjangan hari raya : "))
total_gaji = gaji_pokok + gaji_harian * gaji_tahunan + gaji_lebaran
print(gaji_pokok,'+',gaji_harian,'*',gaji_tahunan,'+',gaji_lebaran,'=',total_gaji)