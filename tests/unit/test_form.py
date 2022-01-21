from distutils.command.clean import clean
from encodings import utf_8

from flask import current_app
from app.forms import RegistrationForm
from app.models import User
from wtforms_test import FormTestCase
from app import create_app, db
from wtforms.validators import ValidationError
import pytest
import json


# def test_new_user(new_user):
#     assert new_user.email == "johndow@gmail.com"
#     assert new_user.username == "John Dow"
#     assert new_user.password == "12345678"

# def test_username_required(app):
#     user = User(username="John Dow", email="johndow@gmail.com", password="12345678")
#     db.session.add(user)
#     db.session.commit()
#     url = "/login"
#     mock_request_data = {
#         'email' : "johndow@gmail.com",
#         'password': '12345678',
#         'submit' : 'Login',
#     }

    # response = client.post(url, data=mock_request_data, follow_redirects=True)
    # assert "Welcome" in response.data.decode("utf-8")
    # assert response.status_code == 200


# def login(client, username, password):
#     return client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)


# def logout(client):
#     return client.get('/logout', follow_redirects=True)

# def test_login_logout(client):
#     """Make sure login and logout works."""

#     username = "USERNAME"
#     password = "PASSWORD"

#     rv = login(client, username, password)
#     assert b'You were logged in' in rv.data
#     print(rv.data.decode('utf-8'))
#     rv = logout(client)
#     assert b'You were logged out' in rv.data

#     rv = login(client, f"{username}x", password)
#     assert b'Invalid username' in rv.data

#     rv = login(client, username, f'{password}x')
#     assert b'Invalid password' in rv.data