# Identation Error
d = [1, 2, 3, 5, 6]
sum = 0
for x in d:
    s = x*x
sum += s
print(sum)

d = [1, 2, 3, 5, 6]
sum = 0
for x in d:
    s = x*x
    sum += s
print(sum)

# Naming Conflicts
#len = 100
x = "Hello World!"
print(len(x))

# Mutable Default Args
def add_names(name , name_list = [] ):
    name_list.append(name)
    print(name_list)

names = ['Adnan','Tariq']
add_names('Tahir',names)
add_names("Rayyaz")
add_names("Mahmood")

def add_names(name , name_list = None):
    if name_list is None:
        name_list = []
        name_list.append(name)
        print(name_list)

names = ['Tahir','Adnan']
add_names("Tariq",names)
add_names("Rayyaz")
add_names("Qasim")

# Object Copy Problem
a = [10, 20, 30, 40, 50]
b = a
print(a)
print(b)
a[1] = 1000
print(a)
print(b)

a = [10, 20, 30, 40, 50]
b = a.copy()
print(a)
print(b)
a[2] = 3000
print(a)
print(b)
