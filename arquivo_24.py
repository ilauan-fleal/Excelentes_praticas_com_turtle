#Novos desafios, para produzir com a turtle!


#Desenho de pentágono!

from turtle import *

n =  Turtle()
d = Screen()
d.bgcolor("pink")
m = 10 #Número de lados!

n.color("blue")
n.pensize(16)

for _ in range(m):
    angulo = 360/m
    n.forward(100)
    n.left(angulo)



d.exitonclick()