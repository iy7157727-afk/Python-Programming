# Python Sets
country_names = {'Pakistan','USA','Canada'}
print(country_names)
print(type(country_names))
# Access Items in sets
#print(country_names[2])
for x in country_names:
   print(x)
# Len Function in set
print(len(country_names))

#Set Constructor
country_names = set(('Pakistan','USA','Canada','Canada'))
print(country_names)
print(type(country_names))

#Check if item exists
country_names = {'Pakistan','USA','Canada'}
print('Canada' in country_names)
print('Japan' in country_names)
print('Australia' not in country_names)
print('Pakistan' not in country_names)
#Update, Add, and Remove in set
country_names = {'Pakistan','USA','Canada'}
country_names.add('Japan')
print(country_names)
country_names.remove('Canada')
print(country_names)
country_names.discard('USA')
print(country_names)
#del country_names
#print(country_names)
#Set Functions
country_names = {'Pakistan','USA','Japan','Canada'}
countries = {'Pakistan','USA','Portugal','Norway'}
country_names.add('Norway')
print(country_names)
country_names.clear()
print(country_names)
countries_list = country_names.copy()
print(countries_list)
country_names.discard('Japan')
print(country_names)
country_names = {'Pakistan','USA','Canada','Norway','Japan'}
print(country_names.pop())
country_names.remove('Pakistan')
print(country_names)
print(country_names.difference(countries))
country_names.difference_update(countries)
print('difference = ',country_names)
country_names = {'Pakistan','USA','Canada','Japan'}
print(country_names.intersection(countries))
country_names.intersection_update(countries)
print('intersection = ',country_names)
print(country_names.isdisjoint(countries))
print(country_names.issubset(countries))
print(country_names.issuperset(countries))
print(country_names.symmetric_difference(countries))
country_names.symmetric_difference_update(countries)
print('symmetric_difference = ',country_names)
print(country_names.union(countries))
country_names.update(countries)
print('countries_union = ',country_names)
