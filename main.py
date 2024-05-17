from utils.user_manager import UserManager
from utils.dice_game import DiceGame
import os
import time

def main():
    user_manager = UserManager()
    user_manager.load_users()

    while True:
        print("\nWelcome to Dice Roll Game!")
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            register_user(user_manager)
        elif choice == '2':
            username = login_user(user_manager)
            if username:
                time.sleep(1)
                os.system("cls")
                game = DiceGame(username)
                game.menu()
        elif choice == '3':
            print("Exiting program . . .")
            time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif not choice:
            print("Cancelling input . . .")
            time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Invalid input, please try again.")

def register_user(user_manager):
    username = input("Enter username (at least 4 characters long): ")
    if not username:
        print("Cancelling input . . .")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return
    if len(username) < 4:
        print("Username must be at least 4 characters long.")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return
    password = input("Enter password (at least 8 characters long): ")
    if not password:
        print("Cancelling input . . .")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return

    user_manager.register(username, password)

def login_user(user_manager):
    username = input("Enter username: ")
    if not username:
        print("Cancelling input . . .")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return None
    if not user_manager.validate_username(username):
        print("Username does not exist.")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return None

    password = input("Enter password: ")
    if not password:
        print("Cancelling input . . .")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return None
    if user_manager.validate_password(username, password):
        print("Login successful.")
        return username
    else:
        print("Incorrect password, please try again.")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        return None

if __name__ == "__main__":
    main()
