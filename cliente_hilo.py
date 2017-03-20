#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import socket
import funciones_servidor
import json
def main():
    ruta_s= socket()
    #coneccion con el servidor
    ruta_s.connect(("localhost",35000))
    while True:
        peliculas=[]
        mensaje_c = raw_input('usuario')
        ruta_s.send(mensaje_c)
        mensaje_c2 = raw_input('clave')
        ruta_s.send(mensaje_c2)

        mensaje_s = ruta_s.recv(1024)
        #mensaje_s1 = json.loads(mensaje_s)
        print mensaje_s



        if  mensaje_c== "admin" and mensaje_c2  =="1234" :

            menu=funciones_servidor.menu()
            menu1=funciones_servidor.menu_lista(menu)
            print menu1


            opcion = int(raw_input("Ingrese Una Opcion : "))
            peliculas.append(opcion)
            #ruta_s.send(str(opcion))

            if opcion == 1:
                #if opcion == 1:
                nombre = raw_input("nombre pelicula : ")
                peliculas.append(nombre)
                #ruta_s.send(nombre)
                costo = raw_input("nombre costo : ")
                peliculas.append(costo)
                #ruta_s.send(str(costo))
                silla = raw_input("nombre silla : ")
                peliculas.append(silla)
                #ruta_s.send(str(silla))
                hora = raw_input("nombre hora : ")
                peliculas.append(hora)
                #ruta_s.send(str(hora))

                resp = ruta_s.recv(1024)
                mensaje_s1 = json.loads(resp)
                print mensaje_s1
               # crear = funciones_servidor.crearpeli(nombre, costo, silla, hora)
                #resp = json.dumps(crear)
                #print resp

                #menu = funciones_servidor.menu()
                #menu1 = funciones_servidor.menu_lista(menu)
                #print menu1
                opcion = int(raw_input("Ingrese Una Opcion : "))
                peliculas.append(opcion)

            elif opcion == 2:
                #crear = funciones_servidor.crearpeli(nombre, costo, silla, hora)
                mostrar = funciones_servidor.listar(pelicula1)
                print mostrar

        #cadena_envio = json.dumps(peliculas)
        #ruta_s.send(cadena_envio)

        #elif opcion==2:
         #   listar = ruta_s.recv(1024)
         #   print listar
       # else:
          #  print" incorrecto"

        #opcion = raw_input("Ingrese Una Opcion : ")
       # ruta_s.send(opcion)

        #if mensaje_c and mensaje_c2:
            #try:
                #ruta_s.send(mensaje_c)
                #ruta_s.send(mensaje_c2)
           # except  TypeError:
                #ruta_s.send(bytes(mensaje_c,"utf-8"))
                #ruta_s.send(bytes(mensaje_c2, "utf-8"))
        #menu = ruta_s.recv(1024)


        #crear = ruta_s.recv(1024)

        #if mensaje_s and crear:


        #print menu
        #print crear
            #print crear
        #break

if __name__ == '__main__':
    main()


