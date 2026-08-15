marks1 = int(input("Enter Mark 1:"))
marks2 = int(input("Enter Mark 2:"))
marks3 = int(input("Enter Mark 3:"))

#Check For Total Percentage
#total=marks1+marks2+marks3
#per=total*100/300
total_percentage = (100 * (marks1 + marks2 + marks3))/300

if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Your Are Pass:", total_percentage)

else:
    print("You Failed, Try Again Nexr Year!", total_percentage)
