#Definindo parâmetros de coordenadas!

from turtle import *

#Desenho de octógono regular!
n = Turtle()



d = Screen()

d.setworldcoordinates(-5,-7.5,5,7.5)



for _ in range(72):
    left(10)


for _ in range(8):
    left(45)
    forward(1)

d.exitonclick()