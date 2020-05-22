from ..config.database import db
from ..models import restaurant


class Plate(db.Model):
    __tablename__ = 'plate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    picture = db.Column(db.String(255))
    unitPrice = db.Column(db.Float(), nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __init__(self, name, picture, unitPrice, restaurant_id):
        self.name = name
        self.picture = picture
        self.unitPrice= unitPrice
        self.restaurant_id = restaurant_id.id

    def __repr__(self):
        return '<Plate {}>'.format(self.name)