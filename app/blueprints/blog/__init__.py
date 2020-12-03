import flask


blog_bp = flask.Blueprint("blog", __name__, url_prefix="/blog")

from . import models, routes
