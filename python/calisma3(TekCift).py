sayi=int(input("bir sayi giriniz: "))

if sayi%2==0:
    print(f"{sayi} cifttir...")
elif sayi<0:
    print("Girilen sayi sifirdan kucuk olamaz...")
else:
    print(f"{sayi} tektir...")