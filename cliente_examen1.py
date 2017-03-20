# -*- coding: utf-8 -*-
import socket
import funciones
import json

ruta_s= socket.socket()

#coneccion con el servidor
ruta_s.connect(("localhost",35000))

while True:

    peliculas = []

    usuario = raw_input('Ingrese usuario: ')
    peliculas.append(usuario)
    clave = raw_input('Ingrese Clave: ')
    peliculas.append(clave)

    if (usuario == 'admin' and clave == '123'):

        print "Bienvenido al Sistema Administrador\n"

        login = 'true'
        menu = funciones.menu()
        listamenu = funciones.menu_lista(menu)

        opcion = raw_input("Seleccione una opción: ")
        peliculas.append(opcion)

        if opcion == 'a':
            nom=raw_input("Nombre de la pelicula: ")
            peliculas.append(nom)
            cos = raw_input("Costo de la Entrada: ")
            peliculas.append(cos)
            silla = raw_input("Numero de Sillas: ")
            peliculas.append(silla)
            hora = raw_input("Hora Presentación: ")
            peliculas.append(hora)

        if opcion == 'b':
            id = int(input("ID de la pelicula: "))
            peliculas.append(id)
            peliculas.append('')
            peliculas.append('')
            peliculas.append('')

        if opcion == 'c':
            peliculas.append('')
            peliculas.append('')
            peliculas.append('')
            peliculas.append('')

        if opcion == 'd':
            peliculas.append('')
            peliculas.append('')
            peliculas.append('')
            peliculas.append('')

    elif (usuario == 'cliente'  and clave == '123'):

        login = 'true'
        menu = funciones.cliente()
        listamenu = funciones.menu_cliente(menu)
        opcion = raw_input("Seleccione una opción ")
        peliculas.append(opcion)

        if opcion == '1':
            print "lista de Peliculas"
            #datosopt.append(opcion)

        if opcion == '2':
            nombre=raw_input("Nombre de la pelicula: ")
            peliculas.append(nombre)
            cliente = raw_input("Nombre cliente: ")
            peliculas.append(cliente)
            cedula = raw_input("cedula Cliente: ")
            peliculas.append(cedula)
            hora = raw_input("Hora: ")
            peliculas.append(hora)

        if opcion == '3':
            print "Mi pelicula"
    else:
        login=''
        print "Datos Incorrecto"
        break

    cadena_envio = json.dumps(peliculas)
    ruta_s.send(cadena_envio)

    datos = ruta_s.recv(1000)
    resp = json.loads(datos)
    print resp