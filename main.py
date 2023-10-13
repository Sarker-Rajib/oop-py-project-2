from Bank import *
from admin import *
from accounts import *

def main():
    ac1 = Account('myself', 'email', 'address', 'Savings')
    ac2 = Account('you', 'email', 'address', 'Current')


    ac1.deposit_money(100)
    # ac1.withdraw_money(1)
    # # ac1.check_balance()
    ac1.get_loan(2000)
    # # print(ac1.loan_amount, ac1.loan_count)
    # # ac1.get_loan(2000)
    # # print(ac1.loan_amount, ac1.loan_count)
    # # ac1.get_loan(2000)
    # # print(ac1.loan_amount, ac1.loan_count)

    # # ac2.check_balance()
    # ac1.transfer_money(87, 'CA102')
    # # ac1.check_balance()
    for th in ac1.transaction_history:
        print(th)
    # ac2.check_balance()

    admin = Admin('s','a','ss','Savings')
    # admin.delete_an_account('CA102')
    # admin.view_users()
    admin.view_total_loan()
    admin.view_balance()


if __name__ == '__main__':
    main()