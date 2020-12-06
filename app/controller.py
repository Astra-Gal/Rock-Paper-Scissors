from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')


# this returns an f string to the browser with the name and choice of the victor
@app.route('/play-game', methods=['POST'])
def play_game():
    name1 = request.form['player1-name']
    name2 = request.form['player2-name']
    choice1 = request.form['player1-choice']
    choice2 = request.form['player2-choice']
    player1 = Player(name1, choice1)
    player2 = Player(name2, choice2)
    game = Game(player1, player1)
    result = play_rps(player1, player2)
    if result != None:
        return render_template('display_result.html', result=result)
        # return f"{result.name} wins with {result.choice.lower()}!"
    else:
        return render_template('draw.html')
