'''
1 .DATA TYPES IN PYTHON
> NUMBERS 
    > INT       :1 2 3 4  400
    > FLOAT     :3.14 22.22 0.033
    > COMPLEX  : 1+2J
> BOOLEAN True/False 0/1
>LIST [any type of data ]
>STRINGS '' or " " or ''' '''
> TUPLE ()
> SETS {}
'''
import numbers


k=(12)
print(k)
print(type(k))

kl=(12,)
print(type(kl))

#in touple we can store the multple values then this type of touple
#if you can store the only one values that is not touple

kk={}
print(type(kk))

k1={0,1}
print(type(k1))

#Set

s=set()
print(s)


name='SupRiyar'
print(set(name))

print('------------set method--------------------')
#methods in set
print(len(name))


d={'diya','siya','diya','riya'}

for i in d:
    print(i)

 #len
    print(len(d)) 

numbers={11,22,33,44,55,66}  
print(len(numbers))

# add
numbers.add(100)
print(numbers)

print(numbers.add((200)))

print(numbers)

#sorted
print(sorted(numbers))

#remove
numbers.remove(200)
print(numbers)

#clear
numbers.clear()
print(numbers)

animals=['lion','tiger','chhita','Dog']

for i in range(len(animals)):
    #print(i)
    print(animals[i])
