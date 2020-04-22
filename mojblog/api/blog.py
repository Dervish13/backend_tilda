from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_optional, jwt_required

from ..schemas.blog import BlogSchema
from ..models.blog import Blog
from ..models.user import User

blueprint = Blueprint('blogs', 'blogs')


@blueprint.route('', endpoint='blog')
class BlogListAPI(MethodView):
    @jwt_required
    @blueprint.response(BlogSchema)
    @blueprint.arguments(BlogSchema)
    def post(self, args):
        """Create blog post"""
        blog = Blog(**args)
        user_id = get_jwt_identity()
        try:
            user = User.get(id=user_id)
        except User.DoesNotExist:
            abort(404, message='User not found')
        blog.author = user
        blog.save()
        return blog
