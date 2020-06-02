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
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.arguments(SearchSchema(partial=True))
    @blueprint.response(BlogPageOutSchema)
    def post(self, pagination, args):
        """Search blog by parameters"""
        blogTitle = args.get('title','')
        blogAuthor = args.get('author','')
        blogContent = args.get('content','')
        query = Blog.select().where(Blog.published &
                                    Blog.author.contains(blogAuthor) &
                                    Blog.title.contains(blogTitle) &
                                    Blog.content.contains(blogContent))
        return paginate(query, pagination)
