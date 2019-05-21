__author__ = 'Dhrumil'
__author__ = 'Dhrumil'
from inharitance.Saving_ac import Saving_ac
from inharitance.Curent_ac import Current_ac
sa=Saving_ac()
ca=Current_ac()

class Bank_account():
    ac_type=0
    users={}
    def menu(self):
        print("\n\n1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        op=int(input("Enter your choice"))
        return op


    def openAccount(self):
        while 1:
            acNo=int(input("Enter your account number: "))
            if acNo in self.users.keys():
                print("Account number already chosen!!!\nPlease choose another.")
            else:
                break
        name=input("Enter you name: ")
        print("Enter Select type 1)Saving 2)Current")
        atype=input("account Type =")
        ibal=int(input("Enter you initial balance: "))

        d={}
        d['name']=name
        d['balance']=ibal
        d['ac_type']=atype
        self.users[acNo]=d

    def getbalance(self,acNo):
        bal = self.users[acNo]['balance']
        return bal

    def getactype(self,acNo):
        ac_type=self.users[acNo]['ac_type']
        return ac_type

    def deposit(self):
        acNo = int(input("Enter your account number: "))
        if acNo not in self.users.keys():
            print("No such account exist!!!")
            return
        else:
            amnt=int(input("Enter your amount: "))
            bal=self.getbalance(acNo)
            bal=bal+amnt
            self.users[acNo]['balance']=bal
            print("Successfully deposited!!!")

    def withdraw(self):
        acNo = int(input("Enter your account number: "))
        if acNo not in self.users.keys():
            print("No such account exist!!!")
            return
        else:
            amnt = int(input("Enter your amount: "))
            bal = self.getbalance(acNo)
            if bal-5000 < amnt:
                print("Not enough balance!!!")
            else:
                bal=bal-amnt
                print("Successfully withdrawn!!!")
            self.users[acNo]['balance'] = bal



    def viewBalance(self):

        acNo = int(input("Enter your account number: "))

        if acNo not in self.users.keys():
            print("No such account exist!!!")
            return
        else:

            bal = self.getbalance(acNo)
            if(self.ac_type == 2):
                ca.viewBalance(bal)
            else:
                sa.viewBalance(bal)





__author__ = 'Dhrumil'
class Saving_ac():

    def viewBalance(self,bal):

        nbal=(bal*4)/100+bal
        print("Balance :",nbal)



__author__ = 'Dhrumil'
class Current_ac():

    def viewBalance(self,bal):
         print("Balance :",bal)




__author__ = 'Dhrumil'

from inharitance.Saving_ac import Saving_ac
from inharitance.Curent_ac import Current_ac
sa=Saving_ac()
ca=Current_ac()
from inharitance.Parrent_class import Bank_account
ba=Bank_account()

while 1:
    op=ba.menu()
    if op==1:
        ba.openAccount()
    elif op==2:
        ba.deposit()
    elif op==3:
        ba.withdraw()
    elif op==4:

        ba.viewBalance()
    elif op==5:
        print("Thank you!!!!")
        print(ba.users)
        break
    else:
        print("Enter a valid option!!!")


