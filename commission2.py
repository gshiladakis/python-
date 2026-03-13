# This program calculates sales commissions.
def main():
    # Create a variable to control the loop.
    keep_going = 'y'

    # Calculate a series of commissions
    while keep_going == 'y':
        # Call the show_commissionfunction to 
        # display a salesperson's commission
        show_commission()

        # See if the user wants to do another one.
        keep_going = raw_input('Do you want to calculate another ' + \
                               'commission (Enter y for yes): ')

# The show_commissionfunction gets the amount of 
# sales and the commission rate, and then displays
# the amount of commission.
def show_commission():
    # Get a salesperson's sales and commission rate.
    sales = input('Enter the commission sales: ')
    comm_rate = input('Enter the commission rate: ')

    # Calcualte the commission.
    commission = sales * comm_rate

    # Display the commission.
    print('The commission is $%.2f.' % commission

# Call the main function.
main() 
