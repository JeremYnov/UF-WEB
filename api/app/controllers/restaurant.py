import os

from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from ..config.database import db
from ..models.restaurant import Restaurant

restaurant = Blueprint('restaurant', __name__, url_prefix='/api/restaurant')


@restaurant.route('/signup',  methods=['POST'])
def signup():

    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        logo = request.files.get('logo')
        address = request.form.get('address')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        if not(name) or not(mail) or not(logo) or not(address) or not(password) or not(repassword):
            return jsonify(success=False, message='il manque des info')

        else:

            searchRestaurant = Restaurant.query.filter_by(mail=mail).first()

            if searchRestaurant:
                return jsonify(success=False, message="L'adresse email entrée est déjà utilisée")

            elif password != repassword:
                return jsonify(success=False, message="Les mots de passes ne sont pas similaires")

            else:
                if allowed_image(logo.filename):
                    if logo.mimetype == 'image/png' or logo.mimetype == 'image/jpg' or logo.mimetype == 'image/jpeg':

                        newRestaurant = Restaurant(name, logo.filename, address, mail, generate_password_hash(password, method="pbkdf2:sha256", salt_length=8))

                        db.session.add(newRestaurant)
                        db.session.commit()

                        filename = secure_filename(logo.filename)
                        uploads_dir = 'uploads/' + str(newRestaurant.id) + '/logo/'

                        os.makedirs(uploads_dir, exist_ok=True)
                        logo.save(os.path.join(uploads_dir, filename))

                        return jsonify(success=True, message="votre compte a été créer")

                    else:
                        return jsonify(success=False, message="Le fichier n'est pas une image")

                else:
                    return jsonify(success=False, message="Le fichier n'a pas la bonne extension")

    return jsonify()


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
