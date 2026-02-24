#Kulanıcadan alınan iki sayının büyük mü küçük mü veya eşit mi olduğunu bulan program.

sayi1=int(input("1.sayiyi giriniz: "))
sayi2=int(input("2.sayiyi giriniz: "))
if sayi1>sayi2:
    print("1. sayi 2. sayidan daha buyuktur...")

elif sayi1==sayi2:
    print("2 sayi birbirine esit...")

else:
    print("2.sayi 1.sayidan daha buyuktur...")