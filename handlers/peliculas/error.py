# coding: utf-8
# Handler que gestiona el mensaje de error en caso de no encontrar la pelicula

#Librerias importadas
import webapp2
from webapp2_extras.users import users
from webapp2_extras import jinja2

class ErrorPeliculaHandler(webapp2.RequestHandler):
    #Datos que obtenemos
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr" : usuario
        }

        #Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("Error.html",**valores_plantilla))

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/error', ErrorPeliculaHandler)
], debug=True)

