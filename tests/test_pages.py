# RUN TESTS
# source myenv/bin/activate (venv/bin/activate)
# pip3 install pytest
# create 'tests' folder
# create test_app.py
# python3 -m pytest tests/

import pytest

from app import app  # Import your Flask app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    # assert b'Welcome' in response.data  # Adjust to match your content







# def inc(x):
#     return x + 1

# def dec(x):
#     return x - 1

# def test_inc():
#     assert inc(3) == 4

# def test_dec():
#     assert dec(3) == 2


# Fuctional Testing - Integrative Testing - Route Testing - End-to-End testing (controller level)

# "Test Coverage"
# 15 routes
# 10 functional tests - 2/3 test coverage 65% test coverage

# unit testing (model level)
    # critical business logic (that is a little complex - risky)
    # e.g. build a polygon around a capital city based on the population density of the city

# UI Testing - Behavioral Testing (view level)
    # critical UI behavior (that is a little complex - risky)
    # when a song is playing, its title is visible






