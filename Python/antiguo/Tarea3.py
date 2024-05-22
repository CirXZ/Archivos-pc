ram = 18500
ssd = 42200
envio = 4990
print("Bienvenidos a Kiwi-Factory")
pro = input("¿Cuáles productos comprará? (A) RAM 8GB, (B) SSD 256GB, (C) RAM 8GB y SSD 256GB:")

#____________________Preguntas_______________________
#CASO A
#_______________________LISTO___________________________
if pro == "A":
    un = int(input("¿Cuántas unidades de RAM 8GB?:"))
    if un == 1:
        sub = ram * un 
    elif 2 <= un <= 3:
        ram = 18000
        sub = ram * un
    else:
        if 4 <= un:
            ram = 15500
            sub = ram * un
    print("Subtotal productos: $",sub)
#CASO B
#_______________________LISTO___________________________
elif pro == "B":
    un = int(input("¿Cuántas unidades de SSD 256GB?:"))
    if un == 1:
        sub = ssd * un 
    if 2 <= un <= 3:
        ssd = 40000
        sub = ssd * un
    if 4 <= un:
        ssd = 35000
        sub = ssd * un
    print("Subtotal productos: $",sub)
#CASO C
#______________________LISTO____________________________
else:
    un = int(input("¿Cuántas unidades de RAM 8GB?:"))
    uni = int(input("¿Cuántas unidades de SSD 256GB?:"))
    if un and uni == 1:
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    if 2 <= un and uni <= 3:
        ssd = 40000
        ram = 18000 
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    if 4 <= un and uni:
        ssd = 35000
        ram = 15500
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif un == 1 and 2 <= uni <= 3:
        ssd = 40000
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif 2 <= un <=3 and uni == 1:
        ram = 18000 
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif 4 <= un and uni ==1:
        ram = 15500
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif un == 1 and 4 <= uni:
        ssd = 35000
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif 4 <= un and 2 <= uni <= 3:
        ram = 15500
        ssd = 40000
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)
    elif 2 <= un <= 3 and 4 <= uni:
        ram = 18000 
        ssd = 35000
        sub = (ram * un) + (ssd * uni)
        print("Subtotal productos: $",sub)

codigo = input("Ingrese código de descuento:")
#___________________LISTO_______________________________
#intento 1
if codigo == "uwu-131":
    descuento = round((sub*10)/100)
    if descuento > 100000:
        descuento = 100000
    print(descuento)
    sub = sub - descuento
    print(sub)
else:
    #into 2
    print("Código inválido")
    codigo = input("Ingrese código de descuento:")
    if codigo == "uwu-131":
        descuento = round((sub*10)/100)
        if descuento > 100000:
            descuento = 100000
        print(descuento)
        sub = sub - descuento
        print(sub)
    else:
        #intento 3
        print("Código inválido")
        codigo = input("Ingrese código de descuento:")
        if codigo == "uwu-131":
            descuento = round((sub*10)/100)
            if descuento > 100000:
                descuento = 100000
            print(descuento)
            sub = sub - descuento
            print(sub)
        else:
            print("Descuento: $ 0")
            print(sub)
dom = int(input("Envío a domicilio (1) / Retiro en tienda (2): "))
if dom == 1:
    if sub > 75000:
        print("Costo envío: $ 0")
        print("Total: $", sub)
    else:
        print("Costo envío: $", envio)
        print("Total: $", sub + envio)
else:
    if dom == 2:
        print("Costo envío: $ 0")
        print("Total: $", sub)
