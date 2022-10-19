
# operators 

# 1)comparison  operator
# 2)logical operator

# < , > , == , !=  <= , >=
# entity < entity  ==================> boolean
# <  ==> less than
# >  ==> greate than
# <=  ==> less than or equal to
# >=  ==> greater then or equal to
# ==  ==> equal tham
# !=  ==> not equal


print(1<=1)
print(5==3)
print(10>=9)
print(4!=4)


#logiacal operator
# or and  not

# and
# True  and  True  ==> True
# False and  True  ==> False
# True  and  False ==> False
# False and  False ==> False

#or

# True  or  True  ==> True
# False or  True  ==> True
# True  or  False ==> True
# False or  False ==> False

# not 

#True ==> False
#False ==> True 
print('=============logical-======================')
#or
print(3==3 or 5!=5)

print(3==4 or 5>=10)

print(True or False)

print('------------------------and-----------------------')

print(3==3 and 5!=5)

print(3==4 and 5>=10)

print(True and False)


print(5!=4 and 1<10)


print('-------------not--------------')

print(not True)
print(not False)
print(not 8==5)
print(not 3==6)

# conditional statement 
# single input =====>    multiple statement

print('-------------------if-------------')
mark=120

if(mark<=200):
    print('this is pass')
else:
    print('not pass')

m=25

if(m>=0 and m<=5):
    print('number of discount 5%')
elif(m>=5 and m<=10):
    print(' discount 10%')
elif(m>=10):
    print('discount 25%')


marks=90
if(marks>=90):
    print('distinction class')
elif(marks>=60):
    print('first class')
elif(marks>=35):
 print('pass')