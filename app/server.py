from flask import Flask

from users import bp_users

from extensions import db, migrate, api, ma

from config import Config

from models import *


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)
api.init_app(app)


api.register_blueprint(bp_users)

if __name__ == "__main__":
    app.run()
