import unittest
from app.models.player import Player
from app.models.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = ("Rocky Balboa", "Rock")
        self.player2 = Player("Paper Balboa", "Paper")
        self.player3 = Player("String Balboa", "String")