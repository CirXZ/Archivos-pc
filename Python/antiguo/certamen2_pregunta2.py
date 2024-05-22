from typing import Text


def analizar_productos(nombre_archivo_tiendas):
    l = {}
    a = open(nombre_archivo_tiendas, "r")
    for linea in a:
        lista = linea.strip().split(";")
        tienda = lista[0]
        tuki = open(tienda +".txt") #no puedo creer que era solo eso 
        for linea in tuki:
            lista = linea.strip().split(";")
            if lista[2] != "0":
                producto = lista[0]
                precio = lista[1]
                if producto not in l:
                    l[producto] = []
                l[producto].append((precio, tienda))
    a.close()
    tuki.close()
    i = 0
    for producto in l:
        nuevo = open(producto + ".txt", "w")
        i += 1
        s = 0
        suma = 0
        for x in l[producto]:
            nuevo.write("{}: ${}\n".format(x[1], x[0]))
            suma += int(x[0])
            s += 1
        promedio = int(suma/s)
        nuevo.write("Precio promedio para {}: ${}".format(producto, promedio))
        nuevo.close()
    return i



print(analizar_productos('tiendas.txt'))

