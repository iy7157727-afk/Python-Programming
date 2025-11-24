# Python Tuples
weekdays = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
print(weekdays)
print(type(weekdays))

#Indexing in Tuple
print(weekdays[2])
print(weekdays[-4])
#Creating Tuple with Single Item
country = ('Pakistan',)
print(country)
print(type(country))
#Slicing of Tuple
weekdays = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
print(weekdays[2:5])
print(weekdays[4:])
print(weekdays[:4])
print(weekdays[-5:-4])
print(weekdays[-2:])
print(weekdays[:-5])
print(len(weekdays))
#Tuple Constructor
weekdays = tuple(('Mon','Tue','Wed','Thu','Fri'))
print(weekdays)

#Update, Add, and Remove in a Tuple
weekdays = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
#weekdays[2] = 'Wed'
#print(weekdays)

weekdays_list = list(weekdays)
print(weekdays_list)
weekdays_list[5] = 'Tue'
print(weekdays_list)
weekdays_list.insert(5,'Sat')
print(weekdays_list)
weekdays_list.pop(6)
print(weekdays_list)
weekdays = tuple((weekdays_list))
print(weekdays)
#Add tuple to tuple
month1 = tuple(('Jan','Feb','Mar'))
month2 = tuple(('Apr','May','Jun'))
months = month1 + month2
print(months)
#Unpacking a Tuple
weekdays = ('Mon','Tue','Wed','Thu','Fri')
(day1,day2,day3,day4,day5) = weekdays

print(day1)
print(day2)
print(day3)
print(day4)
print(day5)
#Looping Through a Tuple
weekdays = ('Mon','Tue','Wed','Thu','Fri')
for days in weekdays:
    print(days)

l = len(weekdays)
i = 0
while i < l:
    print(weekdays[i])
    i += 1

#Multiply Tuples
weekdays = ('Mon','Tue','Wed','Thu','Fri')
print(weekdays*10)
# Tuple Functions
weekdays = ('Mon','Tue','Wed','Thu','Fri','Mon')
print(weekdays.count('Mon'))
print(weekdays.index('Tue'))
#del weekdays
print(weekdays)
