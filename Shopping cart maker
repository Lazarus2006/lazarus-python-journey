#shopping cart 

cart = []
prices = []
total = 0 

while True:
    item = input("what do you wanna buy , (q to quit) : ")
    if item.lower() == "q":
        break
    else:
        while True:
            try:
                price = float(input(f"enter the price of the {item} :"))
                break
            except ValueError:
                continue
        
        
        cart.append(item)
        prices.append(price)


print("            ")
print("            ")
print("            ")
print("            ")

print("------#shopping cart#------")
for i,p in zip(cart,prices):
    print(f"{i:<10}  :    {p:.2f}")


for price in prices:
    total += price

print("")
print(f"your total is: {total:.2f}")




