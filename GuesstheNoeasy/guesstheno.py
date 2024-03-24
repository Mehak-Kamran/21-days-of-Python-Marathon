#No guesssing Game (EASY)

import random



def playgame():
    compguess=random.randint(1,40)
    print(compguess)
    print(" Guess the Number between 1-40 \n")
    guess=0
    while True:
        userguess = input()
        guess += 1
        if userguess.isdigit():
            userguess = int(userguess)
            if compguess == userguess:
                print("Congratulations You got it right in", guess, "guesses....")
                break
            elif userguess > compguess:
                print("Try to guess a lower no")
            else:
                print("Try to guess a higher no")
        else:
            print("Please Enter a no Next time...")
            break 



print(".........Welcome........ ")
choice=input("\n Press 'q' to quit:\n Press 'c' to continue:\n")




if choice=="q":
  quit
else:
  
  playgame()





print("-----GAME OVER-----")