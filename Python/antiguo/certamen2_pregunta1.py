#debe retornar el nombre de la tienda y el local mas cercano a las coordenadas de la persona 
def tienda_mas_cercana(nombre_archivo_tiendas, x, y):
    f = []
    a = open(nombre_archivo_tiendas, "r")
    for linea in a:
        lista = linea.strip().split(";")
        tienda = lista[0]
        locales = lista[1].split(":")
        for local in locales:
            posi = local.split(",")
            lugar = posi[0]
            x1 = int(posi[1])
            y1 = int(posi[2])
            cord = ((x - x1)**2 + (y - y1)**2)**(1/2)
            f.append((cord,lugar,tienda))
    a.close()
    s = min(f)
    ret = "{} {}".format(s[2], s[1])
    return ret
    
print(tienda_mas_cercana('tiendas.txt', 10, 5))