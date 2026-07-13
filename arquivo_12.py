
from turtle import *


q = Turtle()


q.begin_fill()

if q.filling():
    q.pensize(30)
else:
    q.pensize(20)


print(q.pensize()) #30 é retornado!

