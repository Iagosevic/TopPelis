# coding: utf-8
# Elimina una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users
import time

class EliminarPeliculaHandler(webapp2.RequestHandler):
    #Datos que obtenemos del index
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Pelicula a borrar
        pelicula = Pelicula.recupera(self.request)

        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }
        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("delete_pelicula.html", **valores_plantilla))

    # Datos que obtenemos del form para eliminar pelicula
    def post(self):
        #Pelicula que queremos eliminar
        pelicula = Pelicula.recupera(self.request)
        #Eliminamos la pelicula
        pelicula.key.delete()
        #Esperamos 1 segundo para que sincronice el borrado
        time.sleep(1)
        #Nos redirecciona al index
        return self.redirect("/")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/eliminar', EliminarPeliculaHandler)
], debug=True)