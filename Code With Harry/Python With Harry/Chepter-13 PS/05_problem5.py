from functools import reduce

l = [523, 412, 869, 147, 325, 642, 326]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))

