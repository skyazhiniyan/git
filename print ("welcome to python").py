import random
print("welcome to the number gussing game")
while True:
    computer = random.randint(1,10)
    user = int(input("enter your crt number:"))
    if user == computer:
        print("your are crt")
    elif user > computer:
        print("try less number")
    elif user < computer:
        print("try higher")
    else:
        print("invealind input")
        break

               
    