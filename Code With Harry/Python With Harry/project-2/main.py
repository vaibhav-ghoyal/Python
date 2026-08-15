import random
n = random.randint(1,100)
guesses1 = 0
guesses2 = 0
p1 = -1
p2 = -1

while(True):

    # Player-1:
    print("\nPlayer-1 Turn")
    p1 = int(input("Guessess Number:"))

    if(p1>n):
        print("Lower Numebr Please.!")
        guesses1 +=1

    elif(p1<n):
        print("higher Numebr Please.!")
        guesses1 +=1

    elif(p1==n):
        print("Player-1 Guessess Correctly")
        break

    # Player-2:
    print("\nPlayer-2 Turn")
    p2 = int(input("Guessess Number:"))

    if(p2>n):
        print("Lower Numebr Please.!")
        guesses2 +=1

    elif(p2<n):
        print("higher Numebr Please.!")
        guesses2 +=1

    elif(p2==n):
        print("Player-2 Guessess Correctly")
        break


# Final Result
# print(f"\n Player-1 Attempts={guesses1}\nPlayer-2 Attempts={guesses2}")
print("\nPlayer-1 Attempts=",guesses1)
print("Player-2 Attempts=",guesses2)

if(guesses1<guesses2):
    print("Player-1 is Winner.!")
else:
    print("Player-2 is Winner.!")
