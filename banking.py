import database
import art
from utils import clear_screen

def show_banking_menu():
    print("\n--- Banking Menu ---")
    print("1. Check Balance")    
    print("2. Deposit Money")    
    print("3. Withdraw Money")    
    print("4. Show Passbook")    
    print("5. Logout")

def deposit_money(username, current_balance):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            new_balance = current_balance + amount
            database.log_transaction(username, "Credit", amount, "Deposited")
            
            # Update database
            users = database.load_users()
            users[username][1] = new_balance
            database.save_users(users)
            
            print(f"Amount deposited successfully! New balance: ₹{new_balance}")
            return new_balance
        else:
            print("Please enter a valid positive amount.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return current_balance

def withdraw_money(username, current_balance):
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Please enter a valid positive amount.")
        elif amount > current_balance:
            print("Insufficient balance.")
        else:
            new_balance = current_balance - amount
            database.log_transaction(username, "Debit", amount, "Withdrawn")
            
            # Update database
            users = database.load_users()
            users[username][1] = new_balance
            database.save_users(users)
            
            print(f"Amount withdrawn successfully! New balance: ₹{new_balance}")
            return new_balance
    except ValueError:
        print("Invalid input. Please enter a number.")
    return current_balance

def show_passbook(username):
    print(f"\n--- Passbook for {username} (Last 10 Transactions) ---")
    history = database.get_transaction_history(username)
    if not history:
        print("No transactions found.")
    else:
        for entry in reversed(history):
            print(entry)

def banking_session(username, balance):
    while True:
        show_banking_menu()
        choice = input("Enter choice: ")
        clear_screen()
        
        if choice == '1':
            print(f"Current Balance: ₹{balance}")
        elif choice == '2':
            balance = deposit_money(username, balance)
        elif choice == '3':
            balance = withdraw_money(username, balance)
        elif choice == '4':
            show_passbook(username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
