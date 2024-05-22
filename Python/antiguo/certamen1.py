def dias(f):
    a = int(f[:4])
    m = int(f[4:6])
    d = int(f[6:])
    print(d, a, m)
    dd = (a-1)*365 + (m-1)*30 + d
    return dd
def dif(x, ñ):
    d1 = dias(x)
    d2 = dias(ñ)
    r = abs(d1-d2)
    return r

def contenedor_vencido(fecha_actual, fruta, fecha_salida):
    d = dif(fecha_actual, fecha_salida)
    a = d//365
    m = (d-a*365)//30
    d = d%30 
    suma = d + (m*30)
    if fruta == "CER":
        if suma > 30:
            return True
        return False
    elif fruta == "UVA":
        if suma  > 45:
            return True
        return False
    elif fruta == "MAN":
        if suma  > 60:
            return True
        return False
    elif fruta == "BER":
        if suma  > 25:
            return True
        return False
    else:
        if suma   > 50:
            return True
        return False

#print(contenedor_vencido("20211028", "MAN", "20210830"))
#________________programa principal_______________

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