from datetime import datetime, timedelta
from ..config.database import db
from ..models import user, restaurant, orderContent, plate


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String(255), nullable=False)
    nameUser = db.Column(db.String(255), nullable=False)
    addressUser = db.Column(db.String(255), nullable=False)
    mailUser = db.Column(db.String(255), nullable=False)
    nameRestaurant = db.Column(db.String(255), nullable=False)
    addressRestaurant = db.Column(db.String(255), nullable=False)
    mailRestaurant = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    delivery_date = db.Column(db.DateTime, default=datetime.now() + timedelta(hours=1), nullable=False)

    id_restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    order_order_content = db.relationship('Plate', secondary='order_content', backref=db.backref('order', lazy='dynamic'))

    def __init__(self, total, restaurant, user):
        self.total = total
        self.id_restaurant = restaurant.id
        self.id_user = user.id
        self.nameUser = user.lastName + " " + user.firstName
        self.addressUser = user.address
        self.mailUser = user.mail
        self.nameRestaurant = restaurant.name
        self.addressRestaurant = restaurant.address
        self.mailRestaurant = restaurant.mail

    def __repr__(self):
        return '<Order {}>'.format(self.id)
