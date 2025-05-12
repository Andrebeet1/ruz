from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import db
from models import Post

# Blueprint pour la page d'accueil et autres vues principales
main_bp = Blueprint('main', __name__)

# Route pour la page d'accueil avec le fil d'actualités
@main_bp.route('/')
@login_required
def home():
    # Récupérer les posts récents (affichage du fil d'actualités)
    posts = Post.query.order_by(Post.timestamp.desc()).all()  # Tri des posts par date décroissante
    return render_template('home.html', posts=posts)

# Route pour afficher le profil de l'utilisateur
@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
