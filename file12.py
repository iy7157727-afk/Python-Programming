# Pattern Programming
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(j, end = ' ')
        j = j + 1
    print()
    i = i + 1


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end = ' ')
        j = j + 1
    print()
    i = i + 1
"""
*
* *
* * *
* * * *
* * * * *
"""
i = 1

while i <= 5:
    j = 1
    while j <= i:
        print('*', end = ' ')
        j = j + 1
    print()
    i = i + 1

print("Hello"*10)
i = 1
while i <= 5:
    print('*'*i)
    i = i + 1
