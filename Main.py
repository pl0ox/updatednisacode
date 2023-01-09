import json
import getpass
import sys

# Load users from JSON file
with open("users.json", "r") as f:
    users = json.load(f)

def main_menu():
    print("Welcome to the main menu! Please choose an option:")
    print("1. Access database")
    print("2. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Access database
        pass
    elif choice == "2":
        logout()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def register():
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")
    # add new usr to database
    users[username] = password
    # save updated to json
    with open("users.json", "w") as f:
        json.dump(users, f)
    print("Thank you for registering! You can now login.")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in users and users[username] == password:
        main_menu()
    else:
        print("Invalid username or password. Please try again.")
        login()

def logout():
    print("You have been logged out. Goodbye!")
    sys.exit()

if __name__ == "__main__":
    print("Welcome! Please choose an option:")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid choice. Please try again.")