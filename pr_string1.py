str=input("Introduceti un sir de caractere: ")
m=0
c=0
cs=0
for simbol in str:
    m+=simbol.isupper()
print("In sir sunt",m,"majuscule")
for cifra in str:    
    c+=cifra.isupper()
print("In sir sunt",c,"cifre")
for caractere_speciale in str:
    cs+=caractere_speciale.isupper()
print("In sir sunt",cs,"caractere speciale")
