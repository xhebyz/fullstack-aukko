from sqlalchemy_serializer import SerializerMixin
from config import db


class Category(db.Model, SerializerMixin):
    serialize_rules = ('-books.category',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='category', lazy=True)


class Book(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    thumbnail_url = db.Column(db.String(120), unique=False, nullable=True)
    price = db.Column(db.String(120), unique=False, nullable=True)
    stock = db.Column(db.Boolean, unique=False, nullable=True)
    product_description = db.Column(db.String(120), unique=False, nullable=True)
    upc = db.Column(db.String(120), unique=False, nullable=True)
