#                       EJERCICIO4



#   Realice un programa en python utilizando clases y generando objetos
#   Debe generar a lo menos 2 objetos
#   La clase debe utilizar 3 funciones o metodos de parte del usuario
#   Una funcion es para ingresar datos, otra funcion para los calculos y la ultima para listar o mostrardatos
#   Los atributos de la clase son :
#   Rut, Nombre, Asignatura, Nota1, Nota2, Nota3, Promedio, Examen, Promedio final y Situacion
#   Todos los alumnos rinden el examen no importando el promedio por ahora
#   La situacion es: Reprobado, Aprobado, Eximido
#   Todos los datos se ingresan por teclado
#   IMPORTANTE:
#   Todos los datos deben ser traspasados como parametros al constructor




class SuperAlumnos():
    Rutt = ""
    Nomm = ""
    Asigg = ""
    Not1 = 0
    Not2 = 0
    Not3 = 0
    Promm = 0
    Examm = 0
    PrommFinal = 0
    Situu = 0

    def __init__(self, AA,BB,CC,DD,EE,FF,GG,HH,II,JJ):
        self.Rutt = AA
        self.Nomm = BB
        self.Asigg = CC
        self.Not1 = DD
        self.Not2 = EE
        self.Not3 = FF
        self.Promm = GG
        self.Examm = HH
        self.PrommFinal = II
        self.Situu = JJ

    def IngresoDeDatos(self):
        print("")
        print(" ..................Ingreso de Datos..................")
        self.Rutt = input("Ingrese Rut del objeto a crear ............:")
        self.NNom = input("Ingrese Nombre del objeto a crear .....:")
        self.AAsig = input("Ingrese Asignatura...................")
        self.NNot1 = int(input("Ingrese Nota1 del objeto a crear..............:"))
        self.NNot2 = int(input("Ingrese Nota2 del objeto a crear..............:"))
        self.NNot3 = int(input("Ingrese Nota3 del objeto a crear..............:"))

    def CalculosVarios(self):
        #Calculo del promedio
        self.PProm = (self.Not1 + self.Not2 + self.Not3)/3

        #Ingreso del examen
        self.EExa = int(input("Ingrese nota del examen objeto a crear........"))

        #Calculo del promedio final
        self.PromedioFinal = (self.PProm + self.EExa)/2

        #Calculo de la situacion
        if (self.PromedioFinal >= 10 and self.PromedioFinal < 40):
            self.SSit = "Ripley"
        if (self.PromedioFinal >= 40 and self.PromedioFinal < 50):
            self.SSit = "Aprobado"
        if (self.PromedioFinal >= 50 and self.PromedioFinal < 71):
            self.SSit = "Eximido"

    def MostrarDatos(self):
        print("")
        print("......................DATOS DEL OBJETO 1 CREADO.......................")
        print("El Rut del alumno Nuevo creado es        :", self.Rutt)
        print("El Nombre del alumno Nuevo creado es         :", self.Nomm)
        print("La asignatura del alumno Nuevo creado es     :", self.Asigg)
        print ("La Nota 1 del alumno Nuevo creado es       : ",self.Not1);
        print ("La Nota 2 del alumno Nuevo creado es       : ",self.Not2);
        print ("La Nota 3 del alumno Nuevo creado es       : ",self.Not3);
        print ("El Promedio del alumno Nuevo creado es     : ",self.Promm);
        print ("La Nota del Examen del alumno Nuevo es     : ",self.Examm);
        print ("El Promedio Final del alumno creado es     : ",self.PrommFinal);
        print ("La Situación final del alumno creado es    : ",self.Situu);
        print("==============================================")
        print("");


#======= SE CREAN LOS OBJETOS  ======
RRut = "";
NNom = "";
AAsig = "";
NNot1 = 0;
NNot2 = 0;
NNot3 = 0;
PProm = 0;
EExa = 0;
PromedioFinal = 0;
SSit = "";

Alumno1c = SuperAlumnos(RRut,NNom,AAsig,NNot1,NNot2,NNot3,PProm,EExa,PromedioFinal,SSit);
Alumno1c.IngresoDeDatos();
Alumno1c.CalculosVarios();
Alumno1c.MostrarDatos();

