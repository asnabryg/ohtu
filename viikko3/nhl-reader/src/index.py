import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games'],
        )

        players.append(player)

    print("Players from FIN")
    fin_players = [player for player in players if player.nationality == "FIN"]
    fin_players.sort(
        key=lambda x: (x.goals + x.assists), reverse=True)
    for player in fin_players:
        print(player)


if __name__ == "__main__":
    main()
