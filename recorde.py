from turtle import *

class Recorde(Turtle):
    def __init__(self):
        super().__init__()
        self.recorde = 0
        self.penup()
        self.goto(0,270)
        self.write(f"Recorde: {self.recorde}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()


    #Implementando função, para atualizar recorde!
    
    
    
    def atualizar_recorde(self):
        self.write(f"Recorde: {self.recorde}", align="center", font=("Arial", 24, "normal"))


    
    #Implementando função, para determinar o fim do jogo!
    
    
    
    def fim_de_jogo(self):
        self.goto(0,0) #Retorno à posição original
        self.write("JOGO FINALIZADO", align="center", font=("Arial", 24, "normal"))


    #Implementando função, para elevar o recorde!


    def elevar_recorde(self):

        self.recorde += 1
        self.clear()
        self.atualizar_recorde() #Chamada do método criado adiante, dentro desse método
    