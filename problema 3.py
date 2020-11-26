s1=str(input("Dati primul cuvant:"))
s2=str(input("Dati al doilea cuvant:"))
s3=str(input("Dati al treilea cuvant:"))
s4=str(input("Dati al patrulea cuvant:"))
if ((len(s1)<3) or (len(s2)<3) or (len(s3)<3) or (len(s4)<3)):
    print("Error")
l1=s1[:2]
l2=s2[0]
l3=s3[:3]
l4=s4[:(len(s4)//2)]
print("Cuvantul format este",l1+l2+l3+l4)