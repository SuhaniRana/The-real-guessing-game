import random

print("Hello")
chances = 0
number = random.randint(1,9)

while chances < 5:
    yourNum = input("Enter a number between 1-10: ")
    if (yourNum == str(number)):
        print("Congrats you win!")
        break
       
    elif(yourNum<str(number)):
        print("Number is too low")
        
        
    else:
        print("Number is too high")

    chances+=1
    
if(chances > 4):
        print("You lose! The number is ", number)      





   
    
    