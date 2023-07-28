from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/home')
def home():
    return render_template("home.html")