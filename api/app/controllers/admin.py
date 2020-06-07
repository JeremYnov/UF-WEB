import os
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from ..config.database import db
from ..models.admin import Admin
from ..models.user import User
from ..models.restaurant import Restaurant
from ..models.order import Order
from ..models.plate import Plate

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
            # user = User.query.get(order.id_user)
            # restaurant = Restaurant.query.get(order.id_restaurant)

            arrayOrders.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": {
                        "id": order.id_restaurant,
                        "name": order.nameRestaurant,
                        "address": order.addressRestaurant,
                        "mail": order.mailRestaurant
                    },
                    "user": {
                        "id": order.id_user,
                        "name": order.nameUser,
                        "address": order.addressUser,
                        "mail": order.mailUser
                    }
                }
            )

        results = arrayOrders
        success = True
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
            # user = User.query.get(order.id_user)
            # restaurant = Restaurant.query.get(order.id_restaurant)

            arrayOrders.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "deliveryDate": order.delivery_date.strftime("%m/%d/%Y"),
                    "restaurant": {
                        "id": order.id_restaurant,
                        "name": order.nameRestaurant,
                        "address": order.addressRestaurant,
                        "mail": order.mailRestaurant
                    },
                    "user": {
                        "id": order.id_user,
                        "name": order.nameUser,
                        "address": order.addressUser,
                        "mail": order.mailUser
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
        orders = Order.query.all()

        results = {
            "numberRestaurant": len(restaurants),
            "numberUser": len(users),
            "numberOrderInProgress": len(ordersInProgress),
            "numberOrder": len(orders),
            "profit": len(orders) * 2.5,
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

        ordersInProgress = Order.query.filter_by(id_user=user.id).filter(Order.delivery_date > datetime.now()).all()
        ordersHistoric = Order.query.filter_by(id_user=user.id).filter(Order.delivery_date < datetime.now()).all()

        arrayPlates = []
        arrayOrdersInProgress = []
        arrayOrdersHistoric = []

        for order in ordersInProgress:
            restaurant = Restaurant.query.get(order.id_user)

            arrayOrdersInProgress.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": {
                        "id": order.id_restaurant,
                        "name": order.nameRestaurant,
                        "address": order.addressRestaurant,
                        "mail": order.mailRestaurant
                    },
                    "creationDate": order.creation_date.strftime("%m/%d/%Y"),
                    "user": order.id_user
                }
            )

        for order in ordersHistoric:
            user = User.query.get(order.id_user)

            arrayOrdersHistoric.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": {
                        "id": order.id_restaurant,
                        "name": order.nameRestaurant,
                        "address": order.addressRestaurant,
                        "mail": order.mailRestaurant
                    },
                    "creationDate": order.creation_date.strftime("%m/%d/%Y"),
                    "user": order.id_user
                }
            )

        results = {
            'id': user.id,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'address': user.address,
            'mail': user.mail,
            'balance': user.balance,
            'ordersInProgress': arrayOrdersInProgress,
            'ordersHistoric': arrayOrdersHistoric
        }

        message = "Voici le profil de l'utilisateur " + str(user.id)
        success = True

    else:

        message = "L'utilisateur n'est pas connecté"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)


