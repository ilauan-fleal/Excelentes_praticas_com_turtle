
#Trabalhando com eventos e a biblioteca Turtle!

from turtle import *



class MyCode(Turtle):
    def Brilhar(self):
        self.fillcolor("blue")
    def Remover_brilho(self):
        self.fillcolor(" ")

k = MyCode()

k.onclick(k.Brilhar)
k.onrelease(k.Remover_brilho)

d = Screen()
d.exitonclick()