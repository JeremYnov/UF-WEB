import os

from flask import Blueprint, request, jsonify, send_file, send_from_directory, url_for
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from ..config.database import db
from ..models.restaurant import Restaurant
from ..models.user import User
from ..models.plate import Plate

restaurant = Blueprint('restaurant', __name__, url_prefix='/api/restaurant')


@restaurant.route('/signup', methods=['POST'])
def signup():

    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        logo = request.files.get('logo')
        address = request.form.get('address')
        category = request.form.get('category')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        if not(name) or not(mail) or not(logo) or not(address) or not(category) or not(password) or not(repassword):
            return jsonify(success=False, message='Il manque des informations')

        else:

            searchRestaurant = Restaurant.query.filter_by(mail=mail).first()

            if searchRestaurant:
                return jsonify(success=False, message="L'adresse email entrée est déjà utilisée")

            elif password != repassword:
                return jsonify(success=False, message="Les mots de passes ne sont pas similaires")

            else:
                if allowed_image(logo.filename):
                    if logo.mimetype == 'image/png' or logo.mimetype == 'image/jpg' or logo.mimetype == 'image/jpeg':

                        newRestaurant = Restaurant(name, category, logo.filename, address, mail, generate_password_hash(password, method="pbkdf2:sha256", salt_length=8))

                        db.session.add(newRestaurant)
                        db.session.commit()

                        filename = secure_filename(logo.filename)
                        uploads_dir = 'uploads/' + str(newRestaurant.id) + '/logo/'

                        os.makedirs(uploads_dir, exist_ok=True)
                        logo.save(os.path.join(uploads_dir, filename))

                        return jsonify(success=True, message="Votre compte a bien été créé")

                    else:
                        return jsonify(success=False, message="Le fichier n'est pas une image")

                else:
                    return jsonify(success=False, message="Le fichier n'a pas la bonne extension")

    return jsonify()


@restaurant.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return jsonify(session=True)
        else:
            return jsonify(session=False)

    if request.method == 'POST':
        mail = request.form.get('mail')
        password = request.form.get('password')

        if not(mail) or not(password):
            return jsonify(session=False, success=False, message="Information imcomplète")

        else:

            restaurant = Restaurant.query.filter_by(mail=mail).first()
            user = User.query.filter_by(mail=mail).first()

            if not(restaurant):
                return jsonify(session=False, success=False, message="Le compte n'existe pas")

            if check_password_hash(restaurant.password, password):
                login_user(restaurant)

                print(current_user)

                session = {
                    "session": True,
                    "user": {
                        "role": "restaurant",
                        "id": int(restaurant.id)
                    }
                }

                return jsonify(session=session, success=True, message="co")

            else:
                return jsonify(session=False, success=False, message="Mot de passe incorrecte")

    return jsonify()


@restaurant.route('/selection')
def getSelectRestaurant():

    restaurants = Restaurant.query.filter_by(selection=1).all()
    arrayRestaurant = []

    for restaurant in restaurants:

        arrayRestaurant.append({
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
            'selection': True if restaurant.selection == 1 else False
        })

    results = arrayRestaurant
    message = 'Voici la selection des restaurants'
    success = True

    return jsonify(success=success, message=message, results=results)


@restaurant.route('/all')
def getAllRestaurant():

    restaurants = Restaurant.query.all()
    arrayRestaurant = []

    for restaurant in restaurants:

        arrayRestaurant.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'category': restaurant.category,
            'logo': {
                'url': request.url_root + 'api/restaurant/' + str(restaurant.id) + '/logo/' + restaurant.logo,
                'name': restaurant.logo
            },
            'address': restaurant.address,
            'mail': restaurant.mail,
            'creation': restaurant.creation
            # 'selection': True if restaurant.selection == 1 else False
        })

    results = arrayRestaurant
    message = "Voici l'ensemble des restaurants"
    success = True

    return jsonify(success=success, message=message, results=results)


@restaurant.route('/category/<category>')
def getCategoryRestaurant(category):

    restaurants = Restaurant.query.filter_by(category=category).all()
    if restaurants:
        arrayRestaurant = []

        for restaurant in restaurants:

            arrayRestaurant.append({
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
                'selection': True if restaurant.selection == 1 else False
            })

        results = arrayRestaurant
        message = "Voici l'ensemble des restaurants avec la catégorie " + category
        success = True
    else:
        message = "La catégorie " + category + " n'est pas reconnue"
        success = False
        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)


@restaurant.route('/last')
def getLastRestaurant():

    restaurants = Restaurant.query.order_by(Restaurant.creation.desc()).limit(6).all()
    arrayRestaurant = []

    for restaurant in restaurants:

        arrayRestaurant.append({
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
            'selection': True if restaurant.selection == 1 else False
        })

    results = arrayRestaurant
    message = 'Voici la selection des restaurants'
    success = True

    return jsonify(success=success, message=message, results=results)


@restaurant.route('/<int:id>/plates')
def getRestaurantPlate(id):

    restaurant = Restaurant.query.get(int(id))
    plates = Plate.query.filter_by(id_restaurant=id).all()
    arrayPlates = []

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
        'plates': arrayPlates
    }

    message = 'Voici la liste des menus du restaurant'
    success = True

    return jsonify(success=success, message=message, results=results)


@restaurant.route('/<int:id>/logo/<logo>', methods=['GET'])
def getImageRestaurant(id, logo):
    filename = str(logo)
    uploads_dir = '../uploads/' + str(id) + '/logo/'

    return send_file(os.path.join(uploads_dir, filename))


@restaurant.route('/<int:idRestaurant>/plates/<int:idPlate>/<image>', methods=['GET'])
def getImagePlate(idRestaurant, idPlate, image):
    filename = str(image)
    uploads_dir = '../uploads/' + str(idRestaurant) + '/plates/' + str(idPlate) + '/'

    return send_file(os.path.join(uploads_dir, filename))


@restaurant.route('/add/new/plate', methods=['POST'])
def setNewPlate():
    if request.method == 'POST':
        if current_user.is_authenticated:
            restaurant = Restaurant.query.get(current_user.id)

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
                message = "Vous n'êtes pas connecté avec le bon utilisateur"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@restaurant.route('/update/plate/<int:id>', methods=['POST'])
def setUpdatePlate(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            plate = Plate.query.get(id)
            restaurant = Restaurant.query.get(current_user.id)

            if restaurant:
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
                message = "Vous n'êtes pas connecté avec le bon utilisateur"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@restaurant.route('/delete/plate/<int:id>', methods=['POST'])
def setDeletePlate(id):
    if request.method == 'POST':
        if current_user.is_authenticated:
            plate = Plate.query.get(id)
            restaurant = Restaurant.query.get(current_user.id)

            if restaurant:
                db.session.delete(plate)
                db.session.commit()

                success = True
                message = "Le plat a été supprimé"

            else:
                success = False
                message = "Vous n'êtes pas connecté avec le bon utilisateur"

        else:
            success = False
            message = "Vous n'êtes pas connecté"

    return jsonify(success=success, message=message)


@restaurant.route('/update/profile', methods=['POST'])
def setUpdateRestaurant():
    if request.method == 'POST':
        if current_user.is_authenticated:
            restaurant = Restaurant.query.get(current_user.id)
            type = request.form.get('type')

            if type == 'password':
                newPassword = request.form.get('newPassword')
                repassword = request.form.get('repassword')

                if newPassword:
                    if newPassword == repassword:
                        restaurant.password = generate_password_hash(newPassword, method="pbkdf2:sha256", salt_length=8)
                        print(restaurant.password)
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
