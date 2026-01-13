import random
while True:
    while True:
        low = input("enter the lower limit value : ")
        if low.isdigit():
            break
        else:
            print("enter a valid lower limit value")
            continue

    while True:
        high = input("engter the high limit value : ")
        if high.isdigit():
            break
        else:
            print("enter a valid higher limit value")
            continue
    
    if int(low) < int(high):
        break
    else:
        print("the lower limit can't be bigger then the higher limit")
        continue
        

print("")
print("")
print("----------------------------------------------")
print("")

while True:
    number = random.randint(int(low),int(high))
    while True:
        try:
            guess = int(input(f"guess the number between {low} and {high} : "))
            break
        except ValueError:
            continue
    if guess == number:
        print("you guessed right")
        break
    else:
        print(f"wrong answer , the answer was {number} , try again")
        continue

