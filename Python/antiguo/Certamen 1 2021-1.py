#"p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
#recorrer el string vots
#separar cada voto
#ver si el voto es el partido que me preguntan
#sumarlo a un contador de votos
#al terminar de recorrer el string
#retornar el contador

def votos_partido(votos, partido):
    contador_votos=0
    votos+='$'
    part_voto=''
    for caracter in votos:
        if caracter == '$':
            if part_voto==partido:
                contador_votos+=1
            part_voto=''
        else:
            part_voto += caracter
    return contador_votos

votos="p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
print(votos_partido(votos, "p3"))
print(votos_partido(votos, "p6"))
print(votos_partido(votos, "p7"))


#recorrer el string de coaliciones
#al llegar a los dos puntos tendremos la coalicion y la imprimiremos
#luego obtendremos los votos de todos los partidos hasta encontrar un ; y los imprimiremos
#en ese momento imprimiremos la cantidad total de la coalicion y compararemos con la coalicion de mayor cantidad de votos
#si es mayor se reemplaza si no no se hace nada
#al terminar de recorrer las coaliciones se mostrara la coalicion ganadora


##c1:p1-p2-p31-p3;c2:p4-p5;c3:p6-p310-p7
coaliciones=input('Ingrese coaliciones: ')
votos=input('Ingrese votos por partido:')
coaliciones+=';'
palabra=''
votos_po_coalicion=0
votos_ganador=0
ganador=''
coalicion=''
for caracter in coaliciones:
    if caracter == ':':
        coalicion=palabra
        print('Coalición: ' + coalicion)
        palabra=''
    elif caracter == '-':
        partido=palabra
        votos_por_partido=votos_partido(votos,partido)
        print(partido,votos_por_partido)
        votos_po_coalicion+=votos_por_partido
        palabra=''
    elif caracter ==';':
        partido = palabra
        votos_por_partido = votos_partido(votos, partido)
        print(partido, votos_por_partido)
        votos_po_coalicion += votos_por_partido
        palabra = ''
        print('Total coalición',coalicion,':',votos_po_coalicion)
        if votos_po_coalicion > votos_ganador:
            votos_ganador=votos_po_coalicion
            ganador=coalicion
        coalicion=''
        votos_po_coalicion = 0

    else:
        palabra+=caracter

print('La coalición ganadora es',ganador,'con',votos_ganador,'votos')