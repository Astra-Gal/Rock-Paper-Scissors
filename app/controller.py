from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', font_url='https://fonts.googleapis.com/css2?family=Codystar&display=swap" rel="stylesheet')