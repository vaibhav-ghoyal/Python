a = int(input("Enter Your Age: "))

#If Statement No:1

if(a%2 == 0):
    print("a is Even.")

#End of Statement no:1

#If Statement No:2
if(a>=18):
    print("You Are Above The Age of Consent.")
    print("Good For You")

elif(a<0):
    print("You Are Entering An Invalid Negative Age.")

else:
    print("Your Are Below The Age of Consent.")

#End of Statement no:1

print("End of The Program.")