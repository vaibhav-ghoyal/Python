# Write a Multiple line in File 
'''
Hello, I am Vaibhav Ghoyal.
I Learning Python Programming Language
Har Har Mahadev.
'''
# data = input("Enter Your Multiple line Data for File:")

# f = open("Chepter-9/multiline.txt","w")
# f.write(data)
# f.close()

# Read a multiple Line in File

f = open("Chepter-9/multiline.txt")
# line = f.readlines() ==>It Retruns Full Data of file in List
# print(line,type(line))

line = f.readline() # It Return Line of File in String(Str)
while(line != ""):
    print(line)
    line = f.readline()

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))
f.close()
