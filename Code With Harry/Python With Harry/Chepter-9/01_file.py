'''
s = "Multiple email"
m  []
'''

# writing File

data = input("Enter String To Store in MyFile Text File:")

f = open("Chepter-9/myfile.txt","w")

f.write(data)

f.close()

# Reading File

f = open("Chepter-9/myfile.txt")

data = f.read()

print(data)

f.close()