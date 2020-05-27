from flask_login import UserMixin
from datetime import datetime, timedelta
from ..config.database import db
from ..models import order, plate


class Restaurant(UserMixin, db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)  # Fast food, Burger, Pizza, Sushi, Asiatique, Japonais
    logo = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    selection = db.Column(db.Boolean, default=False, nullable=False)
    creation = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    restaurant_plate = db.relationship('Plate', backref='restaurant', lazy='dynamic')
    restaurant_order = db.relationship('Order', backref='order', lazy='dynamic')

    def __init__(self, name, category, logo, address, mail, password):
        self.name = name
        self.category = category
        self.logo = logo
        self.address = address
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)
