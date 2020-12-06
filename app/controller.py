from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/play/<player1>/<player2>')
# def play(player1, player2):
#     return f"The winner is {play_rps(player1, player2)}"

@app.route('/play-game', methods=['POST'])
def play_game():
    name1 = request.form['player1-name']
    name2 = request.form['player2-name']
    choice1 = request.form['player1-choice']
    choice2 = request.form['player2-choice']
    player1 = Player(name1, choice1)
    player2 = Player(name2, choice2)
    game = Game(player1, player1)
    # return f"{play_rps(player1, player2)} wins!"
    return f"{game.check_winner(player1, player2).name} wins!"


       

# next step: include their weapon of choice in the string!