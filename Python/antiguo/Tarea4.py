#adivina el umbral 
from random import randint
intentos = int(input("ingrese cantidad de intentos:"))
contador = 1
logros = 0
derrotas = 0
while contador <= intentos:
    flag = True
    suma = 0
    while flag:
        n = int(input("Ingrese intento " + str(contador) + ":"))
        umbral = randint(1,100)
        if n > 999:
            flag = False
            while n > 0:
                ultimo_digito = n % 10
                suma += ultimo_digito
                n = n // 10
            if umbral % 2 == 0: #[como es par la suma debe ser mayor que el umbral]
                if suma > umbral:
                    print("intento ganado!! suma: ", suma, " umbral: ", umbral)
                    logros += 1
                else:
                    print("intento perdido!! suma: ", suma, " umbral: ", umbral)
                    derrotas += 1
            else:
                if suma < umbral:
                    print("intento ganado!! suma: ", suma, " umbral: ", umbral)
                    logros += 1
                else:
                    print("intento perdido!! suma: ", suma, " umbral: ", umbral)
                    derrotas += 1    
        else:
            print("El número no es válido.")
    contador += 1
if logros > derrotas:
    print("Felicitaciones, ganaste la partida")
else:
    print("Lo siento, perdiste la partida")
