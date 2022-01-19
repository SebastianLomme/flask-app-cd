from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "6887c8ea17d1ed72306e37708f21e55c"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from app import routes

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
