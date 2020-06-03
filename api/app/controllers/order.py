import json
from datetime import datetime, timedelta
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
    if request.method == 'POST':
        if current_user.is_authenticated:

            order = request.form.get('order')
            order = json.loads(order)

            idRestaurant = int(order['idRestaurant'])
            idUser = int(order['idUser'])
            plates = order['orderContent']

            restaurant = Restaurant.query.get(idRestaurant)
            user = current_user

            if user.id == idUser:
                total = 2.5
                for plate in plates:
                    total += float(plate['price'])

                if user.balance > total:
                    user.balance -= total

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
                    message = "votre compte n'a pas assez d'argent"

            else:
                success = False
                message = " ce n'est pas le bon utilisateur"

        else:
            success = False
            message = "vous etes pas connecter"

    return jsonify(success=success, message=message)


@order.route('/progress')
def getOrderInProgress():
    if current_user.is_authenticated:
        orderInProgress = Order.query.filter_by(id_restaurant=current_user.id).filter(Order.delivery_date > datetime.now()).all()

        if orderInProgress:
            arrayOrderInProgress = []
            for order in orderInProgress:

                user = User.query.get(order.id_user)
                arrayOrderInProgress.append(
                    {
                        "id": order.id,
                        "total": float(order.total),
                        "restaurant": order.id_restaurant,
                        "user": {
                            "id": user.id,
                            "name": user.lastName + ' ' + user.firstName,
                            "address": user.address,
                            "mail": user.mail
                        }
                    }
                )

            results = arrayOrderInProgress
            message = "les commande en cours"
            success = True

        else:
            results = None
            message = "il ny a pas de commande en cours"
            success = False

        return jsonify(success=success, message=message, results=results)

    else:
        success = False
        message = "vous etes pas connecter"

    return jsonify(success=success, message=message)


@order.route('/historic')
def getOrderHistoric():
    if current_user.is_authenticated:
        orderHistorics = Order.query.filter_by(id_restaurant=current_user.id).filter(Order.delivery_date < datetime.now()).all()

        if orderHistorics:
            arrayOrderHistorics = []

            for order in orderHistorics:
                user = User.query.get(order.id_user)
                arrayOrderHistorics.append(
                    {
                        "id": order.id,
                        "total": float(order.total),
                        "restaurant": order.id_restaurant,
                        "creationDate": order.creation_date.strftime("%m/%d/%Y"),
                        "user": {
                            "id": user.id,
                            "name": user.lastName + ' ' + user.firstName,
                            "address": user.address,
                            "mail": user.mail
                        }
                    }
                )

            results = arrayOrderHistorics
            message = "les commande en cours"
            success = True

        else:
            results = None
            message = "il ny a pas de commande en cours"
            success = False

        return jsonify(success=success, message=message, results=results)

    else:
        success = False
        message = "vous etes pas connecter"

    return jsonify(success=success, message=message)
