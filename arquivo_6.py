#Carimbo da forma da tartaruga.

#Uso de clearstamp() para limpar.


from turtle import *

s = Turtle()
s.color('blue')

id_cod = s.stamp()

s.forward(100)

s.clearstamp(id_cod)

k = s.position()

print(k)