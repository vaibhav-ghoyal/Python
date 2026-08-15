n =  int(input("Enter Any Number:"))

for i in range(2,n):
    if(n%i==0):
        print("Number is Not Prime.!")
        break

else:
    print("Number is Prime")

# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count+=1
    
    
# print(count)
# if count==2:
#     print("Number is Prime")
# else:
#     print("Number is Not Prime.!")
