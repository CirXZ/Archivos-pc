# count = 0
# n = int(input("Ingree un numero: "))
# while count < n:
#     count+= 1
#     if count % 3 == 0:
#         print(count, end = " ")
#     else:
#         pass
# #end of while

# numbers = [2,5,7,15,9]
# i = 0
# while i < len(numbers):
#     print(numbers[i], end =" ")
#     i += 1
# else:
#     print("\nWhile ends. always executed")
#     print("also executed")
# #end of while

# programa que determine el promedio de n cantidad de numeros enteros
 
# cont = 0
# n = int(input("Ingrese cuantos numeros a promediar: "))
# suma = 0
# numero = 1
# while cont < n:
#     numero = int(input("Introduzca un numero entero: "))
#     if numero > 0:
#         suma+= numero
#         cont+=1
# else:
#     promedio = suma/cont

# print(f"El promedio de los {cont} numeros es: ", round(promedio,1))

# programa bucle for con breack

# for c in "ToolsQA":
#     if c == "Q":
#         pass #salta la Q, coninue hace lo mismo, breack rompe ciclo
#     else:
#         print(c, end = " ")

# import statistics
# A = [2,4,6,8,10]
# print("la media de la lista A es:",statistics.mean(A))

# import heapq
# Nvalores = [19,11,4,8,33,22,15]
# print()

# from statistics import mean
# notas = [4,6,7,3,5,2]
# resultado = mean(notas)
# print("La media de las notas es: ", resultado)
# from math import sqrt
# ab = float(input("Escriba el valor de la longitud del vertice AB: "))
# bc = float(input("Escriba el valor de la longitud del vertice BC: "))

# Hipotenusa = sqrt(ab**2 + bc**2)

# print("La longitud de la hipotenusa es: ", Hipotenusa)

# realizar un programa que genere una lista de 10 numeros enteros aleatorios entre 1 y 100 para calcular el maximo y minimo valor, ocupar la funcion max y min

# from random import randint
# A = []
# for i in range(10):
#     w = randint(1,100)
#     A.append(w)

# print(A)
# print("El valor maximo de la lista es: ", max(A))
# print("El valor minimo de la lista es: ", min(A))

# promedio de una lista. deben importar del modulo stadistics la funcion mean

# lista = [2,4,6,8,10]
# resultado = mean(lista)
# print(resultado)

# este programa simula el lanzamiento de un dado
# from random import randint as aleatorio
# from math import pi,e
# lanzamiento = aleatorio(1,6)
# print(lanzamiento)
# if lanzamiento < 4:
#     print(round(pi * lanzamiento,2))
# else:
#     print(round(e * lanzamiento,2))

# calcular la moda de un conjunto de datos numericos y nominales

# from statistics import mode
# numeros = [2,7,2,3,3,2,5,11,3]
# if True:
#     try:
#         print(mode(numeros))
#     except ValueError:
#         print("Existen mas de dos modas en la lista Numeros")

# def enviarMensaje():
#     print("Hola mundo desde funcion")

# print("Hola esto se ejecuta antes de la funcion")
# enviarMensaje()
# print("Esto se ejecuta despues")
# enviarMensaje()
# print("Esto se ejecuta despues de lo anterior")

# Tabla de multiplicar del 5
# def dibujar_tabla_del_5():
#     for i in range(11):
#         print("5 * {} = {}".format(i,i*5))

# dibujar_tabla_del_5()

# def sumar(a,b):
#     print("la suma es", a+b)

# sumar(5,6)
# sumar()



#------------------------------------------------------------------------------------------------------------------------------------


# try:
#     n = float(input("introduce un numero: "))
#     m = 4
#     print("{}/{} = {}".format(n,m,n/m))
# except:
#     print("Ha ocurrido un error, introduzca un valor valido")

# while True:
#     try:
#         n = float(input("Introduzca un numero: "))
#         m = 4
#         print("{}/{} = {}".format(n,m,n/m))
#     except:
#         print("Ha ocurrido un error, introduzca un valor correcto")
#     else:
#         print("Todo ha funcionao correctamente.")
#         break
# try:
#     n = float(input("Introduzca un numero a divir: "))
#     R = 5/n
# except TypeError:
#     print("No se puede dividir el numero entre una cadena")
# except ValueError:
#     print("Debes introducir una cadena que sea un numero")
# except ZeroDivisionError:
#     print("No se puede dividir por cero {0}, intenta otro numero")
# else:
#     print("El resultado es: ", round(R,2))

# class Humano():
#     def __init__(self, edad, nombre, ocupacion):
#         self.edad = edad
#         self.nombre = nombre
#         self.ocupacion = ocupacion
#     def presentar(self):
#         presentacion = ("Hola soy {}, mi edad es {} y mi ocupacion es {}")
#         print(presentacion.format(self.nombre, self.edad, self.ocupacion))
#     def contratar(self, puesto):
#         self.puesto = puesto
#         print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
#         self.ocupacion = puesto
# Persona1 = Humano(31,"Pedro", "Desocupado")
# Persona1.presentar()
# Persona1.contratar("Obrero")
# Persona1.presentar()

# class Alumno():
#     def __init__(self):
#         self.nombre = input("Ingrese nombre del alumno: ")
#         self.nota = float(input("Ingrese nota del alumno: "))
#     def imprmir(self):
#         print("Alumno: ", self.nombre)
#         print("Nota: ", self.nota)
#         print(" ")
#         print(" ")
#     def resultado(self):
#         if self.nota < 4:
#             print("El alumno/a esta reprobado")
#         else:
#             print("El alumno/a esta aprobado")
# alumno1 = Alumno()

