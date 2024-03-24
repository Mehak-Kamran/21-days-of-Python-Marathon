#No guesssing Game (EASY)

import random

print(".........Welcome........ ")


compguess=random.randint(1,40)

while True:
  userguess=int(input(" Guess the Number between 1-40 \n"))
  if compguess==userguess:
    print("Congratulations You got it right....")
    break
  elif userguess>compguess:
    print("Try to guess a lower no")
  else:
   print("Try to guess a higher no")



print("-----GAME OVER-----")