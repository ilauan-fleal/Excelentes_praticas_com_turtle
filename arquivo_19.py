
from turtle import *


#Desenho de hexágono
#Detecção de evento

d = Screen()

def g():
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)
    left(60)
    forward(100)

d.onkey(g(), "Up")



d.exitonclick()