# Python Dictionary
person = {
    'name' : 'Shahveer',
    'age' : 34,
    'salary' : 50000
}
print(person)
print(type(person))

#Access Items
print(person['salary'])
print(person.get('salary'))
# Len function in dictonary
print(len(person))
#Dict Constructor
car = dict({
    'name' : 'Camry',
    'brand' : 'Toyota',
    'model' : 2018
})
print(car)
print(type(car))
#Check if item exists
print('age' in person)
print('country' in person)
print('brand' not in person)
print('salary' not in person)
# Get all keys and values function
print(person.keys())
print(person.values())

person = {
    'name' : 'Shahveer',
    'age' : 34,
    'salary' : 50000
}

for x in person.values():
   print(x)
print(person.items())

#Update , Add and Remove in a dict
person['age'] = 40
person['name'] = 'Anees'
print(person)

person['country'] = 'Canada'
print(person)

person.pop('age')
print(person)

del person['salary']
print(person)

#del person
#print(person)
#Looping Through Dictionary
person = {
    'name' : 'Shahveer',
    'age' : 34,
    'salary' : 50000
}
for x in person:
    print(person[x])

for x in person:
    print(x)

for x in person.items():
    print(x)

for (x,y) in person.items():
    print('x=',x,'y=',y)
    
for x in person:
    print(x,'=',person[x])

#Dictionary Functions
another_person = person.copy()
print(another_person)
third_person = dict(person)
print(third_person)

person.update({'name' : 'Shaheen'})
person.update({'salary' : 60000})
print(person)
person.clear()
print(person)
#Dict Functions
person.clear()
print(person)
first_person = person.copy()
print(first_person)
person = {'name' : 'Shahwaiz','age' : 26 , 'salary' : 60000}
print(person.get('name'))
print(person.items())
print(person.keys())
person.pop('salary')
print(person)
person.update({'age' : 50})
print(person)
print(person.values())
x = ('key 1','key 2','key 3')
y = 25
this_dict = dict.fromkeys(x,y)
print(this_dict)
person.popitem()
print(person)
person.setdefault('salary' , 100000)
print(person)
