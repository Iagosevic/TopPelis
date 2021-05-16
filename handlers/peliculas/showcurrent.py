# coding: utf-8
# Muestra los datos de una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.pelicula import Pelicula

class ShowcurrentPeliculaHandler(webapp2.RequestHandler):
    #Datos que obtenemos del index
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Pelicula a mostrar
        pelicula = Pelicula.recupera(self.request)
        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }

        #Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("pelicula_showcurrent.html",**valores_plantilla))

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/showcurrent', ShowcurrentPeliculaHandler)
], debug=True)