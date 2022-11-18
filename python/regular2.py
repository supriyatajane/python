import re

#search
qq='aun shine sum times day'
ss=re.search(r's\w\w',qq)
if ss:
    print('occurences is find')
    print(ss.group())
else:
    print('occurences not found')

ww='map more manage'
ww1=re.search(r'm\w\w',ww)
if ww1:
    print('occurence find')
    print(ww1.group())
else:
    print('not found')

#findAll
qq='may life is my life'
qq1=re.findall(r'l\w\w\w',qq)
print(qq1)
for i in qq1:
    print(i)

#match
str='sun wiill rise tommorow again'
dd=re.match(r's\w\w',str)
if dd:
    print('string is match')
    print(dd.group())
else:
    print('string not match')

#sub
sts='i am Tester'
rr=re.sub(r'Tester','Developer',sts)
print(rr)

#spilt
sts2='I am learning javascript,cypress'
ff=re.split(r'\W+',sts2)
print(ff)

#-----------------------------------------------------
#\w  ===>  [a-z] [A-Z][0-9]
#\b     ===> " "
#\W     ===> not [a-z][A-Z][0-9]
#\d     ===> [0,9]
str6 = 'an apple a day keeps the doctor away'
e6 = re.findall(r'\ba[\w]*\b',str6)
print(e6)

str2='by the b is ball ballon'
e=re.findall(r'\bb[\w]+\b',str2)
print(e)
#* 0 or more reptitions  0 > 2
#+ 1 or more repetation  1, more repetion

str3= 'i am 22th way to 40th'
e1=re.findall(r'\d[\w]*\b',str3)
print(e1)

e2=re.findall(r'\d',str3)
print(e2)