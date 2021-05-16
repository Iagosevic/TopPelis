# coding: utf-8
# Comentarios hechos por usuarios en una pelicula

#Librerias importadas
from google.appengine.ext import ndb
from pelicula import Pelicula

#Clase comentario
class Comentario(ndb.Model):
    #Titulo de la pelicula
    titulo = ndb.KeyProperty(kind = Pelicula)
    #Usuario que realiza el comentario
    login = ndb.StringProperty(required=True)
    #Comentario sobre la pelicula
    comentario = ndb.StringProperty(required=True)
    #Fecha en la que se introduce el comentario
    fecha_comentario = ndb.DateProperty(auto_now_add = True)
    #Hora en la que se introduce el comentario
    hora_comentario = ndb.TimeProperty(auto_now_add=True)

    #Metodo para recuperar la key de la pelicula desde una url
    @staticmethod
    def recupera_para(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        if id:
            titulo = ndb.Key(urlsafe=id)
            comentarios = Comentario.query(Comentario.titulo == titulo)
            return titulo.get(), comentarios
        else:
            print("ERROR: no se ha encontrado esa pelicula")
