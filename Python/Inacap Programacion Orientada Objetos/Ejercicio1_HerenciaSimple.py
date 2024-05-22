#       Ejercicio N1 HERENCIA

# Este es el ejercicio mas basico de herencia simple
# Los ejercicios con herencia, a lo menos deben tener dos clases
# En el mismo archivo. una clase padre y la otra clase hija.
# La clase padre : esta es la clase donde sacara codigo la clase hija.
# La clase hija : Tambien conocida como sub-clase, es aquella clase que sacara codigo de otra clase
#                (de una clase padre)


from os import system
system("cls")

#Class Padre llama carreras
class Carreras():
    Numlab = 99 # Atributo publico 

    # Constructor que recibe 4 argumentos: Asig, Prof, NHrs, TipoA
    def __init__(self, Asig, Profe, NHrs, TipoA) -> None:
        self.Asignatura = Asig
        self.Profesor = Profe
        self.NumeroHrs = NHrs
        self.TipoAsig = TipoA

    def MostrarDatos(self):
        print("\n................ MUESTRA DE DATOS ..................")
        print("La asignatura creada es ...........................: ", self.Asignatura)
        print("El porfesor que dicta la asignatura es.......: ", self.Profesor)
        print("El numero de Horas de la asignaturas es ............: ", self.NumeroHrs)
        print("El tipo de asignatura es ......................: ", self.TipoAsig)
        print("La clase se dicta en el laboratorio N°......: ", self.Numlab)


#   ========================    Esta es otra clase  ================================

# Clase hija o sub-clase llamada enfermeria
# Esta clase no tiene constructor, atributos, etc, todo lo hereda de la clase padre

class Enfermeria(Carreras):
    pass

# ............ SE CREA EL OBJETO 1 DE ENFERMERIA ......................
# Se instancia o copia la clase ENFERMERIA, pero hereda el constructor , los atributos
# y el metodo CrearAsignatura de la clase padre
Carrera1 = Enfermeria("Farmacologia", "JuanPerez", 72, "Practica")
Carrera1.MostrarDatos()

# ........... SE CREA EL OBJETO 2 .......................
# Se instancia o copia la clase ENFERMERIA, pero hereda el constructor, los  atributos 
# y el metodo CrearAsignatura de la clase padre
Carrera2 = Enfermeria("Anatomia", "Alumnos", 88, "Teorica")
Carrera2.MostrarDatos()
Carrera2.Numlab = 777
Carrera2.MostrarDatos()