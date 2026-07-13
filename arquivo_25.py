#Como fazer um desenho de diferentes formas usando a turtle?

from turtle import *

n =  Turtle()

n.pensize(5)
n.pencolor("blue")
d = Screen()
d.bgcolor("yellow")

#Criando função, para desenhar forma!


def desenha_forma(m):
    angulo = 360/m
    for _ in range(m):
        n.forward(100)
        n.left(angulo)


for x in range(3,12):
    #Chamada da função, dentro do loop for!s
    desenha_forma(x)



d.exitonclick()