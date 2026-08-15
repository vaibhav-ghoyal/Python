
with open("Chepter-9 PS/log.txt","r") as f:
    data = f.read()

if("Python" in data):
    print("Python is Present in Log.txt File")
else:
    print("Python is Not Present in Log.txt File")
