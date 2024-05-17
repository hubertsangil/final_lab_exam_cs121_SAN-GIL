from utils.user import User
import os
import time


class UserManager:
    def __init__(self):
        self.folder_path = 'data_folder'
        self.file = 'users.txt'
        self.file_path = os.path.join(self.folder_path, self.file)
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    if line.strip(): 
                        username, password = line.strip().split(',')
                        self.users[username] = password
        except Exception as e:
            print(f"Error loading users: {e}")

    def save_users(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        
        with open(self.file_path, 'w') as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        return username in self.users

    def validate_password(self, username, password):
        stored_password = self.users.get(username)
        return stored_password == password
    
    def register(self, username, password):
        if username not in self.users:
            user = User(username, password)
            self.users[username] = password
            self.save_users()
            print("Registration successful.")
            time.sleep(1)
            os.system("cls")
        else:
            print("Registration failed. Username already exists.")
    
    def login(self, username, password):
        if self.validate_password(username, password):
            print("Login successful.")
        else:
            print("Login unsuccessful. Invalid username or password.")
