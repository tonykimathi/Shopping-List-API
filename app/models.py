from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    user_name = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):

        raise AttributeError('password cannot be accessed.')

    @password.setter
    def password(self, password):

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ShoppingList(db.Model):

    __tablename__ = 'shopping_lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    shopping_list = db.relationship('User', backref='shoppinglist', lazy='dynamic')

    def __repr__(self):
        return '<ShoppingList: {}>'.format(self.name)


class ShoppingListItem(db.Model):

    __tablename__ = 'shopping_list_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    shopping_list_item = db.relationship('User', backref='shoppinglistitem', lazy='dynamic')

    def __repr__(self):
        return '<ShoppingListItem: {}>'.format(self.name)

