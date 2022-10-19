#FIND THE DATA TYPE AND LENGHT OF z
z = "Repetition is the mother of learning"
print(len(z))
print(type(z))

print('=========reverse String===========')
# 2 . REVERSE THE STRING USING NEGATIVE INDEXING/SLICING 
k  = "Was it a car or a cat I saw? "
p = "Do geese see God?"
print(k[::-1])
print(p[::-1])

print('============Range============')
# 3 . PRINT THE FOLLOWING USING range()
h = "HYDERABAD"
c = "CHENNAI"
d = "DELHI"

for x in range(0,9):
    print(h[x])

print('=====================')
for y in range(0,7):
    print(c[y])

print('===========================')

for z in range(0,5):
    print(d[z])

    

# 4.  find number of spaces in song2
#     find count of Ganga in song2
#     replace  Ganga with "GANGA" in song2

song2 = '''
Jana Gana Mana Adhinaayak Jaya Hey, 
Bhaarat Bhaagya Vidhaataa 
Panjaab Sindhu Gujarat Maraatha, 
Draavid Utkal Banga 
Vindhya Himaachal Yamuna Ganga, 
Vindhya Himaachal Yamuna Ganga, 
Uchchhal Jaladhi Taranga
Tav Shubh Naamey Jaagey, 
Tav Shubh Aashish Maange Gaahey 
Tav Jayagaathaa 
Jana Gana Mangal Daayak, Jaya Hey Bhaarat Bhaagya Vidhaataa 
Jaya Hey, 
Jaya Hey, 
Jaya Hey, 
Jaya Jaya jaya, 
Jaya Hey
'''
print('======================count=====================')
print(song2.count(" "))
print(song2.count('Ganga'))
l=song2.replace('Ganga',"GANGA")
print(l)

print('=====================format()===============')
# 5 . using format() method print below  

s = "sun"
m = "moon"
e = "earth"
#sun is farthest from earth and nearest is moon
#print("{0} is farthest from {1} and nearest is {2}".format(s,e,m))


"moon is nearest and sun is farthest from earth"
print("{1} is nearest and {0} is farthest from {2}".format(s,m,e))

"sun is biggest of earth and moon"

print('{0} is biggest of {2} and {1}'.format(s,m,e))

"the order is sun , earth and moon"

print('the order is {0},{2} and {1}'.format(s,m,e))


