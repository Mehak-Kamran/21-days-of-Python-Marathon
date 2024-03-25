#Adventure Game

print("Welcome to The Game of Adventure")

ans=input("You have to worked hard for exams and Your momma has promised you if you will she will give you a beautiful surprise.Will you work hard or not?(yes/no) ")
if ans=='yes':
    ans=input("You have worked hard but your mama could not arranged the gift. what you do(shout/say its okay) ")
    if ans=="say its okay":
        ans=input("Your mama surprise you and says she was testing you.she have two boxes red and blue which box you choose?")
        if ans=="red":
            print("It was a diamond ring , you kiss your mama")
        elif ans=="blue":
            ans=input("you choose blue box, it contain 2 BTS Concert ticket , You and your mama are going to the concert tonight but your mama becomes sick, what you will do go out for concert or go out to buy medicines?(concert/medicine)")
            if ans=="medicine":
                print("You met Jimin there ,he was taking medicine for him, Both talk to each other, jimin offer you a quick dinner and you have a nice time with him")
            elif ans=="concert":
                print("You enjoy concert and V highfive you")
            else:
                print("Enter a valid input")
    elif ans=="shout":
        print("Your mama was just testing you , she gives you a beautiful dress , now your happy")
    else:
        print("enter valid answer")
elif ans=="no":
    print("You dont work hard hence no gift from mama, you loose")
else:
    print("Enter valid answer")