import random
import time
print("Welcome to maths Quiz")
print("==========")
OPERATORS=["+","-","*"]
MINOPERAND=3
MAXOPERAND=12
TOTALPROBLEMS=10

def generateexp():

    right=random.randint(MINOPERAND,MAXOPERAND)
    left=random.randint(MINOPERAND,MAXOPERAND)
    operand=random.choice(OPERATORS)
    exp=str(left)+operand+str(right)
    result=eval(exp)
    return exp,result


wrong=0
starttime=time.time()

for i in range(TOTALPROBLEMS):
    exp,result=generateexp()
    while True:
        que=int(input(exp+":"+" "))
        #print(type(que),type(result))
        if que==result:
            break
        wrong+=1

endtime=time.time()
totaltime=round(endtime-starttime,2)
print('You were wrong',wrong,'Times.You completed in ',totaltime,"seconds")
print("Great work!")
print("=============")
    
        
    
    
    
    

     
    
