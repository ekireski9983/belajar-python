# operasi komporasi
# setiap hasil dari operasi komporasi adalah boolean

a = 4
b = 2

# lebih besar dari >
print(" lebih besar dari > ")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = a > 2
print(a,'>',2,'=',hasil)

# kurang dari dari <
print("kurang lebih dari <")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b > 3
print(b,'<',3,'=',hasil)
hasil = a < 2
print(a,'<',2,'=',hasil)

# lebih dari sama >=
print("lebih sama dari >= ")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = a >= 2
print(a,'>=',2,'=',hasil)

# lebih kurang dari sama >=
print("lebih kurang sama dari <= ")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = a <= 2
print(a,'<=',2,'=',hasil)

# tidak sama dengan (!=)
print("tidak sama dengan == ")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

#  sama dengan (==)
print(" sama dengan == ")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# perintah "is" sebagai komporasi object identity

x = 5 
y = 5
# ini adalah assigment membuat object
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is 5
print('x is y = ',hasil)

print("ini perintan indentity (is)")
x = 5 
y = 6
# ini adalah assigment membuat object
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not 5
print('x is y = ',hasil)