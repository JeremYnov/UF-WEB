import json
from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user
from ..config.database import db
from ..models.restaurant import Restaurant
from ..models.user import User
from ..models.plate import Plate
from ..models.order import Order
from ..models.orderContent import OrderContent

order = Blueprint('order', __name__, url_prefix='/api/order')


@order.route('/add', methods=['POST'])
def setAddOrder():
    {
        "idRestaurant": 1,
        "idUser": 1,
        "orderContent": [
            {
                "id": 1,
                "price": 3,
                "quantity": 2
            },
            {
                "id": 2,
                "price": 3,
                "quantity": 1
            },
            {
                "id": 3,
                "price": 3.5,
                "quantity": 2
            }
        ]
    }

    if request.method == 'POST':
        if current_user.is_authenticated:

            order = request.form.get('order')
            order = json.loads(order)

            idRestaurant = order['idRestaurant']
            idUser = order['idUser']
            plates = order['orderContent']

            restaurant = Restaurant.query.get(int(idRestaurant))
            user = User.query.get(int(idUser))
            total = 2.5

            for plate in plates:
                total += float(plate['price'])

            order = Order(total, restaurant, user)
            db.session.add(order)
            db.session.commit()

            for plate in plates:
                getPlate = Plate.query.get(int(plate['id']))
                orderContent = OrderContent(int(plate['quantity']), order, getPlate)
                db.session.add(orderContent)
                db.session.commit()

            success = True
            message = "la commande a bien été pris en compte"

        else:
            success = False
            message = "vous etes pas connecter"

    return jsonify(success=success, message=message)
