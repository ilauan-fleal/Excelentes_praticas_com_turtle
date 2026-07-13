

from turtle import *

from random import random

n = Turtle()

for z in range(20):
    passos = int(random() * 100)
    angulo = int(random() * 150)
    n.right(angulo) #right()
    n.fd(passos) #forward()



n.screen.mainloop()