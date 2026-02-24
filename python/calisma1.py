#Kulanıcadan alınan iki sayının büyük mü küçük mü veya eşit mi olduğunu bulan program.

sayi1=int(input("1.sayiyi giriniz: "))
sayi2=int(input("2.sayiyi giriniz: "))
if sayi1>sayi2:
    print(f"{sayi1}, {sayi2}'den daha buyuktur...")

elif sayi1==sayi2:
    print(f"{sayi1} ve {sayi2} birbirine esit...")

else:
    print(f"{sayi2}, {sayi1}'den daha buyuktur...")