from flask import Blueprint, render_template, request, redirect, url_for, flash

pages = Blueprint("pages", __name__)

@pages.route('/')
def home():
    return render_template('index.html')