##count
#it is using some elements



z = ['c', 'h', 'i', 'n', 'm', 'a', 'Y', 'N']
print(z.count('h'))
print(z.count('N'))

coach1 = ['M', 'I', 'N', 'S', 'K', 'O', 'L', 'E']
print(coach1.count('I'))

#POP
# it is use to remove lat element in list
print('-------------------------------------------------')
coach1 = ['M', 'I', 'N', 'S', 'K', 'O', 'L', 'E', 'E']
coach1.pop()
coach1.pop()
print(coach1)

# we alo provide index of pop the element

coach1.pop(2)
print(coach1)

#coach1.pop(6)#if the index not found they dhow the error
#print(coach1) -->IndexError: pop index out of range

#-----------------------------------------------------------------------------------------

#  remove
#it removes the the first occurnces
print('===============remove============================')

coach1 = ['M', 'I', 'N', 'S', 'K', 'O', 'L', 'E']
coach1.remove('M')
print(coach1)

#  reverse
print('===========================reverse======================')
name=['s','u','p','r','i','y','a']
#print(name[::-1])
name.reverse()
print(name)

vowels=['a','e','i','o','u']
vowels.reverse()
print(vowels)

print('=======================Sort=============================')
#  sort
alpha1 = ['Z','A', 'E', 'I', 'O', 'U']
alpha1.sort()
print(alpha1)

name=['s','u','p','r','i','y','a']
name.sort()
print(name)

nm=['a','b','L','D']#here sort capital letters first AsCii value
nm.sort()
print(nm)

# mm=[1,2,3,'m','l'] ot supported between instances of 'str' and 'int'
# mm.sort()
# print(mm)