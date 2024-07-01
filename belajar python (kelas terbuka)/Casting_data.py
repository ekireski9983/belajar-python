# belajar casting data
# merubah dari satu tipe data ke tipe lain
# tipe data = int,float,str,bool

## integer
print("=====tipe data integer =====")
data_int = 9;
print("data =", data_int, ", type=", type("data_int"))

data_float = float(data_int)
data_int = str(data_int)
data_bool = bool(data_int) 
# ini false jika nilai int = 0
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))
print("data = ", data_int, "type = ", type(data_int))

## float 
print("ini adalah program tipe data float")
data_float = 0;
print("data = ", data_int, ",type = ",type(data_float))

data_int = int(data_float)
# akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)

## boolean
print("ini adalah program tipe data String")
data_str = 10;
print("data = ", data_str, ",type = ",type(data_str))
data_int    = int(data_str) # string harus angka
data_float  = float(data_str)  # string harus angka
data_bool   = bool(data_str) # false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))
