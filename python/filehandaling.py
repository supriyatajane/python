#C:\Users\admin\Desktop\phython\new.txt

# reading an existing file in python
data=open(r"C:\Users\admin\Desktop\phython\new.txt")
print(data.read())
data.close()

#reading non existing file
#data1=open(r"C:\Users\admin\Desktop\phython\demo.txt")
#print(data1.read())
#data1.close()

print('----------creating file------------')
# creating a file 
test=open(r"C:\Users\admin\Desktop\phython\test.txt","w")
test.write('I am Automation tester')
test.close()

test1=open(r"C:\Users\admin\Desktop\phython\test.txt","r")
print(test1.read())
test1.close()

# over writing data 
print('------------over writing data------------')
tast3=open(r"C:\Users\admin\Desktop\phython\test.txt","w")
tast3.write('''

data1
data2
''')
tast3.close()

f2=open(r"C:\Users\admin\Desktop\phython\test.txt","a")
f2.write('\nData4, \nData5')
f2.close()

f1=open(r"C:\Users\admin\Desktop\phython\test.txt")
print(f1.read(6))
f1.close()
# printing line 
print("****---------------readline-------------***")

ff=open(r"C:\Users\admin\Desktop\phython\test.txt")
print(ff.readline())
print(ff.readline())
print(ff.readline())

# resetting cursor position
ff.seek(0)
print(ff.readline())

print('----------------------using loop---------------')
#using loop
for i in ff:
    print(i)


print('--------------------------------')
ff.seek(0)
print(ff.readlines())
ff.close()
#print(ff.readlines()[2])

# content manager
with open(r"C:\Users\admin\Desktop\phython\test.txt","r")as hh:
    print(hh.read(5))
    print(hh.mode)



