from ..config.database import db
from ..models import user, restaurant, orderContent, plate


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String(255), nullable=False)

    id_restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    order_order_content = db.relationship('Plate', secondary='order_content', backref=db.backref('order', lazy='dynamic'))

    def __init__(self, total, id_restaurant, id_user):
        self.total = total
        self.id_restaurant = id_restaurant.id
        self.id_user = id_user.id

    def __repr__(self):
        return '<Order {}>'.format(self.id)
