from flask_login import UserMixin
from ..config.database import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    age = db.Column(db.Integer)
    mail = db.Column(db.String(255))
    password = db.Column(db.String(255))
    avatar = db.Column(db.String(255))

    def __init__(self, username, age, mail, password, avatar):
        self.username = username
        self.age = age
        self.mail = mail
        self.password = password
        self.avatar = avatar

    def __repr__(self):
        return '<User {}>'.format(self.username)
