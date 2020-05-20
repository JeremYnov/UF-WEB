from flask import Flask

from .config.database import db
from .settings import Config

# Import routes
from .controllers import main

app = Flask(__name__)
app.config.from_object(Config)

# initialization
db.init_app(app)

# route
app.register_blueprint(main.main)
