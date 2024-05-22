



class VentaEntradas():
    NomPelicula = ""
    ValEntrada = 0
    CantEntrada = 0
    Total = 0
    Dscto = 0
    TotalPagar = 0

    def __init__(self) -> None:
        pass
    
    def IngresarDatos(self):
        print("")
        print("...................... VENTA DE ENTRADAS .............................")
        print("==============================================================================")
        print("")
        self.NomPelicula = input("Ingrese el Nombre de la Pelicula ...............:")
        self.ValEntrada = int(input("Ingrese Valor de la Entrada .............:"))
        self.CantEntrada = int(input("Ingrese Cantidad de Entradas ................"))

    def Finalizado(self):
        self.Total = self.ValEntrada * self.CantEntrada
        self.TotalPagar = self.Total - self.Dscto

        if self.Total < 99999:
            self.Dscto = 0
        
        if self.Total > 99999 and self.Total < 200000:
            self.Dscto = self.Total * (5/100)
            self.TotalPagar = self.Total - self.Dscto

        if self.Total >= 200000 and self.Total < 400000:
            self.Dscto = self.Total * (10/100)
            self.TotalPagar = self.Total - self.Dscto

        if self.Total >= 400000:
            self.Dscto = self.Total * (20/100)
            self.TotalPagar = self.Total - self.Dscto


class Venta():
    
    def __init__(self) -> None:
        pass

    def TotalFinalPagar(self):
        print("=========================== TOTAL FINAL A PAGAR ==============================")
        print("El Total a Pagar es ", self.TotalPagar)

class Final(VentaEntradas, Venta):

    pass
    
    

Objeto1 = Final()
Objeto1.IngresarDatos()
Objeto1.Finalizado()
Objeto1.TotalFinalPagar()

Objeto2 = Final()
Objeto2.IngresarDatos()
Objeto2.Finalizado()
Objeto2.TotalFinalPagar()
