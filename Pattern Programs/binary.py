n = int(input("Enter Any Number: "))

for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2, end=" ")
    print()