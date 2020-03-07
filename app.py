from flask import render_template, send_from_directory
from api.v1.category import CategoryAPI
from api.v1.book import BooksAPI
from flask_restful import Resource
from config import app, api

api_route = '/api/v1'

app.config.update(
    DEBUG=True,
    WEBPACKEXT_MANIFEST_PATH='/app/webkit-build/manifest.json'
)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(CategoryAPI, api_route + '/categories')
api.add_resource(BooksAPI, api_route + '/books/<int:id>')


@app.route('/dist/<path:path>')
def send_js(path):
    return send_from_directory('webkit-build', path)


#
#
@app.route('/')
@app.route('/<section>')
def home(section="top"):
    return render_template('app.html', section=section)
