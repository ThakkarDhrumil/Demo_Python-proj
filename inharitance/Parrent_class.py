__author__ = 'Dhrumil'

class Bank_account():
    ac_type=0
    users={}

    def openAccount(self):
        while 1:
            acNo=int(input("Enter your account number: "))
            if acNo in self.users.keys():
                print("Account number already chosen!!!\nPlease choose another.")
            else:
                break
        name=input("Enter you name: ")
        ibal=int(input("Enter you initial balance: "))

        d={}
        d['name']=name
        d['balance']=ibal
        self.users[acNo]=d
        return ibal


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




