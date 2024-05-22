import  cx_Oracle;



from os import system;
system("cls");

class ArriendoVehiculos():
    Rut = ""
    Nombre = ""
    ValorDia = 0
    CantidadDia = 0
    Total = 0
    Dscto = 0
    TotalPagar = 0

    def __init__(self):
               
        self.ConexionBDMN=cx_Oracle.connect(
            user="system",
            password="123456",
            dsn="localhost/xe"        #dsn = Data Source Name ( Nombre de la funte de los datos )
            #dsn="localhost:1521/xe"  #1521 = Este es el puerto que oracle  que trae por defecto.           
        );

        
        self.AA = self.ConexionBDMN.cursor();
        print("\n=========================================================");
        print(" . . . . . . Conexión Establecida a la BD  . . . . . . !!! ");
        print("===========================================================\n");
    

    def IngresarDatos(self):
        print("")
        print("...................... CHILE ARRIENDO .............................")
        print("==============================================================================")
        print("")
        self.Rut = input("Ingrese su rut ...............:")
        self.Nombre = input("Ingrese su Nombre .............:")
        self.ValorDia = int(input("Ingrese el valor por dia ...............: "))
        self.CantidadDia = int(input("Ingrese la Cantidad de dias ...............: "))



    def CalculoDeDatos(self):
        self.Total = (self.ValorDia * self.CantidadDia)

        #calculo del descuento
        if  (self.Total > 0 and self.Total < 100000):         #Puede ser if  (self.Total > 0 and self.Total <= 99999)
            self.Dscto = 0

        if  (self.Total >= 100000 and self.Total < 300000):
            self.Dscto = ((self.Total * 10) / 100)
        
        if (self.Total >= 300000):
            self.Dscto = ((self.Total * 20) / 100)

        #calculo del total a pagar
        self.TotalPagar = (self.Total - self.Dscto)
        

    def ListarDatos(self):
        print("")
        print("............................ LISTADO DE DATOS .............................")
        print("===========================================================================")
        print("El Nombre ................:", self.Nombre)
        print("El Valor por dia ..................:", self.ValorDia)
        print("La cantidad de dias ....................: ",self.CantidadDia);
        print("El Total es ...............................: ",self.Total);
        print("El Descuento es ...........................: ",self.Dscto);
        print("El Total a pagar es ...............................: ",self.TotalPagar);

    def InsertarDatos(self):
        print("\n==========================================================")
        print("\n . . . . . . GRBADO DE REGISTROS EN LA BD . . . . . . .!!!")
        print("============================================================")

        try:
            print(" ")
            print("       ....  LISTADO DEL SUELDO CON BD  ....       ")
            print(" ==================================================")
            print(" El Rut es ..................: ", self.Rut)
            print(" El Nombre es ..................: ", self.Nombre)
            print(" El Valor por dia es .................: ", self.ValorDia)
            print(" La Cantidad de dias es ..........................: ", self.CantidadDia)
            print(" El Total es ............................: ", self.Total)
            print(" El Descuento es .....................: ", self.Dscto)
            print(" El Total a pagar es .....................: ", self.TotalPagar)
            print("")

            # ==================== GRABADO DE DATOS ======================

            self.AA.execute("Insert into ChileArriendo (Rut, Nombre, ValorDia, CantidadDia, Total, Dscto, TotalPagar) VALUES ('{}','{}',{},{},{},{},{})".format(self.Rut, self.Nombre, self.ValorDia, self.CantidadDia, self.Total, self.Dscto, self.TotalPagar))
            self.ConexionBDMN.commit()
            
            print("====================================================")
            print(" .............. Registro Insertado ............. ")
            print("====================================================")
        except Exception:
            print("\n==================================================")
            print(" .......... Error al Grabar los Datos ............ ")
            print("\n==================================================")


    def EliminarUnRegistro(self):
        try:
            self.RRut  = input("Ingrese rut a Eliminar ........................: ")
            self.AA.execute("Delete From ChileArriendo where Rut = ","'"+self.RRut+"'")
            self.ConexionBDMN.commit()
            print("====================================================")
            print(" .............. Registro Eliminado ............. ")
            print("====================================================")

        except Exception:
            print("\n==================================================")
            print(" .......... Error al Eliminar el Registro ............ ")
            print("\n==================================================")

    def ActualizarRegistros(self):
        try:
            self.RRut = input("Ingrese Rut del Registro a Modificar ........:")
            self.AA.execute("Update From ChileArriendo set Nombre  = 'Eileen', CantidadDia = 12 where rut = '" +self.RRut+ "'")
            self.ConexionBDMN.commit()
            print("\n\n")
        except Exception:
            print("Error al Modificar el Registro .....") 

    def Listado1(self):         
        try:        
            self.AA.execute("Select * From ChileArriendo");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            # Busque = self.AA.fetchone();  # Devuelve solo un  registros de la consulta , solo el primer registro
            print(" " );
            print(" Los datos son  :\n", Busque);
            print(" " );
        except Exception:
            print("\n==============================================");
            print("....... Error  en la Consulta  Realizado ....... ");
            print("==============================================\n");
    def Listado2(self):        
        try:
            # Cursor ejecuta la consulta que  almacena AA
            self.AA.execute("Select * From  ChileArriendo"); 
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            print(" " );
            print("\n  ================ LISTADO  Nº2 DESDE LA  BASE DE DATOS ================");
            print("");   
            print(" El Rut es  ........ :",Busque[0]);
            print(" El Nombre es ...... :",Busque[1]); 
            print(" El valor por dia........ :",Busque[2]);
            print(" La cantidad de dias ... :",Busque[3]);
            print(" el total : ....:",Busque[4]);
            print(" El descuento es .....: ", Busque[5])
            print(" El total a pagar es .....: ", Busque[6])                        
            print(" " ); 
        except Exception:
            print("\n==============================================");
            print("....... Error  en la Consulta  Realizada ....... ");
            print("==============================================\n");

    def Listado3(self):        
        try:
            # Cursor ejecuta la consulta que  almacena el cursor llamado AA
            self.AA.execute("Select * From  ChileArriendo");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            print(" " );
            print("\n   ========== LISTADO Nº3 DESDE LA BASE DE DATOS =========");
            print("");   

            for x in Busque :
                print(" El Rut es  ........ :",Busque[0]);
                print(" El Nombre es ...... :",Busque[1]); 
                print(" El valor por dia........ :",Busque[2]);
                print(" La cantidad de dias ... :",Busque[3]);
                print(" el total : ....:",Busque[4]);
                print(" El descuento es .....: ", Busque[5])
                print(" El total a pagar es .....: ", Busque[6])                        
                print(" " ); 
        except Exception:
                print("\n==============================================");
                print("....... Error  en la Consulta 3  Realizado ....... ");
                print("==============================================\n");





##          Programa Opciones

while True:
    print("Bienvenidos a Chile Arriendos, elija que opcion desea realizar:")
    print("1.-Arriendo de Vehiculos")
    print("2.-Autor del Programa")
    print("3.-Salir del Programa")
    Opciones = input("Ingrese Opcion: ")
    if Opciones == "1":
        Objeto1 = ArriendoVehiculos()
        Objeto1.IngresarDatos()
        Objeto1.CalculoDeDatos()
        Objeto1.ListarDatos()
        Objeto1.InsertarDatos()
        Objeto1.Listado1()
    if Opciones == "2":
        print("Cristopher roman, vespertino, 152-v, 13-12-2023, Cesar Arce")
    if Opciones == 3:
        Salir = input("Esta seguro de que desea salir?")
        if Salir == "Si":
            break
        if Salir == "No":
            continue


    # Opciones = int(input("Bienvenidos a ChileArriendo, elija que es lo que desa hacer\n1.-Arriendo de Vehiculos\n2.-Autor del Programa\n3.-Salir del Programa"))