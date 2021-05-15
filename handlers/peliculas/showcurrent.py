# coding: utf-8
# Añade una nueva pelicula

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
import model.pelicula
from model.pelicula import Pelicula
from google.appengine.ext import ndb

class ShowcurrentPeliculaHandler(webapp2.RequestHandler):

    def get(self):
        usuario = users.get_current_user()
        pelicula = Pelicula.recupera(self.request)
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("pelicula_showcurrent.html",**valores_plantilla))


app = webapp2.WSGIApplication([
    ('/peliculas/showcurrent', ShowcurrentPeliculaHandler)
], debug=True)