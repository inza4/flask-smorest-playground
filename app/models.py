from extensions import db


class UserSchema(db.Model):
    __tablename__ = "users"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(128))
