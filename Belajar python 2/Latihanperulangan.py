total_belanja = input("Total belanja: ")
bayar = total_belanja

if total_belanja > 1000000:
    print("kamu mendapatkab bonus Teh pucuk")
    print("dan mendapatkan diskon 10%")

#hitung diskon
diskon = total_belanja * 10/100 #10%
bayar = total_belanja - diskon

print("Total yang harus dibayar: Rp %s" % bayar)
print("Terima kasih sudah berbelanja")
print("Datang lagi yaa...")
