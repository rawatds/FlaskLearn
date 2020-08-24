
class Config:
    SECRET_KEY = '0388e119a3e3b3323b1e522ad3e6da99'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '010c05e9d9680c'   # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = '46493b81fe388c'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
