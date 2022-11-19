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

    def get_points(self):
        return self.goals + self.assists
    """
    def __str__(self):
        return self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
    """
    """
    def __str__(self):
        return f"{self.name:20}" + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
    """
    def __str__(self):
        return f"{self.name:20}" + self.team + " " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.goals + self.assists)

    