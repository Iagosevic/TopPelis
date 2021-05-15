import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.puntuacion import Puntuacion
from google.appengine.ext import ndb

class PuntuacionShowallHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()
        tupla = Puntuacion.recupera_para(self.request)
        pelicula = tupla[0]
        puntuaciones = tupla[1]
        media = 0.0
        suma = 0.0
        if puntuaciones.count() > 0:
            for i in puntuaciones:
                suma += i.nota
            media = suma / puntuaciones.count()

        n = Puntuacion.query(ndb.AND
                             (Puntuacion.titulo == tupla[0].key,
                              Puntuacion.login == users.get_current_user().nickname())).get()

        if not n:
            nota_user = -1.0
        else:
            nota_user = n.nota

        valores_plantilla = {
            "usr": usuario,
            "puntuaciones": puntuaciones,
            "pelicula": pelicula,
            "media": "{0:.2f}".format(media),
            "nota_user": nota_user
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("puntuacion_showall.html",**valores_plantilla))

    def post(self):
        #pelicula = Pelicula.recupera(self.request)
        #titulo = self.request.GET["id"]
        #usuario = users.get_current_user()
        tupla = Puntuacion.recupera_para(self.request)
        pelicula = tupla[0].key
        login = users.get_current_user().nickname()
        p = Puntuacion.query(ndb.AND
                             (Puntuacion.titulo == pelicula,
                              Puntuacion.login == login)).get()

        if p:
            p.nota = float(self.request.get("edNota"))
            #puntuacion = Puntuacion(titulo=ndb.Key(urlsafe=titulo), login=login, nota=nota)
            #puntuacion.key.delete()
            p.put()

        else:
            pelicula = self.request.GET["id"]
            nota = float(self.request.get("edNota"))
            puntuacion = Puntuacion(titulo=ndb.Key(urlsafe=pelicula), login=login, nota=nota)
            puntuacion.put()

        return self.redirect("/")
app = webapp2.WSGIApplication([
    ('/puntuacion/showall', PuntuacionShowallHandler)
], debug=True)
