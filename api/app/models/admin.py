from flask_login import UserMixin
from ..config.database import db


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable = False)
    mail = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)

    def __init__(self, username, mail, password):
        self.username = username
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<Admin {}>'.format(self.username)