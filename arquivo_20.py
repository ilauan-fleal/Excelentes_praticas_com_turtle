
from turtle import *


r = True

k = Screen()


def f():
    if r:
        forward(150)
        
        k.ontimer(f, 250)


f()

r = False

k.exitonclick()