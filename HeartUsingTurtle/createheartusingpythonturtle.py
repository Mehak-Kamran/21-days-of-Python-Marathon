#Creating Heart using Python Turtle Module

#install turtle by pip install pythonturtle
import turtle
heart=turtle.Turtle()
heart.begin_fill()
heart.shape("turtle")
heart.color("red")

heart.left(50)
heart.forward(100)
heart.circle(40,180)

heart.left(260)
heart.circle(40,180)
heart.forward(100)
heart.end_fill()


turtle.done()



