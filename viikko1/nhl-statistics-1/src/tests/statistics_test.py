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
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    """
    def test_init_toimii_oikein(self):
        self.assertEqual(self.statistics._players, [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ])
    """
    """
    def test_toimii_oikein__init__(self, reader):
        self._reader = reader

        self._players = self._reader.get_players()
    """

    def test_search(self):
        name = "Kurri"

        self.assertEqual(self.statistics.search(name).__str__(), "Kurri EDM 37 + 53 = 90")
        # f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

    def test_search_kun_pelaaja_ei_loydy(self):
        name = "Kuri"

        self.assertEqual(self.statistics.search(name), None)

    def test_team(self):
        team = "PIT"
        #pop? listan eka ulos miten?
        self.assertEqual(self.statistics.team(team).pop().__str__(), "Lemieux PIT 45 + 54 = 99")
    """
    def test_top(self):
        self.assertEqual(self.statistics.top(3)[1].__str__(), "Lemieux PIT 45 + 54 = 99")
    """

    def test_top_goals(self):
        self.assertEqual(self.statistics.top(3, "SortBy.GOALS")[0].__str__(), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_assists(self):
        self.assertEqual(self.statistics.top(3, "SortBy.ASSISTS")[0].__str__(), "Gretzky EDM 35 + 89 = 124")
    
    def test_top_points(self):
        self.assertEqual(self.statistics.top(3, "")[0].__str__(), "Gretzky EDM 35 + 89 = 124")
    