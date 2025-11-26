# Python Output
p = 20
q = 40
r = 50
print(p,q,r)
# Python Concatenation of int into str
name = "Furqan"
age = 36
country = "China"
print("My name is" ,name, "and I Live in " ,country)
print("My name is " ,name, "and my age is " ,age)
print("My name is " +name+  " and I Live in " +country)
print("My name is " +name+ " and my age is " +str(age))
print(f"My name is {name} and I Live in {country} " )
print(f"My name is {name} and my age is {age}")
print("Print 1" , "Print 2" , "Print 3" ,sep = '$#$')
print("Print World 1" ,end = ' = ')
print("Print World 2" ,end = ' = ')
print("Print World 3")
# Input starts here
name = input("Please enter your name: ")
print("Your name is" ,name)
print(type(name))
n = int(input("Please enter n: "))
m = int(input("Please enter m: "))
p = n + m
print(f"Sum of {n} and {m} is {p}")

# Python Program to Swap Two Numbers
x = input("Please enter x:")
y = input("Please enter y:")
z = x
x = y
y = z
print(x)
print(y)
