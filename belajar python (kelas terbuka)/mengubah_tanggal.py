# mengubah teks menjadi format tanggal
from datetime import datetime

# masukan input
hari = str(input("masukan tanggal : "))
bulan = str(input("Masukan bulan (angka) :"))
tahun = str(input("Masukkan tahun (lengkap): "))
jam = str(input("masukan jam : "))
menit = str(input("Masukan menit : "))

tanggal = hari + ' ' + bulan + ' ' + tahun + ' ' + jam + ':' + menit


datetime_object = datetime.strptime(tanggal, "%d %m %Y %H:%M")
print(type(datetime_object))
print(datetime_object)