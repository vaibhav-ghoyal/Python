import random

'''
1-For Snake
2-For Water
3-For Gun

'''
# Game Dictionary
game = {
    1 : "Snake",
    2 : "Water",
    3 : "Gun"
}

# Random Choice Using Random Librery with Choice Function 
computer = random.choice([1,2,3])

print("1-Snake\n2-Water\n3-Gun")
you = int(input("Enter Your Choice[1,2,3]:"))

print(f"Computer Choose:{game[computer]} \n You Choose:{game[you]}")

if(computer == you):
    print("Game Draw.!\nPlay Again.!")

else:
    # -1:loose 1:win 2:loose -2:win

    if((computer-you)==1 or (computer-you)==-2):
        print("You Win.!")

    elif((computer-you)==-1 or (computer-you)==2):
        print("You Loose.!")

    else:
        print("Something Went Wrong.!")

    # if(computer == 1 and you==2): # 1-2=-1
    #     print("You Loose.!")
    
    # elif(computer == 2 and you==1):# 2-1=1
    #     print("You Win.!")

    # elif(computer == 1 and you==3): # 1-3=-2
    #     print("You Win.!")

    # elif(computer == 3 and you==1): # 3-1=2
    #     print("You Loose.!")

    # elif(computer == 2 and you==3): # 2-3=-1
    #     print("You Loose.!")

    # elif(computer == 3 and you==2): # 3-2=1
    #     print("You Win.!")
    
    # else:
    #     print("Something Went Wrong.!")
