import tkinter as tk

def hitung():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        operator = entry_operator.get()

        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            hasil = angka1 / angka2
        else:
            hasil = "Operator tidak valid"

        label_hasil.config(text="Hasil: " + str(hasil))
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid")

# Membuat window
window = tk.Tk()
window.title("Kalkulator")

# Membuat label dan entry untuk angka pertama
label_angka1 = tk.Label(window, text="Angka Pertama:")
label_angka1.pack()
entry_angka1 = tk.Entry(window)
entry_angka1.pack()

# Membuat label dan entry untuk operator
label_operator = tk.Label(window, text="Operator (+, -, *, /):")
label_operator.pack()
entry_operator = tk.Entry(window)
entry_operator.pack()

# Membuat label dan entry untuk angka kedua
label_angka2 = tk.Label(window, text="Angka Kedua:")
label_angka2.pack()
entry_angka2 = tk.Entry(window)
entry_angka2.pack()

# Membuat tombol hitung
button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

# Membuat label untuk hasil
label_hasil = tk.Label(window, text="Hasil:")
label_hasil.pack()

# Menjalankan aplikasi
window.mainloop()
