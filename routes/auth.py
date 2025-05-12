from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import db
from models import User
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint pour l'authentification
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Route pour la page d'inscription
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('L\'email est déjà enregistré.', 'danger')
            return redirect(url_for('auth.register'))
        
        # Créer un nouvel utilisateur
        user = User(username=form.username.data, email=form.email.data,
                    password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        flash('Inscription réussie. Vous pouvez maintenant vous connecter.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

# Route pour la page de connexion
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Connexion réussie!', 'success')
            return redirect(url_for('main.home'))  # Rediriger vers la page d'accueil après connexion
        flash('Email ou mot de passe incorrect', 'danger')

    return render_template('login.html', form=form)

# Route pour la déconnexion
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Déconnexion réussie', 'success')
    return redirect(url_for('main.home'))
