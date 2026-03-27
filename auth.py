import hashlib
import database
import art
from utils import clear_screen
import banking

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_pw = hash_password(password)

    users = database.load_users()
    if username in users and users[username][0] == hashed_pw:
        print(f"Login Successful! Welcome, {username} ✅")
        balance = users[username][1]
        banking.banking_session(username, balance)
    else:
        print("Invalid username or password ❌")

def admin_session():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Show All Users")
        print("2. Create User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back")
        
        choice = input("Enter choice: ")
        clear_screen()

        if choice == '1':
            show_all_users()
        elif choice == '2':
            create_user()
        elif choice == '3':
            update_user_menu()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def show_all_users():
    users = database.load_users()
    if not users:
        print("No users found.")
    else:
        print("\nList of Users:")
        for username, data in users.items():
            print(f"- {username} (Balance: ₹{data[1]})")

def create_user():
    username = input("Enter new username: ")
    password = input("Enter password: ")
    confirm_pw = input("Confirm password: ")

    if password != confirm_pw:
        print("Passwords do not match!")
        return

    users = database.load_users()
    if username in users:
        print("Username already exists!")
        return

    users[username] = [hash_password(password), 0]
    database.save_users(users)
    print(f"User '{username}' created successfully! ✅")

def update_user_menu():
    users = database.load_users()
    username = input("Enter username to update: ")
    if username not in users:
        print("User not found.")
        return

    print("1. Change Password")
    print("2. Change Username")
    print("3. Update Balance")
    choice = input("Enter choice: ")

    if choice == '1':
        new_pw = input("Enter new password: ")
        users[username][0] = hash_password(new_pw)
    elif choice == '2':
        new_username = input("Enter new username: ")
        if new_username in users:
            print("Username already exists.")
            return
        users[new_username] = users.pop(username)
    elif choice == '3':
        try:
            new_balance = int(input("Enter new balance: "))
            users[username][1] = new_balance
        except ValueError:
            print("Invalid balance.")
            return
    
    database.save_users(users)
    print("User updated successfully!")

def delete_user():
    users = database.load_users()
    username = input("Enter username to delete: ")
    if username in users:
        del users[username]
        database.save_users(users)
        print("User deleted successfully.")
    else:
        print("User not found.")
