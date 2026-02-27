Number=int(input("Enter a integer: "))

for item in range(Number):
    if(item%2==0): #(item%2==1) olsaydı tek olanları yazardı
        continue
    print(item,end=" ")
else:
    print("\nFor loop finished!")