from ..config.database import db


class Plate(db.Model):
    __tablename__ = 'plate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    picture = db.Column(db.String(255))
    unitPrice = db.Column(db.Float(), nullable = False)

    def __init__(self, name, picture, unitPrice):
        self.name = name
        self.picture = picture
        self.unitPrice= unitPrice

    def __repr__(self):
        return '<Plate {}>'.format(self.name)