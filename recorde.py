from turtle import *

class Recorde(Turtle):
    def __init__(self):
        super().__init__()
        self.recorde = 0
        self.recorde_mais_alto = 0
        self.penup()
        self.goto(0,270)
        self.write(f"Recorde: {self.recorde}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()


    #Implementando função, para atualizar recorde!
    
    
    
    def atualizar_recorde(self):
        self.clear()
        self.write(f"Recorde: {self.recorde}", align="center", font=("Arial", 24, "normal"))


    
    #Implementando função, para determinar o fim do jogo!

    def resetar_jogo(self):
        if self.recorde > self.recorde_mais_alto:
            self.recorde_mais_alto = self.recorde
        self.recorde = 0
        self.atualizar_recorde()
   
    


    #Implementando função, para elevar o recorde!


    def elevar_recorde(self):

        self.recorde += 1
        self.atualizar_recorde() #Chamada do método criado adiante, dentro desse método
    
