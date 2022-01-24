def test_config(app):
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite://"

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "This is the home page!" in response.data.decode('utf-8')

def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert "This is the about page!" in response.data.decode('utf-8')

