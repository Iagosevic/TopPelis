import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.pelicula import Pelicula

class RespuestaHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()

        peliculas = Pelicula.query().order(Pelicula.titulo)

        valores_plantilla = {
            "peliculas": peliculas
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html",**valores_plantilla))


app = webapp2.WSGIApplication([
    ('/', RespuestaHandler)
], debug=True)
