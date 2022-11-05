def addAll(a,b,c):
    print(a+b+c)

addAll(1,2,3)

def addalls(*args):
   print(args)
   print(sum(args))

addalls(1,2,3,4,5)

def adds(**kwargs):
   print(kwargs.items())
   print(kwargs.keys())
   for i,j in kwargs.items():
        print(i,j)

adds(name='supriya',job='tester')

k=11,12
print(type(k))
print(k)
a,b=k
print(a)
print(b)

#program4 
#local scope
def demo():
  l=10
  print(l)
demo()
#print(l) it is not acessible outside the function

#program5
#global scope
jj=10
def dd():
    print(jj)

dd()
print(jj)

#program 6
#global differnt local

mm=33
def vv():
 mm=30
 print(mm)#30

print(mm)#33
vv()


#program7
d=90
def ss():
    print(d)

print(d)
ss()
print(d)

#program 8
def kl():
    global g
    g=88
    print(g)
kl()
print(g)#if you acess the under  function  value than we declare global

#lambda
def sqr(x):
    return(x*x)

print(sqr(10))

#using lambda
ww=lambda x:x*x
print(ww(20))

def grater(x,y):
    if(x>y):
        return x
    else:
        return y

print(grater(20,30))

pp=lambda a,b:a if a>b else b
print(pp(45,40))