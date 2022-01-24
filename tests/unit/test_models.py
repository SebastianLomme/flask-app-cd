from flask_login import current_user
from app.forms import RegistrationForm
from app.models import User, db
from flask import request




def test_new_user(new_user):
    assert new_user.email == "johndow@gmail.com"
    assert new_user.username == "John Dow"
    assert new_user.password == "12345678"

def test_validation_username(new_user):
    user = User(username="John Dow", email="johndow@gmail.com", password="12345678")
    assert user == new_user



def test_register_user(app):
    with app.test_client() as client:
        url = "/register"
        form = {
            'username': 'Peter Pannekoek',
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            'confirm_password': '12345678',
            'submit' : 'Sign up',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        print(response.data.decode('utf-8'))
        assert "This is the home page!" in response.data.decode("utf-8")
        assert "Account created for Peter Pannekoek" in response.data.decode("utf-8")

def test_db_peter(app):
    assert User.query.filter_by(username="Peter Pannekoek").first().username == "Peter Pannekoek"

def test_login(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        assert "This is the home page!" in response.data.decode("utf-8")
        assert "Welcome Peter Pannekoek you are succesvul logged in!" in response.data.decode("utf-8")


def test_already_logged_in_redirect_login_page(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        assert "This is the home page!" in response.data.decode("utf-8")
        assert "Welcome Peter Pannekoek you are succesvul logged in!" in response.data.decode("utf-8")
        response = client.get(url, follow_redirects=True)
        assert "This is the home page" in response.data.decode("utf-8")


def test_already_logged_in_redirect_register_page(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        assert "This is the home page!" in response.data.decode("utf-8")
        assert "Welcome Peter Pannekoek you are succesvul logged in!" in response.data.decode("utf-8")
        response = client.get("/register", follow_redirects=True)
        assert "This is the home page" in response.data.decode("utf-8")



def test_login_wrong_password(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '00000000',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        assert "Login unsuccessfull. Please check email and password" in response.data.decode("utf-8")

def test_logout(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        assert current_user.is_authenticated == True
        response = client.get("/logout", follow_redirects=True)
        assert current_user.is_authenticated == False
        assert "Successfull logout" in response.data.decode("utf-8")

def test_db(app, new_user):
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    assert new_user.username == "John Dow"
    assert User.query.filter_by(username="John Dow").first().username == "John Dow"

def test_db_two(app):
    assert User.query.filter_by(username="John Dow").first().username == "John Dow"

def test_account_already_exists(app):
    with app.test_client() as client:
        url = "/register"
        form = {
            'username': 'Peter Pannekoek',
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            'confirm_password': '12345678',
            'submit' : 'Sign up',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        print(response.data.decode('utf-8'))
        assert "That email has a account, Please Login" in response.data.decode("utf-8")
        assert "That username is taken. Please choose a nother one" in response.data.decode("utf-8")

def test_account_page_not_logedin(app):
    with app.test_client() as client:
        url = "/account"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.get(url, follow_redirects=True)
        assert response.status_code == 200
        assert "Please log in to access this page." in response.data.decode("utf-8")


def test_account_page_logedin(app):
    with app.test_client() as client:
        url = "/login"
        form = {
            'email' : "peterpannekoek@gmail.com",
            'password': '12345678',
            }
        response = client.post(url, data=form, follow_redirects=True)
        assert response.status_code == 200
        response = client.get("/account", follow_redirects=True)
        assert "Account Peter Pannekoek!" in response.data.decode("utf-8")