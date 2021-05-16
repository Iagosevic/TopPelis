# coding: utf-8
# Peliculas registradas en la aplicacion

#Librerias importadas
from google.appengine.ext import ndb

#Clase pelicula
class Pelicula(ndb.Model):
    #Titulo de la pelicula
    titulo = ndb.StringProperty(indexed = True, required = True)
    #Año de estreno
    anho = ndb.IntegerProperty(required = True)
    #Nacionalidad de la pelicula
    pais = ndb.StringProperty(required = True)
    #Director de la pelicula
    director = ndb.StringProperty(required = True)
    #Breve resumen de la pelicula
    resumen = ndb.TextProperty(required = True)
    #Portada de la pelicula
    portada = ndb.BlobProperty(default=None)

    # Metodo para recuperar la key de la pelicula desde una url
    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    # Metodo para actualizar una pelicula
    @ndb.transactional
    def update(pelicula):

        return pelicula.put()