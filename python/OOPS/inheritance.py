class Student:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
     print('name is {},address is {}'.format(self.name,self.address))

s1=Student('supriya','Mumbai')
s1.display()

##inheritance

class Employee:
    def __init__(self,empName,company):
        self.empName=empName
        self.company=company

    def show(self):
        print('empName is {},company is {}'.format(self.empName,self.company))


class Manager(Employee):
    def __init__(self, empName, company,id):
        super().__init__(empName, company)
        self.id=id
    
    def show(self):
        print('the id:{}'.format(self.id))
        return super().show()
    
m1=Manager('satya','GOOGLE',123)
m1.show()

##multilevel inheritance
print('-----multilevel------')
class stud:
    def __init__(self,name,std,age):
        self.name=name
        self.std=std
        self.age=age

    def demo(self):
        print('the name is: {},the std is {} the age is {} '.format(self.name,self.std,self.age))

class Teacher(stud):
    def __init__(self, name, std, age,id):
        super().__init__(name, std, age)
        self.id=id

    def demo(self):
        print('id is: {}'.format(self.id))
        return super().demo()        
    
class Professor(Teacher):
    def __init__(self, name, std, age, id,special):
        super().__init__(name, std, age, id)
        self.special=special
    def demo(self):
        print('special is: {}'.format(self.special))
        return super().demo()

p1=Professor('sarika','11th',24,123,'IT')
p1.demo()

print('-----------multiple----')
class Father:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def prop(self):
     print('the fname is: {},the lname is: {}'.format(self.fname,self.lname))

class Son(Father):
    def __init__(self, fname, lname,snme):
        super().__init__(fname, lname)
        self.snme=snme
    
    def prop(self):
        print('the sname is {}'.format(self.snme))
        return super().prop()


class Daughter(Father):
    def __init__(self, fname, lname,dname):
        super().__init__(fname, lname)
        self.dname=dname
    def prop(self):
        print('dname is {}'.format(self.dname))
        return super().prop()

ss1=Son('Sunil','Tajane','Abhijit')
dd1=Daughter('sunil','Tajane','supriya')
ss1.prop()
dd1.prop()

        