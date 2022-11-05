#list an argument

print(13%2==0)

a=[1,2,3,4,5,6,7,8,9,10]
b=[]

for i in a:
 if(i%2==0):
    b.append(i)
print(b)

def filter_no(x):
 b=[]
 for i in x:
  if(i%2==0):
   b.append(i)
 print(b)

filter_no([10,20,30,40])


def double(z):
 b=[]
 for i in z:
   b.append(i+2)
 print(b)

double([11,22,33])



def concat(x,y,z,w):
     return x+y+z+w

#print(concat("A","B","C"))
print(concat("A","B","C", "D"))


#concat
def concat_name(a,b):
    return a+b

jj=concat_name('supriya','tajane')
print(jj)
#dd=concat_name('sara','diya','jj')
#print(dd)


def concat_name(*args):
    s = []
    for i in args:
        s.append(i)
    return s

print(concat_name("Vikas","Suresh","Chaudhary","One", "Two"))


def dd(*args):
    d=[]
    for i in args:
        d.append(i)
    return d

print(dd('mahesh','vijay','arjun'))