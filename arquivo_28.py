
from turtle import *
import turtle as s
import random

n =  Turtle()

n.pensize(7)

n.speed(3)
s.colormode(255)

def RGB():
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    Random_Color = (x,y,z) #Uma tupla!
    return Random_Color

direcoes = [0,90,180,270,360]


for _ in range(200):
    n.color(RGB())
    n.circle(100)
    n.setheading(random.choice(direcoes))


d =  Screen()
d.exitonclick()

