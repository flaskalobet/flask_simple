from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    #return "<h1>Hello World!!!</h1>"
    return render_template('index.html')
