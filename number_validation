def number_validation():
    n = input("enter your number :")
    num_length = len(n)
    ls = n.isdigit()
    verify = "next" if num_length == 10 and ls == True else "invalid number, please provide a valid number :"
    print(verify)
    if verify != "next":
        number_validation()
        
number_validation()
