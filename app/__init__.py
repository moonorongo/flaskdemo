# -*- coding: iso-8859-1 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import basedir

import logging
from logging import Formatter 
from logging.handlers import RotatingFileHandler



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

file_handler = RotatingFileHandler('log.error', mode='a', maxBytes=0, backupCount=0, encoding="ISO_8859_1", delay=0)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(file_handler)

# aqui para evitar referencias circulares...
from app import views, models