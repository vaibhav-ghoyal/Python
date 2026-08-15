import random

def game():
    print("You Are Playing Game...")
    score = random.randint(1,100)
    highscore = 0

    print(f"Your Score is:{score}")
    with open("Chepter-9 PS/highscore.txt","w") as f:
        if(score>highscore):
            f.write(str(score))

    with open("Chepter-9 PS/highscore.txt") as f:
        highscore = f.read()

    if(highscore != ""):
        highscore = int(highscore)
    else:
        highscore = 0

game()