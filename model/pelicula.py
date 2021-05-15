# Peliculas registradas en la aplicacion

from google.appengine.ext import ndb

class Pelicula(ndb.Model):
    titulo = ndb.StringProperty(indexed = True, required = True)
    anho = ndb.IntegerProperty(required = True)
    pais = ndb.StringProperty(required = True)
    director = ndb.StringProperty(required = True)
    resumen = ndb.TextProperty(required = True)
    portada = ndb.BlobProperty(default=None)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    @ndb.transactional
    def update(pelicula):

        return pelicula.put()