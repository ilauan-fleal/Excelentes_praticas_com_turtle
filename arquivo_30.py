#Extraindo cor de imagem com Python!!


import colorgram

cores_rgb = [] #Lista , que irá armazenar as cores RGB!

cor = colorgram.extract('images.jpg', 10)


for x in cor:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b

    nova_cor = (r,g,b)
    cores_rgb.append(nova_cor)

print(cores_rgb)
