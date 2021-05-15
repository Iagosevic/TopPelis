# coding: utf-8
# Añade una nueva pelicula

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
import model.pelicula
from model.pelicula import Pelicula
from google.appengine.ext import ndb
import time

class EditPeliculaHandler(webapp2.RequestHandler):

    def get(self):
        usuario = users.get_current_user()
        pelicula = Pelicula.recupera(self.request)
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("pelicula_edit.html",**valores_plantilla))

    def post(self):

        titulo = self.request.get("edTitulo", "")
        pelicula = Pelicula.query(Pelicula.titulo == titulo).get()
        pelicula.titulo = self.request.get("edTitulo", "")
        pelicula.anho = int(self.request.get("edAnho", ""))
        pelicula.pais = self.request.get("edPais", "")
        pelicula.director = self.request.get("edDirector")
        pelicula.resumen = self.request.get("edResumen")

        if self.request.get("edPortada") != "":
            image_file = self.request.get("edPortada", None)
            pelicula.portada = image_file


        Pelicula.update(pelicula)
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/peliculas/edit', EditPeliculaHandler)
], debug=True)