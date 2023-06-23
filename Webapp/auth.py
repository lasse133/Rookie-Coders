from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import check_password
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password(user.password, password):
                flash('You are logged in now', category='success')
            else:
                flash('Incorrect password. Please try again!', category='error')
        else:
            flash('User account does not exist. Please sign up first.', category='error')

        if len(email) < 8:
            flash('Email must be greater than 7 characters.', category='error')
        elif '@' not in email:
            flash('Invalid email', category='error') 
        elif len(password) < 4:
            flash('Password must be greater than 3 characters.', category='error')
        else:
            flash('You are logged in now!', category='success')
            pass
    return render_template("logInPage.html", text="Testing")

@auth.route('/logout')
def logout():
    return "<p> logout</p>"

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
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('You are signed up now!', category='success')
            return redirect(url_for('views.ApplicationPart1'))
        
    return render_template("signUpPage.html")





