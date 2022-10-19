list = [11,22,33]
listA=list
listA[0]=33
print(listA)
print(list)

##in list not create new memory crate new refernce and point the old memory
##Copy
#here create new memory
listC=[11,22,33]
listD=listC.copy()
listD[1]=111
print(listD)
print(listC)


##String methods
#string also store values by index
print("------------------------------Defining string--------------")
first_name='supriya Tajane'
first_name1="supriya Tajane"

print(first_name)
print(first_name1)

multiline='''
I am learnning python
'''
print(multiline)

multiline2="""
hii
bye
"""
print(multiline2)


city='pune'
print(city[0])
print(city[1])

#loop string
for char in city:print(char)

print('==========================================Range========================')
#using range
for x in range(1,9):
    print(x)

for x in range(4):
    print(x)  


for x in range(len(city)):
    print(x)  


for x in range(len(city)):
    print(city[x])  

city2='Mumbai'
for l in city2:
    print(l)

for x in range(len(city2)):
    print(city2[x])

print('====================slice=================')

city4 = "chandrapur"

print(city4[2])
print(city4[-2])
print(city4[2:4])
print(city4[1:9:2])
print(city4[::-1])

q1=len(city4)
print(q1)