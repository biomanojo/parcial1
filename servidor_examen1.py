from threading import Thread
from socket import socket,error
import funciones
import json
import time


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
                recibido = self.conexion.recv(1024)
                datoC = json.loads(recibido)
                #print datoC

                if datoC[0] == 'admin' and datoC[1] == '123':

                    if datoC[2] == 'a': # Crear Peliculas Administrador
                        resp = funciones.crear_pelicula(pelicula,datoC[3],datoC[4],datoC[5],datoC[6])
                        resp = json.dumps(pelicula)
                        self.conexion.send(resp)

                    if datoC[2] == 'b': # Eliminar Peliculas Admin
                        resp = funciones.Eliminar(pelicula, datoC[3])
                        resp = json.dumps(pelicula)
                        self.conexion.send(resp)

                    if datoC[2] == 'c': # Listar Peliculas Admin
                        resp = funciones.ListarPelAdmin(pelicula)
                        resp = json.dumps(pelicula)
                        self.conexion.send(resp)

                    if datoC[2] == 'd': # Ver Peliculas Vendidas
                        data = funciones.listarp(ventas)
                        resp = json.dumps(pelicula)
                        self.conexion.send(resp)

                    if datoC[2] == 'e': # Sillas Disponibles
                        data = funciones.listarp(ventas)
                        resp = json.dumps(data)

                elif datoC[0] == 'cliente' and datoC[1] == '12345':

                    print datoC
                    if datoC[2] == '1':
                        lispel = funciones.ListarPelAdmin(pelicula)
                        resp = json.dumps(pelicula)
                        self.conexion.send(resp)

                    if datoC[2] == '2':
                        resp = funciones.VentaC(ventas, datoC[3],datoC[4],datoC[5],datoC[6])
                        #print ventas
                        resp=json.dumps(ventas)
                        self.conexion.send(resp)

                    if datoC[2] == '3':
                        resp = funciones.ListarPelCliente(ventas)
                        resp = json.dumps(ventas)
                        self.conexion.send(resp)

            except error:
                print ("[%s] Error de lectura" %self.name)
                break

def main():
    server=socket()
    server.bind(("localhost", 35000))
    server.listen(1)
    while True:
        con,dire=server.accept()
        hilo = Cliente(con,dire)
        hilo.start()

if __name__ == '__main__':
    main()
