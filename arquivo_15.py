#Trabalhando com formas!

from turtle import *


x = Shape("compound")

poligono_1 = ((0,0),(10,-5),(0,10),(-10,-5))

x.addcomponent(poligono_1, "blue", "violet")

poligono_2 = ((0,0),(10,-5),(-10,-5))


x.addcomponent(poligono_2, "pink", "green")




register_shape("myshape", x)

shape("myshape")

print(x)

d = Screen()

d.exitonclick()