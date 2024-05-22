
## Cristopher Roman
## 21218773-9
## 162-v
## Profesor: Cesar Arce 
## Informatica
## 08-11-23


class SuperCar():
    Rut = ""
    Vehi = ""
    ValVehi = 0
    Cant = 0
    Total = 0
    ForPagos = ""
    Dcto = 0
    _Interes = 0
    TotalPagar = 0

    def __init__(self, AA, BB, CC) -> None:
        self.Rut = AA
        self.Vehi = BB
        self.ValVehi = CC

    def IngresarDatos(self):
        print("")
        print("...................... VENTA DE VEHICULOS .............................")
        print("==============================================================================")
        print("")
        self.Cant = input("Ingrese cantidad de vehiculos ...............:")
        self.ForPagos = int(input("Ingrese Forma de Pago .............:"))
        
    def CalculoDeDatos(self):
        self.Total = (self.Cant * self.ValVehi)

        if (self.ForPagos == "Contado"):

            self.Dcto = (20/100)
            self.TotalPagar = self.Total - (self.Total * self.Dcto) 

        if (self.ForPagos == "Tarjeta Banco"):

            self.Dcto = (10/100)
            self.TotalPagar = self.Total - (self.Total * self.Dcto) 

        if (self.ForPagos == "Cheque"):
            print("Indique el Tipo de Cheque:")
            if self.ForPagos == "Cheque a Fecha":
                self.Fecha = input("Indique Tiempo(Ejemplo 1 Mes):")
                self._Interes = self.Total * (10/100) * self.Fecha
                self.TotalPagar = self.Total + (self._Interes)

        if (self.ForPagos == "Tarjeta Tienda"):
            self.Fecha = input("Indique Tiempo(Ejemplo 1 Mes):")
            self._Interes = self.Total * (20/100) * self.Fecha
            self.TotalPagar = self.Total + (self._Interes)

    def ListarDatos(self):
        print("")
        print("............................ LISTADO DE DATOS .............................")
        print("===========================================================================")
        print("El Nombre del Vehiculo ................:", self.Vehi)
        print("El Valor del Vehiculo es ..................:", self.ValVehi)
        print("La cantidad de vehiculos ....................: ",self.Cant);
        print("El Total es ...............................: ",self.Total);
        print("El Descuento es ...........................: ",self.Dcto);

    def TotalFinalPagar(self):
        print("=========================== TOTAL FINAL A PAGAR ==============================")
        print("Segun La Forma de Pago ", self.ForPagos," el Total a Pagar es", self.TotalPagar)
    


