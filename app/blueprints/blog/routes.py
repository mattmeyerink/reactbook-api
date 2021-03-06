from flask import jsonify, request
from .models import BlogPost
from . import blog_bp
from app.blueprints.authentication.models import User



@blog_bp.route("/posts", methods=['GET'])
def show_all_blog_posts():
    """Output all of the blog posts."""
    posts = [post.to_dict() for post in BlogPost.query.all()]
    return jsonify(posts)

@blog_bp.route("/posts/<int:id>", methods=['GET'])
def show_one_blog_post(id):
    """Output one specific blog post."""
    post = BlogPost.query.get(id)
    return jsonify(post.to_dict())
