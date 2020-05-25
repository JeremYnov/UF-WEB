from .models.user import User
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from .config.database import db
from .settings import Config

# Import routes
from .controllers.user import user
from .controllers.admin import admin
from .controllers.restaurant import restaurant

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# initialization
db.init_app(app)

CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(id))


# route
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(restaurant)
