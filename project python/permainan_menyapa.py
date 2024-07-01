import datetime

def sapa_pengguna():
    # mendapatkan waktu saat ini
    waktu_sekarang = datetime.datetime.now()

    # Menyapa pengguna berdasarkan waktu
    if waktu_sekarang.hour < 12:
        print("Selamat pagi!")
    elif waktu_sekarang.hour < 18:
        print("Selamat siang!")
    else:
        print("Selamat malam!")

# Memanggil fungsi sapa_pengguna
sapa_pengguna()