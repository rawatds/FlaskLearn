from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.forms import RegistrationFrom, LoginForm
#from blog.models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '0388e119a3e3b3323b1e522ad3e6da99'
# SQLAlchemy related configurations
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db = SQLAlchemy(app)

# To avoid circular depedencies
from blog import routes

