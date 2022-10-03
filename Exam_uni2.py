

def estudiantes():
    archivo=open('Estudiantes.txt','r')
    cadena=archivo.read()
    lista=cadena.split('\n')
    archivo.close()
    con=set()
    for ctrl in lista:
        tupla=(ctrl[:8],ctrl[8:])
        con.add(tupla)
    return con
print(estudiantes())



def Kardex():
    archivo = open('Kardex.txt', 'r')
    cadena = archivo.read()
    archivo.close()
    lista = cadena.split("\n")
    con=set()
    for kar in lista:
        lista9=kar.split('|')
        tupla=(lista9[0],lista9[1],lista9[2])
        con.add(tupla)
    return con

print(Kardex())


def materias_alum(nctrl):
    estudiante = estudiantes()
    materias = Kardex()
    list = []
    ban = True
    for i in nctrl:
        for est in estudiante:
            dir = {}
            if i == int(est[0]):
                ban = False
                dir["Nombre"] = est[1]
                Materias = []
                for mat in materias:
                    if i == int(mat[0]):
                        Materias.append(mat[1])
                dir["Materias"] = Materias
                list.append(dir)
    if ban:
        for est in estudiante:
            dir = {}
            dir["Nombre"] = est[1]
            Materias = []
            for mat in materias:
                if int(est[0]) == int(mat[0]):
                    Materias.append(mat[1])
            dir["Materias"] = Materias
            list.append(dir)
    return list

try:
    datos=materias_alum([18420495,18420485])
except Exception as error:
    print("ERROR: ", error)
else:
    print(datos)


