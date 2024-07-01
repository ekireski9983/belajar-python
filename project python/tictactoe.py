# Inisialisasi papan permainan
papan = [' ' for _ in range(9)]

# Fungsi untuk menggambar papan permainan
def gambar_papan():
    print('-------------')
    print('|', papan[0], '|', papan[1], '|', papan[2], '|')
    print('-------------')
    print('|', papan[3], '|', papan[4], '|', papan[5], '|')
    print('-------------')
    print('|', papan[6], '|', papan[7], '|', papan[8], '|')
    print('-------------')

# Fungsi untuk mengecek apakah ada pemenang
def cek_pemenang():
    pemenang = None

    # Cek baris
    for i in range(0, 9, 3):
        if papan[i] == papan[i+1] == papan[i+2] != ' ':
            pemenang = papan[i]
            break

    # Cek kolom
    for i in range(3):
        if papan[i] == papan[i+3] == papan[i+6] != ' ':
            pemenang = papan[i]
            break

    # Cek diagonal
    if papan[0] == papan[4] == papan[8] != ' ':
        pemenang = papan[0]
    elif papan[2] == papan[4] == papan[6] != ' ':
        pemenang = papan[2]

    # Cek apakah ada pemenang
    if pemenang:
        print('Pemenangnya adalah', pemenang)
        return True

    # Cek apakah ada kotak yang kosong
    if ' ' not in papan:
        print('Permainan berakhir dengan hasil seri!')
        return True

    return False

# Fungsi untuk menjalankan permainan
def main():
    giliran = 'X'

    while True:
        gambar_papan()
        posisi = int(input('Pilih posisi (1-9): ')) - 1

        if papan[posisi] == ' ':
            papan[posisi] = giliran

            if cek_pemenang():
                break

            giliran = 'O' if giliran == 'X' else 'X'
        else:
            print('Posisi sudah terisi. Pilih posisi lain.')

# Memulai permainan
main()
