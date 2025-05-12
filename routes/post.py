from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models import Post, Comment, Like
from forms import PostForm, CommentForm

# Blueprint pour la gestion des posts
post_bp = Blueprint('post', __name__, url_prefix='/post')

# Route pour publier un post (ruz)
@post_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Créer un nouveau post
        post = Post(body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Votre ruz a été publié!', 'success')
        return redirect(url_for('main.home'))

    return render_template('post.html', form=form)

# Route pour afficher un post et ses commentaires
@post_bp.route('/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(body=comment_form.body.data, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Votre commentaire a été ajouté!', 'success')
        return redirect(url_for('post.post_detail', post_id=post.id))

    comments = post.comments.order_by(Comment.timestamp.desc()).all()
    return render_template('post_detail.html', post=post, comments=comments, comment_form=comment_form)

# Route pour liker un post
@post_bp.route('/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Vérifier si l'utilisateur a déjà aimé ce post
    existing_like = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first()
    if existing_like:
        flash('Vous avez déjà aimé ce post.', 'warning')
    else:
        like = Like(user=current_user, post=post)
        db.session.add(like)
        db.session.commit()
        flash('Vous avez aimé ce post!', 'success')

    return redirect(url_for('post.post_detail', post_id=post.id))
