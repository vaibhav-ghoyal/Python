def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [12, 15, 35, 45, 85, 96, 74, 88]

f = list(filter(divisible5,a))
print(f)