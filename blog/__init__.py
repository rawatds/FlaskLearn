from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config
import pymysql
# from blog.models import User, Post

mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

login_manager.login_view = 'users_bp.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'To URL you are trying to access needs login first. Please login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from blog.users.routes import users_bp
    from blog.posts.routes import posts_bp
    from blog.main.routes import main_bp
    from blog.errors.handlers import errors_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)

    return app


# To avoid circular depedencies
from blog.users.forms import RegistrationForm, LoginForm
