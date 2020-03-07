from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from config import db


class Category(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='category', lazy=True)


class Book(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(120), unique=True, nullable=False)
    thumbnail_url = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)
    stock = db.Column(db.String(120), unique=True, nullable=False)
    product_description = db.Column(db.String(120), unique=True, nullable=False)
    upc = db.Column(db.String(120), unique=True, nullable=False)