@admin.route('/restaurant/<int:id>/dashboard')
def getRestaurantDashboard(id):
    if current_user.is_authenticated:
        restaurant = Restaurant.query.get(id)
        plates = Plate.query.filter_by(id_restaurant=restaurant.id).all()
        ordersInProgress = Order.query.filter_by(id_restaurant=restaurant.id).filter(Order.delivery_date > datetime.now()).all()
        ordersHistoric = Order.query.filter_by(id_restaurant=restaurant.id).filter(Order.delivery_date < datetime.now()).all()

        arrayPlates = []
        arrayOrdersInProgress = []
        arrayOrdersHistoric = []

        for order in ordersInProgress:
            user = User.query.get(order.id_user)

            arrayOrdersInProgress.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": order.id_restaurant,
                    "creationDate": order.creation_date.strftime("%m/%d/%Y"),
                    "user": {
                        "id": order.id_user,
                        "name": order.nameUser,
                        "address": order.addressUser,
                        "mail": order.mailUser
                    }
                }
            )

        for order in ordersHistoric:
            user = User.query.get(order.id_user)

            arrayOrdersHistoric.append(
                {
                    "id": order.id,
                    "total": float(order.total),
                    "restaurant": order.id_restaurant,
                    "creationDate": order.creation_date.strftime("%m/%d/%Y"),
                    "user": {
                        "id": order.id_user,
                        "name": order.nameUser,
                        "address": order.addressUser,
                        "mail": order.mailUser
                    }
                }
            )

        for plate in plates:
            arrayPlates.append({
                'id': plate.id,
                'name': plate.name,
                'type': plate.type,
                'picture': {
                    'url': request.url_root + 'api/restaurant/' + str(restaurant.id) + '/plates/' + str(plate.id) + '/' + plate.picture,
                    'name': plate.picture
                },
                'content': plate.content,
                'unitPrice': plate.unitPrice,
                'id_restaurant': plate.id_restaurant
            })

        results = {
            'id': restaurant.id,
            'name': restaurant.name,
            'category': restaurant.category,
            'logo': {
                'url': request.url_root + 'api/restaurant/' + str(restaurant.id) + '/logo/' + restaurant.logo,
                'name': restaurant.logo
            },
            'address': restaurant.address,
            'mail': restaurant.mail,
            'creation': restaurant.creation,
            'selection': True if restaurant.selection == 1 else False,
            'plates': arrayPlates,
            'ordersInProgress': arrayOrdersInProgress,
            'ordersHistoric': arrayOrdersHistoric
        }

        message = "Voici le profil du restaurant " + str(restaurant.id)
        success = True

    else:

        message = "L'utilisateur n'est pas connecté"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)


