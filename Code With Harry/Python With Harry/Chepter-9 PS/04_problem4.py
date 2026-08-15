
with open("Chepter-9 PS/Donkey.txt","r") as f:
    data = f.read()

newdata = data.replace("Donkey","#####")


with open("Chepter-9 PS/Donkey.txt","w") as f:
    f.write(newdata)