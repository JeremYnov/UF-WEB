from ..config.database import db
from ..models import restaurant, user


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String(255), nullable = False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, total, restaurant_id,user_id):
        self.total = total

        self.restaurant_id = restaurant_id.id
        self.user_id = user_id.id

    # def __repr__(self):
    #     return '<Order {}>'.format(self.name)