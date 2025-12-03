import pytest

from app import app  # Import your Flask app
from faker import Faker

# FIXTURES
@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def authenticated_client(client):
    login_response = client.post(
        "/login",
        data={"email": "test@twelve.com", "password": "password123"},
        follow_redirects=True
    )
    return client

# TESTS
# INDEX
def test_articles_index_not_logged_in(client):
    response = client.get('/articles')
    assert response.status_code == 302
    assert response.location == '/login?next=%2Farticles'

def test_articles_index_logged_in(authenticated_client):
    response = authenticated_client.get('/articles')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'

# SHOW
def test_articles_show_not_logged_in(client):
    response = client.get('/articles/1')
    assert response.status_code == 302
    assert response.location == '/login?next=%2Farticles%2F1'

def test_articles_show_logged_in(authenticated_client):
    from app import Article
    a = Article.get_id(1)
    title = a.title
    response = authenticated_client.get('/articles/1')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert title in response.data  

# NEW
# CREATE
# EDIT
# UPDATE
# DESTORY (DELETE)
