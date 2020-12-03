from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()

def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    cors = CORS(app)

    from .blueprints.authentication import auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.blog import blog_bp
    app.register_blueprint(blog_bp)

    from .blueprints.shop import bp as shop_bp
    app.register_blueprint(shop_bp)

    with app.app_context():
        db.create_all()
        from .import routes


    return app