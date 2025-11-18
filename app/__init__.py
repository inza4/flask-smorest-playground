from flask import Flask

from .users import bp_users

from .extensions import db, migrate, api

from .config import Config

from .models import *


server = Flask(__name__)
server.config.from_object(Config)

db.init_app(server)
migrate.init_app(server, db)
api.init_app(server)


api.register_blueprint(bp_users)
