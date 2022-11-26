class student:
    pass

s1=student()
print(type(s1))

#class have attributes and methods
class studentMain:
    name='supriya',
    lastname='Tajane',
    age:22
    
    def display():
        print('I am in studenmain')

s2=studentMain()
#s2.display()
#chaging the attribute value
s3=studentMain()
s3.age=30
print(s3.age)

#after chaging the class atrributte value
studentMain.age=55
print(studentMain.age)
print(s2.age)
print(s3.age)

print('-------------self----------')
#understand python
class demo:
    name='diya'
    lastname='mirza'

    def show(self):
     print(id(self))
     print('i am in show')


d1=demo()
print(id(d1))
d1.show()

#another way to call the method using class name
demo.show(d1)

print('-------------------------')

class Designer:
    name="manish"
    lastname="manotra"

    def fashion(self):
        print('design high')
        price=2000
        print(price)

D1=Designer()
D2=Designer()
D3=Designer()
 
D1.fashion()
D2.fashion()
D3.fashion()

print('-----------------------')
#using class name

Designer.fashion(D3)

