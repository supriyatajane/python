import re
#in regular expression in phython we need import this

# 'm\w\w' // [a-z][A-Z][0-9] // nor special symbol
print('-----------------------------sesrch()-------------------')
#program 1
str="sun will rise again will"
e=re.search(r'w\w\w',str)
print(e.group())


r=re.search(r'a\w',str)
print(r.group())

#program2
str2='keeps the hope one day will be sucess'
ff=re.search(r'k\w\w\w',str2)
print(ff.group())

#in seearch method we pass string then search and returns it
print('-----------------findall()----------------------')
#findall	Returns a list containing all matches
#program 3
sts='Dont judge book by covers ,bamit'
gg=re.findall('b\w\w\w',sts)
print(gg)
for i in gg:
    print(i)

#program 4

sts2='map mau mani machine'
hh=re.findall(r'm\w\w',sts2)
print(hh)

for i in hh:
    print(i)

print('----------------------------------sub()------------------')
#sub	Replaces one or many matches with a string
#program 5
ss='I proud of sangamaner'
dd=re.sub(r'sangamaner','India',ss)
print(dd)

#program6
ss1='improve our hardwork'
dd1=re.sub(r'hardwork','confidence',ss1)
print(dd1)

#match
print('------------------match()----------------------------')
strs='sun always shine'
sss=re.match(r'd\w\w',strs)
if sss:
    print('occurences found')
    print(sss.group())
else:
    print('not found')


str5 = "sun sand surface sub"
e6 = re.match(r's\w\w',str5)
if e6:
    print('occurence found')
    print(e6.group())
else:
    print('no occurence')