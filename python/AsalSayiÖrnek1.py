inputNumber=int(input("Bir sayi giriniz: "))
isPrime=True
if(inputNumber<0):
    print("Negatif bir sayi girdiniz. Pozitif bir sayi giriniz")
elif(inputNumber>0 and inputNumber<2):
    print("En kücük asal sayi 2'dir")
else:
    for i in range(2,int(inputNumber**0.5)+1):
        if(inputNumber %i ==0):
            isPrime=False
            break
    if(isPrime):
        print(f"{inputNumber} bir asal sayidir")
    else:
        print(f"{inputNumber} bir asal sayi degildir")

#Girilen bir sayının asal olup olmadığını belirleyen program