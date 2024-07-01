# studi kasus 2
print("selesaikan studi kasus 2 berikut")
nama_lengkap = input("nama lengkap : ")
Nim = input("Nim : ")
absensi = int(input("absensi :  "))
Perilaku = int(input("Perilaku : "))
tugas = int(input("tugas : "))
formatif = int(input("formatif : "))
uts = int(input("Uts : "))
uas = int(input("Uas : "))
Ipk = absensi + Perilaku + tugas * formatif + uts / uas
print("hasil IPk nya")
print(absensi,'+',Perilaku,'+',tugas,'+',formatif,'*',uts,'/',uas,'=',Ipk)