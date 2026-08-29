import random
print("welcome to the number guessing game")
while True:
    computer = random.randint(1,5)  
    user_input = input("enter your correct number: ")
    if user_input == "show the number":
        print(f"The number is: {computer}")
    else:
        try:
            user = int(user_input)
            if user == computer:
                print("you are correct")
                break
            elif user > computer:
                print("try a lower number")
            elif user < computer:
                print("try a higher number")
        except ValueError:
            print("invalid input, please enter a number or 'show the number'")
            break




