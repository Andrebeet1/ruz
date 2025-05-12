from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialisation des extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation des extensions Flask
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Définit la vue de login pour Flask-Login

    # Enregistrement des blueprints pour séparer les routes
    from routes.auth import auth_bp
    from routes.post import post_bp
    from routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(main_bp)

    # Ajout de Flask-Migrate pour les migrations de base de données
    Migrate(app, db)

    return app
