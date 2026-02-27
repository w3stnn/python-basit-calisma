import random

randomNumber=random.randint(1,100) #rasgele 1-100 arası tam sayı üret
remainingAttempts=5 #5 deneme hakkı atandı
score=100 #başlangıç puanı
attemptCount=0 #deneme sayısı
print("Guess a number between 1 and 100") #kullanıcıya 1-100 arasındaki sayıyıy tahmin et mesajı verildi
print(f"Your starting score:{score}") #başlangıç puanı yazıldı

while (remainingAttempts>0):
    guess=int(input("your guess: "))
    attemptCount+=1
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100")
        continue
    if(guess==randomNumber):
        print(f"Congratulationsa! You guessed the number correctly on your {attemptCount}.attempt")
        print(f"Your total score:{score}")
        break
    elif(guess<randomNumber):
        print("Try a larger number")
    else:
        print("Try a smaller number")
    remainingAttempts-=1
    score-=20
    if(remainingAttempts>0):
        print(f"Remaining attempts:{remainingAttempts}")
        print(f"Current score:{score}")
    else:
        print("Unfortunately! you ran out of attempts!")
        print(f"Your total score:{score}")