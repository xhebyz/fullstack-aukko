from flask_restful import Resource, reqparse
from models import Category, Book
from config import db
from load import load_data


class CategoryAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name is a string')

    def get(self):
        load_data()
        categories = Category.query.all()
        res = [c.to_dict() for c in categories]
        return {'categories': res}

    def post(self):
        args = self.parser.parse_args()
        db.session.add(Category(name=args.name))
        db.session.commit()
        return {'name': args.name}