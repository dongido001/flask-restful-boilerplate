from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

class Hello(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, comment):
        self.comment = comment

class HelloSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    comment = fields.String(required=True, validate=validate.Length(250))
    url = ma.URLFor('api.categoryresource', id='<id>', _external=True)
    comments = fields.Nested('HelloSchema', many=True)


