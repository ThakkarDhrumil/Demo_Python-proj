__author__ = 'Dhrumil'
__author__ = 'Dhrumil'

anumber = 15040010
account = []
cousomer = []
balance=0
d={}

def create_account(anumber):
    name = input("Enter your name=")
    ia = int(input("Enter initial amount to open account="))
    print("Your account number")
    balance=ia
    anumber= anumber +1
    d[anumber]=balance
    print(d)
    return balance

def deposit( balance ,anumber):

    cbalance=input("Enter add amount=")
    balance=balance+cbalance
    return balance


def withdraw(bal,wa):

    if(bal>wa):
        bal=bal-wa
        return bal

    else:
        print("You dont have enough balance")


def view_balance(balance):
    print("Your balance is " ,balance)



def bank():
    print("1)create account")
    print("2)Deposit")
    print("3)withdraw")
    print("4)view Balance")
    print("5)Exit")
    ch =input("Select choice=")

    if (ch=='1'):
        balance=create_account(anumber)
        bank()

    elif(ch=='2'):
        unumber=input("Enter account number=")
        if(anumber=='unumber'):
            balance = deposit( balance ,anumber)
            bank()
            view_balance(balance)
        else:
            print("please enter right account number")

    elif(ch=='3'):
        unumber=int(input("Enter account number="))
        if(anumber==unumber):
            wa=int(input("Enter amount to withdraw="))
            balance=withdraw(balance,wa)
            bank()
            view_balance(balance)
        else:
            print("please enter right account number")


    elif(ch=='4'):
        unumber=int(input("Enter account number="))
        if(anumber==unumber):
            view_balance(balance)
            bank()
        else:
            print("please enter right account number")


    else:
        print(" Thanks for using System ")
        exit()

bank()

