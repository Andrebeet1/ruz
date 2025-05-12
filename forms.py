from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# Formulaire pour la connexion de l'utilisateur
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Formulaire pour l'inscription de l'utilisateur
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

# Formulaire pour publier un post (ruz)
class PostForm(FlaskForm):
    body = TextAreaField('Ruz', validators=[DataRequired(), Length(max=280)])
    submit = SubmitField('Post')

# Formulaire pour commenter un post
class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[DataRequired(), Length(max=280)])
    submit = SubmitField('Comment')
