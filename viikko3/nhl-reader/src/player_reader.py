import requests
from player import Player

class PlayerReader:
    def __init__(self, address):
        self.address = address
    
    def get_players(self):
        return requests.get(self.address).json()
        """
        players = []

        for player_dict in response:
            player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )

            players.append(player)

        return players
        """
