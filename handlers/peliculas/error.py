import webapp2
from webapp2_extras.users import users
from webapp2_extras import jinja2

class ErrorPeliculaHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        valores_plantilla = {
            "usr" : usuario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("Error.html",**valores_plantilla))


app = webapp2.WSGIApplication([
    ('/peliculas/error', ErrorPeliculaHandler)
], debug=True)

