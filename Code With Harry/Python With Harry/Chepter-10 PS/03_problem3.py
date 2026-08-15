class Demo:
    a=4

O = Demo()
print(f"Class Attribute:{O.a}") # Print The Class Attribute Because Instance Attribute is Not Present

O.a = 0 # Instance Attribute is Set
print(f"Class Instance Set Attribute Value:{O.a}") # Print The Instance Attribute Because instance Attribute is Present

print(f"Orginal Class Attribute:{Demo.a}")# Print The Class Attribute