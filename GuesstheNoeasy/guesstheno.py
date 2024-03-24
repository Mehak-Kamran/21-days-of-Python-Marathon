#No guesssing Game (EASY)

import random

print(".........Welcome........ ")


compguess=random.randint(1,40)
print(compguess)
print(" Guess the Number between 1-40 \n")

while True:
  userguess=int(input())
  if userguess.isdigit():
     if compguess==userguess:
                print("Congratulations You got it right....")
                break
     elif userguess>compguess:
                print("Try to guess a lower no")
     else:
                print("Try to guess a higher no")
  else:
    print("Please Enter a no Next time...")
    break 



print("-----GAME OVER-----")