import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Rocky Balboa", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Rocky Balboa", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player.choice)
