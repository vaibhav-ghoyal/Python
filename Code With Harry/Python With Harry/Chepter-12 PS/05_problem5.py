n = int(input("Enter The Number:"))

table = [n*i for i in range(1,11)]

with open("Chepter-12 PS/table.txt","a") as f:
    f.write(f"Table {n} is: {str(table)}\n")