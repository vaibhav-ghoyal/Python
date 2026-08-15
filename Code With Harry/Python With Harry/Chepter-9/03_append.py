# writing File

data = input("Enter String To Store in MyFile Text File:")

f = open("Chepter-9/myfile.txt","a") # Append Content At The End of File Content.
 
f.write(data)

f.close()