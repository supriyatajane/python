##set the attriobute different types
# // hardcode value 
# // hardcode value 
# // constructor (hardvalues)
# // passing parameter to constructor 
# // using mutators and accessors

class Qa:
   def __init__(self):
          self.name='supriya'
          self.age=24
          self.company='TCS'
   def display(self):
        print('name is:{},age is:{},company is:{}'.format(self.name,self.age,self.company))

q1=Qa()
q1.display()
q2=Qa()
q2.display()

print('--------------------------using constructor----------------------------')
##using constructor we set varibles value

class Enginneer:
    def __init__(self,desg,branch,year):
        self.desg=desg
        self.branch=branch
        self.year=year 

    def show(self):
        print('the desg is: {},branch is: {},year is {}'.format(self.desg,self.branch,self.year))        

e1=Enginneer('manager','civil',2020)
e2=Enginneer('Employee','mech',2222)
e3=Enginneer('Qa','computer',2033)
e1.show()
e2.show()
e3.show()

print('--------------')
##class varible and instnce varible
class Company:
    name='TCS'
    def __init__(self,year,feature):
        self.year=year
        self.feature=feature
    def flow(self):
        print('year is {},feature is {},name is: {}'.format(self.year,self.feature,self.name))

    #class method
    @classmethod
    def changename(self):
        self.name='Wipro'

c1=Company(2022,'IT')
c2=Company(2002,'IIT')
c2.name='Capgemini'
c1.changename()
c1.flow()
c2.changename()
c2.flow()


# Accessor and mutators
# get and set
print('-------------')
class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
       return self.name

    def setBranc(self,branch):
        self.barnch=branch
    

    def getBranch(self):
        return self.barnch

ss1=Student()
ss1.setName('supriya')
ss1.setBranc('IT')
q1=ss1.getName()
a=ss1.getBranch()
print(a)
print(q1)

ss2=Student()
ss2.setName('rutuja')
ss2.setBranc('LOcal')
dd1=ss2.getName()
dd2=ss2.getBranch()
print(dd1)
print(dd2)


class Bird:
    wings=3
    @classmethod
    def fly(cls,bird):
        print(cls.wings,bird)

Bird.fly('sparrow')
Bird.fly('cat')       

     
