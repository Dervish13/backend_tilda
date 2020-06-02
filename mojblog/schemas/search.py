import sys

from freenit.schemas.base import BaseSchema
from freenit.schemas.user import UserSchema
from marshmallow import fields

class SearchSchema(BaseSchema):
    title = fields.String()
    author = fields.Nested(UserSchema, dump_only=True)
    content = fields.String()
