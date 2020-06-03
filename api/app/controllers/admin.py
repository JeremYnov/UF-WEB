from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..config.database import db
from ..models.admin import Admin

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
