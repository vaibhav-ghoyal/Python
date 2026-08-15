a = 4

def fun():
    global a
    a = 7
    print(a)

#print(a) This is Use a Variable
fun()
print(a) # This is Use Gloabal a Variable