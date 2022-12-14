from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        # self._matcher = All()
        self._matcher = matcher

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
        #return QueryBuilder(HasAtLeast(value, attr))
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
        #return QueryBuilder(PlaysIn(team))
        ##self._matcher = PlaysIn(team)
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
 
    
    def build(self):
        return self._matcher

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").build()
    matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()


    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
    )

    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
    )

    matcher = query.oneOf(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)
"""
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

    
    #print("")

    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))
    """

if __name__ == "__main__":
    main()

