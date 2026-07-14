

from turtle import *

x = Turtle()

y = Screen()

x.pensize(5)


#Implementação da função para seguir reto!


def seguir_reto():
    x.forward(10)


#Implementação de função para seguir para trás!


def seguir_para_tras():
    x.backward(10)


#Implementação de função para virar à esquerda!

def virar_esquerda():
    novo_sentido = x.heading() + 10
    x.setheading(novo_sentido)

#Implementação de função para virar à direita!

def virar_direita():
    novo_sentido = x.heading() - 10
    x.setheading(novo_sentido)

#Implementação de função, para limpar a tela, método clear()

def limpar():
    x.clear()
    x.penup()
    x.home()
    x.pendown()




y.listen()
y.onkey(key="space", fun=seguir_reto)
y.onkey(seguir_reto, "w")
y.onkey(seguir_para_tras, "s")
y.onkey(virar_esquerda, "a")
y.onkey(virar_direita, "d")
limpar() #Chamada da função limpar!
y.bgcolor("green")
y.exitonclick()

