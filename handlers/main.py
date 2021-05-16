# coding: utf-8
# Muestra todas las peliculas del sistema

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.pelicula import Pelicula

class MainHandler(webapp2.RequestHandler):
    #Datos que obtenemos
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Si hay un usuario conectado le mostramos la opcion de desconectarse
        if usuario:
            url_usuario = users.create_logout_url("/")
        #Si no hay un usuario conectado le mostramos la opcion de conectarse
        else:
            url_usuario = users.create_login_url("/")

        #Buscamos las peliculas
        peliculas = Pelicula.query().order(Pelicula.titulo)

        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr": usuario,
            "url_usr": url_usuario,
            "peliculas": peliculas
        }

        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html",**valores_plantilla))

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
