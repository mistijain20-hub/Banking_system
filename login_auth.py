import os
import pickle
import hashlib

def show_menu():
    print("press 1 for login as a user")
    print("press 2 for login as a admin")
    print("press 3 for Exit")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    

def user():
    while True:
        print("1. Login")
        print("2. Back")
        #os.system("cls")
        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
           user_login()

        elif user_choice ==2:
            break
        else:
            print("Pls enter valid number")


def user_login():
    user_name=input("Enter username: ")
    password= input("Enter password: ")

    password = hash_password(password)

    if not os.path.exists("users.pkl") or os.path.getsize("users.pkl") ==0:
        print("User Not found")
        return 

    with open('users.pkl','rb') as f:
        users = pickle.load(f)
    if user_name in users and users[user_name] == password:
        print("Login Successfully ✅")
    else:
        print("Invalid Username and password")
        


def admin():
    # user_name=input("Enter username: ")
    # password= input("Enter password: ")
    admin_show_menu()

def admin_show_menu():
    while True:
        print("1. Show All users")
        print("2. Create user")
        print("3. Update user")
        print("4. Delete user")
        print("5. Back")

        
        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
            show_all_user()
        
        elif user_choice == 2:
            create_user()

        elif user_choice ==3:
            update_user()

        elif user_choice ==4:
            delete_user()

        
        elif user_choice ==5:
            break

        else:
            print("Pls enter valid number")



def show_all_user():
    if os.path.exists("users.pkl"):
        with open("users.pkl",'rb') as f:
            users = pickle.load(f)
        
        print("\nAll users:")
        for username in users.keys():
            print(username)
    else:
        print("No user found ❌")


def update_user():
    while True:
        print("1. Change Password")
        print("2. Update Username")
        print("3. Update Balance")
        print("4. Back")

        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
           change_user_pass()

        elif user_choice ==2:
            update_username()
        
        elif user_choice ==3:
            update_balance()
        
        elif user_choice ==4:
            break

        else:
            print('Pls enter valid number')


def change_user_pass():
    show_all_user()
    if not os.path.exists("users.pkl"):
        print("User not found ❌")
        return
    with open("users.pkl",'rb')as f:
        users = pickle.load(f)
    username=input("Enter username: ")
    if username in users:
        password=input("Enter password: ")
        if users[username] == hash_password(password):
            new_pass = input("Enter new_pass: ")
            confirm_pass = input("Enter confirm_pass: ")
            if new_pass == confirm_pass:
                users[username] = hash_password(new_pass)
                with open("users.pkl",'wb')as f:
                    pickle.dump(users,f)
                    print("Password changed Successfully ✅")
            else:
                print("Password Mismatched")

        else:
            print("Password does not match ❌")

    else:
        print("User Not Found ❌")

def update_username():
    show_all_user()
    if not os.path.exists("users.pkl"):
        print("User not found ❌")
        return
    with open("users.pkl",'rb')as f:
        users = pickle.load(f)

    username = input("Enter username: ")
    if username in users:
        new_username = input("New_username: ")
        if new_username in users:
            print("Username already exist")
            return
        users[new_username] = users[username]
        del users[username]
        with open("users.pkl",'wb')as f:
            pickle.dump(users,f)
        print("Username Updated Successfully ✅")
    else:
        print("Username does not match ❌")


def update_balance():
    show_all_user()

def delete_user():
    show_all_user()
    username=input("Enter username: ")

    #if os.path.exists("users.pkl"):
    with open("users.pkl",'rb')as f:
        users = pickle.load(f)
    if username in users:
        del users[username]
        print("User deleted Successfully ✅")
    else:
        print("User Not found ❌")
    with open("users.pkl",'wb')as f:
        pickle.dump(users,f)




def create_user():
    user_name=input("Enter username: ")
    password= input("Enter password: ")
    confirm_password=input("Enter confirm_pass: ")

    if password != confirm_password:
        print("Password does not match ❌")
        return

    password = hash_password(password)
    if os.path.exists("users.pkl") and os.path.getsize("users.pkl") !=0:
        with open("users.pkl",'rb') as f:
            users = pickle.load(f)
    else: 
        users = {}
    
    if user_name in users:
        print("User already exist ❌")
        return
    users[user_name] = password

    with open("users.pkl",'wb') as f:
        pickle.dump(users,f)

    print("Account Created Successfully ✅\n",user_name)



def exit():
    print("Exit")
    


while True:
    show_menu()

    press=int(input("Enter number: "))
    os.system('cls')

    if press == 1:
       user()
    
    elif press == 2:
        admin()
    
    elif press == 3:
        exit()
        break
    
    else:
        print("Pls enter valid input")

        


