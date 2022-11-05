#functions in python

print('hello')

x='hello'
print(x)
print(len(x))

x=10
y=10
print(x+y)

a=10
b=5
print(a-b)


# syntax 

'''
def name_of_function(x,y,z,....):
    code 

'''

#function without parameter 
print('-------function without parameter------')
def div():
    print('hello')

def demo():
    print('bye')

div()
demo()

print('----------function with parameter-------------')
#function with parameter
def add(x,y):
    print(x+y)

add(2,3)
add(5,6) 

#functions returns some value

def sub(a,b):
   return a-b

ss=sub(10,5)
print(ss)


def div(a,b):
    return a/b

dd=div(4,2)
print(dd)


#functions returns multiple values
def common(a,b):
  return a-b,a*b,a+b


dd=common(4,2)
print(dd)

#default values

def greet(name,age,city='pune'):
    print(name,age,city)

greet('supriya',22,'sangamaner')
greet('ss',22)



def geets(name,age=22,city='loni'):
    print(name,age,city)

geets('supriya')
