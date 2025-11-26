# Python If Else
x = 5
if x < 20:
    print("x is less than 20")
    print("Its in if")
    print("Another if")
else:
    print("x is not less than 20")
    print("Another Else")

print("End")

# Python Program to check if number is odd or even
x = int(input("Please enter any number:"))
if x % 2 == 0 :
    print(f"{x} is a even number")
else:
    print(f"{x} is a odd number")

# If Elif Else
x = int(input("Please enter marks:"))
if x > 80:
    print("Grade A")
    age = int(input("What is your age:"))
    if age < 20:
        print("Awesome! you are very young")
    else:
        print("Good")
elif x > 60:
    print("Grade B")
elif x > 50:
    print("Grade C")
else:
    print("Grade D")

print("Exit")
# Short Hand If
x = 14
if x < 20:
    print("x is less than 20")
   
#if x < 20: print ("x is less than 20")
# Short Hand If Else
x = 5
if x < 10:
    print("x is less than 10")
else:
    print("x is not less than 10")
print("x is less than 10") if x < 10 else print("x is not less than 10")
# Pass Statement
x = 2
if x < 20:
    pass
else:
    print("x is not less than 20")

# Python Program for Arithmetic Calculations
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("5: Modulus")
print("6: Floor Divide")
print("7: Exponentiation")

opt = int(input("Enter Option (1-7):"))
if opt == 1:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Sum of {x} + {y} = ", x + y)
elif opt == 2:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Difference of {x} - {y} = ", x - y)
elif opt == 3:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Product of {x} * {y} = ", x * y)
elif opt == 4:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Quotient of {x} / {y} = ", x / y)
elif opt == 5:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Modulus of {x} % {y} = ", x % y)
elif opt == 6:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Floor Division of {x} // {y} = ", x // y)
elif opt == 7:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print(f"Exponentiation of {x} ** {y} = ", x ** y)
else:
    print("Invalid Option")
