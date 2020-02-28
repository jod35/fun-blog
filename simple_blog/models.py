from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments=db.relationship('Comment',backref='author',lazy=True)

    def __repr__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content_paragraph1 = db.Column(db.Text(), nullable=True)
    content_paragraph2 = db.Column(db.Text(), nullable=True)
    content_paragraph3 = db.Column(db.Text(), nullable=True)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __str__(self):
        return self.title


class Comment(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    user_id=db.Column(db.Integer(),db.ForeignKey('user.id'))
    post_id=db.Column(db.Integer(),db.ForeignKey('post.id'))
    comment_body=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return "{}".format(self.comment_body)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
