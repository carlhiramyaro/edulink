from flask import Blueprint, render_template, request, flash, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #library to hash passwords
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
     if request.method == 'POST':
         email =request.form.get('email')
         password =request.form.get('password')

         user = User.query.filter_by(email=email).first()
         if user:
             if check_password_hash(user.password, password):
                 flash('Logged in successfully!', category='success')
                 return redirect(url_for('views.subject'))
             else:
                 flash("Incorrect Password, try again", category='error')
         else:
             flash('Email does not Exist')
                
     
     return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up',  methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')
        age = request.form.get('age')
        print("success:", email)

        #Error handling, Dont forget to implement the flashes later
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif not email or len(email) < 4:
            flash("Invalid Email", category="error")
        elif not name or len(name) < 2:
            flash("Invalid name", category="error")
        elif not password or len(password) < 4:
            flash("Password is too short", category="error")
        elif password != confirmpassword:
            flash("Passwords do not match", category="error")
        elif not age or len(age) < 1:
            flash("Please enter age", category="error")
        else:
            new_user = User(email=email, name=name, age=age, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash(" Account created!", category="success")
            return redirect(url_for('auth.login'))
        
    return render_template("index.html")