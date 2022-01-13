from flask import render_template, url_for, flash, redirect
from app.models import User
from app.forms import RegistrationForm, LoginForm
from app import app

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
        if form.email.data == "sebastian.lomme@gmail.com" and form.password.data == "password":
            flash(f"Succesvul logged in Welcome {form.email.data}", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessfull. Please check username and password", "danger")

    return render_template("login.html", title="login", form=form)


@app.route("/about")
def about():
    return render_template("about.html")