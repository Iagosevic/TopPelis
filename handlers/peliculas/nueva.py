# coding: utf-8
# Añade una nueva pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users
import time

class NuevaPeliculaHandler(webapp2.RequestHandler):
    #Datos que obtenemos
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr" : usuario
        }

        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_pelicula.html",**valores_plantilla))

    #Datos que obtenemos del form para añadir pelicula
    def post(self):
        #Almacena la portada
        image_file = None
        if self.request.get("edPortada") != "":
            #Guardamos la imagen
            image_file = self.request.get("edPortada", None)
        #Almacena el resto de datos
        titulo = self.request.get("edTitulo", "")
        anho = int(self.request.get("edAnho", ""))
        pais = self.request.get("edPais", "")
        director = self.request.get("edDirector")
        resumen = self.request.get("edResumen")

        #Crea una pelicula con los datos introducidos para almacenarla en el Datastore
        pelicula = Pelicula(titulo=titulo, anho=anho, pais=pais, director=director, resumen=resumen, portada=image_file)
        #Añade la pelicula
        pelicula.put()
        #Esperamos 1 segundo para que sincronice la insercion
        time.sleep(1)
        #Nos redirecciona al index
        return self.redirect("/")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/nueva', NuevaPeliculaHandler)
], debug=True)