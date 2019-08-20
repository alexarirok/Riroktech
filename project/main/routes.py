from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html', title='About')
