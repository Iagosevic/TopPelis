import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.comentario import Comentario
from google.appengine.ext import ndb

class ComentariosShowallHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        tupla = Comentario.recupera_para(self.request)
        pelicula = tupla[0]
        comentarios = tupla[1]

        valores_plantilla = {
            "usr": usuario,
            "comentarios": comentarios,
            "pelicula": pelicula
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("comentarios_showall.html",**valores_plantilla))


app = webapp2.WSGIApplication([
    ('/comentarios/showall', ComentariosShowallHandler)
], debug=True)
