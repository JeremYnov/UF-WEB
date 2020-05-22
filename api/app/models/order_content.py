from ..config.database import db
from ..models import restaurant, user

order_content = db.Table('order_content',
db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False),
db.Column(db.Integer, db.ForeignKey('plate.id'), nullable=False)
)

class OrderContent(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    plate_id = db.relationship('Plate', secondary=order_content, backref=db.backref('plates',lazy='dynamic'))
    

    def __init__(self, quantity, order_id,plate_id):
        self.quantity = quantity

        self.order_id = order_id.id
        self.plate_id = plate_id.id