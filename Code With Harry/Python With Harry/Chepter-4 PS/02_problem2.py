marks = []

# f1 = int(input("Enter Marks Here: "))
# marks.append(f1)

# f2 = int(input("Enter Marks Here: "))
# marks.append(f2)

# f3 = int(input("Enter Marks Here: "))
# marks.append(f3)

# f4 = int(input("Enter Marks Here: "))
# marks.append(f4)

# f5 = int(input("Enter Marks Here: "))
# marks.append(f5)

# f6 = int(input("Enter Marks Here: "))
# marks.append(f6)

i=0
for i in range(0,5):
    f1 = input(f"Enter Fruits {i}:") #input("Enter Marks",i)
    marks.append(f1)

marks.sort()

print(marks)