@admin.route('/member/<int:id>/update/profile', methods=['POST'])
def setMemberUpdateProfile(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            user = User.query.get(id)
            type = request.form.get('type')

            if user:

                if type == 'password':
                    newPassword = request.form.get('newPassword')
                    repassword = request.form.get('repassword')

                    if newPassword:
                        if newPassword == repassword:
                            user.password = generate_password_hash(newPassword, method="pbkdf2:sha256", salt_length=8)

                            message = "le mot de passe à bien été modifié"
                            success = True

                        else:
                            message = "le mot de passe n'est pas le meme sur les deux champs"
                            success = False

                    else:
                        message = "le champ du mot de passe est vide"
                        success = False

                else:
                    firstName = request.form.get('firstName')
                    lastName = request.form.get('lastName')
                    address = request.form.get('address')
                    balance = request.form.get('sold')

                    args = []

                    if firstName and user.firstName != firstName:
                        user.firstName = firstName
                        args.append("le prénom")

                    if lastName and user.lastName != lastName:
                        user.lastName = lastName
                        args.append("le nom")

                    if address and user.address != address:
                        user.address = address
                        args.append("l'adresse")

                    if balance and user.balance != float(balance):
                        user.balance = float(balance)
                        args.append("le solde")

                    if len(args) == 4:
                        message = args[0] + ', ' + args[1] + ', ' + args[2] + ', ' + args[3] + ' ont été modifié'
                        success = True

                    if len(args) == 3:
                        message = args[0] + ', ' + args[1] + ', ' + args[2] + ' ont été modifié'
                        success = True

                    elif len(args) == 2:
                        message = args[0] + ', ' + args[1] + ' ont été modifié'
                        success = True

                    elif len(args) == 1:
                        message = args[0] + ' a été modifié'
                        success = True

                    else:
                        message = 'Tous les champs sont vide'
                        success = False

                db.session.commit()

            else:
                success = False
                message = "L'utilisateur n'est pas reconnue"

        else:
            message = "L'utilisateur n'est pas connecté"
            success = False

    return jsonify(success=success, message=message)


@admin.route('/member/<int:id>/delete')
def setMemberDelete(id):
    if current_user.is_authenticated:
        user = User.query.get(id)

        if user:
            db.session.delete(user)
            db.session.commit()
            success = True
            message = "L'utilisateur a été supprimé"

        else:
            success = False
            message = "L'utilisateur n'est pas reconnue"

    else:
        message = "L'utilisateur n'est pas connecté"
        success = False

    return jsonify(success=success, message=message)


@admin.route('/restaurant/<int:id>/delete')
def setRestaurantDelete(id):
    if current_user.is_authenticated:
        restaurant = Restaurant.query.get(id)
        plates = Plate.query.filter_by(id_restaurant=restaurant.id)

        if restaurant:
            for plate in restaurant.restaurant_plate:
                db.session.delete(plate)
            db.session.delete(restaurant)
            db.session.commit()
            success = True
            message = "Le restaurant a été supprimé"

        else:
            success = False
            message = "Le restaurant n'est pas reconnue"

    else:
        message = "L'utilisateur n'est pas connecté"
        success = False

    return jsonify(success=success, message=message)


@admin.route('/restaurant/<int:id>/update/profile', methods=['POST'])
def setRestaurantUpdateProfile(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            restaurant = Restaurant.query.get(id)
            type = request.form.get('type')

            if restaurant:
                if type == 'password':
                    newPassword = request.form.get('newPassword')
                    repassword = request.form.get('repassword')

                    if newPassword:
                        if newPassword == repassword:
                            restaurant.password = generate_password_hash(newPassword, method="pbkdf2:sha256", salt_length=8)

                            message = "Le mot de passe à bien été modifié"
                            success = True

                        else:
                            message = "Le mot de passe n'est pas similaire sur les deux champs"
                            success = False
                    else:
                        message = "Le champ du mot de passe est vide"
                        success = False
                else:
                    name = request.form.get('name')
                    category = request.form.get('category')
                    address = request.form.get('address')
                    logo = request.files.get('logo')

                    args = []

                    if logo and restaurant.logo != logo.filename:
                        if allowed_image(logo.filename):
                            if logo.mimetype == 'image/png' or logo.mimetype == 'image/jpg' or logo.mimetype == 'image/jpeg':

                                filename = secure_filename(logo.filename)
                                uploads_dir = 'uploads/' + str(restaurant.id) + '/logo/'

                                os.makedirs(uploads_dir, exist_ok=True)
                                logo.save(os.path.join(uploads_dir, filename))

                                restaurant.logo = logo.filename
                                args.append("le logo")

                            else:
                                return jsonify(success=False, message="Le fichier n'est pas une image")

                        else:
                            return jsonify(success=False, message="Le fichier n'a pas la bonne extension")

                    if name and restaurant.name != name:
                        restaurant.name = name
                        args.append("le nom")

                    if category and restaurant.category != category:
                        restaurant.category = category
                        args.append("la categorie")

                    if address and restaurant.address != address:
                        restaurant.address = address
                        args.append("l'adresse")

                    if len(args) == 4:
                        message = args[0] + ', ' + args[1] + ', ' + args[2] + ', ' + args[3] + ' ont été modifié'
                        success = True

                    elif len(args) == 3:
                        message = args[0] + ', ' + args[1] + ', ' + args[2] + ' ont été modifié'
                        success = True

                    elif len(args) == 2:
                        message = args[0] + ', ' + args[1] + ' ont été modifié'
                        success = True

                    elif len(args) == 1:
                        message = args[0] + ' a été modifié'
                        success = True

                    else:
                        message = 'Tous les champs sont vides'
                        success = False

                db.session.commit()

            else:
                success = False
                message = "Le restaurant n'est pas reconnue"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@admin.route('/restaurant/<int:id>/add/new/plate', methods=['POST'])
def setRestaurantNewPlate(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            restaurant = Restaurant.query.get(id)

            if restaurant:
                name = request.form.get('name')
                type = request.form.get('type')
                content = request.form.get('content')
                unitPrice = request.form.get('price')
                picture = request.files.get('picture')

                if name and type and unitPrice and picture:
                    if allowed_image(picture.filename):
                        if picture.mimetype == 'image/png' or picture.mimetype == 'image/jpg' or picture.mimetype == 'image/jpeg':

                            if type != 'Boisson' and content:
                                newPlate = Plate(name, type, content, picture.filename, float(unitPrice), restaurant)

                            elif type == 'Boisson':
                                newPlate = Plate(name, type, None, picture.filename, float(unitPrice), restaurant)

                            else:
                                return jsonify(success=False, message="Le plat a besoin d'une description")

                            db.session.add(newPlate)
                            db.session.commit()

                            filename = secure_filename(picture.filename)
                            uploads_dir = 'uploads/' + str(restaurant.id) + '/plates/' + str(newPlate.id) + '/'
                            os.makedirs(uploads_dir, exist_ok=True)
                            picture.save(os.path.join(uploads_dir, filename))

                            success = True
                            message = "Le plat a été créé"

                        else:
                            success = False
                            message = "Le fichier n'est pas une image"

                    else:
                        success = False
                        message = "Le fichier n'a pas la bonne extension"

                else:
                    success = False
                    message = "Il manque des informations"

            else:
                success = False
                message = "Le restaurant n'est pas reconnu"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@admin.route('/restaurant/<int:idRestaurant>/delete/plate/<int:idPlate>')
def setDeletePlate(idRestaurant, idPlate):
    if current_user.is_authenticated:
        plate = Plate.query.get(idPlate)
        restaurant = Restaurant.query.get(idRestaurant)

        if restaurant:
            if plate:
                if restaurant.id == plate.id_restaurant:
                    db.session.delete(plate)
                    db.session.commit()
                    success = True
                    message = "Le plat a été supprimé"

                else:
                    success = False
                    message = "Le plat n'appartient pas au restaurant"

            else:
                success = False
                message = "Le plat n'est pas reconnu"

        else:
            success = False
            message = "Le restaurant n'est pas reconnu"

    else:
        success = False
        message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@admin.route('/restaurant/<int:idRestaurant>/update/plate/<int:idPlate>', methods=['POST'])
def setUpdatePlate(idRestaurant, idPlate):
    if request.method == 'POST':
        if current_user.is_authenticated:
            plate = Plate.query.get(idPlate)
            restaurant = Restaurant.query.get(idRestaurant)

            if restaurant:
                if plate:
                    if restaurant.id == plate.id_restaurant:
                        name = request.form.get('name')
                        type = request.form.get('type')
                        content = request.form.get('content')
                        unitPrice = request.form.get('price')
                        picture = request.files.get('picture')

                        args = []

                        if picture and plate.picture != picture.filename:
                            if allowed_image(picture.filename):
                                if picture.mimetype == 'image/png' or picture.mimetype == 'image/jpg' or picture.mimetype == 'image/jpeg':
                                    filename = secure_filename(picture.filename)
                                    uploads_dir = 'uploads/' + str(current_user.id) + '/plates/' + str(plate.id) + '/'

                                    os.makedirs(uploads_dir, exist_ok=True)
                                    picture.save(os.path.join(uploads_dir, filename))

                                    plate.picture = picture.filename
                                    args.append("l'image")

                                else:
                                    return jsonify(success=False, message="Le fichier n'est pas une image")

                            else:
                                return jsonify(success=False, message="Le fichier n'a pas la bonne extension")

                        if name and plate.name != name:
                            plate.name = name
                            args.append("le nom")

                        if content and plate.content != content:
                            plate.content = content
                            args.append("la description")

                        if type and plate.type != type:
                            if type == 'Boisson':
                                plate.type = type
                                plate.content = None
                            else:
                                plate.type = type

                                if not(content):
                                    return jsonify(success=False, message="Le plat a besoin d'une description")

                            args.append("le type")

                        if unitPrice and plate.unitPrice != float(unitPrice):
                            plate.unitPrice = float(unitPrice)
                            args.append("le prix")

                        if len(args) == 5:
                            message = args[0] + ', ' + args[1] + ', ' + args[2] + ', ' + args[3] + ', ' + args[4] + ' ont été modifié'
                            success = True

                        elif len(args) == 4:
                            message = args[0] + ', ' + args[1] + ', ' + args[2] + ', ' + args[3] + ' ont été modifié'
                            success = True

                        elif len(args) == 3:
                            message = args[0] + ', ' + args[1] + ', ' + args[2] + ' ont été modifié'
                            success = True

                        elif len(args) == 2:
                            message = args[0] + ', ' + args[1] + ' ont été modifié'
                            success = True

                        elif len(args) == 1:
                            message = args[0] + ' a été modifié'
                            success = True

                        else:
                            message = 'Tous les champs sont vides'
                            success = False

                        db.session.commit()

                    else:
                        success = False
                        message = "Le plat n'appartient pas au restaurant"

                else:
                    success = False
                    message = "Le plat n'est pas reconnu"

            else:
                success = False
                message = "Le restaurant n'est pas reconnu"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


def allowed_image(filename):
    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in ["JPEG", "JPG", "PNG"]:
        return True
    else:
        return False
