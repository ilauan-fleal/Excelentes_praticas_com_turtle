


from turtle import *
import turtle as s
import random


s.pensize(2)
s.speed(3)
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


def desenho_dinamico(m):
    for _ in range(int(360/m)):
        s.color(RGB())
        s.circle(100)
        s.setheading(s.heading() + m)

desenho_dinamico(7)




d.exitonclick()


