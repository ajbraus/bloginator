from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from models import db
from models.article import Article

articles = Blueprint("articles", __name__)

# ARTICLES#INDEX
@articles.route('/articles', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        # fetch all articles from DB 
        articles = Article.query.all()
        
        # return articles-index template
        return render_template('articles-index.html', articles=articles)

    elif request.method == "POST":
        print('create')
        # instantiate new article
        # save new article
        # url_for('articles.show', id=article.id)

@articles.route('/articles/<int:id>', methods=['GET'])
@login_required
def show(id):
    a = Article.get_id(1)
    
    return render_template('articles-show.html', a=a)

@articles.route('/articles/new', methods=['GET'])
@login_required
def new():
    return render_template('articles-new.html')
