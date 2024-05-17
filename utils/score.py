import datetime
class Score:
    def __init__(self, username, game_id):
        self.username = username
        self.game_id = game_id
        self.points = 0
        self.wins = 0
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f'Username: {self.username}, Game ID: {self.game_id}, Points: {self.points}, Wins: {self.wins}, Achieved on: {self.timestamp}'

    def add_points(self, points):
        self.points += points

    def add_win(self):
        self.wins += 1
