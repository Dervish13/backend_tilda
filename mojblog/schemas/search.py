import sys

from freenit.schemas.paging import PageInSchema
from marshmallow import fields

class SearchSchema(PageInSchema):
    Search = fields.String()
