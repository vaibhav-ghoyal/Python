# Enter Three Number Which one Greater

#Function Definition
def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        return "Invalid"
    
    '''
    if(a>b):
        if(a>c)
            return a
        else
            return b

    elif(b>c):
        return b
    
    else:
        return c
    '''

a = int(input("Enter Number-1:"))
b = int(input("Enter Number-2:"))
c = int(input("Enter Number-3:"))

ans = gretest(a,b,c)
print(f"Gretest Number is:{ans}")