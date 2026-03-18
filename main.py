
balance = 2500000

def show_menu():
    print("Enter 1 for check the balance")    
    print("Enter 2 for deposite the money")    
    print("Enter 3 for withdraw the money")    
    print("Enter 4 for show the passbook")    
    print("Enter 5 for Exit")    

def get_money():
    global balance
    print(f"Current balance : {balance}")

def deposite_money():
    global balance
    get_money()
    amount=int(input("Enter amount: "))
    if amount>0:
        balance+=amount
        print("Amount deposited\nCurrent_balance:",balance)

    else:
        print("Pls enter valid amount")
        return
    # with open("trans_hist.txt",'a') as file:
    #     file.writelines('')
    



def withdraw_money():
    global balance
    amount=int(input("Enter amount: "))
    if amount>0 and amount<balance:
        balance-=amount
        print("Amount deposited\nCurrent_balance:",balance)
    elif amount>balance:
        print("Insufficient balance")
        return
    else:
        print("Pls enter valid amount")
        return
    # with open("trans_hist.txt",'a') as file:
    #     file.write('st')
    


def show_passbook():
    get_money()
    # with open("trans_hist.txt",'r') as file:
    #     print(file.readlines())


def exit():
    print("Thanks for visiting our bank")





while True:
    show_menu()

    press=int(input("Enter a number: "))

    if press ==1:
        get_money()

    elif press==2:
        deposite_money()

    elif press==3:
        withdraw_money()

    elif press==4:
        show_passbook()

    elif press==5:
        exit()
        break

    else:
        print("Pls enter Valid number")

