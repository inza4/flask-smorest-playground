from flask import Flask
from .extensions import db, migrate

from .config import Config

from .models import *


server = Flask(__name__)
server.config.from_object(Config)

db.init_app(server)
migrate.init_app(server, db)
