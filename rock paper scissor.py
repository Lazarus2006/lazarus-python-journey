import random

user_input = ""
options = ("rock" , "paper" , "scissor")

while True:
    user_input = input("rock / paper / scissor : ").lower()
    
    if user_input in options:
        break
    else:
        continue

computer_guess = random.choice(options)
print(f"the computer choosed {computer_guess}")
if user_input == "rock":
    if computer_guess == "paper":
        print("you lost")
    elif computer_guess == "scissor":
        print("you won")
    elif computer_guess == "rock":
        print("draw")
elif user_input == "paper":
    if computer_guess == "paper":
        print("draw")
    elif computer_guess == "scissor":
        print("you lost")
    elif computer_guess == "rock":
        print("you won")
elif user_input == "scissor":
    if computer_guess == "paper":
        print("you won")
    elif computer_guess == "scissor":
        print("draw")
    elif computer_guess == "rock":
        print("you lost")

