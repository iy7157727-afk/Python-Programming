#Continue
x = 1
while x <= 10:
    if x == 6:
        x = x + 1
        continue
    print(x)
    x = x + 1

s1 = "Hello World"
for x in s1:
    if x in 'aeiou ':
        continue
    print(x)

#Break
s1 = "HelloWorld"
for x in s1:
    if x == ' ':
        break
    print(x)
sum = 0
while True:
    x = input("Please enter any number to add or enter N to exit:")
    if x == 'N':
        break
    sum = sum + int(x)

print(sum)

s1 = "Hello World"
for x in s1:
    if x == ' ':
        break
    print(x)
else:
    print("For Else")
