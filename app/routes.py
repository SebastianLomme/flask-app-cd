from logging import captureWarnings
from flask import render_template, url_for, flash, redirect, request, Blueprint
from wtforms.validators import Email
from app.models import User
from app.forms import RegistrationForm, LoginForm
from app import bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint("main", __name__,  template_folder='templates')

@main.route("/")
def home():
    return render_template("home.html", title="homepage")


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", title="register", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password ,form.password.data):
            flash(f"Welcome {user.username} you are succesvul logged in!", "success")
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login unsuccessfull. Please check email and password", "danger")

    return render_template("login.html", title="login", form=form)


@main.route("/about")
def about():
    return render_template("about.html")

@main.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@main.route("/logout")
def logout():
    logout_user()
    flash("Successfull logout.",  "success")
    return redirect(url_for("main.home"))

@main.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")