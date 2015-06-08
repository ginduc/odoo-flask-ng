from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


class Recipient(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    mobileNo = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(self, firstname, lastname, mobileNo, address):
        self.firstname = firstname
        self.lastname = lastname
        self.mobileNo = mobileNo
        self.address = address

    def __repr__(self):
        return '<Recipient Name: %s %s>' % (self.firstname, self.lastname)

class Sender(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
