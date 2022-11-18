'''1. catch exception in below code using try... except else print " Code Execution was successful"
'''
try:
 list_z = [1,2,3,"a"]
 for i in range(5):
    if type(list_z[i]) == int:
        print("This is int")
    else:
        print("This is not int") 
except IndexError as e:
    print('Element not found',e)
else:
    print("All code exceuted successfully")

finally:
    print("This will excute irrespective of exception")

print('----------------------------------------------')
#2. catch exception in below code using try... exceptelse print " Code Execution was successful"
#also close the file irrespective of operation on file
try:
 f = open(r"one.txt")
 print(f.read())
 
except FileNotFoundError as e:
    print('some error occured',e)
finally:
 try:
  f.close()
 except:
  print("Something went wrong when opening the file")



#3. catch exception in below code using try... except
