class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def handle_even(self, score):
        if score >= 0 and score < len(self.scores):
            return self.scores[score] + "-All"
        return 'Deuce'

    def handle_possible_win(self):
        minus_result = self.player1_score - self. player2_score
        if minus_result == 1:
            return "Advantage player1"
        if minus_result == -1:
            return "Advantage player2"
        if minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def handle_score(self):
        return self.scores[self.player1_score] + "-" + self.scores[self.player2_score]

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.handle_even(self.player1_score)
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.handle_possible_win()
        return self.handle_score()