# alumno1.imprmir()
# alumno1.resultado()

# miLista = [10,8,6,4,2]
# nuevaLista = miLista[1:3]
# print(nuevaLista)

# miLista = [1,2,3,4]
# print(miLista[1:-1])
# print(miLista[-2:-1])
# print(miLista[-1:-2])
# print(miLista[0:999])

# miLista = [1,2,3,4,5]
# print(miLista[2:])
# print(miLista[ :-1])
# print(miLista[:])

# Lista = ["año", 2021]
# Lista2021 = Lista.copy()
# print(Lista2021)

# Lista = ["año", 2020, 2021,2020]
# print(Lista.count(2020))
# print(Lista.count(2021))
# print(Lista.count(2022))


#------------------------------------------------------------------------------------------------------------------------------

# materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
# aprobado = []
# for materia in materias:
#     notas = float(input("Que nota has sacado en "+ materia + "?"))
#     if notas >= 4:
#         aprobado.append(materia)
# for materia in aprobado:
#     materias.remove(materia)
# print("Tienes que repetir " + str(materias))

#cuenta vocales en una palabra
# palabra = input("Introduce una palabra: ")
# vocales = ["a", "e", "i","o", "u"]
# for vocal in vocales:
#     veces = 0
#     for letra in palabra:
#         if letra == vocal:
#             veces += 1
#     print("La vocal "+ vocal + " aparece "+ str(veces)+ " veces")

# tupla = "a","a","a"
# print(type(tupla))
# tupla = ("Nelvin", "Andrade", "INACAP", 2021)
# #si se quiere crear una tupla con un unico valor debemos finaliza con ,
# version = ("1.0",)

#-------------------------------------------------------------------------------------------------------------------------------

# tupla = ("Nelvin", "Andrade", "INACAP", 2021)
# #Es posible recorrer elementos con for
# for t in tupla:
#     print(t, end = " ")
# print("\n")
# print(tupla[0:2])
# clon = tupla[ : ]
# print(clon)
# print(type(clon))
# # tupla[0]= "Maria" error

# miTupla = (1,10,100)

# t1 = miTupla + (1000,10000)
# print(t1)
# t2 = miTupla *3
# print(t2)

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in miTupla)
# print(-10 not in miTupla)

# a = "palabra"
# lista = list(a)
# print(lista)

#palindromo

# palabra = input("Introduce una palabra")
# reversed_palabra = palabra
# palabra = list(palabra)
# reversed_palabra = list(reversed_palabra)
# reversed_palabra.reverse()
# if palabra == reversed_palabra:
#     print("Es un palindromo")
# else:
#     print("No es un palindromo")

# diccionario = {"gato":"cat", "perro":"dog", "virus": "virus"}
# print(diccionario["gato"])
# print(diccionario.keys())
# print(diccionario.values())
# print("dog" in diccionario)
# print("gato" in diccionario)
# # print(diccionario["conejo"])
# for k in diccionario:
#     print(k)

#------------------------------------------------------------------------------------------------------------------------------------------------------

# import numpy as np
# arr = np.array([3,5,7])
# print(arr.sum())
# print(type(arr))
# print()
# a = np.array([1,2,3])
# print(a)
# print()

# np.square(a)
# b = np.array([5,6,7])
# print(b)
# print(a+b)
# print(a-b)

# m = np.array([[10,11,12],[13,14,15]])
# print(m.shape)
# print(m.dtype)
# print(m.ndim)
# print(m)

# m = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])
# print(m.shape)
# print(m.dtype)
# print(m.ndim)
# print(m)

#--------------------------------------------------------------------------------------------------------------------------------------

# import numpy as np

# a = np.reshape(np.array(range(1,26)),(5,5))
# print(a)
# print()
# print(a[1])
# print()
# print(a[-2])
# print()
# print(a[1][2])
# print()
# print(a[1,2])
# print()
# print(a[1:4,3])
# print()
# print(a[1:3, 2:4])

# print(a[:3, 3:])
# print()
# print(a[:, 3])
# print()
# print(a[3, :])
# print()
# print(a[3, :])
# print(a[:2, :])

# print(a[[3,1]])
# print()
# print(a[[3,1],[2,0]])
# print()
# print(a[[4,2],[1,3]])

# a = np.array([[1,2,3],[4,5,6]])
# print(a+1)
# print()
# print(a-1)
# print()
# print(1+a)
# print()
# print(1-a)
# print()
# print(a*2)
# print()
# print(a*1.5)
# print()
# print(a/2)
# print()
# print(a/2.5)
# print()
# print(a**2)
# print()
# print(2**a)

# def buble_sort(num):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(num)-1):
#             if num[i] > num[i+1]:
#                 num[i], num[i + 1] = num[i + 1], num[i]
#                 swapped = True
# a = [-2,5,3,9,33,-12,8]
# buble_sort(a)
# print(a)

# nombre = input("¿como te llamas? ")
# edad = input("¿cuantos años tienes? ")
# direccion = input("¿cual es tu direccion? ")
# telefono = input("¿cual es tu numero de telefono? ")
# persona = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
# print(persona["nombre"], " tiene ", persona["edad"], " años, vive en ", persona["direccion"]," y su numero de telefono es ", persona["telefono"])

#---------------------------------------------------------------------------------------------------------------------------------------

