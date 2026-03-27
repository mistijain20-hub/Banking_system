import pickle
import os
from utils import get_formatted_time

USERS_FILE = "users.pkl"
TRANS_FILE = "trans_hist.txt"

def load_users():
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        return {}
    try:
        with open(USERS_FILE, 'rb') as f:
            return pickle.load(f)
    except (EOFError, pickle.UnpicklingError):
        return {}

def save_users(users):
    with open(USERS_FILE, 'wb') as f:
        pickle.dump(users, f)

def log_transaction(username, action, amount, status):
    timestamp = get_formatted_time()
    with open(TRANS_FILE, 'a', encoding="utf-8") as f:
        f.write(f"{timestamp} | {username:<10} | {action:<8} | ₹{amount:<8} | {status}\n")

def get_transaction_history(username, limit=10):
    if not os.path.exists(TRANS_FILE):
        return []
    
    user_history = []
    with open(TRANS_FILE, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # Find transactions for this specific user
        for line in reversed(lines):
            if f"| {username:<10} |" in line:
                user_history.append(line.strip())
                if len(user_history) >= limit:
                    break
    return user_history
