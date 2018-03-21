from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nzwimqfncgdjsg:ca9b0d4de24ab862ecd584c29790cb85cae795611082c33022535745d9b550e2@ec2-23-21-166-148.compute-1.amazonaws.com:5432/d7jhehmvge3btg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
