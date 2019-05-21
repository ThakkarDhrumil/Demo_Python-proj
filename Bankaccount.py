__author__ = 'Dhrumil'
class bankaccount:
    balance=0
    def create_account(self):
        name = input("Enter your name=")
        ia = int(input("Enter initial amount to open account="))
        self.balance=ia



    def deposit(self):
        cbalance=int(input("Enter add amount="))
        self.balance = self.balance+cbalance
        print(self.balance)


    def withdraw(self):
        wa=int(input("Enter amount to withdraw="))
        if(self.balance >wa+1000):
            self.balance=self.balance-wa

        else:
            print("You dont have enough balance")


    def view_balance(self):

        print("Your balance is " ,self.balance)


