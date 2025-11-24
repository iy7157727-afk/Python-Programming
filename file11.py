# While Loop Exercise 1
s1 = "Python Programming"
l = len(s1)
x = 0
while x < l:
    print(s1[x])
    x = x + 1

print("Exit")
# Python Program to print all characters except vowels
s1 = input("Please enter any string:")
l = len(s1)
x = 0
while x < l:
    if  s1[x].lower() not in 'aeiou':
        print(s1[x])
    x = x + 1

print("Exit")
# Python Program to find the sum off odd numbers from 1 to 100
x = 1
sum = 0
while x <= 100:
    if x % 2 != 0:
        sum = sum + x
    x = x + 1
print(sum)
# Python Program to find sum of all numbers from 1 to 100
x = 1
sum = 0
while x <= 100:
    sum = sum + x
    x = x + 1
print(sum)

sum = 0
x = ''
while x != 'N':
    x = (input("Please enter any number to add or enter N to exit:"))
    if x != 'N':
        sum = sum + int(x)
print(sum)
# Python Program to find Prime Numbers
x = int(input("Please enter number if prime or not:"))
factors = 0
i = 1
while i <= x:
    if x % i == 0:
        factors = factors + 1
    i = i + 1
if factors == 2:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")
