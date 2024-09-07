from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('E-Posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    submit = SubmitField('Giriş')

class RegistrationForm(FlaskForm):
    email = StringField('E-Posta', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    confirm_password = PasswordField('Şifreyi Onayla', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Kaydı Tamamla')
class PostForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired()])
    content = TextAreaField('İçerik', validators=[DataRequired()])
    submit = SubmitField('Gönder')

class CommentForm(FlaskForm):
    content = TextAreaField('Yorum', validators=[DataRequired()])
    post_id = HiddenField('Post ID', validators=[DataRequired()])
    submit = SubmitField('Gönder')

class ReactionForm(FlaskForm):
    reaction_type = SelectField('Reaction Type', choices=[
        ('like', 'Beğenme'),
        ('funny', 'Saçma Bulma'),
        ('useful', 'Olsa Kullanırdım'),
        ('wish', 'Geliştiricileri Arasında Olmak İsterdim')
    ], validators=[DataRequired()])
    post_id = HiddenField('Post ID', validators=[DataRequired()])
    submit = SubmitField('Add Reaction')
