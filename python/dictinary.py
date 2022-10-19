from copy import copy


s=(11,22)#-------this is touple

print(type(s))
print(s)

d=[11,22,33,44]#---------this is list
print(type(d))
print(d)

q={11,33,55,66}# this is set
print(type(q))
print(q)

print('-------------Dictinary------------------')

dict={}# this is dict
print(type(dict))

#dictinary does not stores the value by index

person={
    'firstName':'supriya',
    'lastname':'Tajane',
    'skill':['javascript','typescript','cypress']
}
print(person)
print(type(person))

#retrive the value dict
print(person['firstName'])
print(person['skill'])

#second way to retrive elemnt
fn=person.get('firstname')
fnn=person.get('lastname')

#update the value dict
person['firstName']='Abhijit'
print(person)

#add the value in dict
person['Adress']='Mumbai'
print(person)

#delete the value in dict'
del person['skill']
print(person)



#duplicate keys in dict



animal = {
    'legs':2,
    'color':'red',
    'eyes':2,
    'legs':4
}
print(animal)

#mebership operator
print('leg' in animal)
print('legs' in animal)

print('----------------------loop----------')
#loop of dict

for ani in animal:
    print(ani,animal[ani])

print('----------methods in dict-----------------')
# thre are three methods in dict

print(animal.keys())

print(animal.values())

print(animal.items())


# using loop
for x in animal.keys():
    print(x)


for y in animal.values():
    print(y)

for x,y in animal.items():
    print(x,y)

s={
    'name':'ss'
}

# dict create refernce not craete new memory
p=s
p['name']='RANI'
print(p)
print(s)

# in copy create new memory
l=copy(p)
l['name']='sarika'
print(l)
print(p)


family = {
    'son':"Abhijit",
    'daughter':'supriya',
    'parent':{
        'mother':'alka',
        'father':'sunil'
    },
    'skills':["python","c++"]
} 
print(family['parent']['mother'])
family['skills'].append('java')
print(family)


j = {
    'studentOne':45,
    'studentTwo':90,
    'studentThree':45
}
print(sum(j.values()))

