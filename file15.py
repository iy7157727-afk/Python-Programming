# Python List
fruit_names = ['Apple','Mango','Orange','Grapes']
print(type(fruit_names))

# Access Items in list
print(fruit_names[0])
print(fruit_names[-3])

#Slicing of List
print(fruit_names[1:3])
print(fruit_names[0:])
print(fruit_names[:2])

print(fruit_names[-3:-1])
print(fruit_names[-3:])
print(fruit_names[:-2])
# len function in list
print(len(fruit_names))

# List Constructor
fruit_names = list(('Apple','Mango','Banana','Orange','Grapes'))
print(fruit_names)
# Chect if item exists
print('Grapes' in fruit_names)
print('Kiwi' in fruit_names)
print('Watermelon' not in fruit_names)
print('Apple' not in fruit_names)

# Update Add and Remove in list
fruit_names = ['Apple','Mango','Orange','Grapes','Mango']
fruit_names[1] = 'Banana'
print(fruit_names)

fruit_names.append('Watermelon')
print(fruit_names)
fruit_names.insert(1,'Pine Apple')
print(fruit_names)
fruit_names.remove('Watermelon')
print(fruit_names)
fruit_names.pop()
print(fruit_names)
fruit_names.pop(2)
print(fruit_names)
del fruit_names[2]
print(fruit_names)
#del fruit_names
#print(fruit_names)
fruit_names = ['Apple','Mango','Banana','Orange','Grapes']
test_list = ['Test', 12 , 34.56 , False , fruit_names]
print(test_list)
# Looping through list
marks = [120,150,200,220,180]
for m in marks:
   print(m)

l = len(marks)
i = 0
while i < l:
    print(marks[i])
    i += 1
#Finding the max number in any list
marks = [120,150,200,220,180]
max = marks[0]
for m in marks:
    if m > max:
        max = m
print(max)

#List Comprehenshion
even = []
numbers = [20,50,68,89,100,119,34,8,19]
for n in numbers:
    if n%2 == 0:
        even.append(n)
print(even)
#newlist = [expression for item in iterable if condition == True]
numbers = [20,50,68,89,100,119,34,8,19]
even = [n*10 for n in numbers if n%2 == 0]
print(even)
fruit_names = ['Apple','Mango','Orange','Grapes']
print(fruit_names*5) 

#List Functions
fruit_names.append('Pineapple')
print(fruit_names)
fruit_names.clear()
print(fruit_names)
fruit_list = fruit_names.copy()
print(fruit_list)
print(fruit_names.count('Mango'))
fruit_names.extend('Orange')
print(fruit_names)
fruit_names = ['Apple','Mango','Orange']
print(fruit_names.index('Orange'))
fruit_names.insert(2,'Pineapple')
print(fruit_names)
fruit_names.pop(2)
print(fruit_names)
fruit_names.remove('Mango')
print(fruit_names)
fruit_names.reverse()
print(fruit_names)
fruit_names.sort()
print(fruit_names)
fruit_names.sort(reverse = True)
print(fruit_names)
