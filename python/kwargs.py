
#doc
def sum(a,b):
 '''
  this is calculate sum of the elements

'''
 print(a-b)
 print(a+b)
 print(a%b)
 print(a/b)

sum(10,10)
#dhunder
print(sum.__doc__)
print(len.__doc__)
#print(print.__doc_)
#print(print._doc_)

#DUNDER _var_  DUNDER VAR 


#default argument

def greet(name,greet='WEL-COME'):
    print(greet,name)


greet('supriya')


#if you pass multiple values then you use *args
#*args
def contact(*args):
    print(type(args))
    print(args)

contact(11,'a','b')


#if you pass the key and value that time we wiill use **kwargs
#**args 
def cont(**args):
    print(type(args))
    print(args)

cont(name='supriya',age=22,job='Tester')

dict={
    'name':'diya',
    'job':'developer'
}

cont(**dict)