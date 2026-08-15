# Function with Arguments

#Function Definition

def goodday(name,ending):
    print("Good Day, "+name)
    print(ending)

goodday("Vaibhav","Thank You.!")
goodday("Shiv","Thanks!")

# Function With Arguments Return Statement

def avg():
    a = int(input("Enter Any Number:"))
    b = int(input("Enter Any Number:"))
    c = int(input("Enter Any Number:"))

    avg = (a+b+c)/3
    return avg

a = avg()
print("Average is:",a)
