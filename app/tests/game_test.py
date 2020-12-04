import unittest
from app.models.player import *
from app.models.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player ("Rocky Balboa", "Rock")
        self.player2 = Player("Paper Balboa", "Paper")
        self.player3 = Player("Scissors Balboa", "Scissors")

# rock tests

    def test_rock_beats_scissors(self):
        result = play_rps(self.player1, self.player3)
        self.assertEqual(self.player1, result)

    def test_rock_loses_to_paper(self):
        result = play_rps(self.player1, self.player2)
        self.assertEqual(self.player2, result)
