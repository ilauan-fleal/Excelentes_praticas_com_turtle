from turtle import *

import turtle as s

import random

s.colormode(255)

s.speed("fastest")

s.penup()

s.setheading(225)
s.forward(300)
s.setheading(0)

s.hideturtle()

d = Screen()


d.bgcolor("blue")



lista_cores = [(254, 254, 254), (242, 253, 250), (253, 247, 251), (229, 243, 250), (13, 188, 156), (241, 141, 49), (229, 55, 114), (99, 183, 217), (240, 74, 43), (237, 220, 68)]



numero_de_pontos = 100

for _ in range(1, numero_de_pontos + 1):
    s.dot(20, random.choice(lista_cores))
    s.forward(50)
   
    if _ % 10 == 0:
        s.setheading(90)
        s.forward(50)
        s.setheading(180)
        s.forward(500)
        s.setheading(0)


d.exitonclick()