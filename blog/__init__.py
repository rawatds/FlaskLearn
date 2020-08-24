from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# from blog.models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '0388e119a3e3b3323b1e522ad3e6da99'
# SQLAlchemy related configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Email
# app.config['MAIL_SERVER'] = 'smtp.office365.com'  # 'localhost' # smtp.gmail.com'
# app.config['MAIL_PORT'] = 587 # 25        # 465
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'dharmender.rawat@jktech.com'
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PW')
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '010c05e9d9680c'
app.config['MAIL_PASSWORD'] = '46493b81fe388c'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)


db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users_bp.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'To URL you are trying to access needs login first. Please login'
# To avoid circular depedencies

from blog.users.routes import users_bp
from blog.posts.routes import posts_bp
from blog.main.routes import main_bp

app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(main_bp)

from blog.users.forms import RegistrationForm, LoginForm
