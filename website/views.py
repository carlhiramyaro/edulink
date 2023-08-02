from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader
from .fetch_books import fetch_books_data

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/subject')
def subject():
    return render_template("subject.html")

@views.route('/math')
def math():
    math_books_data = fetch_books_data("Mathematics")
    return render_template('math.html', subject='Math', books=math_books_data)


@views.route('/science')
def science():
    science_books_data = fetch_books_data("Science")
    return render_template('science.html', subject='Science', books=science_books_data)


@views.route('/history')
def history():
    history_books_data = fetch_books_data("History")
    return render_template('history.html', subject='History', books=history_books_data)
