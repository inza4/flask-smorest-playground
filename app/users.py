from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import UserSchema
from .extensions import db

import uuid

bp_users = Blueprint("users", "users", url_prefix="/users", description="Users API")


class CreateUser(Schema):
    username = fields.String()


class User(SQLAlchemyAutoSchema):
    class Meta:
        model = UserSchema


class ListUsers(Schema):
    users = fields.List(fields.Nested(User))


@bp_users.route("/")
class UsersCollection(MethodView):
    @bp_users.response(status_code=200, schema=ListUsers)
    def get(self):
        users = (
            db.session.execute(db.select(UserSchema).order_by(UserSchema.username))
            .scalars()
            .all()
        )
        return {"users": users}

    @bp_users.arguments(CreateUser)
    @bp_users.response(status_code=201, schema=User)
    def post(self, data: CreateUser):
        user_data = dict(id=uuid.uuid4(), username=data["username"])
        new_user = User().dump(user_data)

        user_schema = UserSchema(**user_data)

        db.session.add(user_schema)
        db.session.commit()

        return new_user
