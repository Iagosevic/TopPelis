# coding: utf-8
# Muestra las puntuaciones de una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.puntuacion import Puntuacion
from google.appengine.ext import ndb

class PuntuacionShowallHandler(webapp2.RequestHandler):
    #Datos que obtenemos del index
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Pelicula y puntuaciones de dicha pelicula
        tupla = Puntuacion.recupera_para(self.request)
        pelicula = tupla[0]
        puntuaciones = tupla[1]

        #Variables para calcular la media
        media = 0.0
        suma = 0.0
        #Calcula la media
        if puntuaciones.count() > 0:
            for i in puntuaciones:
                suma += i.nota
            media = suma / puntuaciones.count()

        #Busca si el usuario ya ha comentado esa pelicula
        n = Puntuacion.query(ndb.AND
                             (Puntuacion.titulo == tupla[0].key,
                              Puntuacion.login == users.get_current_user().nickname())).get()
        #Si no ha puntuado la pelicula le asigna un -1
        if not n:
            nota_user = -1.0
        #Si la ha puntuado le asigna la nota que corresponda
        else:
            nota_user = n.nota

        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr": usuario,
            "puntuaciones": puntuaciones,
            "pelicula": pelicula,
            "media": "{0:.2f}".format(media),
            "nota_user": nota_user
        }
        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("puntuacion_showall.html",**valores_plantilla))

    #Datos que obtenemos del form para añadir nota
    def post(self):
        #Key de la pelicula a puntuar
        tupla = Puntuacion.recupera_para(self.request)
        pelicula = tupla[0].key
        #Usuario conectado
        login = users.get_current_user().nickname()
        #Buscamos si el usuario ha puntuado o no esa pelicula
        p = Puntuacion.query(ndb.AND
                             (Puntuacion.titulo == pelicula,
                              Puntuacion.login == login)).get()
        #Si la ha puntuado
        if p:
            #Recoge la nota
            p.nota = float(self.request.get("edNota"))
            #La actualiza
            p.put()
        #Si no la ha puntuado
        else:
            #Key de la pelicula a puntuar
            pelicula = self.request.GET["id"]
            #Nota que le asigna
            nota = float(self.request.get("edNota"))
            #Creamos la puntuacion para añadirla al Datastore
            puntuacion = Puntuacion(titulo=ndb.Key(urlsafe=pelicula), login=login, nota=nota)
            #Añade la nota
            puntuacion.put()
        #Nos redirecciona al index
        return self.redirect("/")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/puntuacion/showall', PuntuacionShowallHandler)
], debug=True)
