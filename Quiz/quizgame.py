#Dataware House and Data Mining Quiz Game

print("======Hello There, This is DWM Quiz Game======")
ready=input("Are you ready to play the Quiz ?").lower()

if(ready=="yes"):
  print("Great")
  question()
else:
    quit()


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
