# Creating Dictionary with Two Lists
list1 = ['name','age','salary']
list2 = ['abdul',36,590000]
dictionary = dict(zip(list1,list2))
print(dictionary)

# Lambda Function
fun1 = lambda a , b , c : a * b * c
print(fun1(5,6,2))

def lambda_multiple ( n ):
    return lambda a : a * n

x = lambda_multiple( 10 )
print(x(2))

# Variable Scope
def func_scope():
    x = 10
    print(x)

func_scope()

x = 10
def func_scope():
    print(x)

func_scope()

x = 10
def func_scope():
    x = 20
    print(x)

func_scope()
print(x)

x = 10
def func_scope():
    global x
    x = 20
    print(x)

func_scope()
print(x)

# Python Modules
import math
s = math.sqrt(25)
print(s)

p = math.pi
print(p)

pow = math.pow(5,3)
print(pow)

from math import sqrt , pi , pow
s = sqrt(30)
print(s)

p = pi
print(p)

pow = pow( 5 , 2 )
print(pow)

import random
print(random.randint(10,50))

import math as m
x = m.sqrt(25)
print(x)

import math
print(dir(math))

# Python Program to find factorial
f = math.factorial(5)
print(f)

# Python Classes/Objects
class Person:
    name = "John"
    age = 25
    salary = 500000

p1 = Person()
print( p1.name )
print(p1.age)
print(p1.salary)

class Person:
    def __init__(self, age):
        self.age = age

p1 = Person(25)
print( p1.age )

p2 = Person(30)
print( p2.age )

class Person:
    def __init__(self,age):
        self.age = age

    def display_age(self):
        print( " Age is :", self.age)

p1 = Person(25)
p1.display_age()

p2 = Person(30)
p2.display_age()

class Person:
    pass

# Python Inheritance
class A:
    def __init__(self,a):
        self.a = a

    def display__a(self):
        print( "a =", self.a)

class B (A):
    def __init__(self, a,b):
        super().__init__(a)
        self.b = b
    
    def display__b(self):
        print( "a=", self.a, "b=", self.b)

o1 = B(10,20)
print(o1.a)
print(o1.b)
o1.display__a()
o1.display__b()

# Access Modifiers
class A:
    def __init__(self,a):
        self.a = a

    def display(self):
        print( "a=", self.a)

o1 = A(10)
print(o1.a)
o1.display()

class A:
    def __init__(self, a):
        self._a = a

    def display(self):
        print( "a=", self._a)

o1 = A(10)
print(o1._a)
o1.display()

class A:
    def __init__(self, a):
        self.__a = a

    def display(self):
        print("a=", self.__a)

class B(A):
    def __init__(self, a):
        super().__init__(a)

    def display(self):
        print( "a=", self._A__a)

o1 = A(10)
print(o1._A__a)
o1.display()

# Operator Overloading
class A():
    def __init__(self, n):
        self.a = n

    def __ne__(self, x):
        return self.a != x.a
    
a1 = A(500)
a2 = A(50)
print(a1!=a2)

# Magic Methods
class Test():
    def __init__(self, n):
        self.a = n

    def __str__(self,x):
        return self.a 
    
t1 = Test(10)
t1 = str(10)
print(t1)

'''import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    database = "mydatabase"
)'''

'''mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()'''
