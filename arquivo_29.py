


from turtle import *
import turtle as s
import random


s.pensize(2)
s.speed("fastest")
s.colormode(255)
d =  Screen()
d.bgcolor("yellow")

#Implementação de função para cores RGB

def RGB():
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    Random_Color = (x,y,z) #Uma tupla!
    return Random_Color

#Implementação de função , para produzir desenho dinâmico
#m -> número de lados do polígono!
 
def desenho_dinamico(m):
    for _ in range(int(360/m)):
        s.color(RGB())
        s.circle(130)
        s.setheading(s.heading() + m)

#Chamada da função que irá produzir o desenho dinâmico.

desenho_dinamico(10)




d.exitonclick()


