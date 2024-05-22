taxis = [ ('t01',(2.5,3),'d'), ('t02',(98,323),'o'),
('t03',(323,32),'d'), ('t04',(0.2,3434),'d'), ('t05',(2323,454),'o'),
('t06',(64,75),'d'), ('t07',(23,4),'d'), ('t08',(254,740),'o'),
('t09',(1,1),'d'), ('t10',(53,3),'d'), ('t11',(2354,40),'o'),
('t12',(231,10),'o') ]

pasajeros = [ ('p01', (23,43)), ('p02', (2,545)), ('p03',(2,5)),
('p04', (65,76)), ('p05', (75,5)), ('p06',(12,7)),
('p07', (11,66)), ('p08', (22,56)),('p09',(88,9))]

# d = ((x2-x1)**2+(y2-y1)**2)**(1/2)

def taxis_disponibles(a):
    lista = []
    for codigo, (x, y), estado in a:
        if estado == "d":
            lista.append((codigo,x,y))
    return lista
#_______________________comentarios de duda______________________
#quizas una distancia le sirva a uno pero al que esta procesando no.
#como necesito actualizar el estado de la lista taxis, tengo que tomar en cuenta el prgrama principal y
#en especial la variable "s", que es la que se asigna al pasajero, y claro, ir limpiando la lista pasajeros 
#________________________________________________________________

def actualizar_estado(a,x):
    lista = []
    for rcod,coordenadas,estado in x:
        if rcod != a:
            lista.append((rcod,coordenadas,estado))
    return lista

def pasajeros_asignados(pas,pasajeros):
    lista = []
    for cod,coordenadas in pasajeros:
        if cod not in pas:
            lista.append((cod,coordenadas))
    return lista

#________________________comentarios de la funcion______________
#recorre la lista de pasajeros y va agregando los que no estan en la lista "pas" a la nueva lista llamada "lista"
#la va recorriendo hasta añadir los que faltan por ser asignados, claro, en caso de que falten taxis, igual añade los ultimos pasjeros
#gracias al ciclo for que itera sobre la lista pasajeros y va comparando los codigos con los que estan en la lista pas
#__________________________________________________________________

i = 0
tax = taxis_disponibles(taxis)
for codigo, (x, y) in pasajeros:
    nuevo = []
    pas = []    #lista de los pasajeros que ya les fueron asignados un taxi
    for co, x1, y1 in tax:
        d = ((x1-x)**2+(y1-y)**2)**(1/2)
        nuevo.append((d,co))
    if nuevo != []:
        s = min(nuevo)
        print("Taxi ",s[1], "asignado a trasladar el pasajero ", codigo)
        tax = actualizar_estado(s[1], tax)
        print(tax)
        pas.append(codigo)  #se agrega el codigo del pasajero que se le asigno un taxi a una lista
        pasajeros = pasajeros_asignados(pas,pasajeros) #se cambia el valor de la variable utilizando la funcion "f1"
    else:
        if i < 1:
            print("No hay mas taxis")
            i+=1         


#break(seria tan sencillo) 