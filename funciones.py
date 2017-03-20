import json

def usuarios():
    lista=['admin','cliente']
    cadena=json.dumps(lista)
    return cadena

def menu():
    lista = ["1 crear pelicula", "2 eliminar pelicuma", "3 listar peliculas", "4 ver peliculas", "6 silla disponible"]
    cadena = json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def cliente():
    lista = ['1. Listar Peliculas', '2. Comprar Entrada', '3. Ver Mi Pelicula']
    cadena = json.dumps(lista)
    return cadena

def menu_cliente(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def crear_pelicula(pelicula,nombre,costo,silla,hora):

    pelicrea = [nombre,costo,silla,hora]
    pelicula.append(pelicrea)
    return pelicula

def Eliminar(pelicula,idpel):
    #idpel = (id)
    #print idpel
    #if idpel in pelicula:
    #    pelicula.pop(idpel)
    #    return pelicula
    #else:
    #    return "El id no se encuentra"
    pelicula.pop(idpel)
    return pelicula

def ListarPelAdmin(pelicula):
    for pelis in pelicula:
        print (pelis)
    #return pelis

def VentaC(venta,nombre,cliente,cedula,hora):

    Vender=[nombre,cliente,cedula,hora]
    venta.append(Vender)
    return venta

# Cliente
def ListarPelCliente(pelicula):
    for pelis in pelicula:
        print (pelis)
    #return pelis