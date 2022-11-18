#1. CREATE TEXT FILE WITH BELOW DATA IN IT AND NAME  IT AS colors.txt
#Brown
#Yellow
#Green

data=open(r'C:\Users\admin\Desktop\phython\colors.txt','w')
data.write('''Brown
Yellow
Green''')
data.close()

#2. READ THE FILE  colors.txt AND DISPLAY THE OUTPUT ON THE SCREEN

data1=open(r'C:\Users\admin\Desktop\phython\colors.txt','r')
print(data1.read())
data1.close()

#3. ADD BELOW DATA IN THE FILE colors.txt WITHOUT REMOVING OLD DATA
data2=open(r'C:\Users\admin\Desktop\phython\colors.txt','a')
data2.write('\nBLUE')
data2.close()


print('---------------------------------------')
#4. DISLAY THE DATA OF THE FILE colors.txt USING FOR LOOP 
data3=open(r'C:\Users\admin\Desktop\phython\colors.txt','r')
for i in data3:
    print(i)



