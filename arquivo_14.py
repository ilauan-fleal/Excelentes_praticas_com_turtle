#Desenhando e construindo um polígono, incluindo seus vértices!

from turtle import *


x = Turtle()

x.home()

x.begin_poly()

x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.forward(100)

x.end_poly()



d = Screen()

d.exitonclick()