class Player:
    """
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    """

    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def get_nationality(self):
        return self.nationality
    
    def __str__(self):
        return self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)