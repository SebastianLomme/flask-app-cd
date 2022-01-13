from flask import render_template, url_for, flash, redirect
from wtforms.validators import Email
from app.models import User
from app.forms import RegistrationForm, LoginForm
from app import app, bcrypt, db

@app.route("/")
def home():
    return render_template("home.html", title="homepage")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if form.email.data == user.email and bcrypt.check_password_hash(user.password ,form.password.data):
            flash(f"Welcome {user.username} you are succesvul logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessfull. Please check username and password", "danger")

    return render_template("login.html", title="login", form=form)


@app.route("/about")
def about():
    return render_template("about.html")