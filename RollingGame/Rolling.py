import random

def roll():
    min=1
    max=6
    value=random.randint(min,max)
    return value

while True:
    player=input("Enter no of players(2-4)")
    if player.isdigit():
        player=int(player)
        if 2<= player <=4:
            break
        else:
            print("enter valid range(2-4)")
    else:
        print("Enter integer (2-4)")

maxscore=50
playerscore=[0 for _ in range(player)]

if max(playerscore)<max:
    