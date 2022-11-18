import re

#\w  ===>  [a-z] [A-Z][0-9]
#\b     ===> " "
#\W     ===> not [a-z][A-Z][0-9]
#\d     ===> [0,9]
#program 1
str='a an apple eat day and keep doctor away'
e1=re.findall(r'a[\w]*',str)
print(e1)

#program 2
e2=re.findall(r'\ba[\w]*\b',str)
print(e2)

#program 3
str2='this is 1st and 2nd start'
e3=re.findall(r'\d[\w]*',str2)
print(e3)

#program 4
e4=re.findall(r'\d',str2)
print(e4)

#program 5
str3 = "one two three four five six seven supriya 8 9 10"
e5=re.search(r'\b\w{5}\b',str3)
print(e5.group())

#program 6
e6=re.findall(r'\b\w{5}\b',str3)
print(e6)

#program 7
e7=re.findall(r'\b\w{4,}\b',str3)
print(e7)
#program 8
e8=re.findall(r'\b\w{3,5}\b',str3)
print(e8)

#program 9
e9=re.findall(r'\b\d\b',str3)
print(e9)
#D+ character
#d+ number
str6='supriya7447203759'
ee=re.search(r'\d+',str6)
print(ee.group())

ee1=re.search(r'\D+',str6)
print(ee1.group())

print('-----------------------------------------------------')
str6 = "anil ankur akshay anant akash arati abhijit abhay bomkesk a67"
#start with a
print(re.findall(r'\ba[\w]*\b',str6))
#start with an
print(re.findall(r'\ban[\w]*\b',str6))
#strt with
print(re.findall(r'\ba[nk][\w]*\b',str6))
#a follow digit
print(re.findall(r'\ba[0-9][\w]*\b',str6))
