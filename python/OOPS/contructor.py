##
class Employee:
   name='supriya'
   job='Tester'

   def display(self):
    print('hello')
    print(self.job)

e1=Employee()
e1.display()

e1.name='sara'
e1.job='sharma'

print(e1.name)
print(e1.job)

print('----------contructor-------------')
#using contructor we not need the hardcode value 
# you pass the vvalue object creation

class Student:

  def __init__(self,name,grade,age):
    self.name=name
    self.grade=grade
    self.age=age

  def show(self):
        print('The emp name is {},grad is {},age is {}'.format(self.name,self.grade,self.age))

s1=Student('Sarika',22,24)
s1.show()

s2=Student('sana',88,23)
s2.show()

print('-----------private varible-----------')

# in python private the varible with double dunder __

class Demo:
    def __init__(self,name,project,language):
        self.name=name
        self.__project=project
        self.__language=language

    def flow(self):
        print('The student name is: {},project name: {},language is: {}'.format(self.name,self.__project,self.__language))

d1=Demo('Rutuja','ecomm','java')
d2=Demo('Aarti','bus Ticket','python')
d1.flow()
d2.flow()
#print(d1.__project)here we cannot acess the private varible outside class
#print(d2.__language)

# in python we create private varible  using(__abc) but cant be acess outside class
#but we acess inside class function using (self.__abc) this function call also 
#outside the class and acess the value

d1.language='C++'
print(d1.language)
d1.flow()

print('------acess private varible outside the class using -------')
# in python nothing is private or  hidden
#acess the class  private attribute outside the class using
# classname_attribute
print(d1.Demo_language)
print(d1.Demo_project)

