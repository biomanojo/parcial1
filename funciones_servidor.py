import json

def menu():
    lista=["1 crear pelicula","2 eliminar pelicuma", "3 listar peliculas","4 ver peliculas","6 silla disponible"]
    cadena = json.dumps(lista)
    return cadena


def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i


def crearpeli(nombre,costo,silla,hora):
    pelicula1 = []
    pelicula = [nombre,costo,silla,hora]
    pelicula1.append(pelicula)
    return pelicula1

def listar(pelicula1):
    for peli in pelicula1:
        print peli

def multi(n1,n2):
    resp=int(n1)*int(n2)
    return str(resp)

def div(n1,n2):
    resp=float(n1)/float(n2)
    return str(resp)