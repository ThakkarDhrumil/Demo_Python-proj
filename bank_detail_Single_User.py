__author__ = 'Dhrumil'

anumber = 15040010
account = []
cousomer = []
global balance
d={}
ch=0

def create_account(anumber):
    name = input("Enter your name=")
    ia = int(input("Enter initial amount to open account="))
    print("Your account number")
    balance=ia
    anumber= anumber +1
    d[anumber]=balance
    print(d)
    return balance

def deposit(balance,anumber):

    cbalance=int(input("Enter add amount="))
    balance=balance+cbalance
    print(balance)
    return balance


def withdraw(balance,wa):

    if(balance >wa+1000):
        balance=balance-wa
        return balance

    else:
        print("You dont have enough balance")


def view_balance(balance):

    print("Your balance is " ,balance)



balance=create_account(anumber)
while(1):
   # print("1)create account")
    print("1)Deposit")
    print("2)withdraw")
    print("3)view Balance")
    print("4)Exit")
    ch =input("Select choice=")


    if(ch=='1'):
        balance = deposit( balance ,anumber)
        #bank()
        view_balance(balance)

    elif(ch=='2'):
        wa=int(input("Enter amount to withdraw="))
        balance=withdraw(balance,wa)
        #bank()
        view_balance(balance)

    elif(ch=='3'):

        view_balance(balance)
        #bank()

    else:
        print(" Thanks for using System ")
        exit()



