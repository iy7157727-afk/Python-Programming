# Python For Loop
s1 = "Python Programming"
for x in s1:
  print(x)
# The Range (start,step,end) function
for i in range(1,11):
  print(i)

for i in range(1,11,2):
  print(i)

for i in range(11):
  print(i)


for i in range(2,11,2):
  print(i)
else:
  print("Else Block")

# Pass Statement
for i in range(1,11):
  pass

# Pattern Programming
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end = ' ')
  print()

# Python Program to print all characters except vowels
s1 = input("Please enter any string:")
for x in s1:
    if x not in 'aeiou':
      print(x)

# Python Program to print all numbers from 1 to 100
sum = 0
for x in range(1,101):
  sum = sum + x
print(sum)

# Python Program to find sum of all odd numbers
sum = 0
for x in range(1,101):
  if x % 2 != 0:
    sum = sum + x
print(sum)

# Python Program to print numbers from 1 to 100
for x in range(1,101):
  if x % 2 == 0:
    print(x)

# Python Program to find Prime Numbers
x = int(input("Please enter any number if prime or not:"))
factors = 0
for i in range(1,x+1):
    if x % i == 0:
        factors = factors + 1
if factors == 2:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")
