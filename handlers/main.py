import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.pelicula import Pelicula

class MainHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        if usuario:
            url_usuario = users.create_logout_url("/")
        else:
            url_usuario = users.create_login_url("/")

        peliculas = Pelicula.query().order(Pelicula.titulo)

        valores_plantilla = {
            "usr": usuario,
            "url_usr": url_usuario,
            "peliculas": peliculas
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html",**valores_plantilla))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
