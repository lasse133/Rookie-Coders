from flask import Blueprint, render_template, request, flash
from .models import User
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

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

        if len(name) < 3:
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
            pass
    return render_template("signUpPage.html")





