# coding: utf-8
# Añade una nueva pelicula

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import images
from webapp2_extras import jinja2
from model.pelicula import Pelicula
from webapp2_extras.users import users
import time

class NuevaPeliculaHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        valores_plantilla = {
            "usr" : usuario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_pelicula.html",**valores_plantilla))

    def post(self):

        image_file = None
        if self.request.get("edPortada") != "":
            # Store the added image
            image_file = self.request.get("edPortada", None)

        titulo = self.request.get("edTitulo", "")
        anho = int(self.request.get("edAnho", ""))
        pais = self.request.get("edPais", "")
        director = self.request.get("edDirector")
        resumen = self.request.get("edResumen")


        pelicula = Pelicula(titulo=titulo, anho=anho, pais=pais, director=director, resumen=resumen, portada=image_file)
        pelicula.put()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/peliculas/nueva', NuevaPeliculaHandler)
], debug=True)