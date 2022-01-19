from app.models import User

def test_new_user():
    user = User(username="John Dow", email="johndow@gmail.com", password="password")
    assert user.email == "johndow@gmail.com"
    assert user.username == "John Dow"
    assert user.password == "password"

