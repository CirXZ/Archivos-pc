fa = input("ingrese fecha actual:") #fecha actual
flag = True
suma = 0
i = 0
v = 0 
while flag:
    codigo = input("ingrese codigo:")
    valor = int(codigo[13:])
    fr = codigo[:3] #fruta
    fs = codigo[4:12] #fecha de salida
    print(fs)
    l = contenedor_vencido(fa,fr,fs)
    if l == False:
        print("Fruta en buen estado")
    else:
        suma+= valor
        v += 1
        print("Contenedor vencido")
    
    i +=1
    if codigo[0] == "F" or codigo[0] == "f":
        flag == False
    i +=1

total = i
porcentaje = round((total*v)/100, 2)
print("Contenedores ingresados", total)
print(porcentaje," $caducados")
print("Perdida efectiva", suma)