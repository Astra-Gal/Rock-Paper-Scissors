from app.models.player import Player


def play_rps(player1, player2):
    if player1.choice == "Rock" and player2.choice == "Scissors":
        return player1

    if player1.choice == "Rock" and player2.choice == "Paper":
        return player2