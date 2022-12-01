#multilevel
#multiple
#single 

#multple inheritance
class Father:
    def __init__(self,fname,lame):
        self.fnme=fname
        self.lame=lame
    def display(self):
        print('the fname is: {} ,lname is: {}'.format(self.fnme,self.lame))

class Mother:
     def __init__(self,mname,lame):
            self.mnme=mname
            self.lame=lame
     def display1(self):
        print('the Mname is: {} ,lname is: {}'.format(self.mname,self.lame))

class Son(Father,Mother):
    pass

s1=Son('sunil','Tajane')
s1.display()

print('-----------------------')

##P1.method()

print('-----------------------------')
class A(object):
    def method(self):
        print('A method called ') #3
        super().method()

class B(object):
    def method(self):
        print('B method called ') # 5
        super().method()

class C(object):
    def method(self):
        print('C method called ')  #6
     

class X(A,B):
    def method(self):
        print('X method called ')  # 2
        super().method()

class Y(B,C):
    def method(self):
        print('Y method called ')   # 4
        super().method()

class P(X,Y,C):
    def method(self):
        print('P method called ') #1 
        super().method()

p = P()
p.method()
    


        
