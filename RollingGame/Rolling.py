while True:
    players=input("Enter No of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            #roll()
            break
        else:
            print("Enter valid range (2-4): ")
            
    else:
        print("Enter a Integer")
        
