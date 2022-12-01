#i python polymorphism have two types 
# ovirriding
#overloading


#overriding
# user defind method
# inbulit method/magic methods

print('---------------inbulit method-----------')
#inbuilt methods
name="ravindra jadeja"
print(len(name))
print(type(name))

s=[12,12,34]
print(len(s))
print(type(s))

a=100
b=100
print(a+b)

n1='supriya'
n2='Tajane'
print(n1+" "+n2)#concat

print('--------------user defined method-----')

class India:
    def capital(self):
        print('new delhi')

class Austarlia:
    def capital(self):
        print('sydney')

class Englad:
    def capital(self):
        print('france')

I1=India()
A1=Austarlia()
E1=Englad()

I1.capital()
A1.capital()
E1.capital()

print('--------------')
class mobile():
    def __init__(self,name,model):
       self.name=name
       self.model=model
    
    def display(self):
        print('name is {},model is {}'.format(self.name,self.model))

class Laptop(mobile):
    def __init__(self, name, model,lnme):
        self.lnme=lnme
        return super().__init__(name, model)
    
    def display(self):
        print('lname is: {}'.format(self.lnme))
        return super().display()

L1=Laptop('OOPO','L1','LENOVO')
L1.display()

print('-----------magic method--------')
class Person():
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def __str__(self):
        return"{},{}".format(self.name,self.lname)

PP=Person('Abhijit','Tajane')
print(PP)

class double:
    def __init__(self,amount,days) -> None:
        self.amount= amount
        self.days = days
    def _len_(self):
        return 3*self.days
d1 =double(5000,25)

print(d1)
#print(len(d1))