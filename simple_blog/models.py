from . import db,login_manager
from flask_login import UserMixin



class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(200),nullable=False,unique=True)
    email=db.Column(db.String(40),nullable=False)
    password_hash=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


