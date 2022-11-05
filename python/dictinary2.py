dict_student = {
    'name' : 'Akash',
     'marks' :  58,
     'rank' : '4th',
     'one' : [1,2,4,5,6,78],
     'two': (7,77,77,777),
    # [1,11] : (5,5) # unhashable type: 'list
   (5,55,555) : 'Minskole'
    }
print(dict_student)

# removing objects

#pop
dict_student.pop('rank')
print(dict_student)


#popItems //remove latest entry
dict_student.popitem()
print(dict_student)


dict_student1=dict_student.copy()
print(dict_student1)

del dict_student
#print(dict_student)


dict_student = {
     'name' : 'Akash',
   'marks' :  58,
    'rank' : '4th',
    "nSem" : 90
 }
#1#update
dict_student.update({'marks':222})
print(dict_student)


a = dict(one = 1 , two = 2, three= 3)

print(a)

a = dict(one = 1 , two = 2, three= 3)

print(a)

c=dict(name='supriya',lastname='tajane')
print(c)
print(type(c))

#get
print(dict_student.get('name'))

#clear
dict_student.clear()
print(dict_student)

#fromKeys
keys=['name','lastname','age']
y='none'

d=dict.fromkeys(keys,y)
print(d)


x=['name','job']
y='supriya','tester'

f=dict.fromkeys(x,y)
print(f)


#setDaefault
person={
    'nname':'diya',
    'job':'Tester'
}
person.setdefault('salary','1000')
print(person)