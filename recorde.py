from turtle import *

class Recorde(Turtle):
    def __init__(self):
        super().__init__()
        self.recorde = 0
        with open("dados.txt") as dado:
            self.recorde_mais_alto = int(dado.read())
        self.penup()
        self.goto(0,270)      
        self.hideturtle()


    #Implementando função, para atualizar recorde!
    
    
    
    def atualizar_recorde(self):
        self.clear()
        self.write(f"Recorde: {self.recorde}", align="center", font=("Arial", 20, "normal"))
        self.goto(0,240)
        self.write(f"Recorde mais alto: {self.recorde_mais_alto}", align="center", font=("Arial", 20, "normal"))
        self.goto(0,210)




    
    #Implementando função, para determinar o fim do jogo!

    def resetar_jogo(self):
        if self.recorde > self.recorde_mais_alto:
            self.recorde_mais_alto = self.recorde
            with open("dados.txt", "w") as dados:
                dados.write(f"{self.recorde_mais_alto}")
        self.recorde = 0
        self.atualizar_recorde()
        
   
    


    #Implementando função, para elevar o recorde!


    def elevar_recorde(self):

        self.recorde += 1
        self.atualizar_recorde()
        
    
