#Padrão criado com turtle
#Contorno geométrico!


from turtle import *
import turtle as t



def Produz_Contorno_Geometrico():
  
    
    for x in range(170):
        for d in ('violet', 'blue','gray', 'green', 'yellow'):
            color(d) #COLOR
            forward(x) #FORWARD
            left(45)  #RIGHT

Produz_Contorno_Geometrico()

e = Screen()

e.bgcolor("yellow")
e.exitonclick()