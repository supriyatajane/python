#1. write a function to take email id from user and separate the name ans domain
#Eg. raghav123@gmail.com
#output should be  [raghav123, gmail.com]
def mail(s):
   return s.split("@")
 

ll=mail('raghav123@gmail.com')
print(ll)

print('-----------------------------------------------------------')
#2. write a function to take 3 integers from user and give average as output

def avg(a,b,c):
    print((a+b+c)/3)

avg(20,20,20)
print('---------------------------------------------')
#3.  write a function to take student name and
#print "Good luck" with student name "Good luck" to be used as default argument
def students(name,greet="Good luck"):
    print(greet,name,"...........")

students('SUPRIYA')
print('---------------------------------')
#4. use *args and find average of 5 nos 
def avrage(*args):
    avg=sum(args)/len(args)
    return avg

print(avrage(5,5,5,5,5))