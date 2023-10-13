from Bank import *
from admin import *
from accounts import *

def main():
    ac1 = Account('Asif Akbar', 'asif09@email.com', 'Chattogram', 'Savings')
    ac2 = Account('Antik', 'antu@email.com', 'Rajshahi', 'Current')
    ac3 = Account('Apsara', 'apsara24@email.com', 'Dhaka', 'Savings')
    admin = Admin('Admin')


    while(True):
        print('Please select an option Below')
        print('1. Create an Account')
        print('2. Login to your account')
        print('3. Login as Admin')
        print('4. Exit')

        x = int(input('Give your input : '))
        if 1 > x > 3:
            print('Invalid Input')
        elif x == 1:
            name = input('Input Account Name : ')
            email = input('Input email : ')
            address = input('Input Address : ')
            print('Input account type (1-savings/ 2-Current)')
            option = int(input('Input 1 or 2 : '))
            account_type = 'Savings'
            if option == 2:
                account_type = 'Current'
            newac = Account(name, email, address, account_type)
            print(newac.account_no)
            print('---------------\n')
            continue
        elif x == 2:
            print('Please Provide Your account No.')
            ac_no = input('Your account No : ')
            if ac_no in Bank.accounts:
                user = Bank.accounts[ac_no]
                while(True):
                    print('Please select an option Below')
                    print('1. Deposit Money')
                    print('2. Withdraw Money')
                    print('3. Check Balance')
                    print('4. View Transaction History')
                    print('5. Take a Loan')
                    print('6. Transfer Money')
                    print('7. Log-out')
                    print('-----###-----')
                    Z = int(input('Provide your input : '))

                    if Z == 1:
                        money = int(input('Place amount : '))
                        user.deposit_money(money)
                    elif Z == 2:
                        amount = int(input('Place amount : '))
                        user.withdraw_money(amount)
                        print('---------------')
                    elif Z == 3:
                        user.check_balance()
                        print('---------------')
                    elif Z == 4:
                        user.get_transaction_history()
                        print('---------------')
                    elif Z == 5:
                        amunt = int(input('Place loan amount : '))
                        user.get_loan(amunt)
                        print('---------------')
                    elif Z == 6:
                        acc_no = input('Input account no : ')
                        amoun = int(input('Place transfer amount : '))
                        user.transfer_money(amoun, acc_no)
                        print('---------------')
                    elif Z == 7:
                        break
            else:
                print('Wrong Account Number Inserted')
                break

        elif x == 3:
            print()
            passcode = int(input('Enter Your password : '))
            if admin.password == passcode:
                while(True):
                    print('Please select an option Below')
                    print('1. Create an Account')
                    print('2. Delete an account')
                    print('3. See user Lists')
                    print('4. View balance')
                    print('5. View Loan given')
                    print('6. Turn of Loan produre')
                    print('7. Log-out')

                    Y = int(input('Provide your input : '))

                    if Y == 1:
                        name = input('Input Account Name : ')
                        email = input('Input email : ')
                        address = input('Input Address : ')
                        print('Input account type (1-savings/ 2-Current)')
                        option = int(input('Input 1 or 2 : '))
                        account_type = 'Savings'
                        if option == 2:
                            account_type = 'Current'
                        Account(name, email, address, account_type)
                        print('---------------')
                        continue
                    elif Y == 2:
                        inp = input('Please input the account no that you want to delete : ')
                        admin.delete_an_account(inp)
                        print('---------------')
                    elif Y == 3:
                        print('Users : ')
                        admin.view_users()
                        print('---------------')
                    elif Y == 4:
                        admin.view_balance()
                        print('---------------')
                    elif Y == 5:
                        admin.view_total_loan()
                        print('---------------')
                    elif Y == 6:
                        admin.turn_off_loan_process()
                        print('---------------')
                    elif Y == 7:
                        break
            else:
                print('Wrong Paassword')
                continue

        elif x == 4:
            break

if __name__ == '__main__':
    main()