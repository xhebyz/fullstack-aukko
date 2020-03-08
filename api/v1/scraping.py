from flask_restful import Resource, reqparse
from utils import book_scraping


class ScrapingAPI(Resource):

    def get(self):
        book_scraping.launch_scraping()
        return {'status': True}
