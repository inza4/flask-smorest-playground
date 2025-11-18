from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import Schema, fields

import uuid

bp_users = Blueprint("users", "users", url_prefix="/users", description="Users API")


class CreateUserSchema(Schema):
    username = fields.String()


class UserSchema(CreateUserSchema):
    id = fields.UUID()


class ListUsers(Schema):
    users = fields.List(fields.Nested(UserSchema))


@bp_users.route("/")
class UsersCollection(MethodView):
    @bp_users.response(status_code=200, schema=ListUsers)
    def get(self):
        return {"users": ["user1", "user2"]}

    @bp_users.arguments(CreateUserSchema)
    @bp_users.response(status_code=201, schema=UserSchema)
    def post(self, data: CreateUserSchema):
        user_data = dict(id=uuid.uuid4(), username=data["username"])
        new_user = UserSchema().dump(user_data)
        return new_user
