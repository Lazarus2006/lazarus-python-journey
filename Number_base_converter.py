decimal = 0
binary = 0
hex = 0 
option = 0

def dec_to_bin(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

def dec_to_hex(decimal):
    if decimal == 0:
        return "0"
    
    char_list = "0123456789ABCDEF"
    hex = ""
    
    while decimal > 0:
        remainder = decimal % 16
        hex = char_list[remainder] + hex
        decimal = decimal // 16

    return hex

def bin_to_dec(binary):
    decimal = 0
    binary = binary[::-1]

    for i in range(len(binary)):
        if binary[i] == "1":
            decimal += 2 ** i
    return decimal

def binary_to_hex(binary):
    hex = ""
    binary = str(binary)
    while len(binary) % 4 != 0:
        binary = "0" + binary

    char_dic = {"0000" : "0" , "0001" : "1" , "0010" : "2" , "0011" : "3" ,
                "0100" : "4" , "0101" : "5" , "0110" : "6" , "0111" : "7" ,
                "1000" : "8" , "1001" : "9" , "1010" : "A" , "1011" : "B" ,
                "1100" : "C" , "1101" : "D" , "1110" : "E" , "1111" : "F" }

    for i in range(0, len(binary), 4):
        char = binary[i:i+4]
        hex += char_dic[char]
    
    return hex

def hex_to_dec(hex):
    decimal = 0
    hex_dic = { '0': 0, '1': 1, '2': 2, '3': 3,
                '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15}    
    
    hex = hex[::-1]
    
    for i in range(len(hex)):
        char = hex[i]
        value = hex_dic[char]

        decimal += value * (16 ** i)

    return decimal

def hex_to_bin(hex):
    binary = ""
    char_dic = {"0" : "0000" , "1" : "0001" , "2" : "0010" , "3" : "0011" ,
                "4" : "0100" , "5" : "0101" , "6" : "0110" , "7" : "0111" ,
                "8" : "1000" , "9" : "1001" , "A" : "1010" , "B" : "1011" ,
                "C" : "1100" , "D" : "1101" , "E" : "1110" , "F" : "1111" }
    

    for i in range(0 , len(hex)):
        char = hex[i]
        binary = binary + char_dic[char]
    
    return binary

print("---Number base converter---")

while True:
    try:
        print("What kind of value you have ?")
        print("1. Decimal")
        print("2. Binary")
        print("3. Hex")
        option = int(input("Enter your choice : "))
        
        if option < 4 and option > 0:
            break
        else:
            continue

    except ValueError:
        print("Please enter valid inputs")
        print("")

if option == 1:
    while True:
        try:
            decimal = int(input("Enter the Decimal value: "))
            break
        except ValueError:
            print("Please enter numbers only")
            print("")

    binary = dec_to_bin(decimal)
    hex = dec_to_hex(decimal)
    
    print(f"The binary value is {binary}")
    print(f"The hex value is {hex}")

elif option == 2:
    while True:
        binary = int(input("Enter the Binary value: "))
        binary = str(binary)
        if set(binary) <= {"0" , "1"}:
            break
        else:
            print("Binary can only contain 0 and 1")
            print("")
            continue

    decimal = bin_to_dec(binary)
    hex = binary_to_hex(binary)

    print("")
    print(f"The decimal value is {decimal}")
    print(f"The Hex value is {hex}")

elif option == 3:
    while True:
        hex = input("Enter the hex value: ")
        hex = str(hex).upper()
        valid = set("0123456789ABCDEF")
        if set(hex) <= valid:
            break
        else:
            print("Please input valid Hex value ")
            print("")
            continue
    
    decimal = hex_to_dec(hex)
    binary = hex_to_bin(hex)

    print(f"The Decimal value is {decimal}")
    print(f"The Binary value is {binary}")