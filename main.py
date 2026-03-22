import art
import os
from datetime import datetime
balance = 2500000

print(art.welcome)

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
    now=datetime.now()
    formatted_time=now.strftime("%d-%m-%h %I:%M %p")
    with open("trans_hist.txt",'a',encoding="utf-8") as file:
        file.write(f"{formatted_time} | {'Credit':<6} | ₹{amount:<8} | deposited\n")
    

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
    now=datetime.now()
    formatted_time=now.strftime("%d-%m-%h %I:%M %p")
    with open("trans_hist.txt",'a',encoding="utf-8") as file:
        file.write(f"{formatted_time} | {'Debit':<6} | ₹{amount:<8} | Withdrawn\n")
    


def show_passbook():
    get_money()
    with open("trans_hist.txt",'r',encoding="utf-8") as file:
        last = (file.readlines())
        last_n = last[-10:]
        for i in last_n:
            print(i,end="")
       
        
def exit():
    print("Thanks for visiting our bank")
    print(art.exit)

while True:
   
    show_menu()
    press=int(input("Enter a number: "))
    os.system('cls')

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

