def user_name():
    username = input("enter your username: ")
    space = username.find(" ")
    if space != -1:
        print("invalid username , your username can't contain spaces")
        user_name()
    elif len(username) > 12:
        print("your username can't be more than 12 characters")
        user_name()
    elif username.isalpha() == False:
        print("your username can't contain numbers or special characters")
        user_name()  
    else:
        print("valid username")

user_name()
