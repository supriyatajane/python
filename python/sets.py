
# 👉 TUPLES  IN PYTHON
# 👉 PACKING/UNPACKING TUPLES  IN PYTHON
# 👉 SETS  IN PYTHON

a=False
b=True
print(int(a))
print(int(b))

c=123
print(str(c))

d='fss'
# print(int(d))  we cannot convert the string into int

# PACKING/UNPACKING TUPLES  IN PYTHON
a,b,c='supriya','sunil','Tajane'
print(c)

t_even=(2,4,6,8,10)
print(t_even[0])
print(t_even[1])

#unpacking touples
city='pune','mumbai','delhi','ncr'
aa,bb,cc,dd=city

print(aa)
print(bb)


country='japan','america','china','landon','India'

a,b,c,_,_=country
print(a)
print(b)
print(_)

# set is an unordered collection of unique elements

p=[True,True,False,False]

print(set(p))

list_new = [12,14,1.44,3.14,"NUm1", True, (True,False),[33,66,99]]


#print(set(list_new))

n='nayan'
print(set(n))

for i in n:
    print(i)
# we can not call elements of  a set by calling the index position

# but we can use loop for calling