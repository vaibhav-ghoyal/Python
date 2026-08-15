word = ["Donkey","Tree","Child"]

with open("Chepter-9 PS/Donkey.txt","r") as f:
    data = f.read()

for word in word:
    data = data.replace(word,"#"*len(word))

with open("Chepter-9 PS/Donkey.txt","w") as f:
    f.write(data)