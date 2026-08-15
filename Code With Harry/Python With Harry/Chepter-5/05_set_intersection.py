s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print("Union",s1.union(s2)) 
print("OR || :",s1 | s2)

print("InterSection :",s1.intersection(s2)) # Same
print("AND & :",s1 & s2)

print("Difference :",s1.difference(s2))
print("Difference:",s1 - s2)

print("Symetric Difference :",s1.symmetric_difference(s2))
print("Caret :",s1 ^ s2)