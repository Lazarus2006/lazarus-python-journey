weight = float(input("what is your weight"))
unit = input("what is the unit of your weight (kg/lb): ")
if unit.lower() == "kg":
   weight_in_lb = weight * 2.20462
   print(f"Your weight in pounds is: {weight_in_lb:.2f} lb") 
elif unit.lower() == "lb":
   weight_in_kg = weight / 2.20462
   print(f"Your weight in kilograms is: {weight_in_kg:.2f} kg")
else:
   print("Invalid unit. Please enter 'kg' or 'lb'.")
