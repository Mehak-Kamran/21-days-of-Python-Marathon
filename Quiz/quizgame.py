#Dataware House and Data Mining Quiz Game
import math 

def question():
  score=0

  answer=input("Data Ware House is used for which type of Data? ").lower()
  if(answer=="historic"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  answer=input("Data Mining is used to discover ? ").lower()
  if(answer=="knowledge"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  answer=input("Distributed Database are not present ? ").lower()
  if(answer=="physically"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  return score




print("======Hello There, This is DWM Quiz Game======")
ready=input("Are you ready to play the Quiz ?").lower()

if(ready=="yes"):
  print("Great")
  result=question()
  print("Your score is:",math.floor((result*100)/3),"%")
else:
    quit()


