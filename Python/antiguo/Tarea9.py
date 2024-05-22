def obtener_postulantes(carreras, postulantes):
    l = {}
    for nombre,codigo,genero in postulantes:
        if codigo not in l:
            l[codigo] = []
        l[codigo].append((nombre, genero))
    n = {}
    for cd, carrera in carreras:
        for codigo in l:
            if codigo == cd and carrera not in n:
                n[carrera] = []
                for nombre, genero in l[codigo]:
                    n[carrera].append((nombre,genero))
    return n

carreras = [
 ('INF','Ing. Civil en Informática'), ('ICO','Ing. Comercial'),
 ('IND','Ing. Civil Industrial'), ('QUI','Ing. Civil Química'),
 ('MAT','Ing. Civil Matemática'), ('IDP','Ing. en Diseño de Productos'),
 ('CON', 'Construcción Civil'), ('MEC','Ing. Civil Mecánica')
]
postulantes = [
 ("Ivonne Navia", 'ICO', 'F'), ("Gary Meza", 'IND', 'M'),
 ("Carlos Reyes", 'IND', 'M'), ("Cecilia Castro", 'INF', 'F'),
 ('Eduardo Villarroel', 'INF', 'M'), ("Ana Meza", 'ICO', 'F'),
 ('Claudia Sánchez', 'CON', 'F'), ("Sofía Arenas", 'INF', 'F'),
 ('Celso Vásquez', 'IND','M'), ("Natalia Ozerova", 'MAT', 'F'),
 ('Paula Soto', 'ICO','F'), ("Andrea Brereton",'MAT','F')
]


print("Postulacion por carreras(sin ningun orden particular):")
carrera = obtener_postulantes(carreras,postulantes)
mujeres = {}
for nombre in carrera:
    print("Carrera:", nombre)
    for estudiante, genero in carrera[nombre]:
        print("\t",estudiante)
        if genero == "F":
            if nombre not in mujeres:
                mujeres[nombre] = 0
            mujeres[nombre] += 1
print("Las 3 carreras con más postulantes mujeres (de mayor a menor):") #ENTER + SHIFT PARA VERIFICAR SI FUNCIONA ESA LINEA
l = []
for nombre in mujeres:
    l.append((mujeres[nombre], nombre))
    l.sort()
    l.reverse()
#muchos for 
aux = 0
for x, y in l:
    if aux < 3:
        print("\t",y)
        aux += 1