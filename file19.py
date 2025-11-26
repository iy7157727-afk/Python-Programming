# Python Functions
def display():
    print("Hello World")
    print("Welcome to Display")

def show():
    print("Welcome to show")
display()
display()
show()
display()
display()
show()
# Function with arguments
def hello(a):
    print("a =",a)
hello(34)

def show_display(a,b):
    print("a =",a)
    print("b =",b)

show_display(1000,1500)

def sum(a,b):
    s = a + b
    print("Sum =",s)

sum(34,56)

# Default Parameter in python
def sum(a=1000,b=500):
    s = a + b
    print("Sum =",s)
sum()
# Pass any data type as argument
def list(x):
    print(x)

list([10,20,30,40,50,60])
# Return Values in function
def sum(a,b):
    s = a + b
    return s

s = sum(20,40)
print("s =",s)

# Pass Statement
def total():
    pass

# Python Program to check if number is odd or even
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
flag = is_even(39)
if (flag):
    print("Number is even")
else:
    print("Number is odd")
    
# Keyword Arguments in function
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

print_numbers(10,20,30)
print_numbers(c = 50,b = 25,a = 15)

# Arbitary Arguments
def print_numbers(a,b, *args):
    print(a)
    print(b)
    print(args)
    print(args[1])

print_numbers(10,20,30,40,50,50)

# Arbitary Keyword Argument
def print_numbers(a,b, **kwargs):
    print(a)
    print(b)
    print(kwargs)
    print(kwargs["age"])

print_numbers(a = 10,b = 20,c = 30,d = 40,name = "Abdul",age = 23,salary = 67000)

# Function Recursion
def print_rec(i):
    if i <= 5 :
        print("Hello World!")
        print_rec(i+1)
        return
    else:
        return

print_rec(1)
