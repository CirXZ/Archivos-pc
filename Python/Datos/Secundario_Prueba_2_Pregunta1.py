from Principal_Prueba_2_Pregunta1 import SuperCar

from os import system

system("cls")

# class VentaVehiculo(SuperCar):
    
#     def MostrarDatos(self):
#         SuperCar().TotalFinalPagar(self)




class VentaVehiculo(SuperCar):
    pass


# =============================== OBJETOS ===================================

Objeto1 = VentaVehiculo("21218773-9", "Nissan", 200000)
Objeto1.IngresarDatos()
Objeto1.CalculoDeDatos()
Objeto1.ListarDatos()
Objeto1.TotalFinalPagar()

Objeto2 = VentaVehiculo("8408322-2", "Subaru", 1000000)
Objeto2.IngresarDatos()
Objeto2.CalculoDeDatos()
Objeto2.ListarDatos()
Objeto2.TotalFinalPagar()