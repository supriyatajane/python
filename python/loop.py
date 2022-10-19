#remove
num1 = [22,33,44,55,66] 
num1.remove(22)
print(num1)


#reverse
num1 = [22,33,44,55,66] 
num1.reverse()
print(num1)

#sort
num2 = [12,45,78,41,56,87] 
num2.sort()
print(num2)

num2.sort(reverse=True)#desending order sort
print(num2)

num2.sort(reverse=False)#asending order
print(num2)


student_list = [1,2,3, " "," "]
print(len(student_list))
print(student_list)

#count dummy element
print(student_list.count(" "))
student_list.remove(" ")
student_list.remove(" ")

print(student_list)


#for loop
cities = ["pune","delhi","kolkata","nagpur","banglore"]


alpha = ['f', 'd', 'a', 'g', 'h', 'e', 'c', 'b']

print(cities)
print(alpha)
print(cities[0])
print(alpha[3])

for i in cities:print(i)

for i in alpha:print(i)
