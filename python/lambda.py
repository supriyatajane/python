# LAMBDA FUNCTION
#nameless
# anonymous
# ONE LINER FUNCTION

x=100
y=100

def sum(a,b):
    return a+b

ll=sum(x,y)
print(ll)

#syntax
# lambda x,y,z : expression
z=lambda x,y:x+y
print(z(10,10))

print((lambda a,b:a+b)(200,200))

#in two ways to write lamda function

def squ(num1,num2):
  return num1*num2

print(squ(10,10))

s=lambda a:a*a
print(s(2))

print((lambda a:a*a)(3))

print('------------------------------map-----filter------reduce')

list_score=[11,22,33,44]

def ff(x):
    #for i in x:
     print(2*x)

#ff(list_score)

#print(list(map(ff,list_score)))
print(list(map(ff,list_score)))
print(type(map(ff,list_score)))
print(list(map(lambda x:2*x,list_score)))


#filter
def even(num):
  if num%2==0:
    return num

def odd(num):
  if num%2!=0:
    return num   

print(list(filter(even,list_score)))
print(list(filter(odd,list_score)))


#reduce 
def sumss(x):
  s=0
  for i in x:
    s=s+i
  return s

print(sumss([1,2,3,4]))
print(reduce(lambda x ,y: x+y ,[1,2,3,4,5]))