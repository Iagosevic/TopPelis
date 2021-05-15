#Puntuacion que un usuario da a una pelicula

from google.appengine.ext import ndb
from pelicula import Pelicula

class Puntuacion(ndb.Model):

    titulo = ndb.KeyProperty(kind = Pelicula)
    login = ndb.StringProperty(required=True)
    nota = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_para(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        if id:
            titulo = ndb.Key(urlsafe=id)
            #pelicula = Pelicula.query(Pelicula.titulo == titulo)
            puntuaciones = Puntuacion.query(Puntuacion.titulo == titulo)
            return titulo.get(), puntuaciones
        else:
            print("ERROR: no se ha encontrado esa pelicula")
