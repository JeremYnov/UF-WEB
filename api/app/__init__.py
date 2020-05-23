from flask import Flask
from flask_cors import CORS

from .config.database import db
from .settings import Config

# Import routes
from .controllers.user import user
from .controllers.admin import admin


app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

# initialization
db.init_app(app)

# route
app.register_blueprint(user)
app.register_blueprint(admin)
