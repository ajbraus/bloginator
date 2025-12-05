import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager

from models import db, bcrypt
from models.user import User
from models.article import Article

from blueprints.pages import pages
from blueprints.auth import auth
from blueprints.articles import articles

# APP
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# INIT DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt.init_app(app)

# FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login page if not authenticated
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# LOAD USER
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# BLUEPRINTS
app.register_blueprint(pages)
app.register_blueprint(auth)
app.register_blueprint(articles)

# CREATE TABLES
with app.app_context():
    db.create_all()
    print("Database tables created.")

if __name__ == '__main__':
    app.run(debug=True)
