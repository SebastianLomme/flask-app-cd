from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "6887c8ea17d1ed72306e37708f21e55c"


@app.route("/")
def home():
    return render_template("home.html", title="homepage")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Succesvul logged in Welcome {form.email.data}", "success")
        return redirect(url_for("home"))
    return render_template("login.html", title="login", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


def plus(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    app.run(debug=True)
