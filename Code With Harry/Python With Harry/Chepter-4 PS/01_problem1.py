fruits = []

# f1 = input("Enter Fruit Name:")
# fruits.append(f1)

# f2 = input("Enter Fruit Name:")
# fruits.append(f2)

# f3 = input("Enter Fruit Name:")
# fruits.append(f3)

# f4 = input("Enter Fruit Name:")
# fruits.append(f4)

# f5 = input("Enter Fruit Name:")
# fruits.append(f5)

# f6 = input("Enter Fruit Name:")
# fruits.append(f6)

# f7 = input("Enter Fruit Name:")
# fruits.append(f7)

# print(fruits)

i=0
for i in range(0,4):
    f1 = input(f"Enter Fruits {i}:")
    fruits.append(f1)

fruits.sort()
print(fruits)