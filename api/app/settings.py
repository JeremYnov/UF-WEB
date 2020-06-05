class Config:
    DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/uf_web"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'latartefrancaise@gmail.com'
    MAIL_PASSWORD = '4XaE1X1j0J9maXXlcf'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
