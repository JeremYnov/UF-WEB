from flask_login import UserMixin
from ..config.database import db
from ..models import order, plate


class Restaurant(UserMixin, db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255))
    address = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    restaurant_plate = db.relationship('Plate', backref='restaurant', lazy='dynamic')
    restaurant_order = db.relationship('Order', backref='order', lazy='dynamic')

    def __init__(self, name, logo, address, mail, password):
        self.name = name
        self.logo = logo
        self.address = address
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)
