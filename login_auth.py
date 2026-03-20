import os

def show_menu():
    print("press 1 for login as a user")
    print("press 2 for login as a admin")
    print("press 3 for Exit")
    

def create_user():
    if press == 11:
        print("Login into account")
    elif press ==12:
        print("Create Account")
        user_name=input("Enter username: ")
        password= input("Enter password: ")
    else:
        print("Pls enter valid number")
        

def create_admin():
    user_name=input("Enter username: ")
    password= input("Enter password: ")

def exit():
    print("Exit")
    


while True:
    show_menu()

    press=int(input("Enter number: "))
    print(os.system('cls'))

    if press == 1:
       create_user()
    
    elif press == 2:
        create_admin()
    
    elif press == 3:
        exit()
        break
    
    else:
        print("Pls enter valid input")

        


