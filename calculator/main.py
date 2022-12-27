Name = input("Enter your name:\n")

print("\nWelcome " + Name + " Good name.") 

print("\nCalculator lets start\n")

num_1 = int(input("Enter your first number:\n"))            

oop = input("Enter operator:\n")

num_2 = int(input("Enter your second number:\n"))    

print(Name + " Your Total is:\n")

if oop == "+":
   print(num_1 + num_2)
  
elif oop == "-":
  print(num_1 - num_2)

elif oop == "*":
  print(num_1 * num_2)

elif oop == "/":
  print(num_1 / num_2)

print("Thank you " + Name)