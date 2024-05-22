import json

print("\n==================================================")
print(". . . . . EJMPLO N°1 CONSUMO API EXTERNA . . . . . !!!")
print("\n==================================================")



def LLamarArchivoJson(RutaArchivo):
    open(RutaArchivo)   

    
    with open (RutaArchivo) as RR: 
        DatosArchivos = json.load(RR)
        print(DatosArchivos)


if __name__ == '__main__':
    
    AA = 'C:\Datos\PruebaDatos2Json.json' 
    LLamarArchivoJson(AA)

print("\n==================================================")
print(". . . . . EJMPLO N°2 CONSUMO API EXTERNA . . . . . !!!")
print("\n==================================================")


def LLamarArchivoJson2(RutaArchivo):
    open(RutaArchivo)   

    
    with open (RutaArchivo) as RR: 
        DatosArchivos = json.load(RR)
        print(DatosArchivos)

        

if __name__ == '__main__':
    
    AA = 'C:\Datos\PruebaDatos2Json.json' 
    LLamarArchivoJson2(AA)


