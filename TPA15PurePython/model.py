from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gr007,,@localhost/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()



    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), nullable=False)
    hostname = db.Column(db.String(150), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

