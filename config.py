from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_webpackext import FlaskWebpackExt
import json

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)
FlaskWebpackExt(app)


def load_data():
    from models import Book, Category
    db.create_all()
    count_category = Category.query.count()

    if count_category <= 0:
        data = read_file_json()

        for d in data:
            categories = d.get('categories')
            books = d.get('books')

            for c in categories:
                save_category(c)

            for b in books:
                save_book(b)

        db.session.commit()


def save_category(cat):
    from models import Book, Category

    name = cat.get('name')
    id = cat.get('id')

    db.session.add(Category(
        id=id,
        name=name
    ))


def save_book(book):

    import  logging
    logging.error(book)

    from models import Book, Category
    id = book.get('id')
    category_id = book.get('category_id')
    title = book.get('title')
    thumbnail_url = book.get('thumbnail_url')
    stock = book.get('stock')
    product_description = book.get('product_description')
    price = book.get('price')
    upc = book.get('upc')

    db.session.add(Book(
        id=id,
        category_id=category_id,
        title=title,
        thumbnail_url=thumbnail_url,
        stock=stock,
        product_description=product_description,
        price=price,
        upc=upc
    ))


def read_file_json():
    data = []
    with open('data.json') as f:
        data = json.load(f)
    return data