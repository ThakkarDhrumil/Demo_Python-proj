__author__ = 'Dhrumil'

from Bankaccount import bankaccount

ba= bankaccount()
balance=ba.create_account()
while(1):

    print("1)Deposit")
    print("2)withdraw")
    print("3)view Balance")
    print("4)Exit")
    ch =input("Select choice=")


    if(ch=='1'):
        balance =ba.deposit(  )
        ba.view_balance()

    elif(ch=='2'):

        balance=ba.withdraw()
        ba.view_balance()

    elif(ch=='3'):

        ba.view_balance()


    else:
        print(" Thanks for usisng System ")
        exit()



