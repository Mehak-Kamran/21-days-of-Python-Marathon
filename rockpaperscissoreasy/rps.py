#Rock Paper Scissor Easy
import random

scorecomp=0
scoreuser=0

print("\nWelcome\n")


def playgame(scorecomp,scoreuser):
    options=['rock','paper','scissor']
    userchoice=input("Enter your choice: Rock, Paper or Scissor\n").lower()
    if userchoice not in options:
        print("Please Enter valid input next time ")
        quit()
    compchoice= random.choice(options)
    print(compchoice)
    if userchoice=='scissor' and compchoice=='paper' or userchoice=='paper' and compchoice=='rock' or userchoice=='rock' and compchoice=='scissor' :
        print("Congratulations You win\n")
        scoreuser+=1
    elif userchoice==compchoice:
        print("Game is Drawn\n")
    else:
        print("You loose\n")
        scorecomp+=1
    return scorecomp,scoreuser

while True:
    choice=input("Press 'c' to continue\nPress 'q' to quit\n").lower()

    if choice=='q':
        break
    elif choice=='c':
        scorecomp,scoreuser=playgame(scorecomp,scoreuser)
    else:
        print("Press 'c' to continue and Press 'q' to quit next time ")

print("Your score",scoreuser,"Computer score",scorecomp,"\n===Game Over===")