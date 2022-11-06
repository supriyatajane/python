from functools import reduce 
#its import for reduce
#program1
birthyear=[1999,1998,2000,2002]
age=[]

for i in birthyear:
    c=2022-i
    age.append(c)

print(age)   

#program2
#using map
ageC=list(map(lambda x:2022-x,birthyear))
print(ageC)

#program3
number=[11,22,33,44,55]
#add every elemnt 2
addc=list(map(lambda x:x+2,number))
print(addc)

#program 4
#multiple by 3
mulc=list(map(lambda x:x*3,number))
print(mulc)

#program 5
no=[10,11,2,3,4,20,34]
nos=[]

for i in no:
    if i>10:
        nos.append(i)

print(nos)

#program 6
#using filter
ff=list(filter(lambda x:x>10,no))
print(ff)

#program 7
evens=[11,22,33,44,55,66,77]
hh=list(filter(lambda x:x%2==0,evens))
print(hh)


#program 8
odd=list(filter(lambda x:x%2!=0,evens))
print(odd)

#program 9
users=['supriya','sarika','diya','om']
rr=list(filter(lambda x:len(x)==4,users))
print(rr)

#progarm 10
sums=[11,22,33,44,55]
qq=0
for i in sums:
    qq=qq+i
print(qq)

#using reduce
print(reduce(lambda acc,nextval:acc+nextval,sums))
print(reduce(lambda acc,nextval:acc+nextval,sums,10))
print(reduce(lambda acc,x:acc+x,sums,40*3))
