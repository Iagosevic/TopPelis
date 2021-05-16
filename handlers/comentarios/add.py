# coding: utf-8
# Handler para añadir un nuevo comentario

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb
from model.comentario import Comentario

class ComentarioAddHandler(webapp2.RequestHandler):
    #Datos que obtenemos desde el showall
    def get(self):
        #Usuario conectado actualmente
        usuario = users.get_current_user()
        #Recuperamos la pelicula en la que vamos a añadir el comentario
        tupla = Comentario.recupera_para(self.request)
        pelicula = tupla[0]
        #Datos que pasamos a la vista de añadir comentario
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }
        #Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("comentarios_add.html",**valores_plantilla))

    #Datos que obtemos del form para añdir comentario
    def post(self):
        #Key de la pelicula
        titulo = self.request.GET["id"]
        #Usuario conectado
        login = users.get_current_user().nickname()
        #Comentario que ha introducido en el form
        comentario = self.request.get("edComentario")

        #Creamos el comentario para añadirlo al Datastore
        comentario = Comentario(titulo=ndb.Key(urlsafe=titulo), login=login, comentario=comentario)
        #Añadimos el comentario
        comentario.put()

        #Nos redirecciona al index
        return self.redirect("/")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/comentarios/add', ComentarioAddHandler)
], debug=True)