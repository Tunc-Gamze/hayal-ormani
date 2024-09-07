from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import PostForm, LoginForm, RegistrationForm, CommentForm, ReactionForm
from app.models import Post, Comment, Reaction

bp = Blueprint('main', __name__)

@bp.route('/home')
def home():
    return "Merhaba Ormancı"

@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    
    if request.method == 'POST':
        post_id = request.form.get('post_id')
        comment_text = request.form.get('comment')
        reaction_type = request.form.get('reaction')

        if comment_text:
            comment = Comment(content=comment_text, user_id=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            flash('Yorum başarıyla eklendi!', 'success')
        elif reaction_type:
            reaction = Reaction(type=reaction_type, user_id=current_user.id, post_id=post_id)
            db.session.add(reaction)
            db.session.commit()
            flash('Reaksiyon başarıyla verildi!', 'success')

        return redirect(url_for('main.index'))

    return render_template('index.html', posts=posts)

@bp.route('/about')
def about():
    return "Bu, hakkında sayfanızdır."

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        flash('Login successful for email: {}'.format(email))
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        flash('Registration successful for email: {}'.format(email))
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)

@bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = ReactionForm()
    if form.validate_on_submit():
        reaction = Reaction(
            type=form.reaction_type.data,
            post_id=post.id
        )
        db.session.add(reaction)
        db.session.commit()
        return redirect(url_for('main.post_detail', post_id=post.id))
    
    reactions = Reaction.query.filter_by(post_id=post.id).all()
    return render_template('post_detail.html', post=post, form=form, reactions=reactions)

@bp.route('/submit', methods=['GET', 'POST'])
def submit():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('submit.html', form=form)

@bp.route('/add_reaction/<int:post_id>', methods=['POST'])
def add_reaction(post_id):
    form = ReactionForm()
    if form.validate_on_submit():
        reaction = Reaction(type=form.reaction_type.data, post_id=post_id)
        db.session.add(reaction)
        db.session.commit()
        flash('Reaksiyon eklendi!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Yorum eklendi!', 'success')
        return redirect(url_for('main.index'))
