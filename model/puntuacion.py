# coding: utf-8
# Puntuacion de un usuario sobre una pelicula

#Librerias importadas
from google.appengine.ext import ndb
from pelicula import Pelicula

#Clase puntuacion
class Puntuacion(ndb.Model):
    # Titulo de la pelicula
    titulo = ndb.KeyProperty(kind = Pelicula)
    # Usuario que realiza la puntuacion
    login = ndb.StringProperty(required=True)
    #Nota de la pelicula
    nota = ndb.FloatProperty(required=True)

    # Metodo para recuperar la key de la pelicula desde una url
    @staticmethod
    def recupera_para(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        if id:
            titulo = ndb.Key(urlsafe=id)
            puntuaciones = Puntuacion.query(Puntuacion.titulo == titulo)
            return titulo.get(), puntuaciones
        else:
            print("ERROR: no se ha encontrado esa pelicula")
