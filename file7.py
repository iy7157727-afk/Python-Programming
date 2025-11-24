# Arithmetic Operators
x = 2020
y = 400


z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)
z = x % y
print(z)
z = x ** y
print(z)
z = x // y
print(z)

# Comparison Operators

print( x == y)
print( x != y)
print( x > y)
print( x >= y)
print( x < y)
print( x <= y)
# Logical Operators
#exp1 (LO) exp2
#and
x = 160
y = 180
z = 200
# AND Operator
print( x < y and z < 100)
print( x > y and z < 100)
print( x < y and z > 100)
print( x > y and z > 100)
print( True and False)
print( True and True)
#OR Operator
print( x < y or z < 100)
print( x > y or z < 100)
print( x < y or z > 100)
print( x > y or z > 100)
print( True or False)
print( False or False)
#Not Operator
print (not( 10 > 2))
print(not(50 < 25))
print(not(True))
# Assignment Operators
x = 200
y = 100
x = x + y
#x += y
print(x)

x = 200
y = 100
x = x - y
#x -= y
print(x)

x = 200
y = 100
x = x * y
#x *= y
print(x)

x = 200
y = 100
x = x / y
#x /= y
print(x)

x = 200
y = 100
x = x % y
#x %= y
print(x)

x = 200
y = 100
x = x // y
#x //= y
print(x)

x = 200
y = 5
x = x ** y
#x **= y
print(x)

x = 33
y = 57
x = x & y
#x &= y
print(x)

x = 33
y = 57
x = x | y
#x |= y
print(x)

x = 33
y = 57
x = x ^ y
#x ^= y
print(x)

x = 33
y = 57
x = x >> y
#x >>= y
print(x)

x = 33
y = 57
x = x << y
#x <<= y
print(x)

# Identity Operators
x = 500
y = 500
print(x is y)
y = 50
print(x is not y)
# Membership Operators
x = "New"
y = "Zealand"
print(x in y)
print(x not in y)
