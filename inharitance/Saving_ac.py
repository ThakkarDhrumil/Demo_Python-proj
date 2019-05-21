__author__ = 'Dhrumil'
from inharitance.Parrent_class import Bank_account

class Saving_ac(Bank_account):
    def viewBalance(self, bal):
        nbal = (bal * 4) / 100 + bal
        print("Balance :", nbal)

