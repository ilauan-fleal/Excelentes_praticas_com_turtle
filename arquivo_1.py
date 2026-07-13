#Padrão criado com turtle
#Contorno geométrico!


from turtle import *


def Produz_Contorno_Geometrico():



    for x in range(20):
        for d in ('violet', 'gray', 'green', 'yellow'):
            color(d) #COLOR
            forward(x) #FORWARD
            right(45)  #RIGHT

Produz_Contorno_Geometrico()


e = Screen()
e.exitonclick()