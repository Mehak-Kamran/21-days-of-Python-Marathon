import random

def roll():
    min=1
    max=6
    value=random.randint(min,max)
    return value

def score(val):
    
            if val!= 1:
                while True:
                    y=input("do you want to play(y):")
                    if y=="y":
                        rolling()
                    else:
                         quit()        
        
            else:
                quit()
       

def rolling():
    val=roll()
    print(val) 
    
    score(val) 
        


while True:
    players=input("Enter No of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            rolling()
            

            
        else:
            print("Enter valid range (2-4): ")
            
    else:
        print("Enter a Integer")
        


