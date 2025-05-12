from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login_manager

# Modèle pour l'utilisateur
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    likes = db.relationship('Like', backref='user', lazy='dynamic')

# Fonction pour charger un utilisateur par ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Modèle pour un post (un "ruz")
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)  # Contenu du post
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Date de création du post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Lien vers l'utilisateur qui a posté
    comments = db.relationship('Comment', backref='post', lazy='dynamic')  # Lien vers les commentaires
    likes = db.relationship('Like', backref='post', lazy='dynamic')  # Lien vers les likes

# Modèle pour un commentaire
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)  # Contenu du commentaire
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Date du commentaire
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Lien vers l'utilisateur qui a commenté
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))  # Lien vers le post auquel le commentaire appartient

# Modèle pour un like
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Lien vers l'utilisateur qui a aimé
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))  # Lien vers le post qui a été aimé
