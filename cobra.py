#Criando classe e métodos, para o clássico Snake Game!
from turtle import *


POSICOES_INICIAIS = [(0,0), (-20,0), (-40,0)]  #Lista de tuplas



DISTANCIA = 20
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0



class Cobra:
    def __init__(self):
        self.caminhos = []
        self.criar_cobra()  #Chamada do método , criado abaixo!
        self.cabeca = self.caminhos[0]
    #Método para criar o formato de cobra


    def criar_cobra(self):
        for x in POSICOES_INICIAIS:
            novo_caminho = Turtle("square")
            novo_caminho.color("yellow")
            novo_caminho.penup()
            novo_caminho.goto(x)
            self.caminhos.append(novo_caminho)
    


    #Função, para movimentar a cobra!

    def mover_cobra(self):
        for y in range(len(self.caminhos) - 1, 0, -1):
            novo_x = self.caminhos[y - 1].xcor()
            novo_y = self.caminhos[y - 1].ycor()
            self.caminhos[y].goto(novo_x, novo_y)
        self.caminhos[0].forward(DISTANCIA)

    #Função, para mover cobra para cima:

    def Cima(self):
        if self.cabeca.heading() != BAIXO:
            self.cabeca.setheading(CIMA)



    #Função, para mover cobra para baixo:

    def Baixo(self):
        if self.cabeca.heading() != CIMA:
            self.cabeca.setheading(BAIXO)


    #Função, para mover cobra para esquerda:


    def Esquerda(self):
        if self.cabeca.heading() != DIREITA:
            self.cabeca.setheading(ESQUERDA)


    #Função, para mover cobra para direita:


    def Direita(self):
        if self.cabeca.heading() !=  ESQUERDA:
            self.cabeca.setheading(DIREITA)


