#el promedio debe ser para los tres alumnos
#las notas deben ser de los 3 alumnos
import numpy as np
# i = 0
# while i < 3:
#     rutt = int(input("Ingrese rut sin puntos ni guion: "))
#     nombre = input("Ingrese nombre de los estudiantes: ")
#     nomarr.append(nombre)
#     rutarr.append(rutt)
#     i+=1

rutarr = []
nomarr = []
asig = []
promarr = []
situacion = []

for i in range(3):
    rutt = int(input("Ingrese rut sin puntos ni guion: "))
    rutarr.append(rutt)
    nombre = input("Ingrese nombre de los estudiantes: ")
    nomarr.append(nombre)
    asignatura = input("Ingrese la asignatura: ")
    asig.append(asignatura)
    nota1 = int(input("Indique su nota1: "))
    nota2 = int(input("Indique su nota2: "))
    nota3 = int(input("Indique su nota3: "))
    promedio = (nota1*0.25)+ (nota2*0.35) + (nota3*0.40)
    promarr.append(promedio) 
    if promedio < 39:
        situa = "reprobado"
        situacion.append(situa)
        print("Situacion final ", situa," ", nombre," ", promedio)
    if promedio >= 40 and promedio <=49:
        situa = "Aprobado"
        situacion.append(situa)
        print("Situacion final ", situa," ", nombre," ", promedio)
    if promedio > 40 and promedio <=70:
        situa = "Eximido"
        situacion.append(situa)
        print("Situacion final ", situa," ", nombre," ", promedio)

promediofinal = sum(promarr) / 3

print("Promedio final de los alumnos es: ", promediofinal)