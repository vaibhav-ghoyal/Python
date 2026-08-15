# userinput 

n = int(input("Enter The Number:"))
even = []
odd = []
for i in range(n):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("even:",even)
print("Odd:",odd)