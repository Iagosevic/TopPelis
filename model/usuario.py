#Usuarios que usan la aplicacion

from google.appengine.ext import ndb

class Usuario(ndb.Model):
    login = ndb.StringProperty(indexed = True);
    password = ndb.StringProperty(required = True);
    nombre = ndb.StringProperty(required = True);
    apellidos = ndb.StringProperty(required = True);
    fecha_nac = ndb.DateProperty(required = True);

