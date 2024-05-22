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

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)