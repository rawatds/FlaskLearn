from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from blog.models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '0388e119a3e3b3323b1e522ad3e6da99'
# SQLAlchemy related configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'To URL you are trying to access needs login first. Please login'
# To avoid circular depedencies

from blog import routes
from blog.forms import RegistrationForm, LoginForm
