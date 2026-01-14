balance = 0
def show_balance():
    global balance
    print(f"your balance is ${balance:.2f}")
    input("press enter to continue : ")
def deposit():
    global balance
    while True:
        try:
            amount = float(input("enter the amount you want to deposit : "))
            if amount < 0:
                print("invalid")
                input("press enter to continue : ")
            else:
                balance += amount
                print(f"you deposited ${amount:.2f} , your new balance is ${balance:.2f}")
                input("press enter to continue : ")
            break
        except ValueError:
            print("invalid")
        continue
def withdraw():
    global balance
    while True:
        try:
            amount = float(input("enter the amount you want to withdraw : "))
            if amount < 0:
                print("invalid")
                input("press enter to continue : ")
            elif amount > balance:
                print(f"insufficient balance {balance}")
                input("press enter to continue : ")
            else:
                balance -= amount
                print(f"you withdrawen ${amount:.2f} , your new balance is ${balance:.2f}")
                input("press enter to continue : ")
            break
        except ValueError:
            print("invalid")
        continue
def exit_app():
    print("Thank you for using Banking Counter!")
    import sys
    sys.exit()



while True:
    print("-----Banking Counter-----")
    print("1. show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4) : ")

    match choice:
        case "1":
            show_balance()
        case "2":
            deposit()
        case "3":
            withdraw()
        case "4":
            exit_app()
        case _:
            print("enter a valid input")
