"""
May 24 2019
cardinalion
"""

from flask import Flask

from bbs.extensions import db, csrf, ckeditor, toolbar
from bbs.models import User, Category
from bbs.fakes import first_admin, some_categories

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG','development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_shell_context(app)
    register_template_context(app)

    return app

def register_extensions(app):
    db.init_app(app)
    initilize_db()

    ckeditor.init_app(app)

def register_blueprints(app):
    app.register_blueprint()
    pass

def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)

def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = User.query.first()
        categories = Category.query.order_by(Category.id).all()
        return dict(admin=admin, categories=categories)

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

def initilize_db():
    db.drop_all()
    db.create_all()
    first_admin()
    some_categories()

