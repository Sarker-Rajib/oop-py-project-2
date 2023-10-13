import datetime
from Bank import *

class Account:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 2
        self.loan_amount = 0

        if account_type == 'Savings':
            x = len(Bank.accounts) + 1
            self.account_no = 'SA10' + str(x)
        else:
            x = len(Bank.accounts) + 1
            self.account_no = 'CA10' + str(x)

        Bank.accounts[self.account_no] = self
    
    # deposit money
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            Bank.available_balence += amount
            self.transaction_history.append(f'Deposit => Amount : {amount}, Date/Time : {datetime.datetime.now()}')
            print(f'Deposit of amount : {amount}$ succesfully done. Your current balance is : {self.balance}$')
        else:
            print('You Provided an Invalid amount')

    # withdraw money
    def withdraw_money(self, amount):
        if not Bank.isBankrupt:
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f'Withdraw => Amount : {amount}, Date/Time : {datetime.datetime.now()}')
                print(f'Withdraw of amount : {amount}$ succesfully done. Your current balance is : {self.balance}$')
            else:
                print('Withdrawal amount exceeded')
        else:
            print('Bank is bankrupt')
    
    # check balance
    def check_balance(self):
        print(f'Your (ac_no : {self.accont_no}) current balance is : {self.balance}$')

    # take loan
    def get_loan(self, amount):
        if self.loan_count == 0:
            print('Sorry ! You have already taken loan for 2 times')
        else:
            self.loan_amount += amount
            self.loan_count -= 1
            Bank.loan_amount += amount
            Bank.available_balence -= amount

    # transfer money
    def transfer_money(self, amount, account_no):
        if account_no in Bank.accounts:
            if 0 < amount <= self.balance:
                Bank.accounts[account_no].balance += amount
                self.balance -= amount
                print(f'After Transfer of {amount}$, Your balance is {self.balance}$')
                self.transaction_history.append(f'Transfer => Amount : {amount}, To Account : {account_no} , Date/Time : {datetime.datetime.now()}')
            else:
                print('The amount You entered is incorrect')
        else:
            print('Account not found')
