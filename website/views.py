from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader

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
    return render_template("math.html")

@views.route('/science')
def science():
    return render_template("science.html")

@views.route('/history')
def history():
    return render_template("history.html")