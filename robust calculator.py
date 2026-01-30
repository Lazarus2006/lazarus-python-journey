def calculator():
    while True:
        try:
            n1 = float(input("enter the first number: "))
            break
        except ValueError:
            continue
    number_1 = n1 
    
    while True:
        try:
            n2 = float(input("enter the second number: "))
            break
        except ValueError:
            continue
    number_2 = n2
    def _sign_():
        s1 = input("choose a oparation (+ , - , * , / ) : ")
        if s1 == "+":
            result = number_1 + number_2
            print(f"the answer is {result}")
        elif s1 == "-":
            result = number_1 - number_2
            print(f"the answer is {result}")
        elif s1 == "*":
            result = number_1 * number_2
            print(f"the answer is {result}")
        elif s1 == "/":
            if number_2 == 0:
                print("can't devide by zero")
            else:
                result = number_1 / number_2
                print(f"the answer is {result}")
        else:
            _sign_()
        
    _sign_()
    def repeat():
        again = input("do you want to run it again (y/n)  : ")
        if again == "y":
            calculator()
        elif again == "n":
            exit()
        else:
            repeat()

    repeat()
        
calculator()


















