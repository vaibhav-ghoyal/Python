a = int(input("Enter Number-1:"))
b = int(input("Enter Number-2:"))

if(b==0):
    raise ZeroDivisionError("Hey Our Program is Not Meant To Divide Number By Zero")

else:
    print(f"The Division a/b is:{a/b}")