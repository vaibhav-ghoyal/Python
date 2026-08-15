
with open("Chepter-9 PS/log.txt","r") as f:
    lines = f.readlines()

lineno = 1 
for line in lines:
    if("Python" in line):
        print(f"Python is Present in Log.txt File:Line No:{lineno}")
        break
    lineno += 1
   
else:
        print("Python is Not Present in Log.txt File.")


