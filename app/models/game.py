from app.models.player import Player


def play_rps(player1, player2):
    if player1.choice == "Rock" and player2.choice == "Scissors":
        return player1

    if player1.choice == "Rock" and player2.choice == "Paper":
        return player2

    if player1.choice == "Paper" and player2.choice == "Scissors":
        return player2

    if player1.choice == "Paper" and player2.choice == "Rock":
        return player1

    if player1.choice == "Scissors" and player2.choice == "Rock":
        return player2

    if player1.choice == "Scissors" and player2.choice == "Paper":
        return player1