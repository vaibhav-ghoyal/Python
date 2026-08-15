# Using Walrus Operator

if(n := len([1,2,3,4,5]))>3:
    print(f"List is Too Long ({n} Elements, Expected <= 3)")
    # Output : List is Too Long (5 Elements, Expected <= 3)