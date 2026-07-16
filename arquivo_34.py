from turtle import *
import time

from cobra import Cobra
from comida import Comida
from recorde import Recorde


t = Screen()

t.setup(width=600, height=600)   #Definindo dimensões da tela : 600 x 600

t.bgcolor("blue")

t.title("Jogo clássico : Snake!")



c = Cobra()

ca = Comida()

r = Recorde()

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
   
    if c.cabeca.distance(ca) < 15:
        ca.atualizar()
        r.elevar_recorde() 


    elif c.cabeca.xcor() > 280 or c.cabeca.xcor() < -280 or c.cabeca.ycor() > 280 or c.cabeca.ycor() < -280:
       
        
           
        jogo_ligado = False
        r.fim_de_jogo()
       # print("Game Over")