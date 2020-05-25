from freenit.api.methodviews import MethodView
from freenit.schemas.paging import PageInSchema, paginate
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt_identity, jwt_optional, jwt_required
from flask import request

from ..schemas.blog import BlogSchema, BlogPageOutSchema
from ..schemas.search import SearchSchema
from ..models.blog import Blog
from ..models.user import User

blueprint = Blueprint('search', 'search')


@blueprint.route('', endpoint='search')
class SearchApi(MethodView):
    @blueprint.arguments(SearchSchema(), location='headers')
    @blueprint.response(BlogPageOutSchema)
    def get(self, headers):
        """Search blog by title"""
        searchParam = headers.get('Search','')
        query = Blog.select().where(Blog.published,
                                    Blog.title.contains(searchParam)).order_by(Blog.author)
        return paginate(query, headers)
