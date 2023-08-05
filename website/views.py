from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader
from .fetch_youtube import fetch_youtube_data

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
    math_youtube_data = fetch_youtube_data("Mathematics")
    return render_template('math.html', subject='Math', youtube=math_youtube_data)


@views.route('/science')
def science():
    science_youtube_data = fetch_youtube_data("Science")
    return render_template('science.html', subject='Science', youtube=science_youtube_data)


@views.route('/history')
def history():
    history_youtube_data = fetch_youtube_data("History")
    return render_template('history.html', subject='History', youtube=history_youtube_data)
