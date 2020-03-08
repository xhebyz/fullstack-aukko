from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_webpackext import FlaskWebpackExt

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)
FlaskWebpackExt(app)