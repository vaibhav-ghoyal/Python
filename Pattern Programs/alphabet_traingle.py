n = int(input("Enter Any Number:"))
#Column
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()

#Row
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+i), end=" ")
    print()