from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from bbs.extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    motto = db.Column(db.Text)

    posts = db.relationship('Posts', back_populates='author')
    comments = db.relationship('Comments', back_populates='author')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 头像，积分


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    subcategories = db.relationship('Subcategory', back_populates='category')
    # posts = db.relationship('Post', back_populates='category')


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='subcategories')
    posts = db.relationship('Post', back_populates='subcategory')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # category = db.relationship('Category', back_populates='posts')
    subcategory = db.relationship('Subcategory', back_populates='posts')
    author = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    author = db.relationship('User', back_populates='comments')
    post = db.relationship('Post', back_populates='comments')
    replies = db.relationship('Comment', backref=db.backref('replied', remote_side=[id]), cascade='all,delete-orphan')




