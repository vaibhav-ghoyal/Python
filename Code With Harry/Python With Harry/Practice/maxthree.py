# Find Out Maximum Nummber out of Given Three Number

n1 = int(input("Enter Number-1:"))
n2 = int(input("Enter Number-2:"))
n3 = int(input("Enter Number-3:"))

if(n1>n2): #n1 Maximum
    if(n1>n3):
        print("N1 is Maximum",n1)
    else:
        print("N3 is Maximum:",n3)

elif(n2>n3):
    print("N2 is Maximum",n2)
    
else:
    print("N3 is Maximum",n3)
    