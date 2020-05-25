from ..config.database import db
from ..models import plate, order


class OrderContent(db.Model):
    __tablename__ = 'order_content'

    quantity = db.Column(db.Integer, nullable=False)
    id_order = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    id_plate = db.Column(db.Integer, db.ForeignKey('plate.id'), primary_key=True)

    def __init__(self, quantity, id_order, id_plate):
        self.quantity = quantity
        self.id_order = id_order.id
        self.id_plate = id_plate.id

    def __repr__(self):
        return '<OrderContent {}>'.format(self.id)
