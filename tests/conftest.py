import pytest
from app import create_app, db
from app.models import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config:
    SECRET_KEY = "6887c8ea17d1ed72306e37708f21e55c"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    EXPLAIN_TEMPLATE_LOADING = True

@pytest.fixture(scope="module")
def new_user():
    user = User(username="John Dow", email="johndow@gmail.com", password="12345678")
    return user


@pytest.fixture(scope="module")
def app():
    app = create_app(Config)
    app.config['template_folder'] = '../templates'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()



@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
