a = int(input("Enter Your Age: "))

#if Elif else Ladder

if(a>=18):
    print("You Are Above The Age of Consent.")
    print("Good For You")

elif(a<0):
    print("You Are Entering An Invalid Negative Age.")

elif(a==0):
    print("You Are Entering 0 which is not a Valid Age.")

else:
    print("Your Are Below The Age of Consent.")

print("End of The Program.")