# coding: utf-8
# Elimina una pelicula

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users
import time

class EliminarPeliculaHandler(webapp2.RequestHandler):

    def get(self):
        usuario = users.get_current_user()
        pelicula = Pelicula.recupera(self.request)
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("delete_pelicula.html", **valores_plantilla))

    def post(self):
        pelicula = Pelicula.recupera(self.request)
        pelicula.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/peliculas/eliminar', EliminarPeliculaHandler)
], debug=True)