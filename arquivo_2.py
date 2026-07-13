#Desenho de estrela com turtle!

from turtle import *



def Desenha_Estrela():

    
    color('blue')
    fillcolor('violet') 
    begin_fill() #Ativa auto-preenchimento




    while(1):
        forward(200)
        left(170)
        if abs(pos()) < 1:  #Verifica se o ponto de referência está na posição inicial!
            break
  

    end_fill()



#Chamada da função!

Desenha_Estrela()


