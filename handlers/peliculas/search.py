# coding: utf-8
# Busca una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users

class SearchPeliculaHandler(webapp2.RequestHandler):
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
        self.response.write(jinja.render_template("pelicula_search.html",**valores_plantilla))

    #Datos que obtenemos del form para buscar
    def post(self):
        #Titulo de la pelicula a buscar
        titulo = self.request.get("edTitulo", "")
        #Buscamos la pelicula en el Datastore
        pelicula = Pelicula.query(Pelicula.titulo == titulo).get()
        #Usuario conectado
        usuario = users.get_current_user()

        #Datos que pasamos a la vista
        valores_plantilla = {
            "usr": usuario,
            "pelicula": pelicula
        }
        #Si encuentra la pelicula
        if pelicula:
            #Nos envia al showcurrent de la pelicula buscada
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("pelicula_showcurrent.html", **valores_plantilla))
        #Si no la encuentra
        else:
            #Nos muestra el error
            return self.redirect("error")

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/peliculas/search', SearchPeliculaHandler)
], debug=True)