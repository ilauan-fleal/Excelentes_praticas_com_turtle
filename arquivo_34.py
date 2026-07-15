from turtle import *
import time

from cobra import Cobra

t = Screen()

t.setup(width=600, height=600)   #Definindo dimensões da tela : 600 x 600

t.bgcolor("blue")

t.title("Jogo clássico : Snake!")



c = Cobra()





#Criando comandos de botões, para o jogo!


t.listen()
t.onkey(c.Cima,"Up") #Para cima
t.onkey(c.Baixo,"Down") #Para baixo
t.onkey(c.Esquerda,"Left") #Esquerda
t.onkey(c.Direita,"Right") #Direita


jogo_ligado = True



while jogo_ligado:
    time.sleep(0.1)
    c.mover_cobra()
  



