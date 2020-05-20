from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.config.database import db
from app.settings import Config
from app.models import *

app = Flask(__name__)
app.config.from_object(Config)

# initialization
db.init_app(app)

# migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

with app.app_context():
    db.drop_all()
    db.create_all()
