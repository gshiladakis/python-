# This program creates an instance of the SavingsAccount
# class and an instance of the CD account.

import accounts

def main():
    # Get the account number, interest rate,
    # and account balance for a savings account.
    print('Enter the following data for a savings account.')
    acct_num = raw_input('Account number: ')
    int_rate = input('Interest rate: ')
    balance = input('Balance: ')

    # Create a SavingAccount object.
    savings = accounts. SavingsAccount(acct_num, int_rate, balance)

    # Get the account number, interest rate,
    # account balance, and maturity data for a CD.
    print('Enter the following data for a CD.')
    acct_num = raw_input('Account number: ')
    int_rate = input('Interest rate: ')
    balance = input('Balance: ')
    maturity = raw_input('Maturity date: ')

    # Create a SavingsAccount object.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Display the data entered.
    print('Here is the data you entered:')
    print
    print('Savings Account')
    print('---------------')
    print('Account number:', savings.get_account_num())
    print('Interest rate:', savings.get_interest_rate())
    print('Balance: $%.2f' % savings.get_balance())
    print
    print('CD')
    print('---------------')
    print('Account number:', cd.get_account_num())
    print('Interest rate:', cd.get_interest_rate())
    print('Balance: $%.2f' % cd.get_balance())
    print('Maturity date:', cd.get_maturity_date())

# Call the main function.
main()
