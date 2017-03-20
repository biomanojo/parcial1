from socket import socket,error
from threading import Thread
import time
import funciones_servidor
import json

pelicula = list()
ventas = list()

class Cliente(Thread):
    '''funcion que genera hilos'''
    def __init__(self,conexion,direccion):
        Thread.__init__(self)
        self.conexion=conexion
        self.direccion=direccion

    def run(self):
        while True:
            try:
                usuario='admin'
                clave='1234'
                mensaje_c=self.conexion.recv(1024)

                mensaje_c2 = self.conexion.recv(1024)

                #opcion = self.conexion.recv(1024)
                if usuario == mensaje_c  and clave ==mensaje_c2:
                    print "bienvedidos"
                   # mensaje = 'bienvenidos'
                    #ruta_c.send(mensaje)
                    mensaje = "BIENVENIDOS TE DICE EL SERVIDOR  "
                    self.conexion.send(mensaje)

                    #break
                    opcion = self.conexion.recv(1024)
                    respu = json.dumps(opcion)
                    print respu
                    if opcion == 1 :
                        mensaje1 = "ESCOJA UNA OPCION  "
                        elf.conexion.send(mensaje1)
                        crear = funciones_servidor.crearpeli(nombre, costo, silla, hora)
                        resp = json.dumps(crear)
                        self.conexion.send(resp)
                        #print resp

                    if opcion == 2:
                        mensaje2 = "ESCOJA UNA OPCION  "
                        self.conexion.send(mensaje2)
                    #crear = funciones_servidor.crearpeli(nombre,costo,silla,hora)
                        #crear1=json.dumps(pelicula1)
                    #self.conexion.send(crear)
                #elif opcion==2:
                 #   listar = funciones_servidor.lista(pelicula1)
                #    self.conexion.send(listar)
                #else:
                # print " incorrecto"
                   # mensaje2 = "INCORRECTO  "
                    #self.conexion.send(mensaje2)



                #else:
                    #print " incorrectos."
                    #mensaje2= " incorrectos."
                    #self.conexion.send(mensaje2)


                #if mensaje_c and mensaje_c2  == 'salir':
                    #self.conexion.close()
                   # tiempo1=time.strftime("%c")
                    #print tiempo1
            except error:
                print ("[%s] Error de lectura" %self.name)
                break
            #else:
                #if mensaje_c and mensaje_c2  != 'salir':
                    #if mensaje_c and mensaje_c2:
                    #print " BIENVENIDOS"
                   # mensaje= "BIENVENIDOS"
                   # self.conexion.send(mensaje)
                #else:
                    #mensaje2= "INCORRECTO"
                    #.conexion.send(mensaje2)
                        #self.conexion.send(mensaje_c2)


def main():
    server=socket()
    server.bind(("", 35000))
    server.listen(1)
    while True:
        con,dire=server.accept()
        hilo = Cliente(con,dire)
        hilo.start()
        #tiempo1 = time.strftime("%c")
       # tf=hilo.run()
        #print tf
        print ("Conexion de %s:%d  " %dire)

if __name__ == '__main__':
    main()
