class Student:
    name='supriya'
    lastname='Tajane'
    age=22
    Role='Tester'

# creating objects
s1=Student()
print(s1.name)
print(s1.lastname)
print(s1.age)
print(s1.Role)

print('------------')
#  creating new objects
s2=Student()
s2.age=21
s2.Role='QA'
print(s2.age)
print(s2.Role)

print('------------')
#creating object and acess old attribute
s3=Student()
print(s3.Role)

print('==============')
#access the attribute using classname
print(Student.name)
print(Student.lastname)
print(Student.Role)