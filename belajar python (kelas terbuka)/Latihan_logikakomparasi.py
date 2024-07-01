# latihan logika dan komperasi
# membuat gabungan area rentang dari angka
# +++++3----------10+++++++++++

inputUser = float(input("masukan angka yang bernilai kurang dari 3 \natau \nlebih besar dari 10 : "))

#++++++++++++3------------
# Memeriksa angka kurang dari 3
iskurangdari = (inputUser < 3)
print(iskurangdari)

# ----------10++++++
# memeriksa angka lebih dari 10
islebihdari = (inputUser > 10)
print("Lebih dari 10 = ",islebihdari)

isCorrect = iskurangdari or islebihdari
print("angka yang anda masukan : ",isCorrect)

# ----------3++++++++10---------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai kurang dari 3 \natau \nlebih besar dari 10 : "))
# --------3+++++++++++
# lebih dari 3
islebihdari = inputUser > 3
print("lebih dari 3 = ",islebihdari)
# ++++++++++++10----------
# kurang dari 10
iskurangdari = inputUser < 10
print("kurang dari 10 = ",iskurangdari)

isCorrect = iskurangdari and islebihdari
print("angka yang anda masukan",isCorrect)