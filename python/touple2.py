
#1 . UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT
z = ([22,33], [True,False],[0,1],[111,999])

a,b,c,d=z
print(c[0])

print('---------------------------------')
# #2. UNPACK THE TUPLE AND PRINT 9 AFTER UNPACKING IT 
t_num = (1,2,3,4,5,6,7,8,9)
     #,,c,,,_ = t_even
_,_,c,_,_,_,_,_,_=t_num
print(_)
print('---------------------------------')

# #3. convert the list into sets:
name1 = ['R', 'A', 'H', 'U', 'L']
name2 = ['A', 'K', 'S', 'H', 'A', 'Y']
bool3 = [True, False, False, False, True]

print(set(name1))
print(set(name2))
print(set(bool3))

print('---------------------------------')
## use for loop to print the items of  the set

d = set([True, False, False, False, True])

for i in d:
   print(i)
