f = open("myfile.txt")
print(f.read())
f.close()

# The Same  Can Be Written Using With Statement Like This.
with open("Chepter-9/myfile.txt") as f:
    print(f.read())

# You Dont Have to Explicitly Close The File