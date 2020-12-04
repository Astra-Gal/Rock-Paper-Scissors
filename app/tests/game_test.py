import unittest
from app.models.player import *
from app.models.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player ("Rocky Balboa", "Rock")
        self.player2 = Player("Paper Balboa", "Paper")
        self.player3 = Player("Scissors Balboa", "Scissors")
        self.player4 = Player("Chippy Balboa", "Rock")
        self.player5 = Player("Rippy Balboa", "Paper")
        self.player6 = Player("Snippy Balboa", "Scissors")

# rock tests

    def test_rock_beats_scissors(self):
        result = play_rps(self.player1, self.player3)
        self.assertEqual(self.player1, result)

    def test_rock_loses_to_paper(self):
        result = play_rps(self.player1, self.player2)
        self.assertEqual(self.player2, result)

# paper tests

    def test_paper_beats_rock(self):
        result = play_rps(self.player2, self.player1)
        self.assertEqual(self.player2, result)

    def test_paper_loses_to_scissors(self):
        result = play_rps(self.player2, self.player3)
        self.assertEqual(self.player3, result)

# scissors tests

    def test_scissors_beats_paper(self):
        result = play_rps(self.player3, self.player2)
        self.assertEqual(self.player3, result)

    def test_scissors_loses_to_rock(self):
        result = play_rps(self.player3, self.player1)
        self.assertEqual(self.player1, result)

#draw tests

    def test_rock_rock_draws(self):
        result = play_rps(self.player1, self.player4)
        self.assertEqual(None, result)

    def test_paper_paper_draws(self):
        result = play_rps(self.player2, self.player5)
        self.assertEqual(None, result)

    def test_scissors_scissors_draws(self):
        result = play_rps(self.player3, self.player6)
        self.assertEqual(None, result)
