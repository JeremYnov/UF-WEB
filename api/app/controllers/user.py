from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from ..config.database import db
from ..models.user import User

user = Blueprint('user', __name__, url_prefix='/api/user')


@user.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify(session=False, success=True, message='Deconnexion')
    else:
        return jsonify(session=False, success=False, message='Pas de compte connecté')


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
            return jsonify(success=False, message='Certaines informations ne sont pas remplies')

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

                return jsonify(success=True, message="Votre compte a été créé")

    return jsonify()


@user.route('/login', methods=['GET', 'POST'])
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
            return jsonify(session=False, success=False, message="Information imcomplaite")

        else:

            user = User.query.filter_by(mail=mail).first()

            if not(user):
                return jsonify(session=False, success=False, message="le compte existe pas")

            if check_password_hash(user.password, password):
                login_user(user)

                return jsonify(session=True, success=True, message="co")

            else:
                return jsonify(session=False, success=False, message="mot de passe incorrecte")

    return jsonify()


@user.route('/profile')
def getProfile():
    if current_user.is_authenticated:
        results = {
            'id': current_user.id,
            'firstName': current_user.firstName,
            'lastName': current_user.lastName,
            'address': current_user.address,
            'mail': current_user.mail,
            'balance': current_user.balance
        }

        message = "Voici le profil de l'utilisateur connecté"
        success = True

    else:

        message = "L'utilisateur n'est pas connecté"
        success = False

        return jsonify(success=success, message=message)

    return jsonify(success=success, message=message, results=results)


@user.route('/profile/update', methods=['POST'],)
def updateProfile():
    if request.method == 'POST':

        if current_user.is_authenticated:
            user = User.query.get(current_user.id)
            type = request.form.get('type')

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
                    message = 'tous les champs sont vide'
                    success = False

            db.session.commit()

        else:
            message = "L'utilisateur n'est pas connecter"
            success = False

    return jsonify(success=success, message=message)
