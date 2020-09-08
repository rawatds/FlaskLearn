from blog import create_app
from blog import db
#from blog.config import ConfigQA

#app = create_app(config_class=ConfigQA)
app = create_app()
app.app_context().push()

#db.create_all()         # Create blank db, and all tables. - just run once

if __name__ == '__main__':
    app.run('localhost',  3500, debug=True)
