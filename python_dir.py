__author__ = 'Dhrumil'
users={}
def menu():
    print("\n\n1. Open Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Balance")
    print("5. Exit")
    op=int(input("Enter your choice"))
    return op

def openAccount():
    while 1:
        acNo=int(input("Enter your account number: "))
        if acNo in users.keys():
            print("Account number already chosen!!!\nPlease choose another.")
        else:
            break
    name=input("Enter you name: ")
    ibal=int(input("Enter you initial balance: "))
    d={}
    d['name']=name
    d['balance']=ibal
    users[acNo]=d

def getbalance(acNo):
    bal = users[acNo]['balance']
    return bal

def deposit():
    acNo = int(input("Enter your account number: "))
    if acNo not in users.keys():
        print("No such account exist!!!")
        return
    else:
        amnt=int(input("Enter your amount: "))
        bal=getbalance(acNo)
        bal=bal+amnt
        users[acNo]['balance']=bal
        print("Successfully deposited!!!")

def withdraw():
    acNo = int(input("Enter your account number: "))
    if acNo not in users.keys():
        print("No such account exist!!!")
        return
    else:
        amnt = int(input("Enter your amount: "))
        bal = getbalance(acNo)
        if bal-5000 < amnt:
            print("Not enough balance!!!")
        else:
            bal=bal-amnt
            print("Successfully withdrawn!!!")
        users[acNo]['balance'] = bal


def viewBalance():
    acNo = int(input("Enter your account number: "))
    if acNo not in users.keys():
        print("No such account exist!!!")
        return
    else:
        bal = getbalance(acNo)
        print("Balance :",bal)

while 1:
    op=menu()
    if op==1:
        openAccount()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        viewBalance()
    elif op==5:
        print("Thank you!!!!")
        print(users)
        break
    else:
        print("Enter a valid option!!!")



