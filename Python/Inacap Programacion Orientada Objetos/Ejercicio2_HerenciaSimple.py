#       Ejercicio N2 HERENCIA

# Este es el ejercicio mas basico de herencia simple


# Realice un programa en python utilizando herencia simple
# El programa debe calcular el valor venta de articulos electronicos
# Atributos a considerar : RutCliente, Nombre, Producto, Cantidad
# Valor Producto, Total, Descuento y Total a Pagar
# Descuento = -Si Total > 100.000 se aplica un 10% de Dcto del Total
#             -Si Total > 300.000 se aplica un 20% de Dcto del Total
#             -Si Total => 400.000 y 500.000,  se aplica un 30% de Dcto del Total
#             -Si Total > 800.000 se aplica un 40% de Dcto del Total

# El programa debe tener a lo menos 2 clases, una clase padre y la otra clase hija
# La clase Padre debe tener a lo menos: 
# 2 variables publicas, 4 metodos o funciones ( IngresoDatos, Calculos, MostrarDatos )

from os import system
system("cls")

class VentaArtElectron():
    _RutClie = " "
    _Nombre = " "
    Producto = " "
    Cantidad = 0
    ValProd = 0
    Total = 0
    Dscto = 0
    TotalPagar = 0

    def __init__(self) -> None:
        pass

    def IngresoDeDatos(self):
        print("\n\n.........Ingreso de Datos..........")
        print("=======================================")
        self.RutClie = input("Ingrese Rut del Cliente .........:")
        self.Nombre = input("Ingrese Nombre del Cliente ........:")
        self.Producto = input("Ingrese Nombre del Producto ........:")
        self.Cantidad = int(input("Ingrese Cantidad del Producto ........:"))
        self.ValProd = int(input("Ingrese Valor del producto .........:"))

    def CalculosDeDatos(self):
        self.Total = (self.Cantidad * self.ValProd)

        #Calculo del descuento