# Convert Temprature Convert into Fahrentheit To Celsius 

# Function Definition
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter Temparature in Fahrenhit:"))
# Function Call
c = f_to_c(f)
print(f"{round(c,2)} Celcius")