from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "6887c8ea17d1ed72306e37708f21e55c"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
from app import routes
