from Bank import *
from accounts import *

class Admin(Account):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)
        self.admin = True
    
    def delete_an_account(self, account_no):
        if account_no in Bank.accounts:
            del Bank.accounts[account_no]
    
    def view_users(self):
        for user in Bank.accounts:
           user = Bank.accounts[user]
           print(f'Account No : {user.account_no}, Name : {user.name}, Email : {user.email}, Address : {user.address}, Account Type : {user.account_type}')
    
    def view_balance(self):
        print(Bank.available_balence)
    
    def view_total_loan(self):
        print(Bank.loan_amount)
    
    def turn_off_loan_process(self):
        Bank.giving_loan = False

    def turn_on_loan_process(self):
        Bank.giving_loan = True