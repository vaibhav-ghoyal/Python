
with open("Chepter-9 PS/this.txt","r") as f:
    data1 = f.read()

with open("Chepter-9 PS/this_copy.txt","r") as f:
    data2 = f.read()

if(data1 == data2):
    print("Yes This File Are Identical")
else:
    print("No This File Are Not Identical")