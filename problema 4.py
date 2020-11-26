s1=str(input("Introdu CNP: "))
n=0
if (len(s1)>13)or(len(s1)<13):
    print("Acest CNP nu e corect")
else:
    for i in s1:
        if ord(i) in range(48,58):
            n+=1
    if (n==13):
        print("Acest CNP e corect")
    else:
        print("Acest CNP nu e corect")
