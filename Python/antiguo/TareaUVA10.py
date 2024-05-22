meses = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo",
         "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre",
         "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}

def obtener_calendario(nombre_archivo):
    d = {}
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        lista = linea.strip().split(";")
        depa = lista[1]
        dia,mes,años = lista[2].split("/")
        nombre = lista[0]
        if depa not in d:
            d[depa] = []
        d[depa].append((mes,dia,nombre))
    archivo.close()
    total = 0
    for depa in d:
        d[depa].sort()
        nuevo = open(depa + ".txt", "w")
        nuevo.write("CUMPLEAÑOS DEL DPTO DE {}\n\n".format(depa))
        total += 1
        aux = {}
        for mes,dia,nombre in d[depa]:
            x = meses[mes]
            if x not in aux:
                aux[x] = 0
            aux[x] += 1
            if aux[x] < 2:
                nuevo.write("Funcionarios nacidos el mes de {}\n".format(x))
                nuevo.write("{} se celebra el cumpleaños de {}\n".format(dia,nombre))
            else:
                nuevo.write("{} se celebra el cumpleaños de {}\n".format(dia,nombre))
            nuevo.write("############################\n\n")
        nuevo.close()
    return total

print(obtener_calendario("Tarea.txt"))

