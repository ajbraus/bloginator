from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from wtforms.validators import Length

class ArticleForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=10)])
    body = StringField('body', widget=TextArea())

articles = Blueprint("articles", __name__)

# ARTICLES#INDEX
@articles.route('/articles', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':

        return render_template('articles-index.html')
        # fetch all articles from DB 

        # return articles-index template

    elif request.method == "POST":
        form = ArticleForm()
        if form.validate_on_submit():
            print('create')
            # return redirect('/success')
        # instantiate new article

        # save new article

        # url_for('articles.show', id=article.id)

@articles.route('/articles/<int:id>', methods=['GET'])
@login_required
def show(id):
    from app import Article
    a = Article.get_id(1)
    
    return render_template('articles-show.html', a=a)

@articles.route('/articles/new', methods=['GET'])
@login_required
def new():
    form = ArticleForm()
    return render_template('articles-new.html', form=form)
