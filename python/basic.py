#concatination
s1=[1,2,3]
s2=[2,4,5]
print(s1+s2)

##concat string
v1=['aba','baba']
v2=['maa','aai']
print(v1+v2)

##mul
a=[1,1,1]
print(a*2)
print(a*3)

#sub
 #b=[2,2,2]
 #c=[3,3,3]
#k=c-b
#print(k)

#div
# s1=[11,22,33]
# s2=[77,88,99]
# print(s1/s2)


# max()  min()
list_marks1 = [7,8,9,4,5,99]
print(max(list_marks1))

name=['s','u','p','r','i','a']
print(max(name))
print(min(name))

mass=['A','b','h','i','J']
print(max(mass))
print(min(mass))

# #  append() # at the end

runs = [5,5,4,2,4]
runs.append(777)
print(runs)

supriya=['s','u','p','r','i','y']
supriya.append('a')
print(supriya)

#  extend 
h1=['ww','bb','cc']
h2=[11,22,33]
h1.extend(h2)
print(h1)

h2.extend(h1)
print(h2)

#  insert # at the given index

company=['TCS','Wipro','Accenture']
company.insert(0,'Mahindra')
print(company)

company.insert(4,'infosys')
print(company)

##index
cc=company.index('Wipro')
print(cc)




