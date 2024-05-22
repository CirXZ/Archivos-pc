#   Este es el archivo N°1
#   Se llama "Principal.py"

#       EJEMPLO N°1
#  HERENCIA ENTRE ARCHIVOS

# La herencia entre archivos conciste en tener un minimo de dos archivos python, donde uno de ellos el principal
# hace uso de codigo o de una clase del otro archivo.

from os import system
system("cls")

# llamo al archivo metFunciion e importo la clase Metodos
from MetFuncion import Metodos

# creo la clase Principal
class principal():
    Mett = Metodos() # variable que instancia la clase Metodos

    def __init__(self) -> None:
        pass

    def CorrerPrograma(self):
        self.Mett.IngresarDatos()
        self.Mett.ListarDatos()

#   CREO LOS OBJETOS

#   OBJETO 1
Venta1 = principal()
Venta1.CorrerPrograma()
print("")

#   OBJETO 2
Venta2 = principal()
Venta2.CorrerPrograma()
print("")

print("\n\n==============================================================")
print(".................... FIN DEL PROGRAMA ............................")
print("==============================================================\n\n")