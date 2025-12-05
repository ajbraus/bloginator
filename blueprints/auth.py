from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from models import db
from models.user import User

auth = Blueprint("auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    # Basic validation
    if not email or not password:
        flash('Please fill in all fields', 'error')
        return render_template('signup.html')
    
    if len(password) < 6:
        flash('Password must be at least 6 characters long', 'error')
        return render_template('signup.html')

    user = User(email=email)
    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()

    flash('Account created successfully!', 'success')
    return redirect(url_for('articles.index'))

  else: # GET request
    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login(): 
  # Redirect if already logged in
  if current_user.is_authenticated:
    return redirect(url_for('articles.index'))
  
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember', False)  # Remember me checkbox
    
    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
      login_user(user, remember=remember)
      flash('Login successful!', 'success')
      
      # Redirect to next page or home
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('articles.index'))
    else:
      return render_template('login.html')
      flash('Invalid email or password', 'error')

  return render_template('login.html')


@auth.route('/logut', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('You have been logged out.', 'info')
  return redirect(url_for('pages.home'))