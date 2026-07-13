#Desenho de caminhos aleatórios com a Turtle!

import random

from turtle import *

n = Turtle()

d = [0, 90, 180, 270, 360]



for _ in range(200):
    n.forward(30)
    n.setheading(random.choice(d))


k = Screen()
k.exitonclick()