class Config:
    DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/test"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
