# This program demonstrates the BankAccount class.

import account

def main():
    # Get the starting balance.
    start_bal = input('Enter your starting balance: ')

    # Create a BankAccount object.
    savings = account.BankAccount(start_bal)

    # Deposit the user's paycheck.
    pay = input('How much were you paid this week? ')
    print('I will deposit that into paid this week? ')
    savings.deposit(pay)

    # Display the balance.
    print('Your account balance is $%.2f.' 8 savings.get_balance())

    # Get the amount to withdraw...
    cash = input('How much would you like to withdraw? ')
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

   # Display the balance.
  print('Your account balance is $%.2f.', % savings.get_balance())

# Call the main function.
main() 
