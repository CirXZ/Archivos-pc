#   Este es el archivo N°2  
#   Se llama "MetFuncion.py"

class Metodos():
    NP = ""
    VE = 0
    CE = 0
    TT = 0
    DC = 0
    _TP = 0

    def __init__(self) -> None:
        pass

    def IngresarDatos(self):
        print("")
        print("...................... VENTA DE ENTRADAS AL CINE .............................")
        print("==============================================================================")
        self.NP = input("Ingrese nombre de la pelicula ...............:")
        self.VE = int(input("Ingrese valor de la entrada .............:"))
        self.CE = int(input("Ingrese cantidad de entradas ............:"))

        #calculo del total.
        self.TT = (self.VE * self.CE)

        #calculo del descuento
        if  (self.TT > 0 and self.TT < 100000):         #Puede ser if  (self.TT > 0 and self.TT <= 99999)
            self.DC = 0

        if  (self.TT >= 100000 and self.TT < 200000):
            self.DC = ((self.TT * 10) / 100)
        
        if (self.TT >= 200000):
            self.DC = ((self.TT * 20) / 100)

        #calculo del total a pagar
        self._TP = (self.TT - self.DC)

    
    def ListarDatos(self):
        print("")
        print("............................ LISTADO DE DATOS .............................")
        print("===========================================================================")
        print("El Nombre de la Pelicula es ................:", self.NP)
        print("El Valor de la Entrada es ..................:", self.VE)
        print ("La cantidad de Entradas....................: ",self.CE);
        print ("El Total es ...............................: ",self.TT);
        print ("El Descuento es ...........................: ",self.DC);
        print ("El Total a Pagar es de ....................: ",self._TP);

from os import system
system("cls")
