from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..config.database import db
from ..models.admin import Admin
from ..models.user import User
from ..models.restaurant import Restaurant
from ..models.order import Order

admin = Blueprint('admin', __name__, url_prefix='/api/admin')


@admin.route('/signup',  methods=['POST'])
def signup():

    if request.method == 'POST':
        userName = request.form.get('userName')
        mail = request.form.get('mail')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        if not(userName) or not(mail) or not(password) or not(repassword):
            return jsonify(success=False, message='Certaines informations ne sont pas remplies')

        else:
            searchAdmin = Admin.query.filter_by(mail=mail).first()

            if searchAdmin:
                return jsonify(success=False, message="L'adresse email entrée est déjà utilisée")

            elif password != repassword:
                return jsonify(success=False, message="Les mots de passes ne sont pas similaires")

            else:
                newAdmin = Admin(userName, mail, generate_password_hash(
                    password, method="pbkdf2:sha256", salt_length=8))

                db.session.add(newAdmin)
                db.session.commit()

                return jsonify(success=True, message="Votre compte a été créé")

    return jsonify()


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mail = request.form.get('mail')
        password = request.form.get('password')

        if not(mail) or not(password):
            return jsonify(session=False, success=False, message="Informations incomplètes")

        else:
            admin = Admin.query.filter_by(mail=mail).first()

            if not(admin):
                return jsonify(session=False, success=False, message="Le compte n'existe pas")

            if check_password_hash(admin.password, password):
                login_user(admin)

                session = {
                    "session": True,
                    "user": {
                        "role": "admin",
                        "id": int(admin.id)
                    }
                }
                success = True
                message = "Vous êtes connecté, vous allez être redirigé"

            else:
                session = False
                success = False
                message = "Mot de passe incorrect"

    return jsonify(session=session, success=success, message=message)


@admin.route('/list/member')
def getAllMember():
    if current_user.is_authenticated:
        users = User.query.all()

        arrayUsers = []

        for user in users:
            arrayUsers.append(
                {
                    "id": user.id,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "address": user.address,
                    "mail": user.mail,
                    "balance": user.balance
                }
            )

        results = arrayUsers
        success = False
        message = "Liste des utilisateurs"

    else:
        message = "L'utilisateur n'est pas connecter"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(results=results, success=success, message=message)


@admin.route('/list/restaurant')
def getAllRestaurant():
    if current_user.is_authenticated:
        restaurants = Restaurant.query.all()

        arrayRestaurants = []

        for restaurant in restaurants:
            arrayRestaurants.append(
                {
                    "id": restaurant.id,
                    "name": restaurant.name,
                    "category": restaurant.category,
                    "logo": {
                        "name": restaurant.logo,
                        "url": request.url_root + 'api/restaurant/' + str(restaurant.id) + '/logo/' + restaurant.logo
                    },
                    "address": restaurant.address,
                    "mail": restaurant.mail,
                    "creation": restaurant.creation
                }
            )

        results = arrayRestaurants
        success = False
        message = "Liste des restaurants"

    else:
        message = "L'utilisateur n'est pas connecter"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(results=results, success=success, message=message)


@admin.route('/all/order/progress')
def getAllOrderInProgress():
    if current_user.is_authenticated:
        orders = Order.query.filter(Order.delivery_date > datetime.now()).all()
        arrayOrders = []

        for order in orders:
            user = User.query.get(order.id_user)
            restaurant = Restaurant.query.get(order.id_restaurant)

            arrayOrders.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": {
                        "id": restaurant.id,
                        "name": restaurant.name,
                        "address": restaurant.address,
                        "mail": restaurant.mail
                    },
                    "user": {
                        "id": user.id,
                        "name": user.lastName + ' ' + user.firstName,
                        "address": user.address,
                        "mail": user.mail
                    }
                }
            )

        results = arrayOrders
        success = False
        message = "Liste des commande en cours"

    else:
        message = "L'utilisateur n'est pas connecter"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(results=results, success=success, message=message)


@admin.route('/all/order/historic')
def getAllOrderHistoric():
    if current_user.is_authenticated:
        orders = Order.query.filter(Order.delivery_date < datetime.now()).all()
        arrayOrders = []

        for order in orders:
            user = User.query.get(order.id_user)
            restaurant = Restaurant.query.get(order.id_restaurant)

            arrayOrders.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": {
                        "id": restaurant.id,
                        "name": restaurant.name,
                        "address": restaurant.address,
                        "mail": restaurant.mail
                    },
                    "user": {
                        "id": user.id,
                        "name": user.lastName + ' ' + user.firstName,
                        "address": user.address,
                        "mail": user.mail
                    }
                }
            )

        results = arrayOrders
        success = False
        message = "Liste des historique de commande"

    else:
        message = "L'utilisateur n'est pas connecter"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(results=results, success=success, message=message)


@admin.route('/dashboard/data')
def getDashboardData():
    if current_user.is_authenticated:

        restaurants = Restaurant.query.all()
        users = User.query.all()
        ordersInProgress = Order.query.filter(Order.delivery_date > datetime.now()).all()
        ordersHistoric = Order.query.filter(Order.delivery_date < datetime.now()).all()

        results = {
            "numberRestaurant": len(restaurants),
            "numberUser": len(users),
            "numberOrderInProgress": len(ordersInProgress),
            "numberOrderHistoric": len(ordersHistoric),
            "profit": (len(ordersHistoric) + len(ordersInProgress)) * 2.5,
        }
        success = False
        message = "Liste des historique de commande"

    else:
        message = "L'utilisateur n'est pas connecté"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)


@admin.route('/member/<int:id>/profile')
def getMemberProfile(id):
    if current_user.is_authenticated:
        user = User.query.get(id)
        results = {
            'id': user.id,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'address': user.address,
            'mail': user.mail,
            'balance': user.balance
        }

        message = "Voici le profil de l'utilisateur " + str(user.id)
        success = True

    else:

        message = "L'utilisateur n'est pas connecté"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)
