# -*- coding: iso-8859-1 -*-
import logging
from flask import render_template, session
from flask.ext.security import login_required
from app import app, models, lm


@app.route('/')
@app.route('/index')
def index():
    app.logger.log(logging.WARNING, "lalala esto es warning")
    return "Hello logged"
    
@app.route('/scripts')
def scripts():
    user = {
        'nickname': 'Mauro Cifuentes',
        'lista' : sorted({'nana1', 'nana2', 'nana3', 'nana4'})
    }  
    
    return render_template('scripts.html',
                           title='Hogar, dulce hogar',
                           user=user)
                           
                           
@app.route('/template')
def template():
    user = {
        'nickname': 'Mauro Cifuentes',
        'lista' : sorted({'nana1', 'nana2', 'nana3', 'nana4'})
    }  
    
    return render_template('index.html',
                           title='Hogar, dulce hogar',
                           user=user)
                           
                  
@lm.request_loader
def load_user(request):
    token = None
    if 'token' in session:
        token = session['token']
    
    if token is None:
        token = request.args.get('token')
 
    if token is not None:
        username,password = token.split(":") # naive token
        alumno = models.User.query.filter_by(NRODOC=username).first()  # @UndefinedVariable
        if (alumno is not None):
            if (alumno.CLAVE == password):
                session['token'] = token
                return alumno
    return None
                  
                  
@app.route('/login', methods=['GET', 'POST'])
def login():
    session['loggued'] = True
    return 'log in' 
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('token', None)
    return 'log out'
    

                
                           
@app.route('/db')
def db():
    # ejemplos de querys que puedo realizar        
    # http://packages.python.org/Flask-SQLAlchemy/index.html  
    alumno = models.User.query.get(1)  # @UndefinedVariable
    u = {
        'nickname': alumno.NOMBRE +" "+ alumno.APELLIDO,
        'lista' : sorted({'nana1', 'nana2', 'nana3', 'nana4'})
    }     
    
    return render_template('index.html',
                           title=alumno.NOMBRE,
                           user=u)                   
                           
                           
@app.route('/protected')
@login_required
def protected():
    return "ni lo sueñes"                       
