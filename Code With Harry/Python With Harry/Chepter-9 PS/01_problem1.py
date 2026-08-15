f = open("Chepter-9 PS/file.txt")
data = f.read()
if("Vaibhav" in data):
    print("Vaibhav Word is present in Data.")
else:
    print("Vaibhav Word is Not present in Data.")

f.close()
