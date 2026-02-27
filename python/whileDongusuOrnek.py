MyNumbers=[]
i=0

while(i<7):
    İnputNumber=int(input("Enter a integer: "))
    MyNumbers.append(İnputNumber)
    i+=1

MyNumbers.sort()
#print(MyNumbers) #liste gibi yazar burda bitirirsen ornegin=[1, 2, 3, 19, 23, 34, 70]
x=0
while(x<7):
    print(MyNumbers[x],end=" ") #end parametresi atanmazsa alt alta yazar
    x+=1