import os
import time
import random
import uuid
from utils.score import Score  # imports score.py module

class DiceGame:
    def __init__(self, username):
        self.username = username
        self.scores_file = os.path.join('data_folder', 'rankings.txt')
        self.user_score = None  # initiates user_score as None
        self.cpu_score = Score('CPU', 'cpu_game')  # 
        self.create_file()

    def create_file(self):
        folder_path = os.path.dirname(self.scores_file)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if not os.path.exists(self.scores_file):
            with open(self.scores_file, 'w') as file:
                file.write('')

    def load_scores(self):
        scores = []
        if os.path.exists(self.scores_file):
            with open(self.scores_file, 'r') as file:
                for line in file:
                    username, game_id, points, wins, timestamp = line.strip().split(',')
                    score = Score(username, game_id)
                    score.points = int(points)
                    score.wins = int(wins)
                    scores.append(score)
        return scores

    def save_score(self, score):
        if score.points > 0 or score.wins > 0: # this makes sure that it does not record lost games
             with open(self.scores_file, 'a') as file:
                  file.write(f'{score.username},{score.game_id},{score.points},{score.wins},{score.timestamp}\n')

    def play_game(self):
        game_id = str(uuid.uuid4())  # made use of uuid which provides unique game IDs for each game played
        self.user_score = Score(self.username, game_id)

        while True:
            print(f"\nStarting stage as {self.username}. . .")
            stage_points = 0
            self.cpu_score.points = 0

            while stage_points < 2 and self.cpu_score.points < 2:
                user_roll = random.randint(1, 6)
                cpu_roll = random.randint(1, 6)
                print(f'{self.username} rolled: {user_roll}')
                print(f'CPU rolled: {cpu_roll}')
                if user_roll > cpu_roll:
                    stage_points += 1
                    print(f"You win this round, {self.username}!\n")
                elif cpu_roll > user_roll:
                    self.cpu_score.add_points(1)
                    print('CPU wins this round!\n')
                else:
                    print('It\'s a tie!\n')

            if stage_points == 2:
                print(f'You won this stage, {self.username}!')
                self.user_score.add_points(stage_points + 3)  # since winning a stage grants 3 points, add 3 points if user wins
                self.user_score.add_win()
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                if choice != '1':
                    break
            else:
                print('Game over. You didn\'t win this stage.')
                break

        # game has ended, displaying total points and wins earned by user
        print(f'\nTotal Points: {self.user_score.points}')
        print(f'Total Wins: {self.user_score.wins}')
        self.save_score(self.user_score)
        input("Press ENTER to continue . . .")
        os.system("cls")

    def show_top_scores(self):
        scores = self.load_scores()
        # sorts the top 10 scores in descending order
        scores.sort(key=lambda s: (s.points, s.wins), reverse=True)
        print("Top 10 Scores:")
        for i, score in enumerate(scores[:10], start=1):
            print(f"{i}. {score.username} - Points: {score.points}, Wins: {score.wins}, Achieved on: {score.timestamp}")
        input("\nPress ENTER to continue . . .")
        os.system("cls")

    def logout(self):
        print("Logging out...")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")

    def menu(self):
        while True:
            os.system("cls")
            print(f"\nWelcome, {self.username}")
            print("\nMenu: ")
            print("\n1. Start Game")
            print("\n2. Show Top Scores")
            print("\n3. Log Out")

            choice = input("\nEnter your choice, or leave blank to cancel: ")

            if choice == '1':
                self.play_game()
            elif choice == '2':
                time.sleep(1)
                os.system("cls")
                self.show_top_scores()
            elif choice == '3':
                self.logout()
                break
            elif not choice:
                print("Cancelling input . . .")
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                print("Invalid input, please try again.")