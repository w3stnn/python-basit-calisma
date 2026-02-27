startNumber=int(input("Enter the start number: "))
endNumber=int(input("Enter the ending number: "))

while(startNumber<endNumber):
    if(startNumber %2 == 0):
        print(startNumber,end=" ")
    startNumber+=1