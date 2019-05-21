__author__ = 'Dhrumil'


from inharitance.Saving_ac import Saving_ac
from inharitance.Curent_ac import Current_ac

ca=Current_ac()


type=int(input("enter 1 for saving acc and  2 current acc"))

if(type==1):
    sa=Saving_ac()
    ch=0

    while 1:

        print("\n\n1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        op=int(input("Enter your choice"))



        if op==1:
            bal=sa.openAccount()
        elif op==2:
            sa.deposit()
        elif op==3:
            sa.withdraw()
        elif op==4:

            sa.viewBalance(bal)
        elif op==5:
            print("Thank you!!!!")
            print(sa.users)
            break
        else:
            print("Enter a valid option!!!")


if(type==2):
    ca=Current_ac()

    ch=0
    while 1:

            print("\n\n1. Open Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Balance")
            print("5. Exit")
            op=int(input("Enter your choice"))

            if op==1:
                bal=ca.openAccount()
            elif op==2:
                ca.deposit()
            elif op==3:
                ca.withdraw()
            elif op==4:

                ca.viewBalance(bal)
            elif op==5:
                print("Thank you!!!!")
                print(ca.users)
                break
            else:
                print("Enter a valid option!!!")


