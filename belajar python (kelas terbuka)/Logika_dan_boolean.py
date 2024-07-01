# operasi Logika dan boolean
# not or and xor

# NOT
print('====NOT====')
a = False
c = not a
print('data a =',a)
print('-------------- NOT')
print('data c =',c)


# OR
print('======OR=====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

# logika AND jika dua buah nilai true, maka hasil true
print('logika AND')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# Logika XOR akan true jika salah satu true akan semua nya OR
print('logika XOR')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)