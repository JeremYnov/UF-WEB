class Config:
    DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/uf_web"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
