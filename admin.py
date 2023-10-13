from Bank import *
from accounts import *

class Admin():
    def __init__(self, name) -> None:
        self.name = name
        self.role = 'Admin'
        self.password = 123

    def create_an_account(self, name, email, address, account_type):
        Account(name, email, address, account_type)
    
    def delete_an_account(self, account_no):
        if account_no in Bank.accounts:
            del Bank.accounts[account_no]
            print('Acoount deleted')
        else:
            print('Account no not exist')
    
    def view_users(self):
        for user in Bank.accounts:
           user = Bank.accounts[user]
           print(f'Account No : {user.account_no}, Name : {user.name}, Email : {user.email}, Address : {user.address}, Account Type : {user.account_type}')
    
    def view_balance(self):
        print(f'Total balance of the bank is : {Bank.available_balence}$')
    
    def view_total_loan(self):
        print(f'Total Loan amount given from the bank is : {Bank.loan_amount}$')
    
    def turn_off_loan_process(self):
        Bank.giving_loan = False

    def turn_on_loan_process(self):
        Bank.giving_loan = True