# Comentarios hechos por usuarios en una pelicula

from google.appengine.ext import ndb
from pelicula import Pelicula
from usuario import Usuario

class Comentario(ndb.Model):

    titulo = ndb.KeyProperty(kind = Pelicula)
    login = ndb.StringProperty(required=True)
    comentario = ndb.StringProperty(required=True)


    @staticmethod
    def recupera_para(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        if id:
            titulo = ndb.Key(urlsafe=id)
            #pelicula = Pelicula.query(Pelicula.titulo == titulo)
            comentarios = Comentario.query(Comentario.titulo == titulo)
            return titulo.get(), comentarios
        else:
            print("ERROR: no se ha encontrado esa pelicula")
