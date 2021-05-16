# coding: utf-8
# Handler para editar una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.pelicula import Pelicula
import time

class EditPeliculaHandler(webapp2.RequestHandler):
    #Datos que obtenemos del index
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Pelicula que queremos editar
        pelicula = Pelicula.recupera(self.request)

        #Datos que le pasamos a la vista de editar pelicula
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }

        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("pelicula_edit.html",**valores_plantilla))

    #Datos que obtenemos del form para editar pelicula
    def post(self):
        #Titulo de la pelicula
        titulo = self.request.get("edTitulo", "")
        #Creamos la pelicula a partir de su titulo buscandola en el Datastore
        pelicula = Pelicula.query(Pelicula.titulo == titulo).get()

        #Modificamos los respectivos campos
        pelicula.titulo = self.request.get("edTitulo", "")
        pelicula.anho = int(self.request.get("edAnho", ""))
        pelicula.pais = self.request.get("edPais", "")
        pelicula.director = self.request.get("edDirector")
        pelicula.resumen = self.request.get("edResumen")
        if self.request.get("edPortada") != "":
            image_file = self.request.get("edPortada", None)
            pelicula.portada = image_file

        #Actulizamos la pelicula
        Pelicula.update(pelicula)
        #Esperamos 1 segundo para que se realice la actualizacion
        time.sleep(1)
        #Nos redirecciona al index
        return self.redirect("/")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/edit', EditPeliculaHandler)
], debug=True)