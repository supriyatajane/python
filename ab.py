print('hello')# # OPERATORS IN LIST

#concatenation
z1 = [1,1,1,1]
z2 = [2,2,2,2]

# print(z1, z2)
# print(z1 + z2) #concatenation

# n1 = z1 +z2
# print(n1)

# print(n1 + z1)

# i1  = ['C', 'H', 'I', 'N', 'M', 'A', 'Y'] 


# print(z1 + i1)

#mul

# print(z1*3) # repeat the elemnt n number of times
# print(z2*2) # repeat the elemnt n number of times

# i1  = ['C', 'H', 'I', 'N', 'M', 'A', 'Y']

# print(i1*3)

# sub
# z1-z2

# # div
# z1/z2 

# #################################################
# max()
#  wont work in mixed list
# #################################################
# list_marks1 = [7,8,9,4,5,99]

# print(max(list_marks1))
# list_marks2 = ['5', '6', '7', '8', '9999']
# print(max(list_marks2))

# i  = ['C', 'H', 'I', 'N', 'M', 'A', 'Y', 'Z'] 
# print(max(i))

# z = ['Z','c', 'h', 'i', 'n', 'm', 'a', 'Y','z' ]
# print(max(z)) # check for ASCII values HW

# #################################################
# #  min()
# #################################################
# # HW try min() on all lists present in max()

# z = ['Z','c', 'h', 'i', 'n', 'm', 'a', 'Y','z' ]
# print(min(z)) # check for ASCII values HW

# # for knowledge seekers read  about ASCII
# #################################################
# #  append() # at the end
# # #################################################

# runs = [5,5,4,2,4]
# # return value =  None
# runs.append(6) # original list will be appended
# print(runs)

# alpha_num = ['f', 'd', 'a', 'g', 'h', 'e', 'c', 'b']
# alpha_num.append('z')
# print(alpha_num)

# alpha_num.append(1234)
# print(alpha_num)


# alpha_num.append([1234])
# print(alpha_num)
#################################################
#  extend 
# will work with iterabels 
#  will try to unwrap each items 
#################################################

z1 = [1,1,1,1, 'one']
z2 = [2,2,2,2,'two']
# z1.extend(z2)
# print(z1)


# z2.extend(z1)
# print(z2)

# z1.extend('two')
# print(z1)

# z1.extend([two])
# print(z1)

# z1.extend('555') # int' object is not iterable
# print(z1)

# z1.extend('t') # int' object is not iterable
# print(z1)

#################################################
#  insert # at the given index
#################################################

banks_India = ["HDFC Bank",
"State Bank of India",
"ICICI Bank",
"Axis Bank",
"Kotak Mahindra Bank",
"IndusInd Bank",
"Yes Bank",
"Punjab National Bank"]

# print(banks_India)

# banks_India.insert(0,'UCO bank')

# print(banks_India)

# banks_India.insert(0,['UCO bank1', 'UCO bank2'])

# print(banks_India)
# print(banks_India[0])

#################################################
#  index
#################################################

alpha_num = ['f', 'd', 'a', 'g','b', 'h', 'e', 'c', 'b']

x = alpha_num.index('b') # gives return value

print(x) # 1st occur