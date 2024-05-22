texto= input("ingrese texto:")
significado= input("ingrese significados:")
resultado = ""
definicion=""
traduccion=""
k=0
ad=0
i=0
for letra in significado:
    if letra != "$":
        resultado +=letra
    else:
        indice=significado.index("$")
        significado=significado[indice+1:len(significado)]
        resolucion = ""
        i=0
        flag= True
        
        while flag:
            if resultado[i] == "*":
                flag=False
                atajo=resultado[:i] # esta supongo que es lo que buscaba 
                definicion=resultado[i+1:]
            else:
                resolucion += resultado[i]
                i+=1
                
        seguir=True
       
        while (k<len(texto)and seguir): 
            if texto[k:len(atajo)+k]==atajo:#asi quedo 
                traduccion+=definicion.upper()
                k+=len(atajo)
                seguir=False
            else:
                traduccion+=texto[k]
                k+=1
        resultado=""
print(traduccion)
