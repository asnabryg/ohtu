import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_constructor_creates_players_list(self):
        self.assertEqual(self.stats._players[0].name, "Semenko")
        self.assertEqual(self.stats._players[1].name, "Lemieux")
        self.assertEqual(self.stats._players[2].name, "Kurri")
        self.assertEqual(self.stats._players[3].name, "Yzerman")
        self.assertEqual(self.stats._players[4].name, "Gretzky")
    
    def test_search_returns_correct_player(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")
    
    def test_search_returns_none(self):
        self.assertEqual(self.stats.search("Selänne"), None)
    
    def test_get_players_of_team(self):
        players = self.stats.team("EDM")
        for player in players:
            self.assertEqual(player.team, "EDM")

    def test_top(self):
        players = self.stats.top(4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")
        self.assertEqual(players[4].name, "Semenko")
