




lista = []
print("1.- Crear Tarea")
print("2.- Modificar Tarea")
print("3.- Consultar Tarea")
print("4.- Salir")
flag = True
i = 0
while flag:
    n = int(input("ingrese opcion:"))
    if n == 1:
        #poner caso en que se borra una tarea, el id ental caso tabie se borraria o se resetearia
        print("Selecciono la opcion crear")
        Nom = input("Nombre:")
        A_i = input("Año de inicio:")
        M_i = input("Mes de inicio:")
        D_i = input("Dia de inicio:")
        A_t = input("Año de finalizacion:")
        M_t = input("Mes de finalizacion:")
        D_t = input("Dia de finalizacion:")
        i += 1
        lista.append([i,Nom, "pendiente", [A_i,M_i,D_i], [A_t,M_t,D_t]])
        print("El id de esta tarea es:", i)
        print("Tarea ingresada correctamente!!")
    elif n == 2:
        print("Selecciono la opción modificar")
        id_tarea = input("ID de la tarea?:")
        #lista vacia 
        for x in lista:
            print(x)
            if x[0] == id_tarea: 
                print("Nombre: ", x[1])
                print("Estado: ", x[2])
                print("Fecha de inicio: ", x[3][0], ", ", x[3][1], ", ", x[3][2])
                print("Fecha de termino: ", x[4][0],", ", x[4][1], ", ",  x[4][2])
                estado = input("Indique el nuevo estado: ")
                lista.insert(2, estado)
                print("Estado de la tarea, actualizado!!")                            
            else:
                print("Tarea no encontrada")
                id_tarea = input("ID de la tarea?:")
    elif n == 3:
        print("Sleecciono la opcion consultar")
        categoria = input("Indique el nombre de la categoria que desea listar:")
        for r in lista:
            if r[2] == categoria:
                print("Tareas que se encuentran en el estado: ", categoria)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                print("Tarea: ", x[0], "- ", x[1],"Inicio: " , x[2], x[3], )
    else:
        if n == 4:
            print("Selecciono la opción salir")
            print("Hasta pronto!!")
            flag = False

