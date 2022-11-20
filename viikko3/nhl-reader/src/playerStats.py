class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players = [
            player for player in all_players if player.nationality == nationality]
        players.sort(
            key=lambda x: (x.goals + x.assists), reverse=True)
        return players
