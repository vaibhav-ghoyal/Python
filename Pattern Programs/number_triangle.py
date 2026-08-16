n = int(input("Enter Any Number: "))

#row
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

#column
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()