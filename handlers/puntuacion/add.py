# coding: utf-8
# Añade una nota

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb
from model.puntuacion import Puntuacion
from model.pelicula import Pelicula
import time

class PuntuacionAddHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        tupla = Puntuacion.recupera_para(self.request)
        pelicula = tupla[0]
        puntuaciones = tupla[1]


        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("puntuacion_add.html",**valores_plantilla))

    def post(self):
        titulo = self.request.GET["id"]
        login = users.get_current_user().nickname()
        nota = self.request.get("edNota")

        puntuacion = Puntuacion(titulo=ndb.Key(urlsafe=titulo), login=login, nota=nota)
        puntuacion.put()

        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/puntuacion/add', PuntuacionAddHandler)
], debug=True)