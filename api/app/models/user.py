from flask_login import UserMixin
from ..config.database import db
from ..models import order


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255),  nullable=False)
    lastName = db.Column(db.String(255),  nullable=False)
    address = db.Column(db.String(255),  nullable=False)
    mail = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255),  nullable=False)
    balance = db.Column(db.Float, default=0.0)

    user_order = db.relationship('Order', backref='user_order', lazy='dynamic')

    def __init__(self, firstName, lastName, address, mail, password):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.id)
