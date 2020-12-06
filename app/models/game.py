from app.models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def check_winner(self, player1, player2):
        return player1


def play_rps(player1, player2):
    if player1.choice == "Rock" and player2.choice == "Scissors":
        winner = player1
        return winner

    if player1.choice == "Rock" and player2.choice == "Paper":
        winner = player2
        return winner

    if player1.choice == "Paper" and player2.choice == "Scissors":
        winner = player2
        return winner

    if player1.choice == "Paper" and player2.choice == "Rock":
        winner = player1
        return winner

    if player1.choice == "Scissors" and player2.choice == "Rock":
        winner = player2
        return player2

    if player1.choice == "Scissors" and player2.choice == "Paper":
        winner = player1
        return winner

    # can I get away with just one return statement at the end?