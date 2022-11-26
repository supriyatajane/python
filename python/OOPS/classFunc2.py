'''1. Create a class with below attribute
group  =  'dog'
age   =  7
class  = 'canine'
also create a method named Display() to print below
"Dog is man's Best friend"
call above attributes and methods by creating object named
Tommy

'''
class Animal:
  group = 'dog'
  age = 7
  classs = 'canine'

  def Display(self):
    print("Dog is man's Best friend")

Tommy=Animal()
print(Tommy.age)
print(Tommy.group)
print(Tommy.classs)
Tommy.Display()

print('------------------------')
print('----another way of calling-----')
Animal.Display(Tommy)