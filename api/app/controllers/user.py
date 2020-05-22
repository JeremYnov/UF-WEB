from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..config.database import db
from ..models.user import User

user = Blueprint('user', __name__, url_prefix='/api/user')


@user.route('/signup',  methods=['POST'])
def signup():

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        address = request.form.get('address')
        mail = request.form.get('mail')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        if not(firstName) or not(lastName) or not(address) or not(mail) or not(password) or not(repassword):
            return jsonify(success=False, message='il manque des info')

        else:
            searchUser = User.query.filter_by(mail=mail).first()

            if searchUser:
                return jsonify(success=False, message="L'adresse email entrée est déjà utilisée")

            elif password != repassword:
                return jsonify(success=False, message="Les mots de passes ne sont pas similaires")

            else:
                newUser = User(firstName, lastName, address, mail, generate_password_hash(
                    password, method="pbkdf2:sha256", salt_length=8))

                db.session.add(newUser)
                db.session.commit()

                return jsonify(success=True, message="votre compte a été créer")

    return jsonify()
