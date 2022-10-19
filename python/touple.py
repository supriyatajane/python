t = (False,False,True,False,True)
#1. CONVERT THE ABOVE  TUPLE INTO A LIST
s=(list(t))
print(s)
print(type(s))

print('------------------------------------')

#2. FIND THE MEMORY ADDRESS OF BOTH TUPLE AND LIST
print(id(t))
print(id(s))

print('-----------------------------')

#3. APPEND 99 AT THE END OF THE LIST
s.append(99)
print(s)
print('-----------------------------------------')

#4. CONVERT BACK THE LIST  INTO TUPLE
t=tuple(s)
print(t)
print(type(t))
print('-----------------------')

#5. NOW FIND THE MEMORY ADDRESS OF THIS TUPLE

print(id(t))







