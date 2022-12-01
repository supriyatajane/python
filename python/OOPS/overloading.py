#overloading
#two types of overloading
#function and operator

print(100)
print(100,200)
print(100,200,300)


def add1(a,b):
    print(a*b)
add1(10,5)
#add1(10,2,3)

class maths():
    def area(self,a):
      print(a*a)
m1=maths()
m1.area(10)

print('--------------overloading----------------')
#here we need extra logic
class demo():
    def area(self,a,b=0):
        if b>0:
            print(a*b)
        else:
            print(a*a)


de1=demo()
de1.area(11,11)
de1.area(12,0)

class greet():
    def show(self,name=None):
        if name is not None:
            print('hello'+name)
        else:
            print('Bye')

G1=greet()
G1.show('supriya')
G1.show()






class  Books:
    def __init__(self,pages):
        self.pages = pages
    def sum_pages(self,other):
        return self.pages + other.pages

    def _add_(self,other):
        return self.pages + other.pages

    def _sub_(self,other):
        return self.pages - other.pages

z1 = Books(300)
z2 = Books(50)

print("Using operator overloading:" , z1+z2)

#print(z1.sum_pages(z2))
print(z1 - z2) 

print(10+20)
#print((10)._add_(20))


