user_input = str(input("masukan parapase :"))
text = user_input.split()
a = ""
for i in text:
    a = a+str(i[0]).upper()
print(a)