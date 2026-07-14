

from turtle import *
import random

n = Turtle()
n.hideturtle() #Ocultar a tartaruga!
k = Screen()

#Definindo dimensções da tela com k.setup()

k.setup(width=500, height=500)

#Criando caixa de diálogo com o usuário!

opiniao_usuario = k.textinput(title="Faça sua aposta:", prompt="Qual tartaruga irá vencer a corrida? Escolha uma cor:")

cores = ["blue", "red", "pink", "green", "orange", "gray"]

y_posicoes = [-70, -40, -10, 20, 50, 80]

liberar_corrida = False

lista_tartarugas = []


for z in range(0,6): #Nessa corrida, terão seis tartarugas , no total!
    n = Turtle(shape="turtle")
    n.color(cores[z])
    n.penup()
    n.goto(x=-230, y = y_posicoes[z])
    lista_tartarugas.append(n)


if opiniao_usuario:
    liberar_corrida = True


while liberar_corrida:
    for z in lista_tartarugas:
        if z.xcor() > 230:
            liberar_corrida = False
            cor_vencedora = z.pencolor()
            if cor_vencedora == opiniao_usuario:
                print(f"Você está correto! A cor vencedora é: {cor_vencedora}!\n")
            else:
                print(f"Você perdeu! A cor vencedora é: {cor_vencedora}!\n")
        distancia_total = random.randint(0,10) 
        z.forward(distancia_total)


k.exitonclick()