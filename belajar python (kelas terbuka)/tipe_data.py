## a = 10, adalah variable dengan nilai 10
# tipe data : angka satuan yang gak ada
# koma nya (integer)

data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print("data :", data_float)
print("data : ", data_float)

# tipe data : kumpulan karakter(string)
data_string = "ucok"
print("data :", data_float)
print("- bertipe : ", type(data_string))

# tipe data : Boolean false/true
data_bool = False
print("data : ", data_bool)
print(" - bertipe", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print(" - bertipe", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))