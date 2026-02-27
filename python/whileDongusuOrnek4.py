result=1
i=1

number=int(input("Enter a integer: "))
while(i<=number):
    result*=i
    i+=1

print(f"{number}!={result}")