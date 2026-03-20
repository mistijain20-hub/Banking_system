import os

def show_menu():
    print("press 1 for login as a user")
    print("press 2 for login as a admin")
    print("press 3 for Exit")
    

def user():
    while True:
        print("1. Login")
        print("2. Create Account")
        print("3. Back")

        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
           user_login()
           
        elif user_choice == 2:
            create_user()

        elif user_choice ==3:
            break
        else:
            print("Pls enter valid number")

def user_login():
    user_name=input("Enter username: ")
    password= input("Enter password: ")

def create_user():
    user_name=input("Enter username: ")
    password= input("Enter password: ")



            

def admin():
    user_name=input("Enter username: ")
    password= input("Enter password: ")

def exit():
    print("Exit")
    


while True:
    show_menu()

    press=int(input("Enter number: "))
    #print(os.system('cls'))

    if press == 1:
       user()
    
    elif press == 2:
        admin()
    
    elif press == 3:
        exit()
        break
    
    else:
        print("Pls enter valid input")

        


