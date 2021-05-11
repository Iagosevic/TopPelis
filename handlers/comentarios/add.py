# coding: utf-8
# Añade un nuevo comentario

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb
from model.comentario import Comentario
from model.pelicula import Pelicula
import time

class ComentarioAddHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        tupla = Comentario.recupera_para(self.request)
        pelicula = tupla[0]
        #comentarios = tupla[1]
        valores_plantilla = {
            "usr" : usuario,
            "pelicula" : pelicula
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("comentarios_add.html",**valores_plantilla))

    def post(self):
        #pelicula = Pelicula.recupera(self.request)
        #titulo = self.request.GET["id"]
        tupla = Comentario.recupera_para(self.request)
        pelicula = tupla[0]
        titulo = pelicula.titulo
        login = users.get_current_user().nickname()
        comentario = self.request.get("edComentario")

        comentario = Comentario(titulo=ndb.Key(urlsafe=titulo), login=login, comentario=comentario)
        comentario.put()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/comentarios/add', ComentarioAddHandler)
], debug=True)