#contexto
def suma_productos(rut):
    suma_n = 0
    i = 2 # constante a multiplicar, comenzando por la derecha: 2, 3, 4, 5, 6, 7, 2, 3
    while rut != 0:
        n = rut %10 # obtiene el d´ıgito de mas a la derecha
        rut = rut//10 # elimina el d´ıgito de mas a la derecha
        suma_n += n*i
        # A continuaci´on, se actualiza la constante para la siguiente iteraci´on
        i += 1
        if i == 8: # despu´es del 7, vuelve a 2
            i = 2
    return suma_n

def digito_verificador(rut):
    p = suma_productos(rut)
    verificador = 11 - (p % 11)
    if verificador == 11:
        verificador = 0
    elif verificador == 10:
        verificador = "k"
    return verificador

#print(digito_verificador(15136120)) 

def votos_partidos(votos, partido):
    total = 0
    nuevo = ""
    votos += "$"
    for letra in votos:   
        if letra != "$":
            nuevo += letra
        else:
            if partido == nuevo:
                total += 1
            nuevo = ""
    return total 


coaliciones = input("ingrese coaliciones:")
votos = input("ingrese votos por partido:")
coalicion = ""
otro = ""
pa = "" #partido
suma = 0 
for letra in coaliciones:
    if letra != ":":
        coalicion += letra
    else:
        otro = coalicion 
        for x in coalicion:
                