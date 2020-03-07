from flask import Blueprint, render_template, jsonify
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from models import Category, Book
from config import db

resource_fields = {
    'name': fields.String,
}


class CategoryAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name is a string')

    def get(self):
        categories = Category.query.all()
        res = [c.to_dict() for c in categories]
        return {'categories': res}

    def post(self):
        args = self.parser.parse_args()
        db.session.add(Category(name=args.name))
        db.session.commit()
        return {'name': args.name}


class BooksAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Rate to charge for this resource')
    parser.add_argument('category_id', type=int, help='category_id is a key of category of books')
    parser.add_argument('title', type=str, help='Rate to charge for this resource')
    parser.add_argument('thumbnail_url', type=str, help='Rate to charge for this resource')
    parser.add_argument('stock', type=bool, help='Rate to charge for this resource')
    parser.add_argument('product_description', type=str, help='Rate to charge for this resource')
    parser.add_argument('upc', type=str, help='Rate to charge for this resource')

    def get(self):
        categories = Book.query.all()
        res = [c.to_dict() for c in categories]
        return {'books': res}

    def post(self):
        args = self.parser.parse_args()
        db.session.add(Book(
            category_id=args.category_id,
            title=args.title,
            thumbnail_url=args.thumbnail_url,
            stock=args.stock,
            product_description=args.product_description,
            upc=args.upc
        ))
        db.session.commit()
        return {'title': args.title}


class BasicAPI(Resource):
    def get(self):
        return jsonify(
            {'header': 'Hello World!!!!!!!', 'body': 'Called by react from the flask API.',
             'tag': 'Now with Materiaul UI'})