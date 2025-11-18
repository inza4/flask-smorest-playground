from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
api = Api()
ma = Marshmallow()
