from turtle import *
import random

class Comida(Turtle):
    
    #Definindo método construtor!
    
    def __init__(self):
        super().__init__()
        self.shape("square") #Formato de quadrado
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("green")
        self.speed("fastest")
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)
        self.atualizar() #Chamada do método!

    #Definindo método de 'refresh para tela'
    
    
    def atualizar(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)

