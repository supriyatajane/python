#string methods
#slicing
from datetime import date
from tokenize import Number


city='pune'
# 0   1  2  3
# p   u   n    e
# -4  -3  -2  -1

print(city[1])
print(city[-1])
print(city[1:3:2])
print(city[::-1])

# for loop string
city2='sangamaner'

for s in city2:
    print(s)

#2---Upper
city3='Nagar'
l=city3.upper()
print(l)

#3---Lower
city4='nasik'
p=city4.lower()
print(city4)

#4---isUpper---return boolean value
city5='aKola'
print(city4.isupper())

#5-----------isLower
city6='gujarat'
print(city6.islower())

#6-------------capitalize()------------firt letter to the capital letter
city7='parner'
o=city7.capitalize()
print(o)

#7------------startswith()

city8='baner'
print(city8.startswith('ba'))

#8----------------endswith()

city9='kota'
print(city9.endswith('a'))

#9--#index
city10='manmad'
print(city10.index('m'))
print(city10.index('d'))

#10---#count 

city11='nagar'
print(city11.count('a'))

#11---# replace
quaote=' I am Tester'
l=quaote.replace('Tester','Developer')
print(l)

#12
code1 =  'ZAQ!@WSX'
print(code1.isspace())

#13
#strip---remove space between string
fruits=" Apple "
print(fruits)

print(fruits.strip())

#14
#spilt
date1='1-10-2022'
print(date1.split("."))


#type conversion/casting
name='supriya'

print(list(name))

