# Python Strings
x = "South Korea"
print(x)
print(type(x))
# Multiline Strings
y = """Bahria Town 1
Phase 1
Phase 2
Phase 3
Phase 4
"""
print(y)
print(type(y))
# Strings are arrays
z = "Python Input"
print(z[0])
print(z[1])

print(z[-7])
print(z[-5])
# String Length
print(len(z))
# String in and not in operators
z = "Python Input"
print("put"  in z)
print("rog" not in z)
# Slicing 
x = "Python Output"
print(x[0:3])
print(x[3:6])

print(x[-9:-6])
print(x[-6:-3])

print(x[3:])
print(x[:3])

print(x[-3:])
print(x[:-3])

# String Concatenation
t1 = "Microsoft"
t2 = "Office"
t3 = t1 +' '+ t2
print(t3) 
print(t2*3)
print("Microsoft " + "Excel")

# String Format
item = "melon"
qty = 2
price = 20
s1 = "I want {} kg {} for {} pounds "
print(s1.format(qty,item,price))

# Escape Sequencing
x = "Pakistan is a \n great country"
print(x)

# String Methods
x = "Great Pakistan"
print(x.upper())
print(x.lower())
print(x.isupper())
print(x.islower())
print(x.capitalize())
print(x.title())
print(x.split(','))
print(x.replace("Great", "Grow"))
print(x.strip())
print(x.lstrip())
print(x.rstrip())
print(x.isdigit())
print(x.isnumeric())
print(x.isalpha())
print(x.istitle())
print(x.isdecimal())
print(x.isalnum())
print(x.isspace())
print(x.swapcase())
print(x.center(10))
