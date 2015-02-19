# -*- coding: iso-8859-1 -*-
from app import db


class User(db.Model):
    __tablename__ = 'alumnos' # TIENE QUE ESTAR EN LOWERCASE!!! increible...
    CODIGO = db.Column('CODIGO', db.Integer, primary_key=True)
    NOMBRE = db.Column('NOMBRE', db.String(150))
    APELLIDO = db.Column('APELLIDO', db.String(100))
    EMAIL = db.Column('EMAIL', db.String(100))
    NRODOC = db.Column('NRODOC', db.String(15))
    CLAVE = db.Column('CLAVE', db.String(15))
    avisos = db.relationship('AvisosAlumnos', backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.CODIGO)  # python 3
            
    def __repr__(self):
        return '<Alumno %r>' % (self.NOMBRE)

# ejemplos de querys que puedo realizar        
# http://packages.python.org/Flask-SQLAlchemy/index.html        
        
        
class AvisosAlumnos(db.Model):
    __tablename__ = 'avisosalumnos'
    CODIGO = db.Column('CODIGO', db.Integer, primary_key = True)
    FECHAALTA = db.Column('FECHAALTA', db.DateTime)
    TEXTO = db.Column('TEXTO', db.LargeBinary)
    CODALUMNO = db.Column('CODALUMNO', db.Integer, db.ForeignKey('alumnos.CODIGO'))

    def __repr__(self):
        return '<AvisoAlumno %r>' % (self.TEXTO)