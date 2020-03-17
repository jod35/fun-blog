from . import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignUpForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Post, Comment
from flask_admin.contrib.sqla import ModelView
from . import admin

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))


@app.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).limit(5).all()
    context = {
        'posts': posts
    }
    return render_template('index.html', **context)


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():

    form = SignUpForm()
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm = form.confirm.data
        user_exists = User.query.filter_by(username=username).first()
        email_taken = User.query.filter_by(email=email).first()

        if user_exists or email_taken:
            flash("The username or email is already taken")
            return redirect(url_for('sign_up'))

        elif password != confirm:
            flash("Passwords do not match!!")
            return redirect(url_for('sign_up'))
        else:
            new_user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password)
            )
            db.session.add(new_user)
            password_hash = generate_password_hash(password)
            db.session.commit()
            flash("{}, creation of your account has been successful. You can now login.".format(
                username))
            return redirect(url_for('login'))

    context = {
        'form': form
    }
    return render_template('signup.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    prompt = request.form.get('prompt')
    password = request.form.get('password')

    email_exists = User.query.filter_by(email=prompt).first()
    username_exists = User.query.filter_by(username=prompt).first()

    user_exist = email_exists or username_exists

    if not user_exist:
        flash("The account doesnot exists!!")

    if user_exist and check_password_hash(user_exist.password_hash, password):
        login_user(user_exist)
        return redirect(url_for('home_page'))

    context = {
        'form': form
    }
    return render_template('login.html', **context)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home_page():
    posts = Post.query.filter_by(author=current_user)
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)


@app.route('/add', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('post_title')
        content_paragraph1 = request.form.get('post_content')
        content_paragraph2 = request.form.get('post_content2')
        content_paragraph3 = request.form.get('post_content3')

        new_post = Post(
            title=title,
            content_paragraph1=content_paragraph1,
            content_paragraph2=content_paragraph2,
            content_paragraph3=content_paragraph3,
            author=current_user
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Your Post is now live")
        return redirect(url_for('home_page'))
    return render_template('addpost.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    post_to_update = Post.query.get_or_404(id)
    if request.method == 'POST':
        post_to_update.post_title = request.form.get('title')
        post_to_update.content_paragraph1 = request.form.get('post_content')
        post_to_update.content_paragraph2 = request.form.get('post_content2')
        post_to_update.content_paragraph3 = request.form.get('post_content3')
        db.session.commit()
        return redirect(url_for('home_page'))

    context = {
        'post_to_update': post_to_update
    }
    return render_template('update.html', **context)


@app.route('/<string:title>')
def individual_post(title):
    indi_post = Post.query.filter_by(title=title).first()
    context = {
        'indi_post': indi_post
    }
    return render_template('individual_post.html', **context)


@app.route('/delete/<int:id>')
@login_required
def delete_post(id):
    post_to_delet = Post.query.get_or_404(id)
    db.session.delete(post_to_delet)
    return redirect(url_for('home_page'))

@app.route('/comment/<int:id>',methods=['POST'])
@login_required
def add_comment(id):
    comment=request.form.get('comment')
    post=db.query.get(id)
    author=current_user

    new_comment=Comment(comment=comment,post=post,author=author)
    db.session.add(new_comment)
    db.session.commit()
    return redirect('/')

