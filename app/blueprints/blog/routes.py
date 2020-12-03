from flask import jsonify, request
from .models import BlogPost
from . import blog_bp


@blog_bp.route("/posts", methods=['GET'])
def show_all_blog_posts():
    """Output all of the blog posts."""
    return jsonify([post.to_dict() for post in BlogPost.query.all()])

@blog_bp.route("/posts/<int:id>", methods=['GET'])
def show_one_blog_post(id):
    """Output one specific blog post."""
    post = BlogPost.query.get(id)
    return jsonify(post.to_dict())
