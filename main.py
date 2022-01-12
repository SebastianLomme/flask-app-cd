from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "6887c8ea17d1ed72306e37708f21e55c"

@app.route("/")
def home():
    return render_template("home.html", title="homepage")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form )


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)


@app.route("/about")
def about():
    return render_template("about.html")

def plus(num1, num2):
    return num1 + num2 

if __name__ == "__main__":
    app.run(debug=True)

