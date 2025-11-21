import pytest

from app import app  # Import your Flask app
from faker import Faker

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def fake_email():
    """Generates a realistic fake email address using Faker."""
    fake = Faker()
    return fake.email()

def test_signup_form(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    # assert b'Welcome' in response.data  # Adjust to match your content


def test_signup(client, fake_email):
    print(fake_email)
    response = client.post('/signup', data={
        "email": fake_email,
        "password": "password123"
    }, follow_redirects=False)

    # ASSERTIONS

    # Verify user was created
    from app import User
    user = User.query.filter_by(email=fake_email).first()
    assert user is not None

    # CHECK THAT IT IS A REDIRECT
    assert response.status_code == 302
    # Check that the second request was to the index page.
    assert response.location == '/articles'

def test_login_form(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    # assert b'Welcome' in response.data  # Adjust to match your content


def test_login(client): 
    with app.app_context():
        from app import User
        user = User.query.filter_by(email="test@twelve.com").first()

        response = client.post('/login', data={
            "email": user.email,
            "password": "password123"
        }, follow_redirects=False)

        # ASSERTIONS

        # Verify user was created
        # from app import User
        # user = User.query.filter_by(email=fake_email).first()
        # assert user is not None

        assert 'Set-Cookie' in response.headers
        assert 'session' in response.headers['Set-Cookie']

        # CHECK THAT IT IS A REDIRECT
        assert response.status_code == 302
        # Check that the second request was to the index page.
        assert response.location == '/articles'


# def test_logout(client):



