from flask import Flask
#asdasdas
app = Flask(__name__, template_folder='templates', static_folder='static')
from app import admin
