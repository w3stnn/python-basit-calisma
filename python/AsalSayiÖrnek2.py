inputNumber=int(input("Bir sayi giriniz: "))
primeNumbers=[]
if(inputNumber<0):
    print("Negatif bir sayi girdiniz. Pozitif bir sayi giriniz")
elif(inputNumber>0 and inputNumber<2):
    print("En kücük asal sayi 2'dir")
else:
    primeNumbers.append(2)
    for i in range(3,inputNumber+1,2):
        for j in range(3,int(i**0.5)+1):
            if(i %j ==0):
                break
        else:
            primeNumbers.append(i)
    print(f"{primeNumbers}")

#Girilen sayıya kadar olan asal sayıları bulan program