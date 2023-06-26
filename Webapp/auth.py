from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('You are logged in now!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.ApplicationPart1'))
            else:
                flash('Incorrect password. Please try again!', category='error')
        else:
            flash('User account does not exist. Please sign up first.', category='error')
            
    return render_template("logInPage.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')    
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email is already in use.',category='error')
        elif len(name) < 3:
            flash('Name must be greater than 2 characters.', category='error')
        elif len(email) < 8:
            flash('Email must be greater than 7 characters.', category='error')
        elif '@' not in email:
            flash('Invalid email', category='error') 
        elif len(password) < 4:
            flash('Password must be greater than 3 characters.', category='error')
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('You are signed up now!', category='success')
            return redirect(url_for('views.ApplicationPart1'))
        
    return render_template("signUpPage.html", user=current_user)





