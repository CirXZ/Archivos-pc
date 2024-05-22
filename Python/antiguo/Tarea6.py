frase = input("Frase:" ) 
frase += "."
nuevo = ""
final = ""
for letra in frase:  #recorriendo el string
    if letra == " " or letra == ".":
        if len(nuevo) >= 6:
            final+=" "
            for x in nuevo:
                if x not in "aeiou":
                    final += x
        else:
            final+=" " +nuevo
        nuevo = ""     #reiniciando la variable 
    else:
        nuevo += letra
print(final)