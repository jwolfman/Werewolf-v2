from flask import Flask;
from routes import *;
from classes import *;
from templated import *;

app = Flask(__name__)
wsgi_app = app.wsgi_app
