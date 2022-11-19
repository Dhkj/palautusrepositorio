from player import Player
import requests
"""
def main():
    pass
"""
def sort_by_points(player):
    return player.get_points()

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()
    """
    print("JSON-muotoinen vastaus:")
    print(response)
    """
    players = []
    """
    for player_dict in response:
        player = Player(
            player_dict['name']
        )

        players.append(player)
    """
    """
    for player_dict in response:
        player = None

        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
        )

        players.append(player)
    """
    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
        )

        players.append(player)
    
    #print("Oliot:")
    """
    for player in players:
        print(player)
    """

    print("Players from FIN:")

    """
    for player in players:
        if player.get_nationality() == "FIN":
            print(player)
    """






    players2 = []

    for player in players:
        if player.get_nationality() == "FIN":
            players2.append(player)

    
    """
    for player in players2:
        print(player)
    """
    """
    for player in filter(player.get_nationality() == "FIN", players):
        print(player)
    """
    for player in sorted(players2, reverse=True, key = sort_by_points):
        print(player)

if __name__ == "__main__":
    main()
