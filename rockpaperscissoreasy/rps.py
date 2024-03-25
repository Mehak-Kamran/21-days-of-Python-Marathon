#Rock Paper Scissor Easy
import random

def playgame():
    options=['rock','paper','scissor']
    userchoice=input("Enter your choice: Rock, Paper or Scissor\n").lower()
    if userchoice not in options:
        print("Please Enter valid input next time ")
        quit()
    compchoice= random.choice(options)
    print(compchoice)
    if userchoice=='scissor' and compchoice=='paper' or userchoice=='paper' and compchoice=='rock' or userchoice=='rock' and compchoice=='scissor' :
        print("Congratulations You win")
    elif userchoice==compchoice:
        print("Game is Drawn")
    else:
        print("You loose")


while True:
    choice=input("Welcome\n Press 'c' to continue\n Press 'q' to quit\n").lower()

    if choice=='q':
        quit()
    elif choice=='c':
        playgame()
    else:
        print("Press 'c' to continue and Press 'q' to quit next time ")

print("===Game Over===")