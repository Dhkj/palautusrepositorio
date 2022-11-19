from player import Player

def sort_by_points(player):
        return player.get_points()

class PlayerStats:
    """
    def sort_by_points(player):
        return player.get_points()
    """
    """
    def __init__(self, players):
        self.players = players
    """
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        response = self.reader.get_players()

        players = []

        for player_dict in response:
            if player_dict['nationality'] == nationality:
                player = Player(
                    player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
                )

                players.append(player)

        players = sorted(players, reverse=True, key = sort_by_points)

        return players





        """
        for player in players:
            if player.get_nationality() == "FIN":
                players2.append(player)

                for player_dict in response:
            player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )

            players.append(player)

        return players
        """