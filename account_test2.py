# This program demonstrates the BankAccount class
# with the __str__ method added to it.

import account2

def main():
    # Get the starting balance.
    start_bal = input('Enter your starting balance: ')

    # Create a BankAccount object.
    savings = account2.BankAccount(start_bal)

    # Deposit the user's paycheck.
    pay = input('How much were you paid this week? ')
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # Display the balance.
    print(savings)

    # Get the amount to withdraw.
    cash = input('How much would you like to withdraw? ')
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    # Display the balance.
    print(savings) 

# Call the main function.
main() 
