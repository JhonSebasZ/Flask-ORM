from flask import Flask
from controllers.UserController import user
from controllers.ProductController import product
from db import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flask_backend'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    migarte = Migrate(app,db)
    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(user)
    app.register_blueprint(product)
    return app
