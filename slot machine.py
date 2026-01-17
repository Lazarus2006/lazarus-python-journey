import random

def spin_row():
    symbols = ["C", "M", "L" ,"B" ,"S"]
    return [ random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "C":
            return bet * 3
        elif row[0] == "M":
            return bet * 4
        elif row[0] == "L":
            return bet * 5
        elif row[0] == "B":
            return bet * 10
        elif row[0] == "S":
            return bet * 20
    return 0

balance = 100
while True:
    
    print("-------------------------------------------")
    print("          slot machine                     ")
    print("symbols: C M L B S")
    print("-------------------------------------------")
    print(f"you have ${balance}")
    while True:
        try: 
            bet = int(input("place your bet amount : "))
            if bet <= 0:
                print("your bet must be higher than 0\n")
                continue
            if bet > balance:
                print("your bet must be lower than your balance ")
                continue
            break

        except ValueError:
            continue
        
    row = spin_row()
    print_row(row)
    payout = get_payout(row,bet)
    if payout > 0:
        balance += payout
        print(f"congrats you won ${payout}")
        print(f"your new balance is {balance}")
    else:
        balance -= bet
        print("sorry you lost")
        print(f"your new balance is {balance}")

    if balance <= 0:
        print("You're out of money! Game over.")
        break


    keep_going = input("do you want to bet again ?(y/n) : ").lower()
    if keep_going == "y":
        continue
    else:
        break


        