principal =  None 
while True:
    s = input("Enter the principal amount: ")
    if s == "":
        continue
    try:
        principal = float(s)
        if principal <= 0:
            continue
        break
    except ValueError:
        continue

Rate = None
while True:
    R = input("Enter the Rate: ")
    if R == "":
        continue
    try:
        Rate = float(R)
        if Rate == 0:
            continue
        break
    except ValueError:
        continue
    
Time = None
while True:
    T = input("Enter the Time: ")
    if T == "":
        continue
    try:
        Time = float(T)
        if Time == 0:
            continue
        break
    except ValueError:
        continue

in_value = (1+ Rate/100)
amount = principal * pow(in_value, Time)
CI = float(amount) - principal

print(f"the total compound intrest is {CI}")
print(f"the return amount is {amount}")
