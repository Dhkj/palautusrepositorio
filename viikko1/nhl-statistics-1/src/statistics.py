# from player_reader import PlayerReader


def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists


class Statistics:
    """
    def __init__(self):
        reader = PlayerReader()

        self._players = reader.get_players()
    """
    def __init__(self, reader):
        self._reader = reader

        self._players = self._reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)
    """
    def top(self, how_many):
        #self?
        #return self.top(self, how_many, "")
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
    """
    def top(self, how_many, enum):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )
        """
        if enum == 1:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
            )
        """
        #
        #print(enum)
        #
        #if enum == 2:
        if str(enum) == "SortBy.GOALS":
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_goals
            )
        #elif enum == 3:
        elif str(enum) == "SortBy.ASSISTS":
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_assists
            )
        
        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result