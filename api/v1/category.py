from flask_restful import Resource, reqparse
from models import Category, Book
from config import db


class CategoryAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name is a string')

    def get(self):
        categories = Category.query.all()
        # all_books = Book.query.all()

        # category_all = [{
        #     "id": "0",
        #     "name": "All Books",
        #     "books": [b.to_dict() for b in all_books]
        # }]

        res = [c.to_dict() for c in categories]
        # res = category_all + res
        return {'categories': res}

    def post(self):
        args = self.parser.parse_args()
        db.session.add(Category(name=args.name))
        db.session.commit()
        return {'name': args.name}
