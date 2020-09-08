from blog.models import User, Post, db
import datetime #pytz
from dateutil.tz import tzlocal

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


db.drop_all()
db.create_all()

#Post.query.delete()
#db.session.commit()

print(User.query.all())
print(Post.query.all())
