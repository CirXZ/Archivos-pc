#      EJERCICIO 1
#   CLASES CON OBJETOS

#   Realice un programa que calcule la venta de productos utilizando clases en python
#   La clase tiene que crear a lo menos dos objetos
#   Debe utilizar un minimo de dos funciones o metodos creados por el usuario
#   Un metodo o funcion debe ser para ingresar los datos
#   El otro metodo o funcion debe ser para listar o mostrar los datos
#   Los datos se deben ingresar por teclado
#   Los atributos para la clase son: nombre cliente, producto, cantidad, valor unitario


class Venta():
    Nomcli = " ";
    Prod = " ";
    Cant = 0;
    Valor = 0;

    def __init__(self) -> None:
        pass;
    def IngresoDeDatos(self):
        print("\n\n.........Ingreso de Datos..........")
        print("=======================================")
        self.Nomcli = input("Ingrese Nombre del cliente ....:")
        self.Prod = input("Ingrese el Nombre del objeto ..:")
        self.Cant = input("Ingrese Cantidad del objeto ...:")
        self.Valor = input("Inngrese el valor del objeto ...:");

    def MostrarDatos(self):
        print("............. LISTADO DE DATOS .............")
        print("El Nombre del Cliente es .............:", self.Nomcli)
        print("El Nombre del producto es ............:", self.Prod)
        print("La Cantidad del producto es ............:", self.Cant)
        print("El Valor del producto es ............:", self.Valor)
        print("=======================================")
        print("");

#-=================== SE CREAN LOS OBJETOS SE INGRESAN Y SE MUESTRAN LOS DATOS ===================#

from os import system
system("cls")

#   Se crean el Objeto 1, se ingresan los datos y se muestra los datos
Objeto1 = Venta();          #   Se crea el Objeto 1
Objeto1.IngresoDeDatos();   #   Se llama a la funcion que ingresa los datos
Objeto1.MostrarDatos();     #   Se llama a la funcion que muestra los datos

#   Se crean el Objeto 2, se ingresan los datos y se muestra los datos
Objeto2 = Venta();          #   Se crea el Objeto 1
Objeto2.IngresoDeDatos();   #   Se llama a la funcion que ingresa los datos
Objeto2.MostrarDatos();     #   Se llama a la funcion que muestra los datos