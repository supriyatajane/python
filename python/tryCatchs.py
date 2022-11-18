#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
  print(x)
except:
  print("An exception occurred")


#problem 2
try:
 a=10
 b=0
 c=a/b
 print(c)

except:
    print('you have pass wrong value 0')

#problem 3
try:
 data=open(r"C:\Users\admin\Desktop\phython\reads.txt")
 print(data.read())

except FileNotFoundError as e:
    print('such no found',e)
print("You have xyz amount in your acc")

print('-----------------------------------------')
#problem 4
try:
 data=open(r"C:\Users\admin\Desktop\phython\reads.txt")
 print(data.read())
 print(100/10)
 list_even=[11,22,33,44]
 print(list_even[20])
except FileNotFoundError as e:
    print('such no found',e)
except IndexError as e:
    print('index not found',e)
else:
    print('executed code sucessfully')

finally:
    print('this will execute irrespective')