import auth
import art
from utils import clear_screen

def show_main_menu():
    print(art.welcome)
    print("\n1. Login as User")
    print("2. Login as Admin")
    print("3. Exit")

def main():
    while True:
        show_main_menu()
        choice = input("Enter choice: ")
        clear_screen()

        if choice == '1':
            auth.user_login()
        elif choice == '2':
            auth.admin_session()
        elif choice == '3':
            print("Thanks for visiting our bank!")
            print(art.exit)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
