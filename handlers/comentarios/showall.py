# coding: utf-8
# Handler para ver todos los comentarios de una pelicula

#Librerias importadas
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.comentario import Comentario


class ComentariosShowallHandler(webapp2.RequestHandler):
    # Datos que obtenemos del index
    def get(self):
        #Usuario conectado
        usuario = users.get_current_user()
        #Pelicula de la que queremos ver sus comentarios y todos los comentarios de la misma
        tupla = Comentario.recupera_para(self.request)
        pelicula = tupla[0]
        comentarios = tupla[1]

        #Datos que pasamos a la vista de ver comentarios
        valores_plantilla = {
            "usr": usuario,
            "comentarios": comentarios,
            "pelicula": pelicula
        }

        # Instancia de jinja2 para cargar la vista
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("comentarios_showall.html",**valores_plantilla))

#Indicamos el handler
app = webapp2.WSGIApplication([
    ('/comentarios/showall', ComentariosShowallHandler)
], debug=True)
