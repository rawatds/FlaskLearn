from flask import Flask
from blog.models import User, Post
from blog import db
import pymysql

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///siteqa.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@localhost/blog'
db.init_app(app)
app.app_context().push()

db.create_all()     # Create all blank tables
user1 = User(username = 'dsrawat', email = 'dsrawat@gmail.com', password = 'password')
db.session.add(user1)
db.session.commit()

User.query.all()


