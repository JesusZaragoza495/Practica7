'''
Tema: Autenticar Usuario con bcrypt
Fecha: 08 de septiembre del 2022
Autor: Jesus Zaragoza Anaya.
'''

from practica7 import *
import bcrypt

def autenticar_usuario(usuario, contrasena):
    registro = generar_contraseña_usu()
    estudiante = estudiantes()
    autenticacion = {}
    for x in registro:
        if x[0] == usuario:
            for estudi in estudiante:
                if estudi[0]==usuario:
                    bandera = bcrypt.checkpw(contrasena.encode('utf-8'), x[2].encode('utf-8'))
                    autenticacion["Bandera"] = bandera
                    autenticacion["Usuario..."] = estudi[1]
                    if bandera:
                        autenticacion["Mensaje"] = "Autenticación de usuarios..."
                    else:
                        autenticacion["Mensaje"] = "Contraseña incorrecta..."
                    return autenticacion
    autenticacion["Bandera"] = False
    autenticacion["Usuario"] = ""
    autenticacion["Mensaje"] = "No existe el Usuario..."
    return autenticacion

print(autenticar_usuario("18420495","2ZIDF3xLJI"))
