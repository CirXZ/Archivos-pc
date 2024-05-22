#           TAREA PARA EL VIERNES


#   -Realice una clase en python para crear objetos celulares
#   -La clase debe tener 3 metodos o funciones creados por el usuario
#   -Una funicion para ingresar los datos, otra para los calculos y la otra listar o mostrar
#   -Atributos de la clase: Nombre del cliente, Nombre del producto, Valor producto, Cantidad total, Descuento y Total a pagar 
#   -Si total > 100.00 se aplica 10% de descuento del total
#   -Si total > 500.00 se aplica 20% de descuento del total
#   -Debe mostrar los datos ordenados
#   -IMPORTANTE: Los datos se deben ingresar por teclado


class Celular():

    Nomcli = " "
    NomPrd = " "
    ValorP = 0
    CantTl = 0
    Descto = 0
    TotalP = 0

    def __init__(self) -> None:
        pass;

    def IngresarDatos(self):
        print("\n\n.........Ingreso de Datos..........")
        print("=======================================")
        self.Nomcli = input("Ingrese Nombre del cliente ....:")
        self.NomPrd = input("Ingrese el Nombre del objeto ..:")
        self.CantTl = int(input("Ingrese Cantidad del objeto ...:"))
        self.ValorP = int(input("Inngrese el valor del objeto ...:"));
    
    def CalcularDatos(self):
        self.TotalP = self.CantTl*self.ValorP
        if self.TotalP >= 100000 and self.TotalP < 500000:
            self.Descto = (self.TotalP * 10) / 100
            self.TotalP = self.TotalP - self.Descto
            return self.TotalP

        if self.TotalP >= 500000:
            self.Descto = (self.TotalP * 20) / 100
            self.TotalP = self.TotalP - self.Descto
            return self.TotalP

    def MostrarDatos(self):
        print("............. LISTADO DE DATOS ............")
        print("El Nombre del Cliente es ..................:", self.Nomcli)
        print("El Nombre del producto es .................:", self.NomPrd)
        print("La Cantidad del producto es ...............:", self.CantTl)
        print("El Valor del producto es ..................:", self.ValorP)
        print("El Valor total a pagar es .................:", self.CalcularDatos())
        print("=========================================================")
        print("");

from os import system
system("cls")

Objeto1 = Celular()
Objeto1.IngresarDatos()
Objeto1.MostrarDatos()