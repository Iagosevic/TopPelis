# coding: utf-8
# Busca una pelicula

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import images
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users
import time

class SearchPeliculaHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        valores_plantilla = {
            "usr" : usuario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("pelicula_search.html",**valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        # pelicula = titulo.get()
        pelicula = Pelicula.query(Pelicula.titulo == titulo).get()
        usuario = users.get_current_user()

        valores_plantilla = {
            "usr": usuario,
            "pelicula": pelicula
        }
        if pelicula:
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("pelicula_showcurrent.html", **valores_plantilla))
        else:
            return self.redirect("error")



app = webapp2.WSGIApplication([
    ('/peliculas/search', SearchPeliculaHandler)
], debug=True)