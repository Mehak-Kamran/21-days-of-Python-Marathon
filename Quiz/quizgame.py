#Dataware House and Data Mining Quiz Game
import math 

def question():
  score=0

  answer=input("Data Ware House is used for which type of Data? \n").lower()
  if(answer=="historic"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  answer=input("Data Mining is used to discover ? \n").lower()
  if(answer=="knowledge"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong Answer")

  answer=input("Distributed Database are not present ? \n").lower()
  if(answer=="physically"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  answer=input("ETL stands for ? \n").lower()
  if(answer=="extract transform load"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")

  
  answer=input("SCD stands for ? \n").lower()
  if(answer=="slowly change dimension"):
    print("Correct Answer")
    score+=1
  else:
    print("Wrong")




  return score




print("======Hello There, This is DWM Quiz Game======\n")
ready=input("Are you ready to play the Quiz ?\n").lower()

if(ready=="yes"):
  print("Great")
  result=math.floor((question()*100)/5)
  if 80<=result<=100:
    print("Congrats your score is:",result,"%")
  else:
    print("Better play next time your score is:",result,"%")

else:
    print("You are out")
    quit()


