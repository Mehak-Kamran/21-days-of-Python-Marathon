import random

def roll():
    min=1
    max=6
    value=random.randint(min,max)
    return value


while True:
    players=input("Enter No of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            if val != 1:
                val=roll()
                print(val)
            else:
                break

            
        else:
            print("Enter valid range (2-4): ")
            
    else:
        print("Enter a Integer")
        